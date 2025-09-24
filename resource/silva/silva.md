---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: "silva@dsmz.de"
      - contact_type: url
        value: "https://www.arb-silva.de/contact"
    label: SILVA Team
creation_date: '2025-09-09T00:00:00Z'
description: SILVA is a comprehensive online resource for quality checked and aligned ribosomal RNA sequence data. It provides regularly updated datasets of aligned small (16S/18S, SSU) and large subunit (23S/28S, LSU) ribosomal RNA sequences for all three domains of life (Bacteria, Archaea and Eukarya). SILVA is a Global Core Biodata Resource and ELIXIR Core Data Resource, currently maintaining over 9.4 million SSU sequences in release 138.2.
domains:
- microbiology
- genomics
- biological systems
- organisms
- biomedical
homepage_url: https://www.arb-silva.de/
id: silva
last_modified_date: '2025-09-24T00:00:00Z'
layout: resource_detail
name: SILVA
products:
  - category: GraphicalInterface
    description: Web-based search interface for SILVA ribosomal RNA sequences with advanced filtering and taxonomic browsing capabilities
    format: http
    id: silva.search
    name: SILVA Search
    original_source:
      - silva
    product_url: https://www.arb-silva.de/search
  - category: GraphicalInterface
    description: Interactive browser for exploring SILVA taxonomic hierarchy and sequence data with phylogenetic context
    format: http
    id: silva.browser
    name: SILVA Browser
    original_source:
      - silva
    product_url: https://www.arb-silva.de/browser
  - category: ProcessProduct
    description: SILVA Incremental Aligner (SINA) for accurate alignment of ribosomal RNA sequences against curated reference alignments
    format: http
    id: silva.aligner
    name: SILVA Alignment, Classification and Tree Service (ACT)
    original_source:
      - silva
    product_url: https://www.arb-silva.de/aligner
  - category: Product
    description: Comprehensive release files including FASTA sequences, alignments, taxonomies, and ARB database files for SSU and LSU rRNA
    format: mixed
    id: silva.release_files
    name: SILVA Release Files
    original_source:
      - silva
    product_url: https://www.arb-silva.de/current-release
  - category: ProcessProduct
    description: TestPrime tool for in silico evaluation of PCR primer coverage and specificity against SILVA sequences
    format: http
    id: silva.testprime
    name: SILVA TestPrime
    original_source:
      - silva
    product_url: https://www.arb-silva.de/testprime
  - category: ProcessProduct
    description: TestProbe tool for in silico evaluation of hybridization probe coverage and specificity against SILVA sequences
    format: http
    id: silva.testprobe
    name: SILVA TestProbe
    original_source:
      - silva
    product_url: https://www.arb-silva.de/testprobe
  - category: Product
    description: ARB-formatted database files for phylogenetic analysis and sequence management in the ARB software environment
    format: mixed
    id: silva.arb_files
    name: SILVA ARB Files
    original_source:
      - silva
    product_url: https://www.arb-silva.de/arb-files
  - category: ProcessProduct
    description: SILVAngs pipeline for high-throughput analysis of ribosomal RNA gene amplicons from next-generation sequencing data
    format: http
    id: silva.ngs_pipeline
    name: SILVAngs
    original_source:
      - silva
    product_url: https://ngs.arb-silva.de/
publications:
  - authors:
      - Christian Quast
      - Elmar Pruesse
      - Pelin Yilmaz
      - Jan Gerken
      - Timmy Schweer
      - Pablo Yarza
      - Jörg Peplies
      - Frank Oliver Glöckner
    doi: "10.1093/nar/gks1219"
    id: "doi:10.1093/nar/gks1219"
    title: "The SILVA ribosomal RNA gene database project: improved data processing and web-based tools"
    year: "2013"
  - authors:
      - Pelin Yilmaz
      - Linda Wegener Parfrey
      - Pablo Yarza
      - Jan Gerken
      - Elmar Pruesse
      - Christian Quast
      - Timmy Schweer
      - Jörg Peplies
      - Wolfgang Ludwig
      - Frank Oliver Glöckner
    doi: "10.1093/nar/gkt1209"
    id: "doi:10.1093/nar/gkt1209"
    title: "The SILVA and 'All-species Living Tree Project (LTP)' taxonomic frameworks"
    year: "2014"
repository: https://github.com/epruesse/SINA
---
# SILVA

SILVA is a comprehensive online resource that provides quality-checked and aligned ribosomal RNA (rRNA) sequence data for phylogenetic analysis and microbial diversity studies. Developed and maintained by the SILVA Team at the Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures in Bremen, Germany, SILVA serves as a foundational resource for microbiology, ecology, and evolutionary biology research worldwide.

