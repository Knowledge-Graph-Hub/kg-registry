---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.cdc.gov/"
    label: Centers for Disease Control and Prevention (CDC)
creation_date: '2026-06-18T00:00:00Z'
description: CDC PLACES (Population Level Analysis and Community Estimates) provides model-based small-area estimates of chronic disease risk factors, health outcomes, prevention practices, and health status measures for the United States. Estimates are produced at the county, place, census tract, and ZIP Code Tabulation Area levels, allowing local health departments and planners to assess and compare community health where direct survey data are sparse. The project is a collaboration between the CDC, the Robert Wood Johnson Foundation, and the CDC Foundation. CDC PLACES is an upstream source for KnowWhereGraph.
domains:
  - public health
  - clinical
  - phenotype
  - epidemiology
homepage_url: https://www.cdc.gov/places/
id: "cdc-places"
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: "https://www.usa.gov/government-works"
  label: U.S. Government Work (public domain)
name: CDC PLACES
products:
  - category: GraphicalInterface
    description: CDC PLACES portal providing interactive maps, data visualizations, and access to model-based small-area estimates of health measures for US counties, places, census tracts, and ZIP Code Tabulation Areas.
    format: http
    id: "cdc-places.portal"
    name: CDC PLACES Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cdc-places
    product_url: https://www.cdc.gov/places/
  - category: Product
    description: CDC PLACES datasets published on the data.cdc.gov open data platform, providing downloadable model-based estimates of health measures by county, place, census tract, and ZIP Code Tabulation Area as CSV, JSON, and other file formats accessible via the Socrata Open Data API.
    format: http
    id: "cdc-places.datasets"
    name: CDC PLACES Open Datasets
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cdc-places
    product_url: https://data.cdc.gov/browse?category=500+Cities+%26+Places
  - category: GraphProduct
    description: KnowWhereGraph knowledge graph with 29+ billion RDF triples integrating 30+ environmental and geospatial data layers accessible through SPARQL endpoint
    edge_count: 29000000000
    format: rdfxml
    id: "knowwheregraph.graph"
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
    description: The SPOKE knowledge graph containing nodes and edges from multiple
      biomedical data sources.
    format: http
    id: spoke.graph
    name: SPOKE Graph
    original_source:
    - relation_type: prov:hadPrimarySource
      source: atc
    - relation_type: prov:hadPrimarySource
      source: bgee
    - relation_type: prov:hadPrimarySource
      source: bindingdb
    - relation_type: prov:hadPrimarySource
      source: biogrid
    - relation_type: prov:hadPrimarySource
      source: bv-brc
    - relation_type: prov:hadPrimarySource
      source: cdc-places
    - relation_type: prov:hadPrimarySource
      source: chembl
    - relation_type: prov:hadPrimarySource
      source: civic
    - relation_type: prov:hadPrimarySource
      source: cl
    - relation_type: prov:hadPrimarySource
      source: clinicaltrialsgov
    - relation_type: prov:hadPrimarySource
      source: cosmic
    - relation_type: prov:hadPrimarySource
      source: dailymed
    - relation_type: prov:hadPrimarySource
      source: diseases
    - relation_type: prov:hadPrimarySource
      source: doid
    - relation_type: prov:hadPrimarySource
      source: drugbank
    - relation_type: prov:hadPrimarySource
      source: drugcentral
    - relation_type: prov:hadPrimarySource
      source: ec
    - relation_type: prov:hadPrimarySource
      source: epa-ucmr
    - relation_type: prov:hadPrimarySource
      source: fideo
    - relation_type: prov:hadPrimarySource
      source: foodb
    - relation_type: prov:hadPrimarySource
      source: foodon
    - relation_type: prov:hadPrimarySource
      source: gdsc
    - relation_type: prov:hadPrimarySource
      source: geonames
    - relation_type: prov:hadPrimarySource
      source: ghr
    - relation_type: prov:hadPrimarySource
      source: go
    - relation_type: prov:hadPrimarySource
      source: gwascatalog
    - relation_type: prov:hadPrimarySource
      source: hp
    - relation_type: prov:hadPrimarySource
      source: hpa
    - relation_type: prov:hadPrimarySource
      source: intact
    - relation_type: prov:hadPrimarySource
      source: interpro
    - relation_type: prov:hadPrimarySource
      source: kegg
    - relation_type: prov:hadPrimarySource
      source: lincs-l1000
    - relation_type: prov:hadPrimarySource
      source: mesh
    - relation_type: prov:hadPrimarySource
      source: metacyc
    - relation_type: prov:hadPrimarySource
      source: mirbase
    - relation_type: prov:hadPrimarySource
      source: mirdb
    - relation_type: prov:hadPrimarySource
      source: ncbigene
    - relation_type: prov:hadPrimarySource
      source: ncbitaxon
    - relation_type: prov:hadPrimarySource
      source: omim
    - relation_type: prov:hadPrimarySource
      source: opentargets
    - relation_type: prov:hadPrimarySource
      source: pathophenodb
    - relation_type: prov:hadPrimarySource
      source: pathwaycommons
    - relation_type: prov:hadPrimarySource
      source: pfam
    - relation_type: prov:hadPrimarySource
      source: pid
    - relation_type: prov:hadPrimarySource
      source: protcid
    - relation_type: prov:hadPrimarySource
      source: pubmed
    - relation_type: prov:hadPrimarySource
      source: reactome
    - relation_type: prov:hadPrimarySource
      source: sider
    - relation_type: prov:hadPrimarySource
      source: spoke
    - relation_type: prov:hadPrimarySource
      source: stitch
    - relation_type: prov:hadPrimarySource
      source: string
    - relation_type: prov:hadPrimarySource
      source: uberon
    - relation_type: prov:hadPrimarySource
      source: uniprot
    - relation_type: prov:hadPrimarySource
      source: who
    - relation_type: prov:hadPrimarySource
      source: wikipathways
    product_url: https://spoke.ucsf.edu/data-tools
publications:
  - authors:
      - Greenlund KJ
      - Lu H
      - Wang Y
      - Matthews KA
      - LeClercq JM
      - Lee B
      - Carlson SA
    doi: "10.5888/pcd19.210459"
    id: "https://www.ncbi.nlm.nih.gov/pubmed/35709356"
    journal: Prev Chronic Dis
    preferred: true
    title: 'PLACES: Local Data for Better Health'
    year: "2022"
---

# CDC PLACES

## Description

CDC PLACES (Population Level Analysis and Community Estimates) is a CDC project that delivers model-based small-area estimates of health measures across the United States. It covers chronic disease risk factors, health outcomes, prevention practices, disabilities, and health status, reported at the county, place, census tract, and ZIP Code Tabulation Area levels. By combining national survey data with population and geographic data, PLACES gives local decision-makers usable estimates even where direct survey samples are too small. CDC PLACES is an upstream data source for KnowWhereGraph.

## Products

- **CDC PLACES Portal** — the official PLACES web portal with interactive maps and visualizations of small-area health estimates.
- **CDC PLACES Open Datasets** — the PLACES datasets on data.cdc.gov, available for bulk download and via the Socrata Open Data API.
