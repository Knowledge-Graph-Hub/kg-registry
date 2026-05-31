---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: ICONCLASS is a comprehensive classification system for the subjects and content of images, used widely by museums, libraries, and other cultural heritage collections.
domains:
  - other
homepage_url: https://iconclass.org/
id: iconclass
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: ICONCLASS
contacts:
  - category: Organization
    label: ICONCLASS
    contact_details:
      - contact_type: email
        value: info@iconclass.org
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
---

# ICONCLASS

ICONCLASS is a controlled classification system for the subjects and content of
images, especially in museums, libraries, and broader cultural-heritage
collections. Its online browser supports subject access to image collections and
links the classification system to related documentation and services.

The owned browser product above represents the canonical entry point for the
live ICONCLASS resource. The OBO-DB-Ingest derivatives are preserved here as
propagated downstream products that transform ICONCLASS for ontology-oriented
integration workflows.
