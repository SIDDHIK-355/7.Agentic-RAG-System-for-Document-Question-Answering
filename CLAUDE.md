# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository layout

```
Session_7/
├── My_Assignment/   ← the assignment codebase (work here)
├── Sir_Code/        ← reference code provided by the instructor
│   ├── S7code/          identical to My_Assignment (reference copy)
│   └── llm_gatewayV7/   the LLM gateway that the agent depends on
└── My_Notes/        ← HTML notes (read-only reference)
```

All development work happens in `My_Assignment/`.

## Running the agent

All commands must be run from `My_Assignment/`:

```bash
# Run the agent with a query
uv run agent7.py "What is the current time in Tokyo and Bangalore?"

# Start the gateway manually (auto-started by agent if not running)
cd ../Sir_Code/llm_gatewayV7 && ./run.sh

# Check if gateway is up
curl -s http://localhost:8107/v1/routers | python3 -m json.tool

# Fetch the 50-article AI corpus (one-time setup)
uv run fetch_corpus.py

# Index the fetched corpus into FAISS
uv run index_corpus.py
```

## Tests

```bash
# Run all non-network tests
uv run pytest test_mcp_server.py -v

# Run a single test
uv run pytest test_mcp_server.py::test_get_time -v

# Run tests that need network/API access
uv run pytest test_mcp_server.py -v -m network

# Run tests that need the embedding endpoint
uv run pytest test_mcp_server.py -v -m embed
```

## Architecture

The agent runs a `MAX_ITERATIONS=20` loop with five typed layers that pass structured Pydantic models from `schemas.py`:

```
memory.read → perception.observe → decision.next_step → action.execute → memory.record_outcome
```

**`gateway.py`** — bridge to `llm_gatewayV7` on port 8107. Auto-starts the gateway process if not running (`ensure_gateway()`). Exposes `LLM` (the gateway client) and `embed(text)`. Every layer imports from here so boot logic lives in one place. The gateway uses `auto_route` to send each layer's calls to appropriate-sized LLMs (TINY/LARGE tier).

**`schemas.py`** — all typed contracts: `MemoryItem`, `Goal`, `Observation`, `DecisionOutput`, `ToolCall`, `Artifact`. The only source of truth for inter-layer data shapes.

**`memory.py`** — typed service with four kinds: `fact`, `preference`, `tool_outcome`, `scratchpad`. Reads use FAISS vector search first; falls back to keyword overlap when vector returns nothing. Writes embed the descriptor via the gateway's `/v1/embed` endpoint (except `scratchpad` items). Two public write paths: `remember()` (LLM-classified, for free-form content) and `record_outcome()` (zero-LLM, for tool results). `add_fact()` is used by the document indexing tools.

**`vector_index.py`** — wraps `faiss.IndexFlatIP` (inner product on L2-normalized vectors = cosine similarity). Persists to `state/index.faiss` and `state/index_ids.json`.

**`perception.py`** — decomposes the user query into goals on iteration 1, then tracks goal completion across iterations. Decides whether the next unfinished goal needs raw artifact bytes attached (synthesis/extract/summarise goals). Does NOT read artifact bytes — sets `attach_artifact_id` and the outer loop in `agent7.py` resolves it.

**`decision.py`** — one LLM call per turn. Receives the current goal, memory hits (with inline `raw`/`chunk` content from `value`), history, and optionally attached artifact bytes. Returns either a plain-text answer or exactly one MCP tool call.

**`action.py`** — pure MCP dispatcher. Results larger than 4 KB go to the artifact store and return an `art:` handle; smaller results pass as text. Guards against `art:` handles being passed as file paths or URLs.

**`artifacts.py`** — SHA-256 content-addressed blob store under `state/artifacts/`. Each artifact is a `.bin` file (bytes) plus a `.json` metadata file. Deduplicates by content hash.

**`mcp_server.py`** — 11 MCP tools via FastMCP stdio transport: `web_search`, `fetch_url`, `get_time`, `currency_convert`, `read_file`, `list_dir`, `create_file`, `update_file`, `edit_file`, `index_document`, `search_knowledge`. File tools are sandboxed to `./sandbox/`. `index_document` chunks a file and writes each chunk as a `fact` into memory (FAISS-searchable). `search_knowledge` is a vector search over indexed facts.

## State files

| Path | Contents |
|---|---|
| `state/memory.json` | Persisted memory items (all kinds) |
| `state/index.faiss` | FAISS binary index |
| `state/index_ids.json` | Parallel list mapping FAISS positions to `MemoryItem` ids |
| `state/artifacts/` | Content-addressed blob store |
| `sandbox/` | Sandboxed filesystem for MCP file tools |
| `usage.json` | Monthly Tavily/DuckDuckGo usage counters |

To clear all state between runs: `python -c "import memory; memory.clear()"` (clears both `memory.json` and the FAISS index). Delete `state/artifacts/` manually to clear the artifact store.

## Critical constraints

**Embedding model is fixed.** The gateway pins `nomic-embed-text` at 768 dimensions. Changing `EMBED_OLLAMA_MODEL` or the dim after building any FAISS index invalidates every vector in that index. Changing the model requires deleting all FAISS state and re-indexing.

**`art:` handles are not file paths.** Artifact handles (`art:<sha256>`) are content-addressed references, not filesystem paths. Never pass them to `read_file`, `fetch_url`, or any tool. Decision receives artifact bytes via the `ATTACHED ARTIFACTS` section of its prompt when Perception sets `attach_artifact_id`.

**Gateway must be available before any LLM call.** `ensure_gateway()` auto-starts it but can take up to 45 seconds on cold boot. The agent calls this at the start of every `run()`.

**12-second inter-iteration sleep.** `agent7.py` calls `time.sleep(12)` between iterations (starting at iteration 2) to respect free-tier rate limits on the gateway's upstream providers.

**Chunking is word-based.** `index_document` and `index_corpus.py` use sliding-window word-count chunking (400 words, 80-word overlap). Semantic chunking is planned for Session 8.

## Environment

The agent reads `.env` from `My_Assignment/.env`. The gateway reads `Sir_Code/.env` (which is also at `Session_7/.env`). Required keys: `TAVILY_API_KEY`, plus whatever LLM provider keys are configured in the gateway (`GEMINI_API_KEY`, `GROQ_API_KEY`, etc.).

The gateway V7 runs on port 8107. Versions V1/V2/V3 run on 8099/8100/8101 respectively and can coexist.
