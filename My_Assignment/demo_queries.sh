#!/bin/zsh
# ONE-FILE PROJECT RUNNER — gateway + index + all demo queries.
#
#   ./demo_queries.sh            → start everything, run the 6 grounding queries
#   ./demo_queries.sh --custom   → also run the 5 custom submission queries
#
# Queries 1-3 are IN the corpus  -> must answer correctly.
# Queries 4-6 are OUT of corpus  -> must refuse, even though the LLM
#                                   knows them from training.
# All runs use --no-web so the web can never rescue an answer.
# Traces are saved to ../traces/grounding_demo/ (and ../traces/custom_queries/)

set -u
cd "$(dirname "$0")"

# ══════════ STEP 1 · Ollama (embeddings) ══════════
if ! pgrep -x ollama >/dev/null 2>&1; then
  echo "[setup] starting ollama..."
  ollama serve >/dev/null 2>&1 &
  sleep 3
fi

# ══════════ STEP 2 · LLM gateway (port 8107) ══════════
if ! curl -s -m 3 http://localhost:8107/v1/routers >/dev/null 2>&1; then
  echo "[setup] starting gateway from Gateway_Code/llm_gatewayV7 ..."
  ( cd ../Gateway_Code/llm_gatewayV7 && nohup ./run.sh >/tmp/gateway.log 2>&1 & )
  echo "[setup] waiting for gateway (cold boot can take ~45 s)..."
  for i in {1..30}; do
    sleep 3
    curl -s -m 3 http://localhost:8107/v1/routers >/dev/null 2>&1 && break
  done
fi
curl -s -m 3 http://localhost:8107/v1/routers >/dev/null 2>&1 \
  && echo "[setup] gateway UP ✅" \
  || { echo "[setup] gateway failed to start — check /tmp/gateway.log"; exit 1; }

# ══════════ STEP 3 · knowledge-base index (one time) ══════════
if [ ! -f state/index.faiss ]; then
  echo "[setup] no index found — building (76 files, ~753 chunks)..."
  uv run index_corpus.py
else
  echo "[setup] index present ✅"
fi

OUT=../traces/grounding_demo
mkdir -p "$OUT"

run() {  # run <outdir> <n> <label> <query>
  echo
  echo "══════════════════════════════════════════════════════════════"
  echo "  QUERY $2 — $3"
  echo "══════════════════════════════════════════════════════════════"
  uv run agent7.py --no-web "$4" | tee "$1/query_$2.txt"
  sleep 15   # respect free-tier rate limits between runs
}

# ══════════ STEP 4 · grounding demo — IN corpus: must answer ══════════

run "$OUT" 1 "IN corpus · GitLab · expect: CEO's merge request closed after feedback" \
  "Answer only from the knowledge base: what does GitLab mean by 'short toes', and what example do they give about the CEO?"

run "$OUT" 2 "IN corpus · Niteo · expect: €190/day" \
  "Answer only from the knowledge base: what is the allowance bonus per day for attending an international conference at Niteo?"

run "$OUT" 3 "IN corpus · PostHog (semantic) · expect: 90 days via Brex" \
  "Answer only from the knowledge base: I bought something for work out of my own pocket by mistake - how long do I have to get my money back from PostHog?"

# ══════════ STEP 5 · grounding demo — OUT of corpus: must refuse ══════════

run "$OUT" 4 "OUT of corpus · Google · expect: refusal (not in knowledge base)" \
  "Answer only from the knowledge base: what is Google's parental leave policy?"

run "$OUT" 5 "OUT of corpus · Attention paper · expect: refusal despite training knowledge" \
  "Answer only from the knowledge base: what are the key contributions of the 'Attention Is All You Need' paper?"

run "$OUT" 6 "OUT of corpus · Netflix keeper test · expect: refusal despite training knowledge" \
  "Answer only from the knowledge base: what does Netflix's culture memo say about 'keeper test'?"

# ══════════ STEP 6 (optional, --custom) · the 5 submission queries ══════════

if [ "${1:-}" = "--custom" ]; then
  CQ=../traces/custom_queries/with_index
  mkdir -p "$CQ"

  run "$CQ" 1 "CUSTOM Q1 · direct · Basecamp · expect: \$96.05 per pay period" \
    "Answer only from the knowledge base: what is the per-pay-period payroll deduction for employee-only medical coverage at 37signals/Basecamp?"

  run "$CQ" 2 "CUSTOM Q2 · direct · Niteo · expect: €190/day" \
    "Answer only from the knowledge base: according to the Niteo handbook, what is the allowance bonus per day for attending an international conference?"

  run "$CQ" 3 "CUSTOM Q3 · semantic · Sourcegraph · expect: \$50/day, \$250 max" \
    "Answer only from the knowledge base: if I'm away on a work trip for Sourcegraph, will the company pay someone to watch my dog, and how much can I get back?"

  run "$CQ" 4 "CUSTOM Q4 · semantic · GitLab · expect: 22nd of each month" \
    "Answer only from the knowledge base: I do freelance work for GitLab from India - on which day each month does my money actually arrive?"

  run "$CQ" 5 "CUSTOM Q5 · semantic · PostHog · expect: 90 days via Brex" \
    "Answer only from the knowledge base: I bought something for work out of my own pocket by mistake - how long do I have to get my money back from PostHog?"
fi

echo
echo "Done. Traces saved in ../traces/"
