---
activity_status: orphaned
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: pandey.akhilesh@mayo.edu
  label: Akhilesh Pandey
creation_date: '2026-10-04T00:00:00Z'
description: The Human Proteome Map (HPM) is a mass spectrometry-based draft map of
  the human proteome from Johns Hopkins University and the Institute of Bioinformatics,
  Bangalore. It reports protein expression from over 290,000 non-redundant peptide
  identifications covering products of more than 17,000 human genes across 30 histologically
  normal tissues and cell types (17 adult tissues, 7 fetal tissues and 6 primary hematopoietic
  cells). The raw data are deposited in PRIDE as PXD000561. The portal has not been
  updated since its 2014 release and some of its pages are broken.
domains:
- proteomics
- anatomy and development
- biomedical
homepage_url: http://www.humanproteomemap.org/
id: human-proteome-map
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: Human Proteome Map
products:
- category: GraphicalInterface
  description: HPM web portal for querying protein and peptide expression across adult
    and fetal tissues and hematopoietic cells.
  format: http
  id: human-proteome-map.portal
  name: Human Proteome Map Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  product_url: http://www.humanproteomemap.org/query.php
  warnings:
  - The HPM portal pages served injected spam links (unrelated escort and shop sites)
    when checked on 2026-10-04, which suggests the site is compromised. Open it with
    care.
  - The Browse (browse.html) and Spectral Library (spectral_library.html) pages linked
    from the portal returned HTTP 404 when checked on 2026-10-04.
- category: Product
  description: Request form for HPM data downloads. Academic users must declare non-commercial
    use and agree not to redistribute the data; commercial users must request a license.
  format: http
  id: human-proteome-map.download
  name: Human Proteome Map Data Download Request
  original_source:
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  product_url: http://www.humanproteomemap.org/download.php
  warnings:
  - The HPM portal pages served injected spam links (unrelated escort and shop sites)
    when checked on 2026-10-04, which suggests the site is compromised. Open it with
    care.
- category: Product
  description: Raw LC-MS/MS data for the draft map of the human proteome, deposited
    in the PRIDE Archive as PXD000561 (about 2,200 Thermo RAW files from LTQ Orbitrap
    Elite and Velos instruments, with Proteome Discoverer MSF result files, SDRF sample
    metadata and a README).
  format: mixed
  id: human-proteome-map.raw-data
  name: Human Proteome Map Raw Data (PXD000561)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  product_url: https://ftp.pride.ebi.ac.uk/pride/data/archive/2014/04/PXD000561/
- category: GraphicalInterface
  description: Expression browser data and source code showing tissue-specific expression
    of dark kinases using GTEx RNA-seq and Human Proteome Map data with kinome-wide
    comparisons. The hosted Shiny application formerly at expression.darkkinome.org
    has been retired; the underlying data and code remain available in this GitHub
    repository.
  format: http
  id: darkkinasekb.expression
  name: DKK Expression Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://github.com/IDG-Kinase/kinase_expression
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
publications:
- authors:
  - Min-Sik Kim
  - Sneha M. Pinto
  - Derese Getnet
  - Raja Sekhar Nirujogi
  - Srikanth S. Manda
  - Raghothama Chaerkady
  - Anil K. Madugundu
  - Dhanashree S. Kelkar
  - Ruth Isserlin
  - Shobhit Jain
  - Joji K. Thomas
  - Babylakshmi Muthusamy
  - Pamela Leal-Rojas
  - Praveen Kumar
  - Nandini A. Sahasrabuddhe
  - Lavanya Balakrishnan
  - Jayshree Advani
  - Bijesh George
  - Santosh Renuse
  - Lakshmi Dhevi N. Selvan
  - Arun H. Patil
  - Vishalakshi Nanjappa
  - Aneesha Radhakrishnan
  - Samarjeet Prasad
  - Tejaswini Subbannayya
  - Rajesh Raju
  - Manish Kumar
  - Sreelakshmi K. Sreenivasamurthy
  - Arivusudar Marimuthu
  - Gajanan J. Sathe
  - Sandip Chavan
  - Keshava K. Datta
  - Yashwanth Subbannayya
  - Apeksha Sahu
  - Soujanya D. Yelamanchi
  - Savita Jayaram
  - Pavithra Rajagopalan
  - Jyoti Sharma
  - Krishna R. Murthy
  - Nazia Syed
  - Renu Goel
  - Aafaque A. Khan
  - Sartaj Ahmad
  - Gourav Dey
  - Keshav Mudgal
  - Aditi Chatterjee
  - Tai-Chung Huang
  - Jun Zhong
  - Xinyan Wu
  - Patrick G. Shaw
  - Donald Freed
  - Muhammad S. Zahari
  - Kanchan K. Mukherjee
  - Subramanian Shankar
  - Anita Mahadevan
  - Henry Lam
  - Christopher J. Mitchell
  - Susarla Krishna Shankar
  - Parthasarathy Satishchandra
  - John T. Schroeder
  - Ravi Sirdeshmukh
  - Anirban Maitra
  - Steven D. Leach
  - Charles G. Drake
  - Marc K. Halushka
  - T. S. Keshava Prasad
  - Ralph H. Hruban
  - Candace L. Kerr
  - Gary D. Bader
  - Christine A. Iacobuzio-Donahue
  - Harsha Gowda
  - Akhilesh Pandey
  doi: 10.1038/nature13302
  id: doi:10.1038/nature13302
  journal: Nature
  preferred: true
  title: A draft map of the human proteome
  year: '2014'
synonyms:
- HPM
- Draft map of the human proteome
taxon:
- NCBITaxon:9606
---
# Human Proteome Map

The Human Proteome Map (HPM) presents the results of the draft map of the human proteome project (Kim et al., Nature 2014), led by Akhilesh Pandey's group at Johns Hopkins University with the Institute of Bioinformatics, Bangalore. Samples from 30 histologically normal human tissues and primary cells were analyzed by high-resolution Fourier transform mass spectrometry on Orbitrap instruments.

The portal reports direct evidence of translation for products of over 17,000 genes, more than 84% of annotated human protein-coding genes, from over 290,000 non-redundant peptides.

## Access

- **Portal:** query interface at http://www.humanproteomemap.org/query.php.
- **Processed data:** available by request through the download form. Academic use is non-commercial with no redistribution; commercial users must request a license.
- **Raw data:** PRIDE Archive project [PXD000561](https://www.ebi.ac.uk/pride/archive/projects/PXD000561).

## Status

When checked on 2026-10-04, the portal still responded, but its pages carried injected spam links and its Browse and Spectral Library pages returned HTTP 404. The PRIDE deposition is the stable copy of the raw data.