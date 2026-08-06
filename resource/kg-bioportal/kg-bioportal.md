---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@bioontology.org
  - contact_type: url
    value: https://www.bioontology.org/
  label: National Center for Biomedical Ontology (NCBO), Stanford
creation_date: '2026-08-06T00:00:00Z'
description: KG-Bioportal transforms the ontologies hosted by BioPortal into KGX
  node and edge files, so each can be used as a knowledge graph. Transforms run
  monthly on GitHub Actions and every successful result is published as a release
  asset, alongside a manifest of per-ontology status and node/edge counts. Over
  a thousand ontologies are covered; the graph browser is the authoritative
  listing.
domains:
- biomedical
- clinical
- information technology
- general
homepage_url: https://ncbo.github.io/kg-bioportal/
id: kg-bioportal
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://www.bioontology.org/terms/
  label: BioPortal Terms of Use (individual ontologies carry their own licenses)
name: KG-Bioportal
products:
- category: GraphicalInterface
  description: Browsable listing of every KG-Bioportal graph, with node and edge
    counts, transform status, and a download link for each. This is the canonical
    index of the transforms; KG-Registry does not mirror the full inventory.
  format: http
  id: kg-bioportal.browser
  name: KG-Bioportal Graph Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-bioportal
  product_url: https://ncbo.github.io/kg-bioportal/graphs/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: bioportal
- category: Product
  description: Manifest of every transform attempt, giving the BioPortal acronym,
    status, node and edge counts, source submission, and release download URL for
    each ontology. Refreshed with each monthly transform run.
  format: yaml
  id: kg-bioportal.manifest
  name: KG-Bioportal Transform Manifest
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-bioportal
  product_url: https://github.com/ncbo/kg-bioportal/releases/latest/download/onto_stats.yaml
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: bioportal
- category: GraphProduct
  description: KGX TSV graphs for all successfully transformed BioPortal
    ontologies, published as one gzipped tar archive per ontology on the latest
    release. Individual archives are at
    https://github.com/ncbo/kg-bioportal/releases/latest/download/<ACRONYM>.tar.gz
    and contain <ACRONYM>_nodes.tsv and <ACRONYM>_edges.tsv.
  compression: targz
  format: kgx
  id: kg-bioportal.graphs
  latest_version: latest
  name: KG-Bioportal KGX Graphs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-bioportal
  product_url: https://github.com/ncbo/kg-bioportal/releases/latest
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: bioportal
- category: ProcessProduct
  description: Python package and GitHub Actions workflow that download BioPortal
    ontologies and convert them to KGX with ROBOT and the KGX toolkit.
  format: python
  id: kg-bioportal.code
  name: KG-Bioportal Transform Pipeline
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-bioportal
  product_url: https://github.com/ncbo/kg-bioportal
repository: https://github.com/ncbo/kg-bioportal
---
# KG-Bioportal

KG-Bioportal is a transform pipeline and graph collection: it takes the ontologies
in [BioPortal](https://bioportal.bioontology.org/) and converts each into
[KGX](https://github.com/biolink/kgx) node and edge TSVs. The transforms run
monthly on GitHub Actions, and each successful result is attached to a GitHub
release as `<ACRONYM>.tar.gz`.

## Finding a graph

Because KG-Bioportal covers all of BioPortal, its inventory runs to well over a
thousand entries -- far more than belongs on a single registry page. Use the
[graph browser](https://ncbo.github.io/kg-bioportal/graphs/) to search the full
set. Every archive is also reachable directly at a stable URL:

```
https://github.com/ncbo/kg-bioportal/releases/latest/download/<ACRONYM>.tar.gz
```

## Relationship to KG-Registry

Where an ontology transformed by KG-Bioportal already has a KG-Registry resource
page, that page carries the transform as its own `<resource>.kg-bioportal`
product, added by `util/sync_kg_bioportal.py`. Transforms that failed or were
skipped have no artifact and are not recorded here; the browser explains those
cases. KG-Bioportal's graph browser in turn draws part of its listing from
KG-Registry, so the sync deliberately never creates registry resources from the
KG-Bioportal manifest.

## Coverage limits

The largest ontologies -- NCBITaxon, SNOMED CT, RxNorm, PR, NCIT, and others --
exceed what GitHub-hosted runners can transform and are skipped rather than
failing the build. Their status and the reason are recorded in the manifest.
