---
layout: intro_doc
title: Parquet Backend for KG-Registry
---

# Parquet Backend for KG-Registry

The KG-Registry now includes a Parquet backend that provides enhanced querying capabilities while keeping data size manageable and maintaining the human-readable YAML files in the `registry` directory.

## Features

- **Efficient Storage**: Parquet format provides columnar storage with better compression than a full DuckDB database
- **Fast Querying**: DuckDB can directly query Parquet files without loading the entire dataset
- **Human-Readable Data**: Original YAML files remain unchanged and editable
- **Rich Query Interface**: Python API and CLI commands for querying resources
- **Statistics**: Built-in analytics and statistics generation
- **Synchronization**: Easy sync from YAML files to Parquet files
- **GitHub-Friendly**: Parquet files can be version controlled with reasonable storage size

## Installation

DuckDB is included as a dependency in the project. To install:

```bash
# Using poetry (recommended)
poetry install

# Or using pip
pip install duckdb pyarrow
```

## Quick Start

### 1. Sync YAML Data to Parquet

```bash
# Sync the registry data to Parquet files
python -m kg_registry.cli parquet sync --yaml-file registry/kgs.yml --output-dir registry/parquet
```

### 2. Query Resources

```bash
# Get statistics about the registry
python -m kg_registry.cli parquet stats --parquet-dir registry/parquet

# Query resources by category
python -m kg_registry.cli parquet query --category KnowledgeGraph --parquet-dir registry/parquet

# Query resources by domain
python -m kg_registry.cli parquet query --domain genomics --parquet-dir registry/parquet

# Search resources by name or description
python -m kg_registry.cli parquet query --search "drug" --parquet-dir registry/parquet
```

## Python API

### Basic Usage

```python
from kg_registry.parquet_backend import ParquetBackend, DuckDBParquetQuerier

# Method 1: Load data into memory for querying
with ParquetBackend() as backend:
    # Load data from Parquet files
    backend.load_from_parquet("registry/parquet")
    
    # Query resources
    active_kgs = backend.query_resources(
        category="KnowledgeGraph",
        activity_status="active"
    )
    
    # Search resources
    drug_resources = backend.search_resources("drug")
    
    # Get statistics
    stats = backend.get_resource_stats()
    print(f"Total resources: {stats['total_resources']}")

# Method 2: Query Parquet files directly without loading into memory
with DuckDBParquetQuerier("registry/parquet") as querier:
    # Execute custom SQL query directly on Parquet files
    results = querier.execute_query("""
        SELECT r.id, r.name, r.category, COUNT(p.product_id) as product_count
        FROM resources r
        LEFT JOIN resource_products p ON r.id = p.resource_id
        WHERE r.activity_status = 'active'
        GROUP BY r.id, r.name, r.category
        HAVING COUNT(p.product_id) > 0
        ORDER BY product_count DESC
        LIMIT 10
    """)
```

### Syncing Data

```python
from kg_registry.parquet_backend import sync_yaml_to_parquet

# Sync YAML data to Parquet files
count = sync_yaml_to_parquet("registry/kgs.yml", "registry/parquet")
print(f"Synced {count} resources to Parquet files")
```

## CLI Commands

### `parquet sync`

Synchronize YAML data to Parquet files.

```bash
python -m kg_registry.cli parquet sync [OPTIONS]

Options:
  --yaml-file TEXT    Path to YAML file to sync (default: registry/kgs.yml)
  --output-dir TEXT   Directory to store Parquet files (default: registry/parquet)
```

### `parquet stats`

Show statistics about the registry from Parquet files.

```bash
python -m kg_registry.cli parquet stats [OPTIONS]

Options:
  --parquet-dir TEXT  Directory containing Parquet files (default: registry/parquet)
```

### `parquet query`

Query resources from Parquet files.

```bash
python -m kg_registry.cli parquet query [OPTIONS]

Options:
  --category TEXT     Filter by category
  --domain TEXT       Filter by domain
  --status TEXT       Filter by activity status
  --search TEXT       Search in name or description
  --parquet-dir TEXT  Directory containing Parquet files (default: registry/parquet)
```

## Web Frontend

The KG-Registry web interface can query Parquet files directly using DuckDB-WASM in the browser.
This allows for complex queries without having to load the entire database.

To set up the web frontend with Parquet support:

1. Export the registry data to Parquet files:
   ```bash
   python -m kg_registry.cli parquet sync
   ```

2. The advanced search interface at `/advanced-search.html` will automatically
   load the Parquet files from `/registry/parquet/` and enable querying.

## Benefits over Full DuckDB Database

1. **Size**: Parquet files are significantly smaller than a full DuckDB database
2. **Version Control**: Parquet files can be effectively tracked in Git
3. **Performance**: Queries only read the columns they need
4. **Compatibility**: Parquet is an open standard supported by many tools
5. **Portability**: Parquet files can be easily shared and used with other systems

## Data Synchronization

The Parquet backend maintains a copy of the YAML data in Parquet format. To keep it synchronized:

1. **Manual Sync**: Run the `parquet sync` command after updating YAML files
2. **Automated Sync**: Integrate the sync command into your CI/CD pipeline
3. **Programmatic Sync**: Use the Python API to sync data in scripts

## Example Use Cases

### 1. Finding Resources with Complex Criteria

```python
# Using DuckDBParquetQuerier for efficient querying without loading into memory
with DuckDBParquetQuerier("registry/parquet") as querier:
    # Find active knowledge graphs in genomics with products
    results = querier.execute_query("""
        SELECT r.* 
        FROM resources r
        JOIN resource_domains d ON r.id = d.resource_id
        JOIN resource_products p ON r.id = p.resource_id
        WHERE r.category = 'KnowledgeGraph'
          AND r.activity_status = 'active'
          AND d.domain = 'genomics'
        GROUP BY r.id
    """)
```

### 2. Generating Analytics Reports

```python
# Get comprehensive domain statistics
with DuckDBParquetQuerier("registry/parquet") as querier:
    domain_stats = querier.execute_query("""
        SELECT d.domain, 
               COUNT(DISTINCT r.id) as resource_count,
               COUNT(DISTINCT p.product_id) as product_count,
               COUNT(DISTINCT CASE WHEN r.activity_status = 'active' THEN r.id END) as active_count
        FROM resource_domains d
        JOIN resources r ON d.resource_id = r.id
        LEFT JOIN resource_products p ON r.id = p.resource_id
        GROUP BY d.domain
        ORDER BY resource_count DESC
    """)
    
    # Export to JSON for web interface
    import json
    with open('domain_report.json', 'w') as f:
        json.dump(domain_stats, f, indent=2)
```

## Migration from Full DuckDB Database

The Parquet backend is designed to replace the full DuckDB database file while preserving all functionality:

1. **YAML files remain authoritative**: All edits should still be made to YAML files
2. **Efficient querying**: Use Parquet files for complex queries instead of full database
3. **Backward compatibility**: CLI interface maintains the same structure
4. **Web support**: Advanced search interface works with both backends

## Contributing

When adding new features to the Parquet backend:

1. Update the backend schema if needed
2. Add corresponding tests
3. Update this documentation
4. Ensure YAML files remain the source of truth
