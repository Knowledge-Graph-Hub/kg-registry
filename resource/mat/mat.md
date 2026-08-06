---
id: mat
name: Minimal anatomical terminology
description: Description unavailable.
activity_status: inactive
license:
  id: ''
  label: Not specified
collection:
- obo-foundry
layout: resource_detail
category: Ontology
creation_date: '2025-09-29T00:00:00Z'
last_modified_date: '2026-08-06T00:00:00Z'
domains:
- anatomy and development
contacts:
- category: Individual
  label: Jonathan Bard
  contact_details:
  - contact_type: email
    value: j.bard@ed.ac.uk
products:
- id: mat.kg-bioportal
  name: MAT KGX graph (KG-Bioportal)
  category: GraphProduct
  description: KGX TSV transform of Minimal Anatomical Terminology (MAT), produced
    by KG-Bioportal from the BioPortal submission. The archive contains MAT_nodes.tsv
    and MAT_edges.tsv.
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/MAT.tar.gz
  format: kgx
  compression: targz
  original_source:
  - source: mat
    relation_type: prov:hadPrimarySource
  node_count: 2204
  edge_count: 3954
  latest_version: '1.1'
publications: []
---
## Description

Minimal set of terms for anatomy.

## Contacts

- Jonathan Bard (j.bard@ed.ac.uk)

**Domains**: anatomy and development

---

*This resource was automatically synchronized from the OBO Foundry registry.*
