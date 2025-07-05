# DuckDB Backend for KG-Registry

The KG-Registry now includes a DuckDB backend that provides enhanced querying capabilities while maintaining the human-readable YAML files in the `resource` directory.

## Features

- **Fast Querying**: DuckDB provides efficient SQL-based queries for large datasets
- **Human-Readable Data**: Original YAML files remain unchanged and editable
- **Rich Query Interface**: Python API and CLI commands for querying resources
- **Statistics**: Built-in analytics and statistics generation
- **Synchronization**: Easy sync from YAML files to DuckDB database

## Installation

DuckDB is included as a dependency in the project. To install:

```bash
# Using poetry (recommended)
poetry install

# Or using pip
pip install duckdb
```

## Quick Start

### 1. Sync YAML Data to DuckDB

```bash
# Sync the registry data to DuckDB
python -m kg_registry.cli duckdb sync --yaml-file registry/kgs.yml --db-path registry/kg_registry.duckdb
```

### 2. Query Resources

```bash
# Get statistics about the registry
python -m kg_registry.cli duckdb stats --db-path registry/kg_registry.duckdb

# Query resources by category
python -m kg_registry.cli duckdb query --category KnowledgeGraph --db-path registry/kg_registry.duckdb

# Query resources by domain
python -m kg_registry.cli duckdb query --domain genomics --db-path registry/kg_registry.duckdb

# Search resources by name or description
python -m kg_registry.cli duckdb query --search "drug" --db-path registry/kg_registry.duckdb
```

## Python API

### Basic Usage

```python
from kg_registry.duckdb_backend import DuckDBBackend

# Create backend and sync data
backend = DuckDBBackend("registry/kg_registry.duckdb")
count = backend.sync_from_yaml("registry/kgs.yml")
print(f"Synced {count} resources")

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

backend.close()
```

### Using Context Manager

```python
from kg_registry.duckdb_backend import DuckDBBackend

with DuckDBBackend("registry/kg_registry.duckdb") as backend:
    backend.sync_from_yaml("registry/kgs.yml")
    
    # Query active knowledge graphs in genomics
    genomics_kgs = backend.query_resources(
        category="KnowledgeGraph",
        activity_status="active",
        domain="genomics"
    )
    
    for kg in genomics_kgs:
        print(f"{kg['id']}: {kg['name']}")
```

### Custom SQL Queries

```python
from kg_registry.duckdb_backend import DuckDBBackend

with DuckDBBackend("registry/kg_registry.duckdb") as backend:
    # Custom SQL query
    query = """
        SELECT r.category, COUNT(*) as count
        FROM resources r
        WHERE r.activity_status = 'active'
        GROUP BY r.category
        ORDER BY count DESC
    """
    
    result = backend.conn.execute(query).fetchall()
    for category, count in result:
        print(f"{category}: {count}")
```

## CLI Commands

### `duckdb sync`

Synchronize YAML data to DuckDB database.

```bash
python -m kg_registry.cli duckdb sync [OPTIONS]

Options:
  --yaml-file TEXT  Path to YAML file to sync (default: registry/kgs.yml)
  --db-path TEXT    Path to DuckDB database file (default: registry/kg_registry.duckdb)
```

### `duckdb stats`

Show statistics about the DuckDB database.

```bash
python -m kg_registry.cli duckdb stats [OPTIONS]

Options:
  --db-path TEXT    Path to DuckDB database file
```

### `duckdb query`

Query resources from DuckDB database.

```bash
python -m kg_registry.cli duckdb query [OPTIONS]

Options:
  --category TEXT   Filter by category
  --domain TEXT     Filter by domain
  --status TEXT     Filter by activity status
  --search TEXT     Search in name or description
  --db-path TEXT    Path to DuckDB database file
```

## Database Schema

The DuckDB backend creates three main tables:

