---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: Intellectual.PropertyServices@ama-assn.org
  - contact_type: url
    value: https://www.ama-assn.org/practice-management/cpt
  label: American Medical Association
description: Current Procedural Terminology (CPT) is a medical code set maintained
  by the American Medical Association for describing procedures and services performed
  by physicians and other healthcare professionals. It is widely used for clinical
  documentation, billing, reporting, and interoperability across healthcare systems.
domains:
- clinical
- health
fairsharing_id: FAIRsharing.wpxab1
homepage_url: https://www.ama-assn.org/practice-management/cpt
id: cpt
last_modified_date: '2026-05-19T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ama-assn.org/about/terms-use
  label: Custom (AMA Terms of Use)
name: Current Procedural Terminology
products:
- category: Product
  description: cpt Nodes TSV
  format: tsv
  id: obo-db-ingest.cpt.tsv
  name: cpt Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpt
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 4342
  product_url: https://w3id.org/biopragmatics/resources/cpt/cpt.tsv
---
# Current Procedural Terminology

Current Procedural Terminology (CPT) is the American Medical Association's maintained
code set for describing medical services and procedures. In KG-Registry it is represented
as a source terminology that also has derived OBO-DB-Ingest products for downstream
integration workflows.