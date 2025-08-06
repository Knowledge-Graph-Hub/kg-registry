#!/usr/bin/env python3

import argparse
import sys
import pathlib
import requests
import yaml
from typing import Dict, Any, Optional, List

# Configuration
REQUEST_TIMEOUT = 10  # seconds
MAX_FILE_SIZE = 1024 * 1024 * 1024  # 1GB - don't download files larger than this
EXCLUDED_CATEGORIES = ['GraphicalInterface', 'ProgrammingInterface']

def get_file_size_from_header(url: str) -> Optional[int]:
    """
    Retrieve file size from HTTP Content-Length header without downloading the file.
    
    Args:
        url: The URL to check
        
    Returns:
        File size in bytes, or None if unable to determine
    """
    try:
        print(f"Checking file size for: {url}")
        
        # Use HEAD request to get headers without downloading content
        response = requests.head(url, timeout=REQUEST_TIMEOUT, allow_redirects=True)
        
        # Check if request was successful
        if response.status_code != 200:
            print(f"  ⚠️  HTTP {response.status_code} for {url}")
            return None
            
        # Get Content-Length header
        content_length = response.headers.get('Content-Length')
        
        if content_length is None:
            print(f"  ⚠️  No Content-Length header found for {url}")
            return None
            
        try:
            file_size = int(content_length)
            print(f"  ✅ File size: {format_file_size(file_size)}")
            return file_size
        except ValueError:
            print(f"  ⚠️  Invalid Content-Length value: {content_length}")
            return None
            
    except requests.exceptions.Timeout:
        print(f"  ⚠️  Timeout connecting to {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"  ⚠️  Error connecting to {url}: {str(e)}")
        return None
    except Exception as e:
        print(f"  ⚠️  Unexpected error for {url}: {str(e)}")
        return None

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

def update_product_file_sizes(data: Dict[str, Any], limit: Optional[int] = None) -> Dict[str, Any]:
    """
    Update product_file_size for all products in the registry data.
    
    Args:
        data: Registry data dictionary
        limit: Optional limit on number of products to process (for testing)
        
    Returns:
        Updated registry data
    """
    if 'resources' not in data:
        print("No resources found in data")
        return data
        
    total_products = 0
    updated_products = 0
    skipped_products = 0
    failed_products = 0
    processed_products = 0
    
    for resource in data['resources']:
        if 'products' not in resource:
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
            
            # Try to get file size
            file_size = get_file_size_from_header(product['product_url'])
            
            if file_size is not None:
                # Check if file size is reasonable (not too large)
                if file_size > MAX_FILE_SIZE:
                    print(f"  ⚠️  File too large ({format_file_size(file_size)}), skipping")
                    failed_products += 1
                    continue
                    
                product['product_file_size'] = file_size
                updated_products += 1
            else:
                failed_products += 1
                
        # Break out of resource loop if we hit the limit
        if limit is not None and processed_products >= limit:
            break
            
    print(f"\n📊 File Size Retrieval Summary:")
    print(f"   Total products: {total_products}")
    print(f"   Processed: {processed_products}")
    print(f"   Updated: {updated_products}")
    print(f"   Skipped: {skipped_products}")
    print(f"   Failed: {failed_products}")
    
    return data

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
        
    # Update file sizes
    updated_data = update_product_file_sizes(data, limit=args.limit)
    
    if not args.dry_run:
        # Save updated data
        try:
            with open(args.output_file, 'w') as f:
                yaml.dump(updated_data, f, default_flow_style=False, allow_unicode=True)
            print(f"✅ Updated data saved to {args.output_file}")
        except Exception as e:
            print(f"Error saving output file {args.output_file}: {e}")
            sys.exit(1)
    else:
        print("🔍 Dry run completed - no files were modified")

if __name__ == "__main__":
    main()
