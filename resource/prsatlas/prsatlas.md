---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.bristol.ac.uk/integrative-epidemiology-unit/
  label: MRC Integrative Epidemiology Unit, University of Bristol
creation_date: '2025-12-03T00:00:00Z'
description: "The PRS Atlas is a comprehensive resource analyzing 162 polygenic risk\
  \ scores (PRS) derived from genome-wide association studies against 551 heritable\
  \ traits from the UK Biobank study (N=334,398). The atlas was developed to highlight\
  \ putative causal relationships across the human phenome using Mendelian randomization\
  \ approaches. PRS were constructed using independent SNPs (p<5\xD710\u207B\u2075\
  ) to evaluate associations with complex traits, providing insights into disease\
  \ susceptibility and potential causal risk factors. The resource includes a web\
  \ application for querying and visualizing associations between genetic liability\
  \ and diverse health outcomes."
domains:
- genomics
- translational
- biomedical
homepage_url: http://mrcieu.mrsoftware.org/PRS_atlas/
id: prsatlas
infores_id: prsatlas
last_modified_date: '2025-12-03T00:00:00Z'
layout: resource_detail
name: PRS Atlas
publications:
- id: doi:10.7554/eLife.43657
  title: An atlas of polygenic risk score associations to highlight putative causal
    relationships across the human phenome
  authors:
  - Tom G Richardson
  - Sean Harrison
  - Gibran Hemani
  - George Davey Smith
  journal: eLife
  year: '2019'
  doi: 10.7554/eLife.43657
  preferred: true
synonyms:
- Polygenic Risk Score Atlas
warnings:
- The web application at http://mrcieu.mrsoftware.org/PRS_atlas/ may no longer be
  accessible
products:
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - epigraphdb
  - kg-monarch
  - vectology
  - ukbiobank
  - prsatlas
  - eqtlgen
  - mondo
  - gtex
  - ensembl
  - cpic
  - opentargets
  - efo
  - semmeddb
  - intact
  - string
  - reactome
  - mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
  secondary_source:
  - epigraphdb
taxon:
- NCBITaxon:9606
---

# PRS Atlas

The PRS Atlas is a comprehensive resource analyzing polygenic risk scores (PRS) for 162 traits derived from genome-wide association studies and their associations with 551 complex traits from the UK Biobank study. Developed by the MRC Integrative Epidemiology Unit at the University of Bristol, this atlas enables phenome-wide association studies using PRS to identify putative causal relationships between genetic liability and health outcomes. The resource was designed to facilitate causal inference through Mendelian randomization approaches and includes a web application for querying results, though the application may no longer be accessible.
