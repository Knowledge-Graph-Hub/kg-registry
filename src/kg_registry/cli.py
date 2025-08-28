"""Command line interface for KG-Registry."""

import click

from kg_registry import standardize_metadata
from kg_registry.constants import ROOT
from kg_registry.parquet_backend import DuckDBParquetQuerier, ParquetBackend, sync_yaml_to_parquet

__all__ = [
    "main",
]


@click.group()
def main():
    """CLI for the KG-Registry."""


@main.group()
def duckdb():
    """Commands for the DuckDB backend."""
    pass


@main.group()
def parquet():
    """Commands for the Parquet backend."""
    pass


@parquet.command(name="sync")
@click.option(
    "--yaml-file",
    default=str(ROOT / "registry" / "kgs.yml"),
    help="Path to YAML file to sync",
)
@click.option(
    "--output-dir",
    default=str(ROOT / "registry" / "parquet"),
    help="Directory to store Parquet files",
)
def parquet_sync(yaml_file: str, output_dir: str):
    """Sync YAML data to Parquet files."""
    try:
        count = sync_yaml_to_parquet(yaml_file, output_dir)
        click.echo(f"Successfully synced {count} resources to Parquet files in {output_dir}")
    except Exception as e:
        click.echo(f"Error syncing data: {e}", err=True)
        raise click.Abort()


@parquet.command(name="stats")
@click.option(
    "--parquet-dir",
    default=str(ROOT / "registry" / "parquet"),
    help="Directory containing Parquet files",
)
def parquet_stats(parquet_dir: str):
    """Show statistics about the resources in Parquet files."""
    try:
        with ParquetBackend() as backend:
            backend.load_from_parquet(parquet_dir)
            stats = backend.get_resource_stats()
            click.echo(f"Total resources: {stats['total_resources']}")
            click.echo(f"Active resources: {stats['active_resources']}")
            click.echo("\nBy category:")
            for category, count in stats["by_category"].items():
                click.echo(f"  {category}: {count}")
            click.echo("\nBy domain:")
            for domain, count in stats["by_domain"].items():
                click.echo(f"  {domain}: {count}")
    except Exception as e:
        click.echo(f"Error getting stats: {e}", err=True)
        raise click.Abort()


@parquet.command(name="query")
@click.option(
    "--parquet-dir",
    default=str(ROOT / "registry" / "parquet"),
    help="Directory containing Parquet files",
)
@click.option("--category", help="Filter by category")
@click.option("--domain", help="Filter by domain")
@click.option("--status", help="Filter by activity status")
@click.option("--search", help="Search in name or description")
def parquet_query(parquet_dir: str, category: str, domain: str, status: str, search: str):
    """Query resources from Parquet files."""
    try:
        # Use DuckDBParquetQuerier for direct querying without loading into memory
        with DuckDBParquetQuerier(parquet_dir) as querier:
            if search:
                # Build search query
                search_query = """
                    SELECT * FROM resources
                    WHERE name ILIKE ? OR description ILIKE ?
                    ORDER BY name
                """
                search_params = [f"%{search}%", f"%{search}%"]
                resources = querier.execute_query(search_query, search_params)
            else:
                # Build filtered query
                query = "SELECT * FROM resources WHERE 1=1"
                params = []

                if category:
                    query += " AND category = ?"
                    params.append(category)

                if status:
                    query += " AND activity_status = ?"
                    params.append(status)

                if domain:
                    query += (
                        " AND id IN (SELECT resource_id FROM resource_domains WHERE domain = ?)"
                    )
                    params.append(domain)

                resources = querier.execute_query(query, params)

            click.echo(f"Found {len(resources)} resources:")
            for resource in resources:
                click.echo(f"  {resource['id']}: {resource['name']} ({resource['category']})")
    except Exception as e:
        click.echo(f"Error querying resources: {e}", err=True)
        raise click.Abort()


main.add_command(standardize_metadata.main)

if __name__ == "__main__":
    main()
