---
activity_status: active
category: DataSource
creation_date: '2025-11-13T00:00:00Z'
description: EPSD (Eukaryotic Phosphorylation Site Database) is a comprehensive database
  that curates and annotates experimentally identified protein phosphorylation sites
  across eukaryotic species. Version 2.0 contains 2,769,163 phosphorylation sites
  in 362,707 phosphoproteins from 223 eukaryotic species (95 animals, 20 protists,
  61 plants, 48 fungi). The database integrates data from high-throughput phosphoproteomic
  studies and 10 public databases, providing detailed annotations including phosphopeptide
  sequences, localization probability scores, cell/tissue sources, and primary references.
  EPSD 2.0 features 88,074 functional annotations for 32,762 phosphorylation sites,
  covering 58 types of downstream effects on phosphoproteins and 107 regulatory impacts
  on biological processes. For eight model organisms (human, mouse, rat, Drosophila,
  C. elegans, Arabidopsis, S. pombe, S. cerevisiae), phosphoproteins are meticulously
  annotated with information from 100 external resources across 15 aspects including
  kinase/phosphatase regulators, 3D structures, physicochemical characteristics, genomic
  variations, functional descriptions, protein domains, molecular interactions, drug-target
  associations, disease data, orthologs, transcript expression, proteomics, subcellular
  localization, and regulatory pathways. EPSD 2.0 represents a 2.5-fold increase in
  data volume compared to version 1.0 and provides intrinsic disorder propensity and
  surface accessibility calculations for phosphorylation sites. The database supports
  advanced search options including substrate search, peptide search, batch search,
  BLAST search, and browse by species functionality.
domains:
- genomics
- proteomics
homepage_url: https://epsd.biocuckoo.cn
id: epsd
infores_id: epsd
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: Eukaryotic Phosphorylation Site Database 2.0
products:
- category: Portal
  description: Main web portal for EPSD 2.0 providing search, browse, and visualization
    of protein phosphorylation sites across 223 eukaryotic species with functional
    annotations
  format: http
  id: epsd.portal
  name: EPSD 2.0 Portal
  original_source:
  - epsd
  product_url: https://epsd.biocuckoo.cn
  warnings:
  - File was not able to be retrieved when checked on 2025-11-13_ Error connecting
    to URL_ HTTPSConnectionPool(host='epsd.biocuckoo.cn', port=443)_ Max retries exceeded
    with url_ / (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ certificate has expired (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-17: Error connecting
    to URL: HTTPSConnectionPool(host=''epsd.biocuckoo.cn'', port=443): Max retries
    exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED]
    certificate verify failed: certificate has expired (_ssl.c:1017)'')))'
- category: Browser
  description: Browse phosphorylation sites by species across 223 eukaryotes including
    95 animals, 20 protists, 61 plants, and 48 fungi
  format: http
  id: epsd.browse
  name: EPSD Browse by Species
  original_source:
  - epsd
  product_url: https://epsd.biocuckoo.cn
  warnings:
  - File was not able to be retrieved when checked on 2025-11-13_ Error connecting
    to URL_ HTTPSConnectionPool(host='epsd.biocuckoo.cn', port=443)_ Max retries exceeded
    with url_ / (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ certificate has expired (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-17: Error connecting
    to URL: HTTPSConnectionPool(host=''epsd.biocuckoo.cn'', port=443): Max retries
    exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED]
    certificate verify failed: certificate has expired (_ssl.c:1017)'')))'
