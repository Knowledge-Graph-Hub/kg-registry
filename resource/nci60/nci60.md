---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://dtp.cancer.gov/
  label: NCI Developmental Therapeutics Program (DTP)
creation_date: '2026-10-04T00:00:00Z'
description: The NCI-60 Human Tumor Cell Lines Screen is the National Cancer Institute
  Developmental Therapeutics Program's panel of 60 human cancer cell lines from nine
  tissue types (leukemia, melanoma and cancers of the lung, colon, brain, ovary, breast,
  prostate and kidney). Compounds identified by NSC number have been screened against
  the panel since 1990. DTP publishes growth inhibition endpoints (GI50, TGI, LC50,
  IC50), full concentration/response data and one-dose prescreen data for public NSC
  compounds, reported per experiment, with 71 current and former NCI-60 cell lines
  making up most of the data.
domains:
- biomedical
- cancer
- drug discovery
- high-throughput screening
- pharmacology
homepage_url: https://dtp.cancer.gov/discovery_development/nci-60/
id: nci60
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: NCI-60 Human Tumor Cell Lines Screen
products:
- category: GraphicalInterface
  description: DTP web pages describing the NCI-60 screen, its cell lines, screening
    methodology and compound submission process.
  format: http
  id: nci60.portal
  name: NCI-60 Screen Web Pages
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_url: https://dtp.cancer.gov/discovery_development/nci-60/
- category: Product
  compression: zip
  description: GI50 (50% growth inhibition) values for public NSC compounds across
    NCI-60 and other cell lines, one row per experiment, NSC, concentration range
    and cell line (DOWNLOAD NCI CELL LINE DATA, July 2026 release; about 401 MB uncompressed).
  format: csv
  id: nci60.gi50
  name: NCI-60 GI50 Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 39004593
  product_url: https://wiki.nci.nih.gov/download/attachments/147193864/GI50.zip
- category: Product
  compression: zip
  description: TGI (total growth inhibition) values for public NSC compounds across
    NCI-60 and other cell lines, per experiment (July 2026 release; about 396 MB uncompressed).
  format: csv
  id: nci60.tgi
  name: NCI-60 TGI Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 34477901
  product_url: https://wiki.nci.nih.gov/download/attachments/147193864/TGI.zip
- category: Product
  compression: zip
  description: LC50 (50% lethal concentration) values for public NSC compounds across
    NCI-60 and other cell lines, per experiment (July 2026 release; about 391 MB uncompressed).
  format: csv
  id: nci60.lc50
  name: NCI-60 LC50 Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 30570051
  product_url: https://wiki.nci.nih.gov/download/attachments/147193864/LC50.zip
- category: Product
  compression: zip
  description: IC50 values for public NSC compounds across NCI-60 and other cell lines,
    per experiment (July 2026 release; about 401 MB uncompressed).
  format: csv
  id: nci60.ic50
  name: NCI-60 IC50 Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 37078627
  product_url: https://wiki.nci.nih.gov/download/attachments/147193864/IC50.zip
- category: Product
  compression: zip
  description: Full concentration/response (percent growth) data for public NSC compounds
    tested in the five-dose NCI-60 assay, per experiment (July 2026 release; about
    2.37 GB uncompressed).
  format: csv
  id: nci60.doseresp
  name: NCI-60 Concentration/Response Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 347853412
  product_url: https://wiki.nci.nih.gov/download/attachments/147193864/DOSERESP.zip
- category: Product
  compression: zip
  description: One-concentration (prescreen) percent growth data for public NSC compounds
    across the NCI-60 panel (July 2026 release; about 470 MB uncompressed).
  format: csv
  id: nci60.oneconc
  name: NCI-60 One-Dose Prescreen Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 54777377
  product_url: https://wiki.nci.nih.gov/download/attachments/147193864/ONECONC.zip
- category: Product
  description: List of public NSC compound numbers covered by the NCI-60 data release.
  format: csv
  id: nci60.public-nscs
  name: NCI-60 Public NSC List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_file_size: 2574659
  product_url: https://wiki.nci.nih.gov/download/attachments/147193864/public_nscs.csv
- category: DocumentationProduct
  description: NCI DTP Data wiki page for the NCI-60 growth inhibition download, with
    background on the screen, file sizes, column definitions and links to previous
    releases.
  format: http
  id: nci60.download-docs
  name: NCI-60 Growth Inhibition Data Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nci60
  product_url: https://wiki.nci.nih.gov/spaces/NCIDTPdata/pages/147193864/NCI-60+Growth+Inhibition+Data
- category: Product
  compression: zip
  description: 'ZIP with two TSV files: Drug_target_reactome_pathway.tsv (611,655
    rows) and Drug_target_reactome_pathway_filtered.tsv (238,317 rows, parent pathways
    removed), with columns for expression dataset, drug name and STITCH ID, tissue,
    cell line, target UniProt ID and symbol, target class, pathway and pathway size.'
  dump_format: other
  format: tsv
  id: date.archive
  name: DATE Archive ZIP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: date
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: nci60
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  product_file_size: 7261526
  product_url: https://tatonettilab-resources.s3.amazonaws.com/syspharm/DATE.zip
- category: GraphicalInterface
  description: CellMiner web portal for querying NCI-60 gene transcript, DNA, protein
    and drug activity patterns, comparing patterns across cell lines and browsing
    cell line metadata.
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
    log10 GI50 values across the NCI-60 cell lines, provided as an Excel workbook
    with drug and cell line metadata documentation.
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
    all replicate experiments) across the NCI-60 cell lines, provided as an Excel
    workbook with drug and cell line metadata documentation.
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
publications:
- authors:
  - Robert H. Shoemaker
  doi: 10.1038/nrc1951
  id: doi:10.1038/nrc1951
  journal: Nature Reviews Cancer
  preferred: true
  title: The NCI60 human tumour cell line anticancer drug screen
  year: '2006'
synonyms:
- NCI-60
- NCI60
- NCI-60 Human Tumor Cell Lines Screen
- NCI 60 cell line screen
taxon:
- NCBITaxon:9606
---
# NCI-60 Human Tumor Cell Lines Screen

The NCI-60 screen is run by the Developmental Therapeutics Program (DTP) of the National Cancer Institute. It tests compounds against 60 human tumor cell lines drawn from leukemia, melanoma and cancers of the lung, colon, brain, ovary, breast, prostate and kidney. Compounds are identified by NSC number. Most NSC numbers are single small molecules, but some are mixtures, extracts or biological agents.

## Data

DTP releases growth inhibition data for public NSC compounds on the NCI DTP Data wiki. The July 2026 release has:

- **GI50, TGI, LC50 and IC50** endpoint files.
- **DOSERESP**, the full concentration/response data from the five-dose assay.
- **ONECONC**, the one-dose prescreen data.
- A list of the public NSC numbers.

Each file is a zipped CSV. Since 2021 the files report individual experiments (EXPID) rather than aggregates, with values to four decimal places. The release covers the 60 current panel lines, 11 former panel lines, and other lines assayed with the same protocol.

Molecular profiling data for the NCI-60 lines (gene expression, mutations, copy number, methylation and more) are served by CellMiner from the NCI Genomics and Pharmacology Facility. That tool is not described here.

## Notes

DTP does not state a license on these pages. The license above is inferred from federal authorship. The cell lines are described in Cellosaurus and can be requested from the DCTD Tumor Repository.