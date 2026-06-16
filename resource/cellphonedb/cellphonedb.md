---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: CellPhoneDB is a publicly available repository of manually curated human
  receptors, ligands and their interactions, paired with a statistical tool to infer
  cell-cell communication from single-cell transcriptomics data. It accounts for the
  subunit architecture of both ligands and receptors, accurately representing heteromeric
  complexes, and predicts enriched signaling between cell types based on the combined
  expression of interacting partners.
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
  description: Curated database of human receptors, ligands and their interactions,
    including heteromeric complex composition, distributed as downloadable files for
    use with the CellPhoneDB analysis package.
  format: csv
  id: cellphonedb.database
  name: CellPhoneDB Interactions Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  product_url: https://www.cellphonedb.org/downloads
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 404 error
    when accessing file'
- category: ProcessProduct
  description: Python package that interrogates single-cell transcriptomics data against
    the CellPhoneDB database to statistically infer enriched ligand-receptor interactions
    between cell types.
  format: python
  id: cellphonedb.package
  name: CellPhoneDB Python Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  product_url: https://github.com/ventolab/CellphoneDB
- category: GraphicalInterface
  description: Web interface for browsing and searching CellPhoneDB receptors, ligands
    and their curated interactions.
  format: http
  id: cellphonedb.web
  name: CellPhoneDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  product_url: https://www.cellphonedb.org/
- category: DocumentationProduct
  description: Source code, tutorials, and documentation for the CellPhoneDB database
    and analysis package.
  format: http
  id: cellphonedb.docs
  name: CellPhoneDB Repository and Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  product_url: https://github.com/ventolab/CellphoneDB
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
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
  title: 'CellPhoneDB: inferring cell–cell communication from combined expression
    of multi-subunit ligand–receptor complexes'
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