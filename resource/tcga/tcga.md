---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://gdc.cancer.gov/support
  label: NCI Genomic Data Commons Support
creation_date: '2025-11-08T00:00:00Z'
description: The Cancer Genome Atlas (TCGA) is a landmark cancer genomics program
  that molecularly characterized over 20,000 primary cancer and matched normal samples
  spanning 33 cancer types. This joint effort between NCI and the National Human Genome
  Research Institute began in 2006, bringing together researchers from diverse disciplines
  and multiple institutions. TCGA generated over 2.5 petabytes of genomic, epigenomic,
  transcriptomic, and proteomic data. The data, which has led to improvements in the
  ability to diagnose, treat, and prevent cancer, remains publicly available through
  the Genomic Data Commons for anyone in the research community to use.
domains:
- genomics
homepage_url: https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga
id: tcga
infores_id: tcga
last_modified_date: '2025-11-08T00:00:00Z'
layout: resource_detail
name: The Cancer Genome Atlas
products:
- category: Product
  description: Genomic Data Commons Data Portal providing access to harmonized TCGA
    data with over 2.5 petabytes of cancer genomic data
  format: http
  id: tcga.gdc_portal
  name: GDC Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://portal.gdc.cancer.gov/
- category: ProgrammingInterface
  description: Genomic Data Commons Application Programming Interface for programmatic
    access to TCGA and other cancer genomic data
  format: http
  id: tcga.gdc_api
  name: GDC API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://gdc.cancer.gov/developers/gdc-application-programming-interface-api
- category: GraphicalInterface
  description: Data Submission Portal for uploading and managing cancer genomic data
    submissions to GDC
  format: http
  id: tcga.gdc_submission
  name: GDC Data Submission Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://portal.gdc.cancer.gov/submission
- category: GraphProduct
  description: Neo4j knowledge graph integrating transcription factor target libraries,
    coexpression networks, and benchmark datasets used by the ChEA3 resource
  dump_format: neo4j
  format: neo4j
  id: chea-kg.graph
  name: ChEA-KG Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries, benchmark
    datasets, and additional supporting libraries
  format: http
  id: chea-kg.libraries
  name: ChEA-KG Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries and
    benchmark datasets
  format: http
  id: chea.libraries
  name: ChEA Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
synonyms:
- TCGA
taxon:
- NCBITaxon:9606
---
# The Cancer Genome Atlas

## Overview

The Cancer Genome Atlas (TCGA) is a landmark cancer genomics program that molecularly characterized over 20,000 primary cancer and matched normal samples spanning 33 cancer types. This joint effort between the National Cancer Institute (NCI) and the National Human Genome Research Institute began in 2006, bringing together researchers from diverse disciplines and multiple institutions.

## Data and Impact

Over twelve years, TCGA generated over 2.5 petabytes of genomic, epigenomic, transcriptomic, and proteomic data. The comprehensive molecular characterization has led to significant improvements in our ability to diagnose, treat, and prevent cancer. All TCGA data remains publicly available through the Genomic Data Commons (GDC) for anyone in the research community to use.

## Key Features

- **33 Cancer Types**: Comprehensive molecular characterization across diverse cancer types
- **20,000+ Samples**: Primary cancer and matched normal samples
- **Multi-omics Data**: Genomic, epigenomic, transcriptomic, and proteomic measurements
- **Harmonized Data**: Standardized clinical and genomic data for cross-analysis
- **Open Access**: All data publicly available through the GDC Data Portal

## Data Access

TCGA data is accessible through the [Genomic Data Commons Data Portal](https://portal.gdc.cancer.gov/), which provides:

- **Data Repository**: Browse and download clinical, biospecimen, and genomic data
- **Cohort Builder**: Create custom cohorts using clinical and biospecimen filters
- **Analysis Tools**: Visualization tools for genomic alterations and clinical features
- **API Access**: Programmatic access through the GDC API
- **Data Transfer Tool**: Efficient download of large data files

## Cancer Types Studied

TCGA selected [33 cancer types](https://www.cancer.gov/ccg/research/genome-sequencing/tcga/studied-cancers) for molecular characterization based on public health impact, availability of samples, and potential for biological insights.

## Information Resource ID

This resource has the Information Resource identifier: `infores:tcga`

## Support

For questions about TCGA data or the GDC applications, contact the [GDC Support team](https://gdc.cancer.gov/support).