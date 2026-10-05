---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bioportal.lirmm.fr/about
  label: LIRMM (Laboratoire d'Informatique, de Robotique et de Microélectronique de
    Montpellier), University of Montpellier and CNRS
creation_date: '2026-10-05T00:00:00Z'
description: SIFR BioPortal is an open repository of French biomedical ontologies
  and terminologies run by LIRMM in Montpellier. It is built on the OntoPortal technology
  (the software behind NCBO BioPortal) and hosts French-language and French-translated
  vocabularies such as the French versions of MeSH, ATC, MedDRA, SNOMED and ICD-10
  (CIM-10), CCAM, ORDO and other national terminologies, with search, browsing, mappings,
  a REST API, a SPARQL endpoint, and the SIFR Annotator for semantic annotation of
  French biomedical text and clinical notes. As of October 2026 it listed 41 ontologies
  with about 889,000 classes. It was developed within the French ANR SIFR project
  and the EU H2020-MSCA SIFRm project.
domains:
- biomedical
- clinical
- clinical coding
- information technology
- metadata
- literature
- natural language processing
homepage_url: https://bioportal.lirmm.fr/
id: sifr-bioportal
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: SIFR BioPortal
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing French biomedical
    ontologies and terminologies and the mappings between them, with recommender and
    landscape views.
  format: http
  id: sifr-bioportal.portal
  name: SIFR BioPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sifr-bioportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://bioportal.lirmm.fr/
- category: ProgrammingInterface
  description: OntoPortal REST API for ontologies, classes, search, mappings, metrics,
    submissions, and the annotator. Endpoints require a free SIFR BioPortal API key.
  format: http
  id: sifr-bioportal.api
  name: SIFR BioPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sifr-bioportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://data.bioportal.lirmm.fr/
- category: ProcessProduct
  description: SIFR Annotator, a semantic annotation service for French biomedical
    text and clinical notes that tags text with concepts from the ontologies hosted
    in SIFR BioPortal. It ports the NCBO Annotator to French, adding lemmatization,
    negation, experiencer and temporality detection, and scoring. Available as a web
    form and through the REST API (/annotator, API key required).
  format: http
  id: sifr-bioportal.annotator
  name: SIFR Annotator
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sifr-bioportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://bioportal.lirmm.fr/annotator
- category: ProgrammingInterface
  connection_url: https://sparql.bioportal.lirmm.fr/sparql/
  description: SPARQL endpoint over the ontology content stored in SIFR BioPortal,
    with a test query form.
  format: http
  id: sifr-bioportal.sparql
  name: SIFR BioPortal SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sifr-bioportal
  product_url: https://sparql.bioportal.lirmm.fr/test/
- category: DocumentationProduct
  description: Documentation of the SIFR BioPortal REST API, listing resources, parameters,
    and response formats.
  format: http
  id: sifr-bioportal.api.docs
  name: SIFR BioPortal REST API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sifr-bioportal
  product_url: https://data.bioportal.lirmm.fr/documentation
publications:
- authors:
  - Andon Tchechmedjiev
  - Amine Abdaoui
  - Vincent Emonet
  - Stella Zevio
  - Clement Jonquet
  doi: 10.1186/s12859-018-2429-2
  id: doi:10.1186/s12859-018-2429-2
  journal: BMC Bioinformatics
  preferred: true
  title: 'SIFR annotator: ontology-based semantic annotation of French biomedical
    text and clinical notes'
  year: '2018'
repository: https://github.com/sifrproject
warnings:
- No overall license is stated for SIFR BioPortal content; individual terminologies
  carry their own licenses and terms (several, such as MedDRA and SNOMED, are restricted).
---
# SIFR BioPortal

SIFR BioPortal is LIRMM's OntoPortal-based repository of French biomedical ontologies and terminologies, with a French-language semantic annotator (SIFR Annotator), REST API, and SPARQL endpoint.
