---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nlm.nih.gov/research/umls/support.html
  label: NLM UMLS Customer Support
creation_date: '2025-10-30T00:00:00Z'
description: The Unified Medical Language System (UMLS) integrates and distributes
  over 200 biomedical vocabularies, terminologies, and classification standards to
  enable interoperability between information systems. It includes the Metathesaurus
  (terms and codes from vocabularies like CPT, ICD-10-CM, LOINC, MeSH, RxNorm, SNOMED
  CT), Semantic Network (broad categories and relationships), and SPECIALIST Lexicon
  (biomedical and general English lexicon with normalization tools).
domains:
- biomedical
- clinical
- literature
homepage_url: https://www.nlm.nih.gov/research/umls/index.html
id: umls
infores_id: umls
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
license:
  id: https://uts.nlm.nih.gov/uts/
  label: UMLS License (free for individuals)
name: Unified Medical Language System
products:
- category: GraphicalInterface
  description: Web interface for browsing UMLS Metathesaurus concepts, CUIs, semantic
    types, and synonymous terms
  format: http
  id: umls.browser
  name: UMLS Metathesaurus Browser
  original_source:
  - umls
  product_url: https://uts.nlm.nih.gov/uts/umls/home
- category: GraphicalInterface
  description: Web interface for viewing semantic types, definitions, and hierarchical
    structure of the UMLS Semantic Network
  format: http
  id: umls.semantic_network_browser
  name: UMLS Semantic Network Browser
  original_source:
  - umls
  product_url: https://uts.nlm.nih.gov/uts/umls/semantic-network/root
- category: ProgrammingInterface
  description: REST API providing programmatic access to UMLS Metathesaurus, Semantic
    Network, and related terminology services
  id: umls.api
  is_public: true
  name: UMLS Terminology Services API
  original_source:
  - umls
  product_url: https://documentation.uts.nlm.nih.gov/rest/home.html
- category: Product
  description: Full UMLS Knowledge Sources release including Metathesaurus, Semantic
    Network, and SPECIALIST Lexicon for local installation with MetamorphoSys customization
    tool
  id: umls.release
  name: UMLS Knowledge Sources Release Files
  product_url: https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html
- category: ProcessProduct
  description: MetamorphoSys tool for customizing UMLS subsets by vocabulary, language,
    or semantic type and loading data into local databases
  id: umls.metamorphosys
  name: MetamorphoSys Customization Tool
  product_url: https://www.nlm.nih.gov/research/umls/implementation_resources/metamorphosys/help.html
- category: ProcessProduct
  description: SPECIALIST Lexicon and Lexical Tools for normalizing strings, generating
    lexical variants, and creating indexes for biomedical text processing
  id: umls.specialist_lexicon
  name: SPECIALIST Lexicon and Lexical Tools
  original_source:
  - umls
  product_url: https://lhncbc.nlm.nih.gov/LSG/index.html
publications:
- id: PMID:14681409
  title: 'The Unified Medical Language System (UMLS): integrating biomedical terminology.'
  preferred: true
synonyms:
- UMLS
---

# Unified Medical Language System (UMLS)

## Overview

The Unified Medical Language System (UMLS) is a comprehensive set of files and software developed by the U.S. National Library of Medicine (NLM) that brings together over 200 health and biomedical vocabularies and standards to facilitate interoperability between computer systems. The UMLS enables linking of different medical terminologies and codes used by physicians, pharmacies, insurance companies, hospitals, and research institutions.

## Three Knowledge Sources

### 1. Metathesaurus
The Metathesaurus is the largest component, containing:
- Terms and codes from many vocabularies including:
  - CPT (Current Procedural Terminology)
  - ICD-10-CM (International Classification of Diseases)
  - LOINC (Logical Observation Identifiers Names and Codes)
  - MeSH (Medical Subject Headings)
  - RxNorm (normalized drug names)
  - SNOMED CT (Systematized Nomenclature of Medicine Clinical Terms)
- Hierarchical relationships
- Definitions and other attributes
- Concept Unique Identifiers (CUIs) linking synonymous terms across vocabularies

### 2. Semantic Network
Provides a consistent categorization of all concepts represented in the Metathesaurus through:
- 133 broad categories (semantic types) such as "Disease or Syndrome," "Pharmacologic Substance"
- 54 relationships (semantic relations) defining interactions between semantic types

### 3. SPECIALIST Lexicon and Lexical Tools
- Large syntactic lexicon covering biomedical and general English
- Tools for normalizing strings, generating lexical variants, and creating indexes
- Supports natural language processing of biomedical text

## Use Cases

The UMLS can be used to:
- Link terminology between healthcare providers, pharmacies, and insurance companies
- Coordinate patient care across hospital departments
- Process clinical texts to extract concepts and relationships
- Map between different terminologies
- Develop information retrieval systems
- Extract custom terminologies from the Metathesaurus
- Build and maintain local terminology services
- Research terminologies and ontologies

## Access Methods

### Web Browsers
- Metathesaurus Browser for searching concepts and relationships
- Semantic Network Browser for exploring semantic types and relations

### Local Installation
- Download full UMLS release files
- Customize using MetamorphoSys tool
- Load into local database systems (MySQL, Oracle, etc.)

### Programmatic Access
- REST API for querying UMLS data within applications
- Comprehensive API documentation available

## Licensing

- Free licensing for individuals (not groups or organizations)
- UMLS Terminology Services (UTS) account required
- No charge for SNOMED CT use in United States and member countries
- Some vocabularies may require additional agreements with vendors

## Maintained By

National Library of Medicine, National Institutes of Health, U.S. Department of Health and Human Services
