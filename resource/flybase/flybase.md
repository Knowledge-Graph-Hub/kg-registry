---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: FlyBase is a comprehensive database of genomic and genetic data for Drosophila
  melanogaster (fruit fly) and related species. It provides curated information on
  genes, genomes, phenotypes, genetic variants, stocks, and experimental tools for
  the Drosophila research community. The database integrates sequence data, genome
  annotations, functional characterizations, expression patterns, genetic interactions,
  disease models, and orthology relationships. FlyBase serves as the primary reference
  for Drosophila gene nomenclature and provides extensive tools for querying and analyzing
  genomic data across multiple Drosophila species.
domains:
- genomics
- organisms
- biological systems
homepage_url: https://flybase.org/
id: flybase
infores_id: flybase
last_modified_date: '2025-10-08T00:00:00Z'
layout: resource_detail
name: FlyBase
products:
- category: Product
  description: Genome annotation files for Drosophila melanogaster in GFF3 format,
    including gene models, transcripts, exons, and functional elements
  format: gff
  id: flybase.genome.annotations.gff
  name: FlyBase Genome Annotations
  original_source:
  - flybase
  product_url: https://wiki.flybase.org/wiki/FlyBase:Downloads_Overview
- category: Product
  description: Complete genome sequences for Drosophila species in FASTA format, including
    chromosome assemblies and scaffolds
  format: fasta
  id: flybase.genome.sequences.fasta
  name: FlyBase Genome Sequences
  original_source:
  - flybase
  product_url: https://wiki.flybase.org/wiki/FlyBase:Downloads_Overview
- category: Product
  description: Gene, transcript, and protein sequence data for Drosophila in FASTA
    format, including CDS, UTRs, and polypeptide sequences
  format: fasta
  id: flybase.gene.sequences.fasta
  name: FlyBase Gene Sequences
  original_source:
  - flybase
  product_url: https://wiki.flybase.org/wiki/FlyBase:Downloads_Overview
- category: Product
  description: Bulk data files containing gene annotations, phenotypes, interactions,
    expression data, stocks, and orthology information in tab-separated format
  format: tsv
  id: flybase.bulk.data
  name: FlyBase Bulk Data Files
  original_source:
  - flybase
  product_url: https://wiki.flybase.org/wiki/FlyBase:Downloads_Overview
- category: GraphicalInterface
  description: Interactive genome browser for visualizing Drosophila genomes, gene
    models, expression data, and genomic features using JBrowse technology
  id: flybase.jbrowse
  name: FlyBase JBrowse Genome Browser
  original_source:
  - flybase
  product_url: https://flybase.org/
- category: GraphicalInterface
  description: Web-based search and query interface for accessing FlyBase data, including
    gene information, phenotypes, stocks, and literature
  id: flybase.web.interface
  name: FlyBase Web Interface
  original_source:
  - flybase
  product_url: https://flybase.org/
- category: GraphicalInterface
  description: Web portal for searching and browsing ncRNA sequences, structures,
    and annotations
  format: http
  id: rnacentral.portal
  name: RNAcentral Portal
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to RNAcentral data
  format: http
  id: rnacentral.api
  name: RNAcentral REST API
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/api
- category: Product
  description: FTP archive with current and archived release files (sequences and
    annotations)
  format: http
  id: rnacentral.ftp
  name: RNAcentral FTP Archive
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
- category: DataModelProduct
  description: Public PostgreSQL database for direct SQL access to RNAcentral data
  format: postgres
  id: rnacentral.public-db
  name: RNAcentral Public Postgres Database
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/help/public-database
- category: Product
  description: Model organism data from FlyBase, SGD, ZFIN and other model organism
    databases
  format: http
  id: genecards.model.organisms
  name: GeneCards Model Organism Data
  original_source:
  - flybase
  - sgd
  - zfin
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-15_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-07_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-23: HTTP 403 error
    when accessing file'
repository: https://github.com/FlyBase
taxon:
- NCBITaxon:7227
---
# FlyBase

## Overview

FlyBase is a comprehensive genomic database and knowledge base for the model organism *Drosophila melanogaster* (fruit fly) and related Drosophila species. It serves as the central repository for curated genetic, genomic, and biological information about Drosophila, supporting research in genetics, genomics, developmental biology, and disease modeling.

## Key Features

- **Genome Data**: Complete genome sequences and annotations for *D. melanogaster* and other Drosophila species
- **Gene Information**: Detailed gene pages with nomenclature, sequences, structures, and functional annotations
- **Phenotype Data**: Curated phenotypic information from genetic studies and allele characterizations
- **Expression Data**: Gene expression patterns across development and tissues (RNA-seq, in situ data)
- **Genetic Interactions**: Documented genetic and physical interactions between genes
- **Disease Models**: Human disease gene associations and Drosophila disease models
- **Stocks & Reagents**: Information about available stocks, antibodies, and experimental tools
- **Literature**: Integrated bibliography with curated data from publications
- **Orthology**: Cross-species gene relationships and comparative genomics data

## Data Types

FlyBase provides access to:
- Gene models and genome annotations (GFF3 format)
- DNA, RNA, and protein sequences (FASTA format)
- Bulk downloadable data files (TSV format)
- Genetic variants and allele information
- Stock center resources and reagent catalogs
- Expression data from multiple experimental platforms
- Protein interaction networks
- Phenotype annotations with controlled vocabularies
- Disease model associations

## Research Applications

FlyBase supports:
- Genome annotation and comparative genomics
- Functional genetics and phenotype analysis
- Gene expression studies across development
- Disease modeling and translational research
- Evolutionary biology and phylogenetics
- Systems biology and network analysis
- Educational resources for teaching genetics

## Data Downloads

FlyBase provides comprehensive bulk data downloads through their FTP site, including:
- GFF3 genome annotation files
- FASTA sequence files (genome, gene, transcript, protein)
- Tab-separated data files for genes, alleles, phenotypes, interactions
- Ontology files and controlled vocabularies
- Stock and reagent information
- Bibliography and literature references

Access downloads at: https://wiki.flybase.org/wiki/FlyBase:Downloads_Overview