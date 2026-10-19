---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/comptox-tools/forms/contact-us-about-comptox-tools
  label: US EPA Center for Computational Toxicology and Exposure (CCTE)
creation_date: '2026-10-19T00:00:00Z'
description: The Toxicity Reference Database (ToxRefDB) is a US EPA database of in
  vivo animal toxicity study data from thousands of guideline or guideline-like studies
  covering over 1,000 chemicals. Study designs, doses, treatment-related effects,
  and endpoints are recorded with a controlled vocabulary, making the data structured
  and computable. ToxRefDB supports retrospective and predictive toxicology analyses,
  including the validation and benchmarking of in vitro high-throughput screening
  and other new approach methodologies (NAMs).
domains:
- toxicology
- chemistry and biochemistry
- public health
homepage_url: https://www.epa.gov/comptox-tools/downloadable-computational-toxicology-data
id: toxrefdb
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0
name: ToxRefDB (Toxicity Reference Database)
products:
- category: Product
  description: ToxRefDB database package and associated files (v3.0, released August
    2025), distributed through EPA's figshare repository.
  format: mixed
  id: toxrefdb.download
  latest_version: 10.23645/epacomptox.6062545.v5
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0
  name: ToxRefDB Database Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxrefdb
  product_url: https://epa.figshare.com/articles/dataset/Animal_Toxicity_Studies_Effects_and_Endpoints_Toxicity_Reference_Database_-_ToxRefDB_files_/6062545
- category: Product
  description: GitHub repository for US EPA's Toxicity Reference Database (ToxRefDB).
  format: http
  id: toxrefdb.repository
  name: ToxRefDB GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxrefdb
  product_url: https://github.com/USEPA/CompTox-ToxRefDB
- category: GraphicalInterface
  description: Web interface to the CompTox Chemicals Dashboard, supporting search
    by chemical identifiers (e.g., DTXSID, CASRN), product use categories, and assays/genes,
    plus advanced (mass/formula) and batch searches, with per-chemical pages covering
    chemistry, hazard, bioactivity, ADME/IVIVE, and exposure data.
  format: http
  id: comptox-dashboard.portal
  is_public: true
  name: CompTox Chemicals Dashboard Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:wasDerivedFrom
    source: dsstoxdb
  - relation_type: prov:wasDerivedFrom
    source: toxcast
  - relation_type: prov:wasDerivedFrom
    source: tox21
  - relation_type: prov:wasDerivedFrom
    source: toxvaldb
  - relation_type: prov:wasDerivedFrom
    source: toxrefdb
  - relation_type: prov:wasDerivedFrom
    source: httk
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  product_url: https://comptox.epa.gov/dashboard
- category: Product
  description: EPA's downloadable computational toxicology data page, collecting bulk
    downloads of the datasets surfaced in the Dashboard (e.g., DSSTox identifiers,
    invitrodb, ToxRefDB, ToxValDB, CPDat, HTTK).
  format: mixed
  id: comptox-dashboard.downloads
  name: Downloadable Computational Toxicology Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:wasDerivedFrom
    source: dsstoxdb
  - relation_type: prov:wasDerivedFrom
    source: toxcast
  - relation_type: prov:wasDerivedFrom
    source: toxrefdb
  - relation_type: prov:wasDerivedFrom
    source: toxvaldb
  - relation_type: prov:wasDerivedFrom
    source: httk
  product_url: https://www.epa.gov/comptox-tools/downloadable-computational-toxicology-data
- category: Product
  description: ToxValDB database releases (current v9.7.0, with archived versions),
    distributed through EPA's figshare repository.
  format: mixed
  id: toxvaldb.download
  latest_version: 10.23645/epacomptox.20394501.v11
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0
  name: ToxValDB Database Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxvaldb
  - relation_type: prov:wasDerivedFrom
    source: toxrefdb
  product_url: https://epa.figshare.com/articles/dataset/ToxValDB_v9_1/20394501
- category: ProcessProduct
  description: R package of scripts that transform staged source data into the normalized
    main ToxValDB format, including loaders for ToxRefDB data.
  format: r
  id: toxvaldb.main
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: toxvaldbmain R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxvaldb
  - relation_type: prov:wasDerivedFrom
    source: toxrefdb
  product_url: https://github.com/USEPA/toxvaldbmain
publications:
- authors:
  - Madison Feshuk
  - Lori Kolaczkowski
  - Sean Watford
  - Katie Paul Friedman
  doi: 10.3389/ftox.2023.1260305
  id: https://doi.org/10.3389/ftox.2023.1260305
  journal: Frontiers in Toxicology
  preferred: true
  title: 'ToxRefDB v2.1: update to curated in vivo study data in the Toxicity Reference
    Database'
  year: '2023'
- authors:
  - Sean Watford
  - Ly Ly Pham
  - Jessica Wignall
  - Robert Shin
  - Matthew T. Martin
  - Katie Paul Friedman
  doi: 10.1016/j.reprotox.2019.07.012
  id: https://doi.org/10.1016/j.reprotox.2019.07.012
  journal: Reproductive Toxicology
  title: 'ToxRefDB version 2.0: Improved utility for predictive and retrospective
    toxicology analyses'
  year: '2019'
repository: https://github.com/USEPA/CompTox-ToxRefDB
---
# ToxRefDB (Toxicity Reference Database)

## Overview

The Toxicity Reference Database (ToxRefDB) is maintained by the US EPA Center for Computational Toxicology and Exposure. It holds structured in vivo animal toxicity study data from guideline and guideline-like studies. EPA uses it as a reference set of in vivo outcomes, against which in vitro high-throughput screening and other new approach methodologies (NAMs) can be validated and benchmarked.

## Data Content

- In vivo study data from thousands of guideline or guideline-like studies covering over 1,000 chemicals.
- Study design, dosing, and treatment-related effect and endpoint information, recorded with a controlled vocabulary.
- The current release is v3.0 (August 2025). ToxRefDB data also feed the hazard data in ToxValDB and the CompTox Chemicals Dashboard.

## Access

- EPA downloadable data page: https://www.epa.gov/comptox-tools/downloadable-computational-toxicology-data
- Database package (figshare): https://epa.figshare.com/articles/dataset/Animal_Toxicity_Studies_Effects_and_Endpoints_Toxicity_Reference_Database_-_ToxRefDB_files_/6062545
- GitHub: https://github.com/USEPA/CompTox-ToxRefDB

## License

The ToxRefDB files on EPA's figshare are released under CC0. As an EPA product, ToxRefDB is also a U.S. Government Work.