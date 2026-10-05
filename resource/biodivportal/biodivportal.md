---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://biodivportal.gfbio.org/feedback
  - contact_type: url
    value: https://www.nfdi4biodiversity.org/en/contact/
  label: NFDI4Biodiversity / GFBio e.V.
- category: Individual
  contact_details:
  - contact_type: email
    value: karam@infai.org
  label: Naouel Karam
creation_date: '2026-10-05T00:00:00Z'
description: BiodivPortal is an OntoPortal-based repository of ontologies and other
  semantic artefacts (vocabularies, taxonomies, thesauri) for biodiversity and environmental
  sciences. It is a core service of the German National Research Data Infrastructure
  consortium NFDI4Biodiversity,
  led by InfAI and Freie Universität Berlin. It provides search, browsing, mappings,
  an annotator, a recommender, a landscape view and a REST API. As of October 2026
  it reported 76 ontologies with about 3 million classes, including NCBITaxon, ChEBI
  and OBA. It federates with sibling OntoPortal instances such as BioPortal, AgroPortal,
  EcoPortal and EarthPortal.
domains:
- biodiversity
- organisms
- environment
- ecology
- information technology
- metadata
homepage_url: https://biodivportal.gfbio.org/
id: biodivportal
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: BiodivPortal
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing biodiversity ontologies
    and semantic artefacts, with mappings, a recommender, and a landscape view of
    the catalogue.
  format: http
  id: biodivportal.portal
  name: BiodivPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodivportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://biodivportal.gfbio.org/
- category: ProgrammingInterface
  description: OntoPortal REST API for artefact metadata, concepts, search, mappings,
    annotation, recommendation, and downloads. Requests require a BiodivPortal API
    key, available with a free account.
  format: http
  id: biodivportal.api
  name: BiodivPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodivportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://data.biodivportal.gfbio.org/
- category: ProcessProduct
  description: Text annotation service that tags free text with concepts from the
    semantic artefacts hosted in BiodivPortal, available through the portal and the
    REST API (https://data.biodivportal.gfbio.org/annotator, API key required).
  format: http
  id: biodivportal.annotator
  name: BiodivPortal Annotator
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodivportal
  product_url: https://biodivportal.gfbio.org/annotator
- category: DocumentationProduct
  description: Documentation for the BiodivPortal REST API, listing endpoints and
    parameters.
  format: http
  id: biodivportal.api-docs
  name: BiodivPortal API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodivportal
  product_url: https://data.biodivportal.gfbio.org/documentation
publications:
- authors:
  - Naouel Karam
  - Jan Fillies
  - Clement Jonquet
  - Syphax Bouazzouni
  - Felicitas Löffler
  - Franziska Zander
  - Birgitta König-Ries
  - Anton Güntsch
  - Michael Diepenbroek
  - Adrian Paschke
  doi: 10.1007/s13222-024-00474-5
  id: doi:10.1007/s13222-024-00474-5
  journal: Datenbank-Spektrum
  preferred: true
  title: 'BiodivPortal: Enabling Semantic Services for Biodiversity within the German
    National Research Data Infrastructure'
  year: '2024'
repository: https://github.com/ontoportal
warnings:
- Individual semantic artefacts have distinct licenses; review each artefact's license
  metadata before reuse.
- As of 2026-10-05 no public SPARQL endpoint was found; https://data.biodivportal.gfbio.org/sparql
  returns HTTP 401 without an API key.
---
# BiodivPortal

BiodivPortal is the NFDI4Biodiversity OntoPortal instance hosting ontologies and vocabularies for biodiversity and environmental sciences, with search, mappings, annotation, a recommender and a REST API.
