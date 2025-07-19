---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://indra.readthedocs.io/en/latest/
  - contact_type: github
    value: sorgerlab
  label: Sorger Lab, Harvard Medical School
description: >-
  INDRA (Integrated Network and Dynamical Reasoning Assembler) is an automated 
  model assembly system interfacing with NLP systems and databases to collect 
  knowledge, and through a process of assembly, produce causal graphs and 
  dynamical models.
domains:
- biomedical
- systems biology
homepage_url: https://www.indra.bio/
id: indra
layout: resource_detail
license:
  id: https://opensource.org/licenses/BSD-2-Clause
  label: BSD 2-Clause License
name: INDRA
repository: https://github.com/sorgerlab/indra
products:
- category: GraphicalInterface
  description: Web interface for the INDRA Biomedical Discovery Engine
  format: http
  id: indra.discovery
  name: INDRA Biomedical Discovery Engine
  original_source:
  - indra
  product_url: https://discovery.indra.bio/
- category: ProcessProduct
  description: Python library for automated model assembly from mechanistic knowledge
  format: python
  id: indra.python
  name: INDRA Python Library
  original_source:
  - indra
  product_url: https://github.com/sorgerlab/indra
  repository: https://github.com/sorgerlab/indra
- category: GraphProduct
  description: INDRA Network Search KG for pathway-level biomedical discovery
  format: kgx
  id: indra.network_search
  name: INDRA Network Search KG
  original_source:
  - ctd
  - drugbank
  - chembl
  - biogrid
  - hprd
  - signor
  - omnipath
  - biopax
  - phosphoelm
  - indra
  product_url: https://discovery.indra.bio/
  secondary_source:
  - indra
publications:
- id: https://doi.org/10.1038/s41587-019-0364-4
  journal: Nature Biotechnology
  preferred: true
  title: >-
    INDRA: a crowd-sourced machine reading platform for mechanistic reasoning in 
    biomedical text
  year: '2020'
tags:
- biopragmatics
- translator
---

INDRA (Integrated Network and Dynamical Reasoning Assembler) is an automated 
model assembly system that interfaces with natural language processing systems 
and structured databases to collect mechanistic and causal assertions. It 
represents them in a standardized form (INDRA Statements) and assembles them 
into various modeling formalisms including causal graphs and dynamical models.

## Key Features

- **Knowledge Integration**: Aggregates mechanistic information from multiple 
  sources including pathway databases, literature extraction via NLP, and 
  curated databases
- **Standardized Representation**: Converts diverse knowledge into uniform 
  INDRA Statements format
- **Assembly Procedures**: Applies knowledge-level assembly to correct 
  systematic errors, resolve redundancies, and assess reliability
- **Multiple Output Formats**: Generates causal graphs, rule-based models 
  (PySB), and network models

## Data Sources

INDRA integrates knowledge from numerous biomedical resources including:

### Pathway Databases
- BioPAX format databases
- SIGNOR
- BioGRID
- Human Protein Reference Database (HPRD)
- Phospho.ELM
- OmniPath

### Chemical Information
- DrugBank
- ChEMBL
- Comparative Toxicogenomics Database (CTD)

### Literature Mining
- Multiple NLP systems (REACH, TRIPS, Sparser, etc.)
- PubMed abstracts and full-text articles

## Applications

- Pathway analysis and modeling
- Drug discovery and mechanism elucidation
- Systems biology model construction
- Biomedical hypothesis generation
- Network-based discovery

## Access

INDRA is available as:
- Open-source Python library
- Web-based discovery interface
- REST API for programmatic access
- Docker containers for deployment
