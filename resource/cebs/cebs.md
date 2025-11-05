---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://manticore.niehs.nih.gov/cebssearch/
  label: NIEHS
creation_date: '2025-11-05T00:00:00Z'
description: Chemical Effects in Biological Systems (CEBS) is a public, web-accessible, manually curated repository of toxicology study data from the National Toxicology Program (NTP) and other research programs. CEBS contains individual-level and summarized study data from carcinogenicity studies, short-term toxicity studies, genetic toxicity assays, and other toxicological investigations. The database integrates chemical structure information, study designs, experimental conditions, and biological effects to support toxicology research and risk assessment.
domains:
  - toxicology
  - biomedical
  - health
  - public health
homepage_url: https://manticore.niehs.nih.gov/cebssearch/
id: cebs
infores_id: cebs
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: CEBS
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing CEBS toxicology data
  format: http
  id: cebs.web
  name: CEBS Search Interface
  original_source:
  - cebs
  product_url: https://manticore.niehs.nih.gov/cebssearch/
- category: Product
  description: Toxicology study data from NTP and other programs
  format: mixed
  id: cebs.data
  name: CEBS Study Data
  original_source:
  - cebs
  product_url: https://manticore.niehs.nih.gov/cebssearch/
- category: ProgrammingInterface
  description: API access to CEBS data
  format: http
  id: cebs.api
  name: CEBS API
  original_source:
  - cebs
  product_url: https://manticore.niehs.nih.gov/cebssearch/
synonyms:
  - CEBS
  - Chemical Effects in Biological Systems
---

# Chemical Effects in Biological Systems

## Overview

Chemical Effects in Biological Systems (CEBS) is a public, web-accessible, manually curated repository of toxicology study data from the National Toxicology Program (NTP) and other research programs.

CEBS contains comprehensive data from multiple study types including carcinogenicity studies, short-term toxicity studies, genetic toxicity assays, reproductive and developmental toxicity studies, and other toxicological investigations. The database provides detailed information at both individual animal and study summary levels.

## Key Features

- **Comprehensive Study Data**: Individual-level and summarized toxicology data
- **Multiple Study Types**: Carcinogenicity, acute/chronic toxicity, genetic toxicity, reproductive/developmental toxicity
- **Chemical Information**: Integrated with chemical structure and properties
- **Study Metadata**: Detailed experimental designs, dosing regimens, and conditions
- **Pathology Data**: Histopathological findings and lesion classifications
- **Public Access**: Free access for research and regulatory purposes

## Research Applications

- Toxicology research and hypothesis generation
- Risk assessment and safety evaluation
- Computational toxicology modeling
- Adverse outcome pathway (AOP) development
- Cross-study comparisons and meta-analysis
- Support for read-across and QSAR approaches

## Products

### CEBS Search Interface
Web-based interface for querying and browsing NTP toxicology studies with advanced search capabilities.

### CEBS Study Data
Downloadable toxicology study data including individual animal data, pathology findings, and study summaries.

### CEBS API
Programmatic access to CEBS data for computational toxicology applications.

## Information Resource ID

This resource has the Information Resource identifier: `infores:cebs`

## Domains

- Toxicology
- Biomedical
- Health
- Public Health
