---
layout: resource_detail
id: goldterms
name: GOLD Environmental Paths
contacts:
- category: Individual
  label: Chris Mungall
  orcid: 0000-0002-6601-2165
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
description: Translation of JGI GOLD (Genomes OnLine Database) ecosystem classification paths to OWL, plus mappings to MIxS and environment ontologies like ENVO.
domains:
- environment
- microbiology
- genomics
- biological systems
homepage_url: https://gold.jgi.doe.gov/
repository: https://github.com/cmungall/gold-ontology
license:
  id: https://github.com/cmungall/gold-ontology/blob/main/LICENSE
  label: BSD 3-Clause License
tags:
- biopragmatics
- core
activity_status: active
category: DataModel
products:
- id: goldterms.data.owl
  product_url: https://w3id.org/goldterms/goldterms.owl
  name: Main GOLDTERMS OWL release
  category: DataModelProduct
  format: owl
  secondary_source:
  - goldterms
  original_source:
  - goldterms
- id: goldterms.bioportal
  product_url: https://bioportal.bioontology.org/ontologies/GOLDTERMS
  name: GOLDTERMS on BioPortal
  category: GraphicalInterface
  format: owl
  secondary_source:
  - goldterms
  original_source:
  - goldterms
- id: goldterms.definitions.yaml
  product_url: https://github.com/cmungall/gold-ontology/blob/main/gold_definitions.yaml
  name: GOLD definitions in YAML format
  category: DataModelProduct
  format: yaml
  secondary_source:
  - goldterms
  original_source:
  - goldterms
collection:
- translator
---

A rendering of the GOLD (Genomes OnLine Database) ecosystem classification as OWL, plus mappings to MIxS and environment ontologies. The ontology represents environmental classification paths from GOLD, organizing them into a hierarchical structure with three main branches:

1. Environmental - Representing natural environments (aquatic, terrestrial, etc.)
2. Host-associated - Representing environments associated with organisms
3. Engineered - Representing human-created environments

Each GOLD path is represented as a class with logical definitions equivalent to the path components. The ontology also includes mappings between GOLD paths and environment ontology expressions (primarily ENVO), conforming to MIxS standards, facilitating interoperability between environmental metadata systems.
