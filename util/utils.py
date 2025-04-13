"""Utilities for working with the OBO Foundry metadata."""

import pathlib
from io import StringIO
from typing import Any, Mapping

import yaml

__all__ = [
    "get_data",
]

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
RESOURCE_DIRECTORY = ROOT.joinpath("resource").resolve()

SCHEMA_PATH = ROOT.joinpath("src", "kg_registry", "kg_registry_schema", "kg_registry_schema.json")


def get_data() -> Mapping[str, Mapping[str, Any]]:
    """Get the resource metadata for all resources by parsing the frontmatter."""
    resources = {}
    for path in RESOURCE_DIRECTORY.glob("*.md"):
        with path.open() as file:
            lines = [line.rstrip("\n") for line in file]

        assert lines[0] == "---"
        idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")

        # Load the data like it is YAML
        data = yaml.safe_load(StringIO("\n".join(lines[1:idx])))
        resources[data["id"]] = data
    return resources
