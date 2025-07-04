"""DuckDB backend for enhanced querying of KG-Registry data."""

import json
import pathlib
import tempfile
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

import duckdb
import yaml

from kg_registry.constants import RESOURCE_DIRECTORY, ROOT

__all__ = [
    "DuckDBBackend",
    "sync_yaml_to_duckdb",
    "create_database",
]


class DuckDBBackend:
    """DuckDB backend for querying KG-Registry data."""

    def __init__(self, db_path: Optional[str] = None):
        """Initialize DuckDB backend.
        
        Args:
            db_path: Path to DuckDB database file. If None, uses in-memory database.
        """
        self.db_path = db_path or ":memory:"
        self.conn = duckdb.connect(self.db_path)
        self._init_tables()

    def _init_tables(self):
        """Initialize DuckDB tables for KG-Registry data."""
        # Create resources table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS resources (
                id VARCHAR PRIMARY KEY,
                name VARCHAR,
                description TEXT,
                category VARCHAR,
                activity_status VARCHAR,
                homepage_url VARCHAR,
                repository VARCHAR,
                creation_date TIMESTAMP,
                last_modified_date TIMESTAMP,
                license_id VARCHAR,
                license_label VARCHAR,
                domains VARCHAR[],
                contacts JSON,
                curators JSON,
                products JSON,
                layout VARCHAR,
                raw_data JSON,
                sync_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create domains table for better querying
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS resource_domains (
                resource_id VARCHAR,
                domain VARCHAR,
                PRIMARY KEY (resource_id, domain)
            )
        """)

        # Create products table for better querying
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS resource_products (
                resource_id VARCHAR,
                product_id VARCHAR,
                product_name VARCHAR,
                product_category VARCHAR,
                product_description TEXT,
                product_format VARCHAR,
                product_url VARCHAR,
                PRIMARY KEY (resource_id, product_id)
            )
        """)

    def sync_from_yaml(self, yaml_file: str) -> int:
        """Sync data from YAML file to DuckDB.
        
        Args:
            yaml_file: Path to YAML file containing resources data
            
        Returns:
            Number of resources synced
        """
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
            
        if not data or 'resources' not in data:
            return 0
            
        resources = data['resources']
        synced_count = 0
        
        # Clear existing data
        self.conn.execute("DELETE FROM resources")
        self.conn.execute("DELETE FROM resource_domains")
        self.conn.execute("DELETE FROM resource_products")
        
        for resource in resources:
            if not resource.get('id'):
                continue
                
            # Insert into resources table
            self._insert_resource(resource)
            
            # Insert domains
            self._insert_domains(resource)
            
            # Insert products
            self._insert_products(resource)
            
            synced_count += 1
            
        return synced_count

    def _insert_resource(self, resource: Dict[str, Any]):
        """Insert a resource into the resources table."""
        license_data = resource.get('license', {})
        
        self.conn.execute("""
            INSERT OR REPLACE INTO resources (
                id, name, description, category, activity_status, homepage_url, repository,
                creation_date, last_modified_date, license_id, license_label, domains,
                contacts, curators, products, layout, raw_data
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            resource.get('id'),
            resource.get('name'),
            resource.get('description'),
            resource.get('category'),
            resource.get('activity_status'),
            resource.get('homepage_url'),
            resource.get('repository'),
            self._parse_date(resource.get('creation_date')),
            self._parse_date(resource.get('last_modified_date')),
            license_data.get('id') if isinstance(license_data, dict) else None,
            license_data.get('label') if isinstance(license_data, dict) else license_data,
            resource.get('domains', []),
            json.dumps(resource.get('contacts', [])),
            json.dumps(resource.get('curators', [])),
            json.dumps(resource.get('products', [])),
            resource.get('layout'),
            json.dumps(resource)
        ])

    def _insert_domains(self, resource: Dict[str, Any]):
        """Insert resource domains into the resource_domains table."""
        resource_id = resource.get('id')
        domains = resource.get('domains', [])
        
        for domain in domains:
            self.conn.execute("""
                INSERT OR IGNORE INTO resource_domains (resource_id, domain)
                VALUES (?, ?)
            """, [resource_id, domain])

    def _insert_products(self, resource: Dict[str, Any]):
        """Insert resource products into the resource_products table."""
        resource_id = resource.get('id')
        products = resource.get('products', [])
        
        for product in products:
            if not product.get('id'):
                continue
                
            self.conn.execute("""
                INSERT OR REPLACE INTO resource_products (
                    resource_id, product_id, product_name, product_category,
                    product_description, product_format, product_url
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [
                resource_id,
                product.get('id'),
                product.get('name'),
                product.get('category'),
                product.get('description'),
                product.get('format'),
                product.get('product_url')
            ])

    def _parse_date(self, date_str: Optional[str]) -> Optional[datetime]:
        """Parse date string to datetime object."""
        if not date_str:
            return None
        try:
            return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        except (ValueError, AttributeError):
            return None

    def query_resources(self, **filters) -> List[Dict[str, Any]]:
        """Query resources with optional filters.
        
        Args:
            **filters: Keyword arguments for filtering resources
            
        Returns:
            List of resources matching the filters
        """
        query = "SELECT * FROM resources WHERE 1=1"
        params = []
        
        if filters.get('category'):
            query += " AND category = ?"
            params.append(filters['category'])
            
        if filters.get('activity_status'):
            query += " AND activity_status = ?"
            params.append(filters['activity_status'])
            
        if filters.get('domain'):
            query += " AND id IN (SELECT resource_id FROM resource_domains WHERE domain = ?)"
            params.append(filters['domain'])
            
        if filters.get('name_contains'):
            query += " AND name ILIKE ?"
            params.append(f"%{filters['name_contains']}%")
            
        result = self.conn.execute(query, params).fetchall()
        columns = [desc[0] for desc in self.conn.description]
        
        return [dict(zip(columns, row)) for row in result]

    def query_by_domain(self, domain: str) -> List[Dict[str, Any]]:
        """Query resources by domain.
        
        Args:
            domain: Domain to filter by
            
        Returns:
            List of resources in the specified domain
        """
        return self.query_resources(domain=domain)

    def query_active_resources(self) -> List[Dict[str, Any]]:
        """Query all active resources.
        
        Returns:
            List of active resources
        """
        return self.query_resources(activity_status='active')

    def search_resources(self, search_term: str) -> List[Dict[str, Any]]:
        """Search resources by name or description.
        
        Args:
            search_term: Term to search for
            
        Returns:
            List of resources matching the search term
        """
        query = """
            SELECT * FROM resources 
            WHERE name ILIKE ? OR description ILIKE ?
            ORDER BY name
        """
        params = [f"%{search_term}%", f"%{search_term}%"]
        
        result = self.conn.execute(query, params).fetchall()
        columns = [desc[0] for desc in self.conn.description]
        
        return [dict(zip(columns, row)) for row in result]

    def get_resource_stats(self) -> Dict[str, Any]:
        """Get statistics about resources in the database.
        
        Returns:
            Dictionary with resource statistics
        """
        stats = {}
        
        # Total resources
        stats['total_resources'] = self.conn.execute(
            "SELECT COUNT(*) FROM resources"
        ).fetchone()[0]
        
        # Active resources
        stats['active_resources'] = self.conn.execute(
            "SELECT COUNT(*) FROM resources WHERE activity_status = 'active'"
        ).fetchone()[0]
        
        # Resources by category
        category_counts = self.conn.execute("""
            SELECT category, COUNT(*) as count 
            FROM resources 
            WHERE category IS NOT NULL 
            GROUP BY category 
            ORDER BY count DESC
        """).fetchall()
        stats['by_category'] = {cat: count for cat, count in category_counts}
        
        # Resources by domain
        domain_counts = self.conn.execute("""
            SELECT domain, COUNT(*) as count 
            FROM resource_domains 
            GROUP BY domain 
            ORDER BY count DESC
        """).fetchall()
        stats['by_domain'] = {domain: count for domain, count in domain_counts}
        
        return stats

    def close(self):
        """Close the DuckDB connection."""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


def sync_yaml_to_duckdb(yaml_file: str, db_path: str = None) -> int:
    """Sync YAML data to DuckDB database.
    
    Args:
        yaml_file: Path to YAML file
        db_path: Path to DuckDB database (optional)
        
    Returns:
        Number of resources synced
    """
    with DuckDBBackend(db_path) as backend:
        return backend.sync_from_yaml(yaml_file)


def create_database(db_path: str = None) -> DuckDBBackend:
    """Create and initialize a DuckDB database.
    
    Args:
        db_path: Path to DuckDB database file
        
    Returns:
        DuckDBBackend instance
    """
    return DuckDBBackend(db_path)