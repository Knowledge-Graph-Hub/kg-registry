---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: finngen-info@helsinki.fi
  label: FinnGen
description: FinnGen is a large-scale genomics research project aimed at improving
  human health through genetic insights from the genetically unique Finnish population,
  combining genome information with digital health record data from 500,000 Finnish
  biobank participants.
domains:
- genomics
- biomedical
- health
- precision medicine
- clinical
homepage_url: https://www.finngen.fi/en
id: finngen
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: FinnGen
products:
- category: Product
  description: Summary statistics from genome-wide association studies of various
    disease phenotypes conducted on Finnish population data, with the most recent
    release being Data Freeze 13.
  id: finngen.summary_stats
  name: FinnGen GWAS Summary Statistics
  product_url: https://www.finngen.fi/en/access_results
- category: GraphicalInterface
  description: A web service for browsing disease endpoints in FinnGen, including
    statistics, definitions, and relationships between diseases.
  id: finngen.risteys
  name: Risteys
  product_url: https://risteys.finngen.fi/
- category: Product
  description: Results from meta-analysis of FinnGen data with other major biobanks,
    allowing for more powerful detection of genetic associations.
  id: finngen.meta_analysis
  name: FinnGen Meta-Analysis Results
  product_url: https://www.finngen.fi/en/access_results
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - clingen
  - clinvar
  - mgd
  - rgd
  - orphanet
  - psygenet
  - uniprot
  - disgenet
  - hp
  - gwascatalog
  - phewascat
  - ukbiobank
  - finngen
  - clinicaltrialsgov
  product_url: https://www.disgenet.com/
  secondary_source:
  - disgenet
- category: Product
  description: Clinical endpoint definitions and control groups for FinnGen data releases,
    including detailed documentation for each data freeze.
  id: finngen.endpoints
  name: FinnGen Clinical Endpoints
  product_url: https://www.finngen.fi/en/researchers/clinical-endpoints
publications:
- doi: 10.1038/s41588-024-01975-5
  id: doi:10.1038/s41588-024-01975-5
  title: Genome-wide association study reveals mechanisms underlying dilated cardiomyopathy
    and myocardial resilience
  year: '2024'
- doi: 10.1038/s41588-025-02100-w
  id: doi:10.1038/s41588-025-02100-w
  title: Genome-wide association study of long COVID
  year: '2025'
taxon:
- NCBITaxon:9606
---
# FinnGen

FinnGen is a large-scale public-private partnership research project combining genome information with digital health record data from Finnish biobanks and health registries. The project aims to improve human health through genetic research and advance the development of personalized medicine.

## About FinnGen

FinnGen is one of the world's leading biobank studies, with the goal of collecting and analyzing genome and health data from 500,000 Finnish biobank participants. The unique genetic makeup of the Finnish population, characterized by genetic isolation and bottleneck effects, makes it particularly valuable for identifying rare genetic variants associated with diseases.

The project is coordinated by the University of Helsinki and includes:
- All Finnish public biobanks
- Finnish universities
- Hospital districts 
- International pharmaceutical companies
- Finnish research institutes

## Key Features

### Comprehensive Health Record Data

FinnGen combines genotype data with extensive digital health record data from national health registries, covering:
- Hospital visits and diagnoses
- Medication purchases and prescriptions
- Surgical procedures
- Cancer registry data
- Death registry data

This comprehensive longitudinal data, sometimes spanning decades for individual participants, enables powerful phenotype analyses across a wide range of diseases and conditions.

### Data Freezes

FinnGen regularly releases data in "freezes" as the project progresses, with each release including more samples and updated analyses:

- **Current Release**: Data Freeze 13 (DF13) - The most recent data release includes detailed clinical endpoint definitions and comprehensive GWAS results
- **Previous Releases**: Data Freezes 2-12 - Each with varying numbers of participants, genotyped variants, and phenotype endpoints

### Clinical Endpoints

The project has developed a significant collection of meaningful clinical endpoints based on digital health record data from Finnish health registries. These endpoints are carefully defined to enable precise genetic association studies across many disease categories.

## Applications and Impact

FinnGen data has been used in hundreds of scientific publications, contributing to the understanding of:

1. **Disease Mechanisms**: Identifying genetic factors contributing to common and rare diseases
2. **Drug Target Discovery**: Finding potential therapeutic targets for various conditions
3. **Genetic Risk Prediction**: Developing and validating polygenic risk scores
4. **Population Genetics**: Understanding the genetic structure and history of Finnish populations
5. **Pharmacogenomics**: Studying how genetic variation affects drug response

## Data Access

FinnGen follows the principles of open science and makes its data accessible to the research community while respecting privacy regulations:

1. **Summary Statistics**: Publicly available GWAS summary statistics for hundreds of phenotypes
2. **Risteys**: A public web interface for browsing phenotype information and summary statistics
3. **Controlled Access**: More detailed data available for qualified researchers through application

## Related Resources

FinnGen data is frequently used in combination with other biobanks and genetic resources, including:
- UK Biobank
- Estonian Biobank
- BioBank Japan
- Million Veteran Program