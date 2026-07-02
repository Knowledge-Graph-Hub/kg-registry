---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.maine.gov/dep/maps-data/egad/
  label: Maine Department of Environmental Protection
creation_date: '2026-07-01T00:00:00Z'
description: The Environmental and Geographic Analysis Database (EGAD) is the Maine
  Department of Environmental Protection's database of environmental sampling and
  monitoring data. It stores site and water quality information for potential and
  actual sources of contamination, including physical, chemical, biological, and spatial
  data for surface water, groundwater, and biological sampling sites across Maine.
  EGAD includes per- and polyfluoroalkyl substance (PFAS) sampling results. SAWGraph
  uses EGAD as a primary source for state-level PFAS occurrence data in Maine.
domains:
- environment
- public health
- chemistry and biochemistry
homepage_url: https://www.maine.gov/dep/maps-data/egad/
id: maine-egad
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Maine state government public records
name: Maine EGAD (Environmental and Geographic Analysis Database)
products:
- category: GraphicalInterface
  description: Maine DEP landing page describing the Environmental and Geographic
    Analysis Database (EGAD), its scope, and data content.
  format: http
  id: maine-egad.landing
  name: Maine EGAD landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maine-egad
  product_url: https://www.maine.gov/dep/maps-data/egad/
- category: GraphicalInterface
  description: Maine DEP EGAD data request interface for obtaining environmental sampling
    data, including PFAS sample results.
  format: http
  id: maine-egad.samples
  name: Maine EGAD data request
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maine-egad
  product_url: https://www.maine.gov/dep/gis/datamaps/egad_samples/
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
---
## Description

The Environmental and Geographic Analysis Database (EGAD) is the Maine
Department of Environmental Protection's database of environmental sampling and
monitoring data. It stores site and water quality information for potential and
actual sources of contamination, including physical, chemical, biological, and
spatial data for surface water, groundwater, and biological sampling sites
across Maine, and includes per- and polyfluoroalkyl substance (PFAS) results.

SAWGraph uses EGAD as a primary source for state-level PFAS occurrence data in
Maine.