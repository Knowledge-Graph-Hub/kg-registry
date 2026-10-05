---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: webadmin@discover.nci.nih.gov
  - contact_type: url
    value: https://discover.nci.nih.gov/contact.jsp
  label: NCI Developmental Therapeutics Branch, Genomics and Pharmacology Facility
creation_date: '2026-10-04T00:00:00Z'
description: CellMiner is a web-based suite from the Genomics and Pharmacology Facility
  of the NCI Developmental Therapeutics Branch for exploring molecular profiles and
  drug activity data of the NCI-60 cancer cell line panel. It integrates DNA (copy
  number, mutation, methylation), RNA (microarray, RNA-seq, microRNA), protein and
  compound activity data (DTP NCI-60 screen, HTS384 screen and NCI-ALMANAC combination
  scores), and provides processed and raw data downloads. Its companion application
  CellMinerCDB extends cross-database analysis to other cancer cell line pharmacogenomic
  datasets, including CCLE, GDSC, CTRP, PRISM and Project Achilles.
domains:
- biomedical
- cancer
- pharmacology
- pharmacogenomics
- genomics
homepage_url: https://discover.nci.nih.gov/cellminer/
id: cellminer
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: CellMiner
products:
- category: GraphicalInterface
  description: CellMiner web portal for querying NCI-60 gene transcript, DNA, protein
    and drug activity patterns, comparing patterns across cell lines and browsing cell
    line metadata.
  format: http
  id: cellminer.portal
  name: CellMiner Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_url: https://discover.nci.nih.gov/cellminer/
- category: Product
  description: CellMiner download page listing processed NCI-60 datasets (drug activity
    z-scores, copy number, exome mutations, methylation, transcript expression, microRNA,
    proteomics and histone marks) and raw datasets, each as a ZIP archive containing
    Excel workbooks plus documentation.
  format: http
  id: cellminer.downloads
  name: CellMiner Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_url: https://discover.nci.nih.gov/cellminer/loadDownload.do
- category: Product
  compression: zip
  description: Processed DTP NCI-60 compound activity data as z-scores of negative
    log10 GI50 values across the NCI-60 cell lines, provided as an Excel workbook with
    drug and cell line metadata documentation.
  format: xlsx
  id: cellminer.drug-zscore
  name: CellMiner DTP NCI-60 Drug Activity Z-Scores
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 8514360
  product_url: https://discover.nci.nih.gov/cellminer/download/processeddataset/DTP_NCI60_ZSCORE.zip
- category: Product
  compression: zip
  description: Raw DTP NCI-60 compound activity data (negative log10 GI50 values for
    all replicate experiments) across the NCI-60 cell lines, provided as an Excel workbook
    with drug and cell line metadata documentation.
  format: xlsx
  id: cellminer.drug-raw
  name: CellMiner DTP NCI-60 Raw Drug Activity
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 21446814
  product_url: https://discover.nci.nih.gov/cellminer/download/rawdataset/DTP_NCI60_RAW.zip
- category: GraphicalInterface
  description: CellMinerCDB web application for integrative cross-database genomics
    and pharmacogenomics analysis of cancer cell lines, combining NCI-60 data with
    CCLE, GDSC, CTRP, PRISM, Project Achilles, NCI-DTP SCLC, MD Anderson and NCATS
    datasets.
  format: http
  id: cellminer.cellminercdb
  name: CellMinerCDB
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_url: https://discover.nci.nih.gov/cellminercdb/
- category: ProgrammingInterface
  description: rcellminer Bioconductor package providing R functions to access, visualize
    and analyze NCI-60 molecular profiles and drug response data from CellMiner.
  format: r
  id: cellminer.rcellminer
  license:
    id: https://www.gnu.org/licenses/lgpl-3.0.html
    label: LGPL-3.0
  name: rcellminer R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  product_url: https://bioconductor.org/packages/release/bioc/html/rcellminer.html
- category: Product
  description: rcellminerData Bioconductor experiment data package containing the
    CellMiner NCI-60 molecular profiles and drug activity data used by rcellminer.
  format: r
  id: cellminer.rcellminerdata
  license:
    id: https://www.gnu.org/licenses/lgpl-3.0.html
    label: LGPL-3.0
  name: rcellminerData R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  product_url: https://bioconductor.org/packages/release/data/experiment/html/rcellminerData.html
