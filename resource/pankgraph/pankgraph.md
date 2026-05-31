---
id: pankgraph
name: PanKgraph
description: PanKgraph is a pancreas-focused biomedical knowledge graph within PanKbase that links genes, variants, pancreatic expression quantitative trait loci, and donor-derived multi-omic data to support diabetes research.
activity_status: active
homepage_url: https://pankbase.org/
products:
- id: pankgraph.portal
  name: PanKgraph Explorer
  description: Interactive PanKgraph web application for exploring pancreas-focused relationships and QTL results.
  category: GraphicalInterface
  format: http
  product_url: https://pankgraph.org/
  original_source:
  - source: pankgraph
    relation_type: prov:hadPrimarySource
- id: pankgraph.sparql
  name: PanKgraph SPARQL
  description: SPARQL endpoint for PanKgraph
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/pankgraph/sparql
  original_source:
  - source: pankgraph
    relation_type: prov:hadPrimarySource
- id: pankgraph.tpf
  name: PanKgraph TPF
  description: Triple Pattern Fragments endpoint for PanKgraph
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/pankgraph
  original_source:
  - source: pankgraph
    relation_type: prov:hadPrimarySource
collection:
- okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-05-30T00:00:00Z'
contacts:
- category: Individual
  label: Jie Liu
  contact_details:
  - contact_type: email
    value: drjieliu@umich.edu
  - contact_type: github
    value: jieliu6
domains:
- biomedical
- genomics
---
PanKgraph

## Description

PanKgraph is a pancreas-focused knowledge graph developed within PanKbase to help researchers navigate linked evidence relevant to diabetes biology.

The graph brings together genes, single nucleotide polymorphisms, pancreatic expression quantitative trait loci, and related donor-derived datasets so that previously disconnected signals can be queried together through OKN-hosted interfaces.

PanKbase itself is a broader resource for harmonized human pancreas and islet data, and PanKgraph serves as its graph-centric discovery layer for relationship finding and integrative analysis.

*This resource was automatically synchronized from the FRINK OKN registry.*
