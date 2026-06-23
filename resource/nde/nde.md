---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: asu@scripps.edu
  - contact_type: github
    value: andrewsu
  label: Andrew Su
- category: Individual
  contact_details:
  - contact_type: email
    value: plwhetzel@gmail.com
  - contact_type: github
    value: twhetzel
  label: Trish Whetzel
description: The nde (NIAID Data Ecosystem) KG contains infectious and immune-mediated
  disease datasets. These include datasets from NIAID-funded repositories as well
  as globally-relevant infectious and immune-mediated disease (IID) repositories from
  NIH and beyond. The datasets include -omics data, clinical data, epidemiological
  data, pathogen-host interaction data, flow cytometry, and imaging.
domains:
- biomedical
- immunology
homepage_url: https://data.niaid.nih.gov/
id: nde
layout: resource_detail
name: NIAID Data Ecosystem KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for NIAID Data Ecosystem KG
  format: http
  id: nde.sparql
  name: NIAID Data Ecosystem KG SPARQL
  original_source:
  - source: nde
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/nde/sparql
- id: nde.tpf
  name: NIAID Data Ecosystem KG TPF
  description: Triple Pattern Fragments endpoint for NIAID Data Ecosystem KG
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/nde
  original_source:
  - source: nde
    relation_type: prov:hadPrimarySource
taxon:
- NCBITaxon:9606
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-06-18T00:00:00Z'
---
NIAID Data Ecosystem KG

## Automated Evaluation

- View the automated evaluation: [nde automated evaluation](nde_eval_automated.html)