## Overview

SILVA offers regularly updated datasets of aligned small subunit (16S/18S, SSU) and large subunit (23S/28S, LSU) ribosomal RNA sequences spanning all three domains of life: Bacteria, Archaea, and Eukarya. The database is recognized as both a Global Core Biodata Resource and an ELIXIR Core Data Resource, reflecting its critical importance to the international research community.

## Key Features

### Comprehensive Coverage
The current release (138.2, July 2024) includes:
- **Over 9.4 million SSU sequences** with quality annotations
- **1.3 million LSU sequences** with comprehensive alignments
- **Complete taxonomic coverage** across Bacteria, Archaea, and Eukarya
- **Multiple quality filtering levels** (basic and strong) for different use cases

### Quality Control and Curation
SILVA implements rigorous quality control measures:
- **Manual curation** by expert taxonomists and bioinformaticians
- **Automated quality assessment** with clear rating systems
- **Alignment quality scoring** for every sequence
- **Phylogenetic consistency checking** across taxonomic assignments
- **Regular updates** incorporating new sequences and taxonomic revisions

### Advanced Alignment Technology
The SILVA Incremental Aligner (SINA) provides:
- **Reference-based alignment** using curated seed alignments
- **Phylogenetic placement** for accurate taxonomic assignment  
- **Quality metrics** for alignment assessment
- **Scalable processing** for large sequence datasets
- **Integration with ARB** phylogenetic analysis software

## Tools and Services

### Search and Browse
- **Advanced search interface** with taxonomic, sequence, and metadata filtering
- **Interactive browser** for exploring phylogenetic relationships
- **Export capabilities** in multiple formats (FASTA, ARB, etc.)

### Analysis Tools
- **TestPrime**: In silico PCR primer evaluation against SILVA sequences
- **TestProbe**: Hybridization probe coverage and specificity analysis
- **ACT (Alignment, Classification and Tree Service)**: Web-based sequence alignment and classification
- **SILVAngs**: High-throughput amplicon analysis pipeline for NGS data

### Data Products
- **Reference datasets** (Ref NR) with high-quality, non-redundant sequences
- **Comprehensive datasets** (Parc) including all processed sequences
- **ARB database files** for phylogenetic analysis
- **Taxonomic frameworks** compatible with major analysis platforms
- **Specialized formats** for QIIME2, DADA2, Kraken2, and other tools

## Applications and Use Cases

### Microbial Ecology
SILVA supports diverse ecological studies:
- **Environmental microbiome analysis** across terrestrial, aquatic, and host-associated systems
- **Biodiversity assessment** using standardized taxonomic frameworks
- **Community structure analysis** with phylogenetic context
- **Temporal and spatial dynamics** of microbial communities

### Phylogenetic Analysis
The database enables sophisticated evolutionary studies:
- **Large-scale phylogenetic reconstruction** across all domains of life
- **Molecular clock analyses** using curated alignments
- **Comparative genomics** with taxonomic context
- **Evolutionary relationship inference** for newly discovered organisms

### Clinical and Applied Microbiology
SILVA provides critical infrastructure for:
- **Pathogen identification** and classification
- **Antimicrobial resistance surveillance** with phylogenetic context
- **Probiotic strain characterization** and quality control
- **Food safety** and industrial microbiology applications

## Integration and Compatibility

SILVA maintains broad compatibility with the scientific ecosystem:
- **ARB software suite**: Native integration for phylogenetic analysis
- **QIIME2, DADA2**: Specialized database formats for amplicon analysis
- **Kraken2, BLAST**: Reference databases for sequence classification
- **RNAcentral**: Contribution as expert database for ribosomal RNA
- **LPSN integration**: Taxonomic consistency with prokaryotic nomenclature standards

## Data Access and Licensing

SILVA operates under the Creative Commons Attribution 4.0 International License, enabling:
- **Free academic use** for research and educational purposes
- **Commercial licensing** available for industrial applications
- **Multiple download formats** including FTP access
- **API access** through integrated web services
- **Version control** with archived releases for reproducibility

## Community and Support

The SILVA project maintains active engagement with the research community:
- **Regular workshops** and training sessions
- **Comprehensive documentation** and tutorials
- **User support** through dedicated help channels
- **Collaborative development** with international partners
- **Integration with DSMZ Digital Diversity** platform for cross-database searches

SILVA's commitment to data quality, accessibility, and community engagement has established it as an indispensable resource for ribosomal RNA-based research, supporting thousands of publications and serving millions of users worldwide in their investigations of microbial diversity and evolution.