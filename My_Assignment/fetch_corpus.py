"""Fetch a clean corpus for the S7 RAG agent.

Downloads pages of the public GitLab Handbook as RAW MARKDOWN from the
handbook's source repository (not scraped HTML), cleans them, and saves
them into sandbox/papers/ ready for index_document / index_corpus.

Why raw markdown instead of scraping the website: the repo files are the
actual text the site is built from, so there are no menus, cookie banners,
or navigation junk to pollute the chunks.

Cleaning applied to each page:
  - strip YAML frontmatter (--- ... ---)
  - strip HTML comments and Hugo shortcodes ({{< ... >}})
  - turn markdown links [text](url) into just: text
  - drop image embeds
  - collapse repeated blank lines

Run once:  uv run fetch_corpus.py
"""

from __future__ import annotations

import re
from pathlib import Path

import httpx

RAW_BASE = (
    "https://gitlab.com/gitlab-com/content-sites/handbook/-/raw/main/content/handbook"
)
OUT_DIR = Path(__file__).resolve().parent / "sandbox" / "papers"
MIN_WORDS = 300  # skip stub pages that would make useless chunks

# Fact-dense handbook sections. Each maps to <section>/_index.md in the repo.
SECTIONS = [
    "values",
    "communication",
    "company/culture",
    "company/mission",
    "leadership",
    "people-group",
    "people-policies",
    "total-rewards",
    "hiring",
    "hiring/interviewing",
    "engineering",
    "engineering/workflow",
    "engineering/devops",
    "security",
    "product",
    "product-development",
    "marketing",
    "sales",
    "finance",
    "legal",
    "support",
    "customer-success",
    "business-technology",
    "it",
    "teamops",
    "tools-and-tips",
    "labor-and-employment-notices",
    "people-group/anti-harassment",
    "people-group/learning-and-development",
    "total-rewards/benefits",
    "total-rewards/compensation",
    "communication/youtube",
    "engineering/architecture",
    "security/product-security",
    "company/structure",
]

_FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_SHORTCODE = re.compile(r"\{\{[<%].*?[>%]\}\}", re.DOTALL)
_IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_BLANKS = re.compile(r"\n{3,}")


def clean(md: str) -> str:
    md = _FRONTMATTER.sub("", md)
    md = _HTML_COMMENT.sub("", md)
    md = _SHORTCODE.sub("", md)
    md = _IMAGE.sub("", md)
    md = _LINK.sub(r"\1", md)  # keep the link text, drop the URL
    md = _BLANKS.sub("\n\n", md)
    return md.strip()


def fetch_section(client: httpx.Client, section: str) -> str | None:
    url = f"{RAW_BASE}/{section}/_index.md"
    r = client.get(url, follow_redirects=True)
    if r.status_code != 200 or r.text.lstrip().startswith("<!DOCTYPE"):
        return None
    return r.text


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    saved, skipped = 0, 0
    with httpx.Client(timeout=30.0) as client:
        for section in SECTIONS:
            raw = fetch_section(client, section)
            if raw is None:
                print(f"  skip (not found)   {section}")
                skipped += 1
                continue
            text = clean(raw)
            words = len(text.split())
            if words < MIN_WORDS:
                print(f"  skip ({words} words)  {section}")
                skipped += 1
                continue
            name = "gitlab_" + section.replace("/", "_") + ".md"
            (OUT_DIR / name).write_text(text, encoding="utf-8")
            print(f"  saved {words:>6} words  {name}")
            saved += 1
    print(f"\ndone: {saved} pages saved to {OUT_DIR}, {skipped} skipped")


if __name__ == "__main__":
    main()
