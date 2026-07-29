"""Fetch a clean corpus for the S7 RAG agent.

Downloads pages of five public company handbooks as RAW MARKDOWN from
each handbook's source repository (not scraped HTML), cleans them, and
saves them into sandbox/papers/ ready for index_document / index_corpus.

Sources (all public):
  - GitLab handbook        (gitlab.com source repo)      -> gitlab_*.md
  - Basecamp/37signals     (github.com/basecamp/handbook) -> basecamp_*.md
  - PostHog handbook       (github.com/PostHog/posthog.com) -> posthog_*.md
  - Sourcegraph handbook   (github.com/sourcegraph/handbook) -> sourcegraph_*.md
  - Niteo handbook         (github.com/teamniteo/handbook) -> niteo_*.md

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

# The other four handbooks live on GitHub; each entry is (repo-relative
# path, saved filename). Curated for fact-dense people/culture/process
# pages; auto-generated pages (tool reports, newsletters) are excluded.
GITHUB_RAW = "https://raw.githubusercontent.com"

BASECAMP = [  # basecamp/handbook @ master, files at repo root
    "benefits-and-perks.md",
    "getting-started.md",
    "how-we-work.md",
    "making-a-career.md",
    "managing-work-devices.md",
    "moonlighting.md",
    "our-internal-systems.md",
    "our-rituals.md",
    "titles-for-QA.md",
    "titles-for-designers.md",
    "titles-for-ops.md",
    "titles-for-programmers.md",
    "titles-for-support.md",
]

POSTHOG = [  # PostHog/posthog.com @ master, under contents/handbook/
    "company/communication.md",
    "company/offsites.md",
    "engineering/development-process.md",
    "growth/sales/how-we-work.md",
    "growth/sales/new-sales.md",
    "people/compensation.mdx",
    "people/hiring-process/index.mdx",
    "people/onboarding.md",
    "people/share-options.mdx",
    "people/spending-money.md",
    "story.md",
    "support/posthog-support.md",
]

SOURCEGRAPH = [  # sourcegraph/handbook @ main, under content/
    "benefits-pay-perks/benefits-perks/leave-of-absence.md",
    "benefits-pay-perks/benefits-perks/parental-leave.md",
    "benefits-pay-perks/benefits-perks/travel/index.md",
    "company-info-and-process/communication/content_guidelines/style_and_mechanics.md",
    "company-info-and-process/working-at-sourcegraph/teammate-development/index.md",
    "departments/engineering/dev/process/incidents/playbooks/index.md",
    "departments/legal/process/ContractReviewandSignatureAuthorityPolicy.md",
    "departments/people-talent/index.md",
    "departments/people-talent/talent/process/types_of_interviews.md",
    "departments/technical-success/support/process/ce-faq.md",
]

NITEO = [  # teamniteo/handbook @ main, files under numbered dirs
    "2_Operations/how-we-work.md",
    "2_Operations/security.md",
    "2_Operations/user-stories.md",
    "2_Operations/work-process.md",
    "4_Marketing-Support/support.md",
    "5_People/benefits.md",
    "5_People/career.md",
    "5_People/catchups.md",
    "5_People/hiring.md",
    "5_People/onboarding.md",
    "5_People/personal-finances.md",
    "5_People/profit-sharing.md",
]

COMPANY_SOURCES = [
    # (prefix, repo, branch, path-prefix inside repo, file list)
    ("basecamp", "basecamp/handbook", "master", "", BASECAMP),
    ("posthog", "PostHog/posthog.com", "master", "contents/handbook/", POSTHOG),
    ("sourcegraph", "sourcegraph/handbook", "main", "content/", SOURCEGRAPH),
    ("niteo", "teamniteo/handbook", "main", "", NITEO),
]

_FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_SHORTCODE = re.compile(r"\{\{[<%].*?[>%]\}\}", re.DOTALL)
_IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_BLANKS = re.compile(r"\n{3,}")
# MDX (PostHog) ships JSX alongside markdown: strip module lines and
# component tags, keeping the text between them.
_MDX_MODULE = re.compile(r"^(?:import|export)\s.*$", re.MULTILINE)
_JSX_TAG = re.compile(r"</?[A-Z][A-Za-z0-9]*[^>]*/?>", re.DOTALL)


def clean(md: str) -> str:
    md = _FRONTMATTER.sub("", md)
    md = _HTML_COMMENT.sub("", md)
    md = _SHORTCODE.sub("", md)
    md = _MDX_MODULE.sub("", md)
    md = _JSX_TAG.sub("", md)
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


def _save(text: str, name: str, label: str) -> bool:
    words = len(text.split())
    if words < MIN_WORDS:
        print(f"  skip ({words} words)  {label}")
        return False
    (OUT_DIR / name).write_text(text, encoding="utf-8")
    print(f"  saved {words:>6} words  {name}")
    return True


def _github_name(prefix: str, path: str) -> str:
    """basecamp + how-we-work.md -> basecamp_how-we-work.md; index files
    take their parent directory's name (people/hiring-process/index.mdx
    -> posthog_hiring-process.md)."""
    parts = path.rsplit(".", 1)[0].split("/")
    if parts[-1] == "index":
        parts.pop()
    stem = parts[-1].lower()
    return f"{prefix}_{stem}.md"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    saved, skipped = 0, 0
    with httpx.Client(timeout=30.0) as client:
        print("== GitLab handbook")
        for section in SECTIONS:
            raw = fetch_section(client, section)
            if raw is None:
                print(f"  skip (not found)   {section}")
                skipped += 1
                continue
            name = "gitlab_" + section.replace("/", "_") + ".md"
            if _save(clean(raw), name, section):
                saved += 1
            else:
                skipped += 1
        for prefix, repo, branch, subdir, files in COMPANY_SOURCES:
            print(f"== {prefix} handbook")
            for path in files:
                url = f"{GITHUB_RAW}/{repo}/{branch}/{subdir}{path}"
                r = client.get(url, follow_redirects=True)
                if r.status_code != 200:
                    print(f"  skip (HTTP {r.status_code})  {path}")
                    skipped += 1
                    continue
                if _save(clean(r.text), _github_name(prefix, path), path):
                    saved += 1
                else:
                    skipped += 1
    print(f"\ndone: {saved} pages saved to {OUT_DIR}, {skipped} skipped")


if __name__ == "__main__":
    main()
