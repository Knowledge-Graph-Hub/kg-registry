---
id: evoweb
name: EvoWeb
description: EvoWeb - An Open Knowledge Graph of Co-evolving Genes (NIAID)
activity_status: active
homepage_url: https://data.niaid.nih.gov/
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: Erik.Wright@bcm.edu
  - contact_type: github
    value: WrightLabScience
  label: Erik Wright
products:
- id: evoweb.sparql
  name: EvoWeb SPARQL
  description: SPARQL endpoint for EvoWeb
  category: ProgrammingInterface
  product_url: https://apps.okn.us/evoweb/sparql
  original_source:
  - source: evoweb
    relation_type: prov:hadPrimarySource
- id: evoweb.tpf
  name: EvoWeb TPF
  description: Triple Pattern Fragments endpoint for EvoWeb
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/evoweb
  original_source:
  - source: evoweb
    relation_type: prov:hadPrimarySource
collection:
- okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-05-28T00:00:00Z'
domains:
- biomedical
- genomics
- proteomics
---
EvoWeb

## Description

EvoWeb - An Open Knowledge Graph of Co-evolving Genes (NIAID)

EvoWeb is a weighted network of protein-protein functional relations reconstructed
from prior knowledge available from genomic sequences. It continues the EvoWeaver
project and supports discovery of proteins involved in complexes or biochemical pathways.

*This resource was automatically synchronized from the FRINK OKN registry.*
