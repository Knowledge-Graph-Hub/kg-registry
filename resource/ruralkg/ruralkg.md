---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  label: Jiaqi Gong
  contact_details:
  - contact_type: email
    value: jiaqi.gong@ua.edu
  - contact_type: github
    value: SAIL-UA
- category: Individual
  contact_details:
  - contact_type: email
    value: jiaqi.gong@ua.edu
  label: Jiaqi Gong
description: Rural Resilience KG is a cross-domain knowledge graph to integrate health
  and justice for rural resilience.
domains:
- biomedical
- public health
homepage_url: https://frink.renci.org/registry/kgs/rural-kg/
id: ruralkg
layout: resource_detail
name: Rural Resilience KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for Rural Resilience KG
  format: http
  id: ruralkg.sparql
  name: Rural Resilience KG SPARQL
  original_source:
  - source: ruralkg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/ruralkg/sparql
- id: ruralkg.tpf
  name: Rural Resilience KG TPF
  description: Triple Pattern Fragments endpoint for Rural Resilience KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/ruralkg
  original_source:
  - source: ruralkg
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: The Rural Resilience KG graph, a cross-domain RDF knowledge graph
    integrating health and justice data for rural resilience. It integrates
    justice/crime data from the National Incident-Based Reporting System (NIBRS),
    substance-use survey data from the National Survey on Drug Use and Health
    (NSDUH), mental health treatment providers from the National Directory of
    Mental Health Treatment Facilities, county rurality classifications from the
    USDA Rural-Urban Continuum Codes, and US administrative-area geography, served
    via the FRINK/Proto-OKN infrastructure.
  format: ttl
  id: ruralkg.graph
  name: Rural Resilience KG graph
  original_source:
  - source: ruralkg
    relation_type: prov:hadPrimarySource
  - source: nibrs
    relation_type: prov:hadPrimarySource
  - source: nsduh
    relation_type: prov:hadPrimarySource
  - source: national-directory-mental-health-facilities
    relation_type: prov:hadPrimarySource
  - source: rural-urban-continuum-codes
    relation_type: prov:hadPrimarySource
  secondary_source:
  - source: us-census
    relation_type: prov:wasInfluencedBy
  product_url: https://frink.renci.org/registry/kgs/rural-kg/
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-03T00:00:00Z'
---
Rural Resilience KG

## Automated Evaluation

- View the automated evaluation: [ruralkg automated evaluation](ruralkg_eval_automated.html)
