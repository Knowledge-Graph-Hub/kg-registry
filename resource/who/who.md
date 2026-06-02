---
activity_status: active
category: DataSource
creation_date: '2026-06-02T00:00:00Z'
description: Stub Resource page for who. This page was automatically generated because
  it was referenced by other resources.
domains:
- stub
id: who
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Who
products:
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
  connection_url: https://api-vast.jrc.service.ec.europa.eu/sparql/
  description: Public SPARQL endpoint for querying eKG
  format: http
  id: ekg.sparql
  name: eKG SPARQL endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_url: https://api-vast.jrc.service.ec.europa.eu/sparql/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: GraphicalInterface
  description: Virtuoso faceted browser for exploring eKG
  format: http
  id: ekg.browser
  name: eKG Faceted Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_url: https://api-vast.jrc.service.ec.europa.eu/fct/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: Product
  description: CSV file containing the raw epidemiological information extractions
    used to derive eKG
  format: csv
  id: ekg.csv
  name: eKG Raw Extractions CSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_file_size: 185806
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/corpus_processed/SUMMARIZED/OutputAnnotatedTexts-LLMs-ENSEMBLE_whoDons.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
warnings:
- This is an automatically generated stub page. Please replace with accurate information
  about this resource.
---
# Who

This is an automatically generated stub page for who. Please update with proper information.