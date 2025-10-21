---
activity_status: active
category: Aggregator
creation_date: '2004-01-01T00:00:00Z'
description: miRBase is the primary online repository for microRNA sequences and annotations, serving as the central registry for microRNA nomenclature and providing a comprehensive archive of published microRNA data including sequences, annotations, predicted targets, and deep sequencing evidence.
domains:
  - genomics
  - biological systems
homepage_url: https://www.mirbase.org/
id: "mirbase"
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: miRBase
products:
  - category: GraphicalInterface
    description: Web portal for searching and browsing microRNA sequences by identifier, keyword, genomic location, tissue expression, or sequence
    format: http
    id: "mirbase.portal"
    name: miRBase Portal
    product_url: https://www.mirbase.org/
  - category: GraphicalInterface
    description: Browse interface for exploring microRNA entries organized by species and other criteria
    format: http
    id: "mirbase.browse"
    name: miRBase Browse Interface
    product_url: https://www.mirbase.org/
  - category: GraphicalInterface
    description: Search interface for finding microRNAs by genomic location coordinates
    format: http
    id: "mirbase.genomic-search"
    name: Genomic Location Search
    product_url: https://www.mirbase.org/
  - category: GraphicalInterface
    description: Search interface for finding microRNAs by tissue expression patterns
    format: http
    id: "mirbase.tissue-search"
    name: Tissue Expression Search
    product_url: https://www.mirbase.org/
  - category: Product
    compression: gzip
    description: All published microRNA data in EMBL format
    format: txt
    id: "mirbase.mirna-dat"
    name: miRNA.dat
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: FASTA format sequences of all microRNA hairpin precursors
    format: fasta
    id: "mirbase.hairpin-fa"
    name: hairpin.fa
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: FASTA format sequences of all mature microRNA sequences
    format: fasta
    id: "mirbase.mature-fa"
    name: mature.fa
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: List of changes between the last release and current release
    format: txt
    id: "mirbase.diff"
    name: miRNA.diff
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: List of entries that have been removed from the database
    format: txt
    id: "mirbase.dead"
    name: miRNA.dead
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: Genome coordinates for human microRNAs in GFF3 format
    format: gff
    id: "mirbase.hsa-gff3"
    name: Human (hsa) Genome Coordinates
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: Genome coordinates for mouse microRNAs in GFF3 format
    format: gff
    id: "mirbase.mmu-gff3"
    name: Mouse (mmu) Genome Coordinates
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: Genome coordinates for rat microRNAs in GFF3 format
    format: gff
    id: "mirbase.rno-gff3"
    name: Rat (rno) Genome Coordinates
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: Genome coordinates for Drosophila microRNAs in GFF3 format
    format: gff
    id: "mirbase.dme-gff3"
    name: Drosophila (dme) Genome Coordinates
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: Genome coordinates for C. elegans microRNAs in GFF3 format
    format: gff
    id: "mirbase.cel-gff3"
    name: C. elegans (cel) Genome Coordinates
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: Genome coordinates for zebrafish microRNAs in GFF3 format
    format: gff
    id: "mirbase.dre-gff3"
    name: Zebrafish (dre) Genome Coordinates
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    compression: gzip
    description: Genome coordinates for Arabidopsis microRNAs in GFF3 format
    format: gff
    id: "mirbase.ath-gff3"
    name: Arabidopsis (ath) Genome Coordinates
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: Product
    description: FTP archive with current release data files and previous releases
    format: http
    id: "mirbase.ftp"
    name: miRBase FTP Archive
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: DocumentationProduct
    description: Release notes and documentation for data file formats
    format: txt
    id: "mirbase.readme"
    name: README
    product_url: https://www.mirbase.org/download/CURRENT/
  - category: DocumentationProduct
    description: Comprehensive help documentation including submission guidelines, search instructions, genome assemblies, and naming conventions
    format: http
    id: "mirbase.help"
    name: miRBase Help Documentation
    product_url: https://www.mirbase.org/help/
publications:
  - authors:
      - Kozomara
      - Birgaoanu
      - Griffiths-Jones
    id: "https://pubmed.ncbi.nlm.nih.gov/30423142/"
    journal: Nucleic Acids Research
    preferred: true
    title: 'miRBase: from microRNA sequences to function'
    year: "2019"
  - authors:
      - Kozomara
      - Griffiths-Jones
    id: "https://pubmed.ncbi.nlm.nih.gov/24275495/"
    journal: Nucleic Acids Research
    title: 'miRBase: annotating high confidence microRNAs using deep sequencing data'
    year: "2014"
  - authors:
      - Kozomara
      - Griffiths-Jones
    id: "https://pubmed.ncbi.nlm.nih.gov/21037258/"
    journal: Nucleic Acids Research
    title: 'miRBase: integrating microRNA annotation and deep-sequencing data'
    year: "2011"
  - authors:
      - Griffiths-Jones
      - Saini
      - van Dongen
      - Enright
    id: "https://pubmed.ncbi.nlm.nih.gov/17991681/"
    journal: Nucleic Acids Research
    title: 'miRBase: tools for microRNA genomics'
    year: "2008"
  - authors:
      - Griffiths-Jones
      - Grocock
      - van Dongen
      - Bateman
      - Enright
    id: "https://pubmed.ncbi.nlm.nih.gov/16381832/"
    journal: Nucleic Acids Research
    title: 'miRBase: microRNA sequences, targets and gene nomenclature'
    year: "2006"
  - authors:
      - Griffiths-Jones
    id: "https://pubmed.ncbi.nlm.nih.gov/14681370/"
    journal: Nucleic Acids Research
    title: The microRNA Registry
    year: "2004"
---

# miRBase

miRBase is the primary online repository for microRNA sequences and annotations, serving as the central registry for microRNA nomenclature. Originally established in 2004 as the microRNA Registry, miRBase has evolved into a comprehensive archive of published microRNA data from a wide range of species.

## Overview

The database provides searchable access to microRNA sequences, annotations, predicted targets, and deep sequencing evidence. Users can search for microRNAs by identifier or keyword, genomic location, tissue expression patterns, or by sequence similarity. The database follows uniform annotation guidelines established by the research community and maintains the official nomenclature system for microRNAs.

## Data Content

miRBase contains:
- **Hairpin sequences**: Complete precursor microRNA sequences
- **Mature sequences**: Processed mature microRNA sequences
- **Genomic coordinates**: Precise locations mapped to genome assemblies for numerous species
- **Annotations**: Functional information and literature references
- **Deep sequencing data**: Evidence supporting microRNA annotation
- **Historical tracking**: Records of changes and removed entries

## Data Access

Data is available through multiple interfaces:
- **Web Portal**: Interactive search and browse functionality
- **Downloads**: Complete data dumps in EMBL and FASTA formats
- **FTP Archive**: Current and historical releases
- **Genome Coordinates**: Species-specific GFF3 files for over 30 organisms

## Key Features

- Search by identifier, keyword, genomic location, tissue expression, or sequence
- Browse microRNAs organized by species
- Download complete datasets in standardized formats (EMBL, FASTA, GFF3)
- Access genome coordinates for integration with genome browsers
- Track changes between releases
- Submit new microRNA sequences for official naming

## Species Coverage

miRBase includes microRNA data for model organisms (human, mouse, rat, Drosophila, C. elegans, zebrafish), plants (Arabidopsis, rice, maize, grape), and many other species, with genome coordinate files available in GFF3 format.

## Contact

For questions or to submit sequences for naming, contact: mirbase@manchester.ac.uk

miRBase is affiliated with the University of Manchester Faculty of Biology, Medicine and Health.
