---
activity_status: inactive
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ibioinformatics.org/
  label: Institute of Bioinformatics
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.hopkinsmedicine.org/profiles/details/akhilesh-pandey
  label: Johns Hopkins University Pandey Lab
- category: Individual
  label: Akhilesh Pandey
  orcid: 0000-0002-7944-3070
creation_date: '2025-10-30T00:00:00Z'
description: The Human Protein Reference Database (HPRD) was a comprehensive, manually
  curated collection of information on human proteins, including protein-protein interactions,
  post-translational modifications (PTMs), enzyme-substrate relationships, subcellular
  localization, tissue expression, and disease associations. Developed through collaboration
  between the Institute of Bioinformatics in Bangalore, India and Johns Hopkins University
  in Baltimore, USA, HPRD contained over 20,000 protein entries with more than 36,500
  unique protein-protein interactions and 18,000 PTMs before being discontinued. The
  database served as a major resource for the human proteome from 2003 to approximately
  2010.
domains:
- biomedical
- proteomics
- biological systems
- systems biology
homepage_url: http://www.hprd.org/
id: hprd
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: HPRD
products:
- category: Product
  description: HPRD protein-protein interaction data in PSI-MITAB format, now archived
    and available through iRefIndex
  format: psi_mi_mitab
  id: hprd.ppi.data
  name: HPRD Protein-Protein Interactions
  original_source:
  - hprd
  product_url: http://www.hprd.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-19_ HTTP 503 error when
    accessing file
  - Original HPRD website is no longer accessible. Data has been archived in iRefIndex
    and other interaction databases.
  - 'File was not able to be retrieved when checked on 2025-11-21: HTTP 503 error
    when accessing file'
- category: DocumentationProduct
  description: HPRD data in XML format for programmatic access
  id: hprd.xml.download
  name: HPRD XML Data Download
  original_source:
  - hprd
  product_url: http://www.hprd.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-19_ HTTP 503 error when
    accessing file
  - Original HPRD website is no longer accessible. Data may be available through archive.org
    or integrated databases.
  - 'File was not able to be retrieved when checked on 2025-11-21: HTTP 503 error
    when accessing file'
- category: DocumentationProduct
  description: HPRD data in tab-delimited format for programmatic access
  id: hprd.tsv.download
  name: HPRD Tab-Delimited Data Download
  original_source:
  - hprd
  product_url: http://www.hprd.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-19_ HTTP 503 error when
    accessing file
  - Original HPRD website is no longer accessible. Data may be available through archive.org
    or integrated databases.
  - 'File was not able to be retrieved when checked on 2025-11-21: HTTP 503 error
    when accessing file'
- category: GraphicalInterface
  description: PhosphoMotif Finder tool for identifying kinase/phosphatase substrate
    and binding motifs
  format: http
  id: hprd.phosphomotif.finder
  name: HPRD PhosphoMotif Finder
  original_source:
  - hprd
  product_url: http://www.hprd.org/
  warnings:
  - Original HPRD website is no longer accessible.
- category: GraphicalInterface
  description: GenProt Viewer for integrated genomic, transcriptomic and proteomic
    view of the human genome
  format: http
  id: hprd.genprot.viewer
  name: GenProt Viewer
  original_source:
  - hprd
  product_url: http://www.genprot.org/
  warnings:
  - GenProt website is no longer accessible.
- category: Product
  description: Historical consolidated protein interaction index in PSI-MITAB 2.5
    format aggregating data from BIND, BioGrid, DIP, HPRD, IntAct, MINT, MPact, MPPI
    and OPHID
  format: psi_mi_mitab
  id: irefindex.database
  name: iRefIndex Database
  original_source:
  - bind
  - biogrid
  - dip
  - hprd
  - intact
  - mint
publications:
- authors:
  - Peri S
  - Navarro JD
  - Amanchy R
  - Kristiansen TZ
  - Jonnalagadda CK
  - Surendranath V
  - Niranjan V
  - Muthusamy B
  - Gandhi TK
  - Gronborg M
  - et al.
  doi: 10.1101/gr.1680803
  id: https://doi.org/10.1101/gr.1680803
  journal: Genome Research
  preferred: true
  title: Development of human protein reference database as an initial platform for
    approaching systems biology in humans
  year: '2003'
