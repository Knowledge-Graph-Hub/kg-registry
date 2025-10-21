---
activity_status: active
category: Aggregator
creation_date: '2014-01-01T00:00:00Z'
description: piRBase is a manually curated database for PIWI-interacting RNAs (piRNAs), focused on piRNA functional analysis and annotation. It integrates high-throughput sequencing data from multiple organisms and provides comprehensive information about piRNA sequences, genomic locations, functional annotations, and epigenetic features.
domains:
  - genomics
  - biological systems
homepage_url: http://bigdata.ibp.ac.cn/piRBase
id: "pirbase"
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: piRBase
products:
  - category: GraphicalInterface
    description: Web portal for searching and browsing piRNA sequences by identifier or keyword
    format: http
    id: "pirbase.portal"
    name: piRBase Portal
    product_url: http://bigdata.ibp.ac.cn/piRBase/
  - category: GraphicalInterface
    description: Browse interface for exploring piRNAs organized by species
    format: http
    id: "pirbase.browse"
    name: piRBase Browse Interface
    product_url: http://bigdata.ibp.ac.cn/piRBase/browse.php
  - category: GraphicalInterface
    description: Function annotation interface for piRNA functional analysis
    format: http
    id: "pirbase.function"
    name: piRNA Function Interface
    product_url: http://bigdata.ibp.ac.cn/piRBase/function.php
  - category: GraphicalInterface
    description: Genome browser interface for viewing piRNA genomic locations
    format: http
    id: "pirbase.genome"
    name: Genome Browser Interface
    product_url: http://bigdata.ibp.ac.cn/piRBase/genome.php
  - category: GraphicalInterface
    description: Epigenetics interface for exploring methylation and other epigenetic features
    format: http
    id: "pirbase.epigenetics"
    name: Epigenetics Interface
    product_url: http://bigdata.ibp.ac.cn/piRBase/methylation.php
  - category: GraphicalInterface
    description: Tools interface for piRNA analysis utilities
    format: http
    id: "pirbase.tools"
    name: piRBase Tools
    product_url: http://bigdata.ibp.ac.cn/piRBase/tools.php
  - category: Product
    compression: gzip
    description: FASTA format sequences for human piRNAs (version 3.0)
    format: fasta
    id: "pirbase.hsa-sequences"
    name: Human piRNA Sequences
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: FASTA format sequences for mouse piRNAs (version 3.0)
    format: fasta
    id: "pirbase.mmu-sequences"
    name: Mouse piRNA Sequences
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: FASTA format sequences for rat piRNAs
    format: fasta
    id: "pirbase.rno-sequences"
    name: Rat piRNA Sequences
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: FASTA format sequences for Drosophila melanogaster piRNAs (version 3.0)
    format: fasta
    id: "pirbase.dme-sequences"
    name: Drosophila piRNA Sequences
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: FASTA format sequences for C. elegans piRNAs (version 3.0)
    format: fasta
    id: "pirbase.cel-sequences"
    name: C. elegans piRNA Sequences
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: FASTA format sequences for zebrafish piRNAs
    format: fasta
    id: "pirbase.dre-sequences"
    name: Zebrafish piRNA Sequences
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: Gold standard human piRNA sequences with high confidence annotations
    format: fasta
    id: "pirbase.hsa-gold"
    name: Human Gold Standard piRNAs
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: Gold standard mouse piRNA sequences with high confidence annotations
    format: fasta
    id: "pirbase.mmu-gold"
    name: Mouse Gold Standard piRNAs
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: Gold standard Drosophila piRNA sequences with high confidence annotations
    format: fasta
    id: "pirbase.dme-gold"
    name: Drosophila Gold Standard piRNAs
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: Genome coordinates for human piRNAs on hg19 assembly in BED format
    format: txt
    id: "pirbase.hsa-bed"
    name: Human piRNA Coordinates (hg19)
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: Genome coordinates for human piRNAs on GRCh38 assembly in BED format
    format: txt
    id: "pirbase.hsa-grch38-bed"
    name: Human piRNA Coordinates (GRCh38)
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: Genome coordinates for mouse piRNAs on GRCm38 assembly in BED format
    format: txt
    id: "pirbase.mmu-bed"
    name: Mouse piRNA Coordinates (GRCm38)
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: Product
    compression: gzip
    description: Genome coordinates for Drosophila piRNAs on BDGP6 assembly in BED format
    format: txt
    id: "pirbase.dme-bed"
    name: Drosophila piRNA Coordinates (BDGP6)
    product_url: http://bigdata.ibp.ac.cn/piRBase/download.php
  - category: DocumentationProduct
    description: Tutorial and user manual for piRBase
    format: http
    id: "pirbase.tutorial"
    name: piRBase Tutorial
    product_url: http://bigdata.ibp.ac.cn/piRBase/about.php
