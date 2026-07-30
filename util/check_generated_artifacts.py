#!/usr/bin/env python3
"""Verify that the generated registry artifacts agree with the registry YAML.

`registry/kgs.yml` is the build's source of truth, but the site serves several
derived files alongside it. If one of those is regenerated and then not
committed, nothing breaks loudly -- the site just keeps serving the stale copy.
That is exactly how the home page silently froze: `registry/kgs-summary.json`
is what the resource browser fetches (see assets/js/registry-data.js), it was
missing from the `git add` list in .github/workflows/update-registry.yml, and
the table showed a two-week-old registry while kgs.yml and kgs.jsonld were
perfectly current.

This runs after `make all` and fails the build if a derived artifact is absent
or out of sync, so that class of drift cannot go unnoticed again.

Run with: ``python util/check_generated_artifacts.py``.
"""

from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent.resolve()

REGISTRY_YAML = Path("registry/kgs.yml")
SUMMARY_JSON = Path("registry/kgs-summary.json")

# Derived files that `make all` produces and the site serves. Every one of
# these must exist and be staged by the update-registry workflow; add new
# `make all` targets here as they are introduced.
REQUIRED_ARTIFACTS = [
    REGISTRY_YAML,
    SUMMARY_JSON,
    Path("registry/kgs.jsonld"),
    Path("registry/kgs.ttl"),
    Path("registry/organizations.yml"),
    Path("registry/taxon_mapping.yaml"),
    Path("registry/parquet-downloads.html"),
    Path("_config.yml"),
]

# How many resources have to be present before an empty/tiny summary is
# obviously a generation failure rather than a legitimately small registry.
MIN_EXPECTED_RESOURCES = 1


def _resource_ids(resources) -> set[str]:
    return {r["id"] for r in resources if isinstance(r, dict) and "id" in r}


def check(root: Path) -> list[str]:
    """Return a list of problems; empty means everything is in sync."""
    problems = []

    missing = [p for p in REQUIRED_ARTIFACTS if not (root / p).is_file()]
    for path in missing:
        problems.append(f"{path} is missing -- did `make all` fail partway through?")

    # The rest of the checks need both files, so stop here if either is absent.
    if (root / REGISTRY_YAML) in {root / p for p in missing}:
        return problems
    if (root / SUMMARY_JSON) in {root / p for p in missing}:
        return problems

    with open(root / REGISTRY_YAML, "r") as stream:
        registry = yaml.load(stream, Loader=yaml.SafeLoader)
    with open(root / SUMMARY_JSON, "r") as stream:
        summary = json.load(stream)

    registry_ids = _resource_ids(registry.get("resources", []))
    summary_ids = _resource_ids(summary.get("resources", []))

    if len(registry_ids) < MIN_EXPECTED_RESOURCES:
        problems.append(
            f"{REGISTRY_YAML} contains {len(registry_ids)} resources; "
            "the registry should never be empty."
        )

    only_in_registry = sorted(registry_ids - summary_ids)
    only_in_summary = sorted(summary_ids - registry_ids)

    if only_in_registry or only_in_summary:
        problems.append(
            f"{SUMMARY_JSON} is out of sync with {REGISTRY_YAML} "
            f"({len(registry_ids)} vs {len(summary_ids)} resources). "
            f"Regenerate it with `make {SUMMARY_JSON}` and commit the result."
        )
    for resource_id in only_in_registry[:20]:
        problems.append(f"  missing from the summary: {resource_id}")
    if len(only_in_registry) > 20:
        problems.append(f"  ...and {len(only_in_registry) - 20} more")
    for resource_id in only_in_summary[:20]:
        problems.append(f"  in the summary but not the registry: {resource_id}")
    if len(only_in_summary) > 20:
        problems.append(f"  ...and {len(only_in_summary) - 20} more")

    return problems


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="repository root to check (default: the repo this script lives in)",
    )
    args = parser.parse_args()

    problems = check(args.root)
    if problems:
        print("Generated registry artifacts are out of sync:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print("Generated registry artifacts are in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
