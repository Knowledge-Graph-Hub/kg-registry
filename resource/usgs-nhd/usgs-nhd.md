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
- category: GraphProduct
  description: The SAWGraph PFAS knowledge graph, integrating PFAS observations and
    releases with the samples, geospatial features, environmental media, and chemical
    substances they describe. The RDF (Turtle) graph is constructed from federal and
    state PFAS datasets and geospatial reference data, and is served through the SAWGraph
    SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: sawgraph.graph
  name: SAWGraph PFAS Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sawgraph
  - relation_type: prov:hadPrimarySource
    source: epa-sdwis
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: water-quality-portal
  - relation_type: prov:hadPrimarySource
    source: epa-ghg
  - relation_type: prov:hadPrimarySource
    source: epa-frs
  - relation_type: prov:hadPrimarySource
    source: maine-egad
  product_url: https://github.com/SAWGraph/pfas-kg
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: epa-echo
  - relation_type: prov:wasInfluencedBy
    source: usgs-nhd
  - relation_type: prov:wasInfluencedBy
    source: us-census
  - relation_type: prov:wasInfluencedBy
    source: knowwheregraph
  - relation_type: prov:wasInfluencedBy
    source: ssurgo
  - relation_type: prov:wasInfluencedBy
    source: cropland-data-layer
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
- category: GraphProduct
  description: The SAWGraph Hydrology knowledge graph, describing surface water bodies
    (lakes, rivers, wetlands), the flowlines that connect them, and groundwater features
    (aquifers, wells, springs) together with their locations. Surface water bodies
    and flowlines are modeled from USGS NHDPlus data (NHDWaterbody and NHDFlowline);
    groundwater features are drawn primarily from individual state geological surveys
    (for example, the Maine Geological Survey). The RDF (Turtle) graph is served through
    the SAWGraph Hydrology KG SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: hydrologykg.graph
  name: SAWGraph Hydrology Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hydrologykg
  - relation_type: prov:wasDerivedFrom
    source: sawgraph
  - relation_type: prov:hadPrimarySource
    source: usgs-nhd
  product_url: https://github.com/SAWGraph/water-kg
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

The National Hydrography Dataset (NHD) is the U.S. Geological Survey's
authoritative geospatial representation of the surface water features of the
United States, including rivers, streams, canals, lakes, ponds, and other
waterbodies. The associated NHDPlus products add flow direction, network
connectivity (NHDFlowline), waterbody features (NHDWaterbody), and catchment
attributes.

SAWGraph uses NHD and NHDPlus as a geospatial reference source for modeling
surface water features and the flowlines that connect them, providing spatial
context for PFAS observations.