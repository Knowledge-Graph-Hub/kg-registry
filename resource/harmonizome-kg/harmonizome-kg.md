---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: avi.maayan@mssm.edu
      - contact_type: url
        value: https://labs.icahn.mssm.edu/maayanlab/
    label: Ma'ayan Laboratory
creation_date: '2025-09-23T00:00:00Z'
description: Harmonizome-KG is a knowledge graph section of Harmonizome 3.0 that serializes Harmonizome's processed gene-attribute datasets into a Neo4j-backed graph interface and API. It supports exploration of genes, biological and biomedical attributes, resources, datasets, and associations derived from Harmonizome's integrated multi-omics knowledge base.
domains:
  - biomedical
  - genomics
  - systems biology
  - biological systems
homepage_url: https://harmonizome-kg.maayanlab.cloud/
id: harmonizome-kg
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Harmonizome-KG
products:
  - category: GraphicalInterface
    description: Interactive web interface for exploring the Harmonizome knowledge graph with gene-centric network visualization
    format: http
    id: harmonizome-kg.portal
    name: Harmonizome-KG Explorer
    product_url: https://harmonizome-kg.maayanlab.cloud/
    original_source:
      - source: harmonizome-kg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: harmonizome
        relation_type: prov:wasDerivedFrom
  - category: ProgrammingInterface
    connection_url: https://harmonizome-kg.maayanlab.cloud/api/knowledge_graph
    description: API endpoint for programmatic access to Harmonizome-KG neighborhoods,
      with filter parameters documented in the Harmonizome knowledge graph API guide
    format: json
    id: harmonizome-kg.api
    name: Harmonizome-KG API
    product_url: https://maayanlab.cloud/Harmonizome/documentation#kg-api
    original_source:
      - source: harmonizome-kg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: harmonizome
        relation_type: prov:wasDerivedFrom
  - category: GraphProduct
    description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
      including genes, attributes, resources, datasets, and gene-attribute associations
    dump_format: neo4j
    format: neo4j
    id: harmonizome-kg.graph
    latest_version: '3.0'
    name: Harmonizome-KG Neo4j Database
    original_source:
      - source: harmonizome-kg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: harmonizome
        relation_type: prov:wasDerivedFrom
    product_url: https://harmonizome-kg.maayanlab.cloud/
publications:
  - authors:
      - Ido Diamant
      - Daniel J B Clarke
      - John Erol Evangelista
      - Nathania Lingam
      - Avi Ma'ayan
    doi: 10.1093/nar/gkae1080
    id: doi:10.1093/nar/gkae1080
    journal: Nucleic Acids Research
    preferred: true
    title: 'Harmonizome 3.0: integrated knowledge about genes and proteins from diverse multi-omics resources'
    year: '2025'
  - authors:
      - Rouillard AD
      - Gundersen GW
      - Fernandez NF
      - Wang Z
      - Monteiro CD
      - McDermott MG
      - Ma'ayan A
    doi: 10.1093/database/baw100
    id: doi:10.1093/database/baw100
    journal: Database
    preferred: false
    title: 'The harmonizome: a collection of processed datasets gathered to serve and mine knowledge about genes and proteins'
    year: '2016'
repository: https://github.com/MaayanLab/Knowledge-Graph-UI
tags:
  - translator
---

# Harmonizome-KG

Harmonizome-KG is the knowledge graph interface for Harmonizome 3.0. It uses the
knowledge graph serializations of processed Harmonizome datasets to support graph
queries and subnetwork visualizations over genes, attributes, datasets, resources,
and associations.

## Key Features

### Comprehensive Data Integration
- Integrates over 100 curated functional genomics datasets
- Spans protein-protein interactions, gene expression, genetic associations, and regulatory relationships
- Contains data from 66 diverse online biological resources
- Covers multiple species with primary focus on human and mouse

### Multi-Scale Biological Networks
- Gene-protein interaction networks from high-throughput screens
- Transcriptional regulatory networks from ChIP-seq and motif analysis
- Metabolic pathway associations from curated databases
- Disease-gene associations from clinical and genetic studies
- Drug-target relationships from pharmacological databases

### Harmonized Data Structure
- Standardized gene and protein identifiers across datasets
- Normalized scoring systems for relationship strengths
- Consistent metadata annotation for all data sources
- Cross-reference mappings between different identifier systems

## Data Categories

### Protein Interactions
- Physical protein-protein interactions from mass spectrometry
- Functional interactions from genetic screens
- Protein complexes from structural and biochemical studies
- Domain-domain interaction predictions

### Gene Expression
- Tissue-specific expression patterns from RNA-seq
- Single-cell expression profiles across cell types
- Condition-specific expression changes
- Developmental stage expression dynamics

### Regulatory Networks
- Transcription factor binding sites from ChIP-seq
- MicroRNA target predictions and validations
- Epigenetic modifications and chromatin states
- Enhancer-promoter interaction maps

### Phenotypic Associations
- Gene-disease associations from clinical studies
- Drug response and pharmacogenomic data
- Model organism phenotype annotations
- Genetic variant effect predictions

## Applications

### Network Medicine
- Disease module identification and characterization
- Drug target prioritization and mechanism analysis
- Biomarker discovery through network propagation
- Pathway-based drug repurposing strategies

### Functional Annotation
- Gene function prediction through network analysis
- Protein complex inference and validation
- Regulatory pathway reconstruction
- Cross-species functional conservation

### Systems Analysis
- Multi-omics data integration and analysis
- Network-based feature selection for machine learning
- Identification of key regulatory hubs and bottlenecks
- Evolutionary analysis of functional networks

## Technical Implementation
The Harmonizome-KG is implemented as a Neo4j graph database with standardized node types for genes, proteins, pathways, diseases, drugs, and other biological entities. Relationships are weighted based on confidence scores derived from experimental evidence and computational predictions.

## Automated Evaluation

- View the automated evaluation: [harmonizome-kg automated evaluation](harmonizome-kg_eval_automated.html)
