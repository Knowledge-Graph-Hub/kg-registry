---
activity_status: active
id: petagraph
name: Petagraph
description: Petagraph is a large-scale biomedical knowledge graph that encompasses over 32 million nodes and 118 million relationships, integrating multi-omics and clinical data. Built on the Unified Biomedical Knowledge Graph (UBKG), Petagraph leverages more than 180 ontologies and standards to embed millions of quantitative genomics data points within a richly connected annotation environment.
domains:
- health
- biomedical
- genomics
- knowledge representation
contacts:
- category: Individual
  label: Deanne M. Taylor
  contact_details:
  - contact_type: github
    value: taylordm
  - contact_type: email
    value: taylordm@chop.edu
- category: Organization
  label: Taylor Research Lab
  contact_details:
  - contact_type: github
    value: TaylorResearchLab
  - contact_type: url
    value: https://taylorlab.chop.edu/
homepage_url: https://github.com/TaylorResearchLab/Petagraph
repository: https://github.com/TaylorResearchLab/Petagraph
products:
- id: petagraph.graph
  name: Petagraph Knowledge Graph (Neo4J)
  description: A comprehensive multi-omics biomedical knowledge graph connecting genomic, transcriptomic, proteomic, and clinical data. Contains over 32 million nodes and 118 million relationships.
  product_url: https://ubkg-downloads.xconsortia.org/
  category: GraphProduct
  dump_format: neo4j
  node_count: 32000000
  edge_count: 118000000
  secondary_source:
  - ubkg
  original_source:
  - petagraph
publications:
- id: https://doi.org/10.1038/s41597-024-04070-w
  preferred: true
  title: "Petagraph: A large-scale unifying knowledge graph framework for integrating biomolecular and biomedical data"
  authors:
  - Benjamin J. Stear
  - Taha Mohseni Ahooyi
  - J. Alan Simmons
  - Charles Kollar
  - Lance Hartman
  - Katherine Beigel
  - Aditya Lahiri
  - Shubha Vasisht
  - Tiffany J. Callahan
  - Christopher M. Nemarich
  - Jonathan C. Silverstein
  - Deanne M. Taylor
  journal: Scientific Data
  year: "2024"
  doi: doi:10.1038/s41597-024-04070-w
license:
  label: UMLS License Agreement
  id: https://www.nlm.nih.gov/databases/umls.html
category: KnowledgeGraph
---

## Petagraph: A Large-Scale Biomedical Knowledge Graph

**Petagraph** is a comprehensive biomedical knowledge graph that encompasses over 32 million nodes and 118 million relationships. It provides a cohesive data environment that enables users to efficiently analyze, annotate, and discern relationships within and across complex multi-omics datasets.

### Overview

Constructed on the foundation of the Unified Biomedical Knowledge Graph (UBKG), Petagraph leverages more than 180 ontologies and standards to support a diversity of genomics data types. The graph significantly extends UBKG by adding over 12 million nodes (an increase of almost 44%) and more than doubling the number of relationships from 52 million to 118 million.

Petagraph was originally developed as a resource for rapid feature selection to identify, annotate, and explore gene candidates for human diseases, but has expanded to serve as a base module for user-customized knowledge graphs supporting various biomedical use cases.

### Architecture and Components

Petagraph has five main data-specific node types:
- **Concept nodes**: The central backbone organizing specific conceptual meanings
- **Code nodes**: Identifiers for references in particular ontologies or standards
- **Term nodes**: Human-readable annotations about linked Code nodes
- **Definition nodes**: Provide definitions for Concept nodes
- **Semantic nodes**: Provide wider semantic type classifications for Concepts

The knowledge graph contains 1,861 distinct edge types, with the majority falling into the category of Concept-to-Concept edges, which are bidirectional and form the primary traversable component of the graph.

### Data Integration

Petagraph integrates 21 sources of supporting omics and annotation data, including:

1. **Genomic Data**:
   - GTEX expression and eQTL data
   - 4D Nucleome program data
   - Single-cell fetal heart data
   - ClinVar genetic variants
   
2. **Mapping Data**:
   - Human-to-mouse ortholog mappings
   - Human gene-to-phenotype mappings
   - Human-to-mouse phenotype mappings
   - Mouse gene-to-phenotype mappings
   - Molecular signatures database

3. **Protein Interaction Data**:
   - STRING (protein-protein interactions)
   - GlyGen (glycosylation information)

4. **Chemical-Gene Interactions**:
   - Connectivity MAP (CMAP)
   - LINCS L1000

### Installation Options

Petagraph can be installed in two ways:

1. **Neo4j dump file (preferred method)**:
   - Requires a UMLS license and API key
   - Uses a pre-built database dump (4.5 GB) that can be installed on local machines with at least 16 GB of memory
   - Simple installation through Neo4j Desktop

2. **Build from source**:
   - Provides more customization options
   - Requires generating UMLS CSVs and UBKG CSVs
   - More time-intensive but allows for custom data integration

### Use Cases

Petagraph supports diverse biomedical research applications, including:

- Identifying genomic features functionally linked to genes or diseases
- Linking across genetics data between human and animal models
- Linking transcriptional perturbations by compound in tissues of interest
- Identifying cell types from single-cell data associated with diseases or genes
- Applying machine learning methods for link prediction and node property prediction
- Supporting integration with Large Language Models (LLMs) to enhance biomedical data analysis

### Access and Requirements

- A UMLS license is required to access and use Petagraph
- The database dump is available at [UBKG Downloads](https://ubkg-downloads.xconsortia.org/)
- Documentation and source code are available on [GitHub](https://github.com/TaylorResearchLab/Petagraph)
- The graph database requires Neo4j (version 5.x recommended)

### Future Development

Ongoing work focuses on:
- Expanding Petagraph's capabilities
- Enhancing automated validation techniques
- Developing standardized benchmarks for knowledge graph comparisons
- Integration with Large Language Models
- Supporting the NIH Common Fund Data Ecosystem Data Distillery Project