### `resources` table
- `id` (VARCHAR): Resource identifier
- `name` (VARCHAR): Resource name
- `description` (TEXT): Resource description
- `category` (VARCHAR): Resource category
- `activity_status` (VARCHAR): Activity status
- `homepage_url` (VARCHAR): Homepage URL
- `repository` (VARCHAR): Repository URL
- `creation_date` (TIMESTAMP): Creation date
- `last_modified_date` (TIMESTAMP): Last modified date
- `license_id` (VARCHAR): License identifier
- `license_label` (VARCHAR): License label
- `domains` (VARCHAR[]): Array of domains
- `contacts` (JSON): Contact information
- `curators` (JSON): Curator information
- `products` (JSON): Product information
- `raw_data` (JSON): Complete raw YAML data

### `resource_domains` table
- `resource_id` (VARCHAR): Resource identifier
- `domain` (VARCHAR): Domain name

### `resource_products` table
- `resource_id` (VARCHAR): Resource identifier
- `product_id` (VARCHAR): Product identifier
- `product_name` (VARCHAR): Product name
- `product_category` (VARCHAR): Product category
- `product_description` (TEXT): Product description
- `product_format` (VARCHAR): Product format
- `product_url` (VARCHAR): Product URL

## Benefits

1. **Performance**: Complex queries execute much faster than processing YAML files
2. **Flexibility**: SQL queries allow for complex filtering and analytics
3. **Scalability**: DuckDB can handle large datasets efficiently
4. **Compatibility**: Original YAML files remain unchanged for human editing
5. **Analytics**: Built-in statistics and reporting capabilities

## Data Synchronization

The DuckDB backend maintains a complete copy of the YAML data. To keep it synchronized:

1. **Manual Sync**: Run the `duckdb sync` command after updating YAML files
2. **Automated Sync**: Integrate the sync command into your CI/CD pipeline
3. **Programmatic Sync**: Use the Python API to sync data in scripts

## Example Use Cases

### 1. Finding Resources by Multiple Criteria
```python
# Find active knowledge graphs in genomics with products
genomics_kgs_with_products = backend.query_resources(
    category="KnowledgeGraph",
    activity_status="active",
    domain="genomics"
)

# Filter those with products
kgs_with_products = [
    kg for kg in genomics_kgs_with_products
    if json.loads(kg['raw_data']).get('products', [])
]
```

### 2. Generating Reports
```python
# Generate domain statistics
stats = backend.get_resource_stats()
domain_report = {
    'total_resources': stats['total_resources'],
    'active_resources': stats['active_resources'],
    'domains': stats['by_domain']
}

# Export to JSON for web interface
import json
with open('domain_report.json', 'w') as f:
    json.dump(domain_report, f, indent=2)
```

### 3. Complex Analytics
```python
# Find resources with most products
query = """
    SELECT r.id, r.name, COUNT(p.product_id) as product_count
    FROM resources r
    JOIN resource_products p ON r.id = p.resource_id
    GROUP BY r.id, r.name
    ORDER BY product_count DESC
    LIMIT 10
"""

top_resources = backend.conn.execute(query).fetchall()
```

## Migration from YAML-only Querying

The DuckDB backend is designed to complement, not replace, the existing YAML-based system:

1. **YAML files remain authoritative**: All edits should still be made to YAML files
2. **Read-only querying**: Use DuckDB for complex queries and analytics
3. **Synchronization**: Regularly sync changes from YAML to DuckDB
4. **Backward compatibility**: Existing scripts continue to work with YAML files

## Testing

Run the DuckDB backend tests:

```bash
# Run all DuckDB tests
python -m pytest tests/test_duckdb_backend.py -v

# Run specific test
python -m pytest tests/test_duckdb_backend.py::TestDuckDBBackend::test_query_resources -v
```

## Contributing

When adding new features to the DuckDB backend:

1. Update the database schema if needed
2. Add corresponding tests in `tests/test_duckdb_backend.py`
3. Update this documentation
4. Ensure YAML files remain the source of truth