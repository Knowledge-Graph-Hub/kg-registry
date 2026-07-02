---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.usgs.gov/national-hydrography/national-hydrography-dataset
  label: U.S. Geological Survey (USGS)
creation_date: '2026-07-01T00:00:00Z'
description: The National Hydrography Dataset (NHD) is the U.S. Geological Survey's
  authoritative geospatial representation of the surface water features of the United
  States, including rivers, streams, canals, lakes, ponds, and other waterbodies.
  The associated NHDPlus products add value with flow direction, network connectivity
  (NHDFlowline), waterbody features (NHDWaterbody), and catchment attributes. SAWGraph
  uses NHD and NHDPlus data as a geospatial reference source for modeling surface
  water features and the flowlines that connect them, supporting spatial context for
  PFAS observations.
domains:
- environment
- general
homepage_url: https://www.usgs.gov/national-hydrography/national-hydrography-dataset
id: usgs-nhd
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. federal government public domain
name: USGS National Hydrography Dataset (NHD)
products:
- category: GraphicalInterface
  description: USGS landing page for the National Hydrography Dataset describing the
    surface water feature data and access options.
  format: http
  id: usgs-nhd.landing
  name: USGS National Hydrography Dataset landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usgs-nhd
  product_url: https://www.usgs.gov/national-hydrography/national-hydrography-dataset
- category: GraphicalInterface
  description: USGS landing page for NHDPlus High Resolution, providing value-added
    flow, network connectivity, and catchment attributes built on the NHD.
  format: http
  id: usgs-nhd.nhdplus
  name: USGS NHDPlus High Resolution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usgs-nhd
  product_url: https://www.usgs.gov/national-hydrography/nhdplus-high-resolution
---
## Description

The National Hydrography Dataset (NHD) is the U.S. Geological Survey's
authoritative geospatial representation of the surface water features of the
United States, including rivers, streams, canals, lakes, ponds, and other
waterbodies. The associated NHDPlus products add flow direction, network
connectivity (NHDFlowline), waterbody features (NHDWaterbody), and catchment
attributes.

SAWGraph uses NHD and NHDPlus as a geospatial reference source for modeling
surface water features and the flowlines that connect them, providing spatial
context for PFAS observations.
