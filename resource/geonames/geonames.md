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
- geographic information systems
homepage_url: https://www.geonames.org/
id: geonames
last_modified_date: '2026-09-23T00:00:00Z'
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
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 20951
  product_url: https://w3id.org/biopragmatics/resources/geonames.feature/geonames.feature.tsv
- category: Product
  description: geonames OBO
  format: obo
  id: obo-db-ingest.geonames.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: geonames OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_file_size: 1082501
  product_url: https://w3id.org/biopragmatics/resources/geonames/geonames.obo
- category: Product
  description: geonames OWL
  format: owl
  id: obo-db-ingest.geonames.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: geonames OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_file_size: 1720320
  product_url: https://w3id.org/biopragmatics/resources/geonames/geonames.owl
- category: Product
  description: geonames OBO Graph JSON
  format: json
  id: obo-db-ingest.geonames.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: geonames OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_file_size: 1475667
  product_url: https://w3id.org/biopragmatics/resources/geonames/geonames.json
- category: Product
  description: geonames.feature OBO
  format: obo
  id: obo-db-ingest.geonames.feature.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: geonames.feature OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_file_size: 22380
  product_url: https://w3id.org/biopragmatics/resources/geonames.feature/geonames.feature.obo
- category: Product
  description: geonames.feature OWL
  format: owl
  id: obo-db-ingest.geonames.feature.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: geonames.feature OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_file_size: 28833
  product_url: https://w3id.org/biopragmatics/resources/geonames.feature/geonames.feature.owl
- category: Product
  description: geonames.feature OBO Graph JSON
  format: json
  id: obo-db-ingest.geonames.feature.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: geonames.feature OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: geonames
  product_file_size: 28938
  product_url: https://w3id.org/biopragmatics/resources/geonames.feature/geonames.feature.json
- category: DocumentationProduct
  description: PDF specification of PROTON 3.0 Beta, describing the System, Top, Extent
    and Knowledge Management modules and their classes and properties.
  format: pdf
  id: proton.ontology
  is_public: true
  name: PROTON 3.0 Beta Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:wasInfluencedBy
    source: geonames
  - relation_type: prov:wasInfluencedBy
    source: freebase
  - relation_type: prov:wasInfluencedBy
    source: wordnet
  - relation_type: prov:wasInfluencedBy
    source: dolce
  product_file_size: 725192
  product_url: https://ontotext.com/documents/proton/Proton-Ver3.0B.pdf
  warnings:
  - Could not be retrieved when checked on 2026-10-04 because the Ontotext site served
    a CAPTCHA page instead of the file.
- category: OntologyProduct
  compression: gzip
  description: PROTON Top module (version 3.0) in Turtle, as mirrored on TriplyDB,
    with core entity types such as Person, Location and Organization plus temporal,
    quantitative and abstract concepts.
  format: ttl
  id: proton.top
  is_public: true
  name: PROTON Top Module
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:wasInfluencedBy
    source: geonames
  - relation_type: prov:wasInfluencedBy
    source: dolce
  product_file_size: 12036
  product_url: https://api.triplydb.com/datasets/ontotext/proton/download.ttl.gz
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
    source: bioplex
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
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
---
# GeoNames

GeoNames maintains a global gazetteer with downloadable datasets, postal code data, and web services for geographic lookup and normalization.

The project distributes daily country and all-countries extracts, separate postal-code files, and a broad suite of place, hierarchy, nearby-feature, and country information services, all under a CC BY license with public rate limits for the free API tier.