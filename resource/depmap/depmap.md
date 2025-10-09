---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: depmap@broadinstitute.org
      - contact_type: url
        value: https://depmap.org/portal/
    label: DepMap Team, Broad Institute
creation_date: '2025-10-09T00:00:00Z'
description: The Cancer Dependency Map (DepMap) is a genome-wide pooled CRISPR-Cas9 knockout and small molecule screen of cancer cell lines. The goal of DepMap is to systematically identify cancer dependencies and the biomarkers that predict them. DepMap provides open access to key cancer dependencies, analytical tools, and visualization resources for the research community.
domains:
  - biomedical
  - genomics
  - health
  - drug discovery
  - precision medicine
homepage_url: https://depmap.org/portal/
id: depmap
last_modified_date: '2025-10-09T00:00:00Z'
layout: resource_detail
license:
  id: https://depmap.org/portal/terms/
  label: DepMap Terms of Use
name: DepMap
products:
  - category: GraphicalInterface
    description: Web portal for exploring cancer dependencies, cell line data, and biomarkers
    format: http
    id: depmap.portal
    name: DepMap Portal
    product_url: https://depmap.org/portal/
  - category: GraphicalInterface
    description: Interactive tool for exploring relationships across DepMap datasets and cell lines
    format: http
    id: depmap.data_explorer
    name: DepMap Data Explorer
    product_url: https://depmap.org/portal/interactive/
  - category: GraphicalInterface
    description: Tool for exploring and selecting cancer cell lines based on various criteria
    format: http
    id: depmap.cell_line_selector
    name: DepMap Cell Line Selector
    product_url: https://depmap.org/portal/cell_line_selector/
  - category: GraphicalInterface
    description: Context Explorer tool for exploring enriched genetic dependencies and compound sensitivities across lineage and subtype contexts
    format: http
    id: depmap.context_explorer
    name: DepMap Context Explorer
    product_url: https://depmap.org/portal/context/
  - category: GraphicalInterface
    description: Target Discovery App for identifying selective and predictable gene dependencies
    format: http
    id: depmap.target_discovery
    name: DepMap Target Discovery
    product_url: https://depmap.org/portal/tda/
  - category: Product
    description: Complete collection of DepMap datasets available for download including CRISPR screens, drug screens, and omics data
    format: mixed
    id: depmap.downloads
    name: DepMap Data Downloads
    product_url: https://depmap.org/portal/data_page/
  - category: Product
    description: CRISPR-Cas9 knockout screening data processed with Chronos algorithm to identify gene dependencies
    format: csv
    id: depmap.crispr_gene_effects
    name: DepMap CRISPR Gene Effects (Chronos)
    product_url: https://depmap.org/portal/data_page/
  - category: Product
    description: Drug screening data from various platforms including GDSC, PRISM, and CTD2
    format: csv
    id: depmap.drug_sensitivity
    name: DepMap Drug Sensitivity Data
    product_url: https://depmap.org/portal/data_page/
  - category: Product
    description: Gene expression data (RNA-seq) for DepMap cell lines
    format: csv
    id: depmap.expression_data
    name: DepMap Expression Data
    product_url: https://depmap.org/portal/data_page/
  - category: Product
    description: Copy number variation data for DepMap cell lines
    format: csv
    id: depmap.copy_number
    name: DepMap Copy Number Data
    product_url: https://depmap.org/portal/data_page/
  - category: Product
    description: Mutation data for DepMap cell lines
    format: csv
    id: depmap.mutations
    name: DepMap Mutation Data
    product_url: https://depmap.org/portal/data_page/
  - category: Product
    description: Proteomics data for DepMap cell lines
    format: csv
    id: depmap.proteomics
    name: DepMap Proteomics Data
    product_url: https://depmap.org/portal/data_page/
  - category: Product
    description: Metabolomics data for DepMap cell lines
    format: csv
    id: depmap.metabolomics
    name: DepMap Metabolomics Data
    product_url: https://depmap.org/portal/data_page/
  - category: Product
    description: Comprehensive metadata and annotations for all DepMap cell lines
    format: csv
    id: depmap.cell_line_info
    name: DepMap Cell Line Information
    product_url: https://depmap.org/portal/data_page/