- authors:
  - Mishra GR
  - Suresh M
  - Kumaran K
  - Kannabiran N
  - Suresh S
  - Bala P
  - Shivakumar K
  - Anuradha N
  - Reddy R
  - Raghavan TM
  - Menon S
  - Hanumanthu G
  - Gupta M
  - Upendran S
  - Gupta S
  - Mahesh M
  - Jacob B
  - Mathew P
  - Chatterjee P
  - Arun KS
  - Sharma S
  - Chandrika KN
  - Deshpande N
  - Palvankar K
  - Raghavnath R
  - Krishnakanth R
  - Karathia H
  - Rekha B
  - Nayak R
  - Vishnupriya G
  - Kumar HG
  - Nagini M
  - Kumar GS
  - Jose R
  - Deepthi P
  - Mohan SS
  - Gandhi TK
  - Harsha HC
  - Deshpande KS
  - Sarker M
  - Prasad TS
  - Pandey A
  doi: 10.1093/nar/gkj141
  id: https://doi.org/10.1093/nar/gkj141
  journal: Nucleic Acids Research
  title: Human protein reference database—2006 update
  year: '2006'
- authors:
  - Peri S
  - Navarro JD
  - Kristiansen TZ
  - Amanchy R
  - Surendranath V
  - Muthusamy B
  - Gandhi TK
  - Chandrika KN
  - Deshpande N
  - Suresh S
  - Rashmi BP
  - Shanker K
  - Padma N
  - Niranjan V
  - Harsha HC
  - Talreja N
  - Vrushabendra BM
  - Ramya MA
  - Yatish AJ
  - Joy M
  - Shivashankar HN
  - Kavitha MP
  - Menezes M
  - Choudhury DR
  - Ghosh N
  - Saravana R
  - Chandran S
  - Mohan S
  - Jonnalagadda CK
  - Prasad CK
  - Kumar-Sinha C
  - Deshpande KS
  - Pandey A
  doi: 10.1093/nar/gkh070
  id: https://doi.org/10.1093/nar/gkh070
  journal: Nucleic Acids Research
  title: Human protein reference database as a discovery resource for proteomics
  year: '2004'
- authors:
  - Gandhi TKB
  - Zhong J
  - Mathivanan S
  - Karthick L
  - Chandrika KN
  - Mohan SS
  - Sharma S
  - Pinkert S
  - Nagaraju S
  - Periaswamy B
  - Mishra G
  - Nandakumar K
  - Shen B
  - Deshpande N
  - Nayak R
  - Sarker M
  - Boeke JD
  - Parmigiani G
  - Schultz J
  - Bader JS
  - Pandey A
  doi: 10.1038/ng1747
  id: https://doi.org/10.1038/ng1747
  journal: Nature Genetics
  title: Analysis of the human protein interactome and comparison with yeast, worm
    and fly interaction datasets
  year: '2006'
taxon:
- NCBITaxon:9606
---
# HPRD - Human Protein Reference Database

**Note: HPRD is no longer actively maintained. The website at www.hprd.org is currently inaccessible. HPRD data has been archived and incorporated into other protein interaction databases such as iRefIndex, IntAct, BioGRID, and STRING.**

## Overview

The Human Protein Reference Database (HPRD) was a pioneering resource in proteomics that provided comprehensive, manually curated information about human proteins. Developed through an international collaboration between the Institute of Bioinformatics in Bangalore, India and the Pandey Laboratory at Johns Hopkins University in Baltimore, USA, HPRD served as a major resource for understanding the human proteome and protein networks from 2003 to approximately 2010.

### Key Statistics (Final Release)

- **20,097 protein entries** including 1,587 isoforms
- **36,500+ unique protein-protein interactions** (one of the largest manually curated collections at the time)
- **18,000+ post-translational modifications** across 26 different types
- **3,343 enzyme-substrate relationships**
- **478 protein domains and motifs**

### Data Types Annotated

1. **Protein-Protein Interactions (PPIs)**
   - Over 36,500 unique interactions
   - Categorized by experimental method:
     - In vivo experiments (19,175 interactions)
     - In vitro experiments (11,114 interactions)
     - Yeast two-hybrid (1,813 interactions)
   - Links to primary literature sources

2. **Post-Translational Modifications (PTMs)**
   - 18,000+ manually curated PTMs
   - 26 different types of modifications
   - Major categories:
     - Phosphorylation (63% of PTM data, 5,011 events)
     - Glycosylation (1,132 events)
     - Proteolytic cleavage
     - Disulfide bridges
     - Others (acetylation, methylation, ubiquitination, etc.)

