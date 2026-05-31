---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: "iisinfo@cdc.gov"
      - contact_type: url
        value: "https://www.cdc.gov/iis/code-sets/index.html"
    label: CDC IIS Helpdesk
description: CVX is the vaccine administered code set maintained by the Centers for Disease Control and Prevention for Immunization Information Systems (IIS). It provides identifiers for vaccine products and historical vaccine administrations used in immunization records, exchange standards, and public health reporting.
domains:
  - clinical
  - health
  - public health
homepage_url: https://www2.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx
id: "cvx"
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: Vaccine Administered Code Set (CVX)
products:
  - category: DocumentationProduct
    description: CDC IIS code-set hub with release notes, related code mappings, and additional access options for vaccine coding resources.
    format: http
    id: "cvx.docs"
    name: CDC Vaccine Code Sets Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cvx
    product_url: https://www.cdc.gov/iis/code-sets/index.html
  - category: Product
    description: cvx Nodes TSV
    format: tsv
    id: "obo-db-ingest.cvx.tsv"
    name: cvx Nodes TSV
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cvx
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
    product_file_size: 6401
    product_url: https://w3id.org/biopragmatics/resources/cvx/cvx.tsv
---

# Vaccine Administered Code Set (CVX)

CVX is the CDC-maintained vaccine administered code set used in Immunization Information Systems and related health data exchange workflows.

The CDC publishes current and archived CVX releases, release notes, and crosswalks alongside the live code table, and the code system is maintained by the National Center for Immunization and Respiratory Diseases for use in IIS and HL7 immunization messaging.
