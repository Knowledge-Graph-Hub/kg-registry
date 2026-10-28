---
activity_status: active
category: DataSource
collection:
- ber
- nams
creation_date: '2025-09-04T00:00:00Z'
description: ToxCast (US EPA Toxicity Forecaster) is a high-throughput screening program
  generating bioactivity profiles for thousands of environmental chemicals across
  diverse in vitro assays to prioritize substances for hazard characterization, integrate
  exposure and pathway information, and support predictive toxicology.
domains:
- toxicology
- environment
- public health
- biomedical
- drug discovery
- high-throughput screening
homepage_url: https://www.epa.gov/comptox-tools/toxicity-forecasting-toxcast
id: toxcast
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://www.epa.gov/privacy/privacy-and-security-notice
  label: EPA Data Usage & Privacy Notice (public domain / open government data)
name: ToxCast
products:
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  format: http
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
- category: GraphicalInterface
  description: Landing page describing the ToxCast high-throughput screening program
    and providing links to data and documentation.
  format: http
  id: toxcast.portal
  name: EPA ToxCast Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://www.epa.gov/chemical-research/toxicity-forecasting
- category: ProgrammingInterface
  description: REST API providing programmatic access to ToxCast-related assay, chemical,
    and bioactivity data via the EPA Computational Toxicology and Exposure (CTX) APIs.
    The Bioactivity domain is backed by ToxCast's invitrodb. An API key (free, via
    ccte_api@epa.gov) is required for data calls.
  format: http
  id: toxcast.api
  name: EPA CTX (Computational Toxicology and Exposure) API (ToxCast Bioactivity)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://comptox.epa.gov/ctx-api/docs/
- category: Product
  description: Bulk release archives (assay annotations, hit-call data, summary tables)
    for ToxCast phases.
  format: mixed
  id: toxcast.downloads
  name: ToxCast Bulk Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://www.epa.gov/chemical-research/toxicity-forecasting#data
- category: GraphProduct
  description: RDF knowledge graph (Turtle) repackaging EPA ToxCast high-throughput
    screening data as an open knowledge graph
  format: ttl
  id: biobricks-toxcast.graph
  name: BioBricks ToxCast Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-toxcast
  - relation_type: prov:wasDerivedFrom
    source: toxcast
  product_url: https://github.com/biobricks-ai/biobricks-okg
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
- category: GraphicalInterface
  description: ToxBAI desktop application (Windows and macOS) for predicting chemical
    toxicity. Users enter substances by CAS number or SMILES, or upload an Excel file,
    and run the AO prediction models (OECD Test Guideline data) and mechanism prediction
    models (ToxCast data); results are shown as a toxicity-category heatmap and per-substance
    detail with applicability-domain flags, with AOP-linked interpretation and Excel
    report export. Requires a Google sign-in. In version 1.0 the prediction toolbox
    is available; the AOP-based AI and NGRA 1.0 panels are coming-soon placeholders.
  format: http
  id: toxbai.app
  name: ToxBAI Prediction Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxbai
  - relation_type: prov:hadPrimarySource
    source: toxcast
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: http://toxbai.com/
- category: GraphicalInterface
  description: NICE Search, the interactive query interface for exploring curated
    chemical, in vitro and high-throughput screening, physicochemical, and reference
    in vivo toxicity data by chemical, assay, endpoint, and mechanistic target, with
    filtering and export.
  format: http
  id: nice.search
  is_public: true
  name: NICE Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nice
  - relation_type: prov:hadPrimarySource
    source: toxcast
  - relation_type: prov:hadPrimarySource
    source: tox21
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: opera
  product_url: https://ice.ntp.niehs.nih.gov/search
- category: Product
  description: The NICE data downloads and dataset descriptions, providing access
    to curated chemical data, curated in vitro and high-throughput screening (cHTS)
    assay data, physicochemical and ADME property data, and reference in vivo toxicity
    datasets.
  format: http
  id: nice.data
  is_public: true
  name: NICE Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nice
  - relation_type: prov:hadPrimarySource
    source: toxcast
  - relation_type: prov:hadPrimarySource
    source: tox21
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: opera
  product_url: https://ice.ntp.niehs.nih.gov/DATASETDESCRIPTION
---
# ToxCast