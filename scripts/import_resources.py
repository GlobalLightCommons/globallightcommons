#!/usr/bin/env python3

from __future__ import annotations

import html
import re
import shutil
import time
from pathlib import Path
from urllib.parse import quote

import requests
from playwright.sync_api import sync_playwright


SOURCE_URL = "https://globallightcommons.org/resources"

OUTPUT_FILE = Path(
    "/Users/nataliapetliak/projects/globallightcommons/"
    "_bibliography/references.bib"
)

TABS = {
    "Preprints": "preprint",
    "Research Articles": "article",
    "Software": "software",
    "Related Projects": "project",
}


# ============================================================
# TEXT / BIBTEX HELPERS
# ============================================================

def clean_text(value: str | None) -> str:
    if not value:
        return ""

    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def bibtex_escape(value: str) -> str:
    """
    Escape characters that commonly break BibTeX.
    Keep Unicode characters because bibtex-ruby/Jekyll Scholar
    handle UTF-8 fine.
    """
    value = clean_text(value)

    replacements = {
        "\\": r"\\",
        "{": r"\{",
        "}": r"\}",
        "%": r"\%",
        "#": r"\#",
    }

    for old, new in replacements.items():
        value = value.replace(old, new)

    return value


def make_key(title: str, index: int) -> str:
    """
    Produce stable-ish readable keys from titles.
    """
    words = re.findall(r"[A-Za-z0-9]+", title.lower())

    ignored = {
        "the", "a", "an", "and", "or", "of", "in",
        "on", "for", "to", "with", "from"
    }

    words = [word for word in words if word not in ignored]

    base = "-".join(words[:6]) or f"resource-{index}"

    return f"{base}-{index}"


# ============================================================
# METADATA ENRICHMENT
# ============================================================

def extract_doi(url: str) -> str | None:
    """
    Detect DOI embedded in URLs, including bioRxiv links.
    """

    decoded = requests.utils.unquote(url)

    match = re.search(
        r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)",
        decoded,
        flags=re.IGNORECASE,
    )

    if not match:
        return None

    doi = match.group(1)

    # Remove common URL suffixes after a DOI.
    doi = re.sub(
        r"(?:\.full(?:\.pdf)?|\.abstract|\.figures-only)$",
        "",
        doi,
        flags=re.IGNORECASE,
    )

    # bioRxiv version markers are not part of the DOI itself
    doi = re.sub(r"v\d+$", "", doi)

    return doi.rstrip(".,;)")


def crossref_metadata(doi: str) -> dict:
    """
    Try to enrich scraped records with authors/year/etc.
    If Crossref has nothing, silently return an empty dict.
    """

    url = f"https://api.crossref.org/works/{quote(doi, safe='')}"

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent":
                    "GLC-Jekyll-Migration/1.0 "
                    "(https://globallightcommons.org)"
            },
        )

        if response.status_code != 200:
            return {}

        message = response.json()["message"]

        result = {}

        # Title
        titles = message.get("title") or []
        if titles:
            result["title"] = clean_text(titles[0])

        # Authors
        authors = []

        for author in message.get("author", []):
            family = clean_text(author.get("family"))
            given = clean_text(author.get("given"))

            if family and given:
                authors.append(f"{family}, {given}")
            elif family:
                authors.append(family)

        if authors:
            result["author"] = " and ".join(authors)

        # Year
        date_fields = [
            message.get("published"),
            message.get("published-print"),
            message.get("published-online"),
            message.get("created"),
        ]

        for field in date_fields:
            if not field:
                continue

            parts = field.get("date-parts", [])

            if parts and parts[0]:
                result["year"] = str(parts[0][0])
                break

        # Journal / container
        container = message.get("container-title") or []

        if container:
            result["journal"] = clean_text(container[0])

        return result

    except Exception as exc:
        print(f"  Crossref lookup failed for {doi}: {exc}")
        return {}


# ============================================================
# PAGE SCRAPING
# ============================================================

def find_card_for_link(link):
    """
    Starting from a resource CTA link, walk upward until we find
    the surrounding card/container that includes a heading.
    """

    return link.evaluate_handle(
        """
        (link) => {
          let node = link;

          for (let i = 0; i < 12 && node; i++, node = node.parentElement) {
            if (!node) break;

            const heading = node.querySelector("h1, h2, h3, h4");
            const text = (node.innerText || "").trim();

            if (
              heading &&
              text.length > 20 &&
              text.length < 5000
            ) {
              return node;
            }
          }

          return link.parentElement;
        }
        """
    )


