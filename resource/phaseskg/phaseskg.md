---
id: phaseskg
name: PHASES KG
description: Knowledge graph Promoting Healthy Aging through Semantic Enrichment
activity_status: active
homepage_url: https://healthyphases.org/
collection:
- okn
domains:
- health
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-04-02T00:00:00Z'
last_modified_date: '2026-05-31T00:00:00Z'
contacts:
- category: Individual
  label: John Beverley
  contact_details:
  - contact_type: email
    value: johnbeve@buffalo.edu
  - contact_type: github
    value: johnbeve
- category: Individual
  label: Regina Hurley
  contact_details:
  - contact_type: email
    value: rhurley3@buffalo.edu
  - contact_type: github
    value: Regina-Hurley
products:
- id: phaseskg.sparql
  name: PHASES KG SPARQL
  description: SPARQL endpoint for PHASES KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/phaseskg/sparql
  original_source:
  - source: phaseskg
    relation_type: prov:hadPrimarySource
- id: phaseskg.tpf
  name: PHASES KG TPF
  description: Triple Pattern Fragments endpoint for PHASES KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/phaseskg
  original_source:
  - source: phaseskg
    relation_type: prov:hadPrimarySource
- id: phaseskg.knowledge-graph-docs
  name: PHASES KG Documentation
  description: Documentation page describing the HealthyPhases knowledge graph, technical
    implementation, and provenance-oriented access patterns.
  category: DocumentationProduct
  format: http
  product_url: https://healthyphases.org/docs/research/knowledge-graph
  original_source:
  - source: phaseskg
    relation_type: prov:hadPrimarySource
---
PHASES KG

## Description

The HealthyPhases knowledge graph models research findings, concepts, definitions, measurement instruments, and expert-curated relationships relevant to solitude and gerotranscendence in aging research.

Its documentation describes an RDF/OWL implementation with named-graph provenance, SHACL-based validation, and interfaces for SPARQL querying, guided exploration, and reusable research patterns across studies.

This makes the graph useful for evidence synthesis, hypothesis generation, assessment selection, and cross-disciplinary integration around healthy aging and solitude research.

*This resource was automatically synchronized from the FRINK OKN registry.*