- category: Search
  description: Advanced search interface supporting substrate search, peptide search,
    batch search, BLAST search, and multi-condition queries
  format: http
  id: epsd.search
  name: EPSD Advanced Search
  original_source:
  - epsd
  product_url: https://epsd.biocuckoo.cn
  warnings:
  - File was not able to be retrieved when checked on 2025-11-13_ Error connecting
    to URL_ HTTPSConnectionPool(host='epsd.biocuckoo.cn', port=443)_ Max retries exceeded
    with url_ / (Caused by SSLError(SSLCertVerificationError(1, '[SSL_ CERTIFICATE_VERIFY_FAILED]
    certificate verify failed_ certificate has expired (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-17: Error connecting
    to URL: HTTPSConnectionPool(host=''epsd.biocuckoo.cn'', port=443): Max retries
    exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, ''[SSL: CERTIFICATE_VERIFY_FAILED]
    certificate verify failed: certificate has expired (_ssl.c:1017)'')))'
- category: Download
  description: Download page for complete phosphorylation site datasets and annotation
    data from EPSD 2.0
  format: http
  id: epsd.download
  name: EPSD Data Download
  original_source:
  - epsd
  product_url: https://epsd.biocuckoo.cn/Download.php
  secondary_source: []
  warnings:
  - File was not able to be retrieved when checked on 2025-11-13_ Error connecting
    to URL_ HTTPSConnectionPool(host='epsd.biocuckoo.cn', port=443)_ Max retries exceeded
    with url_ /Download.php (Caused by SSLError(SSLCertVerificationError(1, '[SSL_
    CERTIFICATE_VERIFY_FAILED] certificate verify failed_ certificate has expired
    (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2025-11-17: Error connecting
    to URL: HTTPSConnectionPool(host=''epsd.biocuckoo.cn'', port=443): Max retries
    exceeded with url: /Download.php (Caused by SSLError(SSLCertVerificationError(1,
    ''[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has
    expired (_ssl.c:1017)'')))'
- category: GraphicalInterface
  description: Interactive web interface for exploring and visualizing kinase-substrate
    interactions
  format: http
  id: kinace.portal
  name: KinAce Web Portal
  original_source:
  - phosphositeplus
  - iptmnet
  - uniprot
  - epsd
  - kinhub
  - coralkinome
  - darkkinasekb
  - hgnc
  - kegg
  - interpro
  product_url: https://kinace.kinametrix.com/
  secondary_source:
  - kinace
publications:
- id: PMID:40581078
- id: PMID:32008039
synonyms:
- EPSD
- Eukaryotic phosphorylation site database
- EPSD 2.0
---
# Eukaryotic Phosphorylation Site Database 2.0

## Overview

The Eukaryotic Phosphorylation Site Database (EPSD) is a comprehensive resource for protein phosphorylation data across eukaryotic species, providing experimentally validated phosphorylation sites with detailed functional annotations. Originally released in 2019 as EPSD 1.0, the database has undergone significant expansion in version 2.0 (published July 2025) to become one of the largest and most extensively annotated phosphorylation databases available.

## Data Content and Coverage

EPSD 2.0 contains **2,769,163 experimentally identified phosphorylation sites** occurring on **362,707 phosphoproteins** from **223 eukaryotic species**, representing a 71% increase in phosphorylation sites compared to version 1.0. The species coverage includes:

- **95 animals** (including human, mouse, rat, Drosophila, C. elegans)
- **20 protists**
- **61 plants** (including Arabidopsis thaliana)
- **48 fungi** (including S. cerevisiae, S. pombe)

Among all phosphorylation sites, the database contains:
- 1,930,151 (69.70%) phosphoserine (pS) residues
- 638,944 (23.07%) phosphothreonine (pT) residues
- 200,020 (7.22%) phosphotyrosine (pY) residues
- Additional sites on other residues including histidine

The database encompasses **3,364,760 phosphopeptides** with their primary references, preserving the initial peptides detected via mass spectrometry along with cell/tissue origins when available.

## Functional Annotations

A distinguishing feature of EPSD 2.0 is its comprehensive functional annotation:

- **88,074 functional downstream events** annotated for **32,762 phosphorylation sites**
- **58 categories** related to protein function effects (e.g., enzymatic activity, molecular association, subcellular localization)
- **107 categories** about biological process impacts (e.g., cell growth, disease progression, autophagy)

For eight model organisms (human, mouse, rat, Drosophila melanogaster, Caenorhabditis elegans, Arabidopsis thaliana, Schizosaccharomyces pombe, and Saccharomyces cerevisiae), EPSD 2.0 provides multilayer annotations integrated from **100 external resources** covering:

- Kinase/phosphatase regulators
- Transcription regulators
- Three-dimensional protein structures (PDB and AlphaFold)
- Physicochemical characteristics
- Genomic variations
- Functional descriptions
- Protein domains
- Molecular interactions (protein-protein interactions)
- Drug-target associations
- Disease-related data
- Orthologs across species
- Transcript expression levels
- Proteomics data
- Subcellular localization
- Regulatory pathways

## Data Collection and Quality

EPSD 2.0 data is derived from multiple sources:

- **873,718 new phosphorylation sites** from **575 high-throughput phosphoproteomic studies** collected from PubMed literature
- Integration with **EPSD 1.0** (1,616,804 sites in 209,326 proteins from 68 species)
- **362,190 additional sites** from 10 public databases (PhosphoSitePlus, dbPTM, UniProt, PhosPhAt, BioGRID, RegPhos, iPTMnet, Plant PTM Viewer, Pf-Phospho, Scop3P)

All phosphorylation sites are mapped to UniProt reference sequences with exact position information. For sites from high-throughput experiments, localization probability (LP) scores are provided and classified into four classes:
- Class I: LP > 0.75
- Class II: 0.50 < LP ≤ 0.75
- Class III: 0.25 ≤ LP ≤ 0.50
- Class IV: LP < 0.25

## Bioinformatic Features

EPSD 2.0 provides several computational analyses for each phosphorylation site:

- **Disorder propensity** calculated by IUPred3 (phosphorylation sites are predominantly situated in intrinsically disordered regions)
- **Surface accessibility** calculated by NetSurfP-3.0 (residues with higher surface accessibility are more likely to be phosphorylated)
- **3D structure visualization** using 3Dmol.js with phosphorylation sites highlighted on experimental structures (PDB) or predicted structures (AlphaFold)

## Database Interface and Search Functions

The EPSD 2.0 web portal offers multiple search and browse options:

- **Substrate Search**: Search by protein name, gene name, UniProt ID, EPSD ID, or species
- **Peptide Search**: Search for phosphopeptides (e.g., "KKpTLCGTPNYIAPEVLSK" where "p" indicates phosphorylated residue)
- **Advanced Search**: Multiple condition queries for precise searches
- **Batch Search**: Line-by-line input of multiple search terms
- **BLAST Search**: Sequence similarity search to identify identical or homologous proteins
- **Browse by Species**: Navigate through all 223 supported eukaryotic species

Each protein entry displays:
- Basic information (UniProt ID, gene name, organism, NCBI taxa ID)
- 3D structure with highlighted phosphorylation sites
- Comprehensive list of all phosphorylation sites with disorder/accessibility predictions
- Detailed phosphopeptide information with LP scores and references
- Functional annotations and downstream effects
- Integrated annotations across 15 categories

## Applications and Impact

EPSD 2.0 serves multiple research communities:

- **Phosphorylation research**: Comprehensive catalog of experimentally validated sites
- **Kinase-substrate relationships**: Identification of upstream kinases and downstream effects
- **Machine learning**: Training data for phosphorylation site predictors (e.g., GPS 6.0 developed using EPSD data)
- **Disease research**: Understanding aberrant phosphorylation in cancer, neurodegeneration, and cardiovascular disorders
- **Drug discovery**: Identifying phosphorylation-related therapeutic targets
- **Comparative phosphoproteomics**: Cross-species analysis of phosphorylation patterns

The database demonstrates that 71.87% of phosphoproteins are modified at multiple sites, highlighting multisite phosphorylation as a dominant regulatory mechanism.

## Maintenance and Updates

EPSD 2.0 is actively maintained by the CUCKOO Workgroup at Huazhong University of Science and Technology, China, led by Professor Yu Xue. The database was last updated on November 1, 2025, and is regularly maintained with:

- Continuous collection of newly reported phosphorylation sites from literature
- Expansion of functional annotations through literature review
- Integration of additional external resources
- Updates to structural data and annotations

The total database size is approximately 36.2 GB, representing a 2.5-fold increase compared to EPSD 1.0 (14.1 GB).

## Data Access and Download

All phosphorylation sites and annotation datasets in EPSD 2.0 are freely accessible for download at https://epsd.biocuckoo.cn/Download.php. The database has been submitted to Database Commons at the National Genomics Data Center (NGDC), China National Center for Bioinformation (CNCB), and is publicly accessible.

## Technical Details

- **Database identifiers**: Each phosphoprotein receives an automatically generated EPSD ID (EP-) with UniProt accession as alternative identifier
- **Primary references**: PubMed IDs provided for all sites with experimental evidence
- **Data format**: Structured data with comprehensive metadata
- **API access**: Available through the download portal
- **Updates**: Regular maintenance with last update November 1, 2025

## Related Resources

EPSD 2.0 integrates and complements data from multiple phosphorylation databases including PhosphoSitePlus, dbPTM, UniProt, PhosPhAt, iPTMnet, and others, providing one of the most comprehensive views of the eukaryotic phosphoproteome. The database also supports the GPS (Group-based Prediction System) 6.0 web server for kinase-specific phosphorylation site prediction.