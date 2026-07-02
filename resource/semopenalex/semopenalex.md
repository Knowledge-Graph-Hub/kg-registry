---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  label: Lew Lefton
  contact_details:
  - contact_type: email
    value: lew.lefton@gmail.com
description: Comprehensive information on scientific publications and related entities.
domains:
- literature
homepage_url: https://semopenalex.org/
id: semopenalex
layout: resource_detail
name: SemOpenAlex
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SemOpenAlex
  format: http
  id: semopenalex.sparql
  name: SemOpenAlex SPARQL
  original_source:
  - source: semopenalex
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/semopenalex/sparql
- id: semopenalex.tpf
  name: SemOpenAlex TPF
  description: Triple Pattern Fragments endpoint for SemOpenAlex
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/semopenalex
  original_source:
  - source: semopenalex
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: RDF graph representation of the OpenAlex scholarly data as Linked Open
    Data, distributed as Turtle (TTL) snapshots via the SemOpenAlex code and data
    repository.
  format: ttl
  id: semopenalex.graph
  name: SemOpenAlex RDF Graph
  original_source:
  - source: semopenalex
    relation_type: prov:hadPrimarySource
  - source: openalex
    relation_type: prov:wasDerivedFrom
  product_url: https://github.com/metaphacts/semopenalex
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
---
SemOpenAlex

## Automated Evaluation

- View the automated evaluation: [semopenalex automated evaluation](semopenalex_eval_automated.html)
