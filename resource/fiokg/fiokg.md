---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: torsten.hahmann@maine.edu
  label: Torsten Hahmann
description: The FRS (Facility Registry Service) KG is the part of the SAWGraph project
  that stores data about facilities from EPA's Facility Registry service (FRS) together
  with their NAICS industry classification and the spatial location.
domains:
- environment
- agriculture
homepage_url: https://sawgraph.github.io/
id: fiokg
layout: resource_detail
name: SAWGraph FRS KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SAWGraph FRS KG
  format: http
  id: fiokg.sparql
  name: SAWGraph FRS KG SPARQL
  original_source:
  - source: fiokg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/fiokg/sparql
- id: fiokg.tpf
  name: SAWGraph FRS KG TPF
  description: Triple Pattern Fragments endpoint for SAWGraph FRS KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/fiokg
  original_source:
  - source: fiokg
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: The SAWGraph Facilities and Industries Ontology (FIO) / Facility Registry
    Service (FRS) knowledge graph, an RDF (Turtle) graph representing US facilities
    from EPA's Facility Registry Service together with their NAICS and SIC industry
    classifications and spatial locations. It is served through the SAWGraph FRS SPARQL
    and Triple Pattern Fragments endpoints.
  format: ttl
  id: fiokg.graph
  name: SAWGraph FRS Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fiokg
  - relation_type: prov:wasDerivedFrom
    source: sawgraph
  - relation_type: prov:hadPrimarySource
    source: epa-frs
  product_url: https://github.com/SAWGraph/fio
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: naics
  - relation_type: prov:wasInfluencedBy
    source: sic
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-03T00:00:00Z'
---
SAWGraph FIO KG

## Automated Evaluation

- View the automated evaluation: [fiokg automated evaluation](fiokg_eval_automated.html)
