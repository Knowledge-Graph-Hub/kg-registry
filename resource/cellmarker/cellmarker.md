---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: xiaoyun@ems.hrbmu.edu.cn
  label: Yun Xiao
creation_date: '2025-07-20T00:00:00Z'
description: CellMarker is a comprehensive and accurate resource of cell markers for
  various cell types in tissues of human and mouse. By manually curating over 100,000
  published papers, the database contains 13,605 cell markers of 467 cell types in
  158 human tissues/sub-tissues and 9,148 cell makers of 389 cell types in 81 mouse
  tissues/sub-tissues.
domains:
- biomedical
- genomics
- biological systems
- organisms
homepage_url: http://xteam.xbio.top/
id: cellmarker
last_modified_date: '2025-07-20T00:00:00Z'
layout: resource_detail
name: CellMarker
products:
- category: Product
  description: Cell markers of different cell types from different tissues in human
  id: cellmarker.human
  name: Human Cell Markers
  product_url: http://xteam.xbio.top/download/Human_cell_markers.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-08-12: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-13: No Content-Length
    header found'
- category: Product
  description: Cell markers of different cell types from different tissues in mouse
  id: cellmarker.mouse
  name: Mouse Cell Markers
  product_url: http://xteam.xbio.top/download/Mouse_cell_markers.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-08-12: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-13: No Content-Length
    header found'
- category: Product
  description: Cell markers derived from single-cell sequencing researches in human
    and mouse
  id: cellmarker.singlecell
  name: Single Cell Markers
  product_url: http://xteam.xbio.top/download/Single_cell_markers.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-08-12: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-13: No Content-Length
    header found'
- category: Product
  description: All cell markers of different cell types from different tissues in
    human and mouse
  id: cellmarker.all
  name: All Cell Markers
  product_url: http://xteam.xbio.top/download/all_cell_markers.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-08-12: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-08-13: No Content-Length
    header found'
- category: GraphicalInterface
  description: ACT is a tool that makes cell type annotation easier by integrating
    the CellMarker resource.
  id: cellmarker.act
  name: ACT (Annotation of Cell Types)
  product_url: http://xteam.xbio.top/ACT/
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - chembl
  - sider
  - reactome
  - wikipathways
  - hp
  - nihreporter
  - disgenet
  - pubmed
  - gwascatalog
  - cellmarker
  - go
  - bgee
  - ccle
  - clinicaltrialsgov
  - indra
  product_url: https://github.com/gyorilab/indra_cogex
  secondary_source:
  - indra
publications:
- authors:
  - Zhang X
  - Lan Y
  - Xu J
  - Quan F
  - Zhao E
  - Deng C
  - Luo T
  - Xu L
  - Liao G
  - Yan M
  - Ping Y
  - Li F
  - Shi A
  - Bai J
  - Zhao T
  - Li X
  - Xiao Y
  doi: 10.1093/nar/gky900
  id: doi:10.1093/nar/gky900
  journal: Nucleic Acids Research
  preferred: true
  title: CellMarker - a manually curated resource of cell markers in human and mouse
  year: '2018'
---
# CellMarker

CellMarker is a comprehensive and accurate resource of cell markers for various cell types in tissues of human and mouse. It was developed to provide researchers with a curated database of cell markers that can be used to distinguish different cell types in tissues.

## Overview

By manually curating over 100,000 published papers, the database contains:
- 13,605 cell markers of 467 cell types in 158 human tissues/sub-tissues 
- 9,148 cell makers of 389 cell types in 81 mouse tissues/sub-tissues

The database provides a user-friendly interface for browsing, searching, and downloading markers of diverse cell types from different tissues. Additionally, a summarized marker prevalence in each cell type is graphically presented through statistical visualizations.

## Features

Users can:
- Browse cell markers in different cells of different tissues in human and mouse
- Retrieve cell markers of particular cell types in any tissues of interest
- Obtain prevalence of cell markers in each cell type through statistical graphs
- Download cell markers of diverse cell types of different tissues
- Submit data to CellMarker

## ACT Tool

The CellMarker team has also developed ACT (Annotation of Cell Types), a tool that makes cell type annotation easier by integrating the CellMarker resource. ACT was developed based on the structural marker map and the cell type enrichment algorithm, with the aim of efficiently facilitating the process of cell type annotation.