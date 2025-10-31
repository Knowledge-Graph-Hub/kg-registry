---
activity_status: active
category: Aggregator
creation_date: '2025-10-30T00:00:00Z'
description: MouseMine is an InterMine data warehouse that provides integrated access to mouse genomic, phenotypic, expression, and disease data from Mouse Genome Informatics (MGI).
domains:
  - genomics
  - organisms
  - phenotype
  - health
  - pathways
id: mousemine
infores_id: mousemine
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
name: MouseMine
homepage_url: http://www.mousemine.org/mousemine/begin.do
taxon:
  - NCBITaxon:10090
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.informatics.jax.org/mgihome/support/mgi_inbox.shtml
    label: MGI User Support
products:
  - category: GraphicalInterface
    description: Web-based interface for searching, querying, and analyzing mouse data from MGI through MouseMine
    id: mousemine.web
    name: MouseMine Web Interface
    original_source:
      - mousemine
    product_url: http://www.mousemine.org/mousemine/begin.do
  - category: ProgrammingInterface
    description: Programmatic access to MouseMine data via RESTful web services with client libraries for Perl, Python, Ruby, and Java
    id: mousemine.api
    is_public: true
    name: MouseMine API
    original_source:
      - mousemine
    product_url: http://www.mousemine.org/mousemine/api.do
  - category: GraphicalInterface
    description: Pre-built query templates for common data retrieval tasks covering genome features, proteins, expression, interactions, phenotypes, diseases, and more
    id: mousemine.templates
    name: MouseMine Query Templates
    original_source:
      - mousemine
    product_url: http://www.mousemine.org/mousemine/templates.do
  - category: GraphicalInterface
    description: Custom query construction tool for building complex, iterative queries across multiple data types
    id: mousemine.querybuilder
    name: MouseMine QueryBuilder
    original_source:
      - mousemine
    product_url: http://www.mousemine.org/mousemine/customQuery.do
synonyms:
  - MouseMine
  - Mouse Genome Informatics MouseMine
---

# MouseMine

## Overview

MouseMine is a data warehouse for accessing integrated mouse data from Mouse Genome Informatics (MGI) and other web resources. Built on the InterMine software framework, MouseMine provides powerful tools for querying and analyzing mouse genomic, phenotypic, expression, and disease data. It offers multiple diverse query templates, custom and iterative querying capabilities, and comprehensive programmatic access through web services APIs in Perl, Python, Ruby, and Java.

## Data Content

MouseMine integrates data from multiple MGI resources:

- **Mouse Genome Database (MGD)**: Comprehensive mouse genetic and genomic data
- **Gene Expression Database (GXD)**: Gene expression information
- **Mouse Models of Human Cancer (MMHCdb)**: Cancer-related data
- **Gene Ontology (GO)**: Functional annotations

Data categories include:
- Genome features and coordinates
- Proteins and functional annotations
- Gene expression patterns
- Protein interactions
- Phenotypes and alleles
- Disease associations
- Homology relationships
- Literature references

## Features

- **Search Interface**: Query by gene names, identifiers, phenotypes, diseases, and keywords
- **List Analysis**: Upload and analyze lists of identifiers and symbols
- **Query Templates**: Pre-built queries for common data retrieval tasks
- **QueryBuilder**: Custom query construction for complex data requests
- **Results Management**: Save, combine, and export results from multiple queries
- **Data Export**: Multiple export formats for downstream analysis
- **Cross-species Links**: Integration with other InterMine resources (FlyMine, RatMine, WormMine, YeastMine, ZebrafishMine, HumanMine)

## Access Methods

- **Web Interface**: Interactive browser-based access at http://www.mousemine.org/
- **RESTful APIs**: Programmatic access via Perl, Python, Ruby, and Java client libraries
- **InterMine Mobile App**: Android application for mobile access

## Use Cases

- Retrieving comprehensive gene information for mouse models
- Identifying disease-associated genes and phenotypes
- Exploring gene expression patterns across tissues and developmental stages
- Finding orthologous relationships between mouse and other model organisms
- Bulk data retrieval for computational analyses
- Integration of MGI data into custom workflows via APIs

## Management

MouseMine is a collaboration between:
- Mouse Genome Informatics (MGI) at The Jackson Laboratory
- The InterMine project at the Cambridge Systems Biology Centre

## Funding

Funded by the National Institutes of Health/National Human Genome Research Institute (NIH/NHGRI).
