---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: MaayanLab
  - contact_type: url
    value: https://maayanlab.cloud/
  label: Ma'ayan Lab
creation_date: '2025-09-23T00:00:00Z'
description: ReproTox-KG is a knowledge graph for structural birth defects and reproductive toxicology that integrates literature-derived and chemical evidence to support exploration of drug-birth defect relationships.
domains:
- biomedical
- toxicology
- drug discovery
homepage_url: https://maayanlab.cloud/reprotox-kg
id: reprotox-kg
last_modified_date: '2026-05-28T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: CC BY-NC 4.0
name: ReproTox-KG
products:
- category: GraphicalInterface
  description: Public web interface for querying and exploring ReproTox-KG relationships.
  format: http
  id: reprotox-kg.portal
  name: ReproTox-KG Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://maayanlab.cloud/reprotox-kg
- category: ProcessProduct
  description: Source repository for the ReproTox-KG website assets, schema, and ingestion notebooks.
  format: http
  id: reprotox-kg.code
  name: ReproTox-KG Source Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  product_url: https://github.com/MaayanLab/Reprotox-KG
- category: Product
  description: Knowledge graph schema definition used by ReproTox-KG.
  format: json
  id: reprotox-kg.schema
  name: ReproTox-KG Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  product_url: https://github.com/MaayanLab/Reprotox-KG/blob/main/schema.json
- category: Product
  description: Data and content assets published with ReproTox-KG (markdown and supporting materials).
  format: http
  id: reprotox-kg.data
  name: ReproTox-KG Data Assets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://github.com/MaayanLab/Reprotox-KG/tree/main/markdown
publications:
- authors:
  - Evangelista JE
  - Clarke DJB
  - Xie Z
  - Marino GB
  - Utti V
  - Jenkins SL
  - Ahooyi TM
  - Bologa CG
  - Yang JJ
  - Binder JL
  - Kumar P
  - Lambert CG
  - Grethe JS
  - Wenger E
  - Taylor D
  - Oprea TI
  - de Bono B
  - Ma'ayan A
  doi: 10.1038/s43856-023-00329-2
  id: PMID:37460679
  journal: Communications Medicine
  preferred: true
  title: Toxicology knowledge graph for structural birth defects
  year: '2023'
repository: https://github.com/MaayanLab/Reprotox-KG
---
# ReproTox-KG

ReproTox-KG is a knowledge graph focused on reproductive toxicology and structural birth defects.

## Current Access Points

- Public interface: https://maayanlab.cloud/reprotox-kg
- Source repository: https://github.com/MaayanLab/Reprotox-KG

## Notes

The legacy reprotox-kg.net endpoints appear to have been retired. This entry now points to the currently maintained Ma'ayan Lab resources and removes stale URL-check warnings tied to the abandoned domain.

## Automated Evaluation

- View the automated evaluation: [reprotox-kg automated evaluation](reprotox-kg_eval_automated.html)
