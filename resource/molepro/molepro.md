---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: translator@broadinstitute.org
  label: Broad Institute Translator Team
creation_date: '2025-10-30T00:00:00Z'
description: The Molecular Data Provider (MolePro) is part of the NCATS Biomedical
  Data Translator project, integrating diverse chemical biology data sources into
  a curated framework for chemical entities and their effects on biological targets.
  MolePro consolidates information from over two dozen public chemical biology datasets,
  portals, and tools, providing comprehensive insights into compounds, protein targets,
  and similarity-based connections through both a custom API and TRAPI interface.
domains:
- drug discovery
- chemistry and biochemistry
- biomedical
- pharmacology
- translational
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Molecular-Data-Provider
id: molepro
infores_id: molepro
last_modified_date: '2025-11-17T00:00:00Z'
layout: resource_detail
name: Molecular Data Provider
products:
- category: ProgrammingInterface
  description: MolePro API providing access to the knowledge graph of chemical entities
    and biological targets
  format: http
  id: molepro.api
  name: MolePro API
  original_source:
  - molepro
  product_url: https://molepro.transltr.io/molecular_data_provider/api
- category: ProgrammingInterface
  description: TRAPI-compliant interface for MolePro knowledge graph following the
    Translator Reasoner API standard
  format: http
  id: molepro.trapi
  name: MolePro TRAPI Interface
  original_source:
  - molepro
  product_url: https://molepro-trapi.transltr.io/molepro/trapi/v1.5/ui/
- category: Product
  description: Catalog of MolePro knowledge sources in JSON format
  format: json
  id: molepro.catalog
  name: MolePro Knowledge Sources Catalog
  original_source:
  - molepro
  product_file_size: 2127887
  product_url: https://translator.broadinstitute.org/molecular_data_provider/transformers
repository: https://github.com/broadinstitute/molecular-data-provider
synonyms:
- MolePro
- Molecular Data Provider
tags:
- translator
---
# Molecular Data Provider

## Overview

The Molecular Data Provider (MolePro) is part of the NCATS Biomedical Data Translator project, serving as a Knowledge Provider that integrates diverse chemical biology data sources into a unified framework. MolePro enhances understanding of chemical entities and their effects on biological targets through comprehensive data integration and curation.

## Key Features

- **Data Integration**: Consolidates information from over two dozen public chemical biology datasets, portals, and tools
- **Unbiased Approach**: Adheres to stringent policies to avoid expert bias, ensuring impartial data scouting and meticulous data provenance
- **Unified Framework**: Provides a cohesive framework for compounds and targets, facilitating "guilt-by-association" inferences
- **Chemical Biology Expertise**: Contributes expertise in drug discovery, probe development, toxicity flagging, and small-molecule mechanism of action elucidation
- **Similarity-Based Connections**: Includes connections based on chemical and biological similarity

## Interfaces

MolePro provides the same molecular data knowledge through two APIs:

### MolePro API
- **NCATS Translator server**: https://molepro.transltr.io/molecular_data_provider/api
- **Broad Institute server**: https://translator.broadinstitute.org/molecular_data_provider/api

### Translator Reasoner API (TRAPI)
MolePro implements the standardized Translator Reasoner API, integrating query graphs, knowledge graphs, and results into a single HTTP message:
- **NCATS Translator server**: https://molepro-trapi.transltr.io/molepro/trapi/v1.5/ui/
- **Broad Institute server**: https://translator.broadinstitute.org/molepro/trapi/v1.5/ui/

## Knowledge Sources

MolePro's knowledge graph integrates information from over two dozen sources, including:

- BiGG Models, BigGIM, BindingDB
- ChEBI, ChemBank, ChEMBL, CMAP
- CTD, CTRP, DepMap
- DGIdb, DrugBank, DrugCentral, Drug Repurposing Hub
- DSSTox, Gelinea, GtoPdb
- HGNC, HMDB, Inxight:Drugs
- Kinomescan, MSigDB, PharmGKB
- Pharos, ProbeMiner, PubChem
- Reactome, RxNorm, SIDER
- STITCH, STRING

For complete details, see the [Catalog of MolePro knowledge sources](https://translator.broadinstitute.org/molecular_data_provider/transformers).

## Source Code

MolePro is open source and available on GitHub: https://github.com/broadinstitute/molecular-data-provider

## Team Contact

- Email: translator@broadinstitute.org
- Team Lead: Vlado Dancik (@vdancik)