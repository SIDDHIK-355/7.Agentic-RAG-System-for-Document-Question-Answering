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

# Fetch the GitLab-handbook corpus into sandbox/papers/ (one-time setup).
# Tries 35 handbook sections as raw markdown; saves the ~29 that exist and
# clear the 300-word minimum. (There is NO index_corpus.py — see session log.)
uv run fetch_corpus.py

# Restrict a run to the indexed knowledge base: withholds web_search and
# fetch_url from Decision's tool list and refuses them at dispatch
uv run agent7.py --no-web "Answer only from the knowledge base: <question>"
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

⚠️ `Session_7/memory.json` (~24.5 MB) and `Session_7/index_ids.json` (921 ids) at the **repo root** are stale leftovers from an older session. The agent never reads them — live state is `My_Assignment/state/` only. Both are gitignored; don't mistake the 921 for the real vector count.

## Critical constraints

**Embedding model is fixed.** The gateway pins `nomic-embed-text` at 768 dimensions. Changing `EMBED_OLLAMA_MODEL` or the dim after building any FAISS index invalidates every vector in that index. Changing the model requires deleting all FAISS state and re-indexing.

**`art:` handles are not file paths.** Artifact handles (`art:<sha256>`) are content-addressed references, not filesystem paths. Never pass them to `read_file`, `fetch_url`, or any tool. Decision receives artifact bytes via the `ATTACHED ARTIFACTS` section of its prompt when Perception sets `attach_artifact_id`.

**Gateway must be available before any LLM call.** `ensure_gateway()` auto-starts it but can take up to 45 seconds on cold boot. The agent calls this at the start of every `run()`.

**12-second inter-iteration sleep.** `agent7.py` calls `time.sleep(12)` between iterations (starting at iteration 2) to respect free-tier rate limits on the gateway's upstream providers.

**Chunking is word-based.** `index_document` uses sliding-window word-count chunking (400 words, 80-word overlap). Semantic chunking is planned for Session 8.

**Indexing is text-only.** `_read_for_index()` in `mcp_server.py` reads with `read_text(encoding="utf-8")`, so PDFs (and any binary file) raise `UnicodeDecodeError`. There is no PDF parser anywhere in the project.

## Environment

The agent reads `.env` from `My_Assignment/.env`. The gateway reads `Sir_Code/.env` (which is also at `Session_7/.env`). Required keys: `TAVILY_API_KEY`, plus whatever LLM provider keys are configured in the gateway (`GEMINI_API_KEY`, `GROQ_API_KEY`, etc.).

The gateway V7 runs on port 8107. Versions V1/V2/V3 run on 8099/8100/8101 respectively and can coexist.

---

## Session log — 2026-07-29 (state snapshot, verified results, open items)

Recorded so a fresh session can continue exactly where this one stopped. Every fact below was measured or verified live in that session, not assumed.

### What is in the index right now

- Live state (`My_Assignment/state/`): **56 memory items** (52 `fact`, 2 `tool_outcome`, 2 `scratchpad`) and **55 FAISS vectors**.
- The facts are essentially the **51 chunks of `sandbox/papers/gitlab_values.md`**, indexed this session via `index_document` (400-word chunks, 80 overlap), plus one older fact from `papers/company_facts.md`.
- The **other 28 corpus files are NOT indexed yet.** There is no batch indexer — `index_corpus.py` was referenced in older docs but **never existed**. Indexing currently happens one `index_document` call at a time, through agent runs.

### Corpus facts

- 29 markdown files in `My_Assignment/sandbox/papers/`, ~0.7 MB, **109,421 words** (~145k tokens; ≈342 chunks if fully indexed). Single source: the public GitLab handbook, fetched by `fetch_corpus.py`.
- `sandbox/` is **gitignored**, so the corpus is not on GitHub. Anyone cloning gets no papers, and the README line saying the handbook is "included in `sandbox/papers/`" is inaccurate for them. Deliberately left as-is for now.
- **No PDFs anywhere, and none can be read** (see "Indexing is text-only" above). Fix sketched but not implemented: `uv add pypdf`, a `.pdf` branch in `_read_for_index()`, and a `_read_pdf()` helper joining `page.extract_text()` per page. Caveats discussed: two-column papers scramble, headers repeat, scanned PDFs need OCR.

### `--no-web` flag (added this session, commit `b9542ae`)

- `agent7.py`: `WEB_TOOLS = frozenset({"web_search", "fetch_url"})`; `_mcp_tools_for_decision(tools, blocked)` filters them out of the list Decision receives; a dispatch guard additionally refuses a withheld tool by name with an explanatory error result.
- Rationale: a prompt saying "don't browse" is advisory — the tool list is the actual permission boundary. Both web tools must be blocked together: blocking only `web_search` leaves `fetch_url` callable on URLs the model knows from training. (`web_search` finds URLs via Tavily/DDG; `fetch_url` opens one known URL via crawl4ai headless Chromium. Neither touches the local corpus.)

### Verified grounding test (both runs green, 2026-07-29)