3. **Protein Features**
   - Domain architecture
   - Protein motifs
   - Subcellular localization (including 489 nucleolar proteins and 270 secreted proteins)
   - Tissue expression patterns
   - Enzyme-substrate relationships

4. **Disease Associations**
   - Links to OMIM (Online Mendelian Inheritance in Man)
   - Disease-related protein annotations

### Special Features

**PhosphoMotif Finder**: A tool for identifying known kinase/phosphatase substrate and binding motifs based on literature-curated data. Unlike prediction tools, it reported the presence of experimentally validated motifs in query sequences.

**GenProt Viewer**: An integrated browser (www.genprot.org) that provided:
- Genomic, transcriptomic, and proteomic views of the human genome
- SNP mapping and annotations
- Transcript information from RefSeq
- Integration with Haploview for population haplotype patterns
- Peptide sequence data from PeptideAtlas and PRIDE repositories

**Pathway Integration**: Curated signaling pathways visualized through GenMAPP (Gene Microarray Pathway Profiler), showing:
- Protein-protein interactions in pathway context
- Post-translational modifications
- Protein shuttling between subcellular compartments
- Enzymatic activity regulation
- mRNA regulation

### Data Formats

HPRD data was available in multiple formats:
- **PSI-MI format**: Protein-protein interaction data in PSI-MI (Proteomics Standards Initiative - Molecular Interactions) level 2.5 format
- **XML format**: Comprehensive database exports
- **Tab-delimited format**: Simple text-based data files
- **Web interface**: Interactive browsing and search capabilities

### Integration and Legacy

HPRD was integrated with:
- **Human Proteinpedia**: A community portal for sharing human protein data
- **RefSeq**: NCBI reference sequences
- **Swiss-Prot**: UniProt protein knowledge base
- **OMIM**: Disease and gene associations
- **Entrez Gene**: NCBI gene database

HPRD data has been archived and incorporated into several active databases:
- **iRefIndex**: Historical consolidated protein interaction index
- **IntAct**: Molecular interaction database
- **BioGRID**: Biological General Repository for Interaction Datasets
- **STRING**: Protein-protein interaction networks

### Search Capabilities

HPRD supported multiple query options:
- Gene symbols
- RefSeq accession numbers
- OMIM IDs
- Swiss-Prot IDs
- HPRD IDs
- Entrez Gene IDs
- BLAST search for sequence-based queries
- Multiple parameter searches

### Curation Process

All protein annotations in HPRD were:
- **Manually curated** by expert biologists
- **Literature-derived** from published scientific papers
- **Evidence-based** with experimental support
- **Linked to primary sources** with PubMed citations

### Impact on Proteomics

HPRD made significant contributions to:
- Systems biology approaches in human proteomics
- Understanding of human protein interaction networks
- Development of protein interaction databases
- Standardization of protein interaction data formats (PSI-MI)
- Integration of genomic, transcriptomic, and proteomic data

### License

HPRD data was available for:
- **Academic use**: Freely accessible and usable
- **Commercial use**: Required a license

Human Proteinpedia content was freely available for anyone to download and use.

## Current Status

HPRD is **no longer actively maintained**. The primary website (www.hprd.org) and associated GenProt Viewer (www.genprot.org) are currently inaccessible. However, the valuable data generated by HPRD has been preserved:

- **iRefIndex** maintains HPRD interaction data in their historical consolidated index
- **IntAct**, **BioGRID**, and **STRING** have incorporated HPRD interactions
- **Archive.org** may have snapshots of the original website
- Publications describing HPRD remain available and continue to be cited

For current protein-protein interaction data, users are encouraged to consult:
- IntAct (www.ebi.ac.uk/intact/)
- BioGRID (thebiogrid.org)
- STRING (string-db.org)
- HuRI - Human Reference Interactome (www.interactome-atlas.org)

## Historical Significance

HPRD represented a landmark effort in manual curation of human protein data and set standards for:
- Quality of manually curated protein interaction data
- Integration of multiple data types (interactions, PTMs, localization, expression)
- Community engagement through feedback mechanisms
- Open data sharing in proteomics research

The database's approach to systematic annotation and its emphasis on literature-derived evidence influenced the development of subsequent protein databases and resources in the proteomics field.