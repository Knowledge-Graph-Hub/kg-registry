#!/usr/bin/env python3
"""
Demo script showcasing DuckDB backend capabilities for KG-Registry.

This script demonstrates the improved querying performance and capabilities
provided by the DuckDB backend while maintaining the human-readable YAML files.
"""

import json
import sys
import time
from pathlib import Path

# Add the source directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from kg_registry.duckdb_backend import DuckDBBackend

def demo_performance_comparison():
    """Demonstrate performance improvements with DuckDB."""
    
    print("=== Performance Comparison Demo ===")
    print("This demo shows the performance benefits of using DuckDB for querying.")
    print()
    
    # Path to the registry data
    registry_path = Path(__file__).parent.parent / "registry" / "kgs.yml"
    
    # Load YAML data directly (traditional approach)
    print("1. Loading YAML data directly (traditional approach)...")
    start_time = time.time()
    
    import yaml
    with open(registry_path, 'r') as f:
        yaml_data = yaml.safe_load(f)
    
    yaml_load_time = time.time() - start_time
    print(f"   YAML loading time: {yaml_load_time:.3f} seconds")
    print(f"   Total resources: {len(yaml_data['resources'])}")
    
    # Filter resources by category using Python (traditional approach)
    start_time = time.time()
    knowledge_graphs = [
        r for r in yaml_data['resources'] 
        if r.get('category') == 'KnowledgeGraph' and r.get('activity_status') == 'active'
    ]
    yaml_filter_time = time.time() - start_time
    print(f"   Python filtering time: {yaml_filter_time:.3f} seconds")
    print(f"   Active Knowledge Graphs found: {len(knowledge_graphs)}")
    print()
    
    # DuckDB approach
    print("2. Using DuckDB backend (enhanced approach)...")
    start_time = time.time()
    
    # Create in-memory database for demo
    backend = DuckDBBackend()
    sync_count = backend.sync_from_yaml(str(registry_path))
    
    duckdb_sync_time = time.time() - start_time
    print(f"   DuckDB sync time: {duckdb_sync_time:.3f} seconds")
    print(f"   Synced resources: {sync_count}")
    
    # Query using DuckDB
    start_time = time.time()
    duckdb_kgs = backend.query_resources(
        category='KnowledgeGraph',
        activity_status='active'
    )
    duckdb_query_time = time.time() - start_time
    print(f"   DuckDB query time: {duckdb_query_time:.3f} seconds")
    print(f"   Active Knowledge Graphs found: {len(duckdb_kgs)}")
    
    # Performance summary
    print()
    print("Performance Summary:")
    print(f"   YAML approach: {yaml_load_time + yaml_filter_time:.3f} seconds")
    print(f"   DuckDB approach: {duckdb_sync_time + duckdb_query_time:.3f} seconds")
    
    if yaml_filter_time > 0:
        speedup = yaml_filter_time / duckdb_query_time if duckdb_query_time > 0 else float('inf')
        print(f"   Query speedup: {speedup:.1f}x faster")
    
    backend.close()
    print()

