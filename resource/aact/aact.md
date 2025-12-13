---
activity_status: active
category: Aggregator
creation_date: '2025-10-30T00:00:00Z'
description: AACT is a publicly available relational PostgreSQL database that contains
  all protocol and result data elements from every study registered in ClinicalTrials.gov,
  refreshed daily from the ClinicalTrials.gov registry.
domains:
- clinical
- public health
- translational
id: aact
infores_id: aact
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
name: Aggregate Analysis of ClinicalTrials.gov (AACT) Database
homepage_url: https://aact.ctti-clinicaltrials.org/
repository: https://github.com/ctti-clinicaltrials/aact
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://aact.ctti-clinicaltrials.org/contactus
  label: Clinical Trials Transformation Initiative (CTTI)
products:
- category: GraphicalInterface
  description: Web-based SQL query playground for running queries on AACT data directly
    from the browser
  format: http
  id: aact.playground
  name: AACT Playground
  original_source:
  - aact
  product_url: https://aact.ctti-clinicaltrials.org/playground
- category: Product
  description: Cloud-based PostgreSQL database with daily refreshed clinical trial
    data, accessible via standard PostgreSQL clients
  format: postgres
  id: aact.database
  name: AACT Cloud Database
  original_source:
  - clinicaltrialsgov
  product_url: https://aact.ctti-clinicaltrials.org/connect
- category: Product
  description: Static downloadable copies of the complete AACT database
  format: postgres
  id: aact.downloads
  name: AACT Database Downloads
  original_source:
  - clinicaltrialsgov
  product_url: https://aact.ctti-clinicaltrials.org/downloads
- category: DocumentationProduct
  description: Complete database schema documentation showing table structure and
    relationships
  id: aact.schema
  name: AACT Database Schema
  original_source:
  - aact
  product_url: https://aact.ctti-clinicaltrials.org/schema
- category: DocumentationProduct
  description: Data dictionary with detailed information about all AACT data elements
    and their relationship to ClinicalTrials.gov definitions
  id: aact.dictionary
  name: AACT Data Dictionary
  original_source:
  - aact
  product_url: https://aact.ctti-clinicaltrials.org/data_dictionary
synonyms:
- AACT
- Aggregate Analysis of ClinicalTrial.gov
taxon:
- NCBITaxon:9606
---

# Aggregate Analysis of ClinicalTrials.gov (AACT) Database

## Overview

AACT is a publicly available relational database that contains all information (protocol and result data elements) about every study registered in ClinicalTrials.gov. The database is maintained by the Clinical Trials Transformation Initiative (CTTI) and provides researchers and analysts with structured access to clinical trial data for analysis and research.

## Key Features

- **Daily Updates**: Database content is refreshed daily from ClinicalTrials.gov
- **Cloud Access**: PostgreSQL database directly accessible in the cloud with free account registration
- **Static Downloads**: Complete database snapshots available for download
- **Open Source**: Built with open source tools (PostgreSQL, Ruby on Rails) and source code available on GitHub
- **Multiple Access Methods**: Support for various PostgreSQL clients including pgAdmin, R/RStudio, SAS, and psql

## Data Content

AACT contains comprehensive information from ClinicalTrials.gov including:

- Study protocols and design information
- Enrollment and demographic data
- Intervention and outcome measures
- Results data including baseline characteristics, outcome measures, and adverse events
- Administrative and regulatory information
- Literature references and related publications

The database is organized into a relational structure with multiple tables representing different aspects of clinical trials data.

## Access Methods

- **Web Playground**: Browser-based SQL query interface for immediate data exploration
- **PostgreSQL Database**: Direct database connection via standard PostgreSQL clients
- **Downloaded Archives**: Full database dumps for local installation and analysis
- **Documentation**: Comprehensive schema documentation, data dictionary, and field mappings

## Use Cases

- Evaluating trends in clinical trial design and conduct
- Meta-analysis and systematic reviews of clinical research
- Analyzing reporting quality and completeness
- Studying geographic and temporal patterns in clinical trials
- Training and education in clinical research methods

## Management

AACT is maintained by the Clinical Trials Transformation Initiative (CTTI), a public-private partnership co-founded by Duke University and the U.S. Food and Drug Administration (FDA) to improve the quality and efficiency of clinical trials.

## Citation

Aggregate Analysis of ClinicalTrials.gov (AACT) Database. Clinical Trials Transformation Initiative (CTTI). Available at: https://aact.ctti-clinicaltrials.org/
