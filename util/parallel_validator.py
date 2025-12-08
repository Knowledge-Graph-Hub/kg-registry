#!/usr/bin/env python3
"""
Parallel validation utilities for KG-Registry metadata.

This module provides backward-compatible parallel validation of resource metadata.
New code should use validation.py directly.
"""

import os
from typing import Dict, List, Any, Optional, Tuple, Callable

from validation import (
    ValidationResults,
    validate_resource,
    validate_resources_parallel as _validate_parallel,
    load_json_schema,
)


def validate_single_resource(
    item: Dict[str, Any],
    schema: Dict[str, Any],
    validate_func: Callable
) -> Tuple[str, Optional[Dict], Optional[Exception]]:
    """
    Validate a single resource against the schema.

    Args:
        item: Resource metadata dictionary
        schema: JSON schema to validate against
        validate_func: The validation function to call

    Returns:
        Tuple of (resource_id, validation_results, error)
    """
    resource_id = item.get('id', 'unknown')
    try:
        result = validate_func(item, schema)
        return (resource_id, result, None)
    except Exception as e:
        return (resource_id, None, e)


def validate_resources_parallel(
    resources: List[Dict[str, Any]],
    schema: Dict[str, Any],
    validate_func: Callable,
    update_results_func: Callable,
    max_workers: Optional[int] = None
) -> Dict[str, List]:
    """
    Validate multiple resources in parallel.

    This is a backward-compatible wrapper. For new code, use
    validation.validate_resources_parallel() directly.

    Args:
        resources: List of resource metadata dictionaries
        schema: JSON schema to validate against
        validate_func: The validation function to call for each resource
        update_results_func: Function to merge validation results
        max_workers: Number of worker threads (default: from env or 10)

    Returns:
        Dictionary with 'error', 'warn', and 'info' lists
    """
    if max_workers is None:
        max_workers = int(os.environ.get('PARALLEL_WORKERS', '10'))

    # Use the original implementation for backward compatibility
    # since the new validation module has a different signature
    from concurrent.futures import ThreadPoolExecutor, as_completed

    # Don't use parallel validation for small sets
    if len(resources) < 50:
        results = {"error": [], "warn": [], "info": []}
        for item in resources:
            add = validate_func(item, schema)
            results = update_results_func(results, add)
        return results

    results = {"error": [], "warn": [], "info": []}

    print(f"Validating {len(resources)} resources with {max_workers} workers...")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all validation tasks
        futures = {
            executor.submit(validate_single_resource, item, schema, validate_func): item.get('id', 'unknown')
            for item in resources
        }

        # Collect results as they complete
        completed = 0
        for future in as_completed(futures):
            resource_id = futures[future]
            resource_id_str, result, error = future.result()

            if error:
                results['error'].append(f"{resource_id}: Validation error: {error}")
                print(f"  ❌ Error validating {resource_id}: {error}")
            elif result:
                # Merge results from this validation
                for key in ['error', 'warn', 'info']:
                    if key in result:
                        results[key].extend(result[key])

            completed += 1
            if completed % 100 == 0:
                print(f"  Progress: {completed}/{len(resources)} resources validated")

    print(f"  ✅ Completed validation of {len(resources)} resources")
    return results

