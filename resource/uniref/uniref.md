---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@uniprot.org
  - contact_type: url
    value: https://www.uniprot.org/contact
  id: ebi
  label: UniProt Consortium
creation_date: '2025-10-31T00:00:00Z'
description: UniRef (Universal Protein Resource Reference Clusters) provides clustered
  sets of protein sequences from the UniProt Knowledgebase and selected UniParc records
  to obtain complete coverage. UniRef100 combines identical sequences and sub-fragments
  into a single UniRef entry, UniRef90 clusters sequences with 90% sequence identity,
  and UniRef50 clusters sequences with 50% sequence identity, providing speed and
  coverage tradeoffs for similarity searches.
domains:
- proteomics
- biomedical
- biological systems
homepage_url: https://www.uniprot.org/help/uniref
id: uniref
infores_id: uniref
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: UniRef
products:
- category: Product
  compression: gzip
  description: UniRef100 database combining identical protein sequences and sub-fragments
    with 11-residue overlap into single representative entries, providing complete
    sequence coverage with 100% identity clustering
  format: fasta
  id: uniref.uniref100.fasta
  name: UniRef100 FASTA
  product_file_size: 124528354456
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref100/uniref100.fasta.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Timeout connecting
    to URL
- category: Product
  compression: gzip
  description: UniRef100 database in XML format with comprehensive metadata including
    cluster membership, representative sequences, taxonomy, and cross-references
  format: xml
  id: uniref.uniref100.xml
  name: UniRef100 XML
  product_file_size: 158103062524
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref100/uniref100.xml.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Timeout connecting
    to URL
- category: Product
  compression: gzip
  description: UniRef90 database clustering sequences with at least 90% sequence identity
    and 80% overlap, balancing speed and sensitivity for sequence searches
  format: fasta
  id: uniref.uniref90.fasta
  name: UniRef90 FASTA
  product_file_size: 46103634991
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref90/uniref90.fasta.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Timeout connecting
    to URL
- category: Product
  compression: gzip
  description: UniRef90 database in XML format with complete cluster information and
    annotations
  format: xml
  id: uniref.uniref90.xml
  name: UniRef90 XML
  product_file_size: 70196113636
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref90/uniref90.xml.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Timeout connecting
    to URL
- category: Product
  compression: gzip
  description: UniRef50 database clustering sequences with at least 50% sequence identity
    and 80% overlap, providing fast sequence searches with broad coverage of protein
    sequence space
  format: fasta
  id: uniref.uniref50.fasta
  name: UniRef50 FASTA
  product_file_size: 12385282557
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref50/uniref50.fasta.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Timeout connecting
    to URL
- category: Product
  compression: gzip
  description: UniRef50 database in XML format with detailed cluster annotations and
    relationships
  format: xml
  id: uniref.uniref50.xml
  name: UniRef50 XML
  product_file_size: 32238584114
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref50/uniref50.xml.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Timeout connecting
    to URL
- category: GraphicalInterface
  description: Web interface for searching, browsing, and analyzing UniRef cluster
    information with advanced search capabilities and visualization tools
  format: http
  id: uniref.portal
  name: UniRef Web Portal
  product_url: https://www.uniprot.org/uniref
- category: ProgrammingInterface
  description: RESTful API for programmatic access to UniRef cluster data supporting
    queries, downloads, and integration with bioinformatics workflows
  format: http
  id: uniref.api
  name: UniRef REST API
  product_url: https://www.uniprot.org/help/api
publications:
- authors:
  - Suzek BE
  - Huang H
  - McGarvey P
  - Mazumder R
  - Wu CH
  doi: 10.1093/bioinformatics/btm098
  id: https://doi.org/10.1093/bioinformatics/btm098
  journal: Bioinformatics
  preferred: true
  title: 'UniRef: comprehensive and non-redundant UniProt reference clusters'
  year: '2007'
synonyms:
- UniRef
- UniRef100
- UniRef90
- UniRef50
---

# UniRef