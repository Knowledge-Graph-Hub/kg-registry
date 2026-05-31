---
id: rdkg
name: Rare Disease Knowledge Graph
description: RDKG is an open knowledge graph for rare diseases that integrates standardized
  disease identifiers and cross-references to support discovery and evidence synthesis.
activity_status: active
homepage_url: https://frink.renci.org/registry/kgs/rdkg/
collection:
- okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-05-31T00:00:00Z'
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jinlian.wang@uth.tmc.edu
  - contact_type: github
    value: wnagjl99
  label: Jinlian Wang
products:
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for RDKG
  format: http
  id: rdkg.tpf
  name: RDKG TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdkg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://apps.okn.us/ldf/rdkg
domains:
- biomedical
- clinical
---
Rare Disease Knowledge Graph

## Description

RDKG is an open knowledge graph for rare diseases that harmonizes disease entities and cross-references across major biomedical terminologies.

The current graph description emphasizes alignment to MONDO, ORDO, OMIM Phenotypic Series, and UMLS so that rare-disease concepts can be linked consistently across source systems and downstream analytic workflows.

This normalization-oriented design makes the graph useful for rare-disease entity reconciliation, knowledge discovery, and evidence synthesis tasks.

*This resource was automatically synchronized from the FRINK OKN registry.*
