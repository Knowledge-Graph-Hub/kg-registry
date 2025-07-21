"""Parquet backend for enhanced querying of KG-Registry data."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import duckdb
import yaml

__all__ = [
    "ParquetBackend",
    "sync_yaml_to_parquet",
    "create_database",
]


class ParquetBackend:
    """Parquet backend for querying KG-Registry data.
    
    This backend uses DuckDB to process the data and exports it as Parquet files,
    which can be efficiently queried by DuckDB without loading the entire database.
    """

    def __init__(self, output_dir: Optional[str] = None):
        """Initialize Parquet backend.

        Args:
            output_dir: Directory to store Parquet files. If None, uses in-memory database only.
        """
        self.output_dir = output_dir
        # Always use in-memory database for processing
        self.conn = duckdb.connect(":memory:")
        self._init_tables()

    def _init_tables(self):
        """Initialize DuckDB tables for KG-Registry data."""
        # Create resources table
        self.conn.execute(
            """
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
        """
        )

        # Create domains table for better querying
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS resource_domains (
                resource_id VARCHAR,
                domain VARCHAR,
                PRIMARY KEY (resource_id, domain)
            )
        """
        )

        # Create products table for better querying
        self.conn.execute(
            """
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
        """
        )

    def sync_from_yaml(self, yaml_file: str) -> int:
        """Sync data from YAML file to in-memory DuckDB database.

        Args:
            yaml_file: Path to YAML file containing resources data

        Returns:
            Number of resources synced
        """
        with open(yaml_file, "r") as f:
            data = yaml.safe_load(f)

        if not data or "resources" not in data:
            return 0

        resources = data["resources"]
        synced_count = 0

        # Clear existing data
        self.conn.execute("DELETE FROM resources")
        self.conn.execute("DELETE FROM resource_domains")
        self.conn.execute("DELETE FROM resource_products")

        for resource in resources:
            if not resource.get("id"):
                continue

            # Insert into resources table
            self._insert_resource(resource)

            # Insert domains
            self._insert_domains(resource)

            # Insert products
            self._insert_products(resource)

            synced_count += 1

        # Export to Parquet if output directory is specified
        if self.output_dir and synced_count > 0:
            self.export_to_parquet()

        return synced_count

    def _insert_resource(self, resource: Dict[str, Any]):
        """Insert a resource into the resources table."""
        license_data = resource.get("license", {})

        self.conn.execute(
            """
            INSERT OR REPLACE INTO resources (
                id, name, description, category, activity_status, homepage_url, repository,
                creation_date, last_modified_date, license_id, license_label, domains,
                contacts, curators, products, layout, raw_data
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            [
                resource.get("id"),
                resource.get("name"),
                resource.get("description"),
                resource.get("category"),
                resource.get("activity_status"),
                resource.get("homepage_url"),
                resource.get("repository"),
                self._parse_date(resource.get("creation_date")),
                self._parse_date(resource.get("last_modified_date")),
                license_data.get("id") if isinstance(license_data, dict) else None,
                license_data.get("label") if isinstance(license_data, dict) else license_data,
                resource.get("domains", []),
                json.dumps(resource.get("contacts", [])),
                json.dumps(resource.get("curators", [])),
                json.dumps(resource.get("products", [])),
                resource.get("layout"),
                json.dumps(resource),
            ],
        )

    def _insert_domains(self, resource: Dict[str, Any]):
        """Insert resource domains into the resource_domains table."""
        resource_id = resource.get("id")
        domains = resource.get("domains", [])

        for domain in domains:
            self.conn.execute(
                """
                INSERT OR IGNORE INTO resource_domains (resource_id, domain)
                VALUES (?, ?)
            """,
                [resource_id, domain],
            )

    def _insert_products(self, resource: Dict[str, Any]):
        """Insert resource products into the resource_products table."""
        resource_id = resource.get("id")
        products = resource.get("products", [])

        for product in products:
            if not product.get("id"):
                continue

            self.conn.execute(
                """
                INSERT OR REPLACE INTO resource_products (
                    resource_id, product_id, product_name, product_category,
                    product_description, product_format, product_url
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                [
                    resource_id,
                    product.get("id"),
                    product.get("name"),
                    product.get("category"),
                    product.get("description"),
                    product.get("format"),
                    product.get("product_url"),
                ],
            )

    def _parse_date(self, date_str: Optional[str]) -> Optional[datetime]:
        """Parse date string to datetime object."""
        if not date_str:
            return None
        try:
            return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            return None

    def export_to_parquet(self):
        """Export all tables to Parquet files."""
        if not self.output_dir:
            raise ValueError("Output directory must be specified to export Parquet files")
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Export each table to a Parquet file
        tables = ["resources", "resource_domains", "resource_products"]
        for table in tables:
            output_path = os.path.join(self.output_dir, f"{table}.parquet")
            self.conn.execute(f"COPY {table} TO '{output_path}' (FORMAT PARQUET)")

    def query_resources(self, **filters) -> List[Dict[str, Any]]:
        """Query resources with optional filters.

        Args:
            **filters: Keyword arguments for filtering resources

        Returns:
            List of resources matching the filters
        """
        query = "SELECT * FROM resources WHERE 1=1"
        params = []

        if filters.get("category"):
            query += " AND category = ?"
            params.append(filters["category"])

        if filters.get("activity_status"):
            query += " AND activity_status = ?"
            params.append(filters["activity_status"])

        if filters.get("domain"):
            query += " AND id IN (SELECT resource_id FROM resource_domains WHERE domain = ?)"
            params.append(filters["domain"])

        if filters.get("name_contains"):
            query += " AND name ILIKE ?"
            params.append(f"%{filters['name_contains']}%")

        result_cursor = self.conn.execute(query, params)
        columns = [desc[0] for desc in result_cursor.description]
        result = result_cursor.fetchall()

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
        return self.query_resources(activity_status="active")

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

        result_cursor = self.conn.execute(query, params)
        columns = [desc[0] for desc in result_cursor.description]
        result = result_cursor.fetchall()

        return [dict(zip(columns, row)) for row in result]

    def get_resource_stats(self) -> Dict[str, Any]:
        """Get statistics about resources in the database.

        Returns:
            Dictionary with resource statistics
        """
        stats = {}

        try:
            # Total resources
            total_result = self.conn.execute("SELECT COUNT(*) FROM resources")
            total_count = total_result.fetchone()
            stats["total_resources"] = total_count[0] if total_count else 0

            # Active resources
            active_result = self.conn.execute(
                "SELECT COUNT(*) FROM resources WHERE activity_status = 'active'"
            )
            active_count = active_result.fetchone()
            stats["active_resources"] = active_count[0] if active_count else 0

            # Resources by category
            category_result = self.conn.execute(
                """
                SELECT category, COUNT(*) as count
                FROM resources
                WHERE category IS NOT NULL
                GROUP BY category
                ORDER BY count DESC
                """
            )
            category_counts = category_result.fetchall()
            stats["by_category"] = {cat: count for cat, count in category_counts}

            # Resources by domain
            domain_result = self.conn.execute(
                """
                SELECT domain, COUNT(*) as count
                FROM resource_domains
                GROUP BY domain
                ORDER BY count DESC
                """
            )
            domain_counts = domain_result.fetchall()
            stats["by_domain"] = {domain: count for domain, count in domain_counts}
        except Exception as e:
            print(f"Error getting resource stats: {e}")
            stats = {
                "total_resources": 0,
                "active_resources": 0,
                "by_category": {},
                "by_domain": {}
            }

        return stats
    
    def load_from_parquet(self, directory: str) -> bool:
        """Load data from Parquet files into in-memory DuckDB database.
        
        Args:
            directory: Directory containing Parquet files
            
        Returns:
            True if data was loaded successfully, False otherwise
        """
        tables = ["resources", "resource_domains", "resource_products"]
        success = True
        
        for table in tables:
            parquet_path = os.path.join(directory, f"{table}.parquet")
            if not os.path.exists(parquet_path):
                print(f"Warning: {parquet_path} does not exist")
                success = False
                continue
                
            self.conn.execute(f"DROP TABLE IF EXISTS {table}")
            self.conn.execute(f"CREATE TABLE {table} AS SELECT * FROM read_parquet('{parquet_path}')")
            
        return success

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


def sync_yaml_to_parquet(yaml_file: str, output_dir: str) -> int:
    """Sync YAML data to Parquet files.

    Args:
        yaml_file: Path to YAML file
        output_dir: Directory to store Parquet files

    Returns:
        Number of resources synced
    """
    with ParquetBackend(output_dir) as backend:
        return backend.sync_from_yaml(yaml_file)


def create_database(output_dir: Optional[str] = None) -> ParquetBackend:
    """Create and initialize a ParquetBackend.

    Args:
        output_dir: Directory to store Parquet files

    Returns:
        ParquetBackend instance
    """
    return ParquetBackend(output_dir)


class DuckDBParquetQuerier:
    """Utility class to query Parquet files directly using DuckDB without loading into memory."""

    def __init__(self, parquet_dir: str):
        """Initialize DuckDB Parquet querier.
        
        Args:
            parquet_dir: Directory containing Parquet files
        """
        self.parquet_dir = parquet_dir
        self.conn = duckdb.connect(":memory:")
        self._register_tables()
    
    def _register_tables(self):
        """Register Parquet files as virtual tables in DuckDB."""
        tables = ["resources", "resource_domains", "resource_products"]
        
        for table in tables:
            parquet_path = os.path.join(self.parquet_dir, f"{table}.parquet")
            if os.path.exists(parquet_path):
                self.conn.execute(f"CREATE VIEW {table} AS SELECT * FROM read_parquet('{parquet_path}')")
            else:
                print(f"Warning: {parquet_path} does not exist")
    
    def execute_query(self, query: str, params: Optional[List[Any]] = None) -> List[Dict[str, Any]]:
        """Execute a SQL query directly on Parquet files.
        
        Args:
            query: SQL query to execute
            params: Query parameters
            
        Returns:
            List of results as dictionaries
        """
        try:
            result_cursor = self.conn.execute(query, params or [])
            if result_cursor and result_cursor.description:
                columns = [desc[0] for desc in result_cursor.description]
                result = result_cursor.fetchall()
                return [dict(zip(columns, row)) for row in result]
            return []
        except Exception as e:
            print(f"Error executing query: {e}")
            return []
    
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
