#!/usr/bin/env python3
"""
Common utilities for KG-Registry scripts.

This module provides shared constants, path helpers, YAML handlers,
and file loading utilities used across multiple scripts.
"""

import pathlib
import re
from datetime import datetime
from io import StringIO
from typing import Any, Dict, List, Mapping, Optional, Tuple

import frontmatter
import yaml
from frontmatter.util import u
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO as RuamelStringIO
from ruamel.yaml.scanner import ScannerError
from yaml.parser import ParserError

__all__ = [
    # Path constants
    "HERE",
    "ROOT",
    "RESOURCE_DIR",
    "ORG_DIR",
    "REGISTRY_DIR",
    "SCHEMA_PATH",
    "SOURCE_SCHEMA_PATH",
    "YAMLLINT_CONFIG_PATH",
    # Status constants
    "INACTIVE_STATUSES",
    # Classes
    "CustomRuamelYAMLHandler",
    # Functions
    "get_resources_data",
    "get_organizations_data",
    "load_frontmatter_file",
    "load_frontmatter_files_parallel",
    "save_frontmatter_file",
    "get_yaml_text",
    "create_id_from_label",
    "get_today_iso",
    "get_separator_for_file",
]

# =============================================================================
# Path Constants
# =============================================================================

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
RESOURCE_DIR = ROOT / "resource"
ORG_DIR = ROOT / "org"
REGISTRY_DIR = ROOT / "registry"

SCHEMA_PATH = ROOT / "src" / "kg_registry" / "kg_registry_schema" / "kg_registry_schema.json"
SOURCE_SCHEMA_PATH = ROOT / "src" / "kg_registry" / "kg_registry_schema" / "schema" / "kg_registry_schema_all.yaml"
YAMLLINT_CONFIG_PATH = HERE / "config.yamllint"

# =============================================================================
# Status Constants
# =============================================================================

INACTIVE_STATUSES = ["inactive", "orphaned", "unresponsive"]

# =============================================================================
# YAML Handler
# =============================================================================


class CustomRuamelYAMLHandler(frontmatter.YAMLHandler):
    """
    Custom YAML handler using ruamel for better formatting preservation.
    
    This handler:
    - Preserves quotes in YAML values
    - Maintains proper indentation
    - Handles wide lines without wrapping
    """

    def __init__(self):
        self.myyaml = YAML()
        self.myyaml.default_flow_style = False
        self.myyaml.allow_duplicate_keys = True
        self.myyaml.indent(mapping=2, sequence=4, offset=2)
        self.myyaml.preserve_quotes = True
        self.myyaml.width = 1500
        super().__init__()

    def load(self, fm, **kwargs):
        return self.myyaml.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        stream = RuamelStringIO()
        self.myyaml.dump(data=metadata, stream=stream)
        metadata = stream.getvalue()
        # Remove trailing newline from YAML dump
        metadata = metadata[:-1] if metadata.endswith('\n') else metadata
        return u(metadata)


# =============================================================================
# File Loading Functions
# =============================================================================


def load_frontmatter_file(
    filepath: pathlib.Path,
    use_ruamel: bool = True
) -> Tuple[Optional[Dict[str, Any]], Optional[str], Optional[Exception]]:
    """
    Load a markdown file with YAML frontmatter.

    Args:
        filepath: Path to the markdown file
        use_ruamel: Whether to use ruamel YAML handler (preserves formatting)

    Returns:
        Tuple of (metadata_dict, content_str, error_or_none)
    """
    try:
        if use_ruamel:
            handler = CustomRuamelYAMLHandler()
            post = frontmatter.load(filepath, handler=handler)
        else:
            post = frontmatter.load(filepath)
        return (dict(post.metadata), post.content, None)
    except (ScannerError, ParserError) as e:
        return (None, None, e)
    except Exception as e:
        return (None, None, e)


