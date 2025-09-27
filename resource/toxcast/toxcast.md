---
activity_status: active
category: DataSource
collection:
- ber
creation_date: '2025-09-04T00:00:00Z'
description: ToxCast (US EPA Toxicity Forecaster) is a high-throughput screening program generating bioactivity profiles for thousands of environmental chemicals across diverse in vitro assays to prioritize substances for hazard characterization, integrate exposure and pathway information, and support predictive toxicology.
domains:
  - toxicology
  - environment
  - public health
  - biomedical
id: toxcast
last_modified_date: '2025-09-16T00:00:00Z'
layout: resource_detail
name: ToxCast
license:
  id: https://www.epa.gov/privacy/privacy-and-security-notice
  label: EPA Data Usage & Privacy Notice (public domain / open government data)
products:
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - aop-wiki
  - ctd
  - toxcast
  - disgenet
  - ncbigene
  - string
  - 1000genomes
  - ensembl
  - gwascatalog
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
  secondary_source:
  - aop-db
- id: toxcast.portal
  name: EPA ToxCast Portal
  description: Landing page describing the ToxCast high-throughput screening program and providing links to data and documentation.
  category: GraphicalInterface
  product_url: https://www.epa.gov/chemical-research/toxicity-forecasting
- id: toxcast.api
  name: CompTox Chemicals Dashboard API (ToxCast)
  description: REST API providing programmatic access to ToxCast-related assay, chemical, and bioactivity data via the CompTox Chemicals Dashboard.
  category: ProgrammingInterface
  product_url: https://api-ccte.epa.gov/dashboard/
- id: toxcast.downloads
  name: ToxCast Bulk Data Downloads
  description: Bulk release archives (assay annotations, hit-call data, summary tables) for ToxCast phases.
  category: Product
  product_url: https://www.epa.gov/chemical-research/toxicity-forecasting#data
---
# ToxCast
