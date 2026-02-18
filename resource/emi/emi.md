---
activity_status: active
category: Ontology
creation_date: '2026-01-15T00:00:00Z'
description: The Earth Metabolome Initiative (EMI) Ontology provides classes and properties
  for metabolites, taxonomy, traits, interactions, and associated metadata used to
  build METRIN-KG.
domains:
- biological systems
- chemistry and biochemistry
homepage_url: https://www.earthmetabolome.org/earth_metabolome_ontology/
id: emi
infores_id: emi
last_modified_date: '2026-01-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Earth Metabolome Initiative Ontology
products:
- category: OntologyProduct
  description: Canonical EMI ontology release (TTL)
  format: ttl
  id: emi.ttl
  name: EMI Ontology TTL
  original_source:
  - emi
  product_file_size: 66397
  product_url: https://w3id.org/emi
- category: GraphProduct
  description: Graph version of the Earth Metabolome Initiative Ontology
  format: kgx
  id: emikg.kg
  name: EMI Knowledge Graph
  original_source:
  - emi
  - pf1600
  - globi
  - try
  product_url: https://doi.org/10.5281/zenodo.17079767
  repository: https://github.com/earth-metabolome-initiative/metrin-kg
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ Timeout connecting
    to URL
- category: ProgrammingInterface
  description: SPARQL endpoint for programmatic access to the EMI Knowledge Graph
  format: http
  id: emikg.sparql
  name: EMI KG SPARQL Endpoint
  original_source:
  - emi
  - pf1600
  - globi
  - try
  product_url: https://qlever.earthmetabolome.org/api/metrin-kg
- category: GraphicalInterface
  description: Web-based SPARQL query editor for the EMI Knowledge Graph
  id: emikg.web
  name: EMI KG SPARQL Query Editor
  original_source:
  - emi
  - pf1600
  - globi
  - try
  product_url: https://sib-swiss.github.io/sparql-editor/emi
repository: https://github.com/earth-metabolome-initiative/earth_metabolome_ontology
---
# Earth Metabolome Initiative Ontology

## Overview

The EMI Ontology defines the semantic model that underpins METRIN-KG, covering metabolites, traits, interactions, taxonomy, and related metadata. Releases are published at the persistent URI https://w3id.org/emi and maintained openly on GitHub.