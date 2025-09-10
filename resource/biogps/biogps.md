---
activity_status: active
category: Aggregator
creation_date: '2025-08-12T00:00:00Z'
contacts:
  - category: Organization
    label: BioGPS / The Scripps Research Institute
    contact_details:
      - contact_type: url
        value: "http://biogps.org/about/"
description: BioGPS is an extensible and customizable gene annotation portal that aggregates gene-centric data (expression profiles, functional annotations, pathways, interactions, ontologies) from numerous external resources using a community-driven plugin system. It enables interactive expression visualization across tissues/cell types and provides programmatic and bulk access to underlying annotation tables.
domains:
  - genomics
  - biomedical
  - biological systems
homepage_url: http://biogps.org/
id: biogps
last_modified_date: '2025-09-10T00:00:00Z'
layout: resource_detail
name: BioGPS
publications:
  - id: doi:10.1186/gb-2009-10-11-r130
    title: "BioGPS: an extensible and customizable portal for querying and organizing gene annotation resources"
    year: '2009'
    journal: Genome Biology
    doi: 10.1186/gb-2009-10-11-r130
    authors:
      - Wu C
      - Orozco C
      - Boyer J
      - Leglise M
      - Goodale J
      - Batalov S
      - Hodge CL
      - Haase J
      - Janes J
      - Huss JW 3rd
      - Su AI
products:
  - category: GraphicalInterface
    description: Main BioGPS web portal with searchable gene pages, expression charts, and plugin system aggregating external annotations
    format: http
    id: biogps.portal
    name: BioGPS Portal
    product_url: http://biogps.org/
  - category: ProgrammingInterface
    description: REST-style API for retrieving gene annotations and expression data (JSON/TSV responses)
    format: http
    id: biogps.api
    name: BioGPS API
    product_url: http://biogps.org/api/
  - category: Product
    description: Bulk annotation and expression data downloads (gene expression compendia, annotation tables)
    format: http
    id: biogps.downloads
    name: BioGPS Downloads
    product_url: http://biogps.org/downloads/
  - category: DocumentationProduct
    description: FAQ and usage guidance including plugin system overview and data interpretation notes
    format: http
    id: biogps.faq
    name: BioGPS FAQ / Help
    product_url: http://biogps.org/faq/
---

# BioGPS

## Overview

BioGPS is a community-extensible gene annotation and expression aggregation portal. It integrates numerous external resources via a plugin architecture, presenting unified gene-centric pages with tissue/cell-type expression charts, functional annotations, pathways, ontologies, interactions, and links out to specialized databases.

## Access

- Portal: interactive gene search and plugin-based annotation panels
- Downloads: bulk annotation and expression tables for offline analysis
- API: programmatic retrieval of gene annotation and expression data
- FAQ/Help: guidance on plugins, normalization, and citation

## Citation

Please cite the 2009 BioGPS portal paper (preferred) and optionally the 2013 update when using the resource.