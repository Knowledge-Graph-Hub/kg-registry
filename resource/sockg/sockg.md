---
activity_status: active
category: KnowledgeGraph
collection:
- okn
- ber
contacts:
- category: Individual
  label: Chengkai Li
  contact_details:
  - contact_type: email
    value: cli@uta.edu
  - contact_type: github
    value: idirlab
- category: Individual
  contact_details:
  - contact_type: email
    value: cli@uta.edu
  label: Chengkai Li
description: The Soil Organic Carbon Knowledge Graph (SOCKG) enhances robust soil
  carbon modeling, which is crucial for voluntary carbon markets.
domains:
- environment
- agriculture
homepage_url: https://idir.sockg.org/
id: sockg
layout: resource_detail
name: SOC-KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SOC-KG
  format: http
  id: sockg.sparql
  name: SOC-KG SPARQL
  original_source:
  - source: sockg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/sockg/sparql
- id: sockg.tpf
  name: SOC-KG TPF
  description: Triple Pattern Fragments endpoint for SOC-KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/sockg
  original_source:
  - source: sockg
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: The Soil Organic Carbon Knowledge Graph (SOCKG), an RDF knowledge graph
    integrating and mapping agricultural experimental data (soil properties, greenhouse
    gas fluxes, crop yields, and management practices) to support soil carbon modeling.
    Terminology is semantically aligned to the National Agricultural Library Thesaurus.
  format: rdfxml
  id: sockg.graph
  name: SOC-KG RDF Knowledge Graph
  original_source:
  - source: sockg
    relation_type: prov:hadPrimarySource
  - source: agcros
    relation_type: prov:hadPrimarySource
  secondary_source:
  - source: nalt
    relation_type: prov:wasInfluencedBy
  product_url: https://idir.sockg.org/
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
---
SOC-KG

## Automated Evaluation

- View the automated evaluation: [sockg automated evaluation](sockg_eval_automated.html)
