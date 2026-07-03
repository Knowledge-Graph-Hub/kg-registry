---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://water.noaa.gov/about/nwm
  label: NOAA National Water Center / Office of Water Prediction
creation_date: '2026-07-02T00:00:00Z'
description: The NOAA National Water Model (NWM) is an operational hydrologic modeling
  framework run by the NOAA/NWS Office of Water Prediction that produces continuous,
  gridded streamflow and hydrologic forecasts for the continental United States. The
  NWM simulates and forecasts water in streams and rivers on the NHDPlus reach network,
  delivering analysis-and-assimilation, short-range, medium-range, and long-range
  forecasts used for flood prediction and water resource applications. The Urban Flooding
  Open Knowledge Network (UF-OKN) uses NWM streamflow forecasts as the operational,
  national-scale forecast source that drives its real-time flood-risk information.
domains:
- environment
- general
- information technology
homepage_url: https://water.noaa.gov/about/nwm
id: noaa-nwm
last_modified_date: '2026-07-02T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. federal government public domain
name: NOAA National Water Model (NWM)
products:
- category: GraphicalInterface
  description: NOAA National Water Center landing page describing the National Water
    Model, its forecast configurations, and access options.
  format: http
  id: noaa-nwm.landing
  name: NOAA National Water Model landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: noaa-nwm
  product_url: https://water.noaa.gov/about/nwm
- category: GraphProduct
  description: The UF-OKN knowledge graph, published as Linked Data (RDF/Turtle),
    that links urban infrastructure features to hydrologic forecasts so that flood
    risk can be explored as connected data. It relates OpenStreetMap building footprints
    and road networks to their nearest river (via the NHD/NHDPlus reach network) and
    to the streamflow forecasts from the NOAA National Water Model that would inundate
    them.
  format: ttl
  id: uf-okn.graph
  name: UF-OKN Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uf-okn
  - relation_type: prov:hadPrimarySource
    source: noaa-nwm
  - relation_type: prov:hadPrimarySource
    source: openstreetmap
  - relation_type: prov:hadPrimarySource
    source: usgs-nhd
  product_url: https://github.com/UFOKN/Knowledge-Graph
---
## Description

The NOAA National Water Model (NWM) is an operational hydrologic modeling
framework run by the NOAA/NWS Office of Water Prediction. It produces continuous,
gridded streamflow and hydrologic forecasts for the continental United States,
simulating water in streams and rivers on the NHDPlus reach network and delivering
analysis-and-assimilation, short-, medium-, and long-range forecasts.

The Urban Flooding Open Knowledge Network (UF-OKN) uses NWM streamflow forecasts as
the operational, national-scale forecast source that drives its real-time flood-risk
information.