---
layout: resource_detail
activity_status: active
id: "icees-kg"
name: Exposures KP (icees-kg)
description: The Integrated Clinical and Environmental Exposures Service Knowledge Graph (ICEES KG) is a Translator Knowledge Provider that integrates patient-level clinical data from electronic health records with environmental exposures data including airborne pollutants, landfills, concentrated animal feeding operations, and socio-economic indicators. ICEES KG provides regulatory-compliant open access to integrated clinical and environmental data to support translational research on exposure-driven disease mechanisms and health disparities.
domains:
  - health
  - clinical
  - biomedical
  - public health
category: KnowledgeGraph
contacts:
  - category: Individual
    label: Kara Fecho
    orcid: 0000-0002-6704-9306
    contact_details:
      - contact_type: email
        value: "kfecho@renci.org"
      - contact_type: github
        value: "karafecho"
creation_date: '2025-11-05T00:00:00Z'
last_modified_date: '2025-11-05T00:00:00Z'
homepage_url: 'https://robokop.renci.org/api-docs/docs/automat/icees-kg'
repository: 'https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES'
publications:
  - id: https://doi.org/10.1093/jamia/ocz042
  - id: https://doi.org/10.2196/17964
tags:
  - translator
taxon:
  - NCBITaxon:9606
products:
  - id: "icees-kg.graph"
    name: KGX distribution of the ICEES Exposures KP
    description: KGX distribution of the ICEES Exposures KP in Knowledge Graph Exchange (KGX) format, containing integrated clinical and environmental exposures data as a knowledge graph with 226 nodes and 14,342 edges
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/icees-kg/1.5.0/
    category: GraphProduct
    format: kgx-jsonl
    secondary_source:
      - icees-kg
    original_source:
      - mesh
      - pubchem
      - chembl
      - mondo
      - chebi
      - hp
      - umls
      - hmdb
      - icees-kg
  - id: icees-kg.trapi
    name: ICEES KG TRAPI API
    description: Translator Reasoner API (TRAPI) endpoint for querying ICEES KG using standardized Translator protocols
    product_url: https://robokop.renci.org/api-docs/docs/automat/icees-kg-trapi
    category: ProgrammingInterface
    format: http
    secondary_source:
      - icees-kg
    original_source:
      - mesh
      - pubchem
      - chembl
      - mondo
      - chebi
      - hp
      - umls
      - hmdb
      - icees-kg
  - id: "icees-kg.metadata"
    name: ICEES KG Metadata
    description: Meta knowledge graph and metadata describing the data sources, node types, edge types, and predicates available in ICEES KG
    product_url: https://robokop.renci.org/api-docs/docs/automat/metadata-metadata-get-icees-kg
    category: Product
    format: json
    secondary_source:
      - icees-kg
    original_source:
      - mesh
      - pubchem
      - chembl
      - mondo
      - chebi
      - hp
      - umls
      - hmdb
      - icees-kg
infores_id: icees-kg
---

## Overview

The Integrated Clinical and Environmental Exposures Service Knowledge Graph (ICEES KG) is a Translator Knowledge Provider that provides regulatory-compliant open access to integrated clinical and environmental exposures data. ICEES KG integrates patient-level clinical data derived from electronic health records, survey data, and clinical research data with environmental exposures data including airborne pollutants, landfills, concentrated animal feeding operations, and various socio-economic indicators.

ICEES KG serves as the knowledge graph representation of the Integrated Clinical and Environmental Exposures Service (ICEES), making this valuable integrated dataset available for computational reasoning and federated query within the NCATS Biomedical Data Translator ecosystem. The knowledge graph provides associations between clinical phenotypes, diseases, medications, and environmental exposures that can be used to investigate exposure-driven disease mechanisms and health disparities.

## Key Features

- **Patient-Level Integration**: Links clinical data from electronic health records with environmental exposures data at the individual patient level
- **Environmental Coverage**: Includes airborne pollutants, landfills, concentrated animal feeding operations, and socio-economic indicators
- **Regulatory Compliance**: Provides open access while maintaining regulatory compliance with patient privacy requirements
- **Translator Integration**: Implements TRAPI (Translator Reasoner API) for standardized query and integration with other Translator Knowledge Providers
- **Federated Querying**: Supports federated queries spanning clinical and environmental knowledge sources via tools like TranQL
- **Statistical Associations**: Provides statistically significant associations between exposures and clinical outcomes
- **Current Version**: Version 8-20-2024 with 226 nodes and 14,342 edges

## Data Sources

ICEES KG integrates data from multiple authoritative sources including:
- **Clinical Data**: Electronic health records from UNC Health and other clinical sources
- **Environmental Data**: EPA air quality data, geographical exposure indicators
- **Terminologies**: MeSH, PubChem, ChEMBL, MONDO, ChEBI, Human Phenotype Ontology, UMLS, HMDB

## Use Cases

ICEES KG has been validated in translational research use cases including:

1. **Sex Differences in Disease**: Identifying diseases differentially associated with males and females, and associated genes and chemical substances for potential therapeutic discovery
2. **Geographic Health Disparities**: Examining diseases differentially expressed in patients living in rural versus urban regions and identifying associated environmental exposures and biomarkers
3. **Exposure-Disease Relationships**: Investigating relationships between environmental exposures (e.g., air pollution, hazardous substances) and pediatric conditions like croup
4. **Drug Repurposing**: Supporting exploratory drug discovery by linking exposure-associated diseases with genes and chemical substances

## Technical Access

ICEES KG is accessible through multiple interfaces:
- **TRAPI Endpoint**: Standard Translator Reasoner API for programmatic access
- **KGX Distribution**: Downloadable knowledge graph in KGX format
- **Cypher Queries**: Direct Neo4j cypher query capability
- **One-Hop Queries**: Simplified interface for single-hop traversals
- **Metadata API**: Machine-readable metadata about the knowledge graph structure

## Translator Ecosystem Role

ICEES KG functions as an Exposures Knowledge Provider within the NCATS Biomedical Data Translator program, enabling researchers to pose translational questions that span clinical observations and environmental factors. The knowledge graph can be queried independently or in federation with other Translator resources like ROBOKOP (Reasoning Over Biomedical Objects linked in Knowledge Oriented Pathways) to generate mechanistic hypotheses about exposure-driven disease mechanisms.
