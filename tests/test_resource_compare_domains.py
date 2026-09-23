"""Regression tests for domain weighting in resource comparison."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest


def _compare(left: dict, right: dict, parents: dict) -> dict:
    """Run compareResources in Node with the given DomainEnum is_a map."""
    if shutil.which("node") is None:
        pytest.skip("node is required to execute the resource compare regression test")

    repo_root = Path(__file__).resolve().parents[1]
    source = (repo_root / "assets/js/resource-compare.js").read_text()
    source = source.replace(
        "  document.addEventListener('DOMContentLoaded', initialize);",
        "  globalThis.__resourceCompareTestHooks = { compareResources };",
    )
    script = f"""
globalThis.window = {{
  location: {{ href: 'http://localhost/compare/' }},
  history: {{ replaceState() {{}} }},
  kgRegistryDomainParents: {json.dumps(parents)},
}};
globalThis.document = {{ addEventListener() {{}}, getElementById() {{ return null; }} }};
globalThis.fetch = async () => {{ throw new Error('fetch should not be called'); }};
globalThis.jsyaml = {{ load() {{ return {{ resources: [] }}; }} }};

{source}

const result = globalThis.__resourceCompareTestHooks.compareResources({json.dumps(left)}, {json.dumps(right)});
console.log(JSON.stringify({{ similarityScore: result.similarityScore, sharedDomains: result.sharedDomains }}));
"""
    result = subprocess.run(
        ["node", "-"], input=script, text=True, capture_output=True, check=True, cwd=repo_root
    )
    return json.loads(result.stdout.strip())


PARENTS = {"neurodegenerative disease": "neuroscience", "cancer": "biomedical"}


def test_shared_specific_domain_outweighs_shared_broad_domain() -> None:
    specific = _compare(
        {"id": "a", "category": "KnowledgeGraph", "domains": ["neuroscience", "neurodegenerative disease"]},
        {"id": "b", "category": "Ontology", "domains": ["neuroscience", "neurodegenerative disease"]},
        PARENTS,
    )
    broad = _compare(
        {"id": "a", "category": "KnowledgeGraph", "domains": ["neuroscience", "biomedical"]},
        {"id": "b", "category": "Ontology", "domains": ["neuroscience", "biomedical"]},
        PARENTS,
    )
    # shared 2+4 of union 2+4+8 against shared 2+2 of union 2+2+8
    assert specific["similarityScore"] == 42.9
    assert broad["similarityScore"] == 33.3
    assert specific["sharedDomains"] == ["neurodegenerative disease", "neuroscience"]


def test_without_hierarchy_every_domain_weighs_the_same() -> None:
    result = _compare(
        {"id": "a", "category": "KnowledgeGraph", "domains": ["neuroscience", "neurodegenerative disease"]},
        {"id": "b", "category": "Ontology", "domains": ["neuroscience", "neurodegenerative disease"]},
        {},
    )
    assert result["similarityScore"] == 33.3
