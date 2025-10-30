#!/usr/bin/env python3
"""
Create stub Resource pages for infores entries not in KG-Registry.

This script:
1. Loads the infores catalog
2. Checks which infores IDs don't have corresponding KG-Registry resources
3. Creates stub Resource pages for missing entries
4. Uses information from infores catalog to pre-populate fields
"""

import argparse
import pathlib
import sys
import urllib.request
from datetime import date
from typing import Dict, List, Set

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


def load_infores_catalog(catalog_path: pathlib.Path) -> Dict[str, Dict]:
    """
    Load infores catalog YAML.

    Returns dict mapping infores IDs (with prefix) to their metadata.
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


def get_existing_resource_ids() -> Set[str]:
    """Get set of all existing KG-Registry resource IDs."""
    resource_ids = set()

    for resource_dir in RESOURCE_DIRECTORY.iterdir():
        if resource_dir.is_dir():
            resource_file = resource_dir / f"{resource_dir.name}.md"
            if resource_file.exists():
                try:
                    post = frontmatter.load(resource_file)
                    resource_id = post.metadata.get('id')
                    if resource_id:
                        resource_ids.add(resource_id)
                except Exception as e:
                    print(f"Warning: Could not parse {resource_file}: {e}")

    print(f"Found {len(resource_ids)} existing KG-Registry resources")
    return resource_ids


def get_existing_infores_ids() -> Set[str]:
    """Get set of all infores IDs already in KG-Registry resources."""
    infores_ids = set()

    for resource_dir in RESOURCE_DIRECTORY.iterdir():
        if resource_dir.is_dir():
            resource_file = resource_dir / f"{resource_dir.name}.md"
            if resource_file.exists():
                try:
                    post = frontmatter.load(resource_file)
                    # Check resource-level infores_id
                    infores_id = post.metadata.get('infores_id')
                    if infores_id:
                        infores_ids.add(infores_id)

                    # Check product-level infores_ids
                    products = post.metadata.get('products', [])
                    for product in products:
                        product_infores = product.get('infores_id')
                        if product_infores:
                            infores_ids.add(product_infores)
                except Exception as e:
                    print(f"Warning: Could not parse {resource_file}: {e}")

    print(f"Found {len(infores_ids)} existing infores IDs in KG-Registry")
    return infores_ids


def infores_to_resource_id(infores_id: str) -> str:
    """
    Convert an infores ID to a KG-Registry resource ID.

    Strip 'infores:' prefix and convert hyphens to underscores.
    For hyphenated IDs, use the part before the first hyphen as the base.
    """
    # Strip prefix
    clean_id = infores_id.replace('infores:', '')

    # For hyphenated IDs (likely products), use the first part
    # e.g., "biothings-semmeddb" -> "biothings"
    # But keep non-hyphenated IDs as-is
    if '-' in clean_id:
        # Could be a product, but we'll create a stub anyway
        # Use the full ID but replace hyphens with underscores
        clean_id = clean_id.replace('-', '_')

    return clean_id


def guess_category_from_infores(infores_entry: Dict) -> str:
    """
    Guess the category based on infores metadata.
    Default to 'DataSource' for most entries.
    """
    description = infores_entry.get('description', '').lower()
    name = infores_entry.get('name', '').lower()

    # Check for keywords
    if any(keyword in description or keyword in name for keyword in ['ontology', 'vocabulary', 'controlled vocabulary']):
        return 'OntologyResource'
    elif any(keyword in description or keyword in name for keyword in ['database', 'repository', 'resource']):
        return 'DataSource'
    elif any(keyword in description or keyword in name for keyword in ['knowledge graph', 'knowledge base']):
        return 'GraphResource'
    elif any(keyword in description or keyword in name for keyword in ['tool', 'software', 'service', 'api']):
        return 'ToolResource'

    # Default
    return 'DataSource'


def extract_homepage_from_xref(xrefs: List[str]) -> str:
    """Extract a homepage URL from xref list."""
    if not xrefs:
        return ''

    # Prefer https URLs
    https_urls = [x for x in xrefs if x.startswith('https://')]
    if https_urls:
        return https_urls[0]

    # Fall back to http
    http_urls = [x for x in xrefs if x.startswith('http://')]
    if http_urls:
        return http_urls[0]

    return xrefs[0] if xrefs else ''


def create_stub_resource(infores_id: str, infores_entry: Dict, dry_run: bool = False) -> pathlib.Path:
    """
    Create a stub Resource page for an infores entry.

    Returns the path to the created file.
    """
    # Determine resource ID
    resource_id = infores_to_resource_id(infores_id)

    # Create directory
    resource_dir = RESOURCE_DIRECTORY / resource_id
    resource_file = resource_dir / f"{resource_id}.md"

    # Check if already exists
    if resource_file.exists():
        print(f"  ⚠️  Resource file already exists: {resource_file}")
        return resource_file

    # Extract information from infores entry
    name = infores_entry.get('name', resource_id.replace('_', ' ').title())
    description = infores_entry.get('description', f'Information resource for {name}')
    xrefs = infores_entry.get('xref', [])
    homepage_url = extract_homepage_from_xref(xrefs)
    synonyms = infores_entry.get('synonym', [])

    # Guess category
    category = guess_category_from_infores(infores_entry)

    # Strip 'infores:' prefix for infores_id field
    clean_infores_id = infores_id.replace('infores:', '')

    # Create metadata
    # Format dates as ISO 8601 with time
    today = date.today()
    today_iso = f"{today.isoformat()}T00:00:00Z"

    metadata = {
        'activity_status': 'unknown',  # Needs curation
        'category': category,
        'creation_date': today_iso,
        'description': description,
        'domains': ['stub'],  # Mark as stub using domains field
        'id': resource_id,
        'infores_id': clean_infores_id,
        'last_modified_date': today_iso,
        'layout': 'resource_detail',
        'name': name,
    }

    # Add optional fields if available
    if homepage_url:
        metadata['homepage_url'] = homepage_url

    if synonyms:
        metadata['synonyms'] = synonyms

    # Create markdown content
    content = f"""# {name}

