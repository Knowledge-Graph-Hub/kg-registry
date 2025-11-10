---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    label: BHKLAB - Computational Oncology Lab
    contact_details:
      - contact_type: url
        value: "https://www.pmgenomics.ca/bhklab/"
      - contact_type: github
        value: "bhklab"
  - category: Organization
    label: Princess Margaret Cancer Centre
    contact_details:
      - contact_type: url
        value: "https://www.uhn.ca/PrincessMargaret"
creation_date: '2025-01-10T00:00:00Z'
description: PharmacoDB is a comprehensive integrative pharmacogenomics database that aggregates and standardizes large-scale cancer drug screening studies to enable systematic exploration and comparison of drug response phenotypes across diverse cancer cell line models. The database addresses critical challenges in pharmacogenomics research by harmonizing disparate datasets that historically used heterogeneous formats for drug sensitivity measurements and lacked standardized identifiers for cell lines and compounds. PharmacoDB integrates multiple major cancer pharmacogenomic datasets including the Cancer Cell Line Encyclopedia (CCLE), Genomics of Drug Sensitivity in Cancer (GDSC), Cancer Therapeutics Response Portal (CTRP), and others, assembling them into a unified queryable resource. The database contains dose-response data for over 56,000 compounds tested across approximately 1,758 cancer cell lines representing 30 different tissue types, with more than 6.3 million individual drug screening experiments profiling sensitivity measurements. Users can search across all integrated studies to identify instances where a specific compound or cell line has been characterized, visualize and compare dose-response curves for particular cell line-compound pairs from different datasets, and explore patterns of drug sensitivity across tissue types. PharmacoDB provides both a user-friendly web interface for interactive browsing and data visualization, as well as a RESTful JSON API for programmatic access enabling computational workflows and large-scale analyses. The database is designed to support biomarker discovery, drug repurposing investigations, and comparative pharmacogenomics studies by providing standardized access to otherwise fragmented cancer drug screening data.
domains:
  - genomics
  - pharmacology
homepage_url: https://pharmacodb.ca/
id: "pharmacodb"
last_modified_date: '2025-01-10T00:00:00Z'
layout: resource_detail
license:
  id: "https://www.gnu.org/licenses/gpl-3.0.en.html"
  label: GPL-3.0
name: PharmacoDB
products:
  - category: GraphicalInterface
    description: Primary web portal for searching and browsing cancer pharmacogenomics data across multiple integrated datasets with interactive dose-response curve visualization
    id: "pharmacodb.portal"
    name: PharmacoDB Web Application
    original_source:
      - pharmacodb
    product_url: https://pharmacodb.ca/
  - category: ProgrammingInterface
    description: RESTful JSON API providing programmatic access to cell lines, compounds, tissues, datasets, experiments, and intersections data
    id: "pharmacodb.api"
    is_public: true
    name: PharmacoDB API
    original_source:
      - pharmacodb
    product_url: http://api.pharmacodb.ca/v1/
  - category: DocumentationProduct
    description: Comprehensive user documentation covering search functionality, datasets, tissues, cell lines, experiments, genes, compounds, and biomarker discovery features
    format: http
    id: "pharmacodb.documentation"
    name: PharmacoDB Documentation
    original_source:
      - pharmacodb
    product_url: https://pharmacodb.ca/documentation
publications:
  - id: "https://doi.org/10.1093/nar/gkx911"
    title: "PharmacoDB: an integrative database for mining in vitro anticancer drug screening studies"
  - id: "https://doi.org/10.1093/bioinformatics/btv723"
    title: "PharmacoGx: an R package for analysis of large pharmacogenomic datasets"
repository: https://github.com/bhklab/PharmacoDB
synonyms:
  - PharmacoDB
  - BHKLAB PharmacoDB
---

# PharmacoDB

## Overview

PharmacoDB is an integrative cancer pharmacogenomics database that assembles and standardizes multiple large-scale in vitro drug screening studies into a unified resource, enabling researchers to mine dose-response data for compounds and cell lines across diverse cancer types.
