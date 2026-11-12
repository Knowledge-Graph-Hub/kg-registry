---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.mavedb.org/
  - contact_type: github
    value: VariantEffect
  label: MaveDB Team (Atlas of Variant Effects Alliance)
creation_date: '2026-11-12T00:00:00Z'
description: MaveDB is an open-source community database of record for datasets
  from multiplexed assays of variant effect (MAVEs), such as deep mutational scanning
  (DMS), saturation genome editing, and massively parallel reporter assays (MPRAs).
  It stores variant effect score sets and, where available, raw count data, together
  with structured metadata on the experiment, the assayed target sequence, and the
  associated publications. The 2024 update holds over 7 million variant effect measurements
  and maps variants to reference genome and protein coordinates, with built-in visualization
  tools, a REST API for data federation and submission, and periodic bulk downloads.
domains:
- genomics
- genetic variation
- proteomics
- precision medicine
homepage_url: https://www.mavedb.org/
id: mavedb
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://api.mavedb.org/api/v1/licenses/
  label: Varies by dataset (CC0 1.0, CC BY 4.0, or CC BY-SA 4.0)
name: MaveDB
products:
- category: GraphicalInterface
  description: Web interface for searching, browsing, visualizing, and submitting
    MAVE experiment sets, experiments, and variant effect score sets.
  format: http
  id: mavedb.portal
  is_public: true
  name: MaveDB Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mavedb
  product_url: https://www.mavedb.org/
- category: ProgrammingInterface
  description: REST API for programmatic search, retrieval, and submission of MaveDB
    records, including score sets, count data, target genes, and variant mappings.
  format: http
  id: mavedb.api
  is_public: true
  name: MaveDB API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mavedb
  product_url: https://api.mavedb.org/docs
- category: Product
  compression: targz
  description: Bulk download of all data published in MaveDB under the Creative Commons
    Zero license, including score and count tables with associated record metadata.
    Deposited periodically on Zenodo.
  format: mixed
  id: mavedb.bulk-download
  is_public: true
  latest_version: '2026-06-24'
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: MaveDB Bulk Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mavedb
  product_file_size: 1907736956
  product_url: https://doi.org/10.5281/zenodo.11201736
- category: ProcessProduct
  description: Source code for the MaveDB API server, which provides the database
    back end and REST API for MaveDB.
  format: python
  id: mavedb.api-code
  is_public: true
  license:
    id: https://www.gnu.org/licenses/agpl-3.0.en.html
    label: AGPL-3.0
  name: MaveDB API Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mavedb
  product_url: https://github.com/VariantEffect/mavedb-api
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
    source: alliance
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
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: civic
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
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: drugcentral
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
    source: faers
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hmdd
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mavedb
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
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panelapp
  - relation_type: prov:hadPrimarySource
    source: pangolin
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
    source: revel
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: saprot
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://sugi.bio/biobtree/api/
publications:
- authors:
  - Alan F. Rubin
  - Jeremy Stone
  - Aisha Haley Bianchi
  - Benjamin J. Capodanno
  doi: 10.1186/s13059-025-03476-y
  id: doi:10.1186/s13059-025-03476-y
  journal: Genome Biology
  preferred: true
  title: 'MaveDB 2024: a curated community database with over seven million variant
    effects from multiplexed functional assays'
  year: '2025'
- authors:
  - Daniel Esposito
  - Jochen Weile
  - Jay Shendure
  - Lea M. Starita
  doi: 10.1186/s13059-019-1845-6
  id: doi:10.1186/s13059-019-1845-6
  journal: Genome Biology
  title: 'MaveDB: an open-source platform to distribute and interpret data from multiplexed
    assays of variant effect'
  year: '2019'
repository: https://github.com/VariantEffect/mavedb-api
---
# MaveDB

MaveDB is a public repository for datasets from multiplexed assays of variant effect (MAVEs), including deep mutational scanning, saturation genome editing, and massively parallel reporter assays. Records are organized as experiment sets, experiments, and score sets, each with metadata describing the assay, the target sequence, and linked publications. Variants are described using MAVE-HGVS notation and, for human targets, are mapped to reference genome and protein coordinates so they can be compared with other variant resources.

The 2024 update (Rubin et al., Genome Biology 2025) expanded MaveDB to over 7 million variant effect measurements, extended the data model to support assays such as saturation genome editing, and added exploration and visualization tools and APIs for federation and submission. Data licensing is set per dataset (CC0 1.0, CC BY 4.0, or CC BY-SA 4.0); the Zenodo bulk download contains all CC0-licensed data.
