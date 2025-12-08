"""Utilities for working with the KG-Registry metadata.

This module provides backward-compatible imports from common.py.
New code should use common.py directly.
"""

from common import (
    ROOT,
    RESOURCE_DIR as RESOURCE_DIRECTORY,
    SCHEMA_PATH,
    get_resources_data as get_data,
)

__all__ = [
    "ROOT",
    "RESOURCE_DIRECTORY",
    "SCHEMA_PATH",
    "get_data",
]
