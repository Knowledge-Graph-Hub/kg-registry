"""Regression tests for resource comparison source aggregation."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest


def _run_resource_compare_harness() -> dict:
    """Execute resource comparison helpers in Node and return computed values."""
    if shutil.which("node") is None:
        pytest.skip("node is required to execute the resource compare regression test")

    repo_root = Path(__file__).resolve().parents[1]
    source = (repo_root / "assets/js/resource-compare.js").read_text()

    # Prevent bootstrapping and expose internals for deterministic unit-style checks.
    source = source.replace(
        "  document.addEventListener('DOMContentLoaded', initialize);",
        "  globalThis.__resourceCompareTestHooks = { collectOriginalSources, compareResources };",
    )

    script = f"""
const logs = [];

globalThis.window = {{
  location: {{ href: 'http://localhost/compare/' }},
  history: {{ replaceState() {{}} }},
}};

globalThis.document = {{
  addEventListener() {{}},
  getElementById() {{ return null; }},
}};

globalThis.fetch = async () => {{ throw new Error('fetch should not be called in test harness'); }};
globalThis.jsyaml = {{ load() {{ return {{ resources: [] }}; }} }};

{source}

const hooks = globalThis.__resourceCompareTestHooks;
if (!hooks) {{
  throw new Error('Failed to expose resource compare test hooks');
}}

const ms = {{
  id: 'ms',
  category: 'Ontology',
  domains: ['biomedical'],
  products: [
    {{
      id: 'ms.obo',
      original_source: [{{ source: 'ms', relation_type: 'prov:hadPrimarySource' }}],
    }},
    {{
      id: 'ms.owl',
      original_source: [{{ source: 'ms', relation_type: 'prov:hadPrimarySource' }}],
    }},
    {{
      id: 'cancer-genome-interpreter.clinicalkg.graph',
      original_source: [
        {{ source: 'uniprot', relation_type: 'prov:hadPrimarySource' }},
        {{ source: 'foo', relation_type: 'prov:hadPrimarySource' }},
      ],
    }},
    {{
      id: 'ckg.graph',
      original_source: [{{ source: 'bar', relation_type: 'prov:hadPrimarySource' }}],
    }},
  ],
}};

const foo = {{
  id: 'foo',
  category: 'Ontology',
  domains: ['biomedical'],
  products: [
    {{
      id: 'foo.graph',
      original_source: [{{ source: 'foo', relation_type: 'prov:hadPrimarySource' }}],
    }},
  ],
}};

const msSources = Array.from(hooks.collectOriginalSources(ms)).sort();
const fooSources = Array.from(hooks.collectOriginalSources(foo)).sort();
const comparison = hooks.compareResources(ms, foo);

console.log(JSON.stringify({{
  msSources,
  fooSources,
  sharedOriginalSources: comparison.sharedOriginalSources,
  similarityScore: comparison.similarityScore,
}}));
"""

    result = subprocess.run(
        ["node", "-"],
        input=script,
        text=True,
        capture_output=True,
        check=True,
        cwd=repo_root,
    )

    return json.loads(result.stdout.strip())


def test_compare_excludes_foreign_product_sources() -> None:
    """Only directly owned products should contribute to a resource's original sources."""
    payload = _run_resource_compare_harness()

    assert payload["msSources"] == ["ms"]
    assert payload["fooSources"] == ["foo"]
    assert payload["sharedOriginalSources"] == []