def load_frontmatter_files_parallel(
    files: List[pathlib.Path],
    max_workers: int = 10,
    use_ruamel: bool = False
) -> List[Tuple[pathlib.Path, Dict[str, Any], str]]:
    """
    Load multiple markdown files in parallel.

    Args:
        files: List of file paths to load
        max_workers: Number of parallel workers
        use_ruamel: Whether to use ruamel YAML handler

    Returns:
        List of tuples (filepath, metadata_dict, content_str) for successfully loaded files
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    results = []
    errors = []

    def load_single(fp):
        metadata, content, error = load_frontmatter_file(fp, use_ruamel=use_ruamel)
        return (fp, metadata, content, error)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(load_single, fp): fp for fp in files}

        for future in as_completed(futures):
            fp, metadata, content, error = future.result()
            if error is not None:
                errors.append((fp, error))
            elif metadata is not None:
                results.append((fp, metadata, content))

    if errors:
        print(f"\n⚠️  Encountered {len(errors)} error(s) while loading files:")
        for fp, error in errors:
            print(f"  ERROR: Failed to parse {fp}: {error}")

    return results


def save_frontmatter_file(
    filepath: pathlib.Path,
    metadata: Dict[str, Any],
    content: str = "",
    use_ruamel: bool = True
) -> None:
    """
    Save a markdown file with YAML frontmatter.

    Args:
        filepath: Path to the markdown file
        metadata: Dictionary of frontmatter metadata
        content: Markdown content after frontmatter
        use_ruamel: Whether to use ruamel YAML handler
    """
    post = frontmatter.Post(content)
    post.metadata = metadata

    if use_ruamel:
        handler = CustomRuamelYAMLHandler()
        with open(filepath, 'wb') as f:
            frontmatter.dump(post, f, handler=handler)
    else:
        with open(filepath, 'wb') as f:
            frontmatter.dump(post, f)


def get_yaml_text(filepath: pathlib.Path) -> str:
    """
    Extract YAML frontmatter text from a markdown file.

    Args:
        filepath: Path to the markdown file

    Returns:
        The YAML frontmatter as a string (without delimiters)
    """
    with open(filepath, "r") as f:
        content = f.read()

    if not content.startswith("---"):
        return ""

    end_idx = content.find("---", 3)
    if end_idx == -1:
        return ""

    return content[3:end_idx].strip()


# =============================================================================
# Data Collection Functions
# =============================================================================


def get_resources_data() -> Mapping[str, Mapping[str, Any]]:
    """
    Get metadata for all resources by parsing frontmatter.

    Returns:
        Dictionary mapping resource IDs to their metadata
    """
    resources = {}

    for resource_dir in RESOURCE_DIR.iterdir():
        if not resource_dir.is_dir():
            continue

        # Find the main resource file (matches directory name)
        resource_file = resource_dir / f"{resource_dir.name}.md"
        if not resource_file.exists():
            continue

        metadata, _, error = load_frontmatter_file(resource_file, use_ruamel=False)
        if error:
            print(f"Warning: Error loading {resource_file}: {error}")
            continue

        if metadata and "id" in metadata:
            resources[metadata["id"]] = metadata

    return resources


def get_organizations_data() -> Mapping[str, Mapping[str, Any]]:
    """
    Get metadata for all organizations by parsing frontmatter.

    Returns:
        Dictionary mapping organization IDs to their metadata
    """
    organizations = {}

    for org_dir in ORG_DIR.iterdir():
        if not org_dir.is_dir():
            continue

        # Find the organization file
        for md_file in org_dir.glob("*.md"):
            metadata, _, error = load_frontmatter_file(md_file, use_ruamel=False)
            if error:
                print(f"Warning: Error loading {md_file}: {error}")
                continue

            if metadata and metadata.get("category") == "Organization":
                org_id = metadata.get("id", org_dir.name)
                organizations[org_id] = metadata
                break  # Only one org file per directory

    return organizations


# =============================================================================
# Utility Functions
# =============================================================================


def create_id_from_label(label: str, max_length: int = 50) -> str:
    """
    Create a valid ID from a label.

    Args:
        label: The label to convert
        max_length: Maximum length of the resulting ID

    Returns:
        A lowercase, hyphenated ID suitable for directory/file names
    """
    # Remove special characters and convert to lowercase
    id_str = re.sub(r'[^\w\s-]', '', label.lower())
    # Replace spaces with hyphens
    id_str = re.sub(r'\s+', '-', id_str)
    # Remove multiple consecutive hyphens
    id_str = re.sub(r'-+', '-', id_str)
    # Strip leading/trailing hyphens
    id_str = id_str.strip('-')
    # Truncate to max length
    if len(id_str) > max_length:
        id_str = id_str[:max_length].rstrip('-')
    return id_str


def get_today_iso() -> str:
    """
    Get today's date in ISO 8601 format for YAML.

    Returns:
        Date string like '2025-12-07T00:00:00Z'
    """
    return datetime.now().strftime("%Y-%m-%dT00:00:00Z")


def get_separator_for_file(filepath: str) -> str:
    """
    Get the appropriate column separator for an output file based on extension.

    Args:
        filepath: Path to the output file

    Returns:
        ',' for CSV, '\t' for TSV/TXT
    """
    if ".csv" in filepath.lower():
        return ","
    return "\t"
