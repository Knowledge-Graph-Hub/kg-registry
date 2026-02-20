---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ncats.nih.gov/translator
  label: NCATS Biomedical Data Translator
creation_date: '2025-10-30T00:00:00Z'
description: SuppKG is a knowledge graph that integrates information about dietary
  supplements and their relationships with diseases, genes, proteins, and other biomedical
  entities, developed to support translational research and clinical decision-making.
domains:
- nutrition
- biomedical
- health
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/SuppKG
id: suppkg
infores_id: suppkg
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: SuppKG
publications:
- id: https://doi.org/10.1016/j.jbi.2022.104120
  title: 'SuppKG: A knowledge graph for dietary supplements'
  year: '2022'
products:
- category: DocumentationProduct
  description: Translator wiki page describing SuppKG scope and example supplement-disease relationships.
  format: http
  id: suppkg.docs
  name: SuppKG Documentation
  original_source:
  - suppkg
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/SuppKG
- category: ProcessProduct
  description: Source data directory used for SuppKG in the SemRep_DS repository.
  format: http
  id: suppkg.source-data
  name: SuppKG Source Data Repository
  original_source:
  - suppkg
  product_url: https://github.com/zhang-informatics/SemRep_DS/tree/main/SuppKG
synonyms:
- SuppKG
- Dietary Supplement Knowledge Graph
taxon:
- NCBITaxon:9606
---
# SuppKG

## Overview

SuppKG (Dietary Supplement Knowledge Graph) is a comprehensive knowledge graph that integrates information about dietary supplements and their relationships with diseases, genes, proteins, chemicals, and other biomedical entities. Developed as part of the NCATS Biomedical Data Translator program, SuppKG addresses the critical need for structured, computable knowledge about dietary supplements to support evidence-based clinical decision-making and translational research.

## Key Features

- **Comprehensive Coverage**: Integrates diverse data about dietary supplements including ingredients, biological activities, and health effects
- **Multi-Entity Relationships**: Links supplements to diseases, genes, proteins, pathways, and chemical compounds
- **Evidence-Based**: Relationships supported by literature and clinical evidence
- **Standardized Representation**: Uses Biolink Model for semantic interoperability
- **TRAPI-Compatible**: Accessible through the Translator Reasoner API
- **Integration with Translator**: Part of the NCATS Translator knowledge provider ecosystem

## Data Content

### Entities

- **Dietary Supplements**: Vitamins, minerals, herbs, botanicals, amino acids, and other supplement products
- **Supplement Ingredients**: Active and inactive components
- **Diseases and Conditions**: Health conditions associated with supplement use
- **Genes and Proteins**: Molecular targets and mechanisms of action
- **Chemical Compounds**: Chemical structures and identifiers
- **Biological Pathways**: Mechanistic pathways affected by supplements

### Relationships

- Supplement-disease associations (therapeutic uses, contraindications)
- Supplement-gene interactions
- Supplement-protein interactions
- Supplement-chemical compound relationships
- Ingredient-supplement compositions
- Mechanism of action relationships
- Drug-supplement interactions

## Data Sources

SuppKG integrates information from multiple authoritative sources:
- Scientific literature (PubMed)
- Clinical databases
- Natural product databases
- Chemical databases (ChEBI, PubChem)
- Protein databases (UniProt)
- Pathway databases
- FDA and regulatory information

## Applications

### Clinical Decision Support

- **Patient Safety**: Identifying potential drug-supplement interactions
- **Treatment Planning**: Evidence-based supplement recommendations
- **Contraindication Checking**: Warning about unsafe supplement use in specific conditions
- **Personalized Medicine**: Tailoring supplement recommendations based on patient profiles

### Research and Discovery

- **Hypothesis Generation**: Discovering novel supplement-disease associations
- **Mechanism Exploration**: Understanding biological mechanisms of supplement effects
- **Repurposing Opportunities**: Identifying new therapeutic applications for supplements
- **Literature Mining**: Systematic extraction of supplement knowledge from publications

### Public Health

- **Evidence Synthesis**: Aggregating evidence about supplement efficacy and safety
- **Policy Support**: Informing regulatory decisions about dietary supplements
- **Consumer Education**: Providing accurate, evidence-based information about supplements

## Technical Implementation

### Knowledge Graph Structure

- **Format**: RDF-based knowledge graph
- **Ontologies**: Biolink Model for semantic standardization
- **Identifiers**: Standard biomedical identifiers (e.g., CUI, ChEBI, UniProt)
- **Provenance**: Comprehensive tracking of data sources and evidence

### Access Methods

- **Translator API**: Query via TRAPI (Translator Reasoner API)
- **Knowledge Provider**: Accessible through Translator ARS (Autonomous Relay System)
- **Programmatic Access**: RESTful API endpoints
- **SPARQL**: Semantic queries for advanced users

## Integration with Translator Ecosystem

SuppKG serves as a Knowledge Provider (KP) in the NCATS Translator program:
- Responds to queries about dietary supplements
- Integrates with other Translator KPs and ARAs
- Supports multi-hop reasoning across biomedical domains
- Contributes to comprehensive translational research queries

## Information Resource ID

This resource has the Information Resource identifier: `infores:suppkg`

## Publication

SuppKG is described in:
- **Title**: "SuppKG: A knowledge graph for dietary supplements"
- **DOI**: https://doi.org/10.1016/j.jbi.2022.104120
- **Year**: 2022

For more information, visit the [SuppKG wiki](https://github.com/NCATSTranslator/Translator-All/wiki/SuppKG) or the [NCATS Translator website](https://ncats.nih.gov/translator).

## Automated Evaluation

- View the automated evaluation: [suppkg automated evaluation](suppkg_eval_automated.html)
