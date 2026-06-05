---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: sergio.consoli@ec.europa.eu
    label: Sergio Consoli
    orcid: 0000-0001-7357-5858
creation_date: '2026-04-22T00:00:00Z'
description: eKG is an epidemiological knowledge graph extracted from the World Health Organization Disease Outbreak News corpus using an ensemble of large language models and published through the European Commission Joint Research Centre Data Catalogue.
domains:
  - biomedical
  - public health
homepage_url: https://data.jrc.ec.europa.eu/dataset/89056048-7f5d-4d7c-96ad-f99d1c0f6601
id: ekg
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: eKG
products:
  - category: GraphProduct
    description: RDF/XML serialization of the eKG epidemiological knowledge graph
    format: rdfxml
    id: ekg.rdf
    name: eKG RDF
    original_source:
      - source: ekg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: who
        relation_type: prov:wasDerivedFrom
      - source: bioportal
        relation_type: prov:wasInformedBy
      - source: geonames
        relation_type: prov:wasInformedBy
    product_file_size: 3853565
    product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/ETOHA-OPEN/epidemicIE-DONs.rdf
  - category: GraphProduct
    description: Turtle serialization of the eKG epidemiological knowledge graph
    format: ttl
    id: ekg.ttl
    name: eKG TTL
    original_source:
      - source: ekg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: who
        relation_type: prov:wasDerivedFrom
      - source: bioportal
        relation_type: prov:wasInformedBy
      - source: geonames
        relation_type: prov:wasInformedBy
    product_file_size: 3874916
    product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/ETOHA-OPEN/epidemicIE-DONs.ttl
  - category: Product
    description: CSV file containing the raw epidemiological information extractions used to derive eKG
    format: csv
    id: ekg.csv
    name: eKG Raw Extractions CSV
    original_source:
      - source: ekg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: who
        relation_type: prov:wasDerivedFrom
    product_file_size: 185806
    product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/corpus_processed/SUMMARIZED/OutputAnnotatedTexts-LLMs-ENSEMBLE_whoDons.csv
  - category: ProgrammingInterface
    connection_url: https://api-vast.jrc.service.ec.europa.eu/sparql/
    description: Public SPARQL endpoint for querying eKG
    format: http
    id: ekg.sparql
    name: eKG SPARQL endpoint
    original_source:
      - source: ekg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: who
        relation_type: prov:wasDerivedFrom
      - source: bioportal
        relation_type: prov:wasInformedBy
      - source: geonames
        relation_type: prov:wasInformedBy
    product_url: https://api-vast.jrc.service.ec.europa.eu/sparql/
  - category: GraphicalInterface
    description: Virtuoso faceted browser for exploring eKG
    format: http
    id: ekg.browser
    name: eKG Faceted Browser
    original_source:
      - source: ekg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: who
        relation_type: prov:wasDerivedFrom
      - source: bioportal
        relation_type: prov:wasInformedBy
      - source: geonames
        relation_type: prov:wasInformedBy
    product_url: https://api-vast.jrc.service.ec.europa.eu/fct/
publications:
  - authors:
      - Sergio Consoli
      - Pietro Coletti
      - Peter V. Markov
      - Lia Orfei
      - Indaco Biazzo
      - Lea Schuh
      - Nicolas Stefanovitch
      - Lorenzo Bertolini
      - Mario Ceresa
      - Nikolaos I. Stilianakis
    doi: 10.1038/s41597-025-05276-2
    id: doi:10.1038/s41597-025-05276-2
    journal: Scientific Data
    preferred: true
    title: An epidemiological knowledge graph extracted from the World Health Organization's Disease Outbreak News
    year: '2025'
---

eKG is an epidemiological knowledge graph derived from the World Health Organization
Disease Outbreak News corpus and published through the European Commission Joint
Research Centre Data Catalogue.

## Automated Evaluation

- View the automated evaluation: [ekg automated evaluation](ekg_eval_automated.html)
