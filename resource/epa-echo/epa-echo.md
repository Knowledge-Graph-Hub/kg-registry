---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://echo.epa.gov/
  label: US Environmental Protection Agency
creation_date: '2026-07-01T00:00:00Z'
description: EPA Enforcement and Compliance History Online (ECHO) is a US Environmental
  Protection Agency web resource that provides access to compliance and enforcement
  information for regulated facilities, along with integrated environmental data downloads.
  ECHO hosts the PFAS Analytic Tools, which aggregate per- and polyfluoroalkyl substance
  (PFAS) information from multiple EPA programs, including drinking water sampling,
  clean water discharge monitoring, facility registry records, and greenhouse gas
  reporting, into downloadable, filterable datasets. SAWGraph obtains several of its
  federal PFAS datasets through the ECHO PFAS Analytic Tools download interface.
domains:
- environment
- public health
- chemistry and biochemistry
homepage_url: https://echo.epa.gov/
id: epa-echo
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: EPA Enforcement and Compliance History Online (ECHO)
products:
- category: GraphicalInterface
  description: The ECHO landing page providing access to facility compliance and enforcement
    information, data downloads, and analytic tools.
  format: http
  id: epa-echo.landing
  name: EPA ECHO landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-echo
  product_url: https://echo.epa.gov/
- category: GraphicalInterface
  description: The ECHO PFAS Analytic Tools, which aggregate PFAS data from multiple
    EPA programs into downloadable, filterable datasets by state and program.
  format: http
  id: epa-echo.pfas-tools
  name: EPA PFAS Analytic Tools
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-echo
  product_url: https://echo.epa.gov/trends/pfas-tools
---
## Description

EPA Enforcement and Compliance History Online (ECHO) is a US Environmental
Protection Agency web resource for facility compliance and enforcement
information and integrated environmental data downloads. Its PFAS Analytic
Tools consolidate per- and polyfluoroalkyl substance data drawn from several
EPA programs into downloadable, filterable datasets.

SAWGraph obtains several of its federal PFAS occurrence and release datasets
(such as drinking water sampling and greenhouse gas reporting) through the ECHO
PFAS Analytic Tools download interface.
