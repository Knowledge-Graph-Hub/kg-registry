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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  product_url: http://biogps.org/
- category: ProgrammingInterface
  description: REST-style API for retrieving gene annotations and expression data
    (JSON/TSV responses)
  format: http
  id: biogps.api
  name: BioGPS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  product_url: http://biogps.org/api/
- category: Product
  description: Bulk annotation and expression data downloads (gene expression compendia,
    annotation tables)
  format: http
  id: biogps.downloads
  name: BioGPS Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  product_url: http://biogps.org/downloads/
- category: DocumentationProduct
  description: FAQ and usage guidance including plugin system overview and data interpretation
    notes
  format: http
  id: biogps.faq
  name: BioGPS FAQ / Help
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  product_url: http://biogps.org/faq/
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: humannet
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharmkg
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://zenodo.org/record/4077338
- category: Product
  description: Gene expression data aggregated from GTEx, BioGPS, Bgee and other expression
    databases
  format: http
  id: genecards.expression.data
  name: GeneCards Expression Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://www.genecards.org/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
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