def scrape_visible_resources(page, resource_type: str) -> list[dict]:
    """
    Extract cards currently visible after selecting one tab.
    """

    resources = []

    links = page.locator("main a[href]")

    for i in range(links.count()):
        link = links.nth(i)

        try:
            if not link.is_visible():
                continue

            href = link.get_attribute("href") or ""
            link_text = clean_text(link.inner_text())

            if not href:
                continue

            # Ignore normal site navigation.
            if href.startswith("/") or href.startswith("#"):
                continue

            # Resource CTAs on the original page are things like:
            # View on bioRxiv, Visit website, View project, etc.
            if not re.search(
                r"\b(view|visit|learn|github|website|project|software|biorxiv|doi)\b",
                link_text,
                flags=re.IGNORECASE,
            ):
                continue

            card_handle = find_card_for_link(link)

            data = card_handle.evaluate(
                """
                (card) => {
                  const heading = card.querySelector("h1, h2, h3, h4");

                  const paragraphs = Array.from(
                    card.querySelectorAll("p")
                  )
                    .map(p => (p.innerText || "").trim())
                    .filter(Boolean);

                  return {
                    title: heading ? heading.innerText.trim() : "",
                    paragraphs: paragraphs,
                    text: (card.innerText || "").trim()
                  };
                }
                """
            )

            title = clean_text(data.get("title"))

            if not title:
                continue

            paragraphs = [
                clean_text(p)
                for p in data.get("paragraphs", [])
                if clean_text(p)
            ]

            # Pick the longest paragraph as the descriptive summary.
            summary = max(paragraphs, key=len) if paragraphs else ""

            resources.append(
                {
                    "title": title,
                    "summary": summary,
                    "url": href,
                    "resource_type": resource_type,
                    "link_text": link_text,
                }
            )

        except Exception:
            # One unusual DOM item should not break the migration.
            continue

    # Deduplicate by title + URL.
    unique = {}

    for item in resources:
        unique[(item["title"], item["url"])] = item

    return list(unique.values())


def scrape_all() -> list[dict]:
    all_resources = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            viewport={
                "width": 1600,
                "height": 1000,
            }
        )

        print(f"Opening {SOURCE_URL}")
        page.goto(
            SOURCE_URL,
            wait_until="networkidle",
            timeout=60_000,
        )

        for tab_name, resource_type in TABS.items():
            print(f"\nScraping: {tab_name}")

            # Find either a button or another clickable element
            # containing the exact tab label.
            tab = page.get_by_text(
                tab_name,
                exact=True,
            ).first

            try:
                tab.click()
                page.wait_for_timeout(700)
            except Exception as exc:
                print(f"  Could not click tab: {exc}")
                continue

            entries = scrape_visible_resources(
                page,
                resource_type,
            )

            print(f"  Found {len(entries)} entries.")

            all_resources.extend(entries)

        browser.close()

    # Final dedupe in case cards remain mounted across tab switches.
    unique = {}

    for item in all_resources:
        key = (
            item["resource_type"],
            item["title"],
            item["url"],
        )
        unique[key] = item

    return list(unique.values())


# ============================================================
# BIBTEX WRITING
# ============================================================

def record_to_bibtex(record: dict, index: int) -> str:
    title = record["title"]
    url = record["url"]
    summary = record["summary"]
    resource_type = record["resource_type"]

    doi = extract_doi(url)

    metadata = {}

    if doi:
        print(f"  Looking up DOI metadata: {doi}")
        metadata = crossref_metadata(doi)

    # Prefer authoritative metadata when available.
    final_title = metadata.get("title") or title
    year = metadata.get("year", "")
    author = metadata.get("author", "")
    journal = metadata.get("journal", "")

    key = make_key(final_title, index)

    # @misc works for all four categories and allows
    # resource_type to control Jekyll display filtering.
    fields = [
        ("title", final_title),
    ]

    if author:
        fields.append(("author", author))

    if year:
        fields.append(("year", year))

    if journal:
        fields.append(("journal", journal))

    if doi:
        fields.append(("doi", doi))

    fields.extend(
        [
            ("url", url),
            ("resource_type", resource_type),
        ]
    )

    if summary:
        fields.append(("summary", summary))

    lines = [f"@misc{{{key},"]

    for n, (field, value) in enumerate(fields):
        comma = "," if n < len(fields) - 1 else ""
        lines.append(
            f"  {field} = {{{bibtex_escape(value)}}}{comma}"
        )

    lines.append("}")

    return "\n".join(lines)


def write_bibliography(records: list[dict]) -> None:
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    if OUTPUT_FILE.exists():
        backup = OUTPUT_FILE.with_suffix(".bib.backup")

        shutil.copy2(
            OUTPUT_FILE,
            backup,
        )

        print(f"\nBacked up existing bibliography to:")
        print(f"  {backup}")

    records.sort(
        key=lambda item: (
            list(TABS.values()).index(item["resource_type"]),
            item["title"].lower(),
        )
    )

    blocks = [
        "# Automatically migrated from:",
        f"# {SOURCE_URL}",
        "#",
        "# Edit this file after migration if bibliographic metadata",
        "# needs manual correction.",
        "",
    ]

    for index, record in enumerate(records, start=1):
        blocks.append(record_to_bibtex(record, index))
        blocks.append("")

    OUTPUT_FILE.write_text(
        "\n".join(blocks),
        encoding="utf-8",
    )

    print("\n========================================")
    print(f"Wrote {len(records)} resources to:")
    print(OUTPUT_FILE)
    print("========================================")


# ============================================================
# MAIN
# ============================================================

def main():
    records = scrape_all()

    if not records:
        raise RuntimeError(
            "No resources were found. "
            "The original website DOM may have changed."
        )

    print("\nResources found:")

    for record in records:
        print(
            f"  [{record['resource_type']}] "
            f"{record['title']}"
        )

    write_bibliography(records)


if __name__ == "__main__":
    main()