---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: jakelever
  label: Jake Lever
creation_date: '2025-10-30T00:00:00Z'
description: PGxMine uses text mining to identify pharmacogenomic associations between chemicals and genetic variants in the biomedical literature to assist curation of PharmGKB. The system uses the Kindred relation classifier along with PubTator annotations to extract chemical-variant associations from PubMed, PubMed Central Open Access, and PubMed Central Author Manuscript Collection.
domains:
- pharmacology
- genomics
- literature
- precision medicine
homepage_url: https://pgxmine.pharmgkb.org/
id: pgxmine
infores_id: pgxmine
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT
name: PGxMine
products:
- category: GraphicalInterface
  description: Interactive Shiny web application for browsing and filtering text-mined pharmacogenomic associations
  format: http
  id: pgxmine.viewer
  name: PGxMine Shiny Viewer
  original_source:
  - pgxmine
  product_url: https://pgxmine.pharmgkb.org/
- category: Product
  description: Collated chemical-variant associations with citation counts, normalized to PharmGKB, dbSNP, and Entrez identifiers
  format: tsv
  id: pgxmine.collated
  name: PGxMine Collated Associations
  original_source:
  - pgxmine
  product_file_size: 2306867
  product_url: https://doi.org/10.5281/zenodo.6617348
- category: Product
  description: Supporting sentences for chemical-variant associations with publication metadata
  format: tsv
  id: pgxmine.sentences
  name: PGxMine Sentences
  original_source:
  - pgxmine
  product_file_size: 115867935
  product_url: https://doi.org/10.5281/zenodo.6617348
- category: ProcessProduct
  description: Python codebase for extracting pharmacogenomic associations using text mining
  id: pgxmine.code
  name: PGxMine Code
  original_source:
  - pgxmine
  product_url: https://github.com/jakelever/pgxmine
repository: https://github.com/jakelever/pgxmine
synonyms:
- PGxMine
---

# PGxMine

## Overview

PGxMine is a text mining system designed to extract pharmacogenomic associations from biomedical literature to assist in the curation of PharmGKB. The system processes millions of documents from PubMed, PubMed Central Open Access, and the PubMed Central Author Manuscript Collection to identify relationships between chemicals (drugs) and genetic variants.

The project uses advanced natural language processing, including the Kindred relation classifier and scispacy, combined with PubTator for entity recognition. PGxMine specifically targets associations between chemical compounds and genetic variants, including rsIDs, star alleles (e.g., CYP2D6*4), and other variant nomenclature.

## Data Content

### Chemical-Variant Associations
PGxMine extracts chemical-variant associations from the biomedical literature with:
- **Normalized chemical identifiers**: Mapped to PharmGKB drug IDs and MeSH terms
- **Variant identifiers**: Including dbSNP rsIDs, star alleles, and gene names from Entrez
- **Supporting evidence**: Citation counts and specific sentences supporting each association
- **Corpus coverage**: Processes PubMed, PubMed Central Open Access, and Author Manuscripts

### Data Products
The system provides three main TSV files:
1. **Collated associations**: Chemical-variant pairs with citation counts and normalized identifiers
2. **Supporting sentences**: Full sentences with publication metadata for each association
3. **Unfiltered results**: Raw predictions for researchers who want to apply their own filtering

## Key Features

- **Relation classification**: Uses supervised machine learning (Kindred) to classify pharmacogenomic relationships
- **Entity normalization**: Links variants to genes via dbSNP and maps chemicals to PharmGKB IDs
- **Star allele detection**: Specialized pattern matching for pharmacogenomic star allele nomenclature
- **MeSH filtering**: Identifies age-specific pharmacogenomic information (pediatric, pregnancy)
- **Interactive viewer**: R Shiny web application for browsing and filtering results
- **Reproducible pipeline**: Snakemake workflow for full pipeline execution

## Access Methods

1. **Web Interface**: Browse associations through the interactive Shiny viewer at https://pgxmine.pharmgkb.org/
2. **Direct Download**: Access TSV files via Zenodo (DOI: 10.5281/zenodo.3360930)
3. **Local Installation**: Run the Shiny viewer locally using code from the GitHub repository
4. **Custom Pipeline**: Execute the full text mining pipeline on custom corpora using provided code

## Technology Stack

- **Python 3**: Core implementation language
- **Kindred**: Relation extraction framework
- **scispacy**: Scientific text processing
- **PubTator**: Entity recognition and normalization
- **BioText**: PubMed/PMC document management
- **R Shiny**: Interactive web interface
- **Snakemake**: Workflow management

## Use Cases

1. **PharmGKB Curation**: Prioritize publications for manual curation of pharmacogenomic associations
2. **Literature Surveillance**: Identify new chemical-variant associations as they appear in literature
3. **Evidence Synthesis**: Aggregate supporting evidence for known pharmacogenomic relationships
4. **Database Development**: Source material for building pharmacogenomics knowledge bases
5. **Research Discovery**: Explore potential pharmacogenomic interactions for hypothesis generation

## Data Dependencies

PGxMine integrates data from multiple sources:
- **MeSH**: Medical Subject Headings for drug categorization
- **DrugBank**: Drug filtering by therapeutic categories
- **PharmGKB**: Drug list and identifier mappings
- **dbSNP**: rsID to gene name mappings
- **Entrez Gene**: Gene nomenclature and identifiers
- **PubTator**: Entity annotations in PubMed/PMC

## Management

Developed and maintained by Jake Lever. The system is designed to support PharmGKB curation efforts by automating the initial identification of relevant pharmacogenomic associations in literature.

## Related Resources

- [PharmGKB](pharmgkb): The Pharmacogenomics Knowledgebase that PGxMine assists in curating
- [PubTator](pubtator): Provides entity annotations used by PGxMine
- [DrugBank](drugbank): Used for drug categorization and filtering

## Last Update

Data files last updated: June 2022 (v10 on Zenodo)

# Text Mined pharmacogenomic polymorphisms

## Overview

Text mined pharmacogenomic polymorphisms to assist curation of PharmGKB.

**Note:** This is a stub entry that was automatically created from the [Translator Information Resource Registry](https://biolink.github.io/information-resource-registry/). It requires manual curation to add complete metadata, products, and additional information.

## Information Resource ID

This resource has the Information Resource identifier: `infores:pgxmine`

## Curation Status

- **Stub**: Yes - needs manual curation
- **Creation Date**: 2025-10-30
- **Original Source**: Translator Information Resource Registry

## What Needs to be Curated

1. **Activity Status**: Verify if this resource is active, inactive, or deprecated
2. **Category**: Confirm the resource category is correct
3. **Description**: Expand and improve the description
4. **Homepage URL**: Verify and update if needed
5. **Products**: Add specific data products/files/APIs offered by this resource
6. **Contacts**: Add contact information
7. **Publications**: Add relevant publications
8. **Domains**: Add relevant domain tags
9. **Repository**: Add code repository if applicable

## Additional Notes
