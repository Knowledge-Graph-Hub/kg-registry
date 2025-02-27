---
layout: resource_detail
activity_status: active
id: kg-microbe
name: KG Microbe
description: >-
  A Knowledge Graph about microbes. The KG is designed to integrate diverse knowledge about microbes from a variety of structured and unstructured sources.
domain: organisms
contacts:
- category: Individual
  github: realmarcin
  email: MJoachimiak@lbl.gov
  label: Marcin P. Joachimiak
homepage_url: https://kghub.org/kg-microbe/index.html
repository: https://github.com/Knowledge-Graph-Hub/kg-microbe
products:
- id: kg-microbe.raw
  is_kgx: true
  name: KG-Microbe KGX Graph - Raw
  description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
  url: https://kghub.io/kg-microbe/KGMicrobe-raw-20250222.tar.gz
  compression: targz
  category: GraphProduct
- id: kg-microbe.core
  is_kgx: true
  name: KG-Microbe KGX Graph - Core
  description: >-
    The core KG KG-Microbe-Core with ontologies, organismal traits,
    and growth preferences.
  url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  compression: targz
  category: GraphProduct
- id: kg-microbe.biomedical
  is_kgx: true
  name: KG-Microbe KGX Graph - Biomedical
  description: >-
    Core plus human biomedical data (ontologies, CTD, Wallen et al)
  url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  compression: targz
  category: GraphProduct
- id: kg-microbe.function
  is_kgx: true
  name: KG-Microbe KGX Graph - Function
  description: >-
    Core plus Uniprot genome annotations
  url: https://kghub.io/kg-microbe/KGMicrobe-function-20250222.tar.gz
  compression: targz
  category: GraphProduct
- id: kg-microbe.biomedical-function
  is_kgx: true
  name: KG-Microbe KGX Graph - Biomedical-Function
  description: >-
    Biomedical plus Uniprot genome annotations
  url: https://kghub.io/kg-microbe/KGMicrobe-biomedical-function-20250222.tar.gz
  compression: targz
  category: GraphProduct
- id: kg-microbe.uniprot
  is_kgx: true
  name: KG-Microbe UniProt microbe transform
  description: UniProt proteins from microbes, as graph nodes and edges
  compression: targz
  url: https://kghub.io/kg-microbe/KGMicrobe-transformed-uniprot-microbes-20240924.tar.gz
  category: GraphProduct
license:
  label: CC0 1.0
  id: https://creativecommons.org/publicdomain/zero/1.0/
category: KnowledgeGraph
---

KG-Microbe.
