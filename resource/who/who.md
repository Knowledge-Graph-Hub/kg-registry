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
description: The World Health Organization (WHO) is a United Nations specialized agency for international public health that publishes global health statistics, classifications, guidance, disease outbreak reports, and emergency information products.
domains:
  - public health
  - health
  - clinical
  - biomedical
homepage_url: https://www.who.int/
id: who
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: World Health Organization
products:
  - category: GraphicalInterface
    description: WHO public website for global health information, public health guidance, emergencies, publications, campaigns, news, and country information.
    format: http
    id: who.portal
    name: WHO Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: who
    product_url: https://www.who.int/
  - category: GraphicalInterface
    description: WHO Data Platform landing page linking WHO data portals including the Global Health Observatory, immunization data, GLAAS, NCD data, SRHR policy data, and other health data sites.
    format: http
    id: who.data-platform
    name: WHO Data Platform
    original_source:
      - relation_type: prov:hadPrimarySource
        source: who
    product_url: https://platform.who.int/data
  - category: GraphicalInterface
    description: WHO Global Health Observatory portal for browsing global health data by indicators, countries, themes, featured datasets, dashboards, and publications.
    format: http
    id: who.gho
    name: WHO Global Health Observatory
    original_source:
      - relation_type: prov:hadPrimarySource
        source: who
    product_url: https://www.who.int/data/gho
  - category: ProgrammingInterface
    connection_url: https://ghoapi.azureedge.net/api/
    description: WHO Global Health Observatory OData API for querying WHO statistics and indicator data through the OData protocol.
    format: http
    id: who.gho-odata-api
    is_public: true
    name: WHO GHO OData API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: who
    product_url: https://www.who.int/data/gho/info/gho-odata-api
  - category: GraphicalInterface
    description: WHO Disease Outbreak News page providing reports on confirmed and potential acute public health events of concern across hazards.
    format: http
    id: who.disease-outbreak-news
    name: WHO Disease Outbreak News
    original_source:
      - relation_type: prov:hadPrimarySource
        source: who
    product_url: https://www.who.int/emergencies/disease-outbreak-news
  - category: ProgrammingInterface
    connection_url: https://www.who.int/api/hubs/diseaseoutbreaknews
    description: WHO Sitefinity REST API endpoint for Disease Outbreak News items, exposing DON identifiers, titles, dates, overview, assessment, advice, and related metadata as JSON.
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
    description: CSV file containing the raw epidemiological information extractions used to derive eKG
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
synonyms:
  - WHO
---

# World Health Organization

The World Health Organization publishes global health information products,
statistics, classifications, and disease outbreak reports. WHO Disease Outbreak
News is also used as an upstream source for the eKG epidemiological knowledge
graph.
