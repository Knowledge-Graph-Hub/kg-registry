---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: ClinicalTrials.gov@nih.gov
  - contact_type: url
    value: https://clinicaltrials.gov/about-site/contact
  id: ncbi
  label: National Library of Medicine Clinical Trials Team
- category: Organization
  contact_details:
  - contact_type: email
    value: register@clinicaltrials.gov
  label: ClinicalTrials.gov Help Desk
description: ClinicalTrials.gov is a database of privately and publicly funded clinical
  studies conducted around the world, maintained by the National Library of Medicine
  (NLM) at the National Institutes of Health (NIH). The registry contains information
  on over 400,000 studies covering a wide range of diseases and conditions, providing
  details about study design, locations, eligibility criteria, interventions, outcomes,
  and results. ClinicalTrials.gov serves as the primary registry for clinical trials
  required by the FDA Amendments Act and WHO International Clinical Trials Registry
  Platform (ICTRP).
domains:
- clinical
- health
- public health
- drug discovery
- precision medicine
- biomedical
- translational
fairsharing_id: FAIRsharing.mewhad
homepage_url: https://clinicaltrials.gov/
id: clinicaltrialsgov
infores_id: clinicaltrials
layout: resource_detail
license:
  id: https://clinicaltrials.gov/about-site/terms-conditions
  label: Public Domain
name: ClinicalTrials.gov
products:
- category: GraphicalInterface
  description: Web-based interface for searching and browsing clinical trials with
    advanced filtering and export capabilities
  format: http
  id: clinicaltrialsgov.search
  name: ClinicalTrials.gov Search Portal
  original_source:
  - clinicaltrialsgov
  product_url: https://clinicaltrials.gov/search
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to all clinical trial records
    with JSON and CSV output formats
  format: http
  id: clinicaltrialsgov.api
  is_public: true
  name: ClinicalTrials.gov API
  original_source:
  - clinicaltrialsgov
  product_url: https://clinicaltrials.gov/data-api/api
- category: Product
  description: Bulk downloads of all clinical trial records in multiple formats including
    XML, JSON, and CSV
  format: mixed
  id: clinicaltrialsgov.downloads
  name: ClinicalTrials.gov Data Downloads
  original_source:
  - clinicaltrialsgov
  product_url: https://clinicaltrials.gov/data-about-studies/download-clinical-trial-data
- category: Product
  description: Aggregate Analysis of ClinicalTrials.gov (AACT) - A relational PostgreSQL
    database containing all clinical trial data, updated daily
  format: postgres
  id: clinicaltrialsgov.aact
  name: AACT Database
  original_source:
  - clinicaltrialsgov
  product_url: https://aact.ctti-clinicaltrials.org/
- category: DocumentationProduct
  description: Comprehensive documentation covering data structure, data element definitions,
    and API usage
  format: http
  id: clinicaltrialsgov.docs
  name: ClinicalTrials.gov Documentation
  original_source:
  - clinicaltrialsgov
  product_url: https://clinicaltrials.gov/about-site
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - pubmed
  - mesh
  - pid
  - doid
  - diseases
  - drugcentral
  - go
  - gwascatalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
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
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - chembl
  - sider
  - reactome
  - wikipathways
  - hp
  - nihreporter
  - disgenet
  - pubmed
  - gwascatalog
  - cellmarker
  - go
  - bgee
  - ccle
  - clinicaltrialsgov
  - indra
  product_url: https://github.com/gyorilab/indra_cogex
  secondary_source:
  - indra
- category: Product
  description: Complete RepoDB dataset containing drug repositioning successes and
    failures, with approved drugs, indications, and clinical trial outcomes
  format: csv
  id: repodb.full_dataset
  name: RepoDB Full Dataset
  original_source:
  - drugcentral
  - clinicaltrialsgov
  product_url: https://unmtid-shinyapps.net/shiny/repodb/session/98046b0f66cea75c432b5576c1ba2840/download/downloadFull?w=
  warnings:
  - File was not able to be retrieved when checked on 2025-12-08_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-07_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-27_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-08-07_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-12-08: HTTP 404 error
    when accessing file'
