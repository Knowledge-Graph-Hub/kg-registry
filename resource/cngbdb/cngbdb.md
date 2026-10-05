---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: CNGBdb@cngb.org
  - contact_type: url
    value: https://db.cngb.org/
  label: China National GeneBank
creation_date: '2026-10-05T00:00:00Z'
description: The China National GeneBank DataBase (CNGBdb) is a platform for sharing
  and analyzing biological data, run by the China National GeneBank (CNGB) in Shenzhen
  and launched in 2018. Its main archive is the CNGB Sequence Archive (CNSA), established
  in 2017, which archives raw sequencing reads and analysis results organized as projects,
  samples, experiments, runs, assemblies and variations, along with metabolomic, single-cell
  and spatial transcriptomic data. CNGBdb also offers search across literature, gene,
  protein, sequence, organism and other sub-databases that include data integrated
  from NCBI and EBI, plus the Spatial Transcript Omics DataBase (STOmicsDB). Public
  CNSA data is free to download over FTP, HTTPS and Aspera.
domains:
- genomics
- organisms
- biodiversity
fairsharing_id: FAIRsharing.9btRvC
homepage_url: https://db.cngb.org/
id: cngbdb
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: China National GeneBank DataBase
products:
- category: GraphicalInterface
  description: CNGBdb web portal for searching CNSA records and the integrated literature,
    gene, protein, sequence, organism, variation and other sub-databases, which include
    data from NCBI and EBI.
  format: http
  id: cngbdb.portal
  name: CNGBdb Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cngbdb
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: ena
  product_url: https://db.cngb.org/
- category: GraphicalInterface
  description: CNGB Sequence Archive (CNSA) interface for submitting and browsing
    projects, samples, experiments, runs, assemblies, variations and other omics data.
    Accessions use prefixes such as CNP (project), CNS (sample), CNX (experiment),
    CNR (run) and CNA (assembly).
  format: http
  id: cngbdb.cnsa
  name: CNSA Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cngbdb
  product_url: https://db.cngb.org/cnsa/
- category: Product
  description: Public FTP/HTTPS download area for CNSA data files, split across data1
    to data7 subdirectories.
  format: mixed
  id: cngbdb.cnsa.ftp
  name: CNSA Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cngbdb
  product_url: https://ftp.cngb.org/pub/CNSA/
- category: GraphicalInterface
  description: Spatial Transcript Omics DataBase (STOmicsDB), the CNGBdb component
    for sharing, analyzing and visualizing spatial transcriptomics datasets.
  format: http
  id: cngbdb.stomicsdb
  name: STOmicsDB
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cngbdb
  product_url: https://db.cngb.org/stomics/
- category: DocumentationProduct
  description: English-language CNSA handbook, covering account setup and how to submit
    and access data.
  format: pdf
  id: cngbdb.cnsa.handbook
  name: CNSA Handbook
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cngbdb
  product_file_size: 1131662
  product_url: https://db.cngb.org/dc_assets/data/dc_cnsa/doc/cnsa_handbook_en.pdf
publications:
- authors:
  - Xueqin Guo
  - Fengzhen Chen
  - Fei Gao
  - Ling Li
  - Ke Liu
  - Lijin You
  - Cong Hua
  - Fan Yang
  - Wanliang Liu
  - Chunhua Peng
  - Lina Wang
  - Xiaoxia Yang
  - Feiyu Zhou
  - Jiawei Tong
  - Jia Cai
  - Zhiyong Li
  - Bo Wan
  - Lei Zhang
  - Tao Yang
  - Minwen Zhang
  - Linlin Yang
  - Yawen Yang
  - Wenjun Zeng
  - Bo Wang
  - Xiaofeng Wei
  - Xun Xu
  doi: 10.1093/database/baaa055
  id: doi:10.1093/database/baaa055
  journal: Database
  preferred: true
  title: 'CNSA: a data repository for archiving omics data'
  year: '2020'
- authors:
  - Weiwen Wang
  - Cong Tan
  - Ling Li
  - Xia Li
  - Lei Zhang
  - Xiaoqiang Li
  - Jieyu Wang
  - Ziyi He
  - Tao Yang
  - Kailong Ma
  - Qingjiang Hu
  - Wenzhen Yang
  - Zhiyong Li
  - Mingwen Zhang
  - Wensi Du
  - Fan Yang
  - Zhicheng Xu
  - Xizheng Ma
  - Jiawei Tong
  - Jia Cai
  - Cong Hua
  - Fengzhen Chen
  - Lijin You
  - Liang Li
  - Wenjun Zeng
  - Bo Wang
  - Xun Xu
  - Xiaofeng Wei
  doi: 10.1093/hr/uhaf036
  id: doi:10.1093/hr/uhaf036
  journal: Horticulture Research
  title: The China National GeneBank Sequence Archive (CNSA) 2024 update
  year: '2025'
synonyms:
- CNGBdb
- CNGB Sequence Archive
- CNSA
- CNGB Nucleotide Sequence Archive
---
# China National GeneBank DataBase

The China National GeneBank DataBase (CNGBdb) is the data platform of the China National GeneBank (CNGB) in Shenzhen. It archives, searches, analyzes and shares biological data, and follows data standards from INSDC, GA4GH and GGBN.

## CNGB Sequence Archive (CNSA)

CNSA is CNGBdb's archive for omics data. It accepts raw sequencing reads and their analysis results, organized as Project, Sample, Experiment, Run, Assembly and Variation records, plus metabolomic, single-cell, spatial transcriptomic and sequence data. Some projects link living samples held in the CNGB biobank to their sample records and data. As of 2024, CNSA held more than 16.3 PB of data supporting over 1,581 publications from more than 560 institutions, including the 10,000 Plant Genomes Project.

Public data can be downloaded over FTP, HTTPS and Aspera. Access to controlled data requires an application through CNGB Data Access (CDA). CNSA is not an INSDC member. The 2017 release announcement says submitters can choose to have their data synchronized to NCBI or ENA, but the 2020 and 2025 papers do not describe automatic exchange with INSDC. The 2025 update says programmatic APIs are planned but not yet available.

## Other Components

CNGBdb also offers search across literature, gene, protein, sequence, organism and variation sub-databases, which include data integrated from NCBI and EBI, as well as the Spatial Transcript Omics DataBase (STOmicsDB) for spatial transcriptomics.