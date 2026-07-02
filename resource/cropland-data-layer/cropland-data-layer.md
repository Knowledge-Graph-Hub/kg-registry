---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php
  label: USDA National Agricultural Statistics Service
creation_date: '2026-06-18T00:00:00Z'
description: The Cropland Data Layer (CDL) is an annual, georeferenced, crop-specific
  land cover raster map covering the conterminous United States, produced by the USDA
  National Agricultural Statistics Service (NASS). It is generated from satellite
  imagery and extensive agricultural ground reference data, classifying each 30-meter
  pixel into crop types and other land cover categories. The CDL serves as an upstream
  source for KnowWhereGraph and supports agricultural monitoring, acreage estimation,
  and land use analysis.
domains:
- agriculture
- environment
- general
homepage_url: https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php
id: cropland-data-layer
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: Cropland Data Layer
products:
- category: GraphicalInterface
  description: CroplandCROS web mapping application for interactive viewing, querying,
    and exporting Cropland Data Layer crop-type raster data.
  format: http
  id: cropland-data-layer.croplandcros
  name: CroplandCROS Viewer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cropland-data-layer
  product_url: https://croplandcros.scinet.usda.gov/
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
publications:
- id: doi:10.1080/10106049.2011.562309
  title: 'Monitoring US agriculture: the US Department of Agriculture, National Agricultural
    Statistics Service, Cropland Data Layer Program'
---
The Cropland Data Layer (CDL) is an annual crop-specific land cover product for the
conterminous United States, produced by the USDA National Agricultural Statistics
Service (NASS). Built from satellite imagery combined with ground reference data,
it provides 30-meter resolution classifications of crop types and other land cover.
The CDL is freely available as a US federal government public domain dataset and is
used as an upstream data source for KnowWhereGraph.