---
name: search-resources
description: Use when asked to find KG-Registry resources about a topic, subject area, or domain (e.g. "everything about RNA interactions", "what proteomics knowledge graphs are there", "find resources mentioning Reactome"). Queries the live hosted KG-Registry Parquet files over HTTP — no local clone needed — mapping a free-text topic to the registry's domain vocabulary plus keyword search.
---

# search-resources

Find resources in the KG-Registry that cover a given topic, subject area, or domain, by querying the live hosted data.

## Prerequisite

- No local clone of the repository is required. This skill reads the published Parquet files over HTTP.
- You need a way to run DuckDB with the `httpfs` extension and internet access. The portable option, which needs nothing preinstalled:
  ```bash
  uv run --with duckdb --no-project python - <<'PY'
  ... query ...
  PY
  ```
  Equivalents: `pip install duckdb` then plain `python`, or the standalone `duckdb` CLI (run `INSTALL httpfs; LOAD httpfs;` first).

## The hosted data

Four Parquet files under `https://kghub.org/kg-registry/registry/parquet/`:

| File | One row per | Key columns |
|------|-------------|-------------|
| `resources.parquet` | resource | `id, name, description, category, activity_status, homepage_url, domains, products, raw_data` (`raw_data` is the full record as JSON) |
| `resource_domains.parquet` | resource×domain | `resource_id, domain` |
| `resource_products.parquet` | product | `resource_id, product_id, product_name, product_category, product_description, product_url` |
| `resource_taxa.parquet` | resource×taxon | `resource_id, taxon` |

Setup block used by every query below:

```python
import duckdb, json
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
BASE = "https://kghub.org/kg-registry/registry/parquet"
R = f"read_parquet('{BASE}/resources.parquet')"
D = f"read_parquet('{BASE}/resource_domains.parquet')"
P = f"read_parquet('{BASE}/resource_products.parquet')"
T = f"read_parquet('{BASE}/resource_taxa.parquet')"
```

## When to use

- "Find everything about RNA interactions."
- "What knowledge graphs cover proteomics / drug discovery / neuroscience?"
- "Which resources mention Reactome / use UniProt / are about human variation?"
- "List active ontologies in the clinical domain."

Skip when:

- The user already names one specific resource and wants its upstream sources (use `trace-upstream-sources`) or where it is used (`find-downstream-usages`).
- The user wants resources *similar to* a named resource (use `find-similar-resources`).

## Inputs

- Required: a topic, subject area, keyword, or domain to search for.
- Optional filters: `category` (DataSource, KnowledgeGraph, Ontology, DataModel, Aggregator), `activity_status` (default to `active` unless the user wants everything), or `taxon` (e.g. NCBITaxon:9606 for human).

## Workflow

1. Separate the topic into two kinds of search.
   - A free-text topic like "RNA interactions" rarely matches a domain value exactly. Treat it as both a possible **domain** and a **keyword** to search in names and descriptions.

2. Map the topic to the actual domain vocabulary.
   - The domains are a controlled list. Read the live values from the data itself, rather than guessing — they change over time:
     ```python
     con.execute(f"SELECT domain, COUNT(*) n FROM {D} GROUP BY domain ORDER BY n DESC").fetchall()
     ```
   - Pick the closest domain(s). "RNA interactions" most likely maps to `genomics` and/or `biological systems`; "drug targets" to `drug discovery`. Only use a value that appears in that list.

3. Query the mapped domain(s).
   ```python
   con.execute(f"""
     SELECT id, name, category, activity_status FROM {R}
     WHERE id IN (SELECT resource_id FROM {D} WHERE domain = ?)
       AND activity_status = 'active'
     ORDER BY name
   """, ['genomics']).fetchall()
   ```
   - Drop the `activity_status` filter if the user wants inactive/all resources. Add `AND category = ?` when the type is constrained.

4. Query the raw topic words as keywords.
   ```python
   con.execute(f"""
     SELECT id, name, category, activity_status FROM {R}
     WHERE name ILIKE ? OR description ILIKE ?
     ORDER BY name
   """, ['%RNA%', '%RNA%']).fetchall()
   ```
   - For a multi-word phrase, run each word and intersect yourself — a single `ILIKE` does not split phrases or imply AND.

5. Catch matches the structured columns miss.
   - Synonyms, product descriptions, and provenance source ids live inside `raw_data`. For proper nouns (a specific database name like "Reactome") sweep there too:
     ```python
     con.execute(f"SELECT id, name FROM {R} WHERE raw_data ILIKE ?", ['%reactome%']).fetchall()
     ```
   - Also check product descriptions directly: `SELECT DISTINCT resource_id FROM {P} WHERE product_description ILIKE ?`.

6. Merge, dedupe, and rank.
   - Union the domain, keyword, and `raw_data` hits by resource `id`.
   - Rank by relevance: a domain match plus a name/description hit beats a single incidental mention buried in `raw_data`.
   - Carry each resource's `category` and `activity_status` so the user can tell a curated KG from an inactive stub.

7. Report.
   - Short list: `id` — name (category, status) — one line on why it matched (domain vs keyword vs name vs buried mention).
   - If the topic mapped to no clean domain, say so and note you fell back to keyword search.
   - Offer follow-ups: trace one resource's upstream sources, find where it is used, or find similar resources.

## Quick reference

| Task | Query |
|------|-------|
| List the live domain vocabulary | `SELECT domain, COUNT(*) n FROM {D} GROUP BY domain ORDER BY n DESC` |
| By domain | `SELECT id,name,category,activity_status FROM {R} WHERE id IN (SELECT resource_id FROM {D} WHERE domain = ?)` |
| Keyword (name/description) | `SELECT id,name,category,activity_status FROM {R} WHERE name ILIKE ? OR description ILIKE ?` |
| Filter by type | add `AND category = 'KnowledgeGraph'` |
| Human resources | `SELECT resource_id FROM {T} WHERE taxon = 'NCBITaxon:9606'` |
| Buried-mention sweep | `SELECT id,name FROM {R} WHERE raw_data ILIKE ?` |

## Common mistakes

- Inventing a domain value that is not in the live `resource_domains` list. Always confirm against the data.
- Relying only on `name`/`description` and missing matches in synonyms, product descriptions, or provenance `source` ids — sweep `raw_data` and `resource_products` too.
- Treating a multi-word topic as an OR when the user meant an AND. Intersect the per-word results yourself.
- Returning stubs and inactive resources without flagging them. Show `activity_status`.
- Assuming a local clone or the `kg_registry` CLI is present. This skill is remote-only; everything comes from the hosted Parquet files.

## Relationship to other skills

- `trace-upstream-sources`, `find-downstream-usages`, and `find-similar-resources` are the natural next steps once this skill has located a resource of interest. They read the same hosted Parquet files.
