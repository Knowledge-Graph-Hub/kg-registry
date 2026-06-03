---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://biomics.lab.nycu.edu.tw/dbPTM/
    label: dbPTM Team
creation_date: '2026-06-02T00:00:00Z'
description: dbPTM is an integrated protein post-translational modification resource that curates experimentally verified PTM sites, literature evidence, proteomic datasets, regulatory networks, and disease-associated PTM annotations.
domains:
  - biomedical
  - proteomics
  - biological systems
homepage_url: https://biomics.lab.nycu.edu.tw/dbPTM/
id: dbptm
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: dbPTM
products:
  - category: GraphicalInterface
    description: dbPTM 2025 web portal for searching proteins, browsing PTM general information, and analyzing disease-associated PTMs, PTM crosstalk, drug-binding-associated PTM sites, and kinase activity profiles.
    id: dbptm.portal
    name: dbPTM Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: dbptm
    product_url: https://biomics.lab.nycu.edu.tw/dbPTM/
  - category: Product
    description: dbPTM downloads for experimental and putative PTM sites, benchmark datasets, and cancer proteomics datasets, with PTM records mapped to UniProtKB protein entries and linked to literature evidence.
    format: tsv
    id: dbptm.downloads
    name: dbPTM Download Datasets
    original_source:
      - relation_type: prov:hadPrimarySource
        source: dbptm
    product_url: https://biomics.lab.nycu.edu.tw/dbPTM/download.php
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: pubmed
      - relation_type: prov:wasDerivedFrom
        source: uniprot
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
      - Chia-Ru Chung
      - Yun Tang
      - Yen-Peng Chiu
      - Shangfu Li
      - Wen-Kai Hsieh
      - Tzong-Yi Lee
    doi: 10.1093/nar/gkae1005
    id: doi:10.1093/nar/gkae1005
    journal: Nucleic Acids Research
    preferred: true
    title: 'dbPTM 2025 update: comprehensive integration of PTMs and proteomic data for advanced insights into cancer research'
    year: '2025'
taxon:
  - NCBITaxon:9606
  - NCBITaxon:10090
---

# dbPTM

dbPTM integrates experimentally verified post-translational modification sites
from curated literature and PTM-related databases, maps records to UniProtKB
proteins, and exposes web analysis views and downloadable PTM datasets.
