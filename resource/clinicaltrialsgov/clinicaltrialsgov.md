---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://clinicaltrials.gov
  label: ClinicalTrials.gov
- category: Organization
  contact_details:
  - contact_type: email
    value: register@clinicaltrials.gov
  label: ClinicalTrials.gov Help Desk
description: ClinicalTrials.gov is a registry and results database of publicly and
  privately supported clinical studies of human participants conducted around the
  world. It is maintained by the National Library of Medicine (NLM) at the National
  Institutes of Health (NIH). The database provides information about clinical trials
  including their purpose, eligibility criteria, locations, and current status.
domains:
- clinical
- health
- public health
- biomedical
- translational
fairsharing_id: FAIRsharing.mewhad
homepage_url: https://clinicaltrials.gov/
id: clinicaltrialsgov
layout: resource_detail
license:
  id: https://clinicaltrials.gov/about-site/terms-conditions
  label: Public Domain
name: ClinicalTrials.gov
products:
- category: GraphicalInterface
  description: Web interface for searching and accessing clinical trial data
  format: http
  id: clinicaltrialsgov.site
  name: ClinicalTrials.gov Web Interface
  original_source:
  - clinicaltrialsgov
  product_url: https://clinicaltrials.gov/
- category: ProgrammingInterface
  description: API for programmatic access to ClinicalTrials.gov data
  format: http
  id: clinicaltrialsgov.api
  is_public: true
  name: ClinicalTrials.gov API
  original_source:
  - clinicaltrialsgov
  product_url: https://clinicaltrials.gov/data-api/
- category: Product
  description: Database for Aggregate Analysis of ClinicalTrials.gov (AACT) providing
    normalized metadata across trials
  format: postgres
  id: clinicaltrialsgov.aact
  name: AACT Database
  original_source:
  - clinicaltrialsgov
  product_url: https://aact.ctti-clinicaltrials.org/
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
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
  - File was not able to be retrieved when checked on 2025-10-21_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-15_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-15_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-08-07_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-10-21: HTTP 404 error
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
  - File was not able to be retrieved when checked on 2025-10-21_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-15_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-10-21: HTTP 403 error
    when accessing file'
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
## Overview

ClinicalTrials.gov is a registry and results database of publicly and privately supported clinical studies of human participants conducted around the world. The resource was established in 2000 in response to the Food and Drug Administration Modernization Act of 1997 (FDAMA) and is maintained by the National Library of Medicine (NLM) at the National Institutes of Health (NIH).

## Features

- Registry of over 444,000 clinical trials from 221 countries
- Detailed information about study protocols, eligibility criteria, and locations
- Results database for completed trials
- Linkage to published literature via PubMed
- Advanced search capabilities
- Data accessible via web interface and API
- Support for regulatory compliance with trial registration and results reporting requirements

## Data Content

The database contains a wealth of information about clinical trials, including:

- Study title and summary
- Study design and methodology
- Intervention details
- Eligibility criteria
- Locations and contact information
- Study start and completion dates
- Participant demographics
- Outcome measures and results
- Adverse events
- Publications related to the trial

## History

ClinicalTrials.gov was made available to the public via the internet on February 29, 2000. The database was expanded in response to the Food and Drug Administration Amendments Act of 2007 (FDAAA) to include more comprehensive trial registration data and basic results reporting. The system continues to evolve to improve transparency in clinical research and provide valuable information to researchers, healthcare providers, and patients.