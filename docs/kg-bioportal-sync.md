# KG-Bioportal Synchronization

This document describes how KG-Registry picks up graph transforms from
[KG-Bioportal](https://ncbo.github.io/kg-bioportal/graphs/).

## Overview

KG-Bioportal transforms BioPortal ontologies into KGX node/edge TSVs and publishes
each result as a GitHub release asset. Its manifest currently covers about 1300
ontologies, of which roughly 1100 transform successfully.

That is far more than belongs in a product inventory on a single registry page, and
most of those ontologies have no KG-Registry resource at all. So this sync is not
shaped like `sync_obo_foundry.py`, which mints and maintains whole resources. It is
an annotation pass: for each successfully transformed ontology that *already* has a
KG-Registry resource page, it adds one `GraphProduct` to that page pointing at the
KGX archive. The `kg-bioportal` resource itself is a hand-written page that links to
the graph browser rather than listing the transforms.

## Files

- `util/sync_kg_bioportal.py` — the sync script
- `util/kg_bioportal_sync_map.yaml` — curated acronym-to-resource decisions
- `resource/kg-bioportal/kg-bioportal.md` — the KG-Bioportal resource page
- `reports/kg_bioportal_unmatched.tsv` — worklist written after every run
- `cache/kg_bioportal_cache.yaml` — cached manifest (24 h TTL by default)

## Usage

```bash
# Full sync
make sync-kg-bioportal

# Preview without writing files
make sync-kg-bioportal-dry-run

# First 50 manifest entries only
make sync-kg-bioportal-test
```

The script takes the same flags as the other sync scripts: `--dry-run`, `--limit`,
`--verbose`, `--no-cache`, `--cache-ttl`, and `--registry-root`. It also runs as part
of `make all`, after `sync-obo-foundry`.

## Data source

The manifest is `onto_stats.yaml`, attached to the latest KG-Bioportal release:

```
https://github.com/ncbo/kg-bioportal/releases/latest/download/onto_stats.yaml
```

Each entry gives the BioPortal acronym, transform status, failure reason, source
name and version, node and edge counts, and the download URL of the KGX archive.
`total_stats.yaml` alongside it carries the site-wide counts and transform date, used
only for logging.

## What gets written

For each entry with `status: OK` that resolves to an existing resource, the resource
page gets a product with id `<resource>.kg-bioportal`:

```yaml
- id: agro.kg-bioportal
  name: AGRO KGX graph (KG-Bioportal)
  category: GraphProduct
  description: KGX TSV transform of AGRonomy Ontology (AGRO), produced by KG-Bioportal
    from the BioPortal submission. The archive contains AGRO_nodes.tsv and AGRO_edges.tsv.
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.08.02-7/AGRO.tar.gz
  format: kgx
  compression: targz
  original_source:
  - source: agro
    relation_type: prov:hadPrimarySource
  node_count: 5102
  edge_count: 8691
```

On re-runs, only the fields the sync owns (see `MANAGED_PRODUCT_FIELDS`) are
rewritten; `product_file_size` and anything a curator added are preserved. A
`product_file_size` recorded against a superseded release URL is dropped, since it no
longer describes the file. If an ontology stops transforming successfully, its
product is removed.

## What deliberately does not get written

**Failed and skipped transforms.** KG-Bioportal records these so its own site can
explain the gap — sources that are too large for GitHub-hosted runners, ontologies
with no current BioPortal submission, transform errors. There is no artifact, so
there is nothing for KG-Registry to list.

**New resources.** KG-Bioportal's graph browser draws part of its listing from
KG-Registry's own JSON-LD dump. Creating registry resources from its manifest would
be a circular sync, so an entry with no matching resource is skipped.

**A source association back to `kg-bioportal`.** `propagate_products` (in
`util/extract-metadata.py`) copies each product onto the page of every resource it
names as a source. Naming the aggregator in `original_source` or `secondary_source`
would therefore rebuild the thousand-entry inventory this design exists to avoid.
The KG-Bioportal provenance lives in the product's name, description, and release
URL instead.

## Matching acronyms to resources

BioPortal acronyms are not KG-Registry ids, and they collide in both directions.
BioPortal's `RO` is the Radiomics Ontology, while the OBO Relation Ontology is
`OBOREL`; `PSO` is a patient-safety ontology, while the Plant Stress Ontology that
KG-Registry calls `pso` is `PLANTSO`. Matching on the lowercased acronym alone would
attach the wrong graph to a dozen or so resources.

The script resolves each entry in this order:

1. **The sync map.** `util/kg_bioportal_sync_map.yaml` holds `confirmed` pairs
   (acronym → resource id) and a `rejected` list. Curated decisions win outright.
2. **Acronym plus name check.** The lowercased acronym must be an existing resource
   id, *and* the two names must be similar enough to rule out a collision. Similarity
   is token coverage in the better direction, with fuzzy per-token matching so
   "Phenotypic Quality Ontology" still matches "Phenotype And Trait Ontology".
   Non-OK entries skip the name check, since all they can do is remove a product this
   sync itself wrote.
3. **Otherwise, no write.** Entries with an OK status that either failed the name
   check or have no resource but whose name exactly matches one are recorded in
   `reports/kg_bioportal_unmatched.tsv` with a suggested resource. That report is the
   worklist for extending the sync map.

When several manifest entries resolve to the same resource — BioPortal hosts some
ontologies under two acronyms — only one can supply the resource's single
`<resource>.kg-bioportal` product. Successful transforms beat unsuccessful ones,
curated matches beat heuristic ones, and the rest is alphabetical, so the choice does
not depend on manifest order.

## Frontmatter formatting

Resource pages exist in two YAML shapes, split roughly evenly across the registry:
`yaml.safe_dump` writes top-level list items flush at column zero, while the ruamel
handler in `util/common.py` indents them. The sync detects which shape a page uses
and writes it back the same way, so adding one product does not reflow every list on
the page.

## Adding a decision to the sync map

1. Run the sync and read `reports/kg_bioportal_unmatched.tsv`.
2. Check the BioPortal entry (`https://bioportal.bioontology.org/ontologies/<ACRONYM>`)
   against the KG-Registry resource. They are frequently different ontologies that
   happen to share an acronym.
3. Add the pair under `confirmed:` if they are the same ontology, or the acronym
   under `rejected:` if they are not. Both sections take a trailing comment; say
   which ontology the acronym actually names.
4. Re-run the sync; the entry should drop off the report.
