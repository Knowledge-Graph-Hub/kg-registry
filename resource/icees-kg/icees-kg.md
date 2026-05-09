---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: kfecho@renci.org
      - contact_type: github
        value: karafecho
    label: Kara Fecho
    orcid: 0000-0002-6704-9306
creation_date: '2025-11-05T00:00:00Z'
description: The Integrated Clinical and Environmental Exposures Service Knowledge Graph (ICEES KG) is a Translator Knowledge Provider that integrates patient-level clinical data from electronic health records with environmental exposures data including airborne pollutants, landfills, concentrated animal feeding operations, and socio-economic indicators. ICEES KG provides regulatory-compliant open access to integrated clinical and environmental data to support translational research on exposure-driven disease mechanisms and health disparities.
domains:
  - health
  - clinical
  - biomedical
  - public health
homepage_url: https://robokop.renci.org/api-docs/docs/automat/icees-kg
id: icees-kg
infores_id: icees-kg
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: Exposures KP (icees-kg)
products:
  - category: GraphProduct
    description: KGX distribution of the ICEES Exposures KP in Knowledge Graph Exchange (KGX) format, containing integrated clinical and environmental exposures data as a knowledge graph with 226 nodes and 14,342 edges
    format: kgx-jsonl
    id: icees-kg.graph
    name: KGX distribution of the ICEES Exposures KP
    original_source:
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: icees-kg
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/icees-kg/1.5.0/
    secondary_source:
      - source: icees-kg
        relation_type: prov:wasInfluencedBy
  - category: ProgrammingInterface
    description: Translator Reasoner API (TRAPI) endpoint for querying ICEES KG using standardized Translator protocols
    format: http
    id: icees-kg.trapi
    name: ICEES KG TRAPI API
    original_source:
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: icees-kg
        relation_type: prov:hadPrimarySource
    product_url: https://robokop.renci.org/api-docs/docs/automat/icees-kg-trapi
    secondary_source:
      - source: icees-kg
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: Meta knowledge graph and metadata describing the data sources, node types, edge types, and predicates available in ICEES KG
    format: json
    id: icees-kg.metadata
    name: ICEES KG Metadata
    original_source:
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: icees-kg
        relation_type: prov:hadPrimarySource
    product_url: https://robokop.renci.org/api-docs/docs/automat/metadata-metadata-get-icees-kg
    secondary_source:
      - source: icees-kg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    compatibility:
      - standard: biolink
        version: 4.3.6
    description: KGX JSONL graph package for ICEES distributed via the NCATS Translator release site (release 2026_03_12; build icees_2024-08-20_3ebb9d85_2025sep1_4.3.6; source version 2024-08-20; Biolink 4.3.6; Node Normalizer 2025sep1).
    edge_count: 13972
    format: kgx-jsonl
    id: translator.icees.graph
    latest_version: '2026_03_12'
    license:
      id: https://opensource.org/license/mit/
      label: MIT
    name: Translator ICEES KGX Graph
    node_count: 224
    original_source:
      - source: icees-kg
        relation_type: prov:hadPrimarySource
    product_url: https://kgx-storage.rtx.ai/releases/icees/latest/
    secondary_source:
      - source: translator
        relation_type: prov:wasInfluencedBy
    versions:
      - '2026_03_12'
      - icees_2024-08-20_3ebb9d85_2025sep1_4.3.6
  - category: GraphProduct
    compatibility:
      - standard: biolink
        version: 4.3.6
    description: Aggregated KGX JSONL graph package combining 29 Translator release sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer 2025sep1).
    edge_count: 29243943
    format: kgx-jsonl
    id: translator.translator_kg.graph
    latest_version: '2026_03_27'
    license:
      id: https://opensource.org/license/mit/
      label: MIT
    name: Translator Aggregate KGX Graph
    node_count: 1696790
    original_source:
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: cohd
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: ctkp
        relation_type: prov:hadPrimarySource
      - source: drug-approvals-kp
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: drugrephub
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
      - source: gene2phenotype
        relation_type: prov:hadPrimarySource
      - source: geneticskp
        relation_type: prov:hadPrimarySource
      - source: go-cam
        relation_type: prov:hadPrimarySource
      - source: goa
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: icees-kg
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pathbank
        relation_type: prov:hadPrimarySource
      - source: semmeddb
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: text-mining-kp
        relation_type: prov:hadPrimarySource
      - source: ttd
        relation_type: prov:hadPrimarySource
      - source: ubergraph
        relation_type: prov:hadPrimarySource
    product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
    secondary_source:
      - source: translator
        relation_type: prov:wasInfluencedBy
    versions:
      - '2026_03_27'
      - 423af7989cac
publications:
  - id: https://doi.org/10.1093/jamia/ocz042
  - id: https://doi.org/10.2196/17964
repository: https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES
tags:
  - translator
taxon:
  - NCBITaxon:9606
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

## Automated Evaluation

- View the automated evaluation: [icees-kg automated evaluation](icees-kg_eval_automated.html)
