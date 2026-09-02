#!/usr/bin/env python3
"""Command-line entry point for upstream license inference.

Examples (run from the repository root)::

    # Show what would change, touch nothing
    uv run python util/infer_licenses.py --dry-run

    # Update resource pages and write a full report
    uv run python util/infer_licenses.py --report reports/license-inference.tsv

    # Restrict to a few resources
    uv run python util/infer_licenses.py --dry-run --ids spoke icees-kg

See ``util/license_inference.py`` for the rules.
"""

from __future__ import annotations

import argparse
import pathlib
import sys
from collections import Counter

HERE = pathlib.Path(__file__).parent.resolve()
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common import RESOURCE_DIR, load_frontmatter_files_parallel  # noqa: E402
from license_inference import TIERS, apply_inferred_licenses, write_report  # noqa: E402


def load_resources(resource_dir: pathlib.Path) -> list[dict]:
    """Load the main page of every resource, in ID order.

    Reading a thousand pages one at a time is nearly all of this command's
    runtime, so the pages go through the shared parallel loader.
    """
    pages = sorted(
        directory / f"{directory.name}.md"
        for directory in resource_dir.iterdir()
        if directory.is_dir() and (directory / f"{directory.name}.md").exists()
    )
    loaded = load_frontmatter_files_parallel(pages)
    resources = []
    for page, metadata, _content in sorted(loaded, key=lambda item: item[0]):
        if metadata.get("id") == page.parent.name:
            resources.append(dict(metadata))
    return resources


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Report changes without writing resource pages."
    )
    parser.add_argument(
        "--report", type=pathlib.Path, help="Write a TSV report of every inheriting resource here."
    )
    parser.add_argument("--ids", nargs="*", help="Only process these resource IDs.")
    parser.add_argument(
        "--resource-dir",
        type=pathlib.Path,
        default=RESOURCE_DIR,
        help="Resource directory (default: resource/).",
    )
    args = parser.parse_args(argv)

    objs = load_resources(args.resource_dir)
    summary = apply_inferred_licenses(
        objs, write=not args.dry_run, resource_dir=args.resource_dir, only_ids=args.ids
    )

    rows = summary["rows"]
    print(f"Inheriting resources considered: {len(rows)}")
    status_counts = Counter(row["status"] for row in rows)
    for status in ("declared", "conflict", "inferred", "unresolved", "placeholder", "no-upstream"):
        print(f"  {status:12s} {status_counts.get(status, 0)}")
    tier_counts = Counter(row["inferred_tier"] for row in rows if row["status"] == "inferred")
    if tier_counts:
        print("Inferred tiers:")
        for tier in TIERS:
            if tier_counts.get(tier):
                print(f"  {tier:16s} {tier_counts[tier]}")
    print(f"Inferred licenses set: {len(summary['inferred'])}")
    print(f"Stale inferred licenses removed: {len(summary['removed'])}")
    if summary["refused"]:
        print(f"Pages that could not take an inferred license: {len(summary['refused'])}")
        for resource_id in summary["refused"]:
            print(f"  {resource_id}")
    if args.dry_run:
        changed = [row["resource_id"] for row in rows if row["status"] in ("inferred",)]
        print(f"Dry run: {len(changed)} page(s) would carry an inferred license")
    else:
        print(f"Resource pages written: {len(summary['written'])}")
        for resource_id in summary["written"]:
            print(f"  {resource_id}")

    if args.report:
        write_report(rows, args.report)
        print(f"Report written to {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
