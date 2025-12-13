---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: The NCI Genomic Data Commons (GDC) is a data sharing platform promoting
  precision medicine in oncology by providing unified access to harmonized cancer
  genomic and clinical data from major cancer research programs including TCGA and
  TARGET, processed with standardized bioinformatics pipelines to enable direct comparison
  and integrated analysis.
domains:
- genomics
- precision medicine
- clinical
- biomedical
id: gdc
infores_id: gdc
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: National Cancer Institute Genomic Data Commons Data Portal
homepage_url: https://portal.gdc.cancer.gov
synonyms:
- GDC
- Genomic Data Commons
contacts:
- category: Organization
  label: National Cancer Institute
  contact_details:
  - contact_type: url
    value: https://www.cancer.gov/
  - contact_type: url
    value: https://gdc.cancer.gov/
taxon:
- NCBITaxon:9606
---

# NCI Genomic Data Commons (GDC)

## Overview

The National Cancer Institute's (NCI) Genomic Data Commons (GDC) is a unified data repository and knowledge network that promotes precision medicine in oncology. It is not just a database or tool, but an expandable platform supporting the import, standardization, and harmonization of genomic and clinical data from cancer research programs. For the first time, major cancer genomic datasets have been processed using common bioinformatics pipelines, enabling direct comparison and integrated analysis across studies.

## Mission

To provide the cancer research community with a unified repository and cancer knowledge base that enables data sharing across cancer genomic studies in support of precision medicine.

## Core Datasets

The GDC contains NCI-generated data from major comprehensive cancer genomic programs:

### The Cancer Genome Atlas (TCGA)
- Comprehensive molecular characterization of over 33 cancer types
- More than 11,000 cases
- Multiple data types: WGS, WXS, RNA-seq, miRNA-seq, methylation, copy number
- Extensive clinical and biospecimen annotations

### Therapeutically Applicable Research to Generate Effective Therapies (TARGET)
- Focus on childhood cancers
- Genomic characterization to identify therapeutic targets
- Multiple pediatric cancer types
- Integrated molecular and clinical data

### Additional Programs
- Foundation Medicine (FMI)
- Clinical Proteomic Tumor Analysis Consortium (CPTAC)
- Human Cancer Models Initiative (HCMI)
- Community-contributed datasets

## Data Harmonization

A key innovation of the GDC is harmonized data processing:

### Standardized Bioinformatics Pipelines
- **DNA Alignment**: BWA, MuSE, MuTect2, VarScan2, SomaticSniper
- **Variant Calling**: Somatic and germline variant detection
- **RNA Analysis**: STAR alignment, HTSeq quantification
- **Methylation**: Liftover and annotation
- **Copy Number**: Segmentation and calling
- **Common Reference**: GRCh38 human reference genome

### Benefits of Harmonization
- Direct comparison across studies
- Reduced technical batch effects
- Standardized file formats
- Consistent quality control
- Reproducible analyses

## Data Portal Features

### Exploration Tools

#### Projects App
- Browse cancer research programs
- View project-level statistics
- Access primary data from foundational studies

#### Cohort Builder
- Create custom patient cohorts
- Filter by clinical features (age, diagnosis, stage, treatment)
- Filter by biospecimen attributes
- Filter by molecular features (mutations, expression)
- Save and share cohorts

#### Repository App
- Browse and filter files
- Search by file type, workflow, experimental strategy
- Download individual or batch files
- Cart management for selections

### Analysis and Visualization

#### Survival Analysis
- Kaplan-Meier survival plots
- Cohort comparison
- Custom survival endpoints

#### Mutation Frequency
- Gene-level mutation frequencies
- Mutation types (missense, nonsense, indels)
- Cohort-specific frequencies

#### ProteinPaint
- Interactive protein structure visualization
- Mutation mapping to protein domains
- 3D structure integration

#### OncoMatrix
- Heatmap visualization of mutations
- Gene × sample matrices
- Co-mutation patterns

## Data Types Available

### Raw Data
- BAM files (aligned reads)
- FASTQ files (unaligned reads)

### Higher-Level Data
- **Variant Calls**: Somatic mutations, germline variants
- **Gene Expression**: RNA-seq quantification (FPKM, TPM, counts)
- **Copy Number**: Segmented and called copy number alterations
- **Methylation**: CpG site methylation values
- **miRNA Expression**: microRNA quantification

### Clinical Data
- Demographics
- Diagnoses and staging
- Treatment history
- Follow-up and outcomes
- Family history
- Exposures

### Biospecimen Data
- Sample types (tumor, normal, blood)
- Anatomical site
- Preservation method
- Molecular analyte information

## Access Methods

### Web-Based Portal
- Interactive exploration at https://portal.gdc.cancer.gov/
- No login required for open-access data
- eRA Commons/dbGaP credentials for controlled-access data

### GDC API
- Programmatic data access
- RESTful endpoints
- Query language for filtering
- JSON responses
- Bulk download support

### GDC Data Transfer Tool
- Command-line tool for large file downloads
- Resume interrupted transfers
- Parallel downloads
- Manifest-based batch downloads

### Data Submission Portal
- Upload and validate data
- Metadata submission
- Quality control checks
- Project management

## Applications

### Precision Oncology
- Molecular subtype classification
- Biomarker discovery and validation
- Therapeutic target identification
- Drug resistance mechanism elucidation

### Cancer Research
- Driver gene identification
- Mutational signature analysis
- Pathway dysregulation studies
- Tumor evolution and heterogeneity
- Cross-cancer comparative analyses

### Clinical Translation
- Companion diagnostic development
- Clinical trial design
- Patient stratification strategies
- Treatment response prediction

### Computational Biology
- Algorithm development and benchmarking
- Machine learning model training
- Network analysis
- Integration with other resources

## Benefits for Research Community

- **Standardized Data**: Common processing eliminates technical variability
- **Open Access**: Majority of data publicly available
- **Cloud Computing**: Integration with cloud platforms for scalable analysis
- **Comprehensive Annotations**: Rich clinical and biospecimen metadata
- **APIs and Tools**: Multiple access methods for diverse use cases
- **Active Development**: Regular updates and new features
- **Community Support**: Documentation, training, helpdesk

## Integration

### NCI Cloud Resources
- Cancer Genomics Cloud pilots
- Seven Bridges Cancer Genomics Cloud
- ISB Cancer Genomics Cloud
- Broad Institute FireCloud

### External Resources
- cBioPortal integration
- UCSC Xena integration
- dbGaP linkage
- ClinVar submissions

## Quality and Standards

- Standardized data formats (BAM, VCF, MAF)
- Controlled vocabularies
- Data quality metrics
- Validation workflows
- Provenance tracking

## Information Resource ID

This resource has the Information Resource identifier: `infores:gdc`

## Documentation and Support

- **Portal**: https://portal.gdc.cancer.gov/
- **API Documentation**: https://docs.gdc.cancer.gov/API/
- **Data Transfer Tool**: https://docs.gdc.cancer.gov/Data_Transfer_Tool/Users_Guide/
- **Support**: https://gdc.cancer.gov/support
- **Publications**: https://gdc.cancer.gov/about-data/publications

For more information, visit https://gdc.cancer.gov/.
