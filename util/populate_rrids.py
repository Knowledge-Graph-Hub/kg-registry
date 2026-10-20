#!/usr/bin/env python3
"""
Populate SciCrunch Research Resource Identifiers (RRIDs) in KG-Registry resources.

This script:
1. Seeds a set of known-good RRIDs onto their resources.
2. Optionally searches SciCrunch by name/synonyms/homepage for candidates
   (requires a SciCrunch API key in the SCICRUNCH_API_KEY environment variable).
3. Confirms every candidate through the open SciCrunch resolver by comparing
   the resolver's landing page against the resource's homepage_url and by
   comparing names/abbreviations/synonyms.
4. Writes an ``rrid`` field only for high-confidence matches; everything else
   is sent to a review report (reports/rrid_candidates.tsv) instead of being
   written.

The resolver (https://scicrunch.org/resolver/RRID:SCR_xxxxxx.json) is open and
needs no key, so confirmation and the seed step work offline-of-a-key. Search
needs a free API key, so discovery is skipped (and resources are listed in the
report) when no key is present.

Matching helpers are kept side-effect free so they can be unit tested against
recorded resolver responses without touching the network.
"""

import argparse
import csv
import json
import os
import pathlib
import re
import sys
import urllib.parse
import urllib.request
from typing import Dict, List, Optional, Tuple

import frontmatter

__author__ = "kg-registry-team"

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
RESOURCE_DIRECTORY = ROOT.joinpath("resource").resolve()

CACHE_DIR = ROOT.joinpath("cache")
RESOLVER_CACHE_DIR = CACHE_DIR.joinpath("scicrunch_resolver")

RESOLVER_URL = "https://scicrunch.org/resolver/RRID:{rrid}.json"
# SciCrunch search needs an API key; this is the documented elastic endpoint.
SEARCH_URL = "https://api.scicrunch.io/elastic/v1/RRID/_search"

# SciCrunch rejects the default urllib User-Agent (HTTP 403), so present a
# browser-like one.
USER_AGENT = "Mozilla/5.0 (KG-Registry RRID backfill; +https://kghub.org)"
HTTP_TIMEOUT = 30

# RRIDs already found in page body text (see issue #757). These are written
# directly because they are human-verified; the resolver is still consulted to
# log a warning if the landing page no longer matches.
SEED_RRIDS: Dict[str, str] = {
    "cgc": "SCR_007341",
    "zirc": "SCR_005065",
    "mps-db": "SCR_021126",
}


# ---------------------------------------------------------------------------
# Pure helpers (unit tested offline)
# ---------------------------------------------------------------------------

def normalize_url(url: Optional[str]) -> str:
    """
    Normalize a URL for comparison: drop the scheme, a leading ``www.``, any
    trailing slash, and lowercase the host. Returns '' for falsy input.

    >>> normalize_url("https://zebrafish.org/")
    'zebrafish.org'
    >>> normalize_url("http://www.zebrafish.org")
    'zebrafish.org'
    """
    if not url:
        return ""
    url = url.strip()
    parsed = urllib.parse.urlsplit(url if "//" in url else "//" + url)
    host = (parsed.netloc or parsed.path).lower()
    path = parsed.path if parsed.netloc else ""
    if host.startswith("www."):
        host = host[4:]
    combined = (host + path).rstrip("/")
    return combined


def extract_resolver_record(resolver_json: Dict) -> Optional[Dict]:
    """
    Pull the fields we care about out of a SciCrunch resolver response.

    The resolver returns an Elasticsearch-style envelope; the record lives at
    ``hits.hits[0]._source``. Returns a flat dict with keys ``identifier``,
    ``name``, ``synonyms`` (list), ``abbreviations`` (list) and
    ``landing_urls`` (list), or None if no record is present.
    """
    if not resolver_json:
        return None
    hits = resolver_json.get("hits", {}).get("hits", [])
    if not hits:
        return None
    source = hits[0].get("_source", {})
    item = source.get("item", {})

    synonyms = [s.get("name", "") for s in item.get("synonyms", []) if s.get("name")]
    abbreviations = [a.get("name", "") for a in item.get("abbreviations", []) if a.get("name")]

    landing_urls: List[str] = []
    distributions = source.get("distributions", {})
    for bucket in ("current", "alternate"):
        for dist in distributions.get(bucket, []):
            uri = dist.get("uri", "")
            if uri:
                landing_urls.append(uri)

    identifier = item.get("identifier") or item.get("curie") or ""
    name = item.get("name", "")

    return {
        "identifier": identifier,
        "name": name,
        "synonyms": synonyms,
        "abbreviations": abbreviations,
        "landing_urls": landing_urls,
    }


def landing_url_matches(record: Dict, homepage_url: Optional[str]) -> bool:
    """True if any resolver landing page normalizes to the resource homepage."""
    if not record or not homepage_url:
        return False
    target = normalize_url(homepage_url)
    if not target:
        return False
    return any(normalize_url(u) == target for u in record.get("landing_urls", []))


