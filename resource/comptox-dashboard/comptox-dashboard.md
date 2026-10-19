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
description: The CompTox Chemicals Dashboard (formerly the Chemistry Dashboard) is
  a US Environmental Protection Agency (EPA) web application that integrates chemistry,
  toxicity, and exposure information for over one million chemicals, with over 300
  chemical lists based on structure or category. Built on the DSSTox chemical database,
  it brings together physicochemical properties, environmental fate and transport,
  exposure and use data, in vivo hazard data (ToxValDB, ToxRefDB), in vitro bioactivity
  from the ToxCast and Tox21 high-throughput screening programs (invitrodb), and high-throughput
  toxicokinetic (HTTK) ADME/IVIVE predictions. Its data and models support chemical
  prioritization and efforts to reduce animal use in chemical testing through new
  approach methodologies (NAMs).
domains:
- chemistry and biochemistry
- cheminformatics
- toxicology
- environment
- environmental exposure
- drug discovery
- high-throughput screening
- public health
homepage_url: https://comptox.epa.gov/dashboard
id: comptox-dashboard
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain)
name: CompTox Chemicals Dashboard
products:
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
- category: DocumentationProduct
  description: Release notes for the CompTox Chemicals Dashboard, listing feature
    updates and the versions of underlying data sources (e.g., ToxValDB, ToxRefDB,
    invitrodb, httk) loaded in each release.
  format: http
  id: comptox-dashboard.release-notes
  name: CompTox Chemicals Dashboard Release Notes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  product_url: https://www.epa.gov/comptox-tools/comptox-chemicals-dashboard-release-notes
- category: GraphicalInterface
  description: Web portal for searching participating chemical information sources
    by substance identifiers, by chemical property and endpoint values, and by GHS
    classification, with direct links to the corresponding records in each source.
  format: http
  id: echemportal.portal
  name: eChemPortal Search Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: echemportal
  - relation_type: prov:wasDerivedFrom
    source: comptox-dashboard
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  product_url: https://www.echemportal.org/echemportal/
publications:
- authors:
  - Antony J. Williams
  - Christopher M. Grulke
  - Jeff Edwards
  - Andrew D. McEachran
  - Kamel Mansouri
  - Nancy C. Baker
  - Grace Patlewicz
  - Imran Shah
  - John F. Wambaugh
  - Richard S. Judson
  - Ann M. Richard
  doi: 10.1186/s13321-017-0247-6
  id: https://doi.org/10.1186/s13321-017-0247-6
  journal: Journal of Cheminformatics
  preferred: true
  title: 'The CompTox Chemistry Dashboard: a community data resource for environmental
    chemistry'
  year: '2017'
synonyms:
- CompTox Chemistry Dashboard
---
# CompTox Chemicals Dashboard

## Overview

The CompTox Chemicals Dashboard is a web application from the US EPA Center for Computational Toxicology and Exposure (CCTE). Formerly called the Chemistry Dashboard, it integrates chemistry, toxicity, and exposure information for over one million chemicals so that decision-makers and scientists can evaluate thousands of chemicals quickly. EPA notes that the data and models in the Dashboard help identify the chemicals that most need further testing and help reduce the use of animals in chemical testing.

## Data Content

- Chemical identity and structure data from DSSTox, with over 300 chemical lists.
- Measured and predicted physicochemical and environmental fate/transport properties.
- In vivo hazard data from ToxValDB and ToxRefDB.
- In vitro bioactivity from the ToxCast and Tox21 high-throughput screening programs (invitrodb).
- High-throughput toxicokinetic (HTTK) ADME and in vitro to in vivo extrapolation (IVIVE) predictions.
- Exposure, product use, and production volume information.

## Access

- Web application: https://comptox.epa.gov/dashboard
- CTX APIs (API key required): https://www.epa.gov/comptox-tools/computational-toxicology-and-exposure-apis-about
- Bulk downloads: https://www.epa.gov/comptox-tools/downloadable-computational-toxicology-data

## License

The Dashboard is produced by the US EPA. As a work of the U.S. federal government it is generally in the public domain (U.S. Government Work). Individual underlying datasets may carry their own terms; for example, EPA distributes several of them on figshare under CC0.