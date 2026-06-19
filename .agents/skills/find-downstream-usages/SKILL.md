---
name: find-downstream-usages
description: Use when asked everywhere a given resource is used or consumed downstream — which knowledge graphs, aggregators, or products draw on it, and any recorded real-world uses — based on what KG-Registry records. Reads the live hosted KG-Registry Parquet files over HTTP (no local clone needed), combining reverse provenance (other resources naming this one as a source) with the resource's own usages field.
---

# find-downstream-usages

Determine everywhere a given resource is used, from what KG-Registry records, using the live hosted data.

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

Setup block:

```python
import duckdb, json
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
BASE = "https://kghub.org/kg-registry/registry/parquet"
R = f"read_parquet('{BASE}/resources.parquet')"           # has raw_data JSON per resource
P = f"read_parquet('{BASE}/resource_products.parquet')"   # resource_id, product_id, ...
```

## Two evidence sources

KG-Registry records downstream use in two distinct places inside `raw_data`. Check both.

1. **Reverse provenance** — other resources whose products name the target in `original_source` or `secondary_source`. This is the authoritative "X is built from <target>" signal.
2. **The target's own `usages` field** — curator-recorded real-world uses, each with `label`, `description`, `type` (actual / experimental / theoretical / other), optional `users`, and optional `publications`.

## Inputs

- Required: a resource id, e.g. `uniprot`. (Find it with `search-resources` if only a topic/name is known.)
- Optional: whether to also match references to the resource's individual **product** ids, not just the top-level resource id (default: yes — products are often what gets cited as a source).

## Workflow

1. Gather the target's own product ids (consumers may reference any of them).
   ```python
   target = 'uniprot'
   pids = [r[0] for r in con.execute(f"SELECT product_id FROM {P} WHERE resource_id = ?", [target]).fetchall()]
   needles = [target] + pids
   ```

2. Reverse-provenance sweep: find every resource whose JSON names the target as a source.
   ```python
   # the quotes make this an EXACT id match — "source": "uniprot" never matches "uniprotkb"
   import re
   rows = con.execute(f"SELECT id, name, category, activity_status, raw_data FROM {R}").fetchall()
   consumers = []
   for rid, name, cat, status, raw in rows:
       if rid == target:                      # skip the target's own page
           continue
       rec = json.loads(raw)
       for prod in rec.get('products', []):
           for slot in ('original_source', 'secondary_source'):
               for a in (prod.get(slot) or []):
                   if a.get('source') in needles:
                       consumers.append({'id': rid, 'name': name, 'category': cat,
                                         'status': status, 'via_product': prod['id'],
                                         'slot': slot, 'relation': a.get('relation_type')})
   ```
   - A faster prefilter, if you prefer SQL: `SELECT id FROM {R} WHERE raw_data LIKE '%"source": "uniprot"%'` — the surrounding quotes anchor the id exactly. Confirm hits by parsing, since JSON whitespace can vary.

3. Read the target's own recorded usages.
   ```python
   rec = json.loads(con.execute(f"SELECT raw_data FROM {R} WHERE id = ?", [target]).fetchone()[0])
   usages = rec.get('usages', [])    # each has label, description, type, users?, publications?
   ```
   - `type: actual` is a real deployment; `experimental`/`theoretical` are weaker claims — preserve the distinction.

4. Report.
   - Section A — **Consumed by** (reverse provenance): each consumer as `id` — name (category, status) — relation — which product consumes it. Strongest signal.
   - Section B — **Recorded usages** (the `usages` field): each with its type and users/publications.
   - If both are empty, say so plainly: KG-Registry records no downstream use, which is common for leaf data sources and does not mean the resource is unused in the wider world.

## Quick reference

| Task | How |
|------|-----|
| Target's product ids | `SELECT product_id FROM {P} WHERE resource_id = ?` |
| Reverse-provenance prefilter | `SELECT id FROM {R} WHERE raw_data LIKE '%"source": "<id>"%'` (quotes anchor the id) |
| Authoritative reverse check | parse each `raw_data`, match `products[*].original_source/secondary_source[*].source` |
| Recorded usages | `json.loads(raw_data)['usages']` on the target |
| Enrich a consumer | the `name, category, activity_status` columns of `resources.parquet` |

## Common mistakes

- Searching only the top-level resource id and missing consumers that reference one of its **product** ids.
- Counting the target's own products' self-references as downstream use.
- Reporting only reverse provenance and ignoring the curator-written `usages` field, or vice versa.
- Treating an empty result as "broken" — leaf data sources legitimately have no recorded downstream consumers.
- Dropping `relation_type` and usage `type`, which tell the user whether a use is a hard dependency, a soft influence, or an experimental claim.
- Matching the id without the surrounding quotes, so `uniprot` also catches `uniprotkb`. Anchor on `"source": "uniprot"`.

## Relationship to other skills

- `trace-upstream-sources` answers the reverse question (a resource's inputs).
- `search-resources` locates the target id from a topic or name.
- All three read the same hosted Parquet files.
