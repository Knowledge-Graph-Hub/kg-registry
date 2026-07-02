---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  label: Tom Luechtefeld
  contact_details:
  - contact_type: email
    value: tom@insilica.co
  - contact_type: github
    value: tomlue
- category: Individual
  contact_details:
  - contact_type: email
    value: tom@insilica.co
  label: Tom Luechtefeld
description: BioBricks Tox21 is an open knowledge graph for Tox21 toxicology screening
  data.
domains:
- toxicology
homepage_url: https://github.com/biobricks-ai/biobricks-okg
id: biobricks-tox21
layout: resource_detail
name: BioBricks Tox21
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for BioBricks Tox21
  format: http
  id: biobricks-tox21.sparql
  name: BioBricks Tox21 SPARQL
  original_source:
  - source: biobricks-tox21
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/biobricks-tox21/sparql
- id: biobricks-tox21.tpf
  name: BioBricks Tox21 TPF
  description: Triple Pattern Fragments endpoint for BioBricks Tox21
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/biobricks-tox21
  original_source:
  - source: biobricks-tox21
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  id: biobricks-tox21.graph
  name: BioBricks Tox21 Knowledge Graph
  description: RDF knowledge graph repackaging EPA/NIH Tox21 high-throughput toxicology
    screening data, distributed via the biobricks-okg repository.
  format: ttl
  product_url: https://github.com/biobricks-ai/biobricks-okg
  original_source:
  - source: biobricks-tox21
    relation_type: prov:hadPrimarySource
  - source: tox21
    relation_type: prov:wasDerivedFrom
repository: https://github.com/biobricks-ai/biobricks-okg
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
---
BioBricks Tox21

## Automated Evaluation

- View the automated evaluation: [biobricks-tox21 automated evaluation](biobricks-tox21_eval_automated.html)
