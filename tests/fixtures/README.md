# Test Fixtures

This directory contains both static test data files and pytest fixture modules.

`tests/conftest.py` registers the Python fixture modules here as pytest plugins, so
their fixtures are automatically available to tests without local import boilerplate.

## Static Fixture Files

### `test_ftp_resources.yml`
Test data for `util/processor.py` `check_urls`.
- Uses the `resource_purl` field expected by `processor.py`
- Contains examples of FTP files, FTP directories, and HTTPS URLs
- Used by [tests/test_ftp_url_checker.py](/home/harry/kg-registry/tests/test_ftp_url_checker.py)

### `test_ftp_parallel.yml`
Test data for `util/retrieve-file-sizes-parallel.py`.
- Uses the `product_url` field expected by the retrieve-file-sizes scripts
- Contains examples of FTP files, FTP directories, and HTTPS URLs
- Used by [tests/test_ftp_url_checker.py](/home/harry/kg-registry/tests/test_ftp_url_checker.py)

## Pytest Fixture Modules

### `frink_fixtures.py`
Reusable example data and objects for FRINK sync tests.
- `frink_syncer`
- `frink_entry_example`
- `frink_existing_resource_example`
- `frink_synced_resource_example`

Used by [tests/test_frink_sync.py](/home/harry/kg-registry/tests/test_frink_sync.py).

### `module_fixtures.py`
Shared dynamic module loaders for tests that exercise utility scripts directly.
- `repo_root`
- `util_dir`
- `extract_metadata_module`
- `quality_dashboard_module`
- `kg_monarch_ingest_module`
- `parallel_validator_module`

Used by multiple tests, including:
- [tests/test_kg_monarch_ingest.py](/home/harry/kg-registry/tests/test_kg_monarch_ingest.py)
- [tests/test_quality_dashboard.py](/home/harry/kg-registry/tests/test_quality_dashboard.py)
- [tests/test_validate_domain_sanitization.py](/home/harry/kg-registry/tests/test_validate_domain_sanitization.py)
- [tests/test_validate_string_coercion.py](/home/harry/kg-registry/tests/test_validate_string_coercion.py)
- [tests/test_parallel_validation.py](/home/harry/kg-registry/tests/test_parallel_validation.py)

### `parquet_backend_fixtures.py`
Reusable sample registry payloads and YAML writers for Parquet backend tests.
- `parquet_backend_sample_data`
- `parquet_backend_taxa_data`
- `parquet_backend_taxon_query_data`
- `parquet_backend_single_taxon_data`
- `parquet_yaml_writer`

Used by [tests/test_parquet_backend.py](/home/harry/kg-registry/tests/test_parquet_backend.py).

## FTP URLs Used

The FTP YAML fixtures use public NCBI FTP endpoints:
- FTP file: `ftp://ftp.ncbi.nlm.nih.gov/README.ftp`
- FTP directory: `ftp://ftp.ncbi.nlm.nih.gov/pub/`

## Example Usage

Static YAML fixture:

```python
from pathlib import Path
import yaml

fixtures_dir = Path(__file__).parent / "fixtures"
with open(fixtures_dir / "test_ftp_resources.yml", "r", encoding="utf-8") as handle:
    test_data = yaml.safe_load(handle)
```

Pytest fixture plugin:

```python
def test_transform_frink_entry_to_resource(frink_syncer, frink_entry_example):
    resource = frink_syncer.transform_frink_to_kg_registry(frink_entry_example)
    assert resource["id"] == "prokn"
```
