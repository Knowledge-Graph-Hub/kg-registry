---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/frs
  label: US Environmental Protection Agency
creation_date: '2026-07-01T00:00:00Z'
description: The Facility Registry Service (FRS) is the US Environmental Protection
  Agency's centrally managed database that identifies facilities, sites, and places
  subject to environmental regulation or of environmental interest. Each facility
  is assigned a unique FRS identifier and described with location, industry classification
  (NAICS and SIC codes), and links to EPA program records. SAWGraph uses FRS as a
  primary source for the facilities associated with PFAS releases and for their industry
  classifications, integrated through the SAWGraph Facilities and Industries Ontology
  (FIO).
domains:
- environment
- general
homepage_url: https://www.epa.gov/frs
id: epa-frs
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: EPA Facility Registry Service (FRS)
products:
- category: GraphicalInterface
  description: EPA landing page for the Facility Registry Service describing the centrally
    managed database of regulated facilities and how to access it.
  format: http
  id: epa-frs.landing
  name: EPA FRS landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-frs
  product_url: https://www.epa.gov/frs
- category: ProgrammingInterface
  description: EPA page describing FRS geospatial data downloads and services for
    facility location and identification records.
  format: http
  id: epa-frs.data
  name: EPA FRS data downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-frs
  product_url: https://www.epa.gov/frs/geospatial-data-download-service
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

The Facility Registry Service (FRS) is the US Environmental Protection Agency's
centrally managed database identifying facilities, sites, and places subject to
environmental regulation or of environmental interest. Each facility carries a
unique FRS identifier and is described with location, industry classification
(NAICS and SIC), and links to EPA program records.

SAWGraph uses FRS as a primary source for the facilities associated with PFAS
releases and their industry classifications, integrated through the SAWGraph
Facilities and Industries Ontology (FIO).