#!/usr/bin/env python3

import argparse
import pathlib
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

import frontmatter
import requests
import yaml

# ---------------------------------------------------------------------------
# URL STATUS CACHE
# ---------------------------------------------------------------------------
# We maintain a YAML cache of prior URL HEAD results so we can
# skip expensive or known-non-file endpoints on subsequent runs.
# A URL will be skipped (no network call) if a previous run determined
# it was an HTML page or had no Content-Type header.
# ---------------------------------------------------------------------------

# Configuration
REQUEST_TIMEOUT = 10  # seconds
EXCLUDED_CATEGORIES = ['GraphicalInterface', 'ProgrammingInterface']
DEFAULT_CACHE_PATH = pathlib.Path('cache/url_status_cache.yml')


def load_url_cache(cache_path: pathlib.Path) -> Dict[str, Any]:
    if cache_path.exists():
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
                if isinstance(data, dict):
                    return data
        except Exception as e:
            print(f"⚠️  Could not read cache at {cache_path}: {e}")
    return {}


def save_url_cache(cache: Dict[str, Any], cache_path: pathlib.Path) -> None:
    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        with open(cache_path, 'w', encoding='utf-8') as f:
            yaml.dump(cache, f, default_flow_style=False, allow_unicode=True)
        print(f"💾 URL status cache written: {cache_path} ({len(cache)} entries)")
    except Exception as e:
        print(f"⚠️  Could not write cache file {cache_path}: {e}")


def cache_should_skip(url: str, cache: Dict[str, Any], ignore_cache: bool = False) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """Return (should_skip, entry) based on cache."""
    if ignore_cache:
        return False, None
    entry = cache.get(url)
    if not entry:
        return False, None
    # Skip if prior run recorded skip_reason we want to honor
    if entry.get('skip_reason') in {'html_page', 'no_content_type'}:
        return True, entry
    return False, entry


def convert_github_url_to_raw(url: str) -> str:
    """
    Convert GitHub blob URLs to raw URLs for direct file access.

    Examples:
    - https://github.com/user/repo/blob/main/file.txt -> https://raw.githubusercontent.com/user/repo/main/file.txt
    - https://github.com/user/repo/blob/master/dir/file.json -> https://raw.githubusercontent.com/user/repo/master/dir/file.json

    Args:
        url: The original URL

    Returns:
        Raw URL if it's a GitHub blob URL, otherwise the original URL
    """
    import re

    # Pattern to match GitHub blob URLs
    github_blob_pattern = r'https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)'
    match = re.match(github_blob_pattern, url)

    if match:
        user, repo, branch, file_path = match.groups()
        raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{file_path}"
        return raw_url

    return url


def get_file_size_from_header(url: str) -> Tuple[Optional[int], Optional[str], Dict[str, Any]]:
    """
    Retrieve file size from HTTP Content-Length header without downloading the file.
    Skips HTML pages as these are not downloadable files, but converts GitHub blob URLs to raw URLs first.

    Args:
        url: The URL to check

    Returns:
        Tuple of (file_size in bytes or None, error_message or None)
    """
    try:
        # Convert GitHub blob URLs to raw URLs for direct file access
        original_url = url
        url = convert_github_url_to_raw(url)

        if url != original_url:
            print(f"Checking file size for: {original_url}")
            print(f"  🔄 Converted to raw URL: {url}")
        else:
            print(f"Checking file size for: {url}")

        # Use HEAD request to get headers without downloading content
        response = requests.head(url, timeout=REQUEST_TIMEOUT, allow_redirects=True)

        # Check if request was successful
        info: Dict[str, Any] = {
            'status_code': response.status_code,
            'checked_at': datetime.utcnow().isoformat(timespec='seconds') + 'Z'
        }

        if response.status_code != 200:
            error_msg = f"HTTP {response.status_code} error when accessing file"
            print(f"  ⚠️  {error_msg}")
            info['error'] = error_msg
            return None, error_msg, info

        # Check Content-Type to skip HTML pages (after URL conversion)
        content_type = response.headers.get('Content-Type', '')
        info['content_type'] = content_type
        ct_lower = content_type.lower()
        if 'text/html' in ct_lower:
            print(f"  ⏭️  Skipping HTML page (Content-Type: {ct_lower})")
            info['skip_reason'] = 'html_page'
            return None, None, info  # Not an error, just not a downloadable file
        if not content_type:
            # Record that there was no content type so we can skip in future
            print("  ⏭️  No Content-Type header; will cache skip for future runs")
            info['skip_reason'] = 'no_content_type'
            # Continue to attempt retrieving size

        # Get Content-Length header
        content_length = response.headers.get('Content-Length')

        if content_length is None:
            error_msg = "No Content-Length header found"
            print(f"  ⚠️  {error_msg}")
            info['error'] = error_msg
            return None, error_msg, info

        try:
            file_size = int(content_length)
            print(f"  ✅ File size: {format_file_size(file_size)}")
            info['content_length'] = file_size
            return file_size, None, info
        except ValueError:
            error_msg = f"Invalid Content-Length value: {content_length}"
            print(f"  ⚠️  {error_msg}")
            info['error'] = error_msg
            return None, error_msg, info

    except requests.exceptions.Timeout:
        error_msg = "Timeout connecting to URL"
        print(f"  ⚠️  {error_msg}")
        return None, error_msg, {'error': error_msg, 'skip_reason': None, 'checked_at': datetime.utcnow().isoformat(timespec='seconds') + 'Z'}
    except requests.exceptions.RequestException as e:
        error_msg = f"Error connecting to URL: {str(e)}"
        print(f"  ⚠️  {error_msg}")
        return None, error_msg, {'error': error_msg, 'skip_reason': None, 'checked_at': datetime.utcnow().isoformat(timespec='seconds') + 'Z'}
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(f"  ⚠️  {error_msg}")
        return None, error_msg, {'error': error_msg, 'skip_reason': None, 'checked_at': datetime.utcnow().isoformat(timespec='seconds') + 'Z'}


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"