1. `uv run agent7.py "Index papers/gitlab_values.md, then summarise GitLab's core values"` → 51 chunks indexed, answered CREDIT correctly. Weak evidence alone — CREDIT is training-famous.
2. `uv run agent7.py --no-web "…what does GitLab mean by 'short toes', and what specific example do they give about the CEO?"` → log showed `--no-web ON … Decision sees 9 tools`, a real `search_knowledge` call, and the answer contained the **CEO's own merge request being closed after respectful feedback** — a detail that exists only in the indexed chunk (`gitlab_values.md` ~line 179). Genuine grounded retrieval, not training knowledge.

### Retrieval-quality finding (concrete case for the "Reranking" roadmap item)

- "short toes" occurs in chunks **6, 7, 42, 50** (of 51), but the **top-1** `search_knowledge` hit was **chunk 45**, which doesn't contain the phrase. A correct chunk sat lower in the k=5 list. **Good recall, weak ranking** — cite this when justifying a cross-encoder reranker.
- Also observed: Decision sometimes answers straight from `memory.read` hits without calling `search_knowledge` (run 1, iter 2). To force retrieval, the prompt must name the tool explicitly.

### Repo / GitHub state

- Remote: `https://github.com/SIDDHIK-355/7.Agentic-RAG-System-for-Document-Question-Answering` — currently **private**; owner intends to flip it public. A secret scan of every commit (24 at the time) was clean: no `.env` ever committed, no live key patterns in any blob, only placeholder `.env.example` files. Safe to publish. `gh` CLI installed but **not authenticated** (`gh auth login` needed before CLI-based visibility changes; browser path: Settings → Danger Zone).
- Commits this session: `74ebb60` (README: RAG-pipeline section moved to top, Phase 1|2 merged into one side-by-side Mermaid diagram, step tables added, walkthrough tabulated, memory-read image removed) and `b9542ae` (`--no-web`). `f7fee1c`/`0b88de8`/`3f6cd63`/`7295333` were made by the owner directly on GitHub (deleted the Design Decisions section, trimmed the MCP-tools section) — preserved via rebase.

### Cleanup candidates (discussed, not done)

- Add `Sir_Code/llm_gatewayV7/gateway_v7.db` to `.gitignore` — runtime SQLite log; dirties `git status` after every run.
- Write `index_corpus.py` (batch-index all of `sandbox/papers/`).
- PDF support via pypdf (sketch above).
- Optional: a second corpus source on a different topic, so retrieval must discriminate between domains — an all-GitLab corpus makes search trivially easy and never stress-tests ranking.
- `My_Assignment/xray.py` is untracked on purpose (owner's scratch file). `docs/memory-read-flow.png` still on disk but unreferenced.

### README / Mermaid conventions (learned the hard way — keep following)

- Side-by-side panels: one `flowchart LR`, one `subgraph` per panel, `direction TB` inside each. The cross-link **must be subgraph→subgraph** (`P1 -.-> P2`) — linking an inner node across panels makes Mermaid discard the inner `direction` and flatten that panel horizontally.
- Keep the invisible trailing spacer (`X ~~~ SP["____"]` + transparent style) in every diagram: it reserves the top-right corner where GitHub overlays its zoom controls.
- GitHub applies **one** style set to a Mermaid block in both light (`#ffffff`) and dark (`#0d1117`) themes. Use opaque fills with dark ink so text contrast is theme-independent, and set explicit `linkStyle` on every edge (GitHub's dark theme draws default edges in a light colour that vanishes on light panel fills). `linkStyle` indices are positional — never style the spacer edge.

### RAG design conclusions settled this session (for future discussions)

- 1M-token context windows don't kill RAG: real corpora exceed any window, and RAG wins on latency, cost/query, per-user permissions, freshness, and attribution. For small stable corpora, long-context + prompt caching is a legitimate alternative (this corpus ≈145k tokens would fit ~7×; cost/query ≈ $0.73 uncached, ≈$0.07 cached, ≈$0.015 with RAG). The modern framing: retrieval moved from a fixed pipeline stage to a *tool the model decides to call* — which is exactly what `search_knowledge` is.
- Prompt caching is a prefix match: writes cost 1.25× (5-min TTL) / 2× (1-hour TTL), reads 0.1×; break-even ≈3 questions/hour on the 1-hour TTL; any byte change invalidates. Frequently-changing data therefore favors RAG (re-embed only the changed doc). These TTLs are provider-side only — the local FAISS index has **no expiry**; it persists until `memory.clear()`.
- Corpus size is measured in words/tokens, not file count. Grounding is tested with a question whose answer the model cannot know from training, plus a paired in-corpus question — one proves refusal, the other proves retrieval.
- Embeddings are local and free (Ollama `nomic-embed-text`; gateway falls back to Gemini `gemini-embedding-001` @768). Paid LLM calls happen at exactly three sites: `perception.py` (`auto_route="perception"`), `decision.py` (`auto_route="decision"`), and `memory.remember()` (`auto_route="memory"`). Any **one** provider key is enough to run; the extra keys (GEMINI, GROQ, CEREBRAS, NVIDIA all set as of 2026-07-29) exist for rate-limit failover, not as separate requirements.


## MY Name is Siddhi Khobragade ?