## Overview

{description}

**Note:** This is a stub entry that was automatically created from the [Translator Information Resource Registry](https://biolink.github.io/information-resource-registry/). It requires manual curation to add complete metadata, products, and additional information.

## Information Resource ID

This resource has the Information Resource identifier: `infores:{clean_infores_id}`

## Curation Status

- **Stub**: Yes - needs manual curation
- **Creation Date**: {today}
- **Original Source**: Translator Information Resource Registry

## What Needs to be Curated

1. **Activity Status**: Verify if this resource is active, inactive, or deprecated
2. **Category**: Confirm the resource category is correct
3. **Description**: Expand and improve the description
4. **Homepage URL**: Verify and update if needed
5. **Products**: Add specific data products/files/APIs offered by this resource
6. **Contacts**: Add contact information
7. **Publications**: Add relevant publications
8. **Domains**: Add relevant domain tags
9. **Repository**: Add code repository if applicable

## Additional Notes

"""

    # Check if this looks like a product (has hyphen in infores ID)
    if '-' in infores_id:
        content += f"""
**Note**: The infores ID `{infores_id}` contains a hyphen, which may indicate this is actually a **Product** rather than a Resource. For example, `infores:biothings-semmeddb` represents the SemMedDB product provided by BioThings. During curation, consider whether this should be:

1. A separate Resource page, or
2. A Product under an existing parent Resource

If this should be a Product, add it to the appropriate parent Resource's `products` field and remove this stub page.
"""

    # Create the post
    handler = CustomRuamelYAMLHandler()
    post = frontmatter.Post(content, handler=handler, **metadata)

    if not dry_run:
        # Create directory and write file
        resource_dir.mkdir(exist_ok=True, parents=True)
        with open(resource_file, 'wb') as f:
            frontmatter.dump(post, fd=f, handler=handler)
        # Add trailing newline
        with open(resource_file, 'a') as f:
            f.write('\n')

        print(f"  ✓ Created stub: {resource_file}")
    else:
        print(f"  [DRY RUN] Would create: {resource_file}")

    return resource_file


def main():
    parser = argparse.ArgumentParser(
        description="Create stub Resource pages for infores entries not in KG-Registry",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be created without creating files'
    )
    parser.add_argument(
        '--force-download',
        action='store_true',
        help='Force re-download of mapping files even if cached'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of stubs to create (for testing)'
    )
    parser.add_argument(
        '--only-simple',
        action='store_true',
        help='Only create stubs for simple IDs (no hyphens)'
    )
    parser.add_argument(
        '--status',
        choices=['released', 'deprecated', 'draft'],
        help='Only create stubs for infores entries with this status'
    )

    args = parser.parse_args()

    # Download/load catalog
    try:
        infores_path = download_file(INFORES_CATALOG_URL, INFORES_CACHE, args.force_download)
    except Exception as e:
        print(f"ERROR: Failed to load infores catalog: {e}")
        return 1

    # Load data
    infores_catalog = load_infores_catalog(infores_path)
    existing_resource_ids = get_existing_resource_ids()
    existing_infores_ids = get_existing_infores_ids()

    print(f"\n{'=' * 60}")
    if args.dry_run:
        print("DRY RUN MODE - No files will be created")
    else:
        print("Creating stub Resource pages for missing infores entries")
    print(f"{'=' * 60}\n")

    # Find missing infores entries
    missing_entries = []
    for infores_id, infores_entry in infores_catalog.items():
        # Strip prefix for comparison
        clean_infores_id = infores_id.replace('infores:', '')

        # Skip if already in KG-Registry
        if clean_infores_id in existing_infores_ids:
            continue

        # Check resource ID
        resource_id = infores_to_resource_id(infores_id)
        if resource_id in existing_resource_ids:
            continue

        # Filter by status if requested
        if args.status:
            if infores_entry.get('status') != args.status:
                continue
        else:
            # By default, exclude deprecated entries
            if infores_entry.get('status') == 'deprecated':
                continue

        # Filter by complexity if requested
        if args.only_simple:
            if '-' in clean_infores_id:
                continue

        missing_entries.append((infores_id, infores_entry))

    # Report filtering results
    if args.status:
        print(
            f"Found {len(missing_entries)} infores entries not in KG-Registry with status='{args.status}'\n")
    else:
        print(f"Found {len(missing_entries)} infores entries not in KG-Registry (excluding deprecated)\n")

    if not missing_entries:
        print("No stub pages needed!")
        return 0

    # Apply limit if specified
    if args.limit:
        missing_entries = missing_entries[:args.limit]
        print(f"Limited to {args.limit} stubs\n")

    # Create stub pages
    created_count = 0
    skipped_count = 0

    for infores_id, infores_entry in missing_entries:
        clean_infores_id = infores_id.replace('infores:', '')
        resource_id = infores_to_resource_id(infores_id)
        status = infores_entry.get('status', 'unknown')
        name = infores_entry.get('name', resource_id)

        print(f"\n📄 {name}")
        print(f"  infores: {clean_infores_id}")
        print(f"  resource_id: {resource_id}")
        print(f"  status: {status}")

        if '-' in clean_infores_id:
            print(f"  ⚠️  Hyphenated ID - may be a Product")

        try:
            create_stub_resource(infores_id, infores_entry, dry_run=args.dry_run)
            created_count += 1
        except Exception as e:
            print(f"  ❌ Error creating stub: {e}")
            skipped_count += 1

    # Summary
    print(f"\n{'=' * 60}")
    print(f"Summary:")
    print(f"  Created: {created_count} stub pages")
    if skipped_count > 0:
        print(f"  Skipped: {skipped_count} (errors)")
    if args.dry_run:
        print(f"\n  ⚠️  DRY RUN - No files were created")
    else:
        print(f"\n  ✅ Stub pages created")
    print(f"{'=' * 60}\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
