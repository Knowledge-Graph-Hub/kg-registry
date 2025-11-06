---
layout: resource_detail
activity_status: active
category: DataSource
contacts:
- category: Individual
  label: Edward Catoiu
  contact_details:
  - contact_type: email
    value: ecatoiu@ucsd.edu
- category: Organization
  label: Systems Biology Research Group at University of California San Diego
  contact_details:
  - contact_type: url
    value: http://systemsbiology.ucsd.edu/
creation_date: '2025-11-06T00:00:00Z'
description: 'iModulonDB is a knowledgebase of microbial transcriptional regulation derived from machine learning. It provides curated sets of iModulons - independently modulated groups of co-expressed genes identified through independent component analysis (ICA) of high-quality transcriptomic datasets - for prokaryotic organisms. The database offers interactive dashboards and analysis tools to explore transcriptional regulatory networks across multiple bacterial species, enabling researchers to understand gene regulation, discover new regulators, and analyze condition-specific cellular responses.'
domains:
  - systems biology
  - microbiology
homepage_url: https://imodulondb.org/
id: "imodulondb"
last_modified_date: '2025-11-06T00:00:00Z'
name: iModulonDB
products:
  - category: GraphicalInterface
    description: Interactive web interface for browsing and analyzing iModulons across 15 prokaryotic organisms with 22 datasets, 1924 curated iModulons, and 9576 expression profiles. Includes organism-specific dataset pages, iModulon dashboards, gene search functionality, and project information pages displaying experimental conditions and publication abstracts.
    format: http
    id: "imodulondb.browser"
    name: iModulonDB Web Interface
    original_source:
      - imodulondb
    product_url: https://imodulondb.org/
  - category: ProgrammingInterface
    description: Python package for characterization, plotting, and analysis of iModulons. Provides functions for threshold determination, transcriptional regulatory network (TRN) enrichment analysis, explained variance calculation, and generation of dashboard files for iModulonDB.
    format: http
    id: "imodulondb.pymodulon"
    name: PyModulon Python Package
    original_source:
      - imodulondb
    product_url: https://github.com/SBRG/pymodulon
  - category: Product
    description: Computational pipeline for gathering publicly available RNA-seq data, aligning reads, performing quality control, computing iModulons using independent component analysis, and formatting dashboard files. Enables users to generate their own iModulon decompositions from transcriptomic datasets.
    format: http
    id: "imodulondb.imodulonminer"
    name: iModulonMiner Pipeline
    original_source:
      - imodulondb
    product_url: https://github.com/SBRG/iModulonMiner
  - category: Product
    description: Modulome workflow for scraping publicly available data for an organism, aligning reads, quality control, and computing iModulons. Used to expand iModulonDB across the prokaryotic evolutionary tree by processing data from the Sequence Read Archive.
    format: http
    id: "imodulondb.modulome_workflow"
    name: Modulome Workflow
    original_source:
      - imodulondb
    product_url: https://github.com/avsastry/modulome-workflow
  - category: Product
    description: Downloadable transcriptomic datasets and iModulon decompositions for 15 organisms including E. coli, B. subtilis, S. aureus, M. tuberculosis, P. aeruginosa, P. putida, and others. Includes gene expression matrices, iModulon activity matrices, gene weights, and metadata for over 9500 expression profiles from 525 studies.
    format: mixed
    id: "imodulondb.datasets"
    name: iModulonDB Datasets
    original_source:
      - imodulondb
    product_url: https://imodulondb.org/
publications:
- authors:
  - Catoiu EA
  - Krishnan J
  - Li G
  - Lou XA
  - Rychel K
  - Yuan Y
  - Bajpe H
  - Patel A
  - Choe D
  - Shin J
  - Decker KT
  - Chauhan SM
  - Phaneuf PV
  - Palsson BO
  doi: doi:10.1093/nar/gkae1009
  id: https://doi.org/10.1093/nar/gkae1009
  journal: Nucleic Acids Research
  preferred: true
  title: 'iModulonDB 2.0: dynamic tools to facilitate knowledge-mining and user-enabled analyses of curated transcriptomic datasets'
  year: '2025'
- authors:
  - Rychel K
  - Decker K
  - Sastry AV
  - Phaneuf PV
  - Poudel S
  - Palsson BO
  doi: doi:10.1093/nar/gkaa810
  id: https://doi.org/10.1093/nar/gkaa810
  journal: Nucleic Acids Research
  preferred: false
  title: 'iModulonDB: a knowledgebase of microbial transcriptional regulation derived from machine learning'
  year: '2021'
repository: https://github.com/SBRG/iModulonMiner
taxon:
  - NCBITaxon:2
---

## Overview

iModulonDB is a comprehensive knowledgebase that applies machine learning to bacterial transcriptomes to reveal independently modulated gene sets and transcriptional regulatory networks. First released in 2020 and significantly expanded in 2024, the database uses Independent Component Analysis (ICA) to decompose high-quality transcriptomic datasets into iModulons - sets of co-expressed genes that represent independently modulated regulatory signals.

## Key Features

- **Extensive Coverage**: Contains 22 ICA decompositions spanning 15 prokaryotic organisms, with 1924 curated iModulons derived from 9576 expression profiles across 525 studies
- **Supported Organisms**: E. coli, B. subtilis, S. aureus, M. tuberculosis, P. aeruginosa, P. putida, P. syringae, S. enterica, A. baumannii, L. reuteri, S. acidocaldarius, S. pyogenes, S. albidoflavus, S. elongatus, V. natriegens, S. pneumoniae
- **Interactive Dashboards**: Organism-specific pages with iModulon browsers, gene search functionality, and detailed visualizations of gene weights, iModulon activities, and regulatory relationships
- **Data Curation**: Comprehensive metadata including study abstracts, experimental conditions, control/experimental variables, and genetic perturbations
- **Analysis Tools**: Search-driven pairwise analysis of iModulon-iModulon, iModulon-gene, and gene-gene relationships; dataset-wide correlation analyses; phase-plane plots showing iModulon activity relationships
- **External Integration**: Direct links to BioCyc operon diagrams and STRING protein-protein interaction networks for biological context

