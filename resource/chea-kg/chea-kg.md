---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: "avi.maayan@mssm.edu"
      - contact_type: url
        value: "https://labs.icahn.mssm.edu/maayanlab/"
    label: Ma'ayan Laboratory
creation_date: '2025-09-23T00:00:00Z'
description: ChEA-KG is a knowledge graph built around the ChEA (ChIP Enrichment Analysis) database that integrates chromatin immunoprecipitation sequencing data with transcription factor binding sites, gene regulatory networks, and functional annotations to provide comprehensive insights into transcriptional regulation across cell types and conditions.
domains:
  - biomedical
  - genomics
  - systems biology
homepage_url: https://maayanlab.cloud/chea-kg/
id: "chea-kg"
last_modified_date: '2025-09-23T00:00:00Z'
layout: resource_detail
license:
  id: "https://creativecommons.org/licenses/by/4.0/"
  label: CC BY 4.0
name: ChEA-KG
products:
  - category: GraphicalInterface
    description: Interactive web interface for exploring transcription factor-target gene relationships with regulatory network visualization
    format: http
    id: "chea-kg.portal"
    name: ChEA-KG Explorer
    product_url: https://maayanlab.cloud/chea-kg/
  - category: ProgrammingInterface
    description: RESTful API for programmatic access to ChIP-seq derived transcription factor binding data
    format: http
    id: "chea-kg.api"
    name: ChEA-KG API
    product_url: https://maayanlab.cloud/chea-kg/api/
  - category: GraphProduct
    description: Neo4j database containing transcription factors, target genes, and regulatory relationships from ChIP-seq studies
    dump_format: neo4j
    format: neo4j
    id: "chea-kg.graph"
    name: ChEA-KG Database
  - category: Product
    description: Processed ChIP-seq datasets with transcription factor binding sites and target gene annotations
    id: "chea-kg.chipseq"
    name: ChEA ChIP-seq Data
    product_url: https://maayanlab.cloud/chea3/index.html#content4-13
publications:
  - authors:
      - Keenan AB
      - Torre D
      - Lachmann A
      - Leong AK
      - Wojtkiewicz ML
      - Utti V
      - Jagodnik KM
      - Kropiwnicki E
      - Wang Z
      - Ma'ayan A
    id: doi:10.1093/nar/gkz446
    journal: Nucleic Acids Research
    preferred: true
    title: 'ChEA3: transcription factor enrichment analysis by orthogonal omics integration'
    year: "2019"
repository: https://github.com/MaayanLab/chea-kg
---

# ChEA-KG

ChEA-KG is a comprehensive knowledge graph that integrates chromatin immunoprecipitation sequencing (ChIP-seq) data from the ChEA database with transcription factor binding information, target gene annotations, and regulatory network data to provide detailed insights into transcriptional regulation mechanisms across diverse biological contexts.

## Key Features

### Comprehensive ChIP-seq Integration
- Over 100,000 ChIP-seq experiments from public repositories
- Transcription factor binding sites mapped across the human genome
- Cell type and tissue-specific regulatory landscapes
- Condition-specific transcriptional programs

### Multi-Species Coverage
- Human transcription factor binding data with extensive coverage
- Mouse regulatory networks for comparative analysis
- Cross-species transcription factor ortholog mapping
- Conservation analysis of regulatory relationships

### Regulatory Network Construction
- Direct transcription factor-target gene relationships
- Co-regulatory transcription factor modules
- Hierarchical regulatory cascades and feedback loops
- Tissue-specific regulatory network topologies

## Data Sources

### ChIP-seq Repositories
- ENCODE Project chromatin immunoprecipitation data
- GEO ChIP-seq datasets with standardized processing
- Roadmap Epigenomics Project regulatory landscapes
- CISTROME database curated ChIP-seq experiments

### Transcription Factor Annotations
- UniProt transcription factor functional classifications
- Gene Ontology transcriptional regulation terms
- Transcription factor family classifications (TF-Class)
- DNA binding domain structural information

### Genomic Annotations
- RefSeq gene models and transcript isoforms
- GENCODE comprehensive gene annotations
- Regulatory element annotations from ENCODE
- Chromatin state segmentations across cell types

### Expression Data Integration
- GTEx tissue-specific gene expression profiles
- Single-cell RNA-seq expression atlases
- Perturbation experiments with transcription factor modulation
- Time-course expression studies of regulatory dynamics

## Data Types

### Binding Site Information
- Peak coordinates from ChIP-seq experiments
- Binding strength and confidence scores
- Motif occurrence within binding regions
- Chromatin accessibility at binding sites

### Regulatory Relationships
- Direct transcription factor-target gene pairs
- Binding distance to transcription start sites
- Correlation between binding and target gene expression
- Context-specific regulatory interactions

### Functional Annotations
- Gene Ontology enrichment for target gene sets
- Pathway enrichment analysis for regulatory modules  
- Disease associations of transcription factor networks
- Drug target information for regulatory proteins

### Comparative Data
- Cross-cell type binding conservation
- Species-specific transcription factor binding patterns
- Evolution of regulatory network architectures
- Regulatory divergence between related cell types

## Applications

### Regulatory Network Analysis
- Reconstruction of cell type-specific regulatory networks
- Identification of master transcription factors and regulatory hubs
- Analysis of transcriptional regulatory cascades
- Network-based prediction of gene expression changes

### Functional Genomics
- Transcription factor enrichment analysis for gene lists
- Prediction of upstream regulators from expression signatures
- Integration of ChIP-seq and RNA-seq data for mechanism discovery
- Identification of regulatory biomarkers for disease states

### Drug Discovery
- Target identification through regulatory network analysis
- Mechanism of action prediction for transcriptional modulators
- Drug repurposing based on transcriptional signatures
- Biomarker discovery for drug response prediction

### Systems Biology
- Multi-omics integration incorporating transcriptional regulation
- Modeling of regulatory network dynamics
- Prediction of cellular responses to perturbations
- Understanding of transcriptional control in development and disease

## Technical Implementation
ChEA-KG is implemented as a Neo4j graph database with nodes representing transcription factors, genes, cell types, and experimental conditions. Relationships capture binding events, regulatory interactions, and functional associations with confidence scores based on experimental evidence quality and reproducibility across studies.
