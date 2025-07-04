"""Command line interface for KG-Registry."""

import click

from kg_registry import standardize_metadata
from kg_registry.duckdb_backend import DuckDBBackend, sync_yaml_to_duckdb
from kg_registry.constants import ROOT

__all__ = [
    "main",
]


@click.group()
def main():
    """CLI for the KG-Registry."""


@main.group()
def duckdb():
    """DuckDB backend commands."""


@duckdb.command()
@click.option(
    "--yaml-file",
    default=str(ROOT / "registry" / "kgs.yml"),
    help="Path to YAML file to sync",
)
@click.option(
    "--db-path",
    default=str(ROOT / "registry" / "kg_registry.duckdb"),
    help="Path to DuckDB database file",
)
def sync(yaml_file: str, db_path: str):
    """Sync YAML data to DuckDB database."""
    try:
        count = sync_yaml_to_duckdb(yaml_file, db_path)
        click.echo(f"Successfully synced {count} resources to DuckDB database at {db_path}")
    except Exception as e:
        click.echo(f"Error syncing data: {e}", err=True)
        raise click.Abort()


@duckdb.command()
@click.option(
    "--db-path",
    default=str(ROOT / "registry" / "kg_registry.duckdb"),
    help="Path to DuckDB database file",
)
def stats(db_path: str):
    """Show statistics about the DuckDB database."""
    try:
        with DuckDBBackend(db_path) as backend:
            stats = backend.get_resource_stats()
            click.echo(f"Total resources: {stats['total_resources']}")
            click.echo(f"Active resources: {stats['active_resources']}")
            click.echo("\nBy category:")
            for category, count in stats['by_category'].items():
                click.echo(f"  {category}: {count}")
            click.echo("\nBy domain:")
            for domain, count in stats['by_domain'].items():
                click.echo(f"  {domain}: {count}")
    except Exception as e:
        click.echo(f"Error getting stats: {e}", err=True)
        raise click.Abort()


@duckdb.command()
@click.option(
    "--db-path",
    default=str(ROOT / "registry" / "kg_registry.duckdb"),
    help="Path to DuckDB database file",
)
@click.option("--category", help="Filter by category")
@click.option("--domain", help="Filter by domain")
@click.option("--status", help="Filter by activity status")
@click.option("--search", help="Search in name or description")
def query(db_path: str, category: str, domain: str, status: str, search: str):
    """Query resources from DuckDB database."""
    try:
        with DuckDBBackend(db_path) as backend:
            filters = {}
            if category:
                filters['category'] = category
            if domain:
                filters['domain'] = domain
            if status:
                filters['activity_status'] = status
            if search:
                filters['name_contains'] = search
                
            if search:
                resources = backend.search_resources(search)
            else:
                resources = backend.query_resources(**filters)
                
            click.echo(f"Found {len(resources)} resources:")
            for resource in resources:
                click.echo(f"  {resource['id']}: {resource['name']} ({resource['category']})")
    except Exception as e:
        click.echo(f"Error querying data: {e}", err=True)
        raise click.Abort()


main.add_command(standardize_metadata.main)

if __name__ == "__main__":
    main()