- category: Product
  description: Clinical trial information from ClinicalTrials.gov
  format: http
  id: genecards.clinical.trials
  name: GeneCards Clinical Trials
  original_source:
  - clinicaltrialsgov
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-08_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-08_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-08: HTTP 403 error
    when accessing file'
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
publications:
- authors:
  - Zarin DA
  - Tse T
  - Williams RJ
  - Califf RM
  - Ide NC
  doi: doi:10.1056/NEJMsa1012065
  id: https://pubmed.ncbi.nlm.nih.gov/21366476/
  journal: The New England Journal of Medicine
  preferred: true
  title: The ClinicalTrials.gov results database--update and key issues
  year: '2011'
repository: https://github.com/ctti-clinicaltrials/aact
---
# ClinicalTrials.gov

## Overview

ClinicalTrials.gov is a comprehensive database of clinical studies conducted in the United States and around the world. Maintained by the National Library of Medicine (NLM) at the National Institutes of Health (NIH), it provides the public with easy access to information on publicly and privately supported clinical studies on a wide range of diseases and conditions.

The resource was established in 2000 in response to the Food and Drug Administration Modernization Act of 1997 (FDAMA). The database was expanded in response to the Food and Drug Administration Amendments Act of 2007 (FDAAA) to include more comprehensive trial registration data and basic results reporting. The system continues to evolve to improve transparency in clinical research and provide valuable information to researchers, healthcare providers, and patients.

## Content and Coverage

### Study Types
- **Interventional Studies**: Trials testing new treatments, drugs, devices, or behavioral interventions
- **Observational Studies**: Studies examining health outcomes in specific populations without intervention
- **Expanded Access**: Investigational treatments available outside of clinical trials
- **Patient Registries**: Collections of patient health information for specific diseases or conditions

### Data Elements
Each clinical trial record includes:
- Study identification and registration information
- Study title and summary
- Study design and methodology
- Eligibility criteria (inclusion/exclusion)
- Interventions and comparators
- Outcome measures (primary and secondary)
- Study locations and contact information
- Study start and completion dates
- Participant demographics
- Results data (when available)
- Adverse events
- Publications and references

### Coverage Statistics
- **400,000+** registered clinical studies
- **220+ countries** represented
- **All 50 US states** plus territories
- **Daily updates** with new and modified records

## Regulatory Context

ClinicalTrials.gov serves as the primary registry for:
- FDA Amendments Act (FDAAA) Section 801 compliance
- WHO International Clinical Trials Registry Platform (ICTRP)
- International Committee of Medical Journal Editors (ICMJE) requirements
- Support for regulatory compliance with trial registration and results reporting requirements

## Data Access Methods

### Web Interface
The primary search portal allows:
- Advanced search with multiple filters
- Geographic visualization of study locations
- Export of search results
- Study comparison tools
- Linkage to published literature via PubMed

### REST API
The ClinicalTrials.gov API provides:
- Programmatic access to all trial records
- JSON and CSV output formats
- Field-level queries
- Pagination for large result sets
- Rate limiting: No authentication required for reasonable use

### Bulk Downloads
Complete database exports available in:
- XML format (pipe-delimited files)
- JSON format
- CSV format
- Daily and monthly update files

### AACT Database
The Aggregate Analysis of ClinicalTrials.gov (AACT) database:
- Relational PostgreSQL database
- Daily updates from ClinicalTrials.gov
- Optimized for aggregate analysis and research
- Free access with straightforward schema
- Maintained by the Clinical Trials Transformation Initiative (CTTI)
- Code repository: https://github.com/ctti-clinicaltrials/aact

## Use Cases

1. **Patient Recruitment**: Finding eligible clinical trials for specific conditions
2. **Research**: Analyzing trends in clinical research and drug development
3. **Systematic Reviews**: Identifying all trials for meta-analyses
4. **Regulatory Compliance**: Meeting trial registration requirements
5. **Transparency**: Public access to study designs and results
6. **Competitive Intelligence**: Tracking clinical development pipelines
7. **Public Health**: Monitoring research activity for specific diseases

## Data Quality and Compliance

- Study sponsors and investigators are responsible for data accuracy
- Results must be submitted within one year of study completion (FDAAA requirement)
- NLM performs quality control checks but does not independently verify all data
- Records marked with data quality issues or non-compliance indicators

## Information Resource ID

This resource has the Information Resource identifier: `infores:clinicaltrials`

## Important Notes

- **Registration is not approval**: Listing a study does not mean it has been evaluated by the US Federal Government
- **Results may be incomplete**: Not all studies are required to submit results
- **Contact study sites**: For participation, contact information is provided in each record
- **Updates**: Records are maintained by study sponsors and may be updated throughout the study lifecycle