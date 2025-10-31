---
activity_status: active
category: KnowledgeGraph
collection:
- ber
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: MJoachimiak@lbl.gov
  - contact_type: github
    value: realmarcin
  label: Marcin P. Joachimiak
description: A Knowledge Graph about microbes. The KG is designed to integrate diverse
  knowledge about microbes from a variety of structured and unstructured sources.
domains:
- microbiology
- organisms
- phenotype
- microbiome
- biological systems
homepage_url: https://kghub.org/kg-microbe/index.html
id: kg-microbe
layout: resource_detail
license:
  id: https://opensource.org/license/bsd-3-clause
  label: BSD3
name: KG Microbe
products:
- category: GraphProduct
  compression: targz
  description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
  format: kgx
  id: kg-microbe.graph.raw
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: KG-Microbe KGX Graph - Raw
  original_source:
  - kg-microbe
  product_url: https://kghub.io/kg-microbe/KGMicrobe-raw-20250222.tar.gz
  secondary_source:
  - kg-microbe
  warnings:
  - File was not able to be retrieved when checked on 2025-10-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-10-31: HTTP 403 error
    when accessing file'
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - kg-microbe
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - kg-microbe
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - kg-microbe
  product_file_size: 4623010863
  product_url: https://kghub.io/kg-microbe/KGMicrobe-function-20250222.tar.gz
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - kg-microbe
  product_file_size: 4640682152
  product_url: https://kghub.io/kg-microbe/KGMicrobe-biomedical-function-20250222.tar.gz
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: UniProt proteins from microbes, as graph nodes and edges
  format: kgx
  id: kg-microbe.graph.uniprot
  name: KG-Microbe UniProt microbe transform
  original_source:
  - uniprot
  product_file_size: 4796343398
  product_url: https://kghub.io/kg-microbe/KGMicrobe-transformed-uniprot-microbes-20240924.tar.gz
  secondary_source:
  - kg-microbe
repository: https://github.com/Knowledge-Graph-Hub/kg-microbe
---
KG-Microbe.