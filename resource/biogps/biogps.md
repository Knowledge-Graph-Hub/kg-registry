---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://biogps.org/about/
  label: BioGPS / The Scripps Research Institute
creation_date: '2025-08-12T00:00:00Z'
description: BioGPS is an extensible and customizable gene annotation portal that
  aggregates gene-centric data (expression profiles, functional annotations, pathways,
  interactions, ontologies) from numerous external resources using a community-driven
  plugin system. It enables interactive expression visualization across tissues/cell
  types and provides programmatic and bulk access to underlying annotation tables.
domains:
- genomics
- biomedical
- biological systems
homepage_url: http://biogps.org/
id: biogps
last_modified_date: '2025-09-10T00:00:00Z'
layout: resource_detail
name: BioGPS
products:
- category: GraphicalInterface
  description: Main BioGPS web portal with searchable gene pages, expression charts,
    and plugin system aggregating external annotations
  format: http
  id: biogps.portal
  name: BioGPS Portal
  product_url: http://biogps.org/
- category: ProgrammingInterface
  description: REST-style API for retrieving gene annotations and expression data
    (JSON/TSV responses)
  format: http
  id: biogps.api
  name: BioGPS API
  product_url: http://biogps.org/api/
- category: Product
  description: Bulk annotation and expression data downloads (gene expression compendia,
    annotation tables)
  format: http
  id: biogps.downloads
  name: BioGPS Downloads
  product_url: http://biogps.org/downloads/
- category: DocumentationProduct
  description: FAQ and usage guidance including plugin system overview and data interpretation
    notes
  format: http
  id: biogps.faq
  name: BioGPS FAQ / Help
  product_url: http://biogps.org/faq/
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  product_url: https://zenodo.org/record/4077338
  secondary_source:
  - pharmkg
- category: Product
  description: Gene expression data aggregated from GTEx, BioGPS, Bgee and other expression
    databases
  format: http
  id: genecards.expression.data
  name: GeneCards Expression Data
  original_source:
  - gtex
  - biogps
  - bgee
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-25_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-11-25_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-26: HTTP 403 error
    when accessing file'
publications:
- authors:
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
  doi: 10.1186/gb-2009-10-11-r130
  id: doi:10.1186/gb-2009-10-11-r130
  journal: Genome Biology
  title: 'BioGPS: an extensible and customizable portal for querying and organizing
    gene annotation resources'
  year: '2009'
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