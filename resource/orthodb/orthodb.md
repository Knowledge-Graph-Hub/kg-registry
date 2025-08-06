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
  label: Evgeny Zdobnov Lab - SIB Swiss Institute of Bioinformatics
description: OrthoDB is a comprehensive database of orthologous protein-coding genes
  across multiple species, providing evolutionary and functional annotations of orthologous
  groups.
domains:
- biological systems
- organisms
homepage_url: https://www.orthodb.org/
id: orthodb
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: OrthoDB
products:
- category: GraphicalInterface
  description: Web interface for exploring OrthoDB data
  id: orthodb.site
  is_public: true
  name: OrthoDB Web Interface
  original_source:
  - orthodb
  product_url: https://www.orthodb.org/
  secondary_source:
  - orthodb
- category: ProgrammingInterface
  description: SPARQL endpoint for querying OrthoDB data
  id: orthodb.api.sparql
  is_public: true
  name: OrthoDB SPARQL Endpoint
  original_source:
  - orthodb
  product_url: https://sparql.orthodb.org/
  secondary_source:
  - orthodb
- category: ProgrammingInterface
  description: RESTful API for programmatic access to OrthoDB data
  id: orthodb.api.rest
  is_public: true
  name: OrthoDB API
  original_source:
  - orthodb
  product_url: https://www.orthodb.org/api/
  secondary_source:
  - orthodb
- category: Product
  compression: gzip
  description: Tab-separated file with species information based on NCBI taxonomy
  format: tsv
  id: orthodb.species
  name: OrthoDB Species Data
  original_source:
  - orthodb
  product_file_size: 644375
  product_url: https://data.orthodb.org/current/download/odb12v1_species.tab.gz
  secondary_source:
  - orthodb
- category: Product
  compression: gzip
  description: Tab-separated file with information about orthologous groups
  format: tsv
  id: orthodb.ogs
  name: OrthoDB Orthologous Groups
  original_source:
  - orthodb
  product_file_size: 145213387
  product_url: https://data.orthodb.org/current/download/odb12v1_OGs.tab.gz
  secondary_source:
  - orthodb
- category: MappingProduct
  compression: gzip
  description: Tab-separated file mapping orthologous groups to genes
  format: tsv
  id: orthodb.og2genes
  name: OrthoDB OG to Genes Mapping
  original_source:
  - orthodb
  product_file_size: 4909850611
  product_url: https://data.orthodb.org/current/download/odb12v1_OG2genes.tab.gz
  secondary_source:
  - orthodb
- category: Product
  compression: gzip
  description: Tab-separated file with gene information and annotations
  format: tsv
  id: orthodb.genes
  name: OrthoDB Genes Data
  original_source:
  - orthodb
  product_file_size: 4785964374
  product_url: https://data.orthodb.org/current/download/odb12v1_genes.tab.gz
  secondary_source:
  - orthodb
- category: MappingProduct
  compression: gzip
  description: Tab-separated file with gene cross-references to other databases
  format: tsv
  id: orthodb.gene_xrefs
  name: OrthoDB Gene Cross-references
  original_source:
  - orthodb
  product_file_size: 4692134033
  product_url: https://data.orthodb.org/current/download/odb12v1_gene_xrefs.tab.gz
  secondary_source:
  - orthodb
- category: Product
  compression: gzip
  description: Tab-separated file with orthologous group functional annotations including
    GO, COG, and InterPro
  format: tsv
  id: orthodb.og_xrefs
  name: OrthoDB OG Functional Annotations
  original_source:
  - orthodb
  product_file_size: 349253826
  product_url: https://data.orthodb.org/current/download/odb12v1_OG_xrefs.tab.gz
  secondary_source:
  - orthodb
- category: Product
  compression: gzip
  description: FASTA-formatted amino acid sequences for all genes
  format: fasta
  id: orthodb.aa_fasta
  name: OrthoDB Protein Sequences
  original_source:
  - orthodb
  product_file_size: 38928290988
  product_url: https://data.orthodb.org/current/download/odb12v1_aa_fasta.gz
  secondary_source:
  - orthodb
- category: Product
  compression: gzip
  description: FASTA-formatted coding sequences for all genes
  format: fasta
  id: orthodb.cds_fasta
  name: OrthoDB CDS Sequences
  original_source:
  - orthodb
  product_file_size: 57560209301
  product_url: https://data.orthodb.org/current/download/odb12v1_cds_fasta.gz
  secondary_source:
  - orthodb
publications:
- authors:
  - Kriventseva EV
  - Kuznetsov D
  - Tegenfeldt F
  - Manni M
  - Dias R
  - Simão FA
  - Zdobnov EM
  doi: doi:10.1093/nar/gky1053
  id: doi:10.1093/nar/gky1053
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
  doi: doi:10.1093/nar/gkw1119
  id: doi:10.1093/nar/gkw1119
  preferred: true
  title: OrthoDB v9.1 - cataloging evolutionary and functional annotations for animal,
    fungal, plant, archaeal, bacterial and viral orthologs
  year: '2017'
repository: https://github.com/zdobnov-lab/orthodb
---
OrthoDB is a comprehensive database of orthologous protein-coding genes across multiple species with a hierarchical catalog of orthologs. It provides evolutionary and functional annotations of orthologous groups at various taxonomic levels, covering Eukaryotes, Prokaryotes, and Viruses.

The database contains information for more than 31,000 species, including:
- More than 5,800 Eukaryotes
- More than 18,100 Prokaryotes
- More than 7,900 Viruses
- Approximately 162 million genes in total

OrthoDB offers several key features:
- Hierarchical orthology classification across the tree of life
- Integration with functional information from GO, InterPro, and COG
- Full amino acid and coding sequence data
- Gene and protein cross-references to major databases
- Orthologous group hierarchies based on phylogenetic relationships

The database is widely used in comparative genomics, molecular evolution studies, functional annotation, and gene family evolution analysis. It serves as a foundation for the popular BUSCO tool (Benchmarking Universal Single-Copy Orthologs) for genome assembly and annotation assessment.

OrthoDB is maintained by the Zdobnov Lab at the University of Geneva and the Swiss Institute of Bioinformatics (SIB), with regular updates incorporating new genome sequences and improving data quality. Access is provided through a user-friendly web interface, a SPARQL endpoint for semantic web queries, a RESTful API for programmatic access, and bulk downloads in various formats.