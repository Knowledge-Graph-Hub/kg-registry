---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.wormbase.org/about/contact
  label: WormBase
creation_date: '2025-10-30T00:00:00Z'
description: WormBase is an online biological database providing comprehensive genomic
  and biological information about C. elegans and related nematodes, including annotated
  genomes, gene structures, functional annotations, genetic maps, gene expression
  data, protein interactions, RNAi phenotypes, and curated literature.
domains:
- genomics
- organisms
- anatomy and development
homepage_url: http://www.wormbase.org/
id: wormbase
infores_id: wormbase
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: Creative Commons Attribution 4.0 International
name: WormBase
products:
- category: GraphicalInterface
  description: Primary web portal for browsing and searching nematode genomic and
    biological data
  format: http
  id: wormbase.portal
  name: WormBase Web Portal
  original_source:
  - wormbase
  product_url: http://www.wormbase.org/
- category: GraphicalInterface
  description: Genome browser for visualizing genes, transcripts, and genomic features
    in their chromosomal context
  id: wormbase.gbrowse
  name: WormBase GBrowse
  original_source:
  - wormbase
  product_url: https://www.wormbase.org/tools/genome/gbrowse/c_elegans/
- category: ProgrammingInterface
  description: REST API providing programmatic access to WormBase data including genes,
    proteins, variations, and annotations
  id: wormbase.api
  is_public: true
  name: WormBase REST API
  original_source:
  - wormbase
  product_url: https://www.wormbase.org/about/userguide/for_developers/API-REST
- category: GraphicalInterface
  description: WormMine InterMine instance for complex queries and bulk data retrieval
    across WormBase datasets
  id: wormbase.wormmine
  name: WormMine
  original_source:
  - wormbase
  product_url: https://im-dev.wormbase.org/tools/wormmine/begin.do
- category: GraphicalInterface
  description: Full-text search tool for querying C. elegans and nematode literature
    with ontology term support
  id: wormbase.textpresso
  name: Textpresso
  original_source:
  - wormbase
  product_url: https://www.textpresso.org/cgi-bin/wb/tfw.cgi
- category: Product
  description: FTP server providing bulk downloads of genome assemblies, annotations,
    gene models, and other WormBase data files
  id: wormbase.ftp
  name: WormBase FTP Downloads
  original_source:
  - wormbase
  product_url: ftp://ftp.wormbase.org/pub/wormbase/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-08_ FTP error_ [Errno
    101] Network is unreachable
  - File was not able to be retrieved when checked on 2025-12-04_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.wormbase.org/pub/wormbase/'
  - 'File was not able to be retrieved when checked on 2025-12-09: FTP error: [Errno
    101] Network is unreachable'
- category: GraphicalInterface
  description: Sub-portal hosting approximately 100 parasitic helminth genomes with
    annotations and comparative genomics tools
  id: wormbase.parasite
  name: WormBase ParaSite
  original_source:
  - wormbase
  product_url: https://parasite.wormbase.org/
publications:
- id: PMID:19910365
  preferred: true
  title: 'WormBase: a comprehensive resource for nematode research.'
repository: https://github.com/WormBase
synonyms:
- WB
taxon:
- NCBITaxon:6237
---
# WormBase

## Overview

WormBase is a comprehensive biological database and online resource for the biology and genome of the nematode model organism *Caenorhabditis elegans* and related nematode species. The database integrates genomic sequences, gene structures, functional annotations, genetic and physical maps, gene expression patterns, protein-protein interactions, RNAi phenotypes, mutant alleles, and curated literature.

## Primary Organism

WormBase primarily focuses on *Caenorhabditis elegans* but also includes data for:
- *C. briggsae*, *C. remanei*, *C. brenneri*, *C. angaria*, *C. japonica*
- *Pristionchus pacificus*
- Parasitic nematodes including *Haemonchus contortus*, *Brugia malayi*, *Meloidogyne hapla*, and *Meloidogyne incognita*

## Data Content

WormBase comprises:
- Annotated genomes with hand-curated gene structures
- ~20,500 protein-coding genes and ~16,000 non-coding genes for C. elegans
- Gene family classifications and orthology relationships
- Comprehensive phenotype and allele information
- Whole-genome RNAi screens
- Gene expression profiles from microarrays, RNA-Seq, and GFP reporter studies
- Complete cell lineage and nervous system wiring diagram
- Protein-protein interaction networks
- Genetic regulatory relationships
- Searchable bibliography of C. elegans research

## Tools & Access

- **Web Portal**: Interactive browsing and search interface
- **GBrowse**: Genome browser for visualizing genomic features
- **WormMine**: InterMine-based data mining facility for complex queries
- **REST API**: Programmatic access to all WormBase data
- **Textpresso**: Literature text mining and search
- **FTP Downloads**: Bulk data files including genome assemblies and annotations
- **WormBase ParaSite**: Sub-portal for parasitic helminth genomes

## Management & Funding

WormBase is a collaboration among the European Bioinformatics Institute, Wellcome Trust Sanger Institute, Ontario Institute for Cancer Research, Washington University in St. Louis, and California Institute of Technology. Supported by the National Institutes of Health (P41-HG002223) and the British Medical Research Council.

## Part of Alliance

WormBase is a founding member of the Alliance of Genome Resources, which integrates data across model organism databases.