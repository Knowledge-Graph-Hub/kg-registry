---
activity_status: active
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: tamerh
  label: Tamer Gür
  orcid: 0000-0001-5822-9201
creation_date: '2026-10-04T00:00:00Z'
description: Sugi Atlas is a deterministic biomedical reference atlas with one canonical
  page for each human gene, drug and disease (about 52,600 pages when checked on 2026-10-04,
  29,337 genes, 4,683 drugs and 18,607 diseases). Pages are assembled by a fixed plan
  of graph queries over BioBTree, which integrates 87 primary databases, and are rendered
  by template, with no language model in the loop, so every figure traces to its source.
  Each page is published as static HTML with a Markdown version and a schema.org JSON-LD
  record, for both human readers and AI agents. Gene, drug and disease pages are seeded
  from HGNC, Mondo and ChEMBL identifiers and are rebuilt at least monthly against
  new BioBTree releases.
domains:
- biomedical
- genomics
- drug discovery
- clinical
homepage_url: https://sugi.bio/atlas/
id: sugi-atlas
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: Sugi Atlas
products:
- category: GraphicalInterface
  description: Sugi Atlas web site with search and one static reference page per human
    gene, drug and disease (for example /atlas/gene/TP53/). Each page also has a Markdown
    version at index.md and embeds a schema.org JSON-LD record.
  format: http
  id: sugi-atlas.portal
  name: Sugi Atlas Web Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sugi-atlas
  - relation_type: prov:wasDerivedFrom
    source: biobtree
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: chembl
  product_url: https://sugi.bio/atlas/
- category: Product
  description: JSON manifest of the atlas corpus, mapping page slugs to canonical
    names and synonyms for genes, drugs, diseases and pathways (about 12.8 MB when
    checked on 2026-10-04).
  format: json
  id: sugi-atlas.manifest
  name: Sugi Atlas Manifest
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sugi-atlas
  - relation_type: prov:wasDerivedFrom
    source: biobtree
  product_file_size: 12797962
  product_url: https://sugi.bio/atlas/manifest.json
- category: ProcessProduct
  description: Python pipeline that queries BioBTree and builds, tests and releases
    the atlas corpus. Versions the pipeline only; the generated corpus is not attached
    to releases.
  format: python
  id: sugi-atlas.code
  latest_version: v1.11.0
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: Sugi Atlas Pipeline
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sugi-atlas
  product_url: https://github.com/tamerh/sugi-atlas
  repository: https://github.com/tamerh/sugi-atlas
- category: DocumentationProduct
  description: HTML version of the Sugi Atlas preprint describing the build method,
    page contract, cross-entity mesh and corpus statistics.
  format: http
  id: sugi-atlas.preprint
  name: Sugi Atlas Preprint (HTML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sugi-atlas
  product_url: https://sugi.bio/atlas/preprint/
- category: DocumentationProduct
  description: List of the 87 primary databases integrated by BioBTree that underlie
    Sugi Atlas, each with its citing paper.
  format: http
  id: sugi-atlas.sources
  name: Sugi Atlas Data Sources
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sugi-atlas
  product_url: https://sugi.bio/atlas/sources/
publications:
- authors:
  - Tamer Gür
  doi: doi:10.5281/zenodo.20569200
  id: doi:10.5281/zenodo.20569200
  journal: Zenodo
  preferred: true
  title: 'Sugi Atlas: A Comprehensive, Deterministic Biomedical Catalog from a Knowledge
    Graph for Humans and AI Agents'
  year: '2026'
repository: https://github.com/tamerh/sugi-atlas
synonyms:
- sugi.bio Atlas
---
# Sugi Atlas

Sugi Atlas is a biomedical reference atlas: one canonical, structured page for every human gene, drug and disease. It is part of the [sugi.bio](https://sugi.bio/) project and is built on [BioBTree](https://sugi.bio/biobtree/), which integrates the 87 primary databases listed on the [Sources](https://sugi.bio/atlas/sources/) page.

## How it is built

Every page is built deterministically. A fixed plan of graph queries traverses BioBTree, and the returned records are rendered into tables and prose by template. No part of a page is written by a language model. The same inputs give the same page on every build. Where a section has no data, the page says so.

Seeds are pre-resolved HGNC (genes), Mondo (diseases) and ChEMBL (drugs) identifiers. The drug set covers approved (phase 4) and late-stage clinical (phase 3) compounds. Non-human and veterinary disease terms are dropped at seed time.

Genes, drugs and diseases are linked by a curated cross-entity mesh, so a relationship recorded once (a drug's target, a disease's gene) is navigable from every page it touches.

## Access

- Web pages at `https://sugi.bio/atlas/{gene,drug,disease}/<slug>/`, for example [TP53](https://sugi.bio/atlas/gene/TP53/).
- A Markdown version of each page at `.../index.md`, with a metadata header.
- A schema.org JSON-LD record (Gene, Drug or MedicalCondition) embedded in each page.
- A corpus [manifest](https://sugi.bio/atlas/manifest.json) of slugs, names and synonyms.

No bulk download of the corpus is published. The pipeline releases on GitHub version the code only.

## License

The pipeline code is MIT. The generated atlas content is published under CC BY-SA 4.0, according to the repository README, and each underlying source keeps its own license and attribution terms.

## Citation

Gür T. Sugi Atlas: A Comprehensive, Deterministic Biomedical Catalog from a Knowledge Graph for Humans and AI Agents. Zenodo, 2026. [doi:10.5281/zenodo.20569200](https://doi.org/10.5281/zenodo.20569200)