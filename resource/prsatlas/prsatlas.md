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
description: The PRS Atlas is a comprehensive resource analyzing 162 polygenic risk
  scores (PRS) derived from genome-wide association studies against 551 heritable
  traits from the UK Biobank study (N=334,398). The atlas was developed to highlight
  putative causal relationships across the human phenome using Mendelian randomization
  approaches. PRS were constructed using independent SNPs (p<5×10⁻⁵) to evaluate associations
  with complex traits, providing insights into disease susceptibility and potential
  causal risk factors. The resource includes a web application for querying and visualizing
  associations between genetic liability and diverse health outcomes.
domains:
- genomics
- biomedical
homepage_url: https://datadryad.org/dataset/doi:10.5061/dryad.h18c66b
id: prsatlas
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://spdx.org/licenses/CC0-1.0.html
  label: CC0-1.0
name: PRS Atlas
products:
- category: Product
  description: Dryad archive for PRS Atlas results, including PRS association results
    at P less than 5e-05 and P less than 5e-08 thresholds
  format: http
  id: prsatlas.dryad
  name: PRS Atlas Dryad Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  product_url: https://datadryad.org/dataset/doi:10.5061/dryad.h18c66b
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mrbase
  - relation_type: prov:wasDerivedFrom
    source: ukbiobank
- category: Product
  description: PRS Atlas results using the P less than 5e-05 polygenic risk score
    threshold, archived by Dryad
  format: txt
  id: prsatlas.results_5e05
  name: PRS Atlas Results P less than 5e-05
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  product_url: https://datadryad.org/downloads/file_stream/83029
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mrbase
  - relation_type: prov:wasDerivedFrom
    source: ukbiobank
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-13: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
- category: Product
  description: PRS Atlas results using the P less than 5e-08 polygenic risk score
    threshold, archived by Dryad
  format: txt
  id: prsatlas.results_5e08
  name: PRS Atlas Results P less than 5e-08
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  product_url: https://datadryad.org/downloads/file_stream/83030
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mrbase
  - relation_type: prov:wasDerivedFrom
    source: ukbiobank
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-13: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epigraphdb
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: vectology
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  - relation_type: prov:hadPrimarySource
    source: eqtlgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: cpic
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
publications:
- authors:
  - Tom G Richardson
  - Sean Harrison
  - Gibran Hemani
  - George Davey Smith
  doi: 10.7554/eLife.43657
  id: doi:10.7554/eLife.43657
  journal: eLife
  preferred: true
  title: An atlas of polygenic risk score associations to highlight putative causal
    relationships across the human phenome
  year: '2019'
synonyms:
- Polygenic Risk Score Atlas
taxon:
- NCBITaxon:9606
warnings:
- The original PRS Atlas web application at http://mrcieu.mrsoftware.org/PRS_atlas/
  returned HTTP 404 after HTTPS redirection on 2026-06-02; the Dryad archive remains
  available.
- The INFORES catalog did not contain an exact PRS Atlas entry on 2026-06-02, so no
  infores_id is asserted.
---
# PRS Atlas

The PRS Atlas is a comprehensive resource analyzing polygenic risk scores (PRS) for 162 traits derived from genome-wide association studies and their associations with 551 complex traits from the UK Biobank study. Developed by the MRC Integrative Epidemiology Unit at the University of Bristol, this atlas enables phenome-wide association studies using PRS to identify putative causal relationships between genetic liability and health outcomes. The original web application is no longer accessible, but a copy of the result data is archived in Dryad.