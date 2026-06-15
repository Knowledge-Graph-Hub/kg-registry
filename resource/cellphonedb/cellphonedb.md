---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: CellPhoneDB is a publicly available repository of manually curated human receptors, ligands and their interactions, paired with a statistical tool to infer cell-cell communication from single-cell transcriptomics data. It accounts for the subunit architecture of both ligands and receptors, accurately representing heteromeric complexes, and predicts enriched signaling between cell types based on the combined expression of interacting partners.
domains:
  - systems biology
  - biological systems
  - immunology
homepage_url: https://www.cellphonedb.org/
id: cellphonedb
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT
name: CellPhoneDB
products:
  - category: MappingProduct
    description: Curated database of human receptors, ligands and their interactions, including heteromeric complex composition, distributed as downloadable files for use with the CellPhoneDB analysis package.
    format: csv
    id: cellphonedb.database
    name: CellPhoneDB Interactions Database
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cellphonedb
    product_url: https://www.cellphonedb.org/downloads
  - category: ProcessProduct
    description: Python package that interrogates single-cell transcriptomics data against the CellPhoneDB database to statistically infer enriched ligand-receptor interactions between cell types.
    format: python
    id: cellphonedb.package
    name: CellPhoneDB Python Package
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cellphonedb
    product_url: https://github.com/ventolab/CellphoneDB
  - category: GraphicalInterface
    description: Web interface for browsing and searching CellPhoneDB receptors, ligands and their curated interactions.
    format: http
    id: cellphonedb.web
    name: CellPhoneDB Web Interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cellphonedb
    product_url: https://www.cellphonedb.org/
  - category: DocumentationProduct
    description: Source code, tutorials, and documentation for the CellPhoneDB database and analysis package.
    format: http
    id: cellphonedb.docs
    name: CellPhoneDB Repository and Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cellphonedb
    product_url: https://github.com/ventolab/CellphoneDB
publications:
  - authors:
      - Mirjana Efremova
      - Miquel Vento-Tormo
      - Sarah A. Teichmann
      - Roser Vento-Tormo
    doi: doi:10.1038/s41596-020-0292-x
    id: doi:10.1038/s41596-020-0292-x
    journal: Nature Protocols
    preferred: true
    title: 'CellPhoneDB: inferring cell–cell communication from combined expression of multi-subunit ligand–receptor complexes'
    year: '2020'
repository: https://github.com/ventolab/CellphoneDB
---

# CellPhoneDB

CellPhoneDB is a publicly available repository of manually curated human receptors,
ligands and their interactions, paired with a statistical tool to infer cell-cell
communication from single-cell transcriptomics data. Unlike resources that treat
interactions as binary pairs, CellPhoneDB accounts for the subunit architecture of
both ligands and receptors, accurately representing heteromeric complexes.

In KG-Registry, the CellPhoneDB products surface the curated interactions database,
the Python analysis package that predicts enriched cell-cell interactions from
single-cell expression data, the web interface for browsing the database, and the
source code and documentation.
