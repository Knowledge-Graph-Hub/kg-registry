---
activity_status: active
category: Ontology
creation_date: '2026-02-26T00:00:00Z'
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://credit.niso.org/
  label: National Information Standards Organization
description: CRediT (Contributor Roles Taxonomy) is a controlled vocabulary of contributor
  roles used to describe how individuals contributed to research and scholarly outputs.
  It provides a standardized taxonomy for representing contributions such as conceptualization,
  software, data curation, and writing.
domains:
- general
- information technology
fairsharing_id: FAIRsharing.fe4816
homepage_url: https://credit.niso.org/
id: credit
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Credit
products:
- category: DocumentationProduct
  description: Official CRediT resource hub describing the ANSI/NISO contributor-role
    taxonomy, its 14 roles, and supporting background material.
  format: http
  id: credit.spec
  name: CRediT Resource Hub
  original_source:
  - relation_type: prov:hadPrimarySource
    source: credit
  product_url: https://credit.niso.org/
- category: MappingProduct
  description: credit SSSOM
  format: sssom
  id: obo-db-ingest.credit.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: credit SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: credit
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 136
  product_url: https://w3id.org/biopragmatics/resources/credit/credit.sssom.tsv
- category: Product
  description: credit Nodes TSV
  format: tsv
  id: obo-db-ingest.credit.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: credit Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: credit
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 1046
  product_url: https://w3id.org/biopragmatics/resources/credit/credit.tsv
publications:
- authors:
  - Brand A
  - Allen L
  - Altman M
  - Hlava M
  - Scott J
  doi: 10.1087/20150211
  id: https://doi.org/10.1087/20150211
  journal: Learned Publishing
  preferred: true
  title: 'Beyond authorship: attribution, contribution, collaboration, and credit'
  year: '2015'
---
# Credit

CRediT is the Contributor Role Taxonomy maintained as a community-owned
ANSI/NISO standard for describing how individuals contribute to research and
scholarly outputs. Its fourteen roles provide a structured alternative to
leaving contribution information implicit in authorship order alone.

This page uses the CRediT resource hub as the owned entry point for the
taxonomy itself. The OBO-DB-Ingest products remain listed as downstream
propagated products that re-express the vocabulary for integration workflows.