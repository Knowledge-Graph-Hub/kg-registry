---
name: trace-upstream-sources
description: Use when asked what upstream data sources a given resource (usually a knowledge graph) is built from — its inputs, dependencies, or provenance — based on what KG-Registry records. Reads the live hosted KG-Registry Parquet files over HTTP (no local clone needed), walks each product's original_source and secondary_source, resolves the referenced ids, and optionally recurses to build the full upstream tree.
---

# trace-upstream-sources

Determine all upstream data sources that feed into a given resource, from the provenance KG-Registry records, using the live hosted data.

## Prerequisite

- No local clone required. This skill reads the published Parquet files over HTTP.
- You need DuckDB with the `httpfs` extension and internet access. Portable option:
  ```bash
  uv run --with duckdb --no-project python - <<'PY'
  ... query ...
  PY
  ```
  (Or `pip install duckdb` + `python`, or the `duckdb` CLI with `INSTALL httpfs; LOAD httpfs;`.)

## The hosted data

`https://kghub.org/kg-registry/registry/parquet/resources.parquet` has one row per resource. Provenance is **not** a flat column — it lives inside the `raw_data` JSON, under each product. Setup block:

```python
import duckdb, json
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
BASE = "https://kghub.org/kg-registry/registry/parquet"
R = f"read_parquet('{BASE}/resources.parquet')"
P = f"read_parquet('{BASE}/resource_products.parquet')"   # resource_id, product_id, ...

def record(rid):
    row = con.execute(f"SELECT raw_data FROM {R} WHERE id = ?", [rid]).fetchone()
    return json.loads(row[0]) if row else None
```

## How provenance is stored

- Each resource's `raw_data` has a `products` list.
- Each product may carry two provenance slots, each a list of `{source, relation_type}` objects:
  - `original_source` — primary inputs. Default relation `prov:hadPrimarySource`.
  - `secondary_source` — non-primary influences/derivatives. Relations like `prov:wasInfluencedBy`, `prov:wasDerivedFrom`, `prov:wasInformedBy`, `prov:used`.
- `source` is a KG-Registry resource **or product** id — not a URL, not an INFORES id, not a label.
- A product owned by the resource itself normally lists the parent resource id in its `original_source`; that self-reference is not an external upstream source.

## Inputs

- Required: a resource id, e.g. `kg-microbe`. (Find it with `search-resources` if only a topic/name is known.)
- Optional: `depth` — recursion levels (default: 1 = direct sources; higher or "full" to chase sources of sources).
- Optional: whether to include `secondary_source` (default: yes, labeled separately from primary).

## Workflow

1. Pull the resource record and collect every provenance reference.
   ```python
   rec = record('kg-microbe')
   refs = []
   for prod in rec.get('products', []):
       for slot in ('original_source', 'secondary_source'):
           for assoc in (prod.get(slot) or []):
               refs.append({'product': prod['id'], 'slot': slot,
                            'source': assoc['source'],
                            'relation': assoc.get('relation_type')})
   ```
   - If `record()` returns `None`, the id is wrong — locate it with `search-resources`.

2. Separate the resource's own products from genuine upstream sources.
   - Drop self-references where `source` equals the resource id (or one of its own product ids).
   - Deduplicate the rest by `source`. That is the set of direct upstream sources.

3. Resolve each upstream id to a real resource.
   ```python
   def resolve(sid):
       r = con.execute(f"SELECT id,name,category,activity_status FROM {R} WHERE id = ?", [sid]).fetchone()
       if r: return r
       # source may be a PRODUCT id — find its owning resource
       o = con.execute(f"SELECT resource_id FROM {P} WHERE product_id = ?", [sid]).fetchone()
       return con.execute(f"SELECT id,name,category,activity_status FROM {R} WHERE id = ?", [o[0]]).fetchone() if o else None
   ```
   - Flag any id that resolves to `None` — it may be an intentionally minted id whose page does not exist yet. Note it; do not silently drop it.

4. Recurse if requested.
   - For depth > 1 or "full", repeat steps 1–3 on each resolved upstream resource.
   - Track visited ids to avoid loops and to dedupe shared ancestors.
   - Stop at sources with no further `original_source`/`secondary_source` (the primary-source leaves).

5. Report the upstream tree.
   - Group by relation: primary inputs (`prov:hadPrimarySource`) first, then secondary influences with their specific relation.
   - Per source: `id` — name (category, status) — relation — which product of the target it feeds.
   - For a recursive trace, render an indented tree and call out leaf-level primary sources distinctly.
   - Note any unresolved ids and any products carrying no provenance at all (a curation gap worth surfacing).

## Quick reference

| Task | How |
|------|-----|
| Get a resource record | `json.loads(con.execute(f"SELECT raw_data FROM {R} WHERE id=?", [rid]).fetchone()[0])` |
| Source ids on a record | walk `rec['products'][*]['original_source'/'secondary_source'][*]['source']` |
| Resolve a resource id | `SELECT id,name,category,activity_status FROM {R} WHERE id=?` |
| Resolve a product id to its owner | `SELECT resource_id FROM {P} WHERE product_id=?` |
| Recurse | call `record()` on each resolved source id |

## Common mistakes

- Counting a product's self-reference to its parent resource as an external upstream source.
- Treating a `source` value as a URL or label. It is a KG-Registry id and must be resolved as one.
- Forgetting that a `source` can be a **product** id, not a resource id — resolve both ways via `resource_products`.
- Ignoring `secondary_source`. It carries real upstream influence; just label it separately from primary inputs.
- Silently dropping an unresolved source id instead of flagging it as a not-yet-created page.
- Recursing without tracking visited ids, producing loops or duplicated subtrees.

## Relationship to other skills

- `find-downstream-usages` answers the reverse question (where a resource is used).
- `search-resources` locates the starting resource id when the user only has a topic or name.
- All three read the same hosted Parquet files.
