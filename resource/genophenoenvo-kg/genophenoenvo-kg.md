---
id: "genophenoenvo-kg"
layout: resource_detail
name: GenoPhenoEnvo Knowledge Graph
description: A knowledge graph integrating plant genomics, phenomics, and environmental data to predict gene expression patterns across multiple species under different environmental conditions, particularly drought stress
category: KnowledgeGraph
activity_status: active
creation_date: '2025-11-22T00:00:00Z'
last_modified_date: '2025-11-22T00:00:00Z'
homepage_url: https://github.com/genophenoenvo/knowledge-graph
publications:
  - id: "PMID:37384147"
    title: Using knowledge graphs to infer gene expression in plants
    authors:
      - Anne E. Thessen
      - Laurel Cooper
      - Tyson L. Swetnam
      - Harshad Hegde
      - Justin Reese
      - Justin Elser
      - Pankaj Jaiswal
    journal: Frontiers in Artificial Intelligence
    year: "2023"
    doi: "10.3389/frai.2023.1201002"
license:
  id: "https://opensource.org/licenses/BSD-3-Clause"
  label: BSD-3-Clause
domains:
  - genomics
  - environment
  - phenotype
  - systems biology
  - biological systems
  - biomedical
products:
  - id: "genophenoenvo-kg.data"
    name: GenoPhenoEnvo KG Data
    description: Merged knowledge graph data files containing over 400,000 nodes and 5,000,000 edges integrating gene expression, molecular interactions, functions, pathways, homology-based annotations, and environmental exposures from Planteome, EMBL-EBI Expression Atlas, and other sources. Available as tab-separated value files in KGX format with nodes and edges following the Biolink model.
    category: GraphProduct
    product_url: https://datacommons.cyverse.org/browse/iplant/home/shared/genophenoenvo
    original_source:
      - genophenoenvo-kg
  - id: "genophenoenvo-kg.neo4j"
    name: GenoPhenoEnvo KG Neo4j Visualization
    description: Interactive graph database visualization and query interface using Neo4j for exploring plant gene expression patterns, homologous genes, and environmental responses across multiple plant species including Arabidopsis thaliana, Populus trichocarpa, Zea mays, Sorghum bicolor, and Oryza sativa.
    category: GraphicalInterface
    product_url: https://github.com/genophenoenvo/knowledge-graph
    original_source:
      - genophenoenvo-kg
  - id: "genophenoenvo-kg.code"
    name: GenoPhenoEnvo KG Construction Pipeline
    description: Python-based pipeline for downloading, transforming, and merging plant genomics and phenomics data into a standardized knowledge graph using KG-Hub tools, custom transformation scripts, and Biolink model annotations. Includes Cypher query utilities for graph exploration.
    category: ProcessProduct
    product_url: https://github.com/genophenoenvo/knowledge-graph
    original_source:
      - genophenoenvo-kg
---

## Overview

The GenoPhenoEnvo Knowledge Graph (genophenoenvo-kg) is an integrative knowledge graph designed to enable in silico experimentation for predicting plant gene expression patterns across multiple species under different environmental conditions. The knowledge graph addresses the critical challenge of scaling up our understanding of genotype-environment-phenotype (G×E×P) dynamics to meet the demands of climate change adaptation in agriculture and ecosystem resilience.

By combining data from Planteome, the EMBL-EBI Expression Atlas, and multiple plant ontologies, genophenoenvo-kg creates a queryable framework that represents qualitative relationships between genes, environments, and phenotypes. The graph enables researchers to leverage knowledge about one species to make predictions about another using ontologically-supported knowledge structures that exploit homologous genes and structures.

## Key Features

- **Multi-Species Integration**: Covers five major plant species including Arabidopsis thaliana, Populus trichocarpa, Zea mays, Sorghum bicolor, and Oryza sativa with comprehensive genomic annotations
- **Environmental Context**: Explicitly models environmental exposures (particularly drought and saline stress) and their effects on gene expression, addressing a critical gap in most plant genomics databases
- **Scale**: Contains over 400,000 nodes and 5,000,000 edges representing genes, phenotypes, environments, ontology terms, and their relationships
- **Standardized Model**: Built using the Biolink model for semantic types and predicates, ensuring interoperability with other biomedical knowledge graphs
- **Expression Data**: Integrates differential gene expression data with statistical significance (p < 0.05) from manually curated experiments
- **Homology-Based Inference**: Enables predictions about gene function and expression across species using orthologous gene relationships
- **Ontology-Driven**: Leverages Plant Ontology (PO), Plant Trait Ontology (TO), Gene Ontology (GO), and Plant Experimental Conditions Ontology (PECO) for standardized annotations

## Data Sources

### Primary Resources

- **Planteome Database**: Version 4.0 (October 2020) with approximately 60,000 ontology terms, 3 million data objects, and 20 million associations covering 125 plant taxa
- **EMBL-EBI Expression Atlas**: Over 900 manually curated plant experiments re-analyzed using standardized workflows and latest reference genome assemblies
- **Gene Ontology (GO)**: GO-Basic annotations for molecular functions, biological processes, and cellular components
- **Plant Ontology (PO)**: Anatomical structures and developmental stages
- **Plant Trait Ontology (TO)**: Plant traits and phenotypes
- **Plant Experimental Conditions Ontology (PECO)**: Experimental conditions and environmental exposures
- **EOLTraitbank**: Additional phenotype data (included in graph but not used in primary analysis)

