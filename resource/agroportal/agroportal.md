---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: agroportal-users@listes.inrae.fr
  - contact_type: url
    value: https://agroportal.eu/
  label: INRAE MISTEA research unit (AgroPortal team)
creation_date: '2026-10-04T00:00:00Z'
description: AgroPortal is an open repository and portal for ontologies, vocabularies,
  thesauri, and other semantic artefacts in agronomy, food, plant sciences, biodiversity,
  and related domains. Built on the BioPortal technology (now the OntoPortal software),
  it provides ontology hosting, versioning, search, browsing, metadata and FAIRness
  assessment, mappings between ontologies, text annotation, ontology recommendation,
  a REST API, and a SPARQL endpoint. It was launched at LIRMM (CNRS and University
  of Montpellier) in 2016 with Stanford University and is now maintained by INRAE.
  As of October 2026 its API listed 264 ontologies, including the Crop Ontology
  trait dictionaries.
domains:
- agriculture
- plants
- organisms
- metadata
- information technology
homepage_url: https://agroportal.eu/
id: agroportal
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: AgroPortal
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing agri-food ontologies
    and semantic artefacts, their metadata, FAIRness scores, and mappings. The former
    address https://agroportal.lirmm.fr/ redirects here.
  format: http
  id: agroportal.portal
  name: AgroPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://agroportal.eu/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: ProgrammingInterface
  description: REST API for ontologies, classes, search, mappings, metrics, annotation,
    and downloads of hosted semantic artefacts. Requests require a free API key, obtained
    by creating an AgroPortal account. The former address https://data.agroportal.lirmm.fr/
    redirects here.
  format: http
  id: agroportal.api
  name: AgroPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://data.agroportal.eu/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: ProgrammingInterface
  connection_url: https://sparql.agroportal.eu/sparql
  description: Public SPARQL endpoint (Virtuoso) over the AgroPortal triple store,
    with a query interface on the portal.
  format: http
  id: agroportal.sparql
  name: AgroPortal SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://agroportal.eu/sparql
- category: GraphicalInterface
  description: Annotator service that tags free text with terms from AgroPortal ontologies.
  format: http
  id: agroportal.annotator
  name: AgroPortal Annotator
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://agroportal.eu/annotator
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: DocumentationProduct
  description: Documentation of the AgroPortal REST API endpoints and parameters.
  format: http
  id: agroportal.api-docs
  name: AgroPortal REST API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://data.agroportal.eu/documentation
- category: DocumentationProduct
  description: Documentation for the OntoPortal software that AgroPortal runs on, covering
    installation, administration, and use of OntoPortal-based portals.
  format: http
  id: agroportal.ontoportal-docs
  name: OntoPortal Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://ontoportal.github.io/documentation/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
publications:
- authors:
  - Clément Jonquet
  - Anne Toulet
  - Elizabeth Arnaud
  - Sophie Aubin
  - Esther Dzalé Yeumo
  - Vincent Emonet
  - John Graybeal
  - Marie-Angélique Laporte
  - Mark A. Musen
  - Valeria Pesce
  - Pierre Larmande
  doi: 10.1016/j.compag.2017.10.012
  id: doi:10.1016/j.compag.2017.10.012
  journal: Computers and Electronics in Agriculture
  preferred: true
  title: 'AgroPortal: A vocabulary and ontology repository for agronomy'
  year: '2018'
repository: https://github.com/ontoportal
warnings:
- No license or terms of use for the portal content were found; individual ontologies
  carry their own licenses, so review each ontology's license metadata before reuse.
---
# AgroPortal

AgroPortal is the ontology and semantic artefact repository for agri-food and related domains, run on the OntoPortal (BioPortal-derived) stack. It offers search, browsing, mappings, annotation, a REST API, and a SPARQL endpoint.
