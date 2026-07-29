"""Batch-index the corpus: every .md file under sandbox/papers/.

Zero LLM calls — only embeddings. Uses the exact same chunking and
add_fact write path as the `index_document` MCP tool, so chunks written
here are indistinguishable from chunks the agent indexes itself.

Usage:
  uv run index_corpus.py           # index files not already in memory
  uv run index_corpus.py --fresh   # memory.clear() first, then index all
"""

from __future__ import annotations

import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import memory  # noqa: E402
from gateway import ensure_gateway  # noqa: E402
from mcp_server import _chunk_text  # noqa: E402  same chunking as index_document

PAPERS = Path(__file__).resolve().parent / "sandbox" / "papers"


def indexed_sources() -> set[str]:
    return {
        item.source
        for item in memory._load()
        if item.kind == "fact" and item.source and item.source.startswith("sandbox:papers/")
    }


def index_file(path: Path, run_id: str) -> int:
    rel = f"papers/{path.name}"
    source = f"sandbox:{rel}"
    text = path.read_text(encoding="utf-8")
    chunks = _chunk_text(text)
    for i, chunk in enumerate(chunks):
        preview = chunk[:120].replace("\n", " ")
        descriptor = f"[{source} chunk {i+1}/{len(chunks)}] {preview}"
        memory.add_fact(
            descriptor=descriptor,
            value={
                "chunk": chunk,
                "chunk_index": i,
                "total_chunks": len(chunks),
                "source": source,
            },
            source=source,
            run_id=run_id,
        )
    return len(chunks)


def main() -> None:
    fresh = "--fresh" in sys.argv
    ensure_gateway()
    if fresh:
        print("clearing memory + FAISS index")
        memory.clear()
    done = set() if fresh else indexed_sources()

    files = sorted(PAPERS.glob("*.md"))
    total_chunks, skipped, t0 = 0, 0, time.time()
    run_id = f"index-corpus-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    for n, path in enumerate(files, 1):
        if f"sandbox:papers/{path.name}" in done:
            print(f"  [{n:>2}/{len(files)}] already indexed  {path.name}")
            skipped += 1
            continue
        chunks = index_file(path, run_id)
        total_chunks += chunks
        print(f"  [{n:>2}/{len(files)}] {chunks:>3} chunks  {path.name}")

    dt = time.time() - t0
    print(
        f"\ndone: {len(files) - skipped} files indexed ({total_chunks} chunks) "
        f"in {dt:.0f}s, {skipped} already present"
    )


if __name__ == "__main__":
    main()
