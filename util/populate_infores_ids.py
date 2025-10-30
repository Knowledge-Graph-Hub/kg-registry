#!/usr/bin/env python3
"""
Populate Information Resource (infores) identifiers in KG-Registry resources and products.

This script:
1. Loads mappings from kgregistry-infores.sssom.tsv 
2. Loads the infores catalog YAML for provenance relationships
3. Updates Resource and Product pages with infores_id fields
4. Translates provenance relationships (consumes/consumed_by) to original_source fields
"""

import argparse
import csv
import pathlib
import sys
import urllib.request
from typing import Dict, List, Tuple, Optional

import frontmatter
import yaml
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

__author__ = "kg-registry-team"

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
RESOURCE_DIRECTORY = ROOT.joinpath("resource").resolve()

# URLs for remote files
SSSOM_MAPPING_URL = "https://raw.githubusercontent.com/matentzn/pks-resource/refs/heads/main/mappings/kgregistry-infores.sssom.tsv"
INFORES_CATALOG_URL = "https://biolink.github.io/information-resource-registry/infores_catalog.yaml"

# Cache file paths
CACHE_DIR = ROOT.joinpath("cache")
SSSOM_CACHE = CACHE_DIR.joinpath("kgregistry-infores.sssom.tsv")
INFORES_CACHE = CACHE_DIR.joinpath("infores_catalog.yaml")


class CustomRuamelYAMLHandler(frontmatter.YAMLHandler):
    """Custom YAML handler for consistent formatting."""

    def __init__(self):
        self.myyaml = YAML()
        self.myyaml.default_flow_style = False
        self.myyaml.allow_duplicate_keys = True
        self.myyaml.indent(mapping=2, sequence=4, offset=2)
        self.myyaml.preserve_quotes = True
        self.myyaml.width = 1500
        super().__init__()

    def load(self, fm, **kwargs):
        return self.myyaml.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        stream = StringIO()
        self.myyaml.dump(data=metadata, stream=stream)
        metadata = stream.getvalue()
        metadata = metadata[:-1]
        return metadata


def download_file(url: str, cache_path: pathlib.Path, force: bool = False) -> pathlib.Path:
    """Download a file and cache it locally."""
    if cache_path.exists() and not force:
        print(f"Using cached file: {cache_path}")
        return cache_path

    print(f"Downloading {url}...")
    cache_path.parent.mkdir(exist_ok=True, parents=True)

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            cache_path.write_bytes(content)
        print(f"Downloaded to {cache_path}")
        return cache_path
    except Exception as e:
        print(f"ERROR: Failed to download {url}: {e}")
        if cache_path.exists():
            print(f"Using cached version from {cache_path}")
            return cache_path
        raise


def load_sssom_mappings(sssom_path: pathlib.Path) -> Dict[str, str]:
    """
    Load SSSOM mappings from TSV file.

    Returns dict mapping kgregistry IDs (without prefix) to infores IDs (without prefix).
    """
    mappings = {}

    with open(sssom_path, 'r') as f:
        # Skip header lines (11 lines starting with #)
        for _ in range(11):
            next(f)

        # Parse TSV
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            kg_id = row['subject_id'].replace('kgregistry:', '')
            infores_id = row['object_id'].replace('infores:', '')
            mappings[kg_id] = infores_id

    print(f"Loaded {len(mappings)} SSSOM mappings")
    return mappings


def load_infores_catalog(catalog_path: pathlib.Path) -> Dict[str, Dict]:
    """
    Load infores catalog YAML.

    Returns dict mapping infores IDs (with prefix) to their metadata including
    consumes and consumed_by relationships.
    """
    with open(catalog_path, 'r') as f:
        catalog_data = yaml.safe_load(f)

    # Build a dictionary keyed by infores ID
    infores_dict = {}
    for resource in catalog_data.get('information_resources', []):
        infores_id = resource.get('id', '')
        infores_dict[infores_id] = resource

    print(f"Loaded {len(infores_dict)} infores catalog entries")
    return infores_dict


