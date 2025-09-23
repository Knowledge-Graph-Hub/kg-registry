---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-09-23T00:00:00Z'
description: Harmonizome-KG is a comprehensive knowledge graph derived from the Harmonizome database, integrating functional genomics data across multiple biological domains to connect genes with their functional annotations, regulatory relationships, protein interactions, and phenotypic associations in a unified graph structure.
domains:
- biomedical
- genomics
- systems biology
- functional genomics
- biological systems
homepage_url: https://maayanlab.cloud/harmonizome-kg/
id: harmonizome-kg
last_modified_date: '2025-09-23T00:00:00Z'
layout: resource_detail
name: Harmonizome-KG
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
products:
- category: GraphicalInterface
  description: Interactive web interface for exploring the Harmonizome knowledge graph with gene-centric network visualization
  format: http
  id: harmonizome-kg.portal
  name: Harmonizome-KG Explorer
  product_url: https://maayanlab.cloud/harmonizome-kg/
- category: ProgrammingInterface
  description: RESTful API for programmatic access to Harmonizome functional genomics knowledge graph
  format: http
  id: harmonizome-kg.api
  name: Harmonizome-KG API
  product_url: https://maayanlab.cloud/harmonizome-kg/api/
- category: GraphProduct
  description: Neo4j database containing integrated functional genomics data with genes, proteins, pathways, diseases, and regulatory relationships
  format: neo4j
  id: harmonizome-kg.graph
  name: Harmonizome-KG Neo4j Database
  dump_format: neo4j
publications:
- id: doi:10.1093/database/baw100
  title: "The harmonizome: a collection of processed datasets gathered to serve and mine knowledge about genes and proteins"
  year: '2016'
  journal: Database
  authors:
  - Rouillard AD
  - Gundersen GW
  - Fernandez NF
  - Wang Z
  - Monteiro CD
  - McDermott MG
  - Ma'ayan A
  preferred: true
repository: https://github.com/MaayanLab/harmonizome-kg
tags:
- translator
---

# Harmonizome-KG

Harmonizome-KG is a comprehensive knowledge graph built from the Harmonizome database, which contains over 100 datasets from 66 online resources that describe functional associations between genes and proteins. The knowledge graph provides a unified view of functional genomics data across multiple biological scales and domains.

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