publications:
  - authors:
      - Meyers RM
      - Bryan JG
      - McFarland JM
      - Weir BA
      - Sizemore AE
      - Xu H
    doi: 10.1038/ng.3984
    id: doi:10.1038/ng.3984
    journal: Nature Genetics
    title: Computational correction of copy number effect improves specificity of CRISPR-Cas9 essentiality screens in cancer cells
    year: '2017'
  - authors:
      - Tsherniak A
      - Vazquez F
      - Montgomery PG
      - Weir BA
      - Kryukov G
      - Cowley GS
    doi: 10.1016/j.cell.2017.06.010
    id: doi:10.1016/j.cell.2017.06.010
    journal: Cell
    title: Defining a Cancer Dependency Map
    year: '2017'
repository: https://github.com/broadinstitute/depmap_omics
---

# DepMap

The Cancer Dependency Map (DepMap) is a comprehensive effort to systematically identify cancer dependencies and the biomarkers that predict them. As a collaborative initiative led by the Broad Institute, DepMap aims to accelerate the development of precision treatments for cancer by providing open access to key cancer dependency data, analytical tools, and visualization resources.

## About DepMap

DepMap uses genome-wide pooled CRISPR-Cas9 knockout screens and small molecule screens across thousands of genomically characterized cancer cell lines to identify dependencies that are specific to tumor subsets. These dependencies represent potential therapeutic targets, as they are genes or pathways that cancer cells rely on for survival but that normal cells can tolerate losing.

### Key Features

- **Comprehensive Screening**: Over 2,000 cancer cell lines representing diverse cancer types and molecular contexts
- **Multi-modal Data**: Integration of CRISPR screens, drug screens, and omics data (genomics, transcriptomics, proteomics, metabolomics)
- **Quarterly Releases**: Regular data updates with new cell lines, assays, and analytical improvements
- **Open Access**: All data and tools are freely available to the research community

## Data Types

### CRISPR Dependency Data
- **Gene Effects**: Processed using the Chronos algorithm to correct for copy number effects
- **Cell Line Coverage**: 2,000+ cell lines spanning multiple cancer types
- **Gene Coverage**: Genome-wide screening targeting ~18,000 genes

### Drug Sensitivity Data
- **Platforms**: Integration of data from GDSC, PRISM, and CTD2 screening efforts
- **Compound Coverage**: Thousands of compounds including FDA-approved drugs and experimental molecules
- **Dose-Response**: Comprehensive dose-response curves for accurate sensitivity measurements

### Omics Data
- **Expression**: RNA-seq data for all cell lines
- **Mutations**: Comprehensive mutation calling from whole-exome sequencing
- **Copy Number**: High-resolution copy number profiles
- **Proteomics**: Mass spectrometry-based protein abundance measurements
- **Metabolomics**: Small molecule metabolite profiles

## Tools and Interfaces

### Data Explorer
Interactive visualization tool allowing users to explore relationships between different data types, compare biomarkers, and identify patterns across cell lines.

### Cell Line Selector
Specialized tool for identifying and selecting cell lines based on specific criteria such as lineage, mutations, expression levels, or dependency profiles.

### Target Discovery App
Advanced analytics platform for identifying the most selective and predictable gene dependencies, helping prioritize potential therapeutic targets.

### Context Explorer
Tool for exploring genetic dependencies and compound sensitivities within specific cancer contexts, lineages, and molecular subtypes.

## Applications

DepMap data enables researchers to:
- Identify novel therapeutic targets specific to cancer subtypes
- Discover biomarkers that predict drug sensitivity
- Understand the genetic basis of cancer dependencies
- Prioritize compounds for further development
- Design combination therapy strategies

## Data Access

All DepMap data is freely available through:
- **Interactive Portal**: Web-based tools for data exploration and visualization
- **Bulk Downloads**: Complete datasets in standard formats (CSV, TSV)
- **Quarterly Releases**: Regular data updates with version control
- **Documentation**: Comprehensive guides and tutorials for data usage

## Citation

When using DepMap data, please cite the foundational publications and acknowledge the specific data release version used in your research.
