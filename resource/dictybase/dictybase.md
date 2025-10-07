---
activity_status: active
category: DataSource
creation_date: '2025-08-13T00:00:00Z'
description: dictyBase is a comprehensive genomic database for the social amoeba Dictyostelium discoideum and related species. It provides genomic, phenotypic, and molecular data including gene annotations, protein sequences, expression data, phenotypes, literature, and community annotations. The database serves as the central resource for Dictyostelium researchers worldwide.
domains:
  - genomics
  - organisms
  - biological systems
homepage_url: https://dictybase.dev/
id: dictybase
last_modified_date: '2025-10-07T00:00:00Z'
layout: resource_detail
name: dictyBase
repository: https://github.com/dictybase
products:
  - category: Product
    description: Genome assembly and annotations in GFF format
    format: gff
    id: dictybase.annotations.gff
    name: dictyBase Genome Annotations
    product_url: https://dictybase.dev/downloads
  - category: Product
    description: Genome sequence data in FASTA format
    format: fasta
    id: dictybase.genome.fasta
    name: dictyBase Genome Sequences
    product_url: https://dictybase.dev/downloads
  - category: Product
    description: Protein sequence data in FASTA format
    format: fasta
    id: dictybase.proteins.fasta
    name: dictyBase Protein Sequences
    product_url: https://dictybase.dev/downloads
  - category: ProgrammingInterface
    description: GraphQL API for programmatic access to dictyBase data
    format: graphql
    id: dictybase.graphql.api
    name: dictyBase GraphQL API
    product_url: https://dictybase.dev/graphql
  - category: GraphicalInterface
    description: Web-based browser for exploring Dictyostelium genomes and annotations
    id: dictybase.genome.browser
    name: dictyBase Genome Browser
    product_url: https://dictybase.dev/
---

# dictyBase

## Overview

dictyBase is the central online resource for the Dictyostelium research community. It provides comprehensive genomic and biological information about *Dictyostelium discoideum*, a social amoeba that serves as an important model organism for studying cell differentiation, signal transduction, cell motility, and social evolution.

## Key Features

- **Genome Data**: Complete genome assemblies and annotations for multiple Dictyostelium species
- **Gene Information**: Detailed gene pages with sequences, structures, and functional annotations
- **Phenotype Data**: Curated phenotype information from genetic studies
- **Expression Data**: Gene expression data from various developmental stages and conditions
- **Literature**: Integrated literature references and community annotations
- **Tools**: Genome browser, BLAST search, and other analysis tools

## Data Resources

dictyBase provides various downloadable datasets including:

- Genome assemblies (FASTA format)
- Gene annotations (GFF format)
- Protein sequences (FASTA format)
- RNA sequences
- Functional annotations

## Access

dictyBase data is freely accessible through:
- Web interface at https://dictybase.dev/
- GraphQL API for programmatic access
- Downloadable data files
