---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.mrbase.org/
  label: MR-Base Team (MRC Integrative Epidemiology Unit, University of Bristol)
creation_date: '2025-09-03T00:00:00Z'
description: MR-Base is a platform that integrates a large database of harmonized
  GWAS summary association datasets with analytical tools (web apps and R packages)
  to support systematic two-sample Mendelian randomization (2SMR) and phenome-wide
  causal inference across the human phenome.
domains:
- health
- biomedical
- genomics
- investigations
homepage_url: https://www.mrbase.org/
id: mrbase
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: MR-Base
products:
- category: GraphicalInterface
  description: Web home and informational landing page for MR-Base platform components
    and publications
  format: http
  id: mrbase.home
  name: MR-Base Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://www.mrbase.org/
  warnings:
  - The legacy MR-Base homepage redirected to an HTTPS endpoint with a certificate
    mismatch for www.mrbase.org when checked on 2026-06-02.
- category: GraphicalInterface
  description: Interactive Shiny-based web application for performing two-sample Mendelian
    randomization analyses using curated GWAS summary datasets
  format: http
  id: mrbase.webapp
  is_public: true
  name: MR-Base Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: http://app.mrbase.org/
  warnings:
  - The legacy MR-Base web application timed out when checked on 2026-06-02.
- category: GraphicalInterface
  description: Phenome-wide association study (PheWAS) web interface enabling exploration
    of SNP-trait associations and hypothesis-free MR scans
  format: http
  id: mrbase.phewas
  is_public: true
  name: MR-Base PheWAS Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://gwas.mrcieu.ac.uk/phewas/
- category: GraphicalInterface
  description: IEU OpenGWAS browser for exploring the harmonized GWAS dataset catalog
    now used by MR-Base-related tooling
  format: http
  id: opengwas.portal
  is_public: true
  name: IEU OpenGWAS Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opengwas
  product_url: https://opengwas.io/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: mrbase
- category: ProgrammingInterface
  description: REST API for programmatic access to IEU OpenGWAS study information,
    top hits, association records, LD proxies, and related MR-Base analysis inputs
  format: http
  id: opengwas.api
  is_public: true
  name: IEU OpenGWAS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opengwas
  product_url: https://api.opengwas.io/api/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: mrbase
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to harmonized GWAS summary
    statistics, LD proxy lookup, instruments, and MR result generation
  id: mrbase.api
  is_public: true
  name: MR-Base REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: http://api.mrbase.org/
  warnings:
  - The legacy MR-Base API returned HTTP 503 when checked on 2026-06-02; current OpenGWAS
    API access is represented by opengwas.api.
- category: ProgrammingInterface
  description: TwoSampleMR R package supporting data extraction, harmonization, instrument
    selection, MR analysis methods, diagnostics, and reproducible code generation
  id: mrbase.twosamplemr
  is_public: true
  name: TwoSampleMR R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://github.com/MRCIEU/TwoSampleMR
  secondary_source:
  - relation_type: prov:used
    source: opengwas
- category: ProgrammingInterface
  description: MRInstruments R package containing curated instruments (top hits) across
    multiple GWAS and QTL sources for instrument selection
  id: mrbase.mrinstruments
  is_public: true
  name: MRInstruments R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://github.com/MRCIEU/MRInstruments
- category: DocumentationProduct
  description: TwoSampleMR package documentation with function reference, usage guides,
    and methodological notes
  format: http
  id: mrbase.twosamplemr.docs
  name: TwoSampleMR Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://mrcieu.github.io/TwoSampleMR/
  secondary_source:
  - relation_type: prov:used
    source: opengwas
- category: DocumentationProduct
  description: Methods paper analysis reproduction code repository for MR-Base platform
    publication
  id: mrbase.paper.reproducibility
  name: MR-Base Methods Paper Reproducibility Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://github.com/explodecomputer/mr-base-methods-paper
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
  - 'File was not able to be retrieved when checked on 2026-06-02: HTTP 403 error
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
  - 'File was not able to be retrieved when checked on 2026-06-02: HTTP 403 error
    when accessing file'
publications:
- authors:
  - Gibran Hemani
  - Jie Zheng
  - Benjamin Elsworth
  - Kaitlin H. Wade
  - Valeriia Haberland
  - Denis Baird
  - Charles Laurin
  - Stephen Burgess
  - Jack Bowden
  - Rebecca Langdon
  - Vanessa Y. Tan
  - James Yarmolinsky
  - Hashem A. Shihab
  - Nicholas J. Timpson
  - David M. Evans
  - Caroline L. Relton
  - Richard M. Martin
  - George Davey Smith
  - Tom R. Gaunt
  - Philip C. Haycock
  category: Publication
  doi: 10.7554/eLife.34408
  id: doi:10.7554/eLife.34408
  journal: eLife
  preferred: true
  title: The MR-Base platform supports systematic causal inference across the human
    phenome
  year: '2018'
taxon:
- NCBITaxon:9606
---
## Overview

MR-Base integrates thousands of harmonized genome-wide association study (GWAS) summary datasets with analytical tooling for systematic two-sample Mendelian randomization (2SMR). The platform supports reproducible causal inference by coupling data extraction, instrument selection, harmonization, statistical analysis, sensitivity diagnostics, and reporting across a large and evolving catalog of phenotypes.

## Components

- Web applications (main portal, analysis web app, PheWAS interface)
- REST API access for programmatic dataset and association queries, with current
  OpenGWAS API access represented separately from the legacy MR-Base API endpoint
- R packages (TwoSampleMR and MRInstruments) for data access, methods, and reproducible workflows
- Harmonized GWAS summary statistics, LD proxy index, and curated instrument catalogs
- Documentation and published methodology (eLife 2018 platform paper)

## Citation

Hemani G, Zheng J, Elsworth B, Wade KH, Haberland V, Baird D, Laurin C, Burgess S, Bowden J, Langdon R, Tan VY, Yarmolinsky J, Shihab HA, Timpson NJ, Evans DM, Relton C, Martin RM, Davey Smith G, Gaunt TR, Haycock PC. The MR-Base platform supports systematic causal inference across the human phenome. eLife. 2018;7:e34408. doi:10.7554/eLife.34408

## Access & Licensing

The platform paper is distributed under CC-BY 4.0. Access to certain GWAS datasets may require authentication or have embargo policies; API access governs permissions using OAuth. Users should review linked dataset source terms when reusing summary statistics.

## Contact

For scientific or data queries, contact corresponding authors (jie.zheng@bristol.ac.uk, tom.gaunt@bristol.ac.uk, philip.haycock@bristol.ac.uk) or Gibran Hemani (g.hemani@bristol.ac.uk). General platform information: https://www.mrbase.org/.