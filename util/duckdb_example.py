#!/usr/bin/env python3
"""
Example script showing how to use the DuckDB backend for enhanced querying.

This script demonstrates how the DuckDB backend can be used to perform
complex queries that would be inefficient with the raw YAML data.
"""

import json
import sys
from pathlib import Path

# Add the source directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from kg_registry.duckdb_backend import DuckDBBackend

def main():
    """Main function demonstrating DuckDB backend usage."""
    
    # Path to the registry data and database
    registry_path = Path(__file__).parent.parent / "registry" / "kgs.yml"
    db_path = Path(__file__).parent.parent / "registry" / "kg_registry.duckdb"
    
    # Create and sync the DuckDB backend
    print("Creating DuckDB backend and syncing data...")
    backend = DuckDBBackend(str(db_path))
    count = backend.sync_from_yaml(str(registry_path))
    print(f"Synced {count} resources to DuckDB")
    
    # Example 1: Get statistics
    print("\n=== Resource Statistics ===")
    stats = backend.get_resource_stats()
    print(f"Total resources: {stats['total_resources']}")
    print(f"Active resources: {stats['active_resources']}")
    
    print("\nTop 5 categories:")
    for category, count in list(stats['by_category'].items())[:5]:
        print(f"  {category}: {count}")
    
    print("\nTop 10 domains:")
    for domain, count in list(stats['by_domain'].items())[:10]:
        print(f"  {domain}: {count}")
    
    # Example 2: Complex query - Active Knowledge Graphs in genomics
    print("\n=== Active Knowledge Graphs in Genomics ===")
    genomics_kgs = backend.query_resources(
        category="KnowledgeGraph",
        activity_status="active",
        domain="genomics"
    )
    print(f"Found {len(genomics_kgs)} active knowledge graphs in genomics:")
    for kg in genomics_kgs:
        print(f"  {kg['id']}: {kg['name']}")
    
    # Example 3: Search for resources related to "drug"
    print("\n=== Resources Related to 'Drug' ===")
    drug_resources = backend.search_resources("drug")
    print(f"Found {len(drug_resources)} resources related to 'drug':")
    for resource in drug_resources[:10]:  # Show first 10
        print(f"  {resource['id']}: {resource['name']} ({resource['category']})")
    
    # Example 4: Query resources by domain
    print("\n=== Resources in Clinical Domain ===")
    clinical_resources = backend.query_by_domain("clinical")
    print(f"Found {len(clinical_resources)} resources in clinical domain:")
    for resource in clinical_resources[:5]:  # Show first 5
        print(f"  {resource['id']}: {resource['name']} ({resource['category']})")
    
    # Example 5: Custom SQL query
    print("\n=== Custom SQL Query: Resources with Most Products ===")
    query = """
        SELECT r.id, r.name, r.category, COUNT(p.product_id) as product_count
        FROM resources r
        LEFT JOIN resource_products p ON r.id = p.resource_id
        WHERE r.activity_status = 'active'
        GROUP BY r.id, r.name, r.category
        HAVING COUNT(p.product_id) > 0
        ORDER BY product_count DESC
        LIMIT 10
    """
    
    result = backend.conn.execute(query).fetchall()
    columns = [desc[0] for desc in backend.conn.description]
    
    print("Top 10 active resources with most products:")
    for row in result:
        resource_data = dict(zip(columns, row))
        print(f"  {resource_data['id']}: {resource_data['name']} "
              f"({resource_data['category']}) - {resource_data['product_count']} products")
    
    # Example 6: Generate JSON output for web consumption
    print("\n=== Generating JSON for Web Interface ===")
    web_data = {
        "stats": stats,
        "active_knowledge_graphs": [
            {
                "id": kg['id'],
                "name": kg['name'],
                "domains": json.loads(kg['raw_data']).get('domains', []),
                "homepage_url": kg['homepage_url']
            }
            for kg in backend.query_resources(
                category="KnowledgeGraph",
                activity_status="active"
            )
        ]
    }
    
    output_file = Path(__file__).parent.parent / "registry" / "kg_registry_enhanced.json"
    with open(output_file, 'w') as f:
        json.dump(web_data, f, indent=2, default=str)
    
    print(f"Enhanced data written to {output_file}")
    
    backend.close()
    print("\nDuckDB backend demonstration complete!")

if __name__ == "__main__":
    main()