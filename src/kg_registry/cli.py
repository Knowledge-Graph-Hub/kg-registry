"""Command line interface for KG-Registry."""

import click

from kg_registry import standardize_metadata

__all__ = [
    "main",
]


@click.group()
def main():
    """CLI for the KG-Registry."""


main.add_command(standardize_metadata.main)

if __name__ == "__main__":
    main()
