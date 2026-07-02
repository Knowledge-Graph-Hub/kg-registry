---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  label: Sergio Baranzini
  contact_details:
  - contact_type: email
    value: sergio.baranzini@ucsf.edu
  - contact_type: github
    value: baranzini-lab
- category: Individual
  contact_details:
  - contact_type: email
    value: sergio.baranzini@ucsf.edu
  label: Sergio Baranzini
description: The spoke-genelab KG complements the spokeokn (SPOKE Open Knowledge Network)
  KG and is designed to integrate omics data from NASA’s Open Science Data Repository
  (OSDR/GeneLab), which hosts results from spaceflight experiments.
domains:
- genomics
- biological systems
homepage_url: https://github.com/BaranziniLab/spoke_genelab
id: spoke-genelab
layout: resource_detail
name: SPOKE GeneLab
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SPOKE GeneLab
  format: http
  id: spoke-genelab.sparql
  name: SPOKE GeneLab SPARQL
  original_source:
  - source: spoke-genelab
    relation_type: prov:hadPrimarySource
  - source: nasa-osdr
    relation_type: prov:hadPrimarySource
  secondary_source:
  - source: spoke-okn
    relation_type: prov:wasInfluencedBy
  product_url: https://apps.okn.us/spoke-genelab/sparql
- id: spoke-genelab.tpf
  name: SPOKE GeneLab TPF
  description: Triple Pattern Fragments endpoint for SPOKE GeneLab
  category: ProgrammingInterface
  product_url: https://apps.okn.us/ldf/spoke-genelab
  original_source:
  - source: spoke-genelab
    relation_type: prov:hadPrimarySource
  - source: nasa-osdr
    relation_type: prov:hadPrimarySource
  secondary_source:
  - source: spoke-okn
    relation_type: prov:wasInfluencedBy
repository: https://github.com/BaranziniLab/spoke_genelab
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
---
SPOKE GeneLab

## Automated Evaluation

- View the automated evaluation: [spoke-genelab automated evaluation](spoke-genelab_eval_automated.html)
