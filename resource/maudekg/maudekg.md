---
id: maudekg
name: FDA MAUDE Adverse Event Knowledge Graph
description: Knowledge graph constructed from FDA MAUDE adverse event reports using
  standardized FDA product codes.
activity_status: active
homepage_url: https://github.com/Prabhadeus/Proto-OKN
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: psingh37@pride.hofstra.edu
  - contact_type: github
    value: Prabhadeus
  label: Prabhjot Singh
products:
- id: maudekg.sparql
  name: FDA MAUDE Adverse Event Knowledge Graph SPARQL
  description: SPARQL endpoint for FDA MAUDE Adverse Event Knowledge Graph
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/maudekg/sparql
  original_source:
  - source: maudekg
    relation_type: prov:hadPrimarySource
- id: maudekg.tpf
  name: FDA MAUDE Adverse Event Knowledge Graph TPF
  description: Triple Pattern Fragments endpoint for FDA MAUDE Adverse Event Knowledge
    Graph
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/maudekg
  original_source:
  - source: maudekg
    relation_type: prov:hadPrimarySource
collection:
- okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-05-31T00:00:00Z'
domains:
- biomedical
- clinical
- pharmacology
---
FDA MAUDE Adverse Event Knowledge Graph

## Description

The MAUDE knowledge graph represents FDA medical-device adverse event reports collected through the openFDA MAUDE API using an ontology-first RDF model.

The OKN registry description highlights that the graph is intended for structured querying of device safety reports and downstream statistical analysis of adverse-event patterns, with current scale on the order of roughly ninety-six thousand triples.

Its focus on standardized product codes and RDF transformation makes it a useful intermediate graph for device surveillance and safety analytics workflows.

*This resource was automatically synchronized from the FRINK OKN registry.*