def build_reverse_mapping(kgr_to_infores: Dict[str, str]) -> Dict[str, str]:
    """Build reverse mapping from infores IDs to KG-Registry IDs."""
    return {v: k for k, v in kgr_to_infores.items()}


def find_resource_file(resource_id: str) -> pathlib.Path:
    """Find the resource markdown file for a given ID."""
    resource_path = RESOURCE_DIRECTORY / resource_id / f"{resource_id}.md"
    if resource_path.exists():
        return resource_path
    return None


def get_all_resource_files() -> List[pathlib.Path]:
    """Get all resource markdown files."""
    files = []
    for resource_dir in RESOURCE_DIRECTORY.iterdir():
        if resource_dir.is_dir():
            resource_file = resource_dir / f"{resource_dir.name}.md"
            if resource_file.exists():
                files.append(resource_file)
    return files


def update_resource_infores(
    resource_path: pathlib.Path,
    kgr_to_infores: Dict[str, str],
    infores_to_kgr: Dict[str, str],
    infores_catalog: Dict[str, Dict],
    dry_run: bool = False
) -> Tuple[bool, List[str]]:
    """
    Update a single resource file with infores_id.

    Returns (modified, messages) tuple.
    """
    handler = CustomRuamelYAMLHandler()
    post = frontmatter.load(resource_path, handler=handler)
    metadata = post.metadata
    messages = []
    modified = False

    resource_id = metadata.get('id')
    if not resource_id:
        messages.append(f"  ⚠️  No resource ID found in {resource_path}")
        return False, messages

    # Check if this is a resource page (not a product page)
    # Resource pages have the ID matching the parent directory name
    if resource_id != resource_path.parent.name:
        # This is a product page, skip (we'll handle these separately)
        return False, []

    # Update Resource infores_id
    if resource_id in kgr_to_infores:
        infores_id = kgr_to_infores[resource_id]
        current_infores = metadata.get('infores_id')

        if current_infores != infores_id:
            if not dry_run:
                metadata['infores_id'] = infores_id
            modified = True
            messages.append(f"  ✓ {resource_id}: set infores_id to '{infores_id}'")

    # Update products
    products = metadata.get('products', [])
    for product in products:
        product_id = product.get('id', '')
        if not product_id:
            continue

        # Check if product has an infores mapping
        if product_id in kgr_to_infores:
            infores_id = kgr_to_infores[product_id]
            current_infores = product.get('infores_id')

            if current_infores != infores_id:
                if not dry_run:
                    product['infores_id'] = infores_id
                modified = True
                messages.append(f"    • Product {product_id}: set infores_id to '{infores_id}'")

            # Check for provenance relationships in infores catalog
            infores_full_id = f"infores:{infores_id}"
            if infores_full_id in infores_catalog:
                infores_entry = infores_catalog[infores_full_id]
                consumes = infores_entry.get('consumes', [])

                if consumes:
                    # Translate infores IDs to KG-Registry resource IDs
                    original_sources = []
                    for consumed_infores in consumes:
                        # Strip prefix
                        consumed_id = consumed_infores.replace('infores:', '')
                        if consumed_id in infores_to_kgr:
                            original_sources.append(infores_to_kgr[consumed_id])

                    if original_sources:
                        current_sources = product.get('original_source', [])
                        # Merge with existing sources (avoid duplicates)
                        if not current_sources:
                            current_sources = []
                        merged_sources = list(set(current_sources + original_sources))
                        merged_sources.sort()

                        if merged_sources != current_sources:
                            if not dry_run:
                                product['original_source'] = merged_sources
                            modified = True
                            new_sources = set(merged_sources) - set(current_sources)
                            if new_sources:
                                messages.append(
                                    f"      └─ Added original_source: {', '.join(new_sources)}")

    # Write back if modified
    if modified and not dry_run:
        post.metadata = metadata
        with open(resource_path, 'wb') as f:
            frontmatter.dump(post, fd=f, handler=handler)
        with open(resource_path, 'a') as f:
            f.write('\n')

    return modified, messages