- category: DocumentationProduct
  description: CellMiner dataset metadata page describing each drug, DNA, RNA and
    protein dataset, its platform, principal collaborators and processing method.
  format: http
  id: cellminer.dataset-metadata
  name: CellMiner Dataset Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  product_url: https://discover.nci.nih.gov/cellminer/datasets.do
- category: DocumentationProduct
  description: CellMiner release notes describing data and feature changes across
    CellMiner versions.
  format: http
  id: cellminer.release-notes
  name: CellMiner Release Notes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellminer
  product_url: https://discover.nci.nih.gov/cellminer/releaseNotes.do
publications:
- authors:
  - William C. Reinhold
  - Margot Sunshine
  - Hongfang Liu
  - Sudhir Varma
  - Kurt W. Kohn
  - Joel Morris
  - James Doroshow
  - Yves Pommier
  doi: 10.1158/0008-5472.CAN-12-1370
  id: doi:10.1158/0008-5472.CAN-12-1370
  journal: Cancer Research
  preferred: true
  title: 'CellMiner: A Web-Based Suite of Genomic and Pharmacologic Tools to Explore
    Transcript and Drug Patterns in the NCI-60 Cell Line Set'
  year: '2012'
- authors:
  - Vinodh N. Rajapakse
  - Augustin Luna
  - Mihoko Yamade
  - Lisa Loman
  - Sudhir Varma
  - Margot Sunshine
  - Francesco Iorio
  - Fabricio G. Sousa
  - Fathi Elloumi
  - Mirit I. Aladjem
  - Anish Thomas
  - Chris Sander
  - Kurt W. Kohn
  - Cyril H. Benes
  - Mathew Garnett
  - William C. Reinhold
  - Yves Pommier
  doi: 10.1016/j.isci.2018.11.029
  id: doi:10.1016/j.isci.2018.11.029
  journal: iScience
  title: CellMinerCDB for Integrative Cross-Database Genomics and Pharmacogenomics
    Analyses of Cancer Cell Lines
  year: '2018'
- authors:
  - Augustin Luna
  - Vinodh N. Rajapakse
  - Fabricio G. Sousa
  - Jianjiong Gao
  - Nikolaus Schultz
  - Sudhir Varma
  - William Reinhold
  - Chris Sander
  - Yves Pommier
  doi: 10.1093/bioinformatics/btv701
  id: doi:10.1093/bioinformatics/btv701
  journal: Bioinformatics
  title: 'rcellminer: exploring molecular profiles and drug response of the NCI-60
    cell lines in R'
  year: '2016'
synonyms:
- CellMinerCDB
- CellMiner NCI-60
taxon:
- NCBITaxon:9606
---
# CellMiner

CellMiner is a suite of web tools from the Genomics and Pharmacology Facility (GPF) of the Developmental Therapeutics Branch at the U.S. National Cancer Institute. It integrates the molecular and pharmacological data collected for the NCI-60 panel of human cancer cell lines, the cell lines used in the NCI Developmental Therapeutics Program (DTP) anti-cancer drug screen.

## Data

CellMiner covers DNA data (copy number from several aCGH and SNP platforms, exome sequencing mutations, DNA methylation), RNA data (Affymetrix, Agilent and RNA-seq transcript expression, microRNA arrays, transporter arrays), protein data (antibody arrays, SWATH mass spectrometry, cell surface markers, histone marks) and compound activity data (the DTP NCI-60 screen, the HTS384 screen and NCI-ALMANAC drug combination scores). Processed and raw datasets can be downloaded from the download page as ZIP archives of Excel workbooks with documentation.

## CellMinerCDB

CellMinerCDB is a companion Shiny application for cross-database analysis. It lets users compare molecular and drug response data from NCI-60 with other cancer cell line sets, including CCLE (Broad-MIT), GDSC (MGH-Sanger), CTRP, PRISM, Project Achilles, NCI-DTP small cell lung cancer lines, MD Anderson and NCATS datasets. The GPF also hosts specialized CellMinerCDB instances for small cell lung cancer, sarcoma and adrenocortical carcinoma.

## Programmatic Access

The rcellminer and rcellminerData Bioconductor packages provide CellMiner NCI-60 data and analysis functions in R.
