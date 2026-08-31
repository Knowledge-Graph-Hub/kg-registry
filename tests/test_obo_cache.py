"""Tests for OBO Foundry cache creation, reuse, expiration, and fallback behavior."""

import os
import time

import pytest
import yaml

from util.sync_obo_foundry import OBOFoundrySync

SAMPLE_ONTOLOGIES = [
    {"id": "go", "title": "Gene Ontology"},
    {"id": "chebi", "title": "Chemical Entities of Biological Interest"},
]


class FakeResponse:
    """Minimal stand-in for the ``requests.Response`` used by the syncer."""

    def __init__(self, payload):
        self.content = yaml.dump(payload).encode("utf-8")

    def raise_for_status(self):
        return None


@pytest.fixture
def fetches(monkeypatch):
    """Replace the live OBO Foundry request with a call-counting fake."""
    calls = []

    def fake_get(url, **kwargs):
        calls.append(url)
        return FakeResponse(SAMPLE_ONTOLOGIES)

    monkeypatch.setattr("util.sync_obo_foundry.requests.get", fake_get)
    return calls


@pytest.fixture
def syncer(tmp_path, fetches):
    """An ``OBOFoundrySync`` whose registry and cache both live under tmp_path."""
    instance = OBOFoundrySync(registry_root=str(tmp_path / "resource"), cache_ttl_hours=24)
    instance.cache_dir = tmp_path / "cache"
    instance.cache_dir.mkdir(parents=True, exist_ok=True)
    instance.cache_file = instance.cache_dir / "obo_foundry_cache.yml"
    return instance


def age_cache(syncer, hours):
    """Backdate the cache file so it reads as ``hours`` old."""
    stale = time.time() - hours * 3600
    os.utime(syncer.cache_file, (stale, stale))


def test_cache_created_on_first_fetch(syncer, fetches):
    """The first fetch hits the network and writes the cache file."""
    assert not syncer.cache_file.exists()

    data = syncer.fetch_obo_foundry_data()

    assert data == SAMPLE_ONTOLOGIES
    assert len(fetches) == 1
    assert syncer.cache_file.exists()
    assert yaml.safe_load(syncer.cache_file.read_text()) == SAMPLE_ONTOLOGIES


def test_cache_reused_within_ttl(syncer, fetches):
    """A second fetch inside the TTL is served from cache without a request."""
    syncer.fetch_obo_foundry_data()
    data = syncer.fetch_obo_foundry_data()

    assert data == SAMPLE_ONTOLOGIES
    assert len(fetches) == 1


def test_expired_cache_triggers_refetch(syncer, fetches):
    """A cache older than the TTL is refreshed from the network."""
    syncer.fetch_obo_foundry_data()
    age_cache(syncer, hours=25)

    data = syncer.fetch_obo_foundry_data()

    assert data == SAMPLE_ONTOLOGIES
    assert len(fetches) == 2


def test_is_cache_valid_respects_ttl(syncer):
    """`_is_cache_valid` is false with no cache, and tracks the file's age."""
    assert syncer._is_cache_valid() is False

    syncer.fetch_obo_foundry_data()
    assert syncer._is_cache_valid() is True

    age_cache(syncer, hours=25)
    assert syncer._is_cache_valid() is False


def test_expired_cache_is_fallback_when_fetch_fails(syncer, monkeypatch, fetches):
    """When a refresh fails, the stale cache is returned rather than raising."""
    syncer.fetch_obo_foundry_data()
    age_cache(syncer, hours=25)

    def boom(url, **kwargs):
        raise RuntimeError("network down")

    monkeypatch.setattr("util.sync_obo_foundry.requests.get", boom)

    assert syncer.fetch_obo_foundry_data() == SAMPLE_ONTOLOGIES


def test_fetch_failure_without_cache_raises(syncer, monkeypatch):
    """With no cache to fall back on, a failed fetch propagates."""

    def boom(url, **kwargs):
        raise RuntimeError("network down")

    monkeypatch.setattr("util.sync_obo_foundry.requests.get", boom)

    with pytest.raises(RuntimeError):
        syncer.fetch_obo_foundry_data()
