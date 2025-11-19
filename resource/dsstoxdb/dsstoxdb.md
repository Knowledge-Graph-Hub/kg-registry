---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: EPA's Distributed Structure-Searchable Toxicity (DSSTox) database provides high-quality chemical and chemistry data underpinning several publicly available computational toxicology applications. DSSTox contains curated chemical substances mapped to chemical identifiers including CAS Registry Numbers, IUPAC names, SMILES, and InChIKeys. The database currently exceeds 1.2 million substances which includes chemical lists of interest to EPA, other federal agencies, states, tribes, industry and stakeholder groups. DSSTox provides accurate linkages of chemical structures to source substance identifiers, allowing high-quality association of chemicals to existing toxicity data, bioactivity data, experimental chemical property data and enabling structure-based predictive modeling. The database supports the CompTox Chemicals Dashboard, EcoTox Knowledgebase, Chemical Exposure Knowledgebase, and other EPA tools.
domains:
  - toxicology
  - chemistry and biochemistry
  - environment
id: dsstoxdb
infores_id: dsstoxdb
last_modified_date: '2025-11-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0
name: Distributed Structure-Searchable Toxicity (DSSTox) Database
homepage_url: https://www.epa.gov/chemical-research/distributed-structure-searchable-toxicity-dsstox-database
products:
  - category: GraphicalInterface
    description: Web-based interface for searching over 1.2 million chemicals with integrated toxicity, bioactivity, and exposure data
    format: http
    id: dsstoxdb.dashboard
    name: CompTox Chemicals Dashboard
    original_source:
      - dsstoxdb
    product_url: https://comptox.epa.gov/dashboard/
  - category: MappingProduct
    description: Downloadable Excel and CSV files containing DSSTox identifiers mapped to CAS numbers, InChIKeys, SMILES, molecular formulas, and other chemical identifiers for over 1.2 million substances
    format: mixed
    id: dsstoxdb.downloads
    name: DSSTox Data Downloads
    original_source:
      - dsstoxdb
    product_url: https://epa.figshare.com/articles/dataset/Chemistry_Dashboard_Data_DSSTox_Identifiers_Mapped_to_CAS_Numbers_and_Names/5588566
  - category: ProgrammingInterface
    description: Public API providing programmatic access to DSSTox chemical data and computational toxicology information
    format: http
    id: dsstoxdb.api
    name: EPA CompTox API
    original_source:
      - dsstoxdb
    product_url: https://api-ccte.epa.gov/docs/index.html
---

# Distributed Structure-Searchable Toxicity (DSSTox) Database

EPA's Distributed Structure-Searchable Toxicity (DSSTox) database is a comprehensive public resource for high-quality chemical and chemistry data. From its inception in 2004, DSSTox has focused on quality data curation to resolve chemical identifier errors and ensure accurate chemical structure alignment with data important to assessing chemical risk.

## Key Features

- **Over 1.2 million curated substances** with quality-controlled chemical identifiers
- **Accurate structure-identifier mappings** including CAS RNs, IUPAC names, SMILES, InChIKeys
- **Multi-tiered quality control** with five QC levels conveying curator confidence
- **Integration with EPA tools** including CompTox Chemicals Dashboard, EcoTox Knowledgebase, and Chemical Exposure Knowledgebase
- **Public data access** through web applications, API, and downloadable files

## Background

DSSTox started as a manual curation of 7,000 chemicals and expanded using auto-loads from EPA's Substance Registry Services (SRS), the National Library of Medicine's ChemID, and PubChem. The curation process requires uniquely mapped identifiers (CAS RN, name, and structure) for each substance, rejecting content where any two identifiers conflict either within or across datasets.

## Information Resource ID

This resource has the Information Resource identifier: `infores:dsstoxdb`