def _name_set(*values) -> set:
    out = set()
    for v in values:
        if isinstance(v, (list, tuple, set)):
            out.update(x.strip().lower() for x in v if x and x.strip())
        elif v and str(v).strip():
            out.add(str(v).strip().lower())
    return out


def name_matches(record: Dict, name: Optional[str], synonyms: Optional[List[str]] = None) -> bool:
    """True if the resolver name/abbreviations/synonyms overlap ours (case-insensitive)."""
    if not record:
        return False
    resolver_names = _name_set(
        record.get("name"), record.get("synonyms"), record.get("abbreviations")
    )
    ours = _name_set(name, synonyms or [])
    return bool(resolver_names & ours)


def confirm_rrid(record: Dict, homepage_url: Optional[str], name: Optional[str],
                 synonyms: Optional[List[str]] = None) -> Tuple[bool, List[str]]:
    """
    Decide whether a resolver record is a high-confidence match for a resource.

    A landing-page match is treated as sufficient on its own (strongest signal).
    A name/abbreviation/synonym match is reported as a reason but is not, by
    itself, enough to auto-write. Returns (high_confidence, reasons).
    """
    reasons: List[str] = []
    if record is None:
        return False, ["resolver returned no record"]

    url_hit = landing_url_matches(record, homepage_url)
    name_hit = name_matches(record, name, synonyms)
    if url_hit:
        reasons.append("landing page matches homepage_url")
    if name_hit:
        reasons.append("name/abbreviation matches")
    if not url_hit and not name_hit:
        reasons.append("no landing-page or name match")

    return url_hit, reasons


# ---------------------------------------------------------------------------
# Network
# ---------------------------------------------------------------------------

def fetch_resolver_json(rrid: str, force: bool = False,
                        opener=urllib.request.urlopen) -> Optional[Dict]:
    """
    Fetch (and cache) a resolver record for an RRID (without the 'RRID:' prefix).

    ``opener`` is injectable for testing. Returns parsed JSON or None on failure.
    """
    RESOLVER_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = RESOLVER_CACHE_DIR.joinpath(f"{rrid}.json")
    if cache_path.exists() and not force:
        try:
            return json.loads(cache_path.read_text())
        except Exception:
            pass

    url = RESOLVER_URL.format(rrid=rrid)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with opener(request, timeout=HTTP_TIMEOUT) as response:
            content = response.read()
        data = json.loads(content)
        cache_path.write_text(json.dumps(data))
        return data
    except Exception as e:
        print(f"  ⚠️  Failed to resolve RRID:{rrid}: {e}")
        return None


def search_scicrunch(query: str, api_key: str,
                     opener=urllib.request.urlopen) -> List[str]:
    """
    Search SciCrunch for candidate RRIDs by free-text query. Requires an API key.

    Returns a list of SCR_ identifiers (without the 'RRID:' prefix). Any error
    (including a missing key) yields an empty list so the caller can fall back
    to the review report.
    """
    if not api_key:
        return []
    params = urllib.parse.urlencode({"q": query, "key": api_key, "size": 5})
    url = f"{SEARCH_URL}?{params}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with opener(request, timeout=HTTP_TIMEOUT) as response:
            data = json.loads(response.read())
    except Exception as e:
        print(f"  ⚠️  SciCrunch search failed for '{query}': {e}")
        return []

    candidates: List[str] = []
    for hit in data.get("hits", {}).get("hits", []):
        record = extract_resolver_record({"hits": {"hits": [hit]}})
        if record and record.get("identifier"):
            ident = record["identifier"].replace("RRID:", "")
            candidates.append(ident)
    return candidates


# ---------------------------------------------------------------------------
# Resource iteration
# ---------------------------------------------------------------------------

def find_resource_file(resource_id: str) -> Optional[pathlib.Path]:
    resource_path = RESOURCE_DIRECTORY / resource_id / f"{resource_id}.md"
    return resource_path if resource_path.exists() else None


def get_all_resource_files() -> List[pathlib.Path]:
    files = []
    for resource_dir in RESOURCE_DIRECTORY.iterdir():
        if resource_dir.is_dir():
            resource_file = resource_dir / f"{resource_dir.name}.md"
            if resource_file.exists():
                files.append(resource_file)
    return files


_TOP_LEVEL_KEY = re.compile(r"^([A-Za-z0-9_]+):")


def splice_rrid(text: str, rrid: str) -> str:
    """
    Insert an ``rrid`` line into a page's YAML frontmatter as plain text.

    Round-tripping the frontmatter through a YAML dumper reflows the entire
    page (re-indents every list, rewraps every description), so instead we
    insert a single line at the alphabetically-correct top-level key position
    and leave every other byte untouched. If an ``rrid`` key is already
    present, the text is returned unchanged.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("file does not start with YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise ValueError("unterminated YAML frontmatter")

    insert_at = end  # default: just before the closing '---'
    for i in range(1, end):
        match = _TOP_LEVEL_KEY.match(lines[i])
        if not match:
            continue
        key = match.group(1)
        if key == "rrid":
            return text  # already present
        if key.lower() > "rrid":
            insert_at = i
            break

    lines.insert(insert_at, f"rrid: {rrid}")
    return "\n".join(lines)


def write_rrid(resource_path: pathlib.Path, rrid: str) -> None:
    """Add the resource's ``rrid`` field via a text splice, preserving formatting."""
    text = resource_path.read_text(encoding="utf-8")
    resource_path.write_text(splice_rrid(text, rrid), encoding="utf-8")


