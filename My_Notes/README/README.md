# 🤖 EAGV3 Session 7 — Agentic RAG System

A production-style AI agent with **vector memory**, **document indexing**, and **semantic retrieval** built on a clean 4-role architecture.

---

## What This Does

This agent can:
- **Remember things** across sessions (FAISS-backed vector memory)
- **Index any document** and make it searchable by meaning, not just keywords
- **Answer questions** from indexed documents — even when the exact words don't match
- **Search the web**, fetch URLs, create files, and more

The core idea: instead of searching for exact words, the agent understands *meaning*. Ask "how does this paper handle credit assignment?" — it finds relevant chunks even if that phrase never appears in the document.

---

## The Problem It Solves

Standard LLMs don't know about your private documents. Keyword search fails when your question uses different words than the document. This system solves both:

1. **Private document access** — index any file locally, never sent to the cloud
2. **Semantic search** — find content by meaning using vector embeddings (768-dimensional vectors via `nomic-embed-text`)
3. **Cross-run memory** — the agent remembers what it indexed even after restart

---

## Architecture — 4 Roles

```
User Query
    ↓
MEMORY      reads stored facts, searches FAISS for relevant items
    ↓
PERCEPTION  understands the query, creates and manages the goal list
    ↓
DECISION    picks which tool to use OR writes the final answer
    ↓
ACTION      executes the tool (index, search, fetch, etc.)
    ↓
MEMORY      stores the result
    ↓
(loop until all goals done)
```

Each role has one job and never does another role's job. This is the separation of concerns principle.

---

## Project Structure

```
S7code/
│
├── agent7.py          # Main loop — orchestrates all 4 roles
├── perception.py      # Role 1: breaks query into goals
├── decision.py        # Role 2: picks tools or answers
├── action.py          # Role 3: executes tool calls
├── memory.py          # Role 4: reads and writes memory (FAISS + JSON)
│
├── gateway.py         # Bridge to LLM Gateway V7 (auto-starts on port 8107)
├── mcp_server.py      # 11 MCP tools the agent can use
├── schemas.py         # Pydantic data contracts between roles
├── artifacts.py       # Stores large binary results (fetched pages, etc.)
├── vector_index.py    # FAISS index management
│
├── sandbox/           # Agent's file workspace (sandboxed)
│   └── papers/        # 5 research papers (indexed corpus)
│       ├── attention.md   # Attention Is All You Need
│       ├── cot.md         # Chain-of-Thought Reasoning
│       ├── dpo.md         # Direct Preference Optimization
│       ├── lora.md        # LoRA
│       └── react.md       # ReAct
│
└── state/             # Persistent memory (survives restarts)
    ├── memory.json        # All memory items with text
    ├── index.faiss        # FAISS vector index (768-dim vectors)
    └── index_ids.json     # Maps FAISS positions to memory IDs
```

---

## The 11 MCP Tools

| Tool | What it does |
|---|---|
| `web_search` | Search the web (Tavily + DuckDuckGo) |
| `fetch_url` | Fetch any URL as clean markdown |
| `get_time` | Current time in any timezone |
| `currency_convert` | Convert between currencies |
| `read_file` | Read a file from sandbox |
| `list_dir` | List directory contents |
| `create_file` | Create a new file in sandbox |
| `update_file` | Overwrite an existing file |
| `edit_file` | Find-and-replace inside a file |
| `index_document` | **NEW** — chunk + embed + save to FAISS |
| `search_knowledge` | **NEW** — vector search over indexed corpus |

---

## How RAG Works Here

```
Document (papers/attention.md)
    ↓ index_document
Split into chunks (400 words, 80 overlap)
    ↓
Each chunk → Ollama (nomic-embed-text) → 768 numbers
    ↓
768 numbers saved to index.faiss
Original text saved to memory.json
    ↓
User asks: "what are the key contributions?"
    ↓
Query → Ollama → 768 numbers
    ↓
FAISS finds closest stored vectors (cosine similarity)
    ↓
Returns original chunk text
    ↓
Decision reads chunks → writes answer
```

---

## Setup

**Requirements:**
- Python 3.11+
- [Ollama](https://ollama.com) (for local embeddings — free, unlimited)
- API keys for at least one LLM provider

**Install:**
```bash
cd S7code
uv sync
ollama pull nomic-embed-text
```

**Configure** — create `.env` in the parent folder (`Session_7/.env`):
```
GEMINI_API_KEY=...
GROQ_API_KEY=...
TAVILY_API_KEY=...
OLLAMA_URL=http://localhost:11434
EMBED_ORDER=ollama,gemini
```

**Run:**
```bash
uv run agent7.py "your query here"
```

The LLM gateway auto-starts on port 8107.

---

## The 8 Base Queries

| Query | Tests |
|---|---|
| A — Claude Shannon Wikipedia | URL fetch + artifact attachment |
| B — Tokyo activities + weather | Multi-goal + memory carryover |
| C — Mom's birthday (2 runs) | Durable memory across restarts |
| D — Python asyncio research | Multi-source web synthesis |
| E — Index attention.md | Basic RAG (index + search) |
| F — Index all 5 papers (2 runs) | FAISS persistence across processes |
| G — Credit assignment problem | Semantic search (words ≠ meaning) |
| H — ReAct vs CoT comparison | Cross-document synthesis |

---

## Reset Agent Memory

```bash
rm state/memory.json state/index.faiss state/index_ids.json
```

---

## Key Rule — Separation of Concerns

`perception.py` must **never** contain MCP tool names. Verify with:

```bash
grep -n "index_document\|search_knowledge\|fetch_url" perception.py
# must return: no matches
```