def generate_missing_infores_report(resource_files: List[pathlib.Path], output_path: Optional[pathlib.Path] = None):
    """
    Generate a report of resources without infores IDs.

    Args:
        resource_files: List of resource file paths to check
        output_path: Path to write the report (default: reports/missing_infores_ids.tsv)
    """
    if output_path is None:
        output_path = ROOT.joinpath("reports/missing_infores_ids.tsv")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    missing_resources = []

    for resource_path in sorted(resource_files):
        post = frontmatter.load(resource_path)
        metadata = post.metadata

        resource_id = metadata.get('id')
        if not resource_id:
            continue

        # Check if this is a resource page (not a product page)
        if resource_id != resource_path.parent.name:
            continue

        # Check if infores_id is missing or empty
        infores_id = metadata.get('infores_id')
        if not infores_id:
            resource_name = metadata.get('name', resource_id)
            category = metadata.get('category', 'unknown')
            homepage_url = metadata.get('homepage_url', '')

            missing_resources.append({
                'resource_id': resource_id,
                'resource_name': resource_name,
                'category': category,
                'homepage_url': homepage_url,
                'file_path': str(resource_path.relative_to(ROOT))
            })

    # Write report
    with open(output_path, 'w', newline='') as f:
        if missing_resources:
            fieldnames = ['resource_id', 'resource_name', 'category', 'homepage_url', 'file_path']
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            writer.writerows(missing_resources)

    return len(missing_resources), output_path


def main():
    parser = argparse.ArgumentParser(
        description="Populate infores identifiers in KG-Registry",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--force-download',
        action='store_true',
        help='Force re-download of mapping files even if cached'
    )
    parser.add_argument(
        '--resource',
        help='Update only a specific resource (by ID)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show verbose output'
    )

    args = parser.parse_args()

    # Download/load mapping files
    try:
        sssom_path = download_file(SSSOM_MAPPING_URL, SSSOM_CACHE, args.force_download)
        infores_path = download_file(INFORES_CATALOG_URL, INFORES_CACHE, args.force_download)
    except Exception as e:
        print(f"ERROR: Failed to load mapping files: {e}")
        return 1

    # Load mappings
    kgr_to_infores = load_sssom_mappings(sssom_path)
    infores_catalog = load_infores_catalog(infores_path)
    infores_to_kgr = build_reverse_mapping(kgr_to_infores)

    print(f"\n{'=' * 60}")
    if args.dry_run:
        print("DRY RUN MODE - No files will be modified")
    else:
        print("Updating KG-Registry resources with infores identifiers")
    print(f"{'=' * 60}\n")

    # Get resource files to process
    if args.resource:
        resource_path = find_resource_file(args.resource)
        if not resource_path:
            print(f"ERROR: Resource '{args.resource}' not found")
            return 1
        resource_files = [resource_path]
    else:
        resource_files = get_all_resource_files()

    # Process each resource
    total_modified = 0
    total_skipped = 0

    for resource_path in sorted(resource_files):
        modified, messages = update_resource_infores(
            resource_path,
            kgr_to_infores,
            infores_to_kgr,
            infores_catalog,
            dry_run=args.dry_run
        )

        if modified:
            total_modified += 1
            resource_name = resource_path.parent.name
            print(f"\n📝 {resource_name}")
            for msg in messages:
                print(msg)
        elif args.verbose and messages:
            total_skipped += 1
            resource_name = resource_path.parent.name
            print(f"\n⏭️  {resource_name}")
            for msg in messages:
                print(msg)

    # Summary
    print(f"\n{'=' * 60}")
    print(f"Summary:")
    print(f"  Modified: {total_modified} resources")
    if args.verbose:
        print(f"  Skipped: {total_skipped} resources")
    if args.dry_run:
        print(f"\n  ⚠️  DRY RUN - No changes were made")
    else:
        print(f"\n  ✅ Changes written to disk")
    print(f"{'=' * 60}\n")

    # Generate missing infores report
    if not args.resource:  # Only generate report when processing all resources
        missing_count, report_path = generate_missing_infores_report(resource_files)
        print(f"📊 Missing infores IDs report:")
        print(f"  Resources without infores_id: {missing_count}")
        print(f"  Report saved to: {report_path.relative_to(ROOT)}\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
