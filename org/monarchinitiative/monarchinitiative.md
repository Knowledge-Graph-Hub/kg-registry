---
activity_status: active
category: Aggregator
creation_date: '2025-10-30T00:00:00Z'
description: The Monarch Initiative is an international consortium that integrates, aligns, and redistributes cross-species gene, genotype, variant, disease, and phenotype data to improve understanding of genetic disease and support translational research.
domains:
  - genomics
  - biological systems
id: "monarchinitiative"
infores_id: "monarchinitiative"
homepage_url: https://monarchinitiative.org/
last_modified_date: '2025-11-26T00:00:00Z'
layout: resource_detail
name: Monarch Initiative
synonyms:
  - Monarch
  - The Monarch Initiative
contacts:
  - category: Organization
    label: Monarch Initiative
    contact_details:
      - contact_type: email
        value: "info@monarchinitiative.org"
repository: https://github.com/monarch-initiative
products:
  - category: KnowledgeGraph
    description: Monarch Knowledge Graph integrating phenotype, disease, gene data across species
    format: mixed
    id: "monarchinitiative.kg"
    name: Monarch Knowledge Graph
    product_url: https://monarchinitiative.org/
    original_source:
      - monarchinitiative
  - category: ProgrammingInterface
    description: Monarch API for programmatic access to integrated data
    format: http
    id: "monarchinitiative.api"
    name: Monarch API
    product_url: https://api.monarchinitiative.org/api/
    original_source:
      - monarchinitiative
  - category: GraphicalInterface
    description: Web interface for browsing genes, diseases, phenotypes across species
    format: http
    id: "monarchinitiative.portal"
    name: Monarch Web Portal
    product_url: https://monarchinitiative.org/
    original_source:
      - monarchinitiative
publications:
  - id: "https://doi.org/10.1093/nar/gkw1128"
    title: "The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species"
    journal: Nucleic Acids Research
    year: "2017"
---

# Monarch Initiative

## Overview

The Monarch Initiative is an international consortium dedicated to improving the understanding of genetic disease through the integration, alignment, and redistribution of cross-species data. The platform connects phenotypes to genotypes across species, enabling researchers to leverage comparative genomics for translational medicine and rare disease research.

## Key Features

- **Cross-Species Integration**: Connects human disease with model organism data
- **Knowledge Graph**: Comprehensive graph integrating genes, diseases, phenotypes, variants
- **Ontologies**: Uses and develops standardized ontologies (Mondo, HPO, Uberon, Phenio)
- **Open Data**: All data freely available with CC-BY licenses
- **Tools Ecosystem**: Suite of interoperable tools for data integration and analysis
- **API Access**: Programmatic access to all integrated data

## Core Components

### Ontologies
- **Mondo Disease Ontology**: Harmonized disease definitions across resources
- **Human Phenotype Ontology (HPO)**: Standardized phenotypic features
- **Uberon**: Multi-species anatomy ontology
- **Phenio**: Cross-species phenotype ontology
- **Gene Ontology (GO)**: Gene function annotations

### Tools & Infrastructure
- **Exomiser**: Variant prioritization tool
- **LinkML**: Data modeling framework
- **SSSOM**: Simple Standard for Sharing Ontology Mappings
- **OAK (Ontology Access Kit)**: Toolkit for ontology access and processing
- **Biolink Model**: Data model for biomedical knowledge graphs

### Data Integration
- Integrates data from multiple sources:
  - Human genetics databases (OMIM, ClinVar)
  - Model organism databases (MGI, ZFIN, FlyBase, WormBase)
  - Phenotype databases
  - Gene-disease associations
  - Variant annotations

## Applications

- **Rare Disease Diagnosis**: Phenotype-driven differential diagnosis
- **Variant Prioritization**: Identifying pathogenic variants in genomic data
- **Model Organism Research**: Finding relevant animal models for human disease
- **Drug Repurposing**: Identifying therapeutic candidates based on phenotype similarity
- **Translational Research**: Bridging basic research with clinical applications
- **Phenotype Analysis**: Cross-species phenotype comparison

## Technical Infrastructure

### Knowledge Graph
- Neo4j graph database for complex queries
- SPARQL endpoint for semantic web queries
- Regular data releases with versioning
- Extensive cross-references and mappings

### APIs and Access
- RESTful API for programmatic access
- Python and R client libraries
- Bulk downloads available
- GraphQL interface in development

## Development & Governance

### Organization
- International collaborative consortium
- Partner institutions across North America, Europe, and beyond
- Open development via GitHub
- Community-driven governance

### Funding
- NIH National Center for Advancing Translational Sciences (NCATS)
- NIH National Human Genome Research Institute (NHGRI)
- NIH Office of the Director (OD)
- Additional support from multiple agencies and institutions

## Citation

McMurry et al. The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species. Nucleic Acids Research (2017) 45 (D1): D712-D722.

## Information Resource ID

This resource has the Information Resource identifier: `infores:monarchinitiative`
