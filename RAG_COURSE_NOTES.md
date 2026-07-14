# RAG Interview Course — Progress Notes

Student goal: master RAG at any depth for AI Engineer / GenAI Engineer interviews.
Teaching style: **simple English, direct explanations (no story/person analogies), only interview-critical code snippets, quiz after each topic.**
Lab codebase: `My_Assignment/` (the student's own working RAG pipeline — FAISS + nomic-embed-text via gateway on port 8107).

## Curriculum (8 modules)

1. ✅ What is RAG + why we need it
2. ✅ Embeddings & vector similarity
3. 🔶 Chunking (taught, **quiz pending — see bottom**)
4. ⬜ Vector databases & indexing (FAISS internals, IndexFlatIP vs HNSW/IVF/PQ, when brute force dies)
5. ⬜ Retrieval quality (top-k, hybrid search BM25+vectors, RRF, re-ranking cross-encoders, query rewriting, HyDE)
6. ⬜ Augmentation & generation details (context ordering, lost-in-the-middle, citations)
7. ⬜ Evaluation (recall@k, MRR, nDCG, faithfulness, RAGAS)
8. ⬜ Advanced & system design (agentic RAG, GraphRAG, RAG vs fine-tuning vs long-context, production concerns) + mock interview drills

---

## Lesson 0 — What is RAG (DONE)

- RAG = Retrieval-Augmented Generation: search your own documents at question time, paste the best chunks into the LLM prompt, LLM answers ONLY from that text.
- LLM = frozen memory (trained weights never update). Five reasons we need RAG:
  1. LLM doesn't have YOUR private data
  2. LLM knowledge is old; RAG store updates in seconds (no retraining)
  3. Hallucination: RAG grounds answers in real text + gives citations + can say "I don't know"
  4. Pasting ALL docs every time = costly, hits context limits, "lost in the middle"
  5. Control: per-user permissions, easy deletion (GDPR)
- Key line: **"Retrieval quality is the ceiling of RAG quality"** — wrong chunks in → LLM cannot fix it.
- Interview 30-sec answer: "RAG combines an LLM with a retrieval system. At query time we search an external knowledge base for passages relevant to the question, inject them into the prompt, and instruct the model to answer from that context. Fixes knowledge cutoff, reduces hallucination, cheaper than stuffing everything into context."

## Lesson 1 — Embeddings (DONE)

- Embedding = text → fixed list of numbers (768 for nomic-embed-text). Similar meaning → nearby points. Search by meaning, not words.
- 768 = the **dimension**. Each single number means nothing; meaning is the whole pattern. More dims = finer meaning separation but more storage/compute. The model decides the dim, not you.
- Output size is FIXED regardless of input length → long documents get "diluted" (blurry vector) and hit token limits → **why we chunk**.
- Similarity: cosine (angle only) is the text standard. Student's code trick (`vector_index.py:33` + `:89`): **L2-normalize all vectors, then FAISS IndexFlatIP (dot product) = cosine similarity.**
  - Memorized interview line: "I used FAISS IndexFlatIP with L2-normalized vectors — inner product on unit vectors equals cosine similarity."
- Asymmetric embedding detail: docs embedded with `task_type="retrieval_document"`, queries with `"retrieval_query"`.
- STRICT RULE: same embedding model for docs and queries forever. Different model, same dim → **silent garbage results** (no error). Change model → delete index → re-embed all.

## Full query flow in the student's own code (DONE)

```
question ──memory.py:138──► 768 numbers (embed query)
         ──vector_index.py:105──► FAISS search → positions [17, 4, 231] + scores
         ──vector_index.py:110──► positions → IDs (via index_ids.json)
         ──memory.py:147──► IDs → items, text in value["chunk"] (via memory.json)
         ──decision.py:101-114──► chunks pasted into LLM prompt (max 10 hits, 2000 chars each)
         ──LLM──► grounded answer
```

- FAISS stores ONLY vectors → returns positions, never text. Two side files map back: `index_ids.json` (position→ID), `memory.json` (ID→text). Real vector DBs hide this plumbing; student built it manually.
- "Build prompt" = just string formatting: chunks + question + rule "Answer ONLY from the context" (anti-hallucination; enables "I don't know").
- The LLM never searches anything — it only sees the one prompt we built.
- War story from student's own code (`decision.py:92-96` comment): earlier the chunk text wasn't pasted into the prompt → the agent looped on search_knowledge forever. Fix: render chunk body inline. Lesson: "retrieval isn't done until the text reaches the model."

## Lesson 2 — Chunking (TAUGHT, quiz pending)

- Student's code `index_corpus.py:17`: `chunk_text(size=400, overlap=80)`, `stride = size - overlap = 320`. Sliding window of words.
- Overlap = insurance so no sentence gets destroyed on a chunk boundary (fact at words 395-405 survives inside chunk 2 which starts at 320). 80/400 = 20% overlap, classic ratio.
- Size trade-off: too small = sharp vector but no context ("It rose 12%" — what rose?); too big = blurry vector, weak match scores. Sweet spot ~200-500 words.
- 4 strategies: fixed-size (what student built), sentence/paragraph, recursive (LangChain default), semantic (cut where topic shifts; planned for student's Session 8).
- KNOWN FLAW in student's pipeline (great "what would you improve" answer): `index_corpus.py:50-52` embeds the **descriptor = only first 80 chars of the chunk**, not the full 400 words. Facts deep in the chunk are invisible to search. Production systems embed the full chunk text.

## QUIZ STATUS (chunking)

1. ✅ Overlap — student answered correctly in own words ("point starts in chunk n, ends in chunk n+1 → cut in half without overlap").
2. ⏳ STILL PENDING — ask first thing next session: 400-word doc → how many chunks with `chunk_text(size=400, overlap=80)`? 500-word doc → how many, chunk 2 starts where? (Answers: 1 chunk; 2 chunks — second starts at word 320.)
3. ✅ Answered FOR the student on request (blurry vector; silent token-limit truncation; bonus: cost + lost-in-the-middle). Re-test verbally later to confirm retention.

## QUESTION BANK — standing responsibility

`RAG_INTERVIEW_QUESTIONS.md` (same folder) = topic-wise list of every interview question discussed, with simple-English answers + human-style interview lines. **At the end of every session, add that session's new questions to it.** Q2's answer is deliberately NOT in that file (only here) so the student has to attempt it.

## CV guidance given (2026-07-08 session)

One deep RAG project on CV = fine; present as "agentic RAG built from scratch, no LangChain"; every CV term = fair game for 2-min grilling; known-flaws-and-fixes is a strong signal. Student prefers human-style answer phrasing over polished/AI-sounding lines — when giving interview lines, keep them casual and in the student's own logic.

## Key architecture facts of the student's project (for reference)

- Gateway on port 8107 auto-starts (`gateway.py ensure_gateway()`), `/v1/embed` endpoint, embedding model pinned: nomic-embed-text, 768 dims.
- `memory.py read()`: vector search first, keyword-overlap fallback if vector returns nothing (crude hybrid; real hybrid = BM25 + vectors + RRF, "future session").
- Metadata filter done by over-fetch 2× + post-filter (`memory.py:144`) — pre-filter vs post-filter is a real vector-DB design topic.
- `IndexFlatIP` = brute-force exact search, O(n) per query — fine at ~1K vectors, dies at scale → HNSW/IVF (Module 4 topic).
