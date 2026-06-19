---
name: find-similar-resources
description: Use when asked to find KG-Registry resources similar to a given one — alternatives, related graphs, or near-duplicates. Reads the live hosted KG-Registry Parquet files over HTTP (no local clone needed), combining structured signals (shared domains, taxa, category, node/edge scale, shared upstream sources) with softer heuristics (description similarity and overlapping publication authors) into a ranked shortlist.
---

# find-similar-resources

Find resources similar to a given resource, blending KG-Registry's structured metadata with text and citation heuristics, using the live hosted data.

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
R = f"read_parquet('{BASE}/resources.parquet')"           # raw_data JSON has products, usages, publications
D = f"read_parquet('{BASE}/resource_domains.parquet')"    # resource_id, domain
T = f"read_parquet('{BASE}/resource_taxa.parquet')"       # resource_id, taxon

def record(rid):
    row = con.execute(f"SELECT raw_data FROM {R} WHERE id = ?", [rid]).fetchone()
    return json.loads(row[0]) if row else None
```

## Similarity signals

Combine several — no single one is sufficient. Structured signals are cheap and narrow the field; the heuristics rank what is left.

**Structured (from metadata):**
- Shared `domains` (strongest cheap signal) — `resource_domains.parquet`.
- Shared `taxon` (same organisms) — `resource_taxa.parquet`.
- Same `category` (usually you want like-for-like).
- Comparable graph scale — `node_count`/`edge_count` on graph products, found in `raw_data.products[*]`.
- Shared upstream sources — two graphs built from the same `source` ids are closely related (the provenance from `trace-upstream-sources`).

**Heuristic (judgment-based):**
- Description similarity — read both `description` fields and judge topical overlap, not just shared words.
- Overlapping publication authors — `raw_data.publications[*].authors`. Shared names often mean the same group, a related or successor resource.

## Inputs

- Required: a resource id, e.g. `kg-microbe`.
- Optional: how many results to return (default: top 5–10).
- Optional: whether to restrict to the same `category` (default: yes).

## Workflow

1. Build the seed fingerprint.
   ```python
   seed = 'kg-microbe'
   rec = record(seed)
   s_domains = {r[0] for r in con.execute(f"SELECT domain FROM {D} WHERE resource_id=?", [seed]).fetchall()}
   s_taxa    = {r[0] for r in con.execute(f"SELECT taxon  FROM {T} WHERE resource_id=?", [seed]).fetchall()}
   s_category = rec['category']
   s_sources = {a['source'] for p in rec.get('products', [])
                for slot in ('original_source','secondary_source')
                for a in (p.get(slot) or []) if a['source'] != seed}
   s_authors = {au for pub in rec.get('publications', []) for au in pub.get('authors', [])}
   s_desc = rec.get('description', '')
   ```

2. Generate candidates with the cheap structured filters.
   ```python
   cands = {r[0] for r in con.execute(
       f"SELECT DISTINCT resource_id FROM {D} WHERE domain IN ({','.join('?'*len(s_domains))})",
       list(s_domains)).fetchall()}
   cands |= {r[0] for r in con.execute(
       f"SELECT DISTINCT resource_id FROM {T} WHERE taxon IN ({','.join('?'*len(s_taxa))})",
       list(s_taxa)).fetchall()} if s_taxa else set()
   cands.discard(seed)
   ```
   - If `s_domains` is empty, fall back to a keyword candidate set via `search-resources`.

3. Score each candidate on the structured signals.
   ```python
   for cid in cands:
       crec = record(cid)
       c_domains = {r[0] for r in con.execute(f"SELECT domain FROM {D} WHERE resource_id=?", [cid]).fetchall()}
       c_taxa    = {r[0] for r in con.execute(f"SELECT taxon  FROM {T} WHERE resource_id=?", [cid]).fetchall()}
       c_sources = {a['source'] for p in crec.get('products', [])
                    for slot in ('original_source','secondary_source')
                    for a in (p.get(slot) or []) if a['source'] != cid}
       shared_domains = s_domains & c_domains
       shared_taxa    = s_taxa & c_taxa
       shared_sources = s_sources & c_sources
       same_category  = crec['category'] == s_category
       # graph scale: pull node_count/edge_count from crec['products'][*] and compare order of magnitude
   ```

4. Apply the heuristics to the surviving shortlist.
   - **Descriptions**: read `s_desc` and each candidate's `description` and rate topical closeness (clearly-the-same / overlapping / tangential). Use meaning, not keyword overlap alone.
   - **Authors**: `c_authors = {au for pub in crec.get('publications', []) for au in pub.get('authors', [])}`; any name in `s_authors & c_authors` is a strong relatedness signal — surface it explicitly.

5. Rank and explain.
   - Combine signals. Weight structured agreement (shared domains, shared sources) and description closeness highest; treat shared authors and matching scale as strong corroboration / tie-breakers.
   - Flag likely **near-duplicates** distinctly (same domains + same sources + near-identical description, or a shared author with an almost-identical name) — candidates for de-duplication or cross-linking, which curators care about.

6. Report.
   - Ranked list: `id` — name (category) — one-line "why similar" naming the concrete signals (e.g. "shares domains genomics+proteomics, both built from uniprot, overlapping authors").
   - State which signals you could and could not evaluate (e.g. seed has no publications, so author overlap was skipped).
   - Call out suspected near-duplicates separately.

## Quick reference

| Task | How |
|------|-----|
| Seed/candidate domains | `SELECT domain FROM {D} WHERE resource_id=?` |
| Seed/candidate taxa | `SELECT taxon FROM {T} WHERE resource_id=?` |
| Candidates by shared domain | `SELECT DISTINCT resource_id FROM {D} WHERE domain IN (...)` |
| Sources / authors / scale | walk `record(id)['products' / 'publications']` |
| Compare descriptions | read both `description` fields and judge meaning |

## Common mistakes

- Relying on a single signal. Domain overlap alone returns the whole field; description similarity alone misses scale and provenance. Combine them.
- Comparing descriptions by shared keywords instead of meaning.
- Ignoring shared upstream sources, often the most telling structural similarity between two knowledge graphs.
- Skipping the heuristics because they need judgment — they are the point of this skill, not optional extras.
- Returning a ranked list with no explanation. Always say *why* each result is similar and which signals were unavailable.
- Forgetting to drop the seed resource from its own candidate list.

## Relationship to other skills

- `search-resources` finds candidates by topic when structured filters are too narrow.
- `trace-upstream-sources` supplies the shared-source comparison used here.
- All three read the same hosted Parquet files.
