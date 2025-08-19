#!/usr/bin/env python3

"""
Ingest node/edge counts from Monarch QC Parquet reports and update kg-monarch.md.

Behavior:
 - Checks remote Last-Modified for edge/node report URLs.
 - If changed since last run (or no state), uses DuckDB to compute total node and edge counts.
 - Updates the kg-monarch resource frontmatter: sets last_modified_date (UTC now) and
   writes node_count/edge_count on all GraphProduct entries.
 - Persists a small state file under build/ingests/kg-monarch/state.json to avoid redundant work.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

import duckdb
import frontmatter  # type: ignore
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from frontmatter.util import u


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

EDGE_URL = "https://data.monarchinitiative.org/monarch-kg/latest/qc/edge_report.parquet"
NODE_URL = "https://data.monarchinitiative.org/monarch-kg/latest/qc/node_report.parquet"

STATE_DIR = ROOT / "build" / "ingests" / "kg-monarch"
STATE_FILE = STATE_DIR / "state.json"
RESOURCE_FILE = ROOT / "resource" / "kg-monarch" / "kg-monarch.md"


def http_last_modified(url: str) -> Optional[str]:
    """Fetch Last-Modified header using HEAD; fall back to GET if necessary."""
    try:
        req = Request(url, method='HEAD')
        with urlopen(req, timeout=30) as resp:
            return resp.headers.get('Last-Modified')
    except Exception:
        try:
            # Fallback GET (should not download full data for most servers when only headers read)
            req = Request(url, method='GET')
            with urlopen(req, timeout=30) as resp:
                return resp.headers.get('Last-Modified')
        except Exception:
            return None


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True))


def counts_from_parquet(edge_url: str, node_url: str) -> Tuple[int, int]:
    # DuckDB can read remote parquet directly
    conn = duckdb.connect(database=':memory:')
    edge_count = conn.execute(f"SELECT COUNT(*) FROM read_parquet('{edge_url}')").fetchone()[0]
    node_count = conn.execute(f"SELECT COUNT(*) FROM read_parquet('{node_url}')").fetchone()[0]
    conn.close()
    return int(edge_count), int(node_count)


class _RuamelFrontmatterHandler(frontmatter.YAMLHandler):
    """Local copy of the ruamel-based handler used elsewhere to preserve quotes/indentation."""

    def __init__(self):
        self.myyaml = YAML()
        self.myyaml.default_flow_style = False
        self.myyaml.allow_duplicate_keys = True
        self.myyaml.indent(mapping=2, sequence=4, offset=2)
        self.myyaml.preserve_quotes = True
        self.myyaml.width = 1500
        super().__init__()

    def load(self, fm, **kwargs):
        return self.myyaml.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        stream = StringIO()
        self.myyaml.dump(data=metadata, stream=stream)
        metadata = stream.getvalue()
        metadata = metadata[:-1]
        return u(metadata)


def update_resource(edge_count: int, node_count: int) -> bool:
    """Update kg-monarch.md frontmatter with counts and last_modified_date.
    Returns True if file was modified.
    """
    if not RESOURCE_FILE.exists():
        print(f"Resource file not found: {RESOURCE_FILE}")
        return False

    handler = _RuamelFrontmatterHandler()
    post = frontmatter.load(RESOURCE_FILE, handler=handler)
    meta = post.metadata.copy()

    changed = False
    # Update last_modified_date (UTC ISO 8601 with Z)
    now_iso = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    if meta.get('last_modified_date') != now_iso:
        meta['last_modified_date'] = now_iso
        changed = True

    # Update counts on all GraphProduct entries
    products = meta.get('products') or []
    if isinstance(products, list):
        new_products = []
        for p in products:
            if isinstance(p, dict) and p.get('category') == 'GraphProduct':
                if p.get('edge_count') != edge_count or p.get('node_count') != node_count:
                    q = p.copy()
                    q['edge_count'] = int(edge_count)
                    q['node_count'] = int(node_count)
                    new_products.append(q)
                    changed = True
                else:
                    new_products.append(p)
            else:
                new_products.append(p)
        meta['products'] = new_products

    if changed:
        post.metadata = meta
        with open(RESOURCE_FILE, 'wb') as fwb:
            frontmatter.dump(post, fd=fwb, handler=handler)
        # Ensure trailing newline for content separation
        with open(RESOURCE_FILE, 'a') as fa:
            fa.write('\n')

    return changed


def main() -> None:
    state = load_state()
    prev_edge_mod = state.get('edge_last_modified')
    prev_node_mod = state.get('node_last_modified')

    edge_mod = http_last_modified(EDGE_URL)
    node_mod = http_last_modified(NODE_URL)

    should_update = (not prev_edge_mod or not prev_node_mod) or (
        edge_mod != prev_edge_mod or node_mod != prev_node_mod)

    if not should_update:
        print("Monarch QC reports unchanged since last check; skipping update.")
        return

    # Compute counts
    edge_count, node_count = counts_from_parquet(EDGE_URL, NODE_URL)
    print(f"Monarch counts: edges={edge_count}, nodes={node_count}")

    # Update resource file
    changed = update_resource(edge_count=edge_count, node_count=node_count)

    # Persist state
    state.update({
        'edge_last_modified': edge_mod,
        'node_last_modified': node_mod,
        'last_run': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'edge_count': edge_count,
        'node_count': node_count,
        'resource_updated': changed,
    })
    save_state(state)


if __name__ == '__main__':
    main()
