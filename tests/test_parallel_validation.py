#!/usr/bin/env python3
"""Test the parallel validation wrapper on small and large input sets."""


def mock_validate_metadata(item, schema):
    """Mock validation function for testing."""
    return {"error": [], "warn": [], "info": []}


def mock_update_results(results, add):
    """Mock update function for testing."""
    for key in ["error", "warn", "info"]:
        results[key].extend(add[key])
    return results


def test_parallel_validation_small_dataset_runs_sequentially(parallel_validator_module):
    resources = [{"id": f"test{i}"} for i in range(10)]
    schema = {}

    results = parallel_validator_module.validate_resources_parallel(
        resources,
        schema,
        mock_validate_metadata,
        mock_update_results,
        max_workers=4,
    )

    assert results == {"error": [], "warn": [], "info": []}


def test_parallel_validation_large_dataset_runs_successfully(parallel_validator_module):
    resources = [{"id": f"test{i}"} for i in range(100)]
    schema = {}

    results = parallel_validator_module.validate_resources_parallel(
        resources,
        schema,
        mock_validate_metadata,
        mock_update_results,
        max_workers=4,
    )

    assert results == {"error": [], "warn": [], "info": []}
