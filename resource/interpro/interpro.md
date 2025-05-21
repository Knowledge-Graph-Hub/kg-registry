---
layout: resource_detail
activity_status: active
id: interpro
name: InterPro
description: InterPro is a database of protein families, domains and functional sites
  in which identifiable features found in known proteins can be applied to unknown
  protein sequences.
domains:
- biological systems
- proteomics
- genomics
- bioinformatics
- drug discovery
contacts:
- category: Organization
  label: InterPro
  contact_details:
  - contact_type: email
    value: interpro-help@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/interpro/contact/
homepage_url: https://www.ebi.ac.uk/interpro/
repository: https://www.ebi.ac.uk/interpro/
license:
  label: CC0-1.0
  id: https://creativecommons.org/publicdomain/zero/1.0/
category: DataSource
products:
- category: GraphicalInterface
  id: interpro.web
  name: InterPro Web Interface
  description: Web interface for browsing and searching the InterPro database
  product_url: https://www.ebi.ac.uk/interpro/
  original_source:
  - interpro
  format: http
- category: ProgrammingInterface
  id: interpro.api
  name: InterPro API
  description: RESTful API for programmatic access to InterPro data
  product_url: https://www.ebi.ac.uk/interpro/api/
  is_public: true
  connection_url: https://www.ebi.ac.uk/interpro/api/
  original_source:
  - interpro
- category: ProcessProduct
  id: interpro.interproscan
  name: InterProScan
  description: Software package for scanning protein sequences against InterPro's signatures
  product_url: http://ftp.ebi.ac.uk/pub/software/unix/iprscan/5/5.74-105.0/interproscan-5.74-105.0-64-bit.tar.gz
  original_source:
  - interpro
  compression: targz
- category: DataModelProduct
  id: interpro.entry_list
  name: InterPro Entry List
  description: Complete list of InterPro entries with their types and short names
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/entry.list
  original_source:
  - interpro
  format: tsv
- category: DataModelProduct
  id: interpro.xml
  name: InterPro XML
  description: Complete InterPro database in XML format containing entries, member database signatures, GO terms, and relationships
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro.xml.gz
  original_source:
  - interpro
  format: xml
  compression: gzip
- category: MappingProduct
  id: interpro.match_complete
  name: InterPro Match Complete
  description: Complete set of matches between protein sequences and InterPro entries/signatures
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/match_complete.xml.gz
  original_source:
  - interpro
  format: xml
  compression: gzip
- category: MappingProduct
  id: interpro.uniparc_match
  name: UniParc Match
  description: InterPro matches for UniParc protein sequences
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/uniparc_match.tar.gz
  original_source:
  - interpro
  format: xml
  compression: targz
- category: MappingProduct
  id: interpro.protein2ipr
  name: Protein to InterPro Mappings
  description: Mappings of protein sequences to InterPro entries in a tab-delimited format
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/protein2ipr.dat.gz
  original_source:
  - interpro
  format: tsv
  compression: gzip
- category: DataModelProduct
  id: interpro.parent_child_tree
  name: Parent-Child Tree
  description: Hierarchical relationships between InterPro entries
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/ParentChildTreeFile.txt
  original_source:
  - interpro
  format: tsv
- category: MappingProduct
  id: interpro.interpro2go
  name: InterPro to GO Mappings
  description: Mappings between InterPro entries and Gene Ontology (GO) terms
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro2go
  original_source:
  - go
  - interpro
  secondary_source:
  - interpro
  format: tsv
publications:
- doi: doi:10.1093/nar/gkae1082
  id: doi:10.1093/nar/gkae1082
  preferred: true
  year: "2024"
  authors:
  - Blum M
  - Andreeva A
  - Florentino LC
  - Chuguransky SR
  - Grego T
  - Hobbs E
  - Pinto BL
  - Orr A
  - Paysan-Lafosse T
  - Ponamareva I
  - Salazar GA
  - Bordin N
  - Bork P
  - Bridge A
  - Colwell L
  - Gough J
  - Haft DH
  - Letunic I
  - Llinares-López F
  - Marchler-Bauer A
  - Meng-Papaxanthos L
  - Mi H
  - Natale DA
  - Orengo CA
  - Pandurangan AP
  - Piovesan D
  - Rivoire C
  - Sigrist CJA
  - Thanki N
  - Thibaud-Nissen F
  - Thomas PD
  - Tosatto SCE
  - Wu CH
  - Bateman A
  title: >-
    InterPro: the protein sequence classification resource in 2025
---

InterPro is a database of protein families, domains and functional sites in which identifiable features found in known proteins can be applied to unknown protein sequences.

## Overview

InterPro is a comprehensive database hosted at the European Bioinformatics Institute (EMBL-EBI) that provides functional analysis of proteins by classifying them into families and predicting the presence of domains and important sites. It integrates predictive protein signatures from multiple partner databases into a unified resource.

## Database Components

InterPro integrates signatures from several member databases, including:

- Pfam: Protein families represented by multiple sequence alignments and hidden Markov models
- PROSITE: Patterns and profiles for protein families and domains
- SMART: Identification and annotation of genetically mobile domains
- PRINTS: Fingerprints for protein sequence classification
- PANTHER: Protein families classified by function
- CDD (Conserved Domain Database): Ancient conserved protein domains
- PIRSF: Hierarchical classification of complete proteins
- SUPERFAMILY: Structural and functional annotation based on SCOP superfamilies
- CATH-Gene3D: Protein domain assignments for genomes
- TIGRFAMs: Protein families based on hidden Markov models
- HAMAP: High-quality automated annotations of microbial proteins

## Features and Applications

InterPro provides:

- Comprehensive protein annotation
- Hierarchical classification of proteins
- Functional and structural insights
- GO (Gene Ontology) term mappings
- Pathway associations
- Taxonomic distribution information
- Cross-references to other biological databases

## Tools and Access

The primary tool for using InterPro signatures is InterProScan, which allows users to scan their protein sequences against all InterPro's signatures simultaneously. InterPro data can be accessed via:

- Web interface for interactive browsing and searching
- Programmatic access via REST API
- Downloadable datasets in various formats (OBO, OWL, JSON, XML)
- InterProScan software package for local installation and high-throughput analysis

InterPro is widely used in genome annotation projects, comparative genomics studies, structural biology research, and functional characterization of proteins across all taxonomic groups.
