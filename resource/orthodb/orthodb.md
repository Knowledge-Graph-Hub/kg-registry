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
description: OrthoDB is a comprehensive database of orthologous protein-coding genes across multiple species, providing evolutionary and functional annotations of orthologous groups.
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
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_url: https://www.orthodb.org/
  - category: ProgrammingInterface
    description: SPARQL endpoint for querying OrthoDB data
    id: orthodb.api.sparql
    is_public: true
    name: OrthoDB SPARQL Endpoint
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_url: https://sparql.orthodb.org/
  - category: ProgrammingInterface
    description: RESTful API for programmatic access to OrthoDB data
    id: orthodb.api.rest
    is_public: true
    name: OrthoDB API
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_url: https://data.orthodb.org/v12/
  - category: Product
    compression: gzip
    description: Tab-separated file with species information based on NCBI taxonomy
    format: tsv
    id: orthodb.species
    name: OrthoDB Species Data
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_file_size: 644375
    product_url: https://data.orthodb.org/current/download/odb12v1_species.tab.gz
  - category: Product
    compression: gzip
    description: Tab-separated file with information about orthologous groups
    format: tsv
    id: orthodb.ogs
    name: OrthoDB Orthologous Groups
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_file_size: 145213387
    product_url: https://data.orthodb.org/current/download/odb12v1_OGs.tab.gz
  - category: MappingProduct
    compression: gzip
    description: Tab-separated file mapping orthologous groups to genes
    format: tsv
    id: orthodb.og2genes
    name: OrthoDB OG to Genes Mapping
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_file_size: 4909850611
    product_url: https://data.orthodb.org/current/download/odb12v1_OG2genes.tab.gz
  - category: Product
    compression: gzip
    description: Tab-separated file with gene information and annotations
    format: tsv
    id: orthodb.genes
    name: OrthoDB Genes Data
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_file_size: 4785964374
    product_url: https://data.orthodb.org/current/download/odb12v1_genes.tab.gz
  - category: MappingProduct
    compression: gzip
    description: Tab-separated file with gene cross-references to other databases
    format: tsv
    id: orthodb.gene_xrefs
    name: OrthoDB Gene Cross-references
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_file_size: 4692134033
    product_url: https://data.orthodb.org/current/download/odb12v1_gene_xrefs.tab.gz
  - category: Product
    compression: gzip
    description: Tab-separated file with orthologous group functional annotations including GO, COG, and InterPro
    format: tsv
    id: orthodb.og_xrefs
    name: OrthoDB OG Functional Annotations
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_file_size: 349253826
    product_url: https://data.orthodb.org/current/download/odb12v1_OG_xrefs.tab.gz
  - category: Product
    compression: gzip
    description: FASTA-formatted amino acid sequences for all genes
    format: fasta
    id: orthodb.aa_fasta
    name: OrthoDB Protein Sequences
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_file_size: 38928290988
    product_url: https://data.orthodb.org/current/download/odb12v1_aa_fasta.gz
  - category: Product
    compression: gzip
    description: FASTA-formatted coding sequences for all genes
    format: fasta
    id: orthodb.cds_fasta
    name: OrthoDB CDS Sequences
    original_source:
      - source: orthodb
        relation_type: prov:hadPrimarySource
    product_file_size: 57560209301
    product_url: https://data.orthodb.org/current/download/odb12v1_cds_fasta.gz
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
  title: 'OrthoDB and BUSCO update: annotation of orthologs with wider sampling of genomes'
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
  title: OrthoDB v10 - sampling the diversity of animal, plant, fungal, protist, bacterial and viral genomes for evolutionary and functional annotations of orthologs
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
  title: OrthoDB v9.1 - cataloging evolutionary and functional annotations for animal, fungal, plant, archaeal, bacterial and viral orthologs
  year: '2017'
repository: https://github.com/zdobnov-lab/orthodb
creation_date: '2025-05-07T00:00:00Z'
last_modified_date: '2026-05-23T00:00:00Z'
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
