---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.census.gov/
  label: US Census Bureau
creation_date: '2026-06-18T00:00:00Z'
description: The United States Census Bureau is the federal agency responsible for
  producing demographic, socioeconomic, and geographic data about the people and economy
  of the United States. Its data products include the decennial Census, the American
  Community Survey (ACS), economic and business surveys, and TIGER/Line geographic
  boundary files. These datasets are widely reused for socioeconomic linkage and administrative
  geography enrichment in downstream knowledge graphs.
domains:
- public health
- general
- information technology
homepage_url: https://www.census.gov/
id: us-census
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain)
name: United States Census Bureau
products:
- category: GraphicalInterface
  description: data.census.gov is the Census Bureau's primary web platform for searching,
    exploring, and downloading data from the decennial Census, American Community
    Survey, and other Census programs.
  format: http
  id: us-census.data
  is_public: true
  name: data.census.gov
  original_source:
  - relation_type: prov:hadPrimarySource
    source: us-census
  product_url: https://data.census.gov/
- category: ProgrammingInterface
  description: The Census Data API provides programmatic access to Census Bureau datasets,
    including the decennial Census, American Community Survey, and economic surveys,
    for developers building applications and data pipelines.
  format: http
  id: us-census.api
  is_public: true
  name: Census Data API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: us-census
  product_url: https://www.census.gov/data/developers.html
- category: Product
  description: Linked neighborhood concentrated disadvantage index (CDI) dataset for
    Louisiana and Kentucky census tracts, enabling socioeconomic analysis of cancer
    incidence patterns and disparities. Demonstrates knowledge graph capability for
    third-party data integration to explain variation in cancer outcomes.
  id: cancer-registry-kg.cdi
  name: Concentrated Disadvantage Index Integration
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cancer-registry-kg
  - relation_type: prov:hadPrimarySource
    source: us-census
  - relation_type: prov:hadPrimarySource
    source: rural-urban-continuum-codes
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 405 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
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
  description: The Neighborhood Information KG (NIKG) RDF graph, a knowledge graph
    warehouse integrating neighborhood-level information such as demographics, land
    use, local incidents and injuries, and proximity to trauma centers. Built from
    census data and other neighborhood-level records, the graph is served in RDF (Turtle)
    through the NIKG SPARQL and Triple Pattern Fragments endpoints hosted on the FRINK
    / Proto-OKN infrastructure.
  format: ttl
  id: nikg.graph
  is_public: true
  name: Neighborhood Information KG RDF Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nikg
  - relation_type: prov:hadPrimarySource
    source: us-census
  product_url: https://frink.renci.org/registry/kgs/neighborhood-kg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: nij
- category: GraphProduct
  description: The Rural Resilience KG graph, a cross-domain RDF knowledge graph integrating
    health and justice data for rural resilience. It integrates justice/crime data
    from the National Incident-Based Reporting System (NIBRS), substance-use survey
    data from the National Survey on Drug Use and Health (NSDUH), mental health treatment
    providers from the National Directory of Mental Health Treatment Facilities, county
    rurality classifications from the USDA Rural-Urban Continuum Codes, and US administrative-area
    geography, served via the FRINK/Proto-OKN infrastructure.
  format: ttl
  id: ruralkg.graph
  name: Rural Resilience KG graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ruralkg
  - relation_type: prov:hadPrimarySource
    source: nibrs
  - relation_type: prov:hadPrimarySource
    source: nsduh
  - relation_type: prov:hadPrimarySource
    source: national-directory-mental-health-facilities
  - relation_type: prov:hadPrimarySource
    source: rural-urban-continuum-codes
  product_url: https://frink.renci.org/registry/kgs/rural-kg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: us-census
- category: GraphProduct
  description: The SAWGraph Spatial KG as an RDF (Turtle) graph. It contains all Level
    13 grid cells from the S2 grid together with administrative regions of levels
    1 to 3 (states, counties, and county subdivisions) and the spatial relationships
    between them for the 48 contiguous U.S. states. S2 grid cells and state/county
    geometries are taken from KnowWhereGraph, and county subdivisions are sourced
    from the US Census Bureau. The graph is served through the SAWGraph Spatial KG
    SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: spatialkg.graph
  name: SAWGraph Spatial KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spatialkg
  - relation_type: prov:wasDerivedFrom
    source: sawgraph
  product_url: https://github.com/SAWGraph/geospatial-kg
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: knowwheregraph
  - relation_type: prov:wasInfluencedBy
    source: us-census
- category: GraphProduct
  description: The SUDOKN manufacturing capability knowledge graph in RDF (Turtle),
    representing the capabilities of small and medium-sized U.S. manufacturers. Company
    profiles (manufacturing processes, materials, industries served, certifications,
    NAICS classification, and locations) are built by web-scraping raw text from manufacturer
    company websites and extracting triples with an LLM-based ETL pipeline, using
    terms from the SUDOKN application ontology (built on the Industrial Ontology Foundry
    and Basic Formal Ontology). Served through the SUDOKN SPARQL and Triple Pattern
    Fragments endpoints.
  format: ttl
  id: sudokn.graph
  name: SUDOKN Manufacturing Capability Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sudokn
  product_url: https://github.com/SUDOKN/graph
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: us-census
---
# United States Census Bureau

## Overview

The United States Census Bureau is the principal federal agency for collecting and disseminating data about the American people and economy. It conducts the constitutionally mandated decennial Census of Population and Housing, the annual American Community Survey (ACS), and numerous economic, business, and demographic surveys.

## Data Content

- **Decennial Census**: Population and housing counts collected every ten years.
- **American Community Survey (ACS)**: Ongoing survey providing detailed socioeconomic and demographic estimates.
- **TIGER/Line**: Geographic and cartographic boundary files for administrative geographies (states, counties, tracts, block groups, ZIP Code Tabulation Areas).
- **Economic surveys**: Business, industry, and economic indicator data.

## Use in Knowledge Graphs

Census data serves as an upstream source for multiple knowledge graphs, including the Cancer Registry KG (socioeconomic linkage) and KnowWhereGraph (administrative geographies and demographics).

## Access

- **data.census.gov**: Web interface for searching and downloading Census data.
- **Census Data API**: Programmatic access for developers (https://www.census.gov/data/developers.html).

## License

As a work of the U.S. federal government, Census Bureau data products are generally in the public domain (U.S. Government Work).