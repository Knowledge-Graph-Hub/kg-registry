---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: xiaoyun@ems.hrbmu.edu.cn
  label: Yun Xiao
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bio-bigdata.hrbmu.edu.cn/CellMarker/
  label: College of Bioinformatics Science and Technology, Harbin Medical University
creation_date: '2025-07-20T00:00:00Z'
description: CellMarker is a comprehensive and accurate resource of cell markers for
  various cell types in tissues of human and mouse. CellMarker 2.0 provides a manually
  curated collection of 26,915 markers across 2,578 cell types and 656 tissues, resulting
  in 83,361 tissue-cell type-marker entries, and includes integrated web tools for
  single-cell data analysis.
domains:
- biomedical
- genomics
- biological systems
- organisms
homepage_url: https://bio-bigdata.hrbmu.edu.cn/CellMarker/
id: cellmarker
infores_id: cellmarker
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: CellMarker
products:
- category: Product
  description: Human CellMarker 2.0 marker dataset in spreadsheet format
  format: mixed
  id: cellmarker.human
  name: Human Cell Markers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  product_file_size: 7982475
  product_url: http://117.50.127.228/CellMarker/CellMarker_download_files/file/Cell_marker_Human.xlsx
- category: Product
  description: Mouse CellMarker 2.0 marker dataset in spreadsheet format
  format: mixed
  id: cellmarker.mouse
  name: Mouse Cell Markers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  product_file_size: 3740448
  product_url: http://117.50.127.228/CellMarker/CellMarker_download_files/file/Cell_marker_Mouse.xlsx
- category: Product
  description: CellMarker 2.0 marker dataset derived from single-cell sequencing studies
    in human and mouse
  format: mixed
  id: cellmarker.singlecell
  name: Single Cell Markers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  product_file_size: 6005874
  product_url: http://117.50.127.228/CellMarker/CellMarker_download_files/file/Cell_marker_Seq.xlsx
- category: Product
  description: Combined CellMarker 2.0 marker dataset for human and mouse in spreadsheet
    format
  format: mixed
  id: cellmarker.all
  name: All Cell Markers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  product_file_size: 10010437
  product_url: http://117.50.127.228/CellMarker/CellMarker_download_files/file/Cell_marker_All.xlsx
- category: GraphicalInterface
  description: CellMarker 2.0 annotation tool for assigning cell types using curated
    marker genes
  format: http
  id: cellmarker.act
  name: Cell Annotation Tool
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  product_url: http://117.50.127.228/CellMarker/CellMarker_annotation.jsp
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  format: python
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/gyorilab/indra_cogex
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
  - Hu C
  - Li T
  - Xu Y
  - Zhang X
  - Li F
  - Bai J
  - Chen J
  - Jiang W
  - Yang K
  - Ou Q
  - Li X
  - Zhang Y
  doi: 10.1093/nar/gkac947
  id: doi:10.1093/nar/gkac947
  journal: Nucleic Acids Research
  preferred: true
  title: 'CellMarker 2.0: an updated database of manually curated cell markers in
    human/mouse and web tools based on scRNA-seq data'
  year: '2023'
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
  title: CellMarker - a manually curated resource of cell markers in human and mouse
  year: '2019'
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# CellMarker

CellMarker is a curated resource of marker genes for cell types across human and mouse tissues. The current CellMarker 2.0 release expands the original database and adds integrated web tools for single-cell analysis workflows.

## Overview

CellMarker 2.0 reports:
- 26,915 cell markers
- 2,578 cell types
- 656 tissues
- 83,361 tissue-cell type-marker entries

The database provides browsing, search, download, and analysis interfaces for markers of diverse cell types from different tissues. It also captures sequencing technology, marker type, and related metadata for each curated entry.

## Features

Users can:
- Browse cell markers in different cells of different tissues in human and mouse
- Retrieve cell markers of particular cell types in any tissues of interest
- Obtain prevalence of cell markers in each cell type through statistical graphs
- Download cell markers of diverse cell types of different tissues
- Submit data to CellMarker

## CellMarker 2.0 Web Tools

CellMarker 2.0 includes integrated tools for cell annotation, clustering, malignancy analysis, differentiation, feature inspection, and cell-cell communication analysis based on single-cell datasets and the curated CellMarker resource.