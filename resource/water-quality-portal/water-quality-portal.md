---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.waterqualitydata.us/
  label: National Water Quality Monitoring Council (USGS, EPA, NWQMC)
creation_date: '2026-07-01T00:00:00Z'
description: The Water Quality Portal (WQP) is a cooperative water quality data service
  sponsored by the US Geological Survey, the US Environmental Protection Agency, and
  the National Water Quality Monitoring Council. It integrates publicly available
  water quality monitoring data from hundreds of federal, state, tribal, and local
  organizations, exposing monitoring locations, sampling activities, and characteristic
  results (including per- and polyfluoroalkyl substance, PFAS, measurements) through
  a standardized web service. SAWGraph uses WQP water quality monitoring results as
  a primary source for PFAS occurrence in surface water and groundwater.
domains:
- environment
- public health
- chemistry and biochemistry
homepage_url: https://www.waterqualitydata.us/
id: water-quality-portal
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: Water Quality Portal (WQP)
products:
- category: GraphicalInterface
  description: The Water Quality Portal web interface for discovering and downloading
    integrated water quality monitoring data from federal, state, tribal, and local
    organizations.
  format: http
  id: water-quality-portal.landing
  name: Water Quality Portal landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: water-quality-portal
  product_url: https://www.waterqualitydata.us/
- category: ProgrammingInterface
  description: The Water Quality Portal web services providing programmatic query access
    to stations, sampling activities, and characteristic results in standardized formats.
  format: http
  id: water-quality-portal.webservices
  name: Water Quality Portal Web Services
  original_source:
  - relation_type: prov:hadPrimarySource
    source: water-quality-portal
  product_url: https://www.waterqualitydata.us/webservices_documentation/
---
## Description

The Water Quality Portal (WQP) is a cooperative water quality data service
sponsored by the US Geological Survey, the US Environmental Protection Agency,
and the National Water Quality Monitoring Council. It integrates publicly
available monitoring data from hundreds of organizations, exposing monitoring
locations, sampling activities, and characteristic results through a
standardized web service.

SAWGraph uses WQP results as a primary source for per- and polyfluoroalkyl
substance (PFAS) occurrence in surface water and groundwater.
