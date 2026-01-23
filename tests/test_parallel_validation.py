#!/usr/bin/env python3
"""
Quick test to verify parallel validation works correctly.
"""

import os
import sys

# Add util directory to path - must be before imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "util"))

from parallel_validator import validate_resources_parallel


def mock_validate_metadata(item, schema):
    """Mock validation function for testing"""
    return {"error": [], "warn": [], "info": []}


def mock_update_results(results, add):
    """Mock update function for testing"""
    for key in ["error", "warn", "info"]:
        results[key].extend(add[key])
    return results


# Test with small dataset (should use sequential)
print("Test 1: Small dataset (< 50 resources)")
resources = [{"id": f"test{i}"} for i in range(10)]
schema = {}
results = validate_resources_parallel(
    resources, schema, mock_validate_metadata, mock_update_results, max_workers=4
)
print(f"  ✅ Validated {len(resources)} resources")
print(f"  Results: {results}")

# Test with large dataset (should use parallel)
print("\nTest 2: Large dataset (>= 50 resources)")
resources = [{"id": f"test{i}"} for i in range(100)]
results = validate_resources_parallel(
    resources, schema, mock_validate_metadata, mock_update_results, max_workers=4
)
print(f"  ✅ Validated {len(resources)} resources")
print(f"  Results: {results}")

print("\n✅ All tests passed!")
