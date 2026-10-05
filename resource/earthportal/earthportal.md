---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://earthportal.eu/feedback
  - contact_type: github
    value: EarthPortal
  label: EarthPortal team (Data Terra / INRAE)
creation_date: '2026-10-05T00:00:00Z'
description: EarthPortal is an OntoPortal-based repository of ontologies and other
  semantic artefacts (thesauri, controlled vocabularies, code lists) for the Earth
  System, environmental sciences and related domains. Developed in the Data Terra
  research infrastructure and the FAIR-IMPACT project, it provides search, browsing,
  mappings, an annotator, a recommender, a SPARQL endpoint and a REST API. As of
  October 2026 its catalogue reported 92 artefacts (76 publicly listed), including
  SWEET, GCMD Keywords, GEMET, GeoNames, SOSA/SSN, EnvThes and many NERC Vocabulary
  Server collections. It federates with sibling OntoPortal instances such as AgroPortal,
  EcoPortal and BiodivPortal.
domains:
- environment
- climate
- geographic information systems
- information technology
- metadata
homepage_url: https://earthportal.eu/
id: earthportal
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: EarthPortal
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing Earth and environmental
    science ontologies and semantic artefacts, with mappings, a recommender, and a
    landscape view of the catalogue.
  format: http
  id: earthportal.portal
  name: EarthPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: earthportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://earthportal.eu/
- category: ProgrammingInterface
  description: OntoPortal REST API for artefact metadata, concepts, search, mappings,
    annotation, and downloads. Requests require an EarthPortal API key, available
    with a free account.
  format: http
  id: earthportal.api
  name: EarthPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: earthportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://data.earthportal.eu/
- category: ProgrammingInterface
  connection_url: https://sparql.earthportal.eu/sparql
  description: Virtuoso SPARQL endpoint over the RDF content of the artefacts hosted
    in EarthPortal, with a query editor in the portal.
  format: http
  id: earthportal.sparql
  name: EarthPortal SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: earthportal
  product_url: https://earthportal.eu/sparql
- category: ProcessProduct
  description: Text annotation service that tags free text with concepts from the
    semantic artefacts hosted in EarthPortal, available through the portal and the
    REST API.
  format: http
  id: earthportal.annotator
  name: EarthPortal Annotator
  original_source:
  - relation_type: prov:hadPrimarySource
    source: earthportal
  product_url: https://earthportal.eu/annotator
- category: DocumentationProduct
  description: Documentation for the EarthPortal REST API, listing endpoints and
    parameters.
  format: http
  id: earthportal.api-docs
  name: EarthPortal API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: earthportal
  product_url: https://data.earthportal.eu/documentation
- category: DocumentationProduct
  description: EarthPortal management wiki, including citation guidance, plus release
    notes in the EarthPortal documentation repository.
  format: http
  id: earthportal.wiki
  name: EarthPortal Wiki
  original_source:
  - relation_type: prov:hadPrimarySource
    source: earthportal
  product_url: https://github.com/EarthPortal/earthportal_management/wiki
publications:
- authors:
  - Christelle Pierkot
  - Guillaume Alviset
  - Anne Puissant
  - Véronique Chaffard
  - Stephane Debard
  - Charly Coussot
  doi: 10.3897/aca.8.e151393
  id: doi:10.3897/aca.8.e151393
  journal: ARPHA Conference Abstracts
  preferred: true
  title: 'Enhancing Semantic Interoperability for Land Surface Data: The Role of EarthPortal'
  year: '2025'
repository: https://github.com/EarthPortal
warnings:
- Individual semantic artefacts have distinct licenses; review each artefact's license
  metadata before reuse.
---
# EarthPortal

EarthPortal is an OntoPortal instance hosting ontologies and vocabularies for Earth System and environmental sciences, with search, mappings, annotation, a SPARQL endpoint and a REST API.
