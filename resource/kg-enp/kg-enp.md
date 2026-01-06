---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: oolonek
  label: Pierre-Marie Allard
creation_date: '2026-01-06T00:00:00Z'
description: 'ENP-KG is a specialized knowledge graph for experimental natural products discovery and characterization. It integrates chemical spectroscopy data, natural product structures, and organism information to support drug discovery research and chemical ecology applications. The knowledge graph provides a unified platform for exploring relationships between organisms and their secondary metabolites.'
domains:
- organisms
- chemistry
- drug discovery
homepage_url: https://enpkg.commons-lab.org/
id: kg-enp
last_modified_date: '2026-01-06T00:00:00Z'
layout: resource_detail
name: kg-enp
products:
- category: GraphicalInterface
  description: Web-based interactive portal for exploring experimental natural products,
    chemical structures, and organism relationships with data visualization
  format: http
  id: kg-enp.portal
  name: ENP-KG Portal
  product_url: https://enpkg.commons-lab.org/
repository: https://github.com/enpkg/enpkg_full
---
# ENP-KG: Experimental Natural Products Knowledge Graph

ENP-KG is a specialized knowledge graph dedicated to experimental natural products discovery, characterization, and integration. It serves as a comprehensive resource for researchers in drug discovery, chemical ecology, ethnobotany, and natural products chemistry by providing structured access to chemical structures, spectroscopic data, and organism-metabolite associations.

## Overview

The Experimental Natural Products Knowledge Graph (ENP-KG) is part of the broader ENPKG ecosystem developed by the commons-lab community. It aggregates natural products data from diverse sources including curated chemical databases, literature, and experimental studies. The knowledge graph enables exploration of chemical diversity, organism-based compound discovery, and drug screening applications through both web interfaces and programmatic access.

## Data Integration and Scope

ENP-KG integrates diverse types of natural products information:

### Chemical Structure Data
- Experimental natural product compound structures
- Chemical formula and molecular weight information
- Structural similarity metrics for compound clustering
- Spectroscopic reference data (mass spectrometry, NMR)

### Organism Information
- Taxonomic classifications and relationships
- Organism-metabolite associations
- Species-specific natural product profiles
- Geographic distribution and habitat information

### Experimental Data
- Spectroscopy data including mass spectrometry and NMR
- Bioactivity information for natural products
- Experimental conditions and protocols
- Reference standards and analytical methods

## Applications

### Drug Discovery
- Natural product screening and prioritization
- Structure-activity relationship analysis
- Lead compound identification from natural sources
- Bioactive compound characterization

### Chemical Ecology
- Organism secondary metabolite profiling
- Chemical diversity assessment across taxa
- Plant-insect and plant-pathogen chemistry interactions
- Evolution of chemical defense mechanisms

### Ethnobotany and Traditional Medicine
- Traditional medicinal plant documentation
- Ethnobotanical use patterns and validation
- Integration of indigenous knowledge with modern chemistry
- Pharmacological profiling of traditional remedies

### Systems Biology
- Natural products as perturbation agents
- Metabolic pathway analysis in organisms
- Multi-omics integration with chemistry data
- Pathway-based compound discovery

## Data Organization and Access

The knowledge graph is accessible through:
- **Web Portal**: Interactive interface at enpkg.commons-lab.org for browsing and searching natural products
- **Source Code Repository**: Complete implementation at github.com/enpkg/enpkg_full enabling local deployment and extension
- **Community Development**: Open-source framework supporting contributions from the natural products research community

## Technical Architecture

ENP-KG is built as a modern knowledge graph infrastructure that integrates chemical informatics tools with semantic web technologies. The system processes experimental data through standardized pipelines to ensure data quality and consistency across diverse source types.

## Community and Development

ENP-KG is developed and maintained through the commons-lab community initiative, bringing together chemists, biologists, and informatics researchers. The project emphasizes accessibility, extensibility, and community-driven curation of natural products data.

## Automated Evaluation

- View the automated evaluation: [kg-enp automated evaluation](kg-enp_eval_automated.html)
