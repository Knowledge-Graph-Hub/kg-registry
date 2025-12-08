#!/usr/bin/env python3

"""
Parallel file loading utility for extract-metadata.py

This module provides backward-compatible imports from common.py.
New code should use common.py directly.
"""

from common import (
    load_frontmatter_file,
    load_frontmatter_files_parallel,
)
from typing import List, Tuple, Dict, Any, Optional
import pathlib


def load_md_single(fn: str) -> Tuple[str, Optional[Dict[str, Any]], Optional[str], Optional[Exception]]:
    """
    Load a single markdown file.

    Returns:
        Tuple of (filename, metadata_dict, content_str, exception_or_none)
    """
    metadata, content, error = load_frontmatter_file(pathlib.Path(fn), use_ruamel=False)
    return (fn, metadata, content, error)


def load_md_parallel(files: List[str], max_workers: int = 10) -> List[Tuple[str, Dict[str, Any], str]]:
    """
    Load multiple markdown files in parallel.

    Args:
        files: List of file paths to load
        max_workers: Number of parallel workers (default: 10)

    Returns:
        List of tuples (filename, metadata_dict, content_str) for successfully loaded files
        Prints errors for failed files
    """
    paths = [pathlib.Path(f) for f in files]
    results = load_frontmatter_files_parallel(paths, max_workers=max_workers, use_ruamel=False)
    # Convert from (path, metadata, content) to (str, metadata, content)
    return [(str(fp), metadata, content) for fp, metadata, content in results]


def filter_library_files(results: List[Tuple[str, Dict[str, Any], str]]) -> List[Tuple[Dict[str, Any], str]]:
    """
    Filter results to only include files where the object ID matches the parent directory name.
    This identifies the main resource files vs product files.

    Args:
        results: List of (filename, metadata, content) tuples

    Returns:
        List of (metadata, content) tuples for library files only
    """
    library = []
    for fn, metadata, content in results:
        if metadata and metadata.get("id") == pathlib.Path(fn).parent.name:
            library.append((metadata, content))
    return library

