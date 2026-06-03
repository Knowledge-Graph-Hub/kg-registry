---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://hivelab.biochemistry.gwu.edu/
    label: GW HIVE Lab
creation_date: '2026-06-02T00:00:00Z'
description: BioMuta is a cancer-associated single-nucleotide variation resource that integrates mutation records from cancer genomics sources into a unified dataset with protein and disease annotations.
domains:
  - biomedical
  - genomics
  - precision medicine
homepage_url: https://hivelab.biochemistry.gwu.edu/biomuta
id: biomuta
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: BioMuta
products:
  - category: GraphicalInterface
    description: Production BioMuta web interface hosted by the GW HIVE Lab for exploring cancer-associated mutation records.
    id: biomuta.portal
    name: BioMuta Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biomuta
    product_url: https://hivelab.biochemistry.gwu.edu/biomuta
  - category: Product
    description: Unified BioMuta cancer mutation dataset produced by combining mutation records from TCGA, ICGC, CIViC, and COSMIC into a common field structure.
    format: csv
    id: biomuta.dataset
    name: BioMuta Cancer Mutation Dataset
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biomuta
    product_url: https://biomuta.readthedocs.io/en/latest/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: civic
      - relation_type: prov:wasDerivedFrom
        source: cosmic
      - relation_type: prov:wasDerivedFrom
        source: icgc
      - relation_type: prov:wasDerivedFrom
        source: tcga
  - category: ProcessProduct
    description: BioMuta v5 data release pipeline for downloading, converting, and combining cancer mutation source files into BioMuta datasets.
    id: biomuta.pipeline
    name: BioMuta Data Release Pipeline
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biomuta
    product_url: https://biomuta.readthedocs.io/en/latest/
    repository: https://github.com/GW-HIVE/biomuta
  - category: Product
    compression: zip
    description: Complete PTMD 2.0 PTM-disease association download in tab-delimited format
    format: tsv
    id: ptmd.total_pda
    name: PTMD Total PTM-Disease Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ptmd
    product_file_size: 4756362
    product_url: https://ptmd.biocuckoo.cn/Download/Total.zip
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: activedriverdb
      - relation_type: prov:wasDerivedFrom
        source: biomuta
      - relation_type: prov:wasDerivedFrom
        source: phosphositeplus
publications:
  - authors:
      - Hayley M Dingerdissen
      - John Torcivia-Rodriguez
      - Yu Hu
      - Ting-Chia Chang
      - Raja Mazumder
      - Robel Kahsay
    doi: 10.1093/nar/gkx907
    id: doi:10.1093/nar/gkx907
    journal: Nucleic Acids Research
    preferred: true
    title: 'BioMuta and BioXpress: mutation and expression knowledgebases for cancer biomarker discovery'
    year: '2018'
repository: https://github.com/GW-HIVE/biomuta
taxon:
  - NCBITaxon:9606
---

# BioMuta

BioMuta aggregates cancer-associated single-nucleotide variation records into a
common structure for search, visualization, and downstream analysis. The v5
pipeline documentation describes the source download, conversion, and combination
steps used to produce the unified BioMuta dataset.
