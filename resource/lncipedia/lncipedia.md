---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: LncIPedia is a comprehensive public database for human long non-coding RNA (lncRNA) sequences and annotations, containing manually curated literature and detailed transcript information.
domains:
  - genomics
  - literature
id: lncipedia
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
name: LncIPedia
homepage_url: https://lncipedia.org/
taxon:
  - NCBITaxon:9606
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://lncipedia.org/
    label: LncIPedia Team
publications:
  - id: PMID:30371849
    category: Publication
    preferred: true
  - id: PMID:25378313
    category: Publication
  - id: PMID:23042674
    category: Publication
products:
  - category: GraphicalInterface
    description: Web interface for searching and browsing human lncRNA sequences and annotations
    format: http
    id: lncipedia.search
    name: LncIPedia Search
    original_source:
      - lncipedia
    product_url: https://lncipedia.org/db/search
  - category: Product
    description: Downloadable database files in FASTA, GFF, and BED formats for both GRCh37/hg19 and GRCh38/hg38 genome assemblies
    format: fasta
    id: lncipedia.downloads
    name: LncIPedia Downloads
    product_url: https://lncipedia.org/download
  - category: GraphicalInterface
    description: UCSC Genome Browser trackhub for directly displaying LncIPedia annotations
    id: lncipedia.trackhub
    name: LncIPedia UCSC Trackhub
    original_source:
      - lncipedia
    product_url: https://www.lncipedia.org/trackhub/hub.txt
  - category: Product
    description: Integration files for Integrative Genomics Viewer (IGV) to visualize lncRNA annotations
    format: http
    id: lncipedia.igv
    name: LncIPedia IGV Integration
    original_source:
      - lncipedia
    product_url: https://lncipedia.org/download#anchor-igv
  - category: Product
    description: Metadata files including locus conservation across species (chimpanzee, mouse, Drosophila, zebrafish) and conversion tables to Ensembl and RefSeq IDs
    format: tsv
    id: lncipedia.metadata
    name: LncIPedia Metadata
    product_url: https://lncipedia.org/download#anchor-metadata
warnings:
  - LncIPedia download files are for non-commercial use only. Any other use should be approved in writing from Ghent University.
---

# LncIPedia

## Overview

LncIPedia is a comprehensive public database for human long non-coding RNA (lncRNA) sequences and annotations. The database integrates lncRNA transcript data from multiple sources and provides manually curated literature associations, making it a valuable reference resource for lncRNA research.

## Data Content

Current release (version 5.2, August 2018) contains:

- **127,802 transcripts** (107,039 in high-confidence set)
- **56,946 genes** (49,372 in high-confidence set)
- **2,482 manually curated lncRNA articles** with gene-specific annotations

The database provides:
- Complete sequence information in FASTA format
- Genomic annotations in GFF and BED formats
- Both full database and high-confidence subset (excluding putative protein-coding genes)
- Coverage for GRCh37/hg19 and GRCh38/hg38 genome assemblies

## Key Features

- **Comprehensive Coverage**: Aggregates lncRNA data from multiple sources into a unified resource
- **Literature Curation**: Manual curation of publications describing lncRNA function and biology
- **Cross-species Conservation**: Locus conservation data for chimpanzee, mouse, Drosophila, and zebrafish
- **Database Cross-references**: Conversion tables to Ensembl and RefSeq identifiers
- **Version Tracking**: Conversion tables between LncIPedia versions for maintaining consistent identifiers

## Access Methods

- **Web Search Interface**: Interactive search and browse functionality
- **Bulk Downloads**: Complete database exports in multiple formats (FASTA, GFF, BED)
- **Custom Exports**: User-defined data subsets via the search interface
- **Genome Browser Integration**: UCSC Genome Browser trackhub and IGV visualization support
- **FTP Archive**: Historical versions available for reproducible research

## Visualization Tools

- **UCSC Genome Browser Trackhub**: Direct integration for viewing lncRNA annotations in genome context
- **IGV Integration**: Pre-configured files for the Integrative Genomics Viewer
- **BED Format Files**: Compatible with standard genome visualization tools

## Use Cases

- Identifying and characterizing novel lncRNAs
- Literature mining for lncRNA functional information
- Comparative genomics of lncRNA loci across species
- Integrating lncRNA annotations into genomic analyses
- Training datasets for lncRNA prediction and classification methods
- Reference annotations for transcriptome studies

## Data Organization

- **Full Database**: Complete set of all lncRNA transcripts
- **High Confidence Set**: Curated subset excluding putative protein-coding genes
- **Metadata Files**: Conservation data and identifier mappings
- **Multiple Genome Builds**: Parallel annotations for hg19 and hg38

## Management

LncIPedia is developed and maintained by researchers at:
- Ghent University
- VIB (Vlaams Instituut voor Biotechnologie / Flanders Institute for Biotechnology)

## Licensing

LncIPedia download files are for non-commercial use only. Commercial use requires written approval from Ghent University.

## Citation

If using LncIPedia, cite: Volders PJ, Anckaert J, Verheggen K, Nuytens J, Martens L, Mestdagh P, Vandesompele J. "LncIPedia 5: towards a reference set of human long non-coding RNAs." Nucleic Acids Research. 2019. PMID:30371849