"""agent7.py — Session 7 agent orchestrator.

The loop layout is unchanged from Session 6. The only thing that changed
underneath is the Memory service: writes now compute an embedding via the
gateway's V7 embed endpoint and append to a FAISS index; reads use vector
similarity first and fall back to keyword search when the vector path is
empty. Two new MCP tools, index_document and search_knowledge, surface
the same machinery to the model so the agent can ingest external
documents on demand.

The four typed layers:

    memory.read -> perception.observe -> decision.next_step ->
    action.execute -> memory.record_outcome

Perception is the only layer that maintains goal state across iterations.
Memory is a typed service (read / write). The artifact store carries raw
bytes; Decision sees them only when Perception attached them to the
current goal.

Run from this folder:
    uv run agent7.py "What is the current time in Tokyo and Bangalore?"
"""

from __future__ import annotations

import asyncio
import json
import sys
import time
import uuid
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import action
import artifacts
import decision
import memory
import perception
from gateway import ensure_gateway
from schemas import Goal

MCP_SERVER = Path(__file__).parent / "mcp_server.py"
MAX_ITERATIONS = 20

# Tools that reach the public internet. `--no-web` withholds these from the list
# Decision sees, so an "answer only from the knowledge base" run cannot quietly
# fall back to the web when search_knowledge comes up empty. A prompt asking the
# model not to browse is a request; removing the tool is the actual rule.
WEB_TOOLS = frozenset({"web_search", "fetch_url"})


def _mcp_tools_for_decision(tools, blocked: frozenset = frozenset()) -> list[dict]:
    """Convert MCP tool descriptors into the shape the gateway expects.

    Anything named in `blocked` is omitted entirely — Decision never learns the
    tool exists, which is what makes the restriction real rather than advisory.
    """
    return [
        {
            "name": t.name,
            "description": t.description or "",
            "input_schema": t.inputSchema or {"type": "object", "properties": {}},
        }
        for t in tools
        if t.name not in blocked
    ]


async def run(query: str, no_web: bool = False) -> str:
    ensure_gateway()
    run_id = uuid.uuid4().hex[:8]
    print(f"\n{'═' * 78}")
    print(f"run {run_id}  ─  query: {query}")
    print(f"{'═' * 78}")

    # Durable memory: classify the user's query so facts/preferences in it
    # survive into future runs. Tool outcomes get recorded later by Action;
    # the query itself only gets a memory record if we put it there now.
    try:
        memory.remember(query, source="user_query", run_id=run_id)
    except Exception as e:
        print(f"[memory.remember] skipped: {e}")

    server_params = StdioServerParameters(command=sys.executable, args=[str(MCP_SERVER)])
    history: list[dict] = []
    prior_goals: list[Goal] = []
    final_answer: str = ""

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            mcp_tools = (await session.list_tools()).tools
            blocked = WEB_TOOLS if no_web else frozenset()
            tools_for_decision = _mcp_tools_for_decision(mcp_tools, blocked)
            print(f"[mcp] loaded {len(mcp_tools)} tools: {[t.name for t in mcp_tools]}")
            if blocked:
                print(f"[mcp] --no-web ON: withheld {sorted(blocked)} — "
                      f"Decision sees {len(tools_for_decision)} tools")

            for it in range(1, MAX_ITERATIONS + 1):
                if it > 1:
                    time.sleep(12)
                print(f"\n─── iter {it} ─────────────────────────────────────────────")

                # 1. MEMORY READ
                hits = memory.read(query, history)
                print(f"[memory.read]   {len(hits)} hits")

                # 2. PERCEPTION
                obs = perception.observe(query, hits, history, prior_goals, run_id)
                prior_goals = obs.goals
                for g in obs.goals:
                    flag = "✓" if g.done else "○"
                    attach = f"  attach={g.attach_artifact_id}" if g.attach_artifact_id else ""
                    print(f"[perception]    {flag} {g.id} — {g.text}{attach}")

                if obs.all_done:
                    print(f"\n[done] all {len(obs.goals)} goals satisfied")
                    break

                goal = obs.next_unfinished()
                if goal is None:
                    print(f"\n[done] no unfinished goal — stopping")
                    break

                # Perception decided whether to attach an artifact.
                attached: list[tuple[str, bytes]] = []
                if goal.attach_artifact_id and artifacts.exists(goal.attach_artifact_id):
                    blob = artifacts.get_bytes(goal.attach_artifact_id)
                    attached.append((goal.attach_artifact_id, blob))
                    print(f"[attach]        {goal.attach_artifact_id} ({len(blob)} bytes)")

                # 3. DECISION
                out = decision.next_step(goal, hits, attached, history, tools_for_decision)

                if out.is_answer:
                    print(f"[decision]      ANSWER: {out.answer[:200]}{'...' if len(out.answer) > 200 else ''}")
                    history.append({
                        "iter": it,
                        "kind": "answer",
                        "goal_id": goal.id,
                        "text": out.answer,
                    })
                    final_answer = out.answer
                    continue

                # 4. ACTION
                tc = out.tool_call
                print(f"[decision]      TOOL_CALL: {tc.name}({json.dumps(tc.arguments)[:120]})")
                if tc.name in blocked:
                    # Belt and braces: the tool was withheld from the list, but a
                    # model can still name one from memory. Refuse at dispatch and
                    # tell Decision why, so the next turn answers from what it has
                    # instead of retrying the same call.
                    art_id = None
                    result_text = (
                        f"ERROR: tool '{tc.name}' is disabled for this run (--no-web). "
                        "Answer using only what search_knowledge returned. If the "
                        "knowledge base holds nothing relevant, say so plainly."
                    )
                    print(f"[blocked]       {tc.name} refused — --no-web is on")
                else:
                    result_text, art_id = await action.execute(session, tc)
                preview = result_text[:200].replace("\n", " ")
                print(f"[action]        → {preview}{'...' if len(result_text) > 200 else ''}"
                      + (f"   +{art_id}" if art_id else ""))

                # 5. MEMORY WRITE (zero-LLM for tool outcomes)
                memory.record_outcome(
                    tool_call=tc,
                    result_text=result_text,
                    artifact_id=art_id,
                    run_id=run_id,
                    goal_id=goal.id,
                )
                history.append({
                    "iter": it,
                    "kind": "action",
                    "goal_id": goal.id,
                    "tool": tc.name,
                    "arguments": tc.arguments,
                    "result_descriptor": result_text[:1500],
                    "artifact_id": art_id,
                })

    print(f"\n{'═' * 78}")
    print(f"FINAL: {final_answer}")
    print(f"{'═' * 78}\n")
    return final_answer


def main() -> None:
    args = sys.argv[1:]
    no_web = "--no-web" in args
    if no_web:
        args = [a for a in args if a != "--no-web"]
    query = " ".join(args) or "What is the current time in Asia/Tokyo and Asia/Kolkata? Tell me the difference in hours."
    asyncio.run(run(query, no_web=no_web))


if __name__ == "__main__":
    main()
