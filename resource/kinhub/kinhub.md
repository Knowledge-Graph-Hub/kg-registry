---
activity_status: active
category: DataSource
creation_date: '2025-11-05T00:00:00Z'
description: A comprehensive resource for human protein kinases featuring KinMap, an interactive web-based tool for visualizing and annotating the human kinome tree, integrating biochemical, structural, and disease association data with a unified naming scheme
domains:
  - genomics
  - biological systems
homepage_url: http://www.kinhub.org/
id: "kinhub"
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: KinHub
synonyms:
  - Human Kinase Hub
  - Human Protein Kinases Hub
products:
  - id: "kinhub.portal"
    name: KinHub Portal
    category: GraphicalInterface
    format: http
    product_url: http://www.kinhub.org/
    description: Main portal providing resources and tools for human protein kinases
  - id: "kinhub.kinmap"
    name: KinMap
    category: GraphicalInterface
    format: http
    product_url: http://www.kinhub.org/kinmap/index.html
    description: Interactive web-based tool for navigating and annotating the human kinome tree with biochemical, structural, and disease data
  - id: "kinhub.kinases-list"
    name: Human Protein Kinases List
    category: Product
    format: http
    product_url: http://www.kinhub.org/kinases.html
    description: Comprehensive list of human protein kinases with unified naming scheme
  - category: GraphicalInterface
    description: Interactive web interface for exploring and visualizing kinase-substrate interactions
    format: http
    id: "kinace.portal"
    name: KinAce Web Portal
    original_source:
      - phosphositeplus
      - iptmnet
      - uniprot
      - epsd
      - kinhub
      - coralkinome
      - darkkinasekb
      - hgnc
      - kegg
      - interpro
    product_url: https://kinace.kinametrix.com/
    secondary_source:
      - kinace
publications:
  - id: "eid2017kinmap"
    preferred: true
    title: 'KinMap: a web-based tool for interactive navigation through human kinome data'
    doi: "10.1186/s12859-016-1433-7"
    year: "2017"
---

## KinHub

KinHub is a comprehensive web-based resource for human protein kinases, centered around KinMap, an interactive visualization tool for the human kinome tree. The resource integrates data from multiple freely-available sources including ChEMBL, the Protein Data Bank, and the Center for Therapeutic Target Validation platform.

### KinMap: Interactive Kinome Tree Viewer

KinMap facilitates the interactive exploration of the human kinome by linking biochemical, structural, and disease association data to phylogenetic relationships:

- **Compound profiling data integration**: Visualize kinase inhibitor selectivity and binding profiles
- **Structural feature annotation**: Display structural characteristics of kinases mapped onto the kinome tree
- **Disease association mapping**: Connect kinase functions to therapeutic indications
- **Unified naming scheme**: Recognizes alternative kinase names and links them to standardized nomenclature

### Key Features

#### Data Integration
- **ChEMBL**: Bioactivity data for kinase inhibitors
- **Protein Data Bank (PDB)**: Structural information for kinases
- **Center for Therapeutic Target Validation**: Disease association and drug target data
- **Proprietary data support**: Users can complement public data with their own datasets

#### Input/Output Formats
- Multiple input formats supported for kinase lists and activity data
- High-quality annotated image generation of kinome trees
- Data exchange capabilities for scientific communications
- Interactive annotations that can be saved and shared

#### Applications
1. **Drug repurposing**: Uncovering new therapeutic indications for known kinase inhibitors
2. **Drug development prioritization**: Identifying promising kinases for drug development efforts
3. **Kinase selectivity analysis**: Comparing inhibitor profiles across the kinome
4. **Target validation**: Linking kinase functions to disease phenotypes

### Human Protein Kinases Database

KinHub provides a comprehensive list of human protein kinases with:
- Standardized nomenclature based on Manning et al. 2002 classification
- Phylogenetic relationships within kinase families
- Alternative names and synonyms for each kinase
- Cross-references to major protein databases

### Manning Kinome Classification

The human kinome comprises approximately 518 protein kinases classified into major groups:
- **AGC group**: PKA, PKG, PKC families
- **CAMK group**: Calcium/calmodulin-dependent kinases
- **CK1 group**: Casein kinase 1 family
- **CMGC group**: CDK, MAPK, GSK3, CLK families
- **STE group**: Homologs of yeast Sterile kinases
- **TK group**: Tyrosine kinases
- **TKL group**: Tyrosine kinase-like kinases
- **Atypical kinases**: RIO, PIKK families
- **Other**: Unclassified protein kinases

### Visualization Capabilities

KinMap enables users to:
- Generate phylogenetic tree views of the entire human kinome
- Highlight specific kinases or groups based on query criteria
- Color-code kinases by activity, selectivity, or other properties
- Overlay structural information (e.g., presence of crystal structures)
- Display disease associations and clinical relevance
- Export high-resolution images for publications

### Data Sources and Updates

The resource is maintained with preprocessed data from:
- **ChEMBL**: Updated kinase bioactivity database
- **PDB**: Current structural information for kinases
- **CTTV (now Open Targets)**: Disease-target associations
- **UniProt**: Protein sequence and functional annotations
- **Manning kinome tree**: Phylogenetic classification framework
