---
activity_status: active
category: DataModel
collection:
- translator
- ber
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
  label: Chris Mungall
  orcid: 0000-0002-6601-2165
description: Translation of JGI GOLD (Genomes OnLine Database) ecosystem classification
  paths to OWL, plus mappings to MIxS and environment ontologies like ENVO.
domains:
- environment
- microbiology
- genomics
- biological systems
homepage_url: https://gold.jgi.doe.gov/
id: goldterms
layout: resource_detail
license:
  id: https://github.com/cmungall/gold-ontology/blob/main/LICENSE
  label: BSD 3-Clause License
name: GOLD Environmental Paths
products:
- category: DataModelProduct
  format: owl
  id: goldterms.data.owl
  name: Main GOLDTERMS OWL release
  original_source:
  - goldterms
  product_url: https://w3id.org/goldterms/goldterms.owl
  secondary_source:
  - goldterms
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-09-11_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2025-12-05: HTTP 404 error
    when accessing file'
- category: GraphicalInterface
  format: owl
  id: goldterms.bioportal
  name: GOLDTERMS on BioPortal
  original_source:
  - goldterms
  product_url: https://bioportal.bioontology.org/ontologies/GOLDTERMS
  secondary_source:
  - goldterms
- category: DataModelProduct
  format: yaml
  id: goldterms.definitions.yaml
  name: GOLD definitions in YAML format
  original_source:
  - goldterms
  product_file_size: 27808
  product_url: https://github.com/cmungall/gold-ontology/blob/main/gold_definitions.yaml
  secondary_source:
  - goldterms
repository: https://github.com/cmungall/gold-ontology
tags:
- biopragmatics
- core
---
A rendering of the GOLD (Genomes OnLine Database) ecosystem classification as OWL, plus mappings to MIxS and environment ontologies. The ontology represents environmental classification paths from GOLD, organizing them into a hierarchical structure with three main branches:

1. Environmental - Representing natural environments (aquatic, terrestrial, etc.)
2. Host-associated - Representing environments associated with organisms
3. Engineered - Representing human-created environments

Each GOLD path is represented as a class with logical definitions equivalent to the path components. The ontology also includes mappings between GOLD paths and environment ontology expressions (primarily ENVO), conforming to MIxS standards, facilitating interoperability between environmental metadata systems.