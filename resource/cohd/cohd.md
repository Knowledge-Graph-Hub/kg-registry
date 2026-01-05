---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://people.dbmi.columbia.edu/~chw7007/
  label: Columbia University Department of Biomedical Informatics - Weng Lab
creation_date: '2025-11-04T00:00:00Z'
description: The Columbia Open Health Data (COHD) API provides access to observed
  clinical frequencies and co-occurrence frequencies from electronic health records
  at Columbia University Medical Center. The database contains counts and frequencies
  of conditions, procedures, drug exposures, and patient demographics from the OHDSI
  common data model, along with statistical associations between clinical concepts.
  To protect patient privacy, all concepts where count ≤10 were excluded and counts
  were randomized using Poisson distribution. COHD offers multiple datasets including
  5-year (2013-2017) and lifetime data, both in hierarchical and non-hierarchical
  forms, plus beta temporal co-occurrence data.
domains:
- clinical
- health
- public health
- precision medicine
homepage_url: https://cohd.io/
id: cohd
infores_id: cohd
last_modified_date: '2025-11-04T00:00:00Z'
layout: resource_detail
name: Columbia Open Health Data (COHD)
products:
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to clinical concept frequencies,
    co-occurrences, and associations with JSON output
  format: http
  id: cohd.api
  name: COHD API
  original_source:
  - cohd
  product_url: https://cohd.io/api
- category: GraphicalInterface
  description: Interactive web interface for exploring clinical concept frequencies
    and associations
  format: http
  id: cohd.portal
  name: COHD Web Interface
  original_source:
  - cohd
  product_url: https://cohd.io/
- category: ProcessProduct
  description: Python Jupyter notebooks demonstrating COHD API usage and analysis
    workflows
  format: http
  id: cohd.notebooks
  name: COHD API Examples
  original_source:
  - cohd
  product_file_size: 2834847
  product_url: https://github.com/WengLab-InformaticsResearch/cohd_api/blob/master/notebooks/COHD_API_Example.ipynb
- category: DocumentationProduct
  description: API documentation covering endpoint descriptions, data structure, and
    usage examples
  format: http
  id: cohd.docs
  name: COHD Documentation
  original_source:
  - cohd
  product_url: https://cohd.io/api
  warnings:
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 502 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-05_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-05: HTTP 502 error
    when accessing file'
repository: https://github.com/WengLab-InformaticsResearch/cohd_api
taxon:
- NCBITaxon:9606
---
# Columbia Open Health Data (COHD)

## Overview

The Columbia Open Health Data (COHD) project provides an API for accessing observed clinical frequencies and co-occurrence patterns from electronic health records at Columbia University Medical Center. The database is built on the OHDSI (Observational Health Data Sciences and Informatics) common data model and provides valuable real-world evidence about the prevalence of medical conditions, procedures, and drug exposures in clinical practice.

## Data Content

### Available Datasets

**1. 5-Year Non-Hierarchical Dataset (2013-2017)**
- Clinical data from a 5-year window
- Counts at the specified concept level only
- Better underlying data consistency

**2. Lifetime Non-Hierarchical Dataset**
- Clinical data from all available dates
- Larger patient population
- Broader concept coverage

**3. 5-Year Hierarchical Dataset (2013-2017)**
- Counts include patients from descendant concepts
- Example: Ibuprofen includes all specific formulations (600mg tablets, 400mg tablets, oral suspensions, etc.)
- Clinical data from 2013-2017

**4. Temporal Co-occurrence Data (BETA)**
- Time-aware co-occurrence patterns
- Still under active development

### Data Elements

COHD provides access to:
- **Concept Counts**: Number of patients associated with each clinical concept
- **Concept Frequencies**: Prevalence (count / total patients) in EHR
- **Co-occurrence Counts**: Number of patients with pairs of concepts
- **Co-occurrence Frequencies**: Joint prevalence of concept pairs
- **Statistical Associations**: Chi-square, relative frequency, and observed-to-expected ratios

### Vocabulary Standards

All clinical concepts are coded using standard concept IDs from the OMOP Common Data Model:
- Conditions (e.g., SNOMED CT)
- Procedures (e.g., CPT, HCPCS)
- Drugs (e.g., RxNorm)
- Demographics

The API includes mapping functionality to translate between vocabularies and other ontologies using the EMBL-EBI Ontology Xref Service (OxO).

## Privacy Protection

To protect patient privacy:
- All concepts and concept pairs with count ≤10 are excluded
- Counts are randomized using Poisson distribution
- No patient-level data is exposed
- Aggregate statistics only

## API Resources

### 1. Metadata
Dataset descriptions, concept counts, and database statistics

### 2. OMOP Vocabulary
Common vocabulary for name and concept identifier mapping between standard terminologies

### 3. Clinical Frequencies
Access to counts and frequencies of:
- Conditions
- Procedures  
- Drug exposures
- Patient demographics

### 4. Concept Associations
Inferred associations between concepts using:
- **Chi-square analysis**: Statistical significance of association
- **Relative frequency**: Ratio of observed to expected co-occurrence
- **Observed-to-expected ratio**: Strength of association

## Use Cases

1. **Hypothesis Generation**: Discovering potential drug-disease associations
2. **Comorbidity Analysis**: Understanding disease co-occurrence patterns
3. **Drug Safety**: Identifying adverse event signals
4. **Clinical Decision Support**: Providing EHR-based prevalence estimates
5. **Phenotype Definition**: Understanding clinical manifestations
6. **Drug Repurposing**: Finding new therapeutic applications
7. **Resource Annotation**: Enriching knowledge graphs with EHR frequencies

## Development Team

COHD was developed at the Columbia University Department of Biomedical Informatics through collaboration between:
- **Weng Lab**: Chunhua Weng, PhD
- **Tatonetti Lab**: Nicholas Tatonetti, PhD  
- **NCATS Biomedical Data Translator Program** (Red Team)

## Funding Support

- NCATS OT3TR002027
- NLM R01LM009886-08A1
- NIGMS R01GM107145

## External Resources

- [OHDSI](https://www.ohdsi.org/) - Observational Health Data Sciences and Informatics
- [OMOP Common Data Model](https://github.com/OHDSI/CommonDataModel/wiki) - Standardized data model
- [Athena](http://athena.ohdsi.org) - OMOP vocabulary browser
- [Atlas](http://www.ohdsi.org/web/atlas/) - OMOP analysis tools

## Information Resource ID

This resource has the Information Resource identifier: `infores:cohd`

## Technical Details

- **Data Source**: Columbia University Medical Center EHR
- **Data Model**: OHDSI OMOP CDM
- **Update Frequency**: Static snapshots from specified time periods
- **API Format**: REST with JSON responses
- **Authentication**: No authentication required