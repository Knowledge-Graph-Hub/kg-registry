---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://waterdata.usgs.gov/nwis
  label: U.S. Geological Survey (USGS)
creation_date: '2026-07-02T00:00:00Z'
description: The National Water Information System (NWIS) is the U.S. Geological Survey's
  principal repository of water resources data for the United States, providing access
  to surface water, groundwater, and water quality data collected at monitoring sites
  and stream gages nationwide. NWIS is the authoritative source for USGS streamgage
  monitoring locations and national aquifer information. Geoconnex draws on NWIS as
  the source of record for its reference stream gage monitoring locations and USGS
  National Aquifer reference features.
domains:
- environment
- general
homepage_url: https://waterdata.usgs.gov/nwis
id: usgs-nwis
last_modified_date: '2026-07-02T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. federal government public domain
name: USGS National Water Information System (NWIS)
products:
- category: GraphicalInterface
  description: USGS Water Data for the Nation web interface to the National Water
    Information System, providing access to streamgage monitoring locations, surface
    water, groundwater, and water quality data.
  format: http
  id: usgs-nwis.landing
  name: USGS Water Data for the Nation (NWIS Web)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usgs-nwis
  product_url: https://waterdata.usgs.gov/nwis
- category: GraphProduct
  description: The Geoconnex knowledge graph, an open community-contributed RDF graph
    linking U.S. hydrologic features via persistent identifiers. It integrates USGS
    reference features (NHDPlus High Resolution hydrologic units, Watershed Boundary
    Dataset subwatersheds, reference stream gages, and national aquifers) with community-contributed
    feature registries, and is served through the Geoconnex SPARQL and Triple Pattern
    Fragments endpoints.
  format: ttl
  id: geoconnex.graph
  name: GEOCONNEX Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geoconnex
  - relation_type: prov:hadPrimarySource
    source: usgs-nhd
  - relation_type: prov:hadPrimarySource
    source: usgs-nwis
  product_url: https://github.com/internetofwater/geoconnex.us
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: epa-sdwis
  - relation_type: prov:wasInfluencedBy
    source: us-census
---
## Description

The National Water Information System (NWIS) is the U.S. Geological Survey's
principal repository of water resources data for the United States. It provides
access to surface water, groundwater, and water quality data collected at
monitoring sites and stream gages nationwide, and is the authoritative source for
USGS streamgage monitoring locations and national aquifer information.

Geoconnex draws on NWIS as the source of record for its reference stream gage
monitoring locations and USGS National Aquifer reference features.