def should_skip_product(product: Dict[str, Any]) -> bool:
    """
    Determine if a product should be skipped for file size retrieval.

    Args:
        product: Product dictionary

    Returns:
        True if the product should be skipped
    """
    # Skip if no product_url
    if 'product_url' not in product or not product['product_url']:
        return True

    # Skip GraphicalInterface and ProgrammingInterface products
    category = product.get('category', '')
    if category in EXCLUDED_CATEGORIES:
        return True

    # Skip if file size already exists and is valid
    existing_size = product.get('product_file_size')
    if existing_size is not None and isinstance(existing_size, int) and existing_size > 0:
        return True

    return False


def write_file_sizes_to_resource_files(updated_products: Dict[str, List[Dict[str, Any]]]) -> None:
    """
    Write updated file sizes back to the original resource files.

    Args:
        updated_products: Dictionary mapping resource_id to list of updated products
    """
    if not updated_products:
        print("No file sizes to write back to resource files")
        return

    print(f"\n💾 Writing file sizes back to {len(updated_products)} resource files...")

    for resource_id, products in updated_products.items():
        resource_file = f"resource/{resource_id}/{resource_id}.md"

        try:
            # Check if the resource file exists
            if not pathlib.Path(resource_file).exists():
                print(f"  ⚠️  Resource file not found: {resource_file}")
                continue

            # Load the resource file
            with open(resource_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            metadata = post.metadata
            content = post.content

            # Update products with file sizes
            if 'products' not in metadata:
                continue

            updated_count = 0
            products_list = metadata.get('products')
            if isinstance(products_list, list):
                for product in products_list:
                    if isinstance(product, dict) and 'id' in product:
                        # Find matching updated product
                        for updated_product in products:
                            if updated_product.get('id') == product['id']:
                                updated_this_product = False

                                # Update file size if we don't already have one
                                if 'product_file_size' in updated_product and 'product_file_size' not in product:
                                    product['product_file_size'] = updated_product['product_file_size']
                                    updated_this_product = True

                                # Update warnings if there are new ones
                                if 'warnings' in updated_product:
                                    if 'warnings' not in product:
                                        product['warnings'] = []
                                    elif not isinstance(product['warnings'], list):
                                        product['warnings'] = []

                                    # Add new warnings that aren't already present
                                    for warning in updated_product['warnings']:
                                        if warning not in product['warnings']:
                                            product['warnings'].append(warning)
                                            updated_this_product = True

                                if updated_this_product:
                                    updated_count += 1

            if updated_count > 0:
                # Write back to file
                with open(resource_file, 'w', encoding='utf-8') as f:
                    f.write("---\n")
                    yaml.dump(metadata, f, default_flow_style=False, allow_unicode=True)
                    f.write("---\n")
                    f.write(content)

                print(f"  ✅ Updated {updated_count} products in {resource_file}")
            else:
                print(f"  ℹ️  No updates needed for {resource_file}")

        except Exception as e:
            print(f"  ❌ Error updating {resource_file}: {str(e)}")


def update_product_file_sizes(data: Dict[str, Any], limit: Optional[int] = None, *, cache: Dict[str, Any], ignore_cache: bool = False) -> Tuple[Dict[str, Any], Dict[str, List[Dict[str, Any]]]]:
    """
    Update product_file_size for all products in the registry data.

    Args:
        data: Registry data dictionary
        limit: Optional limit on number of products to process (for testing)

    Returns:
        Tuple of (updated registry data, dictionary of updated products by resource_id)
    """
    if 'resources' not in data:
        print("No resources found in data")
        return data, {}

    total_products = 0
    updated_products = 0
    skipped_products = 0
    failed_products = 0
    cache_skipped = 0
    processed_products = 0

    # Track updated products by resource ID for writing back to files
    updated_products_by_resource: Dict[str, List[Dict[str, Any]]] = {}

    for resource in data['resources']:
        if 'products' not in resource:
            continue

        resource_id = resource.get('id')
        if not resource_id:
            continue

        for product in resource['products']:
            total_products += 1

            # Check if we've hit the limit
            if limit is not None and processed_products >= limit:
                print(f"🔬 Reached limit of {limit} products, stopping")
                break

            if should_skip_product(product):
                skipped_products += 1
                continue

            processed_products += 1

            url = product['product_url']
            should_skip_cache, cache_entry = cache_should_skip(
                url, cache, ignore_cache=ignore_cache)
            if should_skip_cache:
                cache_skipped += 1
                reason = cache_entry.get('skip_reason') if isinstance(
                    cache_entry, dict) else 'cached'
                print(f"⏭️  Skipping (cache): {url} (reason: {reason})")
                continue

            # Try to get file size and any error information
            file_size, error_message, info = get_file_size_from_header(url)
            # Update cache with latest info
            cache_record = cache.get(url, {})
            cache_record.update({k: v for k, v in info.items() if v is not None})
            if file_size is not None:
                cache_record['last_success_bytes'] = file_size
            cache[url] = cache_record

            if file_size is not None:
                product['product_file_size'] = file_size
                updated_products += 1

                # Track this update for writing back to resource files
                if resource_id not in updated_products_by_resource:
                    updated_products_by_resource[resource_id] = []
                updated_products_by_resource[resource_id].append(product.copy())
            elif error_message is not None:
                # Add warning with current date
                current_date = datetime.now().strftime("%Y-%m-%d")
                warning_message = f"File was not able to be retrieved when checked on {current_date}: {error_message}"

                # Ensure warnings list exists
                if 'warnings' not in product:
                    product['warnings'] = []
                elif not isinstance(product['warnings'], list):
                    product['warnings'] = []

                # Add the warning if it's not already there
                if warning_message not in product['warnings']:
                    product['warnings'].append(warning_message)

                    # Track this update for writing back to resource files
                    if resource_id not in updated_products_by_resource:
                        updated_products_by_resource[resource_id] = []
                    updated_products_by_resource[resource_id].append(product.copy())

                failed_products += 1
            else:
                # This case is for HTML pages that we intentionally skip (no error)
                failed_products += 1

        # Break out of resource loop if we hit the limit
        if limit is not None and processed_products >= limit:
            break

    print(f"\n📊 File Size Retrieval Summary:")
    print(f"   Total products: {total_products}")
    print(f"   Processed: {processed_products}")
    print(f"   Updated: {updated_products}")
    print(f"   Skipped (category/has-size/no-url): {skipped_products}")
    print(f"   Skipped via cache: {cache_skipped}")
    print(f"   Failed: {failed_products}")

    return data, updated_products_by_resource


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve file sizes for products with URLs and update product_file_size field",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("input_file", help="Input YAML file containing registry data")
    parser.add_argument("output_file", help="Output YAML file to write updated data")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be updated without making changes")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limit processing to first N products (for testing)")
    parser.add_argument("--write-back", action="store_true", default=True,
                        help="Write file sizes back to original resource files (default: True)")
    parser.add_argument("--no-write-back", dest="write_back", action="store_false",
                        help="Don't write file sizes back to original resource files")
    parser.add_argument("--cache-file", default=str(DEFAULT_CACHE_PATH),
                        help="Path to URL status cache YAML (default: cache/url_status_cache.yml)")
    parser.add_argument("--ignore-cache", action="store_true",
                        help="Ignore existing cache when deciding to skip URLs")

    args = parser.parse_args()

    # Load input data
    try:
        with open(args.input_file, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading input file {args.input_file}: {e}")
        sys.exit(1)

    if args.dry_run:
        print("🔍 DRY RUN MODE - No changes will be saved")

    if args.limit:
        print(f"🔬 LIMIT MODE - Processing only first {args.limit} products")

    # Load cache
    cache_path = pathlib.Path(args.cache_file)
    cache = load_url_cache(cache_path)
    if cache:
        print(f"🗃️  Loaded URL status cache with {len(cache)} entries from {cache_path}")
    else:
        print(f"🗃️  Starting with empty URL status cache (path: {cache_path})")

    # Update file sizes
    updated_data, updated_products_by_resource = update_product_file_sizes(
        data, limit=args.limit, cache=cache, ignore_cache=args.ignore_cache)

    # Write file sizes back to resource files (unless disabled or in dry-run mode)
    if args.write_back and not args.dry_run and updated_products_by_resource:
        write_file_sizes_to_resource_files(updated_products_by_resource)
    elif args.dry_run and updated_products_by_resource:
        print(
            f"\n🔍 DRY RUN: Would write file sizes back to {len(updated_products_by_resource)} resource files")

    if not args.dry_run:
        # Save updated data
        try:
            with open(args.output_file, 'w') as f:
                yaml.dump(updated_data, f, default_flow_style=False, allow_unicode=True)
            print(f"✅ Updated data saved to {args.output_file}")
        except Exception as e:
            print(f"Error saving output file {args.output_file}: {e}")
            sys.exit(1)
        # Persist cache
        save_url_cache(cache, cache_path)
    else:
        print("🔍 Dry run completed - no files were modified")


if __name__ == "__main__":
    main()