publications:
  - authors:
      - Wang
      - Shi
      - Zhou
      - Zhang
      - Song
      - Ying
      - Yu
      - Li
      - Zhao
      - Zeng
      - He
      - Chen
    id: "https://pubmed.ncbi.nlm.nih.gov/34871445/"
    journal: Nucleic Acids Research
    preferred: true
    title: 'piRBase: integrating piRNA annotation in all aspects'
    year: "2022"
  - authors:
      - Wang
      - Zhang
      - Lu
      - Li
      - Zheng
      - Kan
      - Chen
      - He
    id: "https://pubmed.ncbi.nlm.nih.gov/30371818/"
    journal: Nucleic Acids Research
    title: 'piRBase: a comprehensive database of piRNA sequences'
    year: "2019"
  - authors:
      - Zhang
      - Si
      - Skogerbø
      - Wang
      - Cui
      - Li
      - Sun
      - Liu
      - Sun
      - Chen
      - He
      - Huang
    id: "https://pubmed.ncbi.nlm.nih.gov/25425034/"
    journal: Database (Oxford)
    title: 'piRBase: a web resource assisting piRNA functional study'
    year: "2014"
warnings:
  - The piRBase website may be intermittently available. If the site is inaccessible, please try again later.
---

# piRBase

piRBase is a manually curated database for PIWI-interacting RNAs (piRNAs), a type of small noncoding RNA with various regulatory functions. Since its initial launch in 2014, piRBase has become a comprehensive resource focused on assisting piRNA functional analysis and annotation.

## Overview

The database integrates high-throughput sequencing data from multiple organisms and provides extensive information about piRNA sequences, genomic locations, functional annotations, and epigenetic features. As of version 3.0, piRBase has integrated hundreds of datasets from numerous organisms, with the collection containing over 173 million piRNA sequences.

## Data Content

piRBase provides:
- **piRNA Sequences**: Comprehensive collection of piRNA sequences from multiple species in FASTA format
- **Gold Standards**: High-confidence piRNA sequences for model organisms
- **Genomic Locations**: Precise genome coordinates in BED format for various genome assemblies
- **Functional Annotations**: Information about piRNA functions and regulatory roles
- **Epigenetic Features**: Methylation and other epigenetic modifications associated with piRNAs
- **Cross-species Data**: piRNA information from over 50 species including humans, mice, rats, Drosophila, C. elegans, zebrafish, and many others

## Species Coverage

The database includes piRNA data for:
- **Model organisms**: Human (hsa), mouse (mmu), rat (rno), Drosophila melanogaster (dme), C. elegans (cel), zebrafish (dre)
- **Primates**: Rhesus macaque, marmoset, crab-eating macaque
- **Other mammals**: Cow (bta), pig (ssc), horse (eca), rabbit (ocu), giant panda, tree shrew
- **Birds**: Chicken (gga)
- **Invertebrates**: Silkworm (bmo), multiple Caenorhabditis species, sea hare, sea anemone, various parasitic worms
- **Other species**: Multiple Drosophila species, mud crab, and more

## Data Access

Data is available through multiple interfaces:
- **Web Portal**: Search and browse piRNA sequences by identifier or keyword
- **Browse Interface**: Explore piRNAs organized by species
- **Function Interface**: Analyze piRNA functional annotations
- **Genome Browser**: View piRNA genomic locations
- **Epigenetics Interface**: Explore methylation and epigenetic features
- **Tools**: Various analysis utilities
- **Downloads**: Complete datasets in FASTA and BED formats

## Key Features

- Search piRNAs by identifier (e.g., piR-hsa-35391, piR-mmu-604679)
- Browse piRNAs by species
- Analyze piRNA functions and regulatory roles
- View genomic locations with integrated genome browser
- Explore epigenetic modifications
- Download sequences and coordinates for bioinformatics analysis
- Access gold standard high-confidence piRNA sets

## Contact

piRBase is affiliated with the BIG Data Center (Beijing Institute of Genomics, Chinese Academy of Sciences).

**Note**: The piRBase website may experience intermittent availability. If you encounter access issues, please try again later.
