---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: griffithlab
  label: Griffith Lab
creation_date: '2025-10-30T00:00:00Z'
description: DoCM (Database of Curated Mutations) was a highly curated database of
  known, disease-causing mutations in cancer, specifically focused on mutations with
  clinical or functional evidence. The project has been retired and succeeded by the
  Clinical Interpretation of Variants in Cancer (CIViC) knowledgebase. All DoCM data
  remains available in archived form.
domains:
- precision medicine
- genomics
- health
homepage_url: http://www.docm.info/
id: docm
infores_id: docm
last_modified_date: '2025-01-20T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT
name: Database of Curated Mutations
products:
- category: Product
  compression: gzip
  description: Curated cancer mutations in tab-separated values format with gene,
    transcript, variant, and disease information
  format: tsv
  id: docm.variants.tsv
  name: DoCM Variants TSV
  original_source:
  - docm
  product_file_size: 35859
  product_url: https://github.com/griffithlab/docm/raw/master/data/variants.tsv.gz
- category: Product
  compression: gzip
  description: Curated cancer mutations in Variant Call Format (VCF)
  format: vcf
  id: docm.variants.vcf
  name: DoCM Variants VCF
  original_source:
  - docm
  product_file_size: 43955
  product_url: https://github.com/griffithlab/docm/raw/master/data/variants.vcf.gz
- category: ProcessProduct
  compression: gzip
  description: Complete DoCM database in SQL format for local installation
  id: docm.data.sql
  name: DoCM SQL Database
  original_source:
  - docm
  product_file_size: 1174722
  product_url: https://github.com/griffithlab/docm/raw/master/data/data.sql.gz
repository: https://github.com/griffithlab/docm
synonyms:
- DoCM
---
# Database of Curated Mutations (DoCM)

## Project Retirement Notice

**⚠️ DEPRECATED:** The DoCM project and DoCM.info web service has been retired as of October 2024. The project has been succeeded by [CIViC (Clinical Interpretation of Variants in Cancer)](https://civicdb.org/), which provides a more comprehensive and actively maintained resource for clinical cancer variant curation.

All historical DoCM data remains available in archived form through the GitHub repository.

## Overview

DoCM (Database of Curated Mutations) was a curated database of known, disease-causing mutations in cancer. The database was developed and maintained by the Griffith Lab at Washington University and focused specifically on mutations that had clinical or functional evidence in the published literature.

The database cataloged somatic mutations with evidence of driver status in human cancer, providing researchers and clinicians with a high-quality reference of well-characterized cancer mutations.

## Data Content

### Curated Mutations
DoCM contained manually curated cancer-associated mutations with:
- **Gene information**: Gene symbols and identifiers
- **Transcript details**: Reference transcripts for each variant
- **Variant nomenclature**: Precise mutation descriptions using HGVS notation
- **Disease associations**: Specific cancer types linked to each mutation
- **Literature evidence**: PubMed references supporting each curation
- **Functional impact**: Assessment of mutation effects on protein function

### Data Formats
The archived DoCM data is available in three formats:
1. **TSV**: Tab-separated values for easy parsing and analysis
2. **VCF**: Variant Call Format for genomics pipelines
3. **SQL**: Complete database dump for local installation

## Key Features

- **High-quality curation**: Manual review and annotation by domain experts
- **Evidence-based**: All mutations supported by published literature
- **Standardized nomenclature**: HGVS variant descriptions
- **Cancer-focused**: Specifically targeted somatic mutations in cancer
- **Multiple formats**: Data available in TSV, VCF, and SQL formats
- **Open access**: Freely available data under MIT license

## Successor Project

DoCM has been succeeded by **CIViC (Clinical Interpretation of Variants in Cancer)**, which provides:
- Broader scope of variant types and clinical significance
- Community-driven curation model
- Regular updates and maintenance
- Enhanced clinical interpretation framework
- Integration with multiple genomic databases

Users seeking actively maintained cancer variant data should use [CIViC](https://civicdb.org/) instead of DoCM.

## Access Methods

1. **Archived Data**: Download TSV, VCF, or SQL files from the GitHub repository
2. **GitHub Repository**: Access source code and archived data at https://github.com/griffithlab/docm
3. **Historical Web Interface**: The original docm.info website is no longer accessible

## Use Cases

While DoCM is retired, the archived data remains valuable for:
1. **Historical Analysis**: Studying the evolution of cancer mutation knowledge
2. **Benchmark Datasets**: Using curated mutations for validation studies
3. **Data Integration**: Incorporating legacy DoCM annotations into pipelines
4. **Comparative Studies**: Comparing historical curation against current resources
5. **Educational Purposes**: Learning about cancer mutation curation practices

## Technology Stack

- **Ruby on Rails**: Web application framework
- **PostgreSQL**: Relational database backend
- **JavaScript**: Frontend interactions
- **Haml**: Template engine
- **Less/CSS**: Styling

## Management

Developed and formerly maintained by the Griffith Lab at Washington University School of Medicine in St. Louis. The project was archived in October 2024, with all future curation efforts redirected to CIViC.

## Related Resources

- [CIViC](civic): Successor project providing actively maintained clinical cancer variant curation
- [ClinGen](clingen): Clinical genome resource for gene-disease validity
- [ClinVar](clinvar): Public archive of interpretations of clinically relevant variants

## Retirement Date

October 15, 2024 - Repository archived; web service discontinued