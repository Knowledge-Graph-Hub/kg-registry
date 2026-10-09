---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.who.int/
  label: World Health Organization
creation_date: '2026-06-02T00:00:00Z'
description: The World Health Organization (WHO) is a United Nations specialized agency
  for international public health that publishes global health statistics, classifications,
  guidance, disease outbreak reports, and emergency information products.
domains:
- public health
- biomedical
- clinical
homepage_url: https://www.who.int/
id: who
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: World Health Organization
products:
- category: GraphicalInterface
  description: WHO public website for global health information, public health guidance,
    emergencies, publications, campaigns, news, and country information.
  format: http
  id: who.portal
  name: WHO Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/
- category: GraphicalInterface
  description: WHO Data Platform landing page linking WHO data portals including the
    Global Health Observatory, immunization data, GLAAS, NCD data, SRHR policy data,
    and other health data sites.
  format: http
  id: who.data-platform
  name: WHO Data Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://platform.who.int/data
- category: GraphicalInterface
  description: WHO Global Health Observatory portal for browsing global health data
    by indicators, countries, themes, featured datasets, dashboards, and publications.
  format: http
  id: who.gho
  name: WHO Global Health Observatory
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/data/gho
- category: ProgrammingInterface
  connection_url: https://ghoapi.azureedge.net/api/
  description: WHO Global Health Observatory OData API for querying WHO statistics
    and indicator data through the OData protocol.
  format: http
  id: who.gho-odata-api
  is_public: true
  name: WHO GHO OData API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/data/gho/info/gho-odata-api
- category: GraphicalInterface
  description: WHO Disease Outbreak News page providing reports on confirmed and potential
    acute public health events of concern across hazards.
  format: http
  id: who.disease-outbreak-news
  name: WHO Disease Outbreak News
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/emergencies/disease-outbreak-news
- category: ProgrammingInterface
  connection_url: https://www.who.int/api/hubs/diseaseoutbreaknews
  description: WHO Sitefinity REST API endpoint for Disease Outbreak News items, exposing
    DON identifiers, titles, dates, overview, assessment, advice, and related metadata
    as JSON.
  format: json
  id: who.disease-outbreak-news-api
  is_public: true
  name: WHO Disease Outbreak News API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/api/hubs/diseaseoutbreaknews/sfhelp
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
synonyms:
- WHO
---
# World Health Organization

The World Health Organization publishes global health information products,
statistics, classifications, and disease outbreak reports. WHO Disease Outbreak
News is also used as an upstream source for the eKG epidemiological knowledge
graph.