def demo_complex_queries():
    """Demonstrate complex querying capabilities."""
    
    print("=== Complex Querying Demo ===")
    print("This demo shows advanced querying capabilities with DuckDB.")
    print()
    
    registry_path = Path(__file__).parent.parent / "registry" / "kgs.yml"
    
    with DuckDBBackend() as backend:
        backend.sync_from_yaml(str(registry_path))
        
        # 1. Multi-criteria filtering
        print("1. Multi-criteria filtering:")
        print("   Finding active Knowledge Graphs in genomics domain...")
        
        genomics_kgs = backend.query_resources(
            category='KnowledgeGraph',
            activity_status='active',
            domain='genomics'
        )
        
        print(f"   Found {len(genomics_kgs)} resources:")
        for kg in genomics_kgs[:5]:  # Show first 5
            print(f"     - {kg['id']}: {kg['name']}")
        if len(genomics_kgs) > 5:
            print(f"     ... and {len(genomics_kgs) - 5} more")
        print()
        
        # 2. Text search across multiple fields
        print("2. Text search across multiple fields:")
        print("   Searching for resources related to 'protein'...")
        
        protein_resources = backend.search_resources('protein')
        print(f"   Found {len(protein_resources)} resources:")
        for resource in protein_resources[:5]:  # Show first 5
            print(f"     - {resource['id']}: {resource['name']} ({resource['category']})")
        if len(protein_resources) > 5:
            print(f"     ... and {len(protein_resources) - 5} more")
        print()
        
        # 3. Custom SQL analytics
        print("3. Custom SQL analytics:")
        print("   Resources with most products (top 5)...")
        
        query = """
            SELECT r.id, r.name, r.category, COUNT(p.product_id) as product_count
            FROM resources r
            LEFT JOIN resource_products p ON r.id = p.resource_id
            WHERE r.activity_status = 'active'
            GROUP BY r.id, r.name, r.category
            HAVING COUNT(p.product_id) > 0
            ORDER BY product_count DESC
            LIMIT 5
        """
        
        result = backend.conn.execute(query).fetchall()
        columns = [desc[0] for desc in backend.conn.description]
        
        for row in result:
            resource_data = dict(zip(columns, row))
            print(f"     - {resource_data['id']}: {resource_data['name']} "
                  f"({resource_data['category']}) - {resource_data['product_count']} products")
        print()
        
        # 4. Domain analytics
        print("4. Domain analytics:")
        print("   Top 10 domains by resource count...")
        
        stats = backend.get_resource_stats()
        top_domains = list(stats['by_domain'].items())[:10]
        
        for domain, count in top_domains:
            print(f"     - {domain}: {count} resources")
        print()

def demo_data_integrity():
    """Demonstrate that YAML files remain unchanged."""
    
    print("=== Data Integrity Demo ===")
    print("This demo shows that YAML files remain unchanged after DuckDB operations.")
    print()
    
    registry_path = Path(__file__).parent.parent / "registry" / "kgs.yml"
    
    # Get original file hash
    import hashlib
    with open(registry_path, 'rb') as f:
        original_hash = hashlib.md5(f.read()).hexdigest()
    
    print(f"Original YAML file hash: {original_hash}")
    
    # Perform DuckDB operations
    print("Performing DuckDB operations...")
    
    with DuckDBBackend() as backend:
        # Sync data
        count = backend.sync_from_yaml(str(registry_path))
        print(f"   Synced {count} resources")
        
        # Perform various queries
        active_count = len(backend.query_active_resources())
        print(f"   Queried {active_count} active resources")
        
        search_results = backend.search_resources('knowledge')
        print(f"   Found {len(search_results)} resources matching 'knowledge'")
        
        stats = backend.get_resource_stats()
        print(f"   Generated statistics for {stats['total_resources']} resources")
    
    # Check file hash again
    with open(registry_path, 'rb') as f:
        final_hash = hashlib.md5(f.read()).hexdigest()
    
    print(f"Final YAML file hash: {final_hash}")
    
    if original_hash == final_hash:
        print("✅ YAML file remains unchanged after DuckDB operations")
    else:
        print("❌ YAML file was modified (this should not happen)")
    
    print()

def main():
    """Main demo function."""
    
    print("KG-Registry DuckDB Backend Demo")
    print("=" * 50)
    print()
    
    # Check if registry file exists
    registry_path = Path(__file__).parent.parent / "registry" / "kgs.yml"
    if not registry_path.exists():
        print(f"Error: Registry file not found at {registry_path}")
        print("Please run this demo from the kg-registry directory.")
        return
    
    try:
        demo_performance_comparison()
        demo_complex_queries()
        demo_data_integrity()
        
        print("Demo completed successfully!")
        print()
        print("Key Benefits of DuckDB Backend:")
        print("- Faster querying for large datasets")
        print("- Complex SQL-based analytics")
        print("- Multi-criteria filtering")
        print("- Full-text search capabilities")
        print("- Statistics and reporting")
        print("- YAML files remain unchanged and editable")
        print()
        print("Try the CLI commands:")
        print("  python -m kg_registry.cli duckdb sync")
        print("  python -m kg_registry.cli duckdb stats")
        print("  python -m kg_registry.cli duckdb query --category KnowledgeGraph")
        
    except Exception as e:
        print(f"Error running demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()