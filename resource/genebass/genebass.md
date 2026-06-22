---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ukbiobank.ac.uk/
  label: UK Biobank
creation_date: '2025-10-30T00:00:00Z'
description: Genebass is a comprehensive resource of exome-based gene-level and single-variant
  association statistics from 281,852 UK Biobank participants across 3,817 phenotypes,
  enabling large-scale genotype-phenotype association studies.
domains:
- genomics
- biomedical
homepage_url: https://genebass.org/
id: genebass
infores_id: genebass
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: 'Genebass: Gene-based association summary statistics'
products:
- category: GraphicalInterface
  description: Interactive web interface for searching and browsing Genebass gene-based
    and variant-level association results.
  format: http
  id: genebass.portal
  name: Genebass Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genebass
  product_url: https://app.genebass.org/
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Genetics KP distributed via the NCATS Translator
    release site (release 2026_03_27; build geneticskp_2026-03-27_1f1ad62b_2025sep1_4.3.6;
    source version 2026-03-27; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 653544
  format: kgx-jsonl
  id: translator.geneticskp.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Genetics KP KGX Graph
  node_count: 28023
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/geneticskp/latest/
  versions:
  - '2026_03_27'
  - geneticskp_2026-03-27_1f1ad62b_2025sep1_4.3.6
publications:
- authors:
  - Konrad J. Karczewski
  - Matthew Solomonson
  - Katherine R. Chao
  - Julia K. Goodrich
  - Grace Tiao
  - Wenhan Lu
  - Bridget M. Riley-Gillis
  - Ellen A. Tsai
  - Hye In Kim
  - Xiuwen Zheng
  - Fedik Rahimov
  - Sahar Esmaeeli
  - A. Jason Grundstad
  - Mark Reppell
  - Jeff Waring
  - Howard Jacob
  - David Sexton
  - Paola G. Bronson
  - Xing Chen
  - Xinli Hu
  - Jacqueline I. Goldstein
  - Daniel King
  - Christopher Vittal
  - Timothy Poterba
  - Duncan S. Palmer
  - Claire Churchhouse
  - Daniel P. Howrigan
  - Wei Zhou
  - Nicholas A. Watts
  - Kevin Nguyen
  - Huy Nguyen
  - Cara Mason
  - Christopher Farnham
  - Charlotte Tolonen
  - Laura D. Gauthier
  - Namrata Gupta
  - Daniel G. MacArthur
  - Heidi L. Rehm
  - Cotton Seed
  - Anthony A. Philippakis
  - Mark J. Daly
  - J. Wade Davis
  - Heiko Runz
  - Melissa R. Miller
  - Benjamin M. Neale
  doi: 10.1016/j.xgen.2022.100168
  id: doi:10.1016/j.xgen.2022.100168
  journal: Cell Genomics
  preferred: true
  title: Systematic single-variant and gene-based association testing of thousands of phenotypes in 394,841 UK Biobank exomes
  year: '2022'
synonyms:
- Genebass
- Gene-based association summary statistics
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