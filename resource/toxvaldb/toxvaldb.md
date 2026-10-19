---
activity_status: active
category: Aggregator
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/comptox-tools/forms/contact-us-about-comptox-tools
  label: US EPA Center for Computational Toxicology and Exposure (CCTE)
creation_date: '2026-10-19T00:00:00Z'
description: The US EPA Toxicity Values Database (ToxValDB) is a large compilation
  of human health-relevant in vivo toxicology data and risk assessment values, covering
  both in vivo toxicity experiment results and derived toxicity and guideline values.
  It was created because consistently annotated, computable toxicology data were needed
  to develop and validate new approach methodologies (NAMs). ToxValDB has
  two components. ToxValDB Stage keeps data close to each source's structure and terminology,
  and main ToxValDB maps all source data to a consistent structure and set of vocabularies.
  Version 9.7.0 contains 249,071 records covering 41,855 chemicals from 51 sources.
domains:
- toxicology
- chemistry and biochemistry
- public health
homepage_url: https://www.epa.gov/comptox-tools/downloadable-computational-toxicology-data
id: toxvaldb
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0
name: ToxValDB (Toxicity Values Database)
products:
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
  description: R package used to process and stage source data for loading into ToxValDB
    (ToxValDB Stage).
  format: r
  id: toxvaldb.stage
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: toxvaldbstage R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxvaldb
  product_url: https://github.com/USEPA/toxvaldbstage
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
- category: ProgrammingInterface
  description: The EPA Computational Toxicology and Exposure (CTX) APIs, providing
    programmatic access to the chemical, hazard, bioactivity, and exposure data domains
    that underlie the CompTox Chemicals Dashboard. A free API key is required.
  format: http
  id: comptox-dashboard.ctx-api
  name: CTX (Computational Toxicology and Exposure) APIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:wasDerivedFrom
    source: dsstoxdb
  - relation_type: prov:wasDerivedFrom
    source: toxcast
  - relation_type: prov:wasDerivedFrom
    source: toxvaldb
  product_url: https://www.epa.gov/comptox-tools/computational-toxicology-and-exposure-apis-about
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
publications:
- authors:
  - Jonathan T. Wall
  - Risa R. Sayre
  - Doris Smith
  - Samuel Winter
  - Maxwell Groover
  - Jasmine Hope
  - Adriana Webb
  - Katie Paul Friedman
  - Madison Feshuk
  - Antony J. Williams
  - Charles Lowe
  - Nisha S. Sipes
  - Jason Lambert
  - Jennifer H. Olker
  - Russell S. Thomas
  - Colleen Elonen
  - Richard S. Judson
  - Chelsea A. Weitekamp
  doi: 10.1016/j.comtox.2025.100365
  id: https://doi.org/10.1016/j.comtox.2025.100365
  journal: Computational Toxicology
  preferred: true
  title: 'Development of the toxicity values database, ToxValDB: A curated resource
    for experimental and derived human health-relevant toxicity data'
  year: '2025'
repository: https://github.com/USEPA/toxvaldbmain
---
# ToxValDB (Toxicity Values Database)

## Overview

The Toxicity Values Database (ToxValDB) is a US EPA compilation of human health-relevant in vivo toxicology data and risk assessment values. EPA built it to supply consistently annotated, computable toxicology data for developing and validating new approach methodologies (NAMs). ToxValDB supplies the hazard data shown in the CompTox Chemicals Dashboard.

## Data Content

- Summary-level in vivo toxicity experiment results, plus derived toxicity and guideline values, from many federal, state, and international sources (including ToxRefDB).
- Two components: ToxValDB Stage, which keeps data close to each source's structure and terminology, and main ToxValDB, which maps all data to a consistent structure and set of vocabularies.
- Version 9.7.0: 249,071 records covering 41,855 chemicals (27,068 with a defined chemical structure) from 51 sources (74 source tables).

## Access

- EPA downloadable data page: https://www.epa.gov/comptox-tools/downloadable-computational-toxicology-data
- Current and archived releases (figshare): https://epa.figshare.com/articles/dataset/ToxValDB_v9_1/20394501
- Processing code: https://github.com/USEPA/toxvaldbstage and https://github.com/USEPA/toxvaldbmain

## License

The ToxValDB releases on EPA's figshare are released under CC0, and the processing code repositories are MIT-licensed. Values compiled from external sources come from those sources.