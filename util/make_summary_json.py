#!/usr/bin/env python3
"""Generate a slim summary JSON from the registry YAML.

The main page table (assets/js/custom.js) only needs a handful of fields
per resource, so serving it the full kgs.jsonld (~30 MB) makes the page
slow to load. This emits registry/kgs-summary.json containing just those
fields, minified, writing the result to STDOUT.
"""

import json
from argparse import ArgumentParser

import yaml

# Fields used by the main page table, filters, and search
SUMMARY_FIELDS = [
    "id",
    "name",
    "description",
    "category",
    "domains",
    "domain",  # legacy field name, still handled by custom.js
    "collection",
    "taxon",
    "activity_status",
    "evaluation_page",
    "homepage_url",
    "is_obsolete",
]

# Only these license subfields are rendered in the table
LICENSE_FIELDS = ["id", "label", "logo"]


def summarize(resource):
    summary = {k: resource[k] for k in SUMMARY_FIELDS if k in resource}

    license_data = resource.get("license")
    if isinstance(license_data, dict):
        summary["license"] = {
            k: license_data[k] for k in LICENSE_FIELDS if k in license_data
        }

    # The table only links to the first publication
    publications = resource.get("publications")
    if isinstance(publications, list) and publications:
        first = publications[0]
        if isinstance(first, dict) and "id" in first:
            summary["publications"] = [{"id": first["id"]}]

    return summary


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("yaml_file", type=str, help="registry YAML file (kgs.yml)")
    args = parser.parse_args()

    with open(args.yaml_file, "r") as stream:
        data = yaml.load(stream, Loader=yaml.SafeLoader)

    summary = {"resources": [summarize(r) for r in data.get("resources", [])]}
    print(json.dumps(summary, sort_keys=True, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
