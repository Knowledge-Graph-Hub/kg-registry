---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  label: Xiangliang Zhang
  contact_details:
  - contact_type: email
    value: xzhang33@nd.edu
  - contact_type: github
    value: XiangqiWang77
- category: Individual
  contact_details:
  - contact_type: email
    value: xzhang33@nd.edu
  label: Xiangliang Zhang
description: This project seeks to create a comprehensive, integrative knowledge network
  for the management of wildlife in the context of climate change
domains:
- environment
- organisms
homepage_url: https://sites.nd.edu/kn-wildlife/
id: wildlifekn
layout: resource_detail
name: Wildlife-KN
products:
- category: GraphicalInterface
  description: Interactive Wildlife-KN portal for exploring wildlife observations
    by taxonomy, location, and time range with map and graph-based views.
  format: http
  id: wildlifekn.portal
  name: Wildlife-KN Portal
  original_source:
  - source: wildlifekn
    relation_type: prov:hadPrimarySource
  product_url: https://kn-wildlife.crc.nd.edu/
- category: ProgrammingInterface
  description: SPARQL endpoint for Wildlife-KN
  format: http
  id: wildlifekn.sparql
  name: Wildlife-KN SPARQL
  original_source:
  - source: wildlifekn
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/wildlifekn/sparql
- id: wildlifekn.tpf
  name: Wildlife-KN TPF
  description: Triple Pattern Fragments endpoint for Wildlife-KN
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/wildlifekn
  original_source:
  - source: wildlifekn
    relation_type: prov:hadPrimarySource
taxon:
- NCBITaxon:131567
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-05-31T00:00:00Z'
---
Wildlife-KN is an open knowledge network for wildlife management under climate
change, developed to support exploration of species observations in relation to
place, time, and environmental context. The project website describes a public,
queryable system for wildlife decision support and currently highlights Florida
amphibian and reptile resources, map-based exploration, and graph-backed search
interfaces.

The registry entry points to the FRINK-hosted Linked Data Fragments endpoint used
for machine querying, while the project portal exposes end-user search and
visualization interfaces. Together these surfaces make the resource usable both
for direct human exploration and for downstream knowledge-graph applications.

## Automated Evaluation

- View the automated evaluation: [wildlifekn automated evaluation](wildlifekn_eval_automated.html)
