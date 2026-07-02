---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: danny.e.oneal@gmail.com
  - contact_type: github
    value: danny-oneal
  label: Danny O'Neal
- category: Individual
  contact_details:
  - contact_type: email
    value: scottgdaniel@gmail.com
  - contact_type: github
    value: scottgdaniel
  label: Scott Daniel
description: SCALES is an integrated justice platform to connect criminal justice
  data across data silos.
domains:
- general
homepage_url: https://scales-okn.org/
id: scales
layout: resource_detail
name: SCALES
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SCALES
  format: http
  id: scales.sparql
  name: SCALES SPARQL
  original_source:
  - source: scales
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/scales/sparql
- id: scales.tpf
  name: SCALES TPF
  description: Triple Pattern Fragments endpoint for SCALES
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/scales
  original_source:
  - source: scales
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: SCALES knowledge graph of U.S. federal court records, derived from PACER
    data and served via the SCALES SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: scales.graph
  name: SCALES Knowledge Graph
  original_source:
  - source: scales
    relation_type: prov:hadPrimarySource
  - source: pacer
    relation_type: prov:wasDerivedFrom
  product_url: https://scales-okn.org/
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
---
SCALES

## Automated Evaluation

- View the automated evaluation: [scales automated evaluation](scales_eval_automated.html)
