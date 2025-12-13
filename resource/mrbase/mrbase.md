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
last_modified_date: '2025-09-03T00:00:00Z'
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
  - mrbase
  product_url: https://www.mrbase.org/
- category: GraphicalInterface
  description: Interactive Shiny-based web application for performing two-sample Mendelian
    randomization analyses using curated GWAS summary datasets
  format: http
  id: mrbase.webapp
  is_public: true
  name: MR-Base Web Application
  original_source:
  - mrbase
  product_url: http://app.mrbase.org/
- category: GraphicalInterface
  description: Phenome-wide association study (PheWAS) web interface enabling exploration
    of SNP-trait associations and hypothesis-free MR scans
  format: http
  id: mrbase.phewas
  is_public: true
  name: MR-Base PheWAS Application
  original_source:
  - mrbase
  product_url: https://gwas.mrcieu.ac.uk/phewas/
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to harmonized GWAS summary
    statistics, LD proxy lookup, instruments, and MR result generation
  id: mrbase.api
  is_public: true
  name: MR-Base REST API
  original_source:
  - mrbase
  product_url: http://api.mrbase.org/
- category: ProgrammingInterface
  description: TwoSampleMR R package supporting data extraction, harmonization, instrument
    selection, MR analysis methods, diagnostics, and reproducible code generation
  id: mrbase.twosamplemr
  is_public: true
  name: TwoSampleMR R Package
  original_source:
  - mrbase
  product_url: https://github.com/MRCIEU/TwoSampleMR
  secondary_source:
  - mrbase
- category: ProgrammingInterface
  description: MRInstruments R package containing curated instruments (top hits) across
    multiple GWAS and QTL sources for instrument selection
  id: mrbase.mrinstruments
  is_public: true
  name: MRInstruments R Package
  original_source:
  - mrbase
  product_url: https://github.com/MRCIEU/MRInstruments
- category: DocumentationProduct
  description: TwoSampleMR package documentation with function reference, usage guides,
    and methodological notes
  format: http
  id: mrbase.twosamplemr.docs
  name: TwoSampleMR Documentation
  original_source:
  - mrbase
  product_url: https://mrcieu.github.io/TwoSampleMR/
- category: DocumentationProduct
  description: Methods paper analysis reproduction code repository for MR-Base platform
    publication
  id: mrbase.paper.reproducibility
  name: MR-Base Methods Paper Reproducibility Code
  original_source:
  - mrbase
  product_url: https://github.com/explodecomputer/mr-base-methods-paper
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
## Overview

MR-Base integrates thousands of harmonized genome-wide association study (GWAS) summary datasets with analytical tooling for systematic two-sample Mendelian randomization (2SMR). The platform supports reproducible causal inference by coupling data extraction, instrument selection, harmonization, statistical analysis, sensitivity diagnostics, and reporting across a large and evolving catalog of phenotypes.

## Components

- Web applications (main portal, analysis web app, PheWAS interface)
- REST API for programmatic dataset and association queries
- R packages (TwoSampleMR and MRInstruments) for data access, methods, and reproducible workflows
- Harmonized GWAS summary statistics, LD proxy index, and curated instrument catalogs
- Documentation and published methodology (eLife 2018 platform paper)

## Citation

Hemani G, Zheng J, Elsworth B, Wade KH, Haberland V, Baird D, Laurin C, Burgess S, Bowden J, Langdon R, Tan VY, Yarmolinsky J, Shihab HA, Timpson NJ, Evans DM, Relton C, Martin RM, Davey Smith G, Gaunt TR, Haycock PC. The MR-Base platform supports systematic causal inference across the human phenome. eLife. 2018;7:e34408. doi:10.7554/eLife.34408

## Access & Licensing

The platform paper is distributed under CC-BY 4.0. Access to certain GWAS datasets may require authentication or have embargo policies; API access governs permissions using OAuth. Users should review linked dataset source terms when reusing summary statistics.

## Contact

For scientific or data queries, contact corresponding authors (jie.zheng@bristol.ac.uk, tom.gaunt@bristol.ac.uk, philip.haycock@bristol.ac.uk) or Gibran Hemani (g.hemani@bristol.ac.uk). General platform information: https://www.mrbase.org/.