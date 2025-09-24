---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: "omnipathdb@gmail.com"
      - contact_type: url
        value: "https://omnipathdb.org/"
    label: OmniPath Development Team
description: OmniPath is a comprehensive prior knowledge resource that integrates molecular interactions and biological pathway information from over 100 original databases and resources. It provides unified access to protein-protein interactions, gene regulatory interactions, enzyme-PTM relationships, protein complexes, protein annotations, and intercellular communication data through multiple interfaces including web services, R/Bioconductor packages, Python clients, and Cytoscape plugins.
domains:
  - systems biology
  - biological systems
  - proteomics
  - pathways
homepage_url: https://omnipathdb.org/
id: omnipath
layout: resource_detail
name: OmniPath
products:
  - category: ProgrammingInterface
    description: Web service API providing programmatic access to OmniPath molecular interaction networks, annotations, and intercellular communication data
    format: json
    id: omnipath.webservice
    name: OmniPath Web Service
    original_source:
      - omnipath
    product_url: https://omnipathdb.org/queries
  - category: ProgrammingInterface
    description: R/Bioconductor package (OmnipathR) for accessing and analyzing OmniPath data within the R statistical computing environment
    format: mixed
    id: omnipath.r_package
    name: OmnipathR Package
    original_source:
      - omnipath
    product_url: https://bioconductor.org/packages/release/bioc/html/OmnipathR.html
  - category: ProgrammingInterface
    description: Python client library providing programmatic access to OmniPath databases for Python-based analysis workflows
    format: python
    id: omnipath.python_client
    name: OmniPath Python Client
    original_source:
      - omnipath
    product_url: https://pypi.org/project/omnipath/
  - category: ProcessProduct
    description: Cytoscape plugin for importing and visualizing OmniPath network data within the Cytoscape network analysis platform
    format: java
    id: omnipath.cytoscape_plugin
    name: OmniPath Cytoscape Plugin
    original_source:
      - omnipath
    product_url: https://apps.cytoscape.org/apps/omnipath
  - category: GraphicalInterface
    description: Interactive database explorer for browsing OmniPath data integrated from 160+ resources
    format: http
    id: omnipath.explorer
    name: OmniPath Explorer
    original_source:
      - omnipath
    product_url: https://explore.omnipathdb.org/
  - category: ProcessProduct
    description: Python package (pypath) for building custom OmniPath databases and accessing the OmniPath infrastructure
    format: python
    id: omnipath.pypath
    name: PyPath Database Builder
    original_source:
      - omnipath
    product_url: https://pypi.org/project/pypath-omnipath/
publications:
  - authors:
      - Dénes Türei
      - Tamás Korcsmáros
      - Julio Saez-Rodriguez
    doi: "10.1038/nmeth.4077"
    id: "doi:10.1038/nmeth.4077"
    title: 'OmniPath: guidelines and gateway for literature-curated signaling pathway resources'
    year: "2016"
  - authors:
      - Dénes Türei
      - Alberto Valdeolivas
      - Lejla Gul
      - Nicolàs Palacio-Escat
      - Michal Klein
      - Olga Ivanova
      - Márton Ölbei
      - Attila Gábor
      - Fabian Theis
      - Dezső Módos
      - Tamás Korcsmáros
      - Julio Saez-Rodriguez
    doi: "10.15252/msb.20209923"
    id: "doi:10.15252/msb.20209923"
    title: Integrated intra- and intercellular signaling knowledge for multicellular omics analysis
    year: "2021"
repository: https://github.com/saezlab/pypath
---

# OmniPath

OmniPath is a comprehensive molecular biology prior knowledge database that integrates and harmonizes data from over 100 original resources to provide unified access to diverse types of molecular interactions and biological pathway information. Developed through collaboration between the Saez Lab at Universitat Pompeu Fabra and the Korcsmaros Lab at Earlham Institute, OmniPath serves as a central hub for accessing curated biological knowledge essential for systems biology and network medicine research.

## Overview

The OmniPath database encompasses five major integrated databases that together provide a comprehensive view of molecular interactions within and between cells:

1. **Signaling Networks**: Protein-protein interactions with directional information and effect signs, focusing on literature-curated signaling pathways
2. **Enzyme-PTM Relationships**: Post-translational modification interactions between enzymes and their substrates
3. **Protein Complexes**: Experimentally verified and computationally predicted protein complex compositions
4. **Molecular Annotations**: Functional, structural, and localization annotations for proteins including Gene Ontology terms, pathway memberships, and tissue expression data
5. **Intercellular Communication**: Ligand-receptor interactions and communication pathways between different cell types

## Key Features

### Comprehensive Integration
OmniPath aggregates data from over 100 original databases and resources, including major interaction databases (BioGRID, IntAct, MINT, STRING), pathway databases (Reactome, KEGG, SIGNOR, NetPath), and specialized resources for protein complexes (CORUM, ComplexPortal), post-translational modifications (PhosphoSitePlus, ELM), and intercellular communication (CellTalkDB, CellPhoneDB, ICELLNET).

### Quality Control and Curation
The database emphasizes high-quality, literature-curated interactions over high-throughput experimental data. Each interaction is associated with literature references and experimental evidence, ensuring reliability for downstream analysis and modeling applications.

### Multiple Access Methods
OmniPath provides flexible access through multiple interfaces designed for different user communities:
- **Web Service API** for programmatic access and integration into computational workflows
- **R/Bioconductor Package** (OmnipathR) for statistical analysis and visualization in R
- **Python Client** for integration with Python-based data science pipelines
- **Cytoscape Plugin** for network visualization and analysis
- **Interactive Web Interface** for exploratory data access and querying

### Network Medicine Applications
The integrated nature of OmniPath makes it particularly valuable for network medicine applications, enabling researchers to:
- Construct comprehensive molecular interaction networks
- Perform pathway enrichment analysis
- Model intercellular communication networks
- Integrate multi-omics data in the context of prior knowledge
- Develop mechanistic models of disease processes

## Applications and Use Cases

OmniPath supports a wide range of applications in systems biology and network medicine:

- **Pathway Analysis**: Enrichment analysis and pathway reconstruction using comprehensive interaction networks
- **Network Modeling**: Construction of mechanistic models incorporating protein-protein interactions, regulatory relationships, and intercellular communication
- **Multi-Omics Integration**: Contextualization of genomics, transcriptomics, and proteomics data within comprehensive interaction networks
- **Drug Discovery**: Target identification and mechanism of action studies using integrated molecular interaction data
- **Disease Research**: Investigation of disease mechanisms through network-based approaches and intercellular communication analysis

## Data Sources and Coverage

The database integrates data from diverse categories of resources:
- **Interaction Databases**: BioGRID, IntAct, MINT, STRING, HPRD, InnateDB
- **Pathway Databases**: Reactome, KEGG, SIGNOR, NetPath, WikiPathways
- **Regulatory Networks**: DoRothEA, RegNetwork, TRRUST
- **Protein Complexes**: CORUM, ComplexPortal, hu.MAP
- **Post-translational Modifications**: PhosphoSitePlus, ELM, dbPTM
- **Intercellular Communication**: CellTalkDB, CellPhoneDB, ICELLNET, ConnectomeDB
- **Functional Annotations**: Gene Ontology, UniProt, Human Protein Atlas

This comprehensive integration ensures broad coverage of molecular interaction types while maintaining data quality through systematic curation and validation procedures.
