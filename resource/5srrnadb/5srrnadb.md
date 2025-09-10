---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: 5SRNAdb (5S rRNA Database) is a curated repository of unique full-length 5S ribosomal RNA sequences and genes across Bacteria, Archaea, and Eukaryota (cytoplasmic and organellar), providing alignments, secondary structure diagrams, taxonomic browsing, and downloadable custom or global alignments for comparative and structural studies.
domains:
  - genomics
  - biological systems
homepage_url: http://www.combio.pl/5srnadb/
id: 5srrnadb
last_modified_date: '2025-09-10T00:00:00Z'
layout: resource_detail
name: 5SRNAdb
publications:
  - id: doi:10.1093/nar/gkv1081
    title: "5SRNAdb: an information resource for 5S ribosomal RNAs"
    year: '2016'
    journal: Nucleic Acids Research
    doi: 10.1093/nar/gkv1081
    preferred: true
products:
  - category: GraphicalInterface
    description: Web portal with search, taxonomic browser, interactive alignments, and secondary structure visualizations
    format: fasta
    id: 5srrnadb.portal
    name: 5SRNAdb Portal
    product_url: http://www.combio.pl/5srnadb/
  - category: Product
    description: Archaea 5S rRNA sequences (non-structural alignment) in FASTA format
    format: fasta
    id: 5srrnadb.downloads.archaea.sequences
    name: Archaea Sequences FASTA
    product_url: http://www.combio.pl/rrna/static/download/Archaea.fasta
  - category: Product
    description: Archaea 5S rRNA structural alignment (FASTA with secondary structure annotation)
    format: fasta
    id: 5srrnadb.downloads.archaea.structural
    name: Archaea Structural Alignment FASTA
    product_url: http://www.combio.pl/rrna/static/download/Archaea.ss.fasta
  - category: Product
    description: Bacteria 5S rRNA sequences (non-structural alignment) in FASTA format
    format: fasta
    id: 5srrnadb.downloads.bacteria.sequences
    name: Bacteria Sequences FASTA
    product_url: http://www.combio.pl/rrna/static/download/Bacteria.fasta
  - category: Product
    description: Bacteria 5S rRNA structural alignment (FASTA with secondary structure annotation)
    format: fasta
    id: 5srrnadb.downloads.bacteria.structural
    name: Bacteria Structural Alignment FASTA
    product_url: http://www.combio.pl/rrna/static/download/Bacteria.ss.fasta
  - category: Product
    description: Eukaryota 5S rRNA sequences (non-structural alignment) in FASTA format
    format: fasta
    id: 5srrnadb.downloads.eukaryota.sequences
    name: Eukaryota Sequences FASTA
    product_url: http://www.combio.pl/rrna/static/download/Eukaryota.fasta
  - category: Product
    description: Eukaryota 5S rRNA structural alignment (FASTA with secondary structure annotation)
    format: fasta
    id: 5srrnadb.downloads.eukaryota.structural
    name: Eukaryota Structural Alignment FASTA
    product_url: http://www.combio.pl/rrna/static/download/Eukaryota.ss.fasta
  - category: Product
    description: Plastids 5S rRNA sequences (non-structural alignment) in FASTA format
    format: fasta
    id: 5srrnadb.downloads.plastids.sequences
    name: Plastids Sequences FASTA
    product_url: http://www.combio.pl/rrna/static/download/Plastids.fasta
  - category: Product
    description: Plastids 5S rRNA structural alignment (FASTA with secondary structure annotation)
    format: fasta
    id: 5srrnadb.downloads.plastids.structural
    name: Plastids Structural Alignment FASTA
    product_url: http://www.combio.pl/rrna/static/download/Plastids.ss.fasta
  - category: Product
    description: Mitochondria 5S rRNA sequences (non-structural alignment) in FASTA format
    format: fasta
    id: 5srrnadb.downloads.mitochondria.sequences
    name: Mitochondria Sequences FASTA
    product_url: http://www.combio.pl/rrna/static/download/Mitochondria.fasta
  - category: Product
    description: Mitochondria 5S rRNA structural alignment (FASTA with secondary structure annotation)
    format: fasta
    id: 5srrnadb.downloads.mitochondria.structural
    name: Mitochondria Structural Alignment FASTA
    product_url: http://www.combio.pl/rrna/static/download/Mitochondria.ss.fasta
---

# 5SRNAdb

## Overview

5SRNAdb is a specialized database of curated 5S ribosomal RNA sequences and genes from Bacteria, Archaea, and Eukaryota, emphasizing high-quality non-redundant sequences, structural alignment, and visualization. It supports dynamic generation of customized multiple sequence alignments and interactive secondary structure diagrams.

## Access

- Portal: search, taxonomy browser, BLAST similarity, interactive secondary structure diagrams
- Downloads: full domain alignments and user-customized FASTA (with bracket notation structures) available through portal windows

## Citation

Please cite: Szymanski M, Zielezinski A, Karlowski WM. 5SRNAdb: an information resource for 5S ribosomal RNAs. Nucleic Acids Res. 2016;44:D180–D183. doi:10.1093/nar/gkv1081