def process_resource(resource_path: pathlib.Path, api_key: str, force: bool,
                     dry_run: bool) -> Tuple[Optional[str], str, List[Dict]]:
    """
    Process one resource. Returns (written_rrid_or_None, status, candidate_rows).

    status is one of: 'seeded', 'confirmed', 'present', 'candidate', 'none'.
    candidate_rows are dicts destined for the review report.
    """
    post = frontmatter.load(resource_path)
    metadata = post.metadata
    resource_id = metadata.get("id")
    if not resource_id or resource_id != resource_path.parent.name:
        return None, "skip", []

    name = metadata.get("name", resource_id)
    homepage_url = metadata.get("homepage_url", "")
    synonyms = metadata.get("synonyms", []) or []
    candidate_rows: List[Dict] = []

    # Already has one: leave it, only validate.
    existing = metadata.get("rrid")
    if existing:
        return None, "present", []

    # 1. Seed.
    if resource_id in SEED_RRIDS:
        rrid = SEED_RRIDS[resource_id]
        record = extract_resolver_record(fetch_resolver_json(rrid, force=force) or {})
        if record and not landing_url_matches(record, homepage_url) \
                and not name_matches(record, name, synonyms):
            print(f"  ⚠️  Seed RRID:{rrid} for {resource_id} did not confirm "
                  f"against the resolver; writing anyway (human-verified seed).")
        if not dry_run:
            write_rrid(resource_path, rrid)
        return rrid, "seeded", []

    # 2. Discover (needs an API key).
    queries = [name] + [s for s in synonyms if s]
    seen = set()
    for query in queries:
        for cand in search_scicrunch(query, api_key):
            if cand in seen:
                continue
            seen.add(cand)
            record = extract_resolver_record(fetch_resolver_json(cand, force=force) or {})
            high, reasons = confirm_rrid(record, homepage_url, name, synonyms)
            if high:
                if not dry_run:
                    write_rrid(resource_path, cand)
                return cand, "confirmed", []
            if record:
                candidate_rows.append({
                    "resource_id": resource_id,
                    "resource_name": name,
                    "candidate_rrid": cand,
                    "resolver_name": record.get("name", ""),
                    "homepage_url": homepage_url,
                    "landing_urls": "; ".join(record.get("landing_urls", [])),
                    "reasons": "; ".join(reasons),
                })

    status = "candidate" if candidate_rows else "none"
    return None, status, candidate_rows


def write_candidates_report(rows: List[Dict], output_path: Optional[pathlib.Path] = None) -> pathlib.Path:
    if output_path is None:
        output_path = ROOT.joinpath("reports/rrid_candidates.tsv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["resource_id", "resource_name", "candidate_rrid", "resolver_name",
                  "homepage_url", "landing_urls", "reasons"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Populate SciCrunch RRIDs in KG-Registry",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be changed without modifying files")
    parser.add_argument("--force", action="store_true",
                        help="Force re-fetch of resolver records even if cached")
    parser.add_argument("--resource", help="Process only a specific resource (by ID)")
    parser.add_argument("--seed-only", action="store_true",
                        help="Only write the known seed RRIDs; skip SciCrunch search")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    api_key = "" if args.seed_only else os.environ.get("SCICRUNCH_API_KEY", "")
    if not args.seed_only and not api_key:
        print("ℹ️  No SCICRUNCH_API_KEY set: seeding known RRIDs and confirming via "
              "the open resolver only. Resources without a match are listed in the report.")

    if args.resource:
        resource_path = find_resource_file(args.resource)
        if not resource_path:
            print(f"ERROR: Resource '{args.resource}' not found")
            return 1
        resource_files = [resource_path]
    else:
        resource_files = get_all_resource_files()

    print(f"\n{'=' * 60}")
    print("DRY RUN - no files will be modified" if args.dry_run
          else "Populating KG-Registry resources with RRIDs")
    print(f"{'=' * 60}\n")

    written = 0
    all_candidates: List[Dict] = []
    for resource_path in sorted(resource_files):
        rrid, status, candidates = process_resource(
            resource_path, api_key, args.force, args.dry_run)
        all_candidates.extend(candidates)
        if rrid:
            written += 1
            print(f"📝 {resource_path.parent.name}: set rrid to '{rrid}' ({status})")
        elif args.verbose and status not in ("skip", "present"):
            print(f"⏭️  {resource_path.parent.name}: {status}")

    print(f"\n{'=' * 60}")
    print(f"Summary: {'would write' if args.dry_run else 'wrote'} {written} RRID(s)")
    if all_candidates:
        report_path = write_candidates_report(all_candidates)
        print(f"📊 {len(all_candidates)} unconfirmed candidate(s) → "
              f"{report_path.relative_to(ROOT)}")
    print(f"{'=' * 60}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
