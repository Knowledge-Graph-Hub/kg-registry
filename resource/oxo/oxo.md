---
activity_status: inactive
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: ols-support@ebi.ac.uk
  - contact_type: github
    value: EBISPOT
  id: ebi
  label: EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT)
creation_date: '2025-11-04T00:00:00Z'
description: OxO (Ontology Xref Service) is a cross-ontology mapping service developed
  by EMBL-EBI's Samples, Phenotypes and Ontologies Team (SPOT). The service provides
  mappings between terms from different ontologies, enabling users to search for equivalent
  or related terms across multiple ontological resources. OxO aggregates cross-references
  from ontologies loaded in the Ontology Lookup Service (OLS) and enriches these with
  manual mappings and inference-based relationships.
domains:
- biomedical
- upper
- biological systems
homepage_url: https://www.ebi.ac.uk/spot/oxo/
id: oxo
infores_id: oxo
last_modified_date: '2025-11-04T00:00:00Z'
layout: resource_detail
name: Ontology Xref Service
products:
- category: ProgrammingInterface
  description: RESTful API for programmatic access to cross-ontology mappings and
    term equivalence searches
  format: http
  id: oxo.api
  name: OxO REST API
  original_source:
  - oxo
  product_url: https://www.ebi.ac.uk/spot/oxo/docs/api
- category: GraphicalInterface
  description: Web-based interface for searching and browsing ontology cross-references
    and mappings
  format: http
  id: oxo.portal
  name: OxO Web Interface
  original_source:
  - oxo
  product_url: https://www.ebi.ac.uk/spot/oxo/
repository: https://github.com/EBISPOT/OXO
synonyms:
- OxO
---

# Ontology Xref Service (OxO)

## Overview

OxO (Ontology Xref Service) is a service developed and maintained by EMBL-EBI's Samples, Phenotypes and Ontologies Team (SPOT) for cross-ontology term mapping. The service facilitates the discovery of mappings between terms from different ontological resources, enabling data integration and interoperability across biomedical databases and tools.

## Current Status

⚠️ **Service Alert**: As of November 2025, the OxO website is experiencing technical issues and returning HTTP 500 server errors. The service may be temporarily unavailable or under maintenance.

## Purpose

OxO serves to:
- Provide mappings between equivalent or related terms across different ontologies
- Facilitate data integration across heterogeneous biomedical resources
- Enable cross-ontology searches and term translation
- Support semantic interoperability in biomedical research

## Data Sources

OxO aggregates cross-reference data from:
- **Ontology Lookup Service (OLS)**: Cross-references embedded in ontologies
- **Manual Mappings**: Curated mappings contributed by domain experts
- **Inference-Based Mappings**: Automatically generated mappings based on term relationships

## Key Features

### Cross-Ontology Mapping
Search for equivalent or related terms across multiple ontologies, enabling translation between different vocabular systems.

### Mapping Provenance
Understand the source and reliability of mappings, with information about whether mappings are:
- Direct cross-references from ontology files
- Manually curated by experts
- Inferred through reasoning

### Programmatic Access
REST API for integration into computational workflows and applications.

## Related Services

OxO is part of the SPOT suite of ontology services at EMBL-EBI:
- **OLS (Ontology Lookup Service)**: Repository and browser for biomedical ontologies
- **ZOOMA**: Service for mapping free-text annotations to ontology terms

## Information Resource ID

This resource has the Information Resource identifier: `infores:oxo`

## Contact and Support

For questions or issues regarding OxO:
- **Email**: ols-support@ebi.ac.uk
- **Organization**: EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT)

## Use Cases

1. **Data Integration**: Mapping identifiers when merging datasets using different ontologies
2. **Ontology Alignment**: Finding equivalent terms for ontology harmonization projects
3. **Cross-Database Queries**: Translating queries across databases using different terminologies
4. **Semantic Interoperability**: Enabling communication between systems using different vocabularies