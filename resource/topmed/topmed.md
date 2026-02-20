---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nhlbi.nih.gov/
  label: NHLBI (National Heart, Lung, and Blood Institute)
creation_date: '2025-10-30T00:00:00Z'
description: The NHLBI Trans-Omics for Precision Medicine (TOPMed) program generates
  scientific resources to enhance understanding of fundamental biological processes
  that underlie heart, lung, blood, and sleep disorders, providing whole genome sequencing
  and multi-omics data from diverse populations.
domains:
- genomics
- clinical
- precision medicine
homepage_url: https://topmed.nhlbi.nih.gov/
id: topmed
infores_id: topmed
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: NHLBI Trans-Omics for Precision Medicine
products:
- category: GraphicalInterface
  description: TOPMed program website for navigating cohorts, resources, and program
    documentation.
  format: http
  id: topmed.portal
  name: TOPMed Portal
  original_source:
  - topmed
  product_url: https://topmed.nhlbi.nih.gov/
- category: GraphicalInterface
  description: TOPMed data access page with instructions and links for controlled-access
    data workflows.
  format: http
  id: topmed.data-access
  name: TOPMed Data Access
  original_source:
  - topmed
  product_url: https://topmed.nhlbi.nih.gov/data-resources/data-access
- category: DocumentationProduct
  description: PDF summary table of whole-genome sequencing counts available in TOPMed.
  format: pdf
  id: topmed.wgs-counts
  name: TOPMed WGS Counts PDF
  original_source:
  - topmed
  product_file_size: 442890
  product_url: https://topmed.nhlbi.nih.gov/sites/default/files/documents/TOPMed%20WGS%20Counts%2020250505.pdf
publications:
- doi: 10.1038/s41586-021-03205-y
  id: doi:10.1038/s41586-021-03205-y
  journal: Nature
  preferred: true
  title: Sequencing of 53,831 diverse genomes from the NHLBI TOPMed Program
  year: '2021'
synonyms:
- TOPMed
- Trans-Omics for Precision Medicine
taxon:
- NCBITaxon:9606
---
# NHLBI Trans-Omics for Precision Medicine

## Overview

The NHLBI Trans-Omics for Precision Medicine (TOPMed) program is a major initiative by the National Heart, Lung, and Blood Institute to generate scientific resources that enhance understanding of fundamental biological processes underlying heart, lung, blood, and sleep (HLBS) disorders. TOPMed combines whole genome sequencing with extensive phenotypic characterization across diverse populations, creating one of the largest and most comprehensive genomic medicine resources.

## Program Scope

### Data Generation
- **Whole Genome Sequencing**: Deep coverage WGS from diverse cohorts
- **Multi-Omics**: RNA-seq, metabolomics, proteomics, epigenomics
- **Sample Size**: Over 180,000 individuals sequenced
- **Diversity**: Represents multiple ancestries and ethnic backgrounds
- **Phenotyping**: Extensive clinical and phenotypic data

### Focus Areas
- Cardiovascular diseases
- Pulmonary disorders
- Hematologic conditions
- Sleep disorders
- Risk factor assessment (blood pressure, lipids, etc.)

## Key Features

- **Population Diversity**: Includes underrepresented populations in genomic research
- **Longitudinal Data**: Many cohorts have decades of follow-up
- **Deep Phenotyping**: Rich clinical, environmental, and lifestyle data
- **Reference Panels**: High-quality haplotype reference for imputation
- **Variant Catalog**: Comprehensive catalog of genetic variation
- **Integrated Analysis**: Links genomic data with multi-omic and phenotypic information

## Data Types

### Genomic Data
- Whole genome sequences (30-40x coverage)
- Variant calls (SNVs, indels, structural variants)
- Haplotype phasing
- Reference panels for genotype imputation

### Phenotypic Data
- Disease diagnoses and outcomes
- Quantitative traits (blood pressure, lipids, lung function, etc.)
- Electronic health records
- Medication history
- Environmental exposures
- Lifestyle factors

### Multi-Omic Data
- RNA sequencing (gene expression)
- Metabolomics profiles
- Proteomic measurements
- Epigenetic marks (DNA methylation)

## Applications

### Precision Medicine
- Genetic risk prediction for HLBS diseases
- Pharmacogenomics and treatment response
- Disease subtype classification
- Personalized intervention strategies

### Scientific Discovery
- Novel gene-disease associations
- Rare variant identification
- Pleiotropy and genetic correlation analysis
- Functional genomics insights
- Population genetics and evolution

### Clinical Translation
- Biomarker discovery
- Drug target identification
- Clinical trial design
- Diagnostic test development

## Data Access

### dbGaP Repository
- Controlled-access individual-level data
- Phenotype and genotype files
- Application process for researchers

### Public Resources
- Summary statistics
- Allele frequencies (TOPMed Bravo variant browser)
- Reference panels for imputation
- Analysis pipelines and tools

## Participating Cohorts

TOPMed includes data from numerous established cohort studies:
- Framingham Heart Study
- Jackson Heart Study
- Multi-Ethnic Study of Atherosclerosis (MESA)
- Women's Health Initiative (WHI)
- Genetic Studies of Atherosclerosis Risk (GeneSTAR)
- And many others

## Computational Resources

- **Analysis Pipelines**: Standardized workflows for variant calling, QC, and analysis
- **Cloud Computing**: Integration with cloud platforms (BioData Catalyst)
- **Tools and Software**: Open-source analysis tools
- **Imputation Server**: TOPMed Imputation Server for genotype imputation

## Information Resource ID

This resource has the Information Resource identifier: `infores:topmed`

## Access

- **Homepage**: https://topmed.nhlbi.nih.gov/
- **Data Access**: https://www.ncbi.nlm.nih.gov/gap/ (dbGaP)
- **Variant Browser**: https://bravo.sph.umich.edu/freeze8/hg38/
- **Imputation Server**: https://imputation.biodatacatalyst.nhlbi.nih.gov/

For more information about TOPMed and data access, visit https://topmed.nhlbi.nih.gov/