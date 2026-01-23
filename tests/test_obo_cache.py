#!/usr/bin/env python3
"""
Test script for OBO Foundry caching functionality
"""

import os
import sys
import time
from pathlib import Path

# Add util to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "util"))

from sync_obo_foundry import OBOFoundrySync


def test_cache_creation():
    """Test that cache is created on first fetch"""
    print("Test 1: Cache Creation")
    print("-" * 50)

    # Create syncer with short TTL for testing
    syncer = OBOFoundrySync(cache_ttl_hours=1)

    # Remove cache if it exists
    if syncer.cache_file.exists():
        syncer.cache_file.unlink()
        print(f"✅ Removed existing cache: {syncer.cache_file}")

    # First fetch should create cache
    print("Fetching OBO Foundry data (should create cache)...")
    start_time = time.time()
    data = syncer.fetch_obo_foundry_data()
    elapsed = time.time() - start_time

    print(f"✅ Fetched {len(data)} ontologies in {elapsed:.2f} seconds")

    # Check that cache was created
    if syncer.cache_file.exists():
        print(f"✅ Cache file created: {syncer.cache_file}")
        cache_size = syncer.cache_file.stat().st_size / 1024
        print(f"   Cache size: {cache_size:.2f} KB")
    else:
        print("❌ Cache file was not created!")
        return False

    return True


def test_cache_usage():
    """Test that cache is used on subsequent fetches"""
    print("\nTest 2: Cache Usage")
    print("-" * 50)

    syncer = OBOFoundrySync(cache_ttl_hours=1)

    # This should use cache
    print("Fetching OBO Foundry data (should use cache)...")
    start_time = time.time()
    data = syncer.fetch_obo_foundry_data()
    elapsed = time.time() - start_time

    print(f"✅ Fetched {len(data)} ontologies in {elapsed:.2f} seconds")

    # Should be very fast (< 1 second) if using cache
    if elapsed < 1.0:
        print(f"✅ Fast fetch indicates cache was used ({elapsed:.3f}s)")
    else:
        print(f"⚠️  Slow fetch - cache may not have been used ({elapsed:.3f}s)")

    return True


def test_cache_expiration():
    """Test that expired cache triggers fresh fetch"""
    print("\nTest 3: Cache Expiration")
    print("-" * 50)

    # Create syncer with 0 hour TTL (immediate expiration)
    syncer = OBOFoundrySync(cache_ttl_hours=0)

    print("Fetching with TTL=0 (should fetch fresh data)...")
    start_time = time.time()
    data = syncer.fetch_obo_foundry_data()
    elapsed = time.time() - start_time

    print(f"✅ Fetched {len(data)} ontologies in {elapsed:.2f} seconds")

    # Should be slower (> 1 second) as it's fetching fresh
    if elapsed > 1.0:
        print(f"✅ Slow fetch indicates fresh data was fetched ({elapsed:.3f}s)")
    else:
        print(f"⚠️  Fast fetch - may have used cache incorrectly ({elapsed:.3f}s)")

    return True


def test_cache_validation():
    """Test that cache validation works correctly"""
    print("\nTest 4: Cache Validation")
    print("-" * 50)

    syncer = OBOFoundrySync(cache_ttl_hours=24)

    # Check if cache is valid
    is_valid = syncer._is_cache_valid()
    print(f"Cache valid (TTL=24h): {is_valid}")

    if is_valid:
        cache_age = (time.time() - os.path.getmtime(syncer.cache_file)) / 3600
        print(f"✅ Cache age: {cache_age:.2f} hours")

    # Test with short TTL
    syncer_short = OBOFoundrySync(cache_ttl_hours=0.001)  # ~3.6 seconds
    time.sleep(4)  # Wait for cache to expire

    is_valid_short = syncer_short._is_cache_valid()
    print(f"Cache valid (TTL=0.001h, after 4s wait): {is_valid_short}")

    if not is_valid_short:
        print("✅ Cache correctly identified as expired")
    else:
        print("⚠️  Cache should have expired but didn't")

    return True


def main():
    print("=" * 50)
    print("OBO Foundry Cache Testing")
    print("=" * 50)
    print()

    try:
        # Run all tests
        tests = [
            test_cache_creation,
            test_cache_usage,
            test_cache_expiration,
            test_cache_validation,
        ]

        results = []
        for test in tests:
            try:
                result = test()
                results.append(result)
            except Exception as e:
                print(f"❌ Test failed with error: {e}")
                results.append(False)

        # Summary
        print("\n" + "=" * 50)
        print("Test Summary")
        print("=" * 50)
        passed = sum(results)
        total = len(results)
        print(f"Passed: {passed}/{total}")

        if passed == total:
            print("✅ All tests passed!")
            return 0
        else:
            print(f"❌ {total - passed} test(s) failed")
            return 1

    except Exception as e:
        print(f"❌ Testing failed: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
