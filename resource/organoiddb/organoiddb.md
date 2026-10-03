---
activity_status: active
category: DataSource
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: panjianbo@cqmu.edu.cn
    label: Jianbo Pan
creation_date: '2026-10-02T00:00:00Z'
description: OrganoidDB is a database of curated bulk and single-cell transcriptome profiles of organoids. It holds 16,218 organoid samples (12,911 human and 3,307 mouse) collected from GEO and ArrayExpress and organized into 1,069 datasets, 145 of them single-cell RNA-seq. Primary tissue and cell line samples are included so that organoids can be compared against them, with GTEx and the Human Protein Atlas linked as references. The web interface supports gene expression search across organoid types, culture sources and protocols, sample types and developmental stages, plus correlation analysis, and datasets can be browsed with culture details, differentially expressed genes, enriched pathways and single-cell clusters. It is run by the Intelligent Bioinformatics Research Group at the Institute of Life Sciences, Chongqing Medical University.
domains:
  - biomedical
  - genomics
  - gene expression profiling
  - biological systems
  - single-cell analysis
  - anatomy and development
homepage_url: http://www.inbirg.com/organoid_db/
id: organoiddb
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  id: http://www.inbirg.com/organoid_db/
  label: Copyright Intelligent Bioinformatics Research Group, Chongqing Medical University (all rights reserved)
name: OrganoidDB
products:
  - category: GraphicalInterface
    description: Web interface for searching gene expression across organoid types, culture sources and protocols, sample types and developmental stages, with correlation analysis and dataset pages showing culture details, differentially expressed genes, enriched pathways and single-cell clusters.
    format: http
    id: organoiddb.portal
    name: OrganoidDB web portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: organoiddb
    product_url: http://www.inbirg.com/organoid_db/genes
  - category: Product
    description: Sample metadata for every organoid sample in OrganoidDB, with study and sample accessions, tissue, platform, species, PubMed ID and sample characteristics.
    format: csv
    id: organoiddb.all-organoid-samples
    name: OrganoidDB all organoid samples
    original_source:
      - relation_type: prov:hadPrimarySource
        source: organoiddb
      - relation_type: prov:hadPrimarySource
        source: gene-expression-omnibus
      - relation_type: prov:hadPrimarySource
        source: arrayexpress
    product_file_size: 3258002
    product_url: http://www.inbirg.com/organoid_db/download/all_org_samples
  - category: Product
    description: Sample metadata for the organoid samples used by the OrganoidDB organoid specificity search.
    format: csv
    id: organoiddb.organoid-specificity-samples
    name: OrganoidDB organoid specificity samples
    original_source:
      - relation_type: prov:hadPrimarySource
        source: organoiddb
      - relation_type: prov:hadPrimarySource
        source: gene-expression-omnibus
      - relation_type: prov:hadPrimarySource
        source: arrayexpress
    product_file_size: 257601
    product_url: http://www.inbirg.com/organoid_db/download/org_specificity_samples
  - category: Product
    description: Sample metadata for the primary tissue and cell line samples that OrganoidDB uses for comparison with organoids.
    format: csv
    id: organoiddb.general-samples
    name: OrganoidDB general samples
    original_source:
      - relation_type: prov:hadPrimarySource
        source: organoiddb
      - relation_type: prov:hadPrimarySource
        source: gene-expression-omnibus
      - relation_type: prov:hadPrimarySource
        source: arrayexpress
    product_file_size: 94026
    product_url: http://www.inbirg.com/organoid_db/download/general_samples
publications:
  - authors:
      - Qinfeng Ma
      - Haodong Tao
      - Qiang Li
      - Zhaoyu Zhai
      - Xuelu Zhang
      - Zhewei Lin
      - Ni Kuang
      - Jianbo Pan
    doi: 10.1093/nar/gkac942
    id: https://pubmed.ncbi.nlm.nih.gov/36271792/
    journal: Nucleic Acids Res
    preferred: true
    title: 'OrganoidDB: a comprehensive organoid database for the multi-perspective exploration of bulk and single-cell transcriptomic profiles of organoids'
    year: '2023'
version: '1.0'
---
# OrganoidDB

OrganoidDB is a database of curated bulk and single-cell transcriptome profiles
of organoids. It holds 16,218 organoid samples (12,911 human and 3,307 mouse)
collected from GEO and ArrayExpress and organized into 1,069 datasets, 145 of
them single-cell RNA-seq.

Primary tissue and cell line samples are included so that organoids can be
compared against them, with GTEx and the Human Protein Atlas linked as
references. The web interface supports gene expression search across organoid
types, culture sources and protocols, sample types and developmental stages,
plus correlation analysis. Sample metadata can be downloaded as CSV.

OrganoidDB is run by the Intelligent Bioinformatics Research Group at the
Institute of Life Sciences, Chongqing Medical University.
