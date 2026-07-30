---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: Intellectual.PropertyServices@ama-assn.org
  - contact_type: url
    value: https://www.ama-assn.org/practice-management/cpt
  label: American Medical Association
creation_date: '2026-02-26T00:00:00Z'
description: Current Procedural Terminology (CPT) is a medical code set maintained
  by the American Medical Association for describing procedures and services performed
  by physicians and other healthcare professionals. It is widely used for clinical
  documentation, billing, reporting, and interoperability across healthcare systems.
domains:
- clinical
- biomedical
fairsharing_id: FAIRsharing.wpxab1
homepage_url: https://www.ama-assn.org/practice-management/cpt
id: cpt
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ama-assn.org/about/terms-use
  label: Custom (AMA Terms of Use)
name: Current Procedural Terminology
products:
- category: DocumentationProduct
  description: Official American Medical Association CPT overview and guidance page
    for the Current Procedural Terminology code set.
  format: http
  id: cpt.spec
  name: CPT Overview and Guidance
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpt
  product_url: https://www.ama-assn.org/practice-management/cpt
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
- category: Product
  description: The proprietary clinical knowledge graph content itself, comprising
    IMO clinical interface terminology concepts, hierarchies, clinical relationships,
    and cross-maps to standard code systems including ICD-10-CM, ICD-10, SNOMED CT,
    CPT, LOINC, and RxNorm. Delivered under commercial license through the IMO Health
    APIs, EHR integrations, or bulk data agreements.
  format: http
  id: imo-knowledge-graph.data
  name: IMO Health Knowledge Graph Content
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://www.imohealth.com/knowledge-graph/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cpt
  - relation_type: prov:wasDerivedFrom
    source: icd10
  - relation_type: prov:wasDerivedFrom
    source: icd10cm
  - relation_type: prov:wasDerivedFrom
    source: loinc
  - relation_type: prov:wasDerivedFrom
    source: rxnorm
  - relation_type: prov:wasDerivedFrom
    source: snomedct
  warnings:
  - The knowledge graph content is proprietary and is not available as a public bulk
    download. Access requires a commercial agreement with IMO Health.
---
# Current Procedural Terminology

Current Procedural Terminology (CPT) is the American Medical Association's maintained
code set for describing medical services and procedures. In KG-Registry it is represented
as a source terminology used across clinical documentation, reimbursement,
quality reporting, and operational healthcare workflows.

This page uses the AMA CPT overview as the owned documentation product for the
resource itself. The derived OBO-DB-Ingest TSV remains listed as a propagated
downstream product because it re-expresses CPT content for integration workflows.