---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://droughtmonitor.unl.edu/About/ContactUs.aspx
  label: National Drought Mitigation Center
creation_date: '2026-06-18T00:00:00Z'
description: The U.S. Drought Monitor (USDM) is a weekly map and dataset that classifies
  the location and severity of drought across the United States, its territories,
  and tribal areas. It is produced jointly by the National Drought Mitigation Center
  at the University of Nebraska-Lincoln, the U.S. Department of Agriculture, and the
  National Oceanic and Atmospheric Administration, drawing on numerous climatic and
  hydrologic indicators plus local expert input. USDM data and maps serve as an upstream
  source for KnowWhereGraph.
domains:
- environment
- agriculture
- public health
homepage_url: https://droughtmonitor.unl.edu/
id: usdm
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: U.S. Drought Monitor
products:
- category: GraphicalInterface
  description: Interactive web portal presenting the current weekly U.S. Drought Monitor
    map and severity classifications.
  format: http
  id: usdm.map
  name: U.S. Drought Monitor Current Map
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usdm
  product_url: https://droughtmonitor.unl.edu/CurrentMap.aspx
- category: Product
  description: GIS and data download portal providing USDM drought severity maps and
    tabular data for download.
  format: http
  id: usdm.data
  name: U.S. Drought Monitor GIS and Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usdm
  product_url: https://droughtmonitor.unl.edu/DmData/GISData.aspx
- category: GraphProduct
  description: KnowWhereGraph knowledge graph with 29+ billion RDF triples integrating
    30+ environmental and geospatial data layers accessible through SPARQL endpoint
  edge_count: 29000000000
  format: rdfxml
  id: knowwheregraph.graph
  name: KnowWhereGraph RDF Knowledge Graph
  node_count: 5000000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: knowwheregraph
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  - relation_type: prov:hadPrimarySource
    source: bluesky
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: cdc-svi
  - relation_type: prov:hadPrimarySource
    source: cropland-data-layer
  - relation_type: prov:hadPrimarySource
    source: epa-aqs
  - relation_type: prov:hadPrimarySource
    source: gadm
  - relation_type: prov:hadPrimarySource
    source: gnis
  - relation_type: prov:hadPrimarySource
    source: hifld
  - relation_type: prov:hadPrimarySource
    source: mtbs
  - relation_type: prov:hadPrimarySource
    source: nhpn
  - relation_type: prov:hadPrimarySource
    source: nifc
  - relation_type: prov:hadPrimarySource
    source: noaa-hms
  - relation_type: prov:hadPrimarySource
    source: noaa-ncei
  - relation_type: prov:hadPrimarySource
    source: openfema
  - relation_type: prov:hadPrimarySource
    source: reliefweb
  - relation_type: prov:hadPrimarySource
    source: ssurgo
  - relation_type: prov:hadPrimarySource
    source: us-census
  - relation_type: prov:hadPrimarySource
    source: usdm
  - relation_type: prov:hadPrimarySource
    source: usgs-comcat
  product_url: https://knowwheregraph.org/
---
## Description

The **U.S. Drought Monitor (USDM)** is a weekly map and dataset that classifies
the location and severity of drought across the United States, its territories,
and tribal areas. It is produced jointly by the **National Drought Mitigation
Center** at the University of Nebraska-Lincoln, the **U.S. Department of
Agriculture (USDA)**, and the **National Oceanic and Atmospheric Administration
(NOAA)**, integrating numerous climatic and hydrologic indicators along with
input from local experts.

USDM drought maps and underlying data serve as an upstream source for
**KnowWhereGraph**.

## Products

- **U.S. Drought Monitor Current Map** — interactive web portal showing the
  current weekly drought severity map.
- **U.S. Drought Monitor GIS and Data** — GIS and data download portal for USDM
  maps and tabular drought data.