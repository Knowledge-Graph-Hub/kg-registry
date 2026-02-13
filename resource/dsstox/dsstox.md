---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: EPA_ComptoxTools@epa.gov
  label: EPA CCTE
description: EPA's Distributed Structure-Searchable Toxicity (DSSTox) Database contains
  curated chemical substances mapped to data including chemical identifiers and structure
  representations, providing the chemical underpinning for EPA's computational toxicology
  tools.
domains:
- biomedical
- chemistry and biochemistry
- environment
- health
homepage_url: https://www.epa.gov/comptox-tools/distributed-structure-searchable-toxicity-dsstox-database
id: dsstox
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0
name: DSSTox
products:
- category: Product
  description: The complete DSSTox database containing over 1.2 million chemical substances
    with identifiers and structures
  format: csv
  id: dsstox.complete
  name: DSSTox Complete Database
  product_url: https://doi.org/10.23645/epacomptox.5588566
  warnings: []
- category: GraphicalInterface
  description: The CompTox Chemicals Dashboard provides access to the DSSTox database
    through a web interface
  format: http
  id: dsstox.dashboard
  name: CompTox Chemicals Dashboard
  product_url: https://comptox.epa.gov/dashboard
- category: ProgrammingInterface
  description: Public API for programmatic access to DSSTox data
  id: dsstox.api
  is_public: true
  name: CompTox API
  product_url: https://api-ccte.epa.gov/docs/index.html
- category: DocumentationProduct
  description: Documentation for the DSSTox database
  format: docx
  id: dsstox.description
  name: DSSToxDB Description
  product_url: https://clowder.edap-cluster.com/files/6616d945e4b063812d70fcb5?dataset=61147fefe4b0856fdc65639b&space=&folder=6616d85ce4b063812d70fc8f
  warnings:
  - File was not able to be retrieved when checked on 2026-01-30_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-13: HTTP 404 error
    when accessing file'
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
publications:
- authors:
  - Williams AJ
  - Grulke CM
  - Edwards J
  - McEachran AD
  - Mansouri K
  - Baker NC
  - Patlewicz G
  - Shah I
  - Wambaugh JF
  - Judson RS
  - Richard AM
  doi: 10.1186/s13321-017-0247-6
  id: doi:10.1186/s13321-017-0247-6
  journal: Journal of Cheminformatics
  preferred: true
  title: 'The CompTox Chemistry Dashboard: a community data resource for environmental
    chemistry'
  year: '2017'
---
# DSSTox

The Distributed Structure-Searchable Toxicity (DSSTox) Database is maintained by the US Environmental Protection Agency (EPA) Center for Computational Toxicology and Exposure (CCTE). It serves as a comprehensive chemical resource that currently includes over 1.2 million chemical substances with accurate mappings between chemical structures and identifiers such as Chemical Abstract Service Registry Numbers (CAS RNs) and chemical names.

## Overview

DSSTox provides the chemical foundation for several EPA computational toxicology applications including:

- The CompTox Chemicals Dashboard
- The Ecotoxicity Knowledgebase
- The Chemical Exposure Knowledgebase
- Other computational toxicology tools

Since its inception in 2004, DSSTox has focused on high-quality data curation to ensure accurate chemical structure alignment with identifiers. This accuracy is critical for chemical risk assessments and computational toxicology applications.

## Data Content

The database includes:
- Chemical identifiers (synonyms, systematic names, CAS RNs)
- Chemical structure representations
- Mappings to InChIKeys, SMILES, molecular formulas
- Physical-chemical properties
- Links to toxicity and bioactivity data

## Access

DSSTox data is publicly available through:
1. The CompTox Chemicals Dashboard web interface
2. Downloadable Excel/CSV files through the EPA's figshare repository
3. A public API for programmatic access
4. Integration with other EPA tools and databases

All data is provided under a Creative Commons Zero (CC0) public domain dedication, allowing unrestricted use of the data.