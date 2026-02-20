---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: Genebass is a comprehensive resource of exome-based gene-level and single-variant association statistics from 281,852 UK Biobank participants across 3,817 phenotypes, enabling large-scale genotype-phenotype association studies.
domains:
  - genomics
  - biomedical
id: "genebass"
infores_id: "genebass"
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: 'Genebass: Gene-based association summary statistics'
homepage_url: https://genebass.org/
synonyms:
  - Genebass
  - Gene-based association summary statistics
contacts:
  - category: Organization
    label: UK Biobank
    contact_details:
      - contact_type: url
        value: "https://www.ukbiobank.ac.uk/"
publications:
  - preferred: true
    id: doi:10.1016/j.xgen.2022.100168
    title: Systematic single-variant and gene-based association testing of thousands
      of phenotypes in 394,841 UK Biobank exomes
    journal: Cell Genomics
    year: "2022"
    doi: 10.1016/j.xgen.2022.100168
---

# Genebass: Gene-based association summary statistics

## Overview

Genebass is a comprehensive public resource providing exome-based association statistics from the UK Biobank. It encompasses 281,852 individuals with exome sequence data analyzed across 3,817 phenotypes, offering both gene-based and single-variant association testing results. This resource enables large-scale genotype-phenotype association studies and supports research in human genetics, rare variant analysis, and precision medicine.

## Data Content

### Dataset Statistics
- **Participants**: 281,852 individuals with exome sequencing data
- **Phenotypes**: 3,817 phenotypes spanning diverse health conditions and traits
- **Analysis Types**: Gene-based tests and single-variant tests
- **Coverage**: Comprehensive exome-wide association testing

### Phenotype Categories
- Quantitative traits (continuous measures)
- Binary traits (disease/control status)
- Clinical diagnoses from health records
- Laboratory measurements
- Anthropometric measurements
- Lifestyle and behavioral phenotypes

## Key Features

- **Gene-Based Testing**: Aggregated variant-level statistics at the gene level
- **Single-Variant Analysis**: Individual variant association results
- **Public Access**: Freely available summary statistics
- **Large Sample Size**: Powered by 281K+ exome-sequenced individuals
- **Diverse Phenotypes**: Thousands of health-related traits
- **UK Biobank Integration**: Leverages extensive UK Biobank phenotypic data

## Applications

### Genetic Research
- Identifying disease-associated genes and variants
- Rare variant association studies
- Functional validation of genetic findings
- Cross-phenotype pleiotropy analysis
- Gene prioritization for experimental studies

### Clinical Translation
- Precision medicine candidate discovery
- Risk prediction model development
- Understanding genetic architecture of diseases
- Drug target identification
- Pharmacogenomics research

### Population Genetics
- Allele frequency estimation in diverse ancestries
- Selection signature detection
- Evolutionary constraint analysis
- Population-specific genetic associations

## Access and Usage

- **Web Interface**: Interactive browser at https://genebass.org/
- **Search Functionality**: Query by gene, variant, or phenotype
- **Download Options**: Bulk download of summary statistics
- **Visualization Tools**: Built-in plotting and exploration features
- **API Access**: Programmatic data retrieval

## Technical Details

### Statistical Methods
- Gene-based burden tests
- SKAT-O (Sequence Kernel Association Test - Optimal)
- Single-variant logistic/linear regression
- Adjustment for covariates and population structure

### Data Format
- Summary statistics tables
- Effect sizes and standard errors
- P-values and confidence intervals
- Allele frequencies
- Sample sizes per analysis

## Information Resource ID

This resource has the Information Resource identifier: `infores:genebass`

## Citation

When using Genebass data, please cite the resource appropriately and acknowledge the UK Biobank.

For more information, visit https://genebass.org/
