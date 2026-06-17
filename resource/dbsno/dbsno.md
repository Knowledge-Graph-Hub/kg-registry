---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://biomics.lab.nycu.edu.tw/dbSNO/index.php
  label: dbSNO Team
creation_date: '2026-06-02T00:00:00Z'
description: dbSNO is a protein S-nitrosylation database that curates experimentally
  verified S-nitrosylated proteins and cysteine sites with structural, functional,
  disease, and regulatory network annotations.
domains:
- biomedical
- proteomics
- biological systems
homepage_url: https://biomics.lab.nycu.edu.tw/dbSNO/index.php
id: dbsno
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
name: dbSNO
products:
- category: GraphicalInterface
  description: dbSNO 3.0 web portal for searching, browsing, and analyzing S-nitrosylated
    proteins, SNO sites, disease associations, SNO regulatory networks, and structural
    environments.
  id: dbsno.portal
  name: dbSNO Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbsno
  product_url: https://biomics.lab.nycu.edu.tw/dbSNO/index.php
- category: Product
  description: Tab-delimited dbSNO 3.0 S-nitrosylation dataset containing UniProt
    identifiers, organisms, positions, and sequence context for manually curated and
    experimentally identified S-nitrosylated peptides.
  format: tsv
  id: dbsno.downloads
  name: dbSNO Download Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbsno
  product_url: https://biomics.lab.nycu.edu.tw/dbSNO/download.php
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 500 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-17: HTTP 500 error
    when accessing file'
- category: GraphProduct
  description: Current iPTMnet PTM record table with PTM type, source, UniProt protein,
    organism, site, enzyme, relation identifiers, and publication evidence.
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
  - Yi-Ju Chen
  - Cheng-Tsung Lu
  - Min-Gang Su
  - Kai-Yao Huang
  - Wei-Chieh Ching
  - Hsiao-Hsiang Yang
  - Yen-Chen Liao
  - Yu-Ju Chen
  - Tzong-Yi Lee
  doi: 10.1093/nar/gku1176
  id: doi:10.1093/nar/gku1176
  journal: Nucleic Acids Research
  preferred: true
  title: 'dbSNO 2.0: a resource for exploring structural environment, functional and
    disease association and regulatory network of protein S-nitrosylation'
  year: '2015'
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# dbSNO

dbSNO curates protein S-nitrosylation sites from literature and proteomics
experiments and provides analyses for structural context, disease associations,
and SNO regulatory networks.