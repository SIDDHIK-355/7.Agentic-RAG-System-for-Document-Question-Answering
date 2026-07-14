# RAG Interview Question Bank

Questions discussed in the course, topic-wise. New questions get added here every session.
Format: question → short answer in simple English → (where useful) a human-style line you can say in the interview.

---

## Topic 1 — What is RAG & why we need it

**Q: What is RAG?**
A: Retrieval-Augmented Generation. At question time we search our own documents, pick the best chunks, paste them into the LLM prompt, and tell the LLM to answer ONLY from that text.

**Q: Why do we need RAG when LLMs are already smart?**
A: Five reasons:
1. The LLM doesn't have YOUR private data.
2. LLM knowledge is frozen at training time; a RAG store updates in seconds, no retraining.
3. Less hallucination — answers are grounded in real text, with citations, and the model can say "I don't know."
4. Pasting ALL documents every time is costly, hits context limits, and causes "lost in the middle."
5. Control — per-user permissions, easy deletion (GDPR).

**Q: What limits the quality of a RAG system?**
A: Retrieval. **"Retrieval quality is the ceiling of RAG quality"** — if wrong chunks go in, the LLM cannot fix it.

**Q: Give a 30-second RAG answer.**
A: "RAG combines an LLM with a retrieval system. At query time we search an external knowledge base for passages relevant to the question, inject them into the prompt, and instruct the model to answer from that context. It fixes knowledge cutoff, reduces hallucination, and is cheaper than stuffing everything into context."

