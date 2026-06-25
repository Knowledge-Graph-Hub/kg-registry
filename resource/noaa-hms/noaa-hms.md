---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ospo.noaa.gov/products/land/hms.html
  label: National Oceanic and Atmospheric Administration (NOAA)
creation_date: '2026-06-18T00:00:00Z'
description: The NOAA Hazard Mapping System (HMS) Fire and Smoke Product is a satellite-derived
  analysis of fire locations and smoke plumes over North America, produced operationally
  by NOAA's National Environmental Satellite, Data, and Information Service (NESDIS)
  Office of Satellite and Product Operations (OSPO). Trained analysts integrate automated
  fire detections from geostationary (GOES) and polar-orbiting satellites with imagery
  to manually quality-control fire points and to delineate smoke plumes by density.
  The daily products are distributed as fire point and smoke polygon datasets in Shapefile
  and KML formats. HMS data are used to monitor wildfire activity and air-quality-relevant
  smoke transport across the United States, Canada, and Mexico.
domains:
- environment
- public health
homepage_url: https://www.ospo.noaa.gov/products/land/hms.html
id: noaa-hms
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain)
name: NOAA Hazard Mapping System Fire and Smoke Product
products:
- category: DataSource
  description: Daily HMS smoke plume polygons over North America, classified by smoke
    density, provided as Shapefile and KML files via NOAA NESDIS data distribution.
  format: mixed
  id: noaa-hms.smoke-polygons
  is_public: true
  name: HMS Smoke Polygons
  original_source:
  - relation_type: prov:hadPrimarySource
    source: noaa-hms
  product_url: https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/
- category: DataSource
  description: Daily HMS analyst-reviewed fire detection points over North America
    derived from geostationary and polar-orbiting satellite observations, provided
    as Shapefile and KML files via NOAA NESDIS data distribution.
  format: mixed
  id: noaa-hms.fire-points
  is_public: true
  name: HMS Fire Points
  original_source:
  - relation_type: prov:hadPrimarySource
    source: noaa-hms
  product_url: https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Fire_Points/
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
The NOAA Hazard Mapping System (HMS) Fire and Smoke Product is an operational, satellite-derived analysis of fire locations and smoke plumes covering North America. It is produced by trained analysts at NOAA/NESDIS Office of Satellite and Product Operations (OSPO), who combine automated fire detections from GOES geostationary and polar-orbiting satellites with satellite imagery to manually verify fire points and to outline smoke plumes by density.

Outputs are released daily as fire point and smoke polygon datasets in Shapefile and KML formats and are widely reused for wildfire monitoring and smoke/air-quality applications. HMS serves as an upstream data source for KnowWhereGraph.