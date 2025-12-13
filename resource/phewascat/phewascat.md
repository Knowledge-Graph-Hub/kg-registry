---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://phewascatalog.org/phewas/#home
  - contact_type: email
    value: joshua.c.denny@vumc.org
  label: Vanderbilt University Medical Center
creation_date: '2025-09-24T00:00:00Z'
description: The PheWAS Catalog is an aggregator of phenome-wide association studies
  that systematically analyzes many phenotypes compared to single genetic variants.
  It aggregates results from electronic medical record (EMR) data analysis, combining
  genetic association data from multiple biobanks and clinical databases to enable
  comprehensive phenotype-genotype association discovery.
domains:
- biomedical
- genomics
- clinical
- precision medicine
homepage_url: https://phewascatalog.org/phewas/#home
id: phewascat
last_modified_date: '2025-09-24T00:00:00Z'
layout: resource_detail
name: PheWAS Catalog
products:
- category: GraphicalInterface
  description: Web portal for browsing and accessing PheWAS association results and
    analysis tools
  format: http
  id: phewascat.portal
  name: PheWAS Catalog Portal
  product_url: https://phewascatalog.org/phewas/#home
- category: Product
  description: PheWAS association results for SNPs from GWAS Catalog analyzed against
    EMR-derived phenotypes
  format: csv
  id: phewascat.associations
  name: PheWAS Association Data
  product_url: https://phewascatalog.org/phewas/#home
- category: Product
  description: Phecode mapping files for translating ICD codes to phenotypes used
    in PheWAS analysis
  format: csv
  id: phewascat.phecodes
  name: Phecode Maps
  product_url: https://phewascatalog.org/phewas/#home
- category: ProgrammingInterface
  description: R package for performing PheWAS analysis using the catalog data and
    methods
  format: http
  id: phewascat.rpackage
  name: PheWAS R Package
  product_url: https://www.vumc.org/cpm/center-precision-medicine-blog/phewas-r-package
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
publications:
- authors:
  - Denny JC
  - Bastarache L
  - Ritchie MD
  id: doi:10.1038/nbt.2749
  journal: Nature Biotechnology
  preferred: true
  title: Systematic comparison of phenome-wide association study of electronic medical
    record data and genome-wide association study data
  year: '2013'
repository: https://github.com/nhgritctran/PheTK
tags:
- translator
taxon:
- NCBITaxon:9606
---
# PheWAS Catalog

The PheWAS Catalog is a comprehensive aggregator of phenome-wide association studies (PheWAS) that systematically analyzes associations between genetic variants and a wide range of phenotypes derived from electronic medical records (EMRs). This resource combines genetic data with clinical phenotypes to enable discovery of genetic associations across the phenome.

## Key Features

### Comprehensive Genetic-Phenotype Associations
- Contains PheWAS results for over 3,144 single-nucleotide polymorphisms (SNPs) from the NHGRI GWAS Catalog
- Analyzes 1,358 EMR-derived phenotypes for each genetic variant
- Includes data from 13,835 European-ancestry individuals across five eMERGE network sites
- Provides systematic comparison between PheWAS and traditional GWAS results

### Phecode System
- Uses standardized Phecode mapping system to translate ICD codes into phenotypes
- Phecode Map 1.2 covers 1,866 phenotypes based on ICD-9 and ICD-10 codes
- Extended Phecode Map X includes 3,612 phenotype groupings based on ICD-10
- Enables consistent phenotype definitions across different healthcare systems

### Validation and Replication
- Successfully replicated 66% (51/77) of sufficiently powered prior GWAS associations
- Identified 210/751 associations from all prior GWAS studies
- Discovered 63 potentially pleiotropic associations with genome-wide significance
- Provides independent validation cohort results for novel associations

## Data Sources

### Electronic Medical Records
- eMERGE (Electronic Medical Records and Genomics) network data
- Vanderbilt DNA biobank (BioVU) with linked EMR data
- Multiple healthcare institutions contributing phenotype data
- Standardized phenotype extraction and coding procedures

### Genetic Data
- NHGRI GWAS Catalog variants as of April 2012
- High-quality genotyped and imputed SNPs
- Population-stratified genetic association results
- Quality control and validation of genetic variants

### Clinical Phenotypes
- ICD-9 and ICD-10 diagnostic codes from EMRs
- Laboratory values and clinical measurements
- Medication prescriptions and procedures
- Longitudinal clinical data spanning multiple visits

## Applications

### Drug Discovery and Repurposing
- Identification of pleiotropic genetic effects for drug target validation
- Discovery of unexpected phenotype associations for drug repurposing
- Safety signal detection through genetic association patterns
- Biomarker identification for drug response prediction

### Precision Medicine
- Genetic risk prediction across multiple phenotypes
- Personalized disease risk assessment using genetic profiles
- Clinical decision support based on genetic associations
- Population-specific genetic risk stratification

### Genomic Medicine Research
- Hypothesis generation for novel genetic associations
- Validation platform for GWAS findings in clinical populations
- Cross-phenotype genetic correlation analysis
- Pleiotropy detection and characterization

### Clinical Phenotyping
- Standardization of EMR-derived phenotype definitions
- Validation of electronic phenotype algorithms
- Cross-institutional phenotype harmonization
- Quality assessment of clinical data extraction

## Technical Implementation
The PheWAS Catalog aggregates data through systematic analysis pipelines that process EMR data, apply Phecode mappings, perform genetic association testing, and provide statistical validation. The resource includes web-based tools for interactive exploration and programmatic access through R packages and APIs for computational workflows.