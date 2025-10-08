#!/usr/bin/env python3

"""
Parallel file loading utility for extract-metadata.py

This module provides parallel file loading functionality to speed up
the concat operation in extract-metadata.py by loading multiple markdown
files concurrently.
"""

import frontmatter
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Dict, Any, Optional
import pathlib
from yaml.parser import ParserError
from ruamel.yaml.scanner import ScannerError


def load_md_single(fn: str) -> Tuple[str, Optional[Dict[str, Any]], Optional[str], Optional[Exception]]:
    """
    Load a single markdown file.

    Returns:
        Tuple of (filename, metadata_dict, content_str, exception_or_none)
    """
    try:
        onto_stuff = frontmatter.load(fn)
        return (fn, onto_stuff.metadata, onto_stuff.content, None)
    except (ScannerError, ParserError) as e:
        return (fn, None, None, e)
    except Exception as e:
        return (fn, None, None, e)


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
    results = []
    errors = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all file loading tasks
        future_to_file = {executor.submit(load_md_single, fn): fn for fn in files}

        # Collect results as they complete
        for future in as_completed(future_to_file):
            fn, metadata, content, error = future.result()

            if error is not None:
                errors.append((fn, error))
            else:
                results.append((fn, metadata, content))

    # Print any errors that occurred
    if errors:
        print(f"\n⚠️  Encountered {len(errors)} error(s) while loading files:")
        for fn, error in errors:
            print(f"ERROR: Failed to parse YAML in {fn}: {error}")

    return results


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
