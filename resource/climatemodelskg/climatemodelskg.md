---
activity_status: active
category: KnowledgeGraph
collection:
- okn
- ber
contacts:
- category: Individual
  label: Aayush Acharya
  contact_details:
  - contact_type: email
    value: climatepub4kg@tuprd.onmicrosoft.com
  - contact_type: github
    value: aayushacharya
- category: Individual
  contact_details:
  - contact_type: email
    value: mustapha.adamu@temple.edu
  label: Mustapha Adamu
description: Climate Models KG is a knowledge graph to support evaluation and development
  of climate models.
domains:
- environment
- information technology
homepage_url: https://frink.renci.org/registry/kgs/climatepub4-kg/
id: climatemodelskg
layout: resource_detail
name: Climate Models KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for Climate Models KG
  format: http
  id: climatemodelskg.sparql
  name: Climate Models KG SPARQL
  original_source:
  - source: climatemodelskg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/climatemodelskg/sparql
- id: climatemodelskg.tpf
  name: Climate Models KG TPF
  description: Triple Pattern Fragments endpoint for Climate Models KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/climatemodelskg
  original_source:
  - source: climatemodelskg
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  id: climatemodelskg.graph
  name: Climate Models KG Graph
  description: RDF/Turtle knowledge graph integrating climate model and dataset
    metadata (from ESGF, CMIP controlled vocabularies, and the NASA GCMD keyword
    taxonomy) with entities and relationships extracted from climate-science
    publications. Served through the FRINK federation and the SPARQL and TPF
    endpoints.
  format: ttl
  product_url: https://frink.renci.org/registry/kgs/climatepub4-kg/
  original_source:
  - source: climatemodelskg
    relation_type: prov:hadPrimarySource
  - source: esgf
    relation_type: prov:hadPrimarySource
  - source: cmip
    relation_type: prov:hadPrimarySource
  - source: gcmd
    relation_type: prov:hadPrimarySource
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-03T00:00:00Z'
---
Climate Models KG

## Automated Evaluation

- View the automated evaluation: [climatemodelskg automated evaluation](climatemodelskg_eval_automated.html)
