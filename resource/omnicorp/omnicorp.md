---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
  label: NCATS Translator
creation_date: '2025-11-05T00:00:00Z'
description: OmniCorp provides co-occurrence data derived from PubMed abstracts, enabling researchers to identify and quantify relationships between biomedical concepts based on their frequency of co-mention in the literature. This resource is part of the NCATS Translator infrastructure and supports literature-based discovery and evidence aggregation for knowledge graph construction.
domains:
  - literature
  - biomedical
  - translational
id: omnicorp
infores_id: omnicorp
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: OmniCorp
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
products:
- category: Product
  description: Co-occurrence data from PubMed abstracts
  format: mixed
  id: omnicorp.cooccurrence
  name: OmniCorp Co-occurrence Data
  original_source:
  - pubmed
  secondary_source:
  - omnicorp
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
- category: ProgrammingInterface
  description: API access to OmniCorp co-occurrence data
  format: http
  id: omnicorp.api
  name: OmniCorp API
  original_source:
  - pubmed
  secondary_source:
  - omnicorp
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
synonyms:
  - OmniCorp
tags:
- translator
---

# OmniCorp

## Overview

OmniCorp provides co-occurrence data derived from PubMed abstracts, enabling researchers to identify and quantify relationships between biomedical concepts based on their frequency of co-mention in the literature. 

This resource is part of the NCATS Translator infrastructure and supports literature-based discovery and evidence aggregation for knowledge graph construction. By analyzing the co-occurrence of biomedical entities (genes, diseases, drugs, phenotypes, etc.) in PubMed literature, OmniCorp helps identify potential relationships and generate hypotheses for further investigation.

## Key Features

- **Literature-Based Discovery**: Identifies relationships between biomedical concepts based on co-occurrence in scientific literature
- **PubMed Coverage**: Comprehensive analysis of PubMed abstracts
- **Translator Integration**: Part of the NCATS Biomedical Data Translator ecosystem
- **Quantitative Analysis**: Provides frequency counts and statistical measures of co-occurrence

## Products

### Co-occurrence Data
OmniCorp provides downloadable co-occurrence data files and API access for programmatic retrieval of co-occurrence statistics between biomedical concepts.

## Information Resource ID

This resource has the Information Resource identifier: `infores:omnicorp`

## Domains

- Literature
- Biomedical
- Translational

## Tags

- NCATS Translator

