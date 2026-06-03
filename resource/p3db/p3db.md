---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.p3db.org/
    label: Plant Protein Phosphorylation Database
creation_date: '2026-06-02T00:00:00Z'
description: P3DB, the Plant Protein Phosphorylation Database, is a plant phosphoproteomics resource that collects phosphorylation sites, phosphopeptides, kinases, organisms, and study datasets with search and BLAST tools.
domains:
  - plant science
  - proteomics
  - biological systems
homepage_url: https://www.p3db.org/
id: p3db
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: P3DB
products:
  - category: GraphicalInterface
    description: P3DB V5.0 web portal for searching plant phosphorylation peptides and sites, browsing kinases and organisms, and using PTM peptide BLAST tools.
    id: p3db.portal
    name: P3DB Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: p3db
    product_url: https://www.p3db.org/
  - category: Product
    description: P3DB study and organism datasets for plant protein phosphorylation, including phosphorylation sites, peptides, substrate proteins, and associated study metadata.
    format: mixed
    id: p3db.datasets
    name: P3DB Plant Phosphorylation Datasets
    original_source:
      - relation_type: prov:hadPrimarySource
        source: p3db
    product_url: https://www.p3db.org/
  - category: ProcessProduct
    description: P3DB PTM peptide BLAST and search tools for querying plant phosphopeptides and phosphorylation sites by sequence or accession.
    id: p3db.ptm-search
    name: P3DB PTM Search and BLAST Tools
    original_source:
      - relation_type: prov:hadPrimarySource
        source: p3db
    product_url: https://www.p3db.org/
  - category: GraphProduct
    description: Current iPTMnet PTM record table with PTM type, source, UniProt protein, organism, site, enzyme, relation identifiers, and publication evidence.
    format: tsv
    id: iptmnet.ptm
    license:
      id: https://creativecommons.org/licenses/by-nc-sa/4.0/
      label: CC BY-NC-SA 4.0
    name: iPTMnet PTM Table
    original_source:
      - relation_type: prov:hadPrimarySource
        source: iptmnet
    product_file_size: 44116546
    product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/ptm.txt
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: dbptm
      - relation_type: prov:wasDerivedFrom
        source: dbsno
      - relation_type: prov:wasDerivedFrom
        source: efip
      - relation_type: prov:wasDerivedFrom
        source: hprd
      - relation_type: prov:wasDerivedFrom
        source: nextprot
      - relation_type: prov:wasDerivedFrom
        source: p3db
      - relation_type: prov:wasDerivedFrom
        source: phosphoelm
      - relation_type: prov:wasDerivedFrom
        source: phosphogrid
      - relation_type: prov:wasDerivedFrom
        source: phosphositeplus
      - relation_type: prov:wasDerivedFrom
        source: phosphat
      - relation_type: prov:wasDerivedFrom
        source: pombase
      - relation_type: prov:wasDerivedFrom
        source: pubtator
      - relation_type: prov:wasDerivedFrom
        source: rlims-p
      - relation_type: prov:wasDerivedFrom
        source: signor
      - relation_type: prov:wasDerivedFrom
        source: uniprot
publications:
  - authors:
      - Jianjiong Gao
      - Liqin Agrawal
      - Allison Thelen
      - Jay J Thelen
      - Dong Xu
    doi: 10.3389/fpls.2012.00206
    id: doi:10.3389/fpls.2012.00206
    journal: Frontiers in Plant Science
    preferred: true
    title: 'P3DB: an integrated database for plant protein phosphorylation'
    year: '2012'
taxon:
  - NCBITaxon:33090
synonyms:
  - Plant Protein Phosphorylation Database
---

# P3DB

P3DB is an integrated plant protein phosphorylation database with searchable
phosphopeptides, phosphorylation sites, kinases, organism views, and study
datasets. Its curated plant PTM information is also represented as an upstream
source in iPTMnet.