## Understanding iModulons

### What are iModulons?

iModulons are independently modulated groups of genes identified through Independent Component Analysis (ICA) of transcriptomic datasets. Each iModulon consists of:

- **Gene Weights**: Indicating how strongly each gene belongs to the iModulon
- **Activity Profiles**: Showing how active the iModulon is under different experimental conditions
- **Regulatory Associations**: Links to known transcription factors and regulons when characterized

### iModulons vs Regulons

While regulons are defined by experimentally validated transcription factor binding sites, iModulons are data-driven:
- **Regulons**: Bottom-up approach based on binding site identification
- **iModulons**: Top-down approach based on co-expression patterns
- Often highly overlapping but iModulons can reveal:
  - Novel genes regulated by known transcription factors
  - Subsets of regulons responding to specific conditions
  - Uncharacterized regulatory modules
  - Cross-regulation between regulatory systems

## Applications and Use Cases

### Gene Function Prediction
- Assign putative functions to uncharacterized genes based on their iModulon membership
- 224 genes in E. coli have been characterized through iModulon analysis

### Regulatory Network Discovery
- Identify new transcriptional regulators and their target genes
- Reveal condition-specific activation patterns
- Understand systems-level organization of transcriptional regulation

### Experimental Validation
- MetJ and CysB regulons in E. coli were expanded through ChIP-exo validation of iModulon predictions
- BrlR-mediated regulation of mexPQ-ompE efflux system discovered in P. aeruginosa

### Comparative Analysis
- Pan-genomic analysis across strains (e.g., Salmonella Typhimurium)
- Evolutionary insights from iModulon conservation
- Understanding adaptation to environmental conditions

### Data Projection
- Project new datasets onto existing iModulon structures
- Perform differential iModulon activity analysis between conditions
- Simplify analysis from hundreds of genes to handful of iModulons

## Technical Details

### ICA Methodology

Independent Component Analysis decomposes a transcriptomic matrix (X) into:
- **M matrix**: Links genes to iModulons (gene weights)
- **A matrix**: Links iModulons to conditions (activity levels)
- Assumes independent, linearly additive effects of transcriptional regulators

### Quality Control

Datasets must meet criteria for high-quality iModulon computation:
- High-quality RNA-seq with rigorous QC (alignment, contamination checks)
- Consistent underlying transcriptional regulatory network (typically strain-specific)
- Large number of unique conditions (minimum ~100 samples recommended)
- Minimal batch effects through careful normalization

### Data Processing Pipeline

1. Download RNA-seq data from public repositories (Sequence Read Archive)
2. Align reads to reference genome
3. Quality control and filtering
4. Normalize expression data to reference conditions
5. Run ICA to compute iModulons
6. Characterize iModulons through regulon enrichment
7. Generate interactive dashboard files

## Access and Usage

### Web Interface

The main website (iModulonDB.org) provides:
- Organism selection page listing all available datasets
- Dataset pages with iModulon tables and dataset-wide analyses
- Individual iModulon dashboards with detailed visualizations
- Gene search functionality across organisms
- Project pages showing experimental metadata and publication information
- Analysis pages for conducting user-specified comparisons

### Programmatic Access

**PyModulon Package**: Available on GitHub and via pip installation, provides Python API for:
- Loading and manipulating iModulon data
- Computing differential iModulon activity
- Generating custom plots and analyses
- Projecting new data onto existing iModulon structures

**Pipeline Tools**: iModulonMiner and Modulome Workflow available for generating custom iModulon decompositions

### Data Downloads

All transcriptomic datasets and iModulon structures are downloadable directly from the website or through associated publications.

## Recent Updates (Version 2.0)

The 2024 update represents a 1370% growth in expression profiles and includes:

- **Expanded Content**: 19 new datasets, 12 additional organisms, 8925 new samples
- **Enhanced Visualization**: Condition-specific coloring, genetic perturbation highlighting, improved correlation plots
- **New Analysis Tools**: Search-driven pairwise analyses, phase-plane plots, dataset-wide correlation searches
- **Improved Curation**: Study abstracts, experimental variables, reference conditions displayed for all projects
- **External Resources**: Direct links to BioCyc operons and STRING interaction networks
- **Interactive Features**: TreeMaps for explained variance, Recall Plots for regulon overlap, correlation heatmaps

## Database Statistics

- **Datasets**: 22 ICA decompositions across 15 organisms
- **iModulons**: 1924 curated sets with characterized functions and regulators
- **Expression Profiles**: 9576 samples from diverse experimental conditions
- **Studies**: 525 unique experiments with 247 accompanying publications
- **Monthly Active Users**: ~500 researchers worldwide
- **Citations**: Over 300 citations of iModulonDB-related publications

## Community and Support

### Contributing

Researchers can submit their own ICA decompositions and transcriptomic datasets through the contact form on the website.

### Contact

For questions, comments, feedback, or collaboration inquiries:
- Email: ecatoiu@ucsd.edu
- Organization: Systems Biology Research Group (SBRG) at UC San Diego
- Website: http://systemsbiology.ucsd.edu/

## Related Resources

- **RegulonDB**: Experimentally validated regulons for E. coli
- **BioCyc**: Metabolic pathways and operon structures
- **STRING**: Protein-protein interaction networks
- **Sequence Read Archive**: Source of public RNA-seq data