### Gene Annotation Methods

- **InParanoid**: Predicted gene orthology based on Arabidopsis thaliana associations from TAIR
- **InterProScan**: GO annotations via protein families and domain mappings
- **Species-Specific Mapping Files**: Gene identifier normalization for Zm-B73-REFERENCE-NAM-5.0, Sorghum bicolor v3.1.1, Populus trichocarpa reference genome, and Oryza sativa v7.0

## Technical Implementation

### Graph Construction Pipeline

The knowledge graph is constructed using a multi-stage pipeline leveraging KG-Hub tools:

1. **Download Stage**: Automated retrieval of data files from Planteome servers (GAF format), GXA (CSV format), and OBO Foundry (JSON/OWL format)
2. **Transform Stage**: Custom Python scripts normalize gene identifiers, annotate entities with Biolink semantic types, and describe relationships using Biolink predicates
3. **Merge Stage**: Deduplicated consolidation of transformed TSV files into standardized KGX format with nodes and edges files

### Biolink Model Integration

All entities and relationships are mapped to Biolink model standards:

**Node Types:**
- Genomic entity (genes from all species)
- Anatomical entity (plant parts from PO)
- Life stage (growth stages from PO)
- Phenotypic feature (traits from TO)
- Environmental exposure (conditions from PECO)
- Organism taxon (NCBITaxonomy)
- Organismal entity (cultivars, germplasm)
- Cellular component, Molecular function, Biological process (GO terms)

**Edge Predicates:**
- biolink:in_taxon
- biolink:active_in
- biolink:regulates
- biolink:enables
- biolink:expressed_in
- biolink:has_phenotype
- biolink:orthologous_to
- biolink:increases_expression_of
- biolink:decreases_expression_of

### Storage and Access

- **Data Format**: Tab-separated value (TSV) files in KGX format
- **Repository**: CyVerse DataCommons with WebDav access for remote visualization
- **Visualization**: Neo4j graph database with Cypher query interface
- **Source Code**: Open-source Python pipeline on GitHub

## Applications and Use Cases

### Homology-Based Expression Prediction

The graph was used to identify 16 pairs of homologous genes between Arabidopsis thaliana and Populus trichocarpa with documented differential expression under drought conditions. Analysis revealed:

- **Similar Expression Patterns**: 8 homologous pairs showed coordinated expression changes (all decreased expression)
- **Divergent Expression Patterns**: 8 pairs showed opposite expression changes
- **Regulatory Insights**: Homologs with similar expression had conserved cis-regulatory regions and similar transcription factor-binding sites, while divergent pairs showed distinct promoter region architecture

### Promoter Region Analysis

Integration with transcription factor-binding site predictions revealed:

- 11 transcription factor families (RAV, MIKC, NAM, G2-like, CPP, ARR-B, tify, TALE, NF-YC, ERF, NF-YA) were absent in promoter regions of Populus genes with divergent expression
- These missing transcription factors are involved in plant stress response in Arabidopsis
- Demonstrates that promoter regions can evolve separately from coding regions, affecting expression patterns

### Network Medicine Approach

The graph enables exploration of gene regulatory networks in the context of environmental exposures, supporting:

- Hypothesis generation about gene-environment-phenotype interactions
- Reduction of in vivo experiments through in silico screening
- Identification of gene function in understudied species
- Integration of spatial and temporal dynamics of gene expression

## Example Queries

### Finding Homologous Genes with Differential Expression

```cypher
MATCH (e {id:'PECO:0007404'})-[r]->(g),
      (g)-[q:'biolink:orthologous_to']-(h),
      (e {id:'PECO:0007404'})-[s]->(h)
RETURN *
```

This query identifies homologous gene pairs that both have documented differential expression under drought conditions (PECO:0007404).

### Exploring Phenotype-Specific Expression

```cypher
MATCH (g)-[r:'biolink:has_phenotype']->(p {id:'TO:0000207'}),
      (g)-[q:'in_taxon']->(t {id:'NCBITaxon:4577'})
RETURN *
```

This query finds genes in maize (NCBITaxon:4577) associated with a specific trait.

## Future Directions

1. **Regulatory Element Integration**: Extending the graph model to include transcription factor-binding site annotations and actual TF genes
2. **Co-expression Networks**: Adding gene regulatory network data supported by empirical validation
3. **Complex Exposures**: Developing ontologies and semantic representations for complex environmental conditions beyond single substances
4. **Gene Coordinates**: Including genomic coordinates to support automated promoter region analysis
5. **Intraspecies Variation**: Modeling conservation and non-conservation of cis- and trans-regulatory regions within species
6. **Additional Species**: Expanding coverage to more crop species and wild relatives

## Clinical Validation

The predictive power of the knowledge graph was validated through a drought stress study comparing gene expression in Arabidopsis thaliana and Populus trichocarpa:

- **Accuracy**: Successfully identified gene pairs with both similar and divergent expression patterns
- **Mechanistic Insights**: Explained expression differences through promoter region analysis
- **Biological Relevance**: Confirmed that homology-based predictions require careful consideration of regulatory elements, not just coding sequence conservation

## Citation

Thessen AE, Cooper L, Swetnam TL, Hegde H, Reese J, Elser J, Jaiswal P. Using knowledge graphs to infer gene expression in plants. Front Artif Intell. 2023 Jun 13;6:1201002. doi: 10.3389/frai.2023.1201002. PMID: 37384147; PMCID: PMC10298150.
