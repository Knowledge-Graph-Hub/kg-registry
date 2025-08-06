# File Size Retrieval Implementation for KG-Registry

## Overview

This implementation adds automatic file size retrieval to the KG-Registry build process. File sizes are fetched from HTTP Content-Length headers for product URLs and displayed in both product detail and resource detail pages.

## Components Added/Modified

### 1. New Utility Script: `util/retrieve-file-sizes.py`

**Purpose**: Retrieves file sizes for products with URLs and populates the `product_file_size` field.

**Features**:
- Uses HTTP HEAD requests to get Content-Length headers without downloading files
- Excludes GraphicalInterface and ProgrammingInterface products as requested
- Handles errors gracefully (timeouts, missing headers, HTTP errors)
- Includes safety checks for file size limits (1GB max)
- Supports dry-run mode and processing limits for testing
- Provides detailed progress reporting

**Usage**:
```bash
# Process all products
python util/retrieve-file-sizes.py input.yml output.yml

# Dry run mode
python util/retrieve-file-sizes.py input.yml output.yml --dry-run

# Limit processing for testing
python util/retrieve-file-sizes.py input.yml output.yml --limit 50
```

### 2. Makefile Integration

**Changes**:
- Added new build step `tmp/unsorted-resources-with-sizes.yml` that retrieves file sizes
- Updated dependency chain to ensure file sizes are retrieved before validation and sorting
- Modified the process flow:
  1. Extract metadata → `tmp/unsorted-resources.yml`
  2. Retrieve file sizes → `tmp/unsorted-resources-with-sizes.yml` 
  3. Validate metadata → `reports/metadata-grid.csv`
  4. Sort resources → `registry/kgs.yml`

### 3. Layout Updates

#### Product Detail Page (`_layouts/product_detail.html`)
- Updated URL display to show file size next to filename
- Format: `filename.ext (size)` e.g., `cl.owl (229.5 MB)`
- Uses Liquid templating for proper size formatting (B, KB, MB, GB)

#### Resource Detail Page (`_layouts/resource_detail.html`)
- Updated both product tables ("From this Resource" and "From other Resources")
- File sizes appear in the URL column alongside the link
- Same formatting as product detail page

## File Size Display Logic

The layouts use Liquid templating to format file sizes in human-readable format:

```liquid
{% if p.product_file_size %}
  {% assign size = p.product_file_size %}
  {% if size < 1024 %}
    ({{ size }} B)
  {% elsif size < 1048576 %}
    ({{ size | divided_by: 1024.0 | round: 1 }} KB)
  {% elsif size < 1073741824 %}
    ({{ size | divided_by: 1048576.0 | round: 1 }} MB)
  {% else %}
    ({{ size | divided_by: 1073741824.0 | round: 1 }} GB)
  {% endif %}
{% endif %}
```

## Schema Compliance

The implementation uses the existing `product_file_size` field from the KG-Registry schema:

```yaml
product_file_size:
  description: >-
    The size of the product file, in bytes.
    The build process will attempt to determine this
    based on the file header and populate the metadata
    where possible.
  range: integer
```

## Error Handling

The script handles various error conditions gracefully:
- **No Content-Length header**: Skips the product, logs warning
- **HTTP errors**: Skips the product, logs HTTP status code
- **Network timeouts**: 10-second timeout, skips on timeout
- **Large files**: Skips files larger than 1GB to prevent issues
- **Invalid Content-Length**: Skips if header value is not a valid integer

## Performance Considerations

- Uses HTTP HEAD requests instead of GET to avoid downloading file content
- Implements connection timeouts to prevent hanging
- Processes products sequentially to avoid overwhelming servers
- Provides limit option for testing with subsets of data
- Skips products that already have file sizes populated

## Testing

The implementation has been tested with:
- Limited product processing (`--limit 10`) to verify functionality
- Dry-run mode to check behavior without making changes
- Integration with the Makefile build process
- Various URL types (direct files, GitHub pages, APIs, etc.)

## Build Process Integration

To build with file sizes:
```bash
# Full build process (includes file size retrieval)
make all

# Just retrieve file sizes
make tmp/unsorted-resources-with-sizes.yml
```

## Excluded Product Types

As requested, the following product categories are excluded from file size retrieval:
- `GraphicalInterface`: Web interfaces, browsers
- `ProgrammingInterface`: APIs, programming interfaces

These typically don't represent downloadable files with meaningful file sizes.

## Example Output

After running the file size retrieval, products will have file sizes displayed like:
- `cl.owl (229.5 MB)`
- `so.obo (187.9 KB)` 
- `anatomy.nodes.zip (332 B)`

## Summary

This implementation successfully adds file size retrieval and display to the KG-Registry build process while:
- Maintaining compatibility with existing schema
- Handling errors gracefully
- Providing good user experience with human-readable file sizes
- Integrating seamlessly into the existing build pipeline
- Following the project's coding patterns and conventions
