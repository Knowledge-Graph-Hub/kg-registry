---
activity_status: active
category: KnowledgeGraph
collection:
  - okn
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: katrina.schweikert@maine.edu
      - contact_type: github
        value: kschweikert
    label: Katrina Schweikert
description: The Safe Agricultural Products and Water Graph (SAWGraph) PFAS KG stores data on PFAS observations and releases, describing the samples, the geospatial features they were taken from, the sampled environmental media, the specific chemical substances and the measurement values observed.
domains:
  - environment
  - chemistry and biochemistry
  - agriculture
homepage_url: https://sawgraph.github.io/
id: sawgraph
layout: resource_detail
name: SAWGraph PFAS KG
products:
  - category: ProgrammingInterface
    description: SPARQL endpoint for SAWGraph PFAS KG
    id: sawgraph.sparql
    name: SAWGraph PFAS KG SPARQL
    original_source:
      - source: sawgraph
        relation_type: prov:hadPrimarySource
    product_url: https://frink.apps.renci.org/sawgraph/sparql
  - id: sawgraph.tpf
    name: SAWGraph PFAS KG TPF
    description: Triple Pattern Fragments endpoint for SAWGraph PFAS KG
    category: ProgrammingInterface
    product_url: https://frink.apps.renci.org/ldf/sawgraph
    original_source:
      - source: sawgraph
        relation_type: prov:hadPrimarySource
repository: https://github.com/sawgraph
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-03-30T00:00:00Z'
---

SAWGraph PFAS graph

## Automated Evaluation

- View the automated evaluation: [sawgraph automated evaluation](sawgraph_eval_automated.html)
