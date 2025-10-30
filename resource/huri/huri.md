---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://ccsb.dana-farber.org/
    label: Center for Cancer Systems Biology
  - category: Individual
    label: Marc Vidal
    orcid: 0000-0002-9500-6065
  - category: Individual
    label: Frederick P. Roth
creation_date: '2025-08-05T00:00:00Z'
description: The Human Reference Interactome (HuRI) is a comprehensive map of binary protein-protein interactions in human cells, generated through systematic high-throughput yeast two-hybrid screening. HuRI provides the largest experimentally verified collection of human protein interactions and serves as a foundational resource for understanding cellular networks and disease mechanisms.
domains:
  - biomedical
  - biological systems
  - proteomics
  - systems biology
homepage_url: http://www.interactome-atlas.org/
id: huri
last_modified_date: '2025-08-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: HuRI
products:
  - category: Product
    description: Human Reference Interactome (HuRI) protein-protein interaction data
    format: tsv
    id: huri.interactions
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC BY 4.0
    name: HuRI Protein-Protein Interactions
    product_url: http://www.interactome-atlas.org/download
  - category: Product
    description: Literature-curated high-quality protein-protein interactions from comparable experimental approaches
    format: tsv
    id: huri.literature_benchmark
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC BY 4.0
    name: HuRI Literature Benchmark
    product_url: http://www.interactome-atlas.org/download
  - category: GraphicalInterface
    description: Web portal for searching and browsing human protein interactions
    id: huri.portal
    name: HuRI Web Portal
    product_url: http://www.interactome-atlas.org/
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - chebi
      - cosmic
      - achilles
      - depmap
      - ccle
      - gdsc
      - cellosaurus
      - clue
      - ctd
      - pharmacodb
      - prism
      - drugbank
      - lincs
      - compartments
      - offsides
      - sider
      - drugcentral
      - repohub
      - chemicalchecker
      - repodb
      - disgenet
      - opentargets
      - creeds
      - interpro
      - reactome
      - tissues
      - dorothea
      - progeny
      - gtex
      - hpa
      - go
      - corum
      - huri
      - intact
      - omnipath
      - string
      - bto
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - bioteque
publications:
  - authors:
      - Katja Luck
      - Dae-Kyum Kim
      - Luke Lambourne
      - Kerstin Spirohn
      - et al.
    doi: 10.1038/s41586-020-2188-x
    id: doi:10.1038/s41586-020-2188-x
    journal: Nature
    preferred: true
    title: A reference map of the human binary protein interactome
    year: '2020'
repository: https://github.com/VIDallab/huri
infores_id: huri
---

# HuRI - Human Reference Interactome

The Human Reference Interactome (HuRI) represents the largest systematically generated map of binary protein-protein interactions in human cells. Developed at the Center for Cancer Systems Biology (CCSB) at Dana-Farber Cancer Institute, HuRI provides a foundational reference for understanding cellular networks, disease mechanisms, and biological processes.

## Overview

HuRI was created through systematic high-throughput yeast two-hybrid (Y2H) screening, testing pairwise combinations of human protein-coding genes to identify direct physical interactions. The project represents a landmark achievement in systems biology, providing unprecedented insight into the human protein interaction landscape.

### Current Statistics

**HuRI Database:**
- **9,094 proteins** with experimentally validated interactions
- **64,006 protein-protein interactions** identified through systematic screening
- **17,500 proteins** tested in the most recent comprehensive effort

**Literature Benchmark:**
- **6,047 proteins** with high-quality interactions from literature
- **13,441 protein-protein interactions** curated from comparable experimental approaches

## Methodology and Quality Control

### Experimental Approach
HuRI interactions are identified using high-throughput yeast two-hybrid screens with rigorous quality control:

1. **Systematic Screening**: Pairwise testing of human protein-coding genes using standardized protocols
2. **Orthogonal Validation**: Multiple independent assay systems to confirm interactions
3. **Quality Assessment**: Systematic comparison with literature-curated interactions
4. **Reproducibility Testing**: Multiple replicates and independent validations

### Data Integration
The HuRI project integrates:
- Experimentally determined interactions from systematic screens
- Literature-curated interactions from comparable high-quality experiments
- Cross-references to major biological databases
- GENCODE gene, transcript, and protein annotations

## Research Impact and Applications

### Disease Research
HuRI has enabled groundbreaking research in:
- **Cancer Biology**: Understanding protein networks disrupted in cancer
- **Infectious Diseases**: Mapping host-pathogen interactions, including COVID-19 research
- **Genetic Disorders**: Identifying disease mechanisms through network analysis
- **Drug Discovery**: Finding new therapeutic targets and understanding drug mechanisms

### Network Biology
Key applications include:
- **Systems-level analysis** of cellular processes
- **Pathway reconstruction** and functional annotation
- **Evolutionary studies** of protein interaction networks
- **Prediction algorithms** for novel protein interactions

### Precision Medicine
HuRI contributes to:
- **Biomarker discovery** through network analysis
- **Patient stratification** based on network disruptions
- **Therapeutic targeting** of network components
- **Understanding drug resistance** mechanisms

## Collaborative Framework

HuRI is developed through collaboration between multiple research groups:

- **Vidal Lab** (Dana-Farber Cancer Institute) - Project leadership and Y2H screening
- **Roth Lab** (University of Toronto) - Computational analysis and validation
- **Tavernier Lab** (Ghent University) - Alternative interaction detection methods
- **Bader Lab** (University of Toronto) - Network analysis and bioinformatics

## Data Standards and Quality

### Experimental Standards
- Standardized Y2H protocols across all participating laboratories
- Systematic quality control measures
- Independent validation using orthogonal assays
- Comprehensive documentation of experimental conditions

### Data Annotation
- GENCODE-based gene and protein identifiers
- UniProt cross-references
- GO functional annotations
- Disease associations and pathway mappings

### Accessibility
- Open access under Creative Commons licensing
- Multiple download formats available
- Web-based search and visualization tools
- API access for programmatic queries

## Technical Infrastructure

### Data Processing
- Automated quality control pipelines
- Standardized data formats
- Version control and data provenance tracking
- Integration with major biological databases

### Web Portal Features
- Interactive search interface
- Network visualization tools
- Bulk data download capabilities
- Cross-references to external resources

## Future Directions

Ongoing developments include:
- **Expansion of screening coverage** to achieve comprehensive proteome coverage
- **Integration with structural data** for mechanistic insights
- **Temporal and conditional interactions** under different cellular states
- **Cross-species comparative analysis** for evolutionary insights
- **Machine learning applications** for interaction prediction and validation

## Significance

HuRI represents a paradigm shift in understanding human cellular networks, providing:
- The most comprehensive experimentally validated human interactome
- A reference standard for computational prediction methods
- A foundation for systems-level understanding of human biology
- Critical insights into disease mechanisms and therapeutic opportunities

The resource continues to drive discoveries across multiple biological disciplines and serves as an essential tool for the global research community working to understand human health and disease.

---
