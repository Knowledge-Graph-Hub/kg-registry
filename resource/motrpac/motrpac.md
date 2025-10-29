---
activity_status: active
category: DataSource
creation_date: '2025-10-29T00:00:00Z'
curators:
  - category: Organization
    label: MoTrPAC BioInformatics Center at Stanford University
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://motrpac-data.org/contact"
    label: MoTrPAC BioInformatics Center
description: The Molecular Transducers of Physical Activity Consortium (MoTrPAC) Data Hub is a national research initiative that generates a comprehensive molecular map of the effects of exercise and physical activity training. The data repository provides multi-omics datasets documenting molecular changes from exercise across multiple tissues, including transcriptomics, proteomics, metabolomics, and epigenomics data. The complete young adult rat endurance training dataset is publicly available, featuring quantitative results and analyses from 20 tissues across 29 assays and 5 time points, studying male and female animals. The data hub provides both browsable study data and pre-bundled datasets organized by tissue type and omics platform, all released under CC BY 4.0 license. The resource includes phenotypic data, sample-level metadata, quality control metrics, and quantitative results to enable comprehensive analysis of the temporal dynamics of multi-omic responses to endurance exercise training.
domains:
  - biological systems
  - health
  - proteomics
  - genomics
  - systems biology
homepage_url: https://motrpac-data.org/
id: motrpac
last_modified_date: '2025-10-29T00:00:00Z'
layout: resource_detail
license:
  id: "https://creativecommons.org/licenses/by/4.0/"
  label: CC BY 4.0
name: Molecular Transducers of Physical Activity Consortium (MoTrPAC) Data Hub
publications:
  - authors:
      - MoTrPAC Study Group
    category: Publication
    id: "https://doi.org/10.1016/j.cell.2020.06.004"
    journal: Cell
    preferred: true
    title: 'Molecular Transducers of Physical Activity Consortium (MoTrPAC): Mapping the Dynamic Responses to Exercise'
    year: "2020"
  - authors:
      - MoTrPAC Study Group
    category: Publication
    id: "https://doi.org/10.1038/s41586-023-06877-w"
    journal: Nature
    preferred: false
    title: Temporal dynamics of the multi-omic response to endurance exercise training
    year: "2024"
products:
  - category: GraphicalInterface
    description: Interactive data browser for exploring and downloading MoTrPAC multi-omics datasets by tissue, ome, or assay type
    format: http
    id: "motrpac.data-browser"
    name: MoTrPAC Data Browser
    product_url: https://motrpac-data.org/data-download
  - category: Product
    description: Phenotypic data from young adult rats (6-month old) that performed endurance exercise training
    format: csv
    id: "motrpac.phenotype"
    name: Rat Young Adult Endurance Training - Phenotype Data
    product_url: https://motrpac-data.org/data-download
  - category: Product
    description: Epigenomics data including ATAC-seq and RRBS analyses, sample-level metadata, QC, and quantitative results across tissues
    format: csv
    id: "motrpac.epigenomics"
    name: Rat Young Adult Endurance Training - Epigenomics Data
    product_url: https://motrpac-data.org/data-download
  - category: Product
    description: RNA-seq analyses, sample-level metadata, QC, and quantitative results across tissues
    format: csv
    id: "motrpac.transcriptomics"
    name: Rat Young Adult Endurance Training - Transcriptomics Data
    product_url: https://motrpac-data.org/data-download
  - category: Product
    description: Untargeted proteomics data including Acetyl Proteomics, Global Proteomics, Phosphoproteomics, and Protein Ubiquitination analyses across tissues
    format: csv
    id: "motrpac.proteomics-untargeted"
    name: Rat Young Adult Endurance Training - Proteomics (Untargeted)
    product_url: https://motrpac-data.org/data-download
  - category: Product
    description: Untargeted metabolomics analyses, sample-level metadata, QC, and quantitative results across tissues
    format: csv
    id: "motrpac.metabolomics-untargeted"
    name: Rat Young Adult Endurance Training - Metabolomics (Untargeted)
    product_url: https://motrpac-data.org/data-download
  - category: Product
    description: Targeted metabolomics analyses, sample-level metadata, QC, and quantitative results across tissues
    format: csv
    id: "motrpac.metabolomics-targeted"
    name: Rat Young Adult Endurance Training - Metabolomics (Targeted)
    product_url: https://motrpac-data.org/data-download
  - category: Product
    description: Targeted proteomics immunoassay data with analyses, sample-level metadata, QC, and quantitative results across tissues
    format: csv
    id: "motrpac.proteomics-targeted"
    name: Rat Young Adult Endurance Training - Proteomics (Targeted/Immunoassay)
    product_url: https://motrpac-data.org/data-download
  - category: DocumentationProduct
    description: Video tutorials demonstrating how to use the MoTrPAC Data Hub and access datasets
    format: http
    id: "motrpac.video-tutorials"
    name: MoTrPAC Data Hub Video Tutorials
    product_url: https://motrpac-data.org/
  - category: GraphicalInterface
    description: Main portal for the MoTrPAC Data Hub providing access to data downloads, documentation, and visualization tools
    format: http
    id: "motrpac.data-hub"
    name: MoTrPAC Data Hub Portal
    product_url: https://motrpac-data.org/
---

# Molecular Transducers of Physical Activity Consortium (MoTrPAC) Data Hub

## Overview

