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
- general
homepage_url: https://www.geonames.org/
id: geonames
last_modified_date: '2026-05-20T00:00:00Z'
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
---
# GeoNames

GeoNames maintains a global gazetteer with downloadable datasets, postal code data, and web services for geographic lookup and normalization.