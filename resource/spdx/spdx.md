---
activity_status: active
category: DataModel
contacts:
  - category: Organization
    label: SPDX Project
    contact_details:
      - contact_type: url
        value: "https://spdx.dev/"
creation_date: '2026-02-26T00:00:00Z'
description: The SPDX License List is a standardized catalog of license and exception identifiers used by the SPDX specification to support consistent software, data, hardware, and documentation licensing metadata.
domains:
  - information technology
homepage_url: https://spdx.org/licenses/
id: "spdx"
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: SPDX License List
synonyms:
  - SPDX
  - System Package Data Exchange
products:
  - category: DocumentationProduct
    description: Human-readable SPDX License List with canonical identifiers, exception pages, and matching guidance.
    format: http
    id: "spdx.portal"
    name: SPDX License List Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: spdx
    product_url: https://spdx.org/licenses/
  - category: ProcessProduct
    description: Machine-readable source repository for SPDX license list data files and releases.
    format: http
    id: "spdx.license-list-data"
    name: SPDX License List Data Repository
    original_source:
      - relation_type: prov:hadPrimarySource
        source: spdx
    product_url: https://github.com/spdx/license-list-data
  - category: Product
    description: spdx OBO
    format: obo
    id: "obo-db-ingest.spdx.obo"
    name: spdx OBO
    original_source:
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
      - relation_type: prov:hadPrimarySource
        source: spdx
    product_file_size: 31617
    product_url: https://w3id.org/biopragmatics/resources/spdx/spdx.obo
  - category: Product
    description: spdx OWL
    format: owl
    id: "obo-db-ingest.spdx.owl"
    name: spdx OWL
    original_source:
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
      - relation_type: prov:hadPrimarySource
        source: spdx
    product_file_size: 37909
    product_url: https://w3id.org/biopragmatics/resources/spdx/spdx.owl
  - category: Product
    description: spdx OBO Graph JSON
    format: json
    id: "obo-db-ingest.spdx.json"
    name: spdx OBO Graph JSON
    original_source:
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
      - relation_type: prov:hadPrimarySource
        source: spdx
    product_file_size: 39391
    product_url: https://w3id.org/biopragmatics/resources/spdx/spdx.json
  - category: Product
    description: spdx Nodes TSV
    format: tsv
    id: "obo-db-ingest.spdx.tsv"
    name: spdx Nodes TSV
    original_source:
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
      - relation_type: prov:hadPrimarySource
        source: spdx
    product_file_size: 11467
    product_url: https://w3id.org/biopragmatics/resources/spdx/spdx.tsv
---

# SPDX License List

The SPDX License List provides stable short identifiers, canonical URLs, and associated license and exception metadata used in SPDX documents and related software supply chain workflows.

The list is maintained as part of the broader SPDX standard, which is now used well beyond software SBOMs across security, data, hardware, and services use cases. The public site pairs human-readable license pages with machine-readable license-list data for automation and tooling.