The Molecular Transducers of Physical Activity Consortium (MoTrPAC) Data Hub is a comprehensive data repository and resource center for a national research initiative aimed at generating a molecular map of the effects of exercise and physical activity training. The consortium brings together researchers to study how physical activity influences molecular changes across multiple tissues and biological systems.

## Mission and Goals

MoTrPAC's primary objective is to map the dynamic responses to exercise at the molecular level. The consortium generates multi-omics datasets that document comprehensive molecular changes resulting from exercise training, enabling researchers to understand the mechanisms by which physical activity promotes health and prevents disease.

## Data Resources

### Young Adult Rat Endurance Training Study

The complete young adult rat endurance training dataset is publicly available, representing a landmark study published in Nature (2024). This comprehensive dataset includes:

**Study Design:**
- **Animals**: Male and female young adult rats (6-month old)
- **Tissues**: 20 different tissue types
- **Assays**: 29 assays across multiple omics platforms
- **Time Points**: 5 time points throughout the training period
- **Exercise Modality**: Endurance training protocol

**Available Data Types:**

1. **Phenotypic Data**: Comprehensive phenotypic measurements and metadata from trained animals
2. **Epigenomics**: ATAC-seq and RRBS (Reduced Representation Bisulfite Sequencing) data
3. **Transcriptomics**: RNA-seq data across all tissues
4. **Proteomics (Untargeted)**: 
   - Acetyl Proteomics
   - Global Proteomics
   - Phosphoproteomics
   - Protein Ubiquitination
5. **Metabolomics (Untargeted)**: Comprehensive metabolite profiling
6. **Metabolomics (Targeted)**: Focused metabolite measurements
7. **Proteomics (Targeted)**: Immunoassay-based protein quantification

### Tissue-Specific Datasets

Pre-bundled datasets are available for individual tissues, including:
- Gastrocnemius (skeletal muscle)
- Heart
- Liver
- Lung
- Kidney
- Brown adipose tissue
- White adipose tissue
- Blood RNA
- Plasma

Each tissue-specific dataset includes analyses, sample-level metadata, quality control metrics, and quantitative results across all relevant omics platforms.

## Data Organization and Access

### Data Structure

All datasets include:
- **Quantitative Results**: Processed and normalized molecular measurements
- **Sample-Level Metadata**: Detailed information about each biological sample
- **Quality Control Metrics**: QC assessments for each assay and sample
- **Analysis Results**: Statistical analyses and differential expression/abundance results

### Data Formats

Data are provided in standardized formats:
- CSV files for quantitative data and metadata
- Comprehensive documentation for data interpretation
- R objects for advanced analysis workflows

### Download Options

The MoTrPAC Data Hub offers flexible data access:
1. **Interactive Browser**: Browse and select specific data by tissue, ome, or assay type
2. **Pre-bundled Downloads**: Complete datasets organized by omics type or tissue
3. **Programmatic Access**: R packages for data retrieval and analysis

## Key Findings

The temporal dynamics study revealed:
- A network of genes functionally related to longevity, muscle system processes, and response to mechanical stimulus
- Training-differential features whose abundances significantly changed over the training time course
- Molecular adaptations occurring at different time points during the training period
- Cross-tissue coordination of molecular responses to exercise

## Technical Infrastructure

The MoTrPAC Data Hub is designed and maintained by the MoTrPAC BioInformatics Center at Stanford University. The infrastructure includes:

- **Data Processing Pipeline**: Standardized workflows from data ingestion to quality control, processing, and analysis
- **Visualization Tools**: Interactive tools for exploring molecular changes across tissues and time points
- **Documentation**: Comprehensive technical guides for data interpretation and analysis
- **Source Code Repository**: Open access to analysis code and processing pipelines

## Licensing and Data Sharing

All MoTrPAC data are released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license, promoting open science and data reuse. Users are required to:
- Cite the MoTrPAC Marker Paper (Cell, 2020)
- Cite dataset-specific publications when using particular datasets
- Acknowledge data from motrpac-data.org in resulting publications

## Publications

### Marker Paper
The foundational MoTrPAC publication describing the consortium's goals, structure, and approach:
- MoTrPAC Study Group (2020). "Molecular Transducers of Physical Activity Consortium (MoTrPAC): Mapping the Dynamic Responses to Exercise." *Cell* 181(7):1464-1474. https://doi.org/10.1016/j.cell.2020.06.004

### Major Data Release
The comprehensive analysis of the young adult rat endurance training study:
- MoTrPAC Study Group (2024). "Temporal dynamics of the multi-omic response to endurance exercise training." *Nature* 629:174-183. https://doi.org/10.1038/s41586-023-06877-w

## Community Engagement

MoTrPAC maintains active engagement with the research community through:
- **Monthly Virtual Office Hours**: Regular opportunities to learn about data and ask questions
- **Newsletter**: Updates on new data releases and available resources
- **Tutorial Videos**: Comprehensive guides for using the Data Hub
- **Contact Support**: Direct assistance for data access and interpretation

## Ongoing Studies

While the young adult rat endurance training dataset is currently publicly available, MoTrPAC has additional ongoing studies across:
- Different exercise modalities
- Various animal models and age groups
- Multiple tissue types and molecular platforms

Data from these studies will be released as they become available, expanding the molecular map of exercise responses.

## Funding

MoTrPAC is funded by the **NIH Common Fund**, supporting this large-scale collaborative effort to understand the molecular mechanisms underlying the health benefits of physical activity.
