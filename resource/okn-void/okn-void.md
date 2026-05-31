---
id: okn-void
name: OKN VoID graph descriptions
description: Collected VoID and VoID-Ext metadata describing registered OKN knowledge graphs, their endpoints, and summary statistics.
activity_status: active
homepage_url: https://registry.okn.us/registry/kgs/okn-void/
contacts:
- category: Individual
  label: Jim Balhoff
  contact_details:
  - contact_type: email
    value: balhoff@renci.org
  - contact_type: github
    value: balhoff
products:
- id: okn-void.sparql
  name: OKN VoID graph descriptions SPARQL
  description: SPARQL endpoint for querying the OKN VoID metadata graph describing registered OKN knowledge graphs.
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/okn-void/sparql
  original_source:
  - source: okn-void
    relation_type: prov:hadPrimarySource
- id: okn-void.tpf
  name: OKN VoID graph descriptions TPF
  description: Triple Pattern Fragments endpoint for browsing the OKN VoID metadata graph and its dataset-level descriptions.
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/okn-void
  original_source:
  - source: okn-void
    relation_type: prov:hadPrimarySource
collection:
- okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-05-30T00:00:00Z'
domains:
- general
---
OKN VoID graph descriptions

## Description

OKN VoID graph descriptions is a registry-scale metadata graph that aggregates
VoID and VoID Extensions descriptions for knowledge graphs in the Open Knowledge
Network ecosystem. It captures dataset-level metadata such as classes,
properties, endpoint locations, and summary statistics so OKN graphs can be
discovered and compared through a single graph.

The OKN registry page reports this graph as a live FRINK-hosted knowledge graph
with millions of triples and explicit use of the VoID and VoID Extensions
vocabularies to describe the registered graph collection.

## Evaluation

- View the evaluation: [okn-void evaluation](okn-void_eval_automated.html)

*This resource was automatically synchronized from the FRINK OKN registry.*
