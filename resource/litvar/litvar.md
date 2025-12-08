---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: zhiyong.lu@nih.gov
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/research/bionlp/
  id: ncbi
  label: NCBI Computational Biology Branch
creation_date: '2025-11-08T00:00:00Z'
description: LitVar is a comprehensive NCBI web service for searching and retrieving
  variant-specific information from the biomedical literature using advanced text
  mining and machine learning techniques. Developed by the National Library of Medicine's
  Computational Biology Branch, LitVar automatically extracts variant-related information
  from over 35 million PubMed articles and 5.7 million full-text articles in PubMed
  Central including supplementary materials, with monthly updates to capture the latest
  research. A key innovation of LitVar is its sophisticated variant normalization
  system that standardizes different forms of the same variant into unique identifiers,
  enabling comprehensive search results regardless of which variant nomenclature is
  used in the query, whether protein level names, DNA level annotations, dbSNP RS
  identifiers, ClinGen identifiers, or SPDI format. LitVar leverages PubTator, a state-of-the-art
  literature annotation tool, to identify and display key biological entities including
  genes, diseases, drugs, chemicals, and mutations within retrieved articles, providing
  rich contextual information around variants of interest.
domains:
- genomics
- literature
homepage_url: https://www.ncbi.nlm.nih.gov/research/litvar2/
id: litvar
infores_id: litvar
last_modified_date: '2025-11-08T00:00:00Z'
layout: resource_detail
name: LitVar
products:
- category: GraphicalInterface
  description: Web interface for searching and retrieving variant information from
    35+ million PubMed articles with autocomplete, filtering, and entity highlighting
  format: http
  id: litvar.web_interface
  name: LitVar Web Interface
  product_url: https://www.ncbi.nlm.nih.gov/research/litvar2/
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to variant summaries, publications,
    search, and gene-level variant queries
  format: http
  id: litvar.api
  name: LitVar API
  product_url: https://www.ncbi.nlm.nih.gov/research/litvar2/api
publications:
- authors:
  - Alexis Allot
  - Chih-Hsuan Wei
  - Lon Phan
  - Timothy Hefferon
  - Melissa Landrum
  - Heidi L. Rehm
  - Zhiyong Lu
  doi: 10.1038/s41588-023-01414-x
  id: litvar_2023
  journal: Nature Genetics
  preferred: true
  title: Tracking genetic variants in the biomedical literature using LitVar 2.0
  year: '2023'
taxon:
- NCBITaxon:9606
---

# LitVar

## Overview

LitVar is the National Center for Biotechnology Information's advanced literature search tool specifically designed for tracking genetic variants in the biomedical literature. Using sophisticated text mining and natural language processing, LitVar provides comprehensive access to variant information extracted from millions of scientific publications.

## Information Resource ID

This resource has the Information Resource identifier: `infores:litvar`

## Key Features

### Variant Normalization
LitVar's core strength lies in its ability to normalize different representations of the same variant into a standardized form. Users can search using any of the following formats and retrieve the same comprehensive results:
- Protein-level names (e.g., P871L, p.P871L, Pro871Leu)
- DNA-level annotations (e.g., c.2612C>T, g.13843A>G)
- dbSNP RS identifiers (e.g., rs799917)
- ClinGen identifiers (e.g., CA123643)
- SPDI format (e.g., NC_000007.14:140753335:A:C)
- Gene plus variant combinations (e.g., BRCA1 P871L)

### Literature Coverage
- Over 35 million PubMed articles
- 5.7 million full-text articles from PubMed Central
- Supplementary materials from applicable PMC articles
- Monthly updates to capture latest research

### Entity Annotation
LitVar integrates PubTator technology to automatically identify and highlight biological entities within articles:
- Genetic variants and mutations
- Genes and gene symbols
- Diseases and phenotypes
- Drugs and chemicals
- Providing contextual relationships between variants and related concepts

### Search and Discovery
- **Autocomplete**: Real-time suggestions as users type queries
- **Gene-level search**: Find all variants associated with a specific gene
- **Keyword filtering**: Combine variant searches with additional text terms
- **Multi-variant queries**: Search for multiple variants simultaneously
- **Publication filters**: Filter by section, journal, date, and publication type
- **Ranking options**: Sort by relevance (BM25 algorithm) or date

### Result Presentation
For each variant, LitVar provides:
- Standardized variant identifier and nomenclature
- Associated genes and their relationships
- Related diseases and phenotypes
- Drug and chemical interactions
- Complete publication list with highlighted sections
- Statistics on publication trends over time

## Data Access

### Web Interface
User-friendly search interface with autocomplete, filters, and interactive visualization of results. Downloads available in TSV format for PMIDs.

### RESTful API
Comprehensive programmatic access including:
- **Variant Summary**: Detailed information about specific variants
- **Search Variant**: Autocomplete and search functionality
- **Variant Publications**: PMIDs and PMCIDs for all publications mentioning a variant
- **Variants for Gene**: All variants associated with a specific gene
- **Sensor**: Integration endpoint for external tools

### RSS Feeds
Subscribe to updates for specific variants to track new publications automatically.

## Technology Foundation

LitVar is powered by cutting-edge NLP tools developed by NCBI:
- **tmVar 3.0**: Advanced variant recognition and normalization
- **PubTator**: Entity recognition and annotation
- **TaggerOne**: Multi-entity recognition
- **GNormPlus**: Gene normalization
- **SR4GN**: Species recognition
- **SimConcept**: Concept similarity

## Use Cases

- **Clinical genetics**: Assess pathogenicity and clinical significance of variants
- **Genetic counseling**: Find literature support for variant interpretation
- **Research**: Track variant studies and relationships
- **Database curation**: Identify literature for variant annotation
- **Drug development**: Understand variant-drug relationships
- **Precision medicine**: Connect genomic findings to published evidence

## Maintenance and Support

LitVar is maintained by NCBI's Computational Biology Branch with monthly data updates incorporating new publications and improved text mining algorithms. Free access without registration requirements ensures broad availability to the research and clinical communities.