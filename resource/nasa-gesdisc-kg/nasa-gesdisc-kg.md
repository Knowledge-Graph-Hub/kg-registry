---
activity_status: active
category: KnowledgeGraph
collection:
- okn
- ber
contacts:
- category: Individual
  label: Lisa Stillwell
  contact_details:
  - contact_type: email
    value: lisa@renci.org
  - contact_type: github
    value: lstillwe
description: The NASA Knowledge Graph Dataset is an expansive graph-based dataset
  designed to integrate and interconnect information about satellite datasets, scientific
  publications, instruments, platforms, projects, data centers, and science keywords.
  This knowledge graph is particularly focused on datasets managed by NASA's Distributed
  Active Archive Centers (DAACs), which are NASA's data repositories responsible for
  archiving and distributing scientific data. In addition to NASA DAACs, the graph
  includes datasets from 184 data providers worldwide, including various government
  agencies and academic institutions.
domains:
- environment
homepage_url: https://disc.gsfc.nasa.gov
id: nasa-gesdisc-kg
layout: resource_detail
license:
  id: https://opensource.org/licenses/Apache-2.0
  label: Apache-2.0
name: NASA-GESDISC-KG
repository: https://huggingface.co/datasets/nasa-gesdisc/nasa-eo-knowledge-graph
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for NASA-GESDISC-KG
  format: http
  id: nasa-gesdisc-kg.sparql
  name: NASA-GESDISC-KG SPARQL
  original_source:
  - source: nasa-gesdisc-kg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/nasa-gesdisc-kg/sparql
- id: nasa-gesdisc-kg.tpf
  name: NASA-GESDISC-KG TPF
  description: Triple Pattern Fragments endpoint for NASA-GESDISC-KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/nasa-gesdisc-kg
  original_source:
  - source: nasa-gesdisc-kg
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: The NASA Knowledge Graph Dataset (NASA-GESDISC-KG), an RDF knowledge
    graph integrating NASA satellite datasets, scientific publications, instruments,
    platforms, projects, data centers, and science keywords, derived from NASA GES
    DISC data holdings.
  format: ttl
  id: nasa-gesdisc-kg.graph
  name: NASA-GESDISC-KG Graph
  original_source:
  - source: nasa-gesdisc-kg
    relation_type: prov:hadPrimarySource
  - source: nasa-gesdisc
    relation_type: prov:wasDerivedFrom
  product_url: https://frink.renci.org/nasa-gesdisc-kg
publications:
- id: doi:10.5334/dsj-2024-001
  authors:
  - Irina Gerasimov
  - Andrey Savtchenko
  - Jerome Alfred
  - James Acker
  - Jennifer Wei
  - Binita Kc
  doi: 10.5334/dsj-2024-001
  journal: Data Science Journal
  preferred: true
  title: 'Bridging the Gap: Enhancing Prominence and Provenance of NASA Datasets in
    Research Publications'
  year: '2024'
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
---
NASA-GESDISC-KG

## Automated Evaluation

- View the automated evaluation: [nasa-gesdisc-kg automated evaluation](nasa-gesdisc-kg_eval_automated.html)
