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
description: SuppKG is a knowledge graph that integrates information about dietary supplements and their relationships with diseases, genes, proteins, and other biomedical entities, developed to support translational research and clinical decision-making.
domains:
  - nutrition
  - biomedical
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/SuppKG
id: suppkg
infores_id: suppkg
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (permissive) among its sources: chebi, uniprot.'
  id: https://creativecommons.org/licenses/by/4.0/
  inferred_from:
  - chebi
  - uniprot
  label: CC BY 4.0
  restrictiveness: permissive
  status: inferred
  unresolved_sources: []
name: SuppKG
publications:
  - id: doi:10.1016/j.jbi.2022.104120
    doi: 10.1016/j.jbi.2022.104120
    title: Discovering novel drug-supplement interactions using SuppKG generated from the biomedical literature
    authors:
      - Dalton Schutte
      - Jake Vasilakes
      - Anu Bompelli
      - Yuqi Zhou
      - Marcelo Fiszman
      - Hua Xu
      - Halil Kilicoglu
      - Jeffrey R. Bishop
      - Terrence Adam
      - Rui Zhang
    journal: Journal of Biomedical Informatics
    year: '2022'
products:
  - category: DocumentationProduct
    description: Translator wiki page describing SuppKG scope and example supplement-disease relationships.
    format: http
    id: suppkg.docs
    name: SuppKG Documentation
    original_source:
      - source: suppkg
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NCATSTranslator/Translator-All/wiki/SuppKG
  - category: ProcessProduct
    description: Source data directory used for SuppKG in the SemRep_DS repository.
    format: http
    id: suppkg.source-data
    name: SuppKG Source Data Repository
    original_source:
      - source: suppkg
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/zhang-informatics/SemRep_DS/tree/main/SuppKG
  - category: ProgrammingInterface
    description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
      querying the BioThings and other APIs registered to the team in SmartAPI.
    format: http
    id: service-kp.trapi
    is_public: true
    name: Service Provider TRAPI
    original_source:
    - relation_type: prov:hadPrimarySource
      source: service-kp
    - relation_type: prov:hadPrimarySource
      source: biothings
    - relation_type: prov:hadPrimarySource
      source: monarchinitiative
    - relation_type: prov:hadPrimarySource
      source: ctd
    - relation_type: prov:hadPrimarySource
      source: complexportal
    - relation_type: prov:hadPrimarySource
      source: uniprot
    - relation_type: prov:hadPrimarySource
      source: litvar
    - relation_type: prov:hadPrimarySource
      source: go
    - relation_type: prov:hadPrimarySource
      source: ols
    - relation_type: prov:hadPrimarySource
      source: alliance
    - relation_type: prov:hadPrimarySource
      source: bindingdb
    - relation_type: prov:hadPrimarySource
      source: bioplanet
    - relation_type: prov:hadPrimarySource
      source: ddinter
    - relation_type: prov:hadPrimarySource
      source: dgidb
    - relation_type: prov:hadPrimarySource
      source: diseases
    - relation_type: prov:hadPrimarySource
      source: gene2phenotype
    - relation_type: prov:hadPrimarySource
      source: foodb
    - relation_type: prov:hadPrimarySource
      source: gtrx
    - relation_type: prov:hadPrimarySource
      source: hp
    - relation_type: prov:hadPrimarySource
      source: idisk
    - relation_type: prov:hadPrimarySource
      source: innatedb
    - relation_type: prov:hadPrimarySource
      source: mgi
    - relation_type: prov:hadPrimarySource
      source: pfocr
    - relation_type: prov:hadPrimarySource
      source: repodb
    - relation_type: prov:hadPrimarySource
      source: rhea
    - relation_type: prov:hadPrimarySource
      source: semmeddb
    - relation_type: prov:hadPrimarySource
      source: suppkg
    - relation_type: prov:hadPrimarySource
      source: ttd
    - relation_type: prov:hadPrimarySource
      source: uberon
    - relation_type: prov:hadPrimarySource
      source: ncbigene
    - relation_type: prov:hadPrimarySource
      source: clingen
    - relation_type: prov:hadPrimarySource
      source: cpdb
    - relation_type: prov:hadPrimarySource
      source: panther
    - relation_type: prov:hadPrimarySource
      source: reactome
    - relation_type: prov:hadPrimarySource
      source: aeolus
    - relation_type: prov:hadPrimarySource
      source: chebi
    - relation_type: prov:hadPrimarySource
      source: chembl
    - relation_type: prov:hadPrimarySource
      source: drugcentral
    - relation_type: prov:hadPrimarySource
      source: disgenet
    - relation_type: prov:hadPrimarySource
      source: mondo
    - relation_type: prov:hadPrimarySource
      source: civic
    - relation_type: prov:hadPrimarySource
      source: clinvar
    - relation_type: prov:hadPrimarySource
      source: dbsnp
    - relation_type: prov:hadPrimarySource
      source: doid
    - relation_type: prov:hadPrimarySource
      source: multiomics-kp
    - relation_type: prov:hadPrimarySource
      source: text-mining-kp
    - relation_type: prov:hadPrimarySource
      source: gdsc
    - relation_type: prov:hadPrimarySource
      source: pubmed
    - relation_type: prov:hadPrimarySource
      source: mygene
    - relation_type: prov:hadPrimarySource
      source: mychem
    product_url: https://bte.transltr.io/v1/team/Service%20Provider
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
