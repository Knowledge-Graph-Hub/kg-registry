---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: iisinfo@cdc.gov
  - contact_type: url
    value: https://www.cdc.gov/iis/code-sets/index.html
  label: CDC IIS Helpdesk
creation_date: '2026-02-26T00:00:00Z'
description: CVX is the vaccine administered code set maintained by the Centers for
  Disease Control and Prevention for Immunization Information Systems (IIS). It provides
  identifiers for vaccine products and historical vaccine administrations used in
  immunization records, exchange standards, and public health reporting.
domains:
- clinical
- biomedical
- public health
- clinical coding
- immunology
- vaccines
homepage_url: https://www2.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx
id: cvx
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: Vaccine Administered Code Set (CVX)
products:
- category: DocumentationProduct
  description: CDC IIS code-set hub with release notes, related code mappings, and
    additional access options for vaccine coding resources.
  format: http
  id: cvx.docs
  name: CDC Vaccine Code Sets Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cvx
  product_url: https://www.cdc.gov/iis/code-sets/index.html
- category: Product
  description: cvx Nodes TSV
  format: tsv
  id: obo-db-ingest.cvx.tsv
  name: cvx Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cvx
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 6401
  product_url: https://w3id.org/biopragmatics/resources/cvx/cvx.tsv
- category: Product
  description: cvx OBO
  format: obo
  id: obo-db-ingest.cvx.obo
  name: cvx OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: cvx
  product_file_size: 12509
  product_url: https://w3id.org/biopragmatics/resources/cvx/cvx.obo
- category: Product
  description: cvx OWL
  format: owl
  id: obo-db-ingest.cvx.owl
  name: cvx OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: cvx
  product_file_size: 16152
  product_url: https://w3id.org/biopragmatics/resources/cvx/cvx.owl
- category: Product
  description: cvx OBO Graph JSON
  format: json
  id: obo-db-ingest.cvx.json
  name: cvx OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: cvx
  product_file_size: 15268
  product_url: https://w3id.org/biopragmatics/resources/cvx/cvx.json
- category: MappingProduct
  description: cvx SSSOM
  format: sssom
  id: obo-db-ingest.cvx.sssom.tsv
  name: cvx SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: cvx
  product_file_size: 128
  product_url: https://w3id.org/biopragmatics/resources/cvx/cvx.sssom.tsv
---
# Vaccine Administered Code Set (CVX)

CVX is the CDC-maintained vaccine administered code set used in Immunization Information Systems and related health data exchange workflows.

The CDC publishes current and archived CVX releases, release notes, and crosswalks alongside the live code table, and the code system is maintained by the National Center for Immunization and Respiratory Diseases for use in IIS and HL7 immunization messaging.