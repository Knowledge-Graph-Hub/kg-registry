---
activity_status: inactive
category: DataSource
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: juri.reimand@utoronto.ca
    label: Juri Reimand
creation_date: '2026-06-02T00:00:00Z'
description: ActiveDriverDB is a human proteo-genomics database for interpreting genetic variation, disease mutations, and cancer driver genes using post-translational modification sites and signaling networks.
domains:
  - biomedical
  - genomics
  - proteomics
homepage_url: https://activedriverdb.org/
id: activedriverdb
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: ActiveDriverDB
products:
  - category: GraphicalInterface
    description: Web interface for searching and browsing ActiveDriverDB proteins, mutations, pathways, and PTM-site annotations.
    id: activedriverdb.portal
    name: ActiveDriverDB Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: activedriverdb
    product_url: https://activedriverdb.org/
  - category: ProgrammingInterface
    description: REST API for retrieving ActiveDriverDB protein mutation, genomic mutation, and network annotations in JSON format.
    format: json
    id: activedriverdb.api
    is_public: true
    name: ActiveDriverDB API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: activedriverdb
    product_url: https://activedriverdb.org/api/
  - category: Product
    compression: zip
    description: Bulk downloadable ActiveDriverDB datasets, including cancer, disease, and population mutations affecting PTM sites and kinase-target site-specific networks.
    id: activedriverdb.downloads
    name: ActiveDriverDB Downloads
    original_source:
      - relation_type: prov:hadPrimarySource
        source: activedriverdb
    product_url: https://activedriverdb.org/download/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: 1000genomes
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: phosphositeplus
      - relation_type: prov:wasDerivedFrom
        source: tcga
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
      - Michal Krassowski
      - Digdem Paczkowska
      - Martin J Fradet-Turcotte
      - Gholamreza R Bader
      - Juri Reimand
    doi: 10.3389/fcell.2021.626821
    id: doi:10.3389/fcell.2021.626821
    journal: Frontiers in Cell and Developmental Biology
    preferred: true
    title: 'ActiveDriverDB: Interpreting genetic variation in human and cancer genomes using post-translational modification sites and signaling networks'
    year: '2021'
repository: https://github.com/reimandlab/ActiveDriverDB
warnings:
  - ActiveDriverDB announced that the database would be retired on May 1, 2026; the website and downloads should be checked before relying on continued availability.
---

# ActiveDriverDB

ActiveDriverDB uses post-translational modification sites and signaling network
context to annotate human genetic variation, disease mutations, and cancer driver
genes. The 2021 release provides a searchable web interface, REST API, and bulk
downloads, but the project homepage announced planned retirement of the service
on May 1, 2026.
