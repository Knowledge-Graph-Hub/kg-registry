---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: ICONCLASS is a comprehensive classification system for the subjects and content of images, used widely by museums, libraries, and other cultural heritage collections.
domains:
  - humanities and cultural heritage
homepage_url: https://iconclass.org/
id: iconclass
last_modified_date: '2026-10-09T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: ICONCLASS
contacts:
  - category: Organization
    label: ICONCLASS
    contact_details:
      - contact_type: email
        value: info@iconclass.org
  - category: Individual
    label: Hans Brandhorst
    orcid: 0000-0001-8403-3552
  - category: Individual
    label: Etienne Posthumus
    orcid: 0000-0002-0006-7542
products:
  - category: GraphicalInterface
    description: Official ICONCLASS browser for searching and navigating the image-subject
      classification system and related resources.
    format: http
    id: iconclass.portal
    name: ICONCLASS Browser
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iconclass
    product_url: https://iconclass.org/
  - category: Product
    description: ICONCLASS data repository holding the notations, keys, and
      multilingual texts and keywords as structured UTF-8 text files, plus scripts
      to build SKOS and SQLite versions.
    format: txt
    id: iconclass.data
    name: ICONCLASS Data Files
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iconclass
    product_url: https://github.com/iconclass/data
  - category: Product
    compression: gzip
    description: List of every ICONCLASS notation, including notations expanded
      with keys.
    format: txt
    id: iconclass.all-notations
    name: ICONCLASS All Notations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iconclass
    product_file_size: 3162405
    product_url: https://raw.githubusercontent.com/iconclass/data/main/all_notations.gz
  - category: ProgrammingInterface
    description: ICONCLASS web API (OpenAPI) for search and for per-notation records
      as JSON, SKOS RDF/XML, JSON-LD, and JSKOS.
    format: http
    id: iconclass.api
    is_public: true
    name: ICONCLASS API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iconclass
    product_url: https://iconclass.org/docs
  - category: Product
    description: iconclass OBO
    format: obo
    id: obo-db-ingest.iconclass.obo
    name: iconclass OBO
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iconclass
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
    product_file_size: 650455
    product_url: https://w3id.org/biopragmatics/resources/iconclass/iconclass.obo
  - category: Product
    description: iconclass OWL
    format: owl
    id: obo-db-ingest.iconclass.owl
    name: iconclass OWL
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iconclass
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
    product_file_size: 864770
    product_url: https://w3id.org/biopragmatics/resources/iconclass/iconclass.owl
  - category: Product
    description: iconclass OBO Graph JSON
    format: json
    id: obo-db-ingest.iconclass.json
    name: iconclass OBO Graph JSON
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iconclass
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
    product_file_size: 694590
    product_url: https://w3id.org/biopragmatics/resources/iconclass/iconclass.json
  - category: Product
    description: iconclass Nodes TSV
    format: tsv
    id: obo-db-ingest.iconclass.tsv
    name: iconclass Nodes TSV
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iconclass
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
    product_file_size: 611565
    product_url: https://w3id.org/biopragmatics/resources/iconclass/iconclass.tsv
publications:
  - authors:
      - Hans Brandhorst
      - Etienne Posthumus
    doi: 10.4324/9781315298375-19
    id: doi:10.4324/9781315298375-19
    journal: The Routledge Companion to Medieval Iconography
    preferred: true
    title: Iconclass
    year: '2016'
  - authors:
      - J.P.J. (Hans) Brandhorst
    doi: 10.1017/alj.2024.14
    id: doi:10.1017/alj.2024.14
    journal: Art Libraries Journal
    title: 'Standardization at Babel - Iconclass at the next level: a laboratory for
      image research'
    year: '2024'
  - authors:
      - L.D. Couprie
    doi: 10.1017/s0307472200003436
    id: doi:10.1017/s0307472200003436
    journal: Art Libraries Journal
    title: 'Iconclass: an iconographic classification system'
    year: '1983'
repository: https://github.com/iconclass/data
---

# ICONCLASS

ICONCLASS is a controlled classification system for the subjects and content of
images, especially in museums, libraries, and broader cultural-heritage
collections. Its online browser supports subject access to image collections and
links the classification system to related documentation and services.

ICONCLASS is maintained by the Henri van de Waal Foundation. Its data files are
published under CC0 in the `iconclass/data` GitHub repository, and individual
concepts are available as linked open data (SKOS RDF/XML, JSON-LD, and JSON) by
appending a file extension to a notation URI. There is no single bulk SKOS dump.

The owned browser product above represents the canonical entry point for the
live ICONCLASS resource. The OBO-DB-Ingest derivatives are preserved here as
propagated downstream products that transform ICONCLASS for ontology-oriented
integration workflows.
