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
description: OmniCorp is a NCATS Translator literature co-occurrence database that
  runs named-entity recognition and entity linking over public PubMed abstracts to
  count publications containing individual Biolink-relevant entities and pairs of
  co-mentioned entities. It supports literature-based discovery and evidence augmentation
  by adding co-occurrence counts or literature co-occurrence edges to TRAPI messages.
domains:
  - literature
  - biomedical
id: omnicorp
infores_id: omnicorp
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: OmniCorp
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
products:
  - category: Product
    description: Co-occurrence database generated from public PubMed abstracts with
      entity normalization for Biolink-relevant biomedical concepts
    format: mixed
    id: omnicorp.cooccurrence
    name: OmniCorp Co-occurrence Data
    original_source:
      - source: omnicorp
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: biolink
        relation_type: prov:used
    product_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
  - category: ProgrammingInterface
    description: API behavior documented for adding co-occurrence counts and literature
      co-occurrence edges to TRAPI messages
    format: http
    id: omnicorp.api
    name: OmniCorp API
    original_source:
      - source: omnicorp
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: biolink
        relation_type: prov:used
    product_url: https://github.com/NCATSTranslator/Translator-All/wiki/OmniCorp
    warnings:
      - The registry points to the Translator wiki documentation; checked RENCI OmniCorp service URLs were unavailable or had certificate issues on 2026-06-02.
repository: https://github.com/NCATS-Gamma/omnicorp
synonyms:
  - OmniCorp
tags:
  - translator
---

# OmniCorp

## Overview

OmniCorp provides co-occurrence data derived from PubMed abstracts, enabling researchers to identify and quantify relationships between biomedical concepts based on their frequency of co-mention in the literature.

This resource is part of the NCATS Translator infrastructure and supports literature-based discovery and evidence aggregation for knowledge graph construction. By analyzing the co-occurrence of Biolink-relevant biomedical entities in PubMed literature, OmniCorp helps identify potential relationships and generate hypotheses for further investigation.

## Key Features

- **Literature-Based Discovery**: Identifies relationships between biomedical concepts based on co-occurrence in scientific literature
- **PubMed Coverage**: Comprehensive analysis of PubMed abstracts
- **Translator Integration**: Part of the NCATS Biomedical Data Translator ecosystem
- **Quantitative Analysis**: Provides frequency counts and statistical measures of co-occurrence

## Products

### Co-occurrence Data
OmniCorp provides co-occurrence counts and can add literature co-occurrence evidence to TRAPI messages. The registry currently points to the Translator wiki documentation and source repository rather than a verified live API URL.

## Information Resource ID

This resource has the Information Resource identifier: `infores:omnicorp`

## Domains

- Literature
- Biomedical
- Translational

## Tags

- NCATS Translator