**Q: If RAG is standard, why do companies build custom pipelines instead of buying a ready product (ChatGPT Enterprise, Glean, Copilot)?**
A: Off-the-shelf RAG exists and works "okay" (~70% quality) — but RAG quality depends on YOUR data and questions, unlike a one-size-fits-all app. A law firm needs section-aware chunking + exact citations; a hospital needs on-prem + per-user permissions; a dev team needs code-aware chunking + hybrid search (error codes don't embed well). Custom engineering closes the 70%→95% gap: parsing, chunking strategy, hybrid retrieval, re-ranking, metadata filters, freshness, permissions, evaluation. The skeleton is standard; the quality is custom.
Human-style line: *"Buying gives average quality on generic data. The value is in decisions tuned to the specific data — that's what 'I built a RAG pipeline' actually means: I made those decisions and can defend them."*

---

## Topic 2 — Embeddings & vector similarity

**Q: What is an embedding?**
A: Text converted into a fixed list of numbers (768 for nomic-embed-text). Similar meaning → nearby points. This lets us search by meaning, not by matching words.

**Q: What does the dimension (768) mean? Is one number one meaning?**
A: 768 is just the size of the vector. No single number means anything alone — the meaning is the whole pattern. More dimensions = finer meaning separation but more storage and compute. The model decides the dimension, not you.

**Q: Why can't we embed a whole long document as one vector?**
A: The output is always the same fixed size regardless of input length. A long document gets "diluted" into a blurry vector, and it can exceed the model's token limit. This is exactly why we chunk.

**Q: Which similarity metric is used for text and why?**
A: Cosine similarity — it compares only the angle (direction) between vectors, not their length. It's the standard for text embeddings.

**Q: How does your project compute cosine similarity with FAISS?**
A: "I used FAISS IndexFlatIP with L2-normalized vectors — inner product on unit vectors equals cosine similarity." (Code: normalize in `vector_index.py`, then dot-product search.)

**Q: What is asymmetric embedding?**
A: Documents and queries are embedded with different task hints — docs with `task_type="retrieval_document"`, queries with `"retrieval_query"`. The model optimizes each side for matching the other.

**Q: Can I change the embedding model later?**
A: Only if you delete the whole index and re-embed everything. Mixing models (even with the same dimension) gives **silent garbage results** — no error, just wrong matches. Rule: same embedding model for docs and queries, forever.

**Q: What happens if you change the embedding model in a live RAG system?**
A: Two cases. Different dimension → immediate error (lucky — you find out instantly; my `vector_index.py` raises on dim mismatch). Same dimension → **silent garbage**: no crash, but old vectors and new queries live in different spaces, similarity scores become meaningless, retrieval quietly returns wrong chunks. Fix: re-embed the ENTIRE corpus with the new model. In production: build a second index in the background with the new model, keep serving from the old one, flip queries over when ready (blue-green migration), delete the old.
Line to remember: "Same dimension, different model = silent garbage."
Human-style answer: *"Nothing crashes, that's the problem. Old vectors and new queries live in different spaces, so retrieval silently returns garbage. You have to re-embed the whole corpus — in production I'd build a second index in the background and switch when it's ready. In my project I pinned the embedding model at the gateway, and my index code raises if the dimension ever changes."*

**Q: FAISS returns positions, not text. How do you get the text back?**
A: FAISS stores only vectors, so it returns positions + scores. Two side files map back: `index_ids.json` (position → item ID) and `memory.json` (ID → text). Real vector DBs hide this plumbing; I built it manually.

---

## Topic 3 — Chunking

**Q: Why do we chunk documents at all?**
A: Two reasons: (1) the embedding vector is fixed size, so a whole document becomes a blurry averaged vector that matches nothing well; (2) embedding models have token limits — extra text gets silently cut off.

**Q: Why do chunks overlap? (quiz Q1 — answered correctly ✅)**
A: Sometimes a point starts at the end of chunk *n* and finishes in chunk *n+1*. Without overlap it gets cut in half and neither chunk has the full thing. Overlap makes sure at least one chunk has it completely.
Short version: "Overlap stops sentences from being cut in half at chunk boundaries."

**Q: With `chunk_text(size=400, overlap=80)`, how many chunks for a 400-word doc? For a 500-word doc? (quiz Q2 — ⏳ still pending, answer it!)**
A: (Work it out: stride = 400 − 80 = 320. Answer is in RAG_COURSE_NOTES.md after you try.)

**Q: A friend uses 3000-word chunks "for more context." Which problems hit him? (quiz Q3)**
A: Two main problems:
1. **Blurry vector** — the embedding is always 768 numbers no matter the length. 3000 words averaged into 768 numbers strongly represents nothing, so match scores are weak and the right chunk often isn't retrieved.
2. **Token limit / silent cut-off** — embedding models have a max input (nomic-embed-text ≈ 2048 tokens ≈ 1500 words). Extra words are thrown away with NO error. Facts in the cut-off part can never be found by search.
Bonus third: even when retrieved, pasting 3000 words into the prompt for one question wastes tokens, costs more, and the answer can get "lost in the middle."
Human-style interview line: *"Two problems. First, the vector is fixed size — 768 numbers — so 3000 words in it becomes a blur, it matches nothing well. Second, embedding models have a token limit, so half his chunk probably got cut off silently and that half is invisible to search."*

**Q: What's the chunk-size trade-off?**
A: Too small (≈50 words) = sharp vector but no context ("It rose 12%" — what rose?). Too big = blurry vector, weak scores, token-limit risk. Sweet spot ≈ 200–500 words. My project uses 400 with 80 overlap (20% — a classic ratio).

**Q: Name the 4 chunking strategies.**
A: 1. Fixed-size sliding window (what I built — simple, fast, ignores meaning). 2. Sentence/paragraph splitting. 3. Recursive (try paragraphs → sentences → words; LangChain default). 4. Semantic (embed sentences, cut where topic shifts — best quality, most expensive).

**Q: What would you improve in your own chunking pipeline?**
A: Two things: (1) my code embeds only the descriptor — the first 80 characters of each chunk — not the full 400 words, so facts deep inside a chunk are invisible to search; production systems embed the full chunk text. (2) Move from word-count chunking to semantic chunking.

---

## Topic — CV & project presentation (discussed this session)

**Q: Is one RAG project on the CV enough?**
A: Yes — one deep project beats three shallow ones. Interviewers pick one project and drill it for 15–20 minutes, so depth matters, not count. But the CV project only gets you in the door — concept depth (indexing, retrieval quality, evaluation) gets the offer.

**Q: How do I present my project?**
A: As an **agentic RAG system built from scratch (no LangChain)**. Selling points:
1. Manual vector-store plumbing — FAISS IndexFlatIP + L2 normalization = cosine, own position→ID→text mapping.
2. Agentic loop with typed Pydantic contracts (perception → decision → action → memory) + 11 MCP tools.
3. Hybrid fallback — vector search first, keyword overlap when vectors return nothing.
4. Real engineering decisions — content-addressed artifact store (SHA-256), sliding-window chunking, multi-tier LLM routing.
5. Known flaws + fixes — strongest interview signal: "here's what I'd improve and why."

**Rule:** every term on the CV = permission to grill you on it for 2 minutes. Never write what you can't explain.

---

## Coming next (Module 4 — vector DBs & indexing)

Questions that will be added after we cover it: IndexFlatIP vs HNSW vs IVF vs PQ, when brute force dies, recall vs speed trade-off, how to scale past 1M documents.
