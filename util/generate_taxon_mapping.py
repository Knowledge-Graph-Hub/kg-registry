#!/usr/bin/env python3
"""
Generate taxon hierarchy mapping for use in the web interface.

This script generates a YAML file containing taxon hierarchy mappings
that enable hierarchical filtering on the main page. It takes all unique
taxa from the registry and computes which database taxa are descendants
of the filter taxa.

Usage:
    python scripts/generate_taxon_mapping.py \
        --parquet-dir registry/parquet \
        --output registry/taxon_mapping.yaml
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Set

import yaml

# Try to import oaklib for hierarchical expansion
try:
    from oaklib import get_adapter
    HAS_OAKLIB = True
except ImportError:
    HAS_OAKLIB = False
    print("Warning: oaklib not available, will use static mappings", file=sys.stderr)


def get_all_database_taxa(parquet_dir: str) -> Set[str]:
    """Get all unique taxa from the parquet files."""
    try:
        import duckdb

        conn = duckdb.connect(":memory:")
        parquet_file = os.path.join(parquet_dir, "resource_taxa.parquet")

        if not os.path.exists(parquet_file):
            print(f"Warning: {parquet_file} not found", file=sys.stderr)
            return set()

        result = conn.execute(
            f"SELECT DISTINCT taxon FROM read_parquet('{parquet_file}') WHERE taxon != 'all' ORDER BY taxon"
        ).fetchall()

        conn.close()
        return {row[0] for row in result}
    except Exception as e:
        print(f"Error reading database taxa: {e}", file=sys.stderr)
        return set()


def get_descendants_with_oak(taxon: str) -> Set[str]:
    """Get all descendant taxa using OAK (Ontology Access Kit)."""
    if not HAS_OAKLIB:
        return {taxon}

    try:
        adapter = get_adapter("obo:NCBITaxon")
        descendants = set()

        # Get all descendants including the taxon itself
        for desc in adapter.descendants(taxon, reflexive=True):
            descendants.add(desc)

        return descendants
    except Exception as e:
        print(f"Warning: Could not expand {taxon} with OAK: {e}", file=sys.stderr)
        return {taxon}


def find_matching_taxa(
    filter_taxon: str, database_taxa: Set[str]
) -> List[str]:
    """Find all database taxa that are descendants of the filter taxon."""
    matching = []

    # If OAK is available, use it
    if HAS_OAKLIB:
        try:
            # Use sqlite:obo:ncbitaxon adapter for fast local access to NCBI Taxonomy
            adapter = get_adapter("sqlite:obo:ncbitaxon")

            # Get ancestors of each database taxon
            for db_taxon in database_taxa:
                try:
                    ancestors = set()
                    for anc in adapter.ancestors(db_taxon, reflexive=True):
                        ancestors.add(anc)

                    # Check if filter_taxon is an ancestor of db_taxon
                    if filter_taxon in ancestors or db_taxon == filter_taxon:
                        matching.append(db_taxon)
                except Exception:
                    # If we can't get ancestors, skip this taxon
                    pass

            return sorted(matching)
        except Exception as e:
            print(
                f"Warning: OAK lookup failed, will use simple hierarchical mapping: {e}",
                file=sys.stderr,
            )
            # Fall through to use the simple mapping below

    # Fallback: use simple hardcoded hierarchical mapping for common cases
    # This ensures Mammalia includes human, mouse, rat, etc.
    simple_hierarchy = {
        "NCBITaxon:40674": [  # Mammalia
            "NCBITaxon:40674",
            "NCBITaxon:9606",   # Human
            "NCBITaxon:10090",  # Mouse
            "NCBITaxon:10116",  # Rat
        ]
    }

    if filter_taxon in simple_hierarchy:
        return [t for t in simple_hierarchy[filter_taxon] if t in database_taxa]

    # Exact match only for other taxa
    return [filter_taxon] if filter_taxon in database_taxa else []


def generate_taxon_mapping(
    parquet_dir: str, filter_taxa: List[str] = None
) -> Dict[str, List[str]]:
    """Generate taxon hierarchy mapping.

    Args:
        parquet_dir: Directory containing parquet files
        filter_taxa: List of taxa to filter by (if None, uses defaults)

    Returns:
        Dictionary mapping filter taxa to their descendant database taxa
    """
    # Default filter taxa if not specified
    if filter_taxa is None:
        filter_taxa = [
            "NCBITaxon:9606",    # Human
            "NCBITaxon:10116",   # Rat
            "NCBITaxon:10090",   # Mouse
            "NCBITaxon:6239",    # C. elegans
            "NCBITaxon:7227",    # Fruit fly
            "NCBITaxon:7955",    # Zebrafish
            "NCBITaxon:4932",    # Yeast
            "NCBITaxon:3702",    # A. thaliana
            "NCBITaxon:40674",   # Mammalia
        ]

    # Get all taxa from the database
    database_taxa = get_all_database_taxa(parquet_dir)
    print(f"Found {len(database_taxa)} unique taxa in database", file=sys.stderr)

    # Generate mappings
    mapping = {}
    for filter_taxon in filter_taxa:
        matching_taxa = find_matching_taxa(filter_taxon, database_taxa)
        mapping[filter_taxon] = matching_taxa

        print(
            f"  {filter_taxon}: {len(matching_taxa)} matching taxa",
            file=sys.stderr,
        )

    return mapping


def main():
    parser = argparse.ArgumentParser(
        description="Generate taxon hierarchy mapping for the web interface"
    )
    parser.add_argument(
        "--parquet-dir",
        default="registry/parquet",
        help="Directory containing parquet files (default: registry/parquet)",
    )
    parser.add_argument(
        "--output",
        default="registry/taxon_mapping.yaml",
        help="Output file for taxon mapping (default: registry/taxon_mapping.yaml)",
    )
    parser.add_argument(
        "--filter-taxa",
        nargs="+",
        help="List of taxa to generate mappings for (uses defaults if not specified)",
    )

    args = parser.parse_args()

    # Create output directory if needed
    output_dir = os.path.dirname(args.output) or "."
    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating taxon mapping from {args.parquet_dir}...", file=sys.stderr)

    # Generate mapping
    mapping = generate_taxon_mapping(args.parquet_dir, args.filter_taxa)

    # Write to YAML file
    with open(args.output, "w") as f:
        yaml.dump(
            {"taxon_hierarchy": mapping},
            f,
            default_flow_style=False,
            sort_keys=True,
        )

    print(f"Taxon mapping written to {args.output}", file=sys.stderr)

    # Also print as JSON for reference
    print("\nGenerated mapping (JSON):")
    print(json.dumps(mapping, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
