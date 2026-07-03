---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.openstreetmap.org/
  label: OpenStreetMap Foundation
creation_date: '2026-07-02T00:00:00Z'
description: OpenStreetMap (OSM) is a collaborative, openly licensed geospatial database
  of the world built and maintained by a global community of contributors. It provides
  detailed vector data for infrastructure features including building footprints,
  road networks, waterways, land use, and points of interest. The data is freely available
  under the Open Database License. The Urban Flooding Open Knowledge Network (UF-OKN)
  uses OpenStreetMap building footprints and road networks as the urban-infrastructure
  features that it relates to their nearest river and to the streamflow that would
  inundate them.
domains:
- environment
- general
- information technology
homepage_url: https://www.openstreetmap.org/
id: openstreetmap
last_modified_date: '2026-07-02T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Open Database License (ODbL) 1.0
name: OpenStreetMap
products:
- category: GraphicalInterface
  description: OpenStreetMap main web map and data portal providing access to the
    collaborative geospatial database of infrastructure features worldwide.
  format: http
  id: openstreetmap.portal
  name: OpenStreetMap web portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openstreetmap
  product_url: https://www.openstreetmap.org/
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

OpenStreetMap (OSM) is a collaborative, openly licensed geospatial database of the
world built and maintained by a global community of contributors. It provides
detailed vector data for infrastructure features including building footprints, road
networks, waterways, land use, and points of interest, available under the Open
Database License.

The Urban Flooding Open Knowledge Network (UF-OKN) uses OpenStreetMap building
footprints and road networks as the urban-infrastructure features that it relates to
their nearest river and to the streamflow that would inundate them.