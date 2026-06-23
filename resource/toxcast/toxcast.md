---
activity_status: active
category: DataSource
collection:
- ber
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
id: toxcast
last_modified_date: '2026-06-18T00:00:00Z'
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
    and bioactivity data via the CompTox Chemicals Dashboard.
  format: http
  id: toxcast.api
  name: CompTox Chemicals Dashboard API (ToxCast)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://api-ccte.epa.gov/dashboard/
- category: Product
  description: Bulk release archives (assay annotations, hit-call data, summary tables)
    for ToxCast phases.
  id: toxcast.downloads
  name: ToxCast Bulk Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://www.epa.gov/chemical-research/toxicity-forecasting#data
---
# ToxCast