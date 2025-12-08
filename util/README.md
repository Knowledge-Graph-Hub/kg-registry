# KG-Registry Utility Modules

This directory contains Python utility scripts for the KG-Registry project.

## Module Structure

### Core Modules (New)

These modules provide shared functionality and should be used by new scripts:

#### `common.py`
Shared utilities for all KG-Registry scripts:
- **Path constants**: `ROOT`, `RESOURCE_DIR`, `ORG_DIR`, `REGISTRY_DIR`, `SCHEMA_PATH`, `SOURCE_SCHEMA_PATH`
- **YAML handling**: `CustomRuamelYAMLHandler` class for format-preserving YAML operations
- **File loading**: `load_frontmatter_file()`, `load_frontmatter_files_parallel()`, `save_frontmatter_file()`
- **Data retrieval**: `get_resources_data()`, `get_organizations_data()`
- **Utilities**: `create_id_from_label()`, `get_today_iso()`, `get_yaml_text()`

#### `validation.py`
Validation utilities for Resources and Organizations:
- **Schema loading**: `load_json_schema()`
- **Resource validation**: `validate_resource()`, `validate_resources_parallel()`
- **Organization validation**: `validate_organization()`, `validate_organizations()`
- **Results handling**: `ValidationResults` class, `print_results()`, `save_results()`

#### `organizations.py`
Organization management utilities:
- **Page creation**: `create_organization_page()`, `remove_organization()`
- **Combination**: `combine_organizations()` - combines all org pages into registry file
- **Resource processing**: `update_resource_contacts()`, `process_resource_organizations()`
- **CLI commands**: `combine`, `create`, `consolidate` subcommands

### Wrapper Scripts

These scripts maintain backward compatibility while using the new modules:

- `combine-organizations.py` - Thin wrapper around `organizations.main_combine()`
- `create_organization_pages.py` - Thin wrapper around `organizations.main_create()`
- `utils.py` - Backward-compatible imports from `common.py`
- `parallel_loader.py` - Uses `common.py` for file loading
- `parallel_validator.py` - Uses `validation.py` for validation

### Original Scripts (To Be Migrated)

These scripts still define their own path constants and could benefit from using `common.py`:

- `validate-metadata.py` - Main resource validation script
- `validate-organizations.py` - Organization validation script
- `extract-metadata.py` - Metadata extraction and combination
- `consolidate_organizations.py` - Specific organization consolidations

### Utility Scripts

These scripts have specialized functionality:

- `processor.py` - Registry processing and data transformation
- `bulk_domain_rename.py` - Bulk domain field updates
- `standardize_license_labels.py` - License field standardization
- `populate_repositories.py` - Repository URL population
- `populate_infores_ids.py` - Infores ID population
- `populate_orcid.py` - ORCID population
- `create_infores_stubs.py` - Stub resource creation
- `add_preferred_prefixes.py` - Prefix management

## Usage

### For new scripts

Import from the core modules:

```python
from common import (
    ROOT,
    RESOURCE_DIR,
    ORG_DIR,
    load_frontmatter_file,
    create_id_from_label,
)

from validation import (
    ValidationResults,
    validate_resource,
    load_json_schema,
)

from organizations import (
    create_organization_page,
    combine_organizations,
)
```

### Running scripts

```bash
# Combine organizations
poetry run python util/combine-organizations.py

# Create organization pages (dry run)
poetry run python util/create_organization_pages.py

# Create organization pages (execute)
poetry run python util/create_organization_pages.py --execute

# Organizations module with subcommands
poetry run python util/organizations.py combine
poetry run python util/organizations.py create --execute
```

## Migration Notes

When migrating older scripts:

1. Replace local path constant definitions with imports from `common.py`
2. Replace custom YAML handlers with `CustomRuamelYAMLHandler` from `common.py`
3. Replace file loading code with `load_frontmatter_file()` or `load_frontmatter_files_parallel()`
4. For validation scripts, consider using `ValidationResults` class from `validation.py`
