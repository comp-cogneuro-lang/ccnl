"""
propose new publications from ORCID for review

compares the works on the ORCID record in _config.yaml (links.orcid) against
the curated list in _data/sources.yaml and the skip list in
_data/candidates-ignore.yaml. works not found in either are appended to the
end of sources.yaml for review. nothing is published until a person reviews
the change (the weekly workflow opens a pull request).

usage: python _cite/orcid_candidates.py [--dry-run]
"""

import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

root = Path(__file__).resolve().parent.parent
config_file = root / "_config.yaml"
sources_file = root / "_data" / "sources.yaml"
ignore_file = root / "_data" / "candidates-ignore.yaml"


def load_yaml(path):
    if not path.exists():
        return None
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def norm_doi(doi):
    doi = str(doi or "").strip().lower()
    doi = re.sub(r"^(doi:|https?://(dx\.)?doi\.org/)", "", doi)
    return doi


def norm_title(title):
    return re.sub(r"[^a-z0-9]+", " ", str(title or "").lower()).strip()


def known_keys(entries):
    """dois and normalized titles of entries in a sources-style list"""
    dois, titles = set(), set()
    for entry in entries or []:
        if not isinstance(entry, dict):
            continue
        _id = str(entry.get("id", ""))
        if _id.lower().startswith("doi:"):
            dois.add(norm_doi(_id))
        if entry.get("doi"):
            dois.add(norm_doi(entry["doi"]))
        if entry.get("title"):
            titles.add(norm_title(entry["title"]))
    return dois, titles


def orcid_works(orcid):
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    request = Request(url=url, headers={"Accept": "application/json"})
    response = json.loads(urlopen(request, timeout=60).read())
    works = []
    for group in response.get("group", []):
        summaries = group.get("work-summary", []) or []
        if not summaries:
            continue
        summary = summaries[0]
        title = ((summary.get("title") or {}).get("title") or {}).get("value", "")
        year = ((summary.get("publication-date") or {}).get("year") or {}) or {}
        year = year.get("value", "") if isinstance(year, dict) else ""
        work_type = summary.get("type", "")
        doi = ""
        for external in (group.get("external-ids") or {}).get("external-id", []):
            if external.get("external-id-type") == "doi":
                doi = norm_doi(external.get("external-id-value", ""))
                break
        works.append({"doi": doi, "title": title, "year": year, "type": work_type})
    return works


def guess_type(orcid_type):
    if orcid_type in ["book-chapter", "book", "encyclopedia-entry"]:
        return "chapter"
    if orcid_type in ["conference-paper", "conference-abstract"]:
        return "proceedings"
    return "article"


def main():
    dry_run = "--dry-run" in sys.argv

    config = load_yaml(config_file) or {}
    orcid = str((config.get("links") or {}).get("orcid", "")).strip()
    if not orcid:
        print("No links.orcid in _config.yaml; nothing to do")
        return

    sources = load_yaml(sources_file) or []
    ignore = load_yaml(ignore_file) or []
    source_dois, source_titles = known_keys(sources)
    ignore_dois, ignore_titles = known_keys(ignore)
    seen_dois = source_dois | ignore_dois
    seen_titles = source_titles | ignore_titles

    candidates = []
    for work in orcid_works(orcid):
        if work["doi"] and work["doi"] in seen_dois:
            continue
        if norm_title(work["title"]) in seen_titles:
            continue
        candidates.append(work)

    if not candidates:
        print("No new ORCID works to propose")
        return

    lines = ["", "# ---- ORCID candidates: review, edit or delete, then merge ----"]
    for work in candidates:
        label = f"{work['title']} ({work['year'] or 'no year'})".replace("\n", " ")
        if work["doi"]:
            lines += [
                f"# ORCID candidate: {label}",
                f"- id: doi:{work['doi']}",
                f"  type: {guess_type(work['type'])}",
            ]
        else:
            # no doi: leave commented out, needs manual title/authors/publisher/date
            lines += [
                f"# ORCID candidate without DOI (add manually or add to candidates-ignore.yaml): {label}",
            ]
    text = "\n".join(lines) + "\n"

    print(f"{len(candidates)} new ORCID work(s):")
    print(text)
    if dry_run:
        return

    with sources_file.open("a", encoding="utf-8") as file:
        file.write(text)


if __name__ == "__main__":
    main()
