---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@geonames.org
  label: GeoNames
creation_date: '2026-02-26T00:00:00Z'
description: GeoNames is a geographical database covering all countries and providing
  over eleven million place names through downloads and web services.
domains:
- environment
- general
homepage_url: https://www.geonames.org/
id: geonames
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: GeoNames
products:
- category: DocumentationProduct
  description: GeoNames feature class and feature code vocabulary for classifying
    geographic entities.
  format: http
  id: geonames.feature-codes
  name: GeoNames Feature Codes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_url: https://www.geonames.org/export/codes.html
- category: DocumentationProduct
  description: GeoNames download and webservice overview for daily data extracts,
    postal code datasets, and usage conditions.
  format: http
  id: geonames.export
  name: GeoNames Download and Webservice Overview
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_url: https://www.geonames.org/export/
- category: ProgrammingInterface
  description: GeoNames web service overview covering search, country, postal code,
    hierarchy, and nearby-place APIs.
  format: http
  id: geonames.api
  name: GeoNames Web Services
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_url: https://www.geonames.org/export/ws-overview.html
- category: Product
  description: geonames Nodes TSV
  format: tsv
  id: obo-db-ingest.geonames.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: geonames Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 549884
  product_url: https://w3id.org/biopragmatics/resources/geonames/geonames.tsv
- category: GraphProduct
  description: RDF dump of the Open Research Knowledge Graph distributed in N-Triples
    format.
  format: ntriples
  id: orkg.dump
  name: ORKG RDF Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orkg
  - relation_type: prov:hadPrimarySource
    source: wikidata
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 642902930
  product_url: https://orkg.org/files/rdf-dumps/rdf-export-orkg.nt
- category: GraphProduct
  description: RDF/XML serialization of the eKG epidemiological knowledge graph
  format: rdfxml
  id: ekg.rdf
  name: eKG RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_file_size: 3853565
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/ETOHA-OPEN/epidemicIE-DONs.rdf
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: GraphProduct
  description: Turtle serialization of the eKG epidemiological knowledge graph
  format: ttl
  id: ekg.ttl
  name: eKG TTL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_file_size: 3874916
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/ETOHA-OPEN/epidemicIE-DONs.ttl
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: ProgrammingInterface
  connection_url: https://data.jrc.ec.europa.eu/yasgui
  description: SPARQL query interface for eKG via the JRC Data Catalogue YASGUI (the
    former dedicated endpoint at api-vast.jrc.service.ec.europa.eu/sparql/ has been
    retired)
  format: http
  id: ekg.sparql
  name: eKG SPARQL endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_url: https://data.jrc.ec.europa.eu/yasgui
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: GraphicalInterface
  description: JRC Data Catalogue dataset landing page for browsing and downloading
    eKG (the former Virtuoso faceted browser at api-vast.jrc.service.ec.europa.eu/fct/
    has been retired)
  format: http
  id: ekg.browser
  name: eKG Data Catalogue Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_url: https://data.jrc.ec.europa.eu/dataset/89056048-7f5d-4d7c-96ad-f99d1c0f6601
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: Product
  description: geonames.feature Nodes TSV
  format: tsv
  id: obo-db-ingest.geonames.feature.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: geonames.feature Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geonames.feature
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 20951
  product_url: https://w3id.org/biopragmatics/resources/geonames.feature/geonames.feature.tsv
---
# GeoNames

GeoNames maintains a global gazetteer with downloadable datasets, postal code data, and web services for geographic lookup and normalization.

The project distributes daily country and all-countries extracts, separate postal-code files, and a broad suite of place, hierarchy, nearby-feature, and country information services, all under a CC BY license with public rate limits for the free API tier.