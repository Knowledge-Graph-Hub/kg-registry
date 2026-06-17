---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@orthodb.org
  - contact_type: url
    value: https://www.orthodb.org/
  id: sib
  label: Evgeny Zdobnov Lab - SIB Swiss Institute of Bioinformatics
creation_date: '2025-05-07T00:00:00Z'
description: OrthoDB is a comprehensive database of orthologous protein-coding genes
  across multiple species, providing evolutionary and functional annotations of orthologous
  groups.
domains:
- biological systems
- organisms
homepage_url: https://www.orthodb.org/
id: orthodb
last_modified_date: '2026-05-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: OrthoDB
products:
- category: GraphicalInterface
  description: Web interface for exploring OrthoDB data
  format: http
  id: orthodb.site
  is_public: true
  name: OrthoDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_url: https://www.orthodb.org/
- category: ProgrammingInterface
  description: SPARQL endpoint for querying OrthoDB data
  format: http
  id: orthodb.api.sparql
  is_public: true
  name: OrthoDB SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_url: https://sparql.orthodb.org/
- category: ProgrammingInterface
  description: RESTful API for programmatic access to OrthoDB data
  format: http
  id: orthodb.api.rest
  is_public: true
  name: OrthoDB API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_url: https://www.orthodb.org/?page=api
- category: Product
  compression: gzip
  description: Tab-separated file with species information based on NCBI taxonomy
  format: tsv
  id: orthodb.species
  name: OrthoDB Species Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_file_size: 647315
  product_url: https://data.orthodb.org/current/download/odb_data_dump/odb12v2_species.tab.gz
- category: Product
  compression: gzip
  description: Tab-separated file with information about orthologous groups
  format: tsv
  id: orthodb.ogs
  name: OrthoDB Orthologous Groups
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_file_size: 134459173
  product_url: https://data.orthodb.org/current/download/odb_data_dump/odb12v2_OGs.tab.gz
- category: MappingProduct
  compression: gzip
  description: Tab-separated file mapping orthologous groups to genes
  format: tsv
  id: orthodb.og2genes
  name: OrthoDB OG to Genes Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_file_size: 4807568773
  product_url: https://data.orthodb.org/current/download/odb_data_dump/odb12v2_OG2genes.tab.gz
- category: Product
  compression: gzip
  description: Tab-separated file with gene information and annotations
  format: tsv
  id: orthodb.genes
  name: OrthoDB Genes Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_file_size: 4837182539
  product_url: https://data.orthodb.org/current/download/odb_data_dump/odb12v2_genes.tab.gz
- category: MappingProduct
  compression: gzip
  description: Tab-separated file with gene cross-references to other databases
  format: tsv
  id: orthodb.gene_xrefs
  name: OrthoDB Gene Cross-references
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_file_size: 5012354765
  product_url: https://data.orthodb.org/current/download/odb_data_dump/odb12v2_gene_xrefs.tab.gz
- category: Product
  compression: gzip
  description: Tab-separated file with orthologous group functional annotations including
    GO, COG, and InterPro
  format: tsv
  id: orthodb.og_xrefs
  name: OrthoDB OG Functional Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_file_size: 346459675
  product_url: https://data.orthodb.org/current/download/odb_data_dump/odb12v2_OG_xrefs.tab.gz
- category: Product
  compression: gzip
  description: FASTA-formatted amino acid sequences for all genes
  format: fasta
  id: orthodb.aa_fasta
  name: OrthoDB Protein Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_file_size: 39697100104
  product_url: https://data.orthodb.org/current/download/odb_data_dump/odb12v2_aa_fasta.gz
- category: Product
  compression: gzip
  description: FASTA-formatted coding sequences for all genes
  format: fasta
  id: orthodb.cds_fasta
  name: OrthoDB CDS Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orthodb
  product_file_size: 58778301483
  product_url: https://data.orthodb.org/current/download/odb_data_dump/odb12v2_cds_fasta.gz
publications:
- authors:
  - Tegenfeldt F
  - Kuznetsov D
  - Manni M
  - Berkeley M
  - Zdobnov EM
  - Kriventseva EV
  doi: 10.1093/nar/gkae987
  id: doi:10.1093/nar/gkae987
  journal: Nucleic Acids Research
  preferred: true
  title: 'OrthoDB and BUSCO update: annotation of orthologs with wider sampling of
    genomes'
  year: '2025'
- authors:
  - Kriventseva EV
  - Kuznetsov D
  - Tegenfeldt F
  - Manni M
  - Dias R
  - Simão FA
  - Zdobnov EM
  doi: 10.1093/nar/gky1053
  id: doi:10.1093/nar/gky1053
  journal: Nucleic Acids Research
  title: OrthoDB v10 - sampling the diversity of animal, plant, fungal, protist, bacterial
    and viral genomes for evolutionary and functional annotations of orthologs
  year: '2019'
- authors:
  - Zdobnov EM
  - Tegenfeldt F
  - Kuznetsov D
  - Waterhouse RM
  - Simão FA
  - Ioannidis P
  - Seppey M
  - Loetscher A
  - Kriventseva EV
  doi: 10.1093/nar/gkw1119
  id: doi:10.1093/nar/gkw1119
  journal: Nucleic Acids Research
  title: OrthoDB v9.1 - cataloging evolutionary and functional annotations for animal,
    fungal, plant, archaeal, bacterial and viral orthologs
  year: '2017'
---
OrthoDB is a comprehensive database of orthologous protein-coding genes across multiple species with a hierarchical catalog of orthologs. It provides evolutionary and functional annotations of orthologous groups at various taxonomic levels, covering Eukaryotes, Prokaryotes, and Viruses.

The current OrthoDB v12.2 release contains information for 32,072 species, including:
- 5,952 Eukaryotes
- 18,158 Prokaryotes
- 7,962 Viruses
- Approximately 165 million genes in total

OrthoDB offers several key features:
- Hierarchical orthology classification across the tree of life
- Integration with functional information from GO, InterPro, and COG
- Full amino acid and coding sequence data
- Gene and protein cross-references to major databases
- Orthologous group hierarchies based on phylogenetic relationships

The database is widely used in comparative genomics, molecular evolution studies, functional annotation, and gene family evolution analysis. It serves as a foundation for the popular BUSCO tool (Benchmarking Universal Single-Copy Orthologs) for genome assembly and annotation assessment.

OrthoDB is maintained by the Zdobnov Lab at the University of Geneva and the Swiss Institute of Bioinformatics (SIB), with regular updates incorporating new genome sequences and improving data quality. Access is provided through a user-friendly web interface, a SPARQL endpoint for semantic web queries, the versioned OrthoDB v12 REST API, and bulk downloads in various formats.