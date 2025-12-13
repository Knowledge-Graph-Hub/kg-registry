---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cpicpgx.org/contact/
  - contact_type: email
    value: contact@cpicpgx.org
  label: Clinical Pharmacogenetics Implementation Consortium (CPIC)
creation_date: '2025-09-03T00:00:00Z'
description: "The Clinical Pharmacogenetics Implementation Consortium (CPIC) creates,\
  \ curates, and disseminates freely available, peer-reviewed, evidence-based, and\
  \ updatable clinical practice guidelines that translate patient pharmacogenetic\
  \ test results into actionable prescribing decisions. CPIC also publishes structured\
  \ gene\u2013drug annotations, allele function data, standardized terminology resources,\
  \ and implementation tools (database, API, SOPs, educational materials) to accelerate\
  \ pharmacogenomics in clinical care."
domains:
- biomedical
- health
- clinical
- drug discovery
homepage_url: https://cpicpgx.org/
id: cpic
last_modified_date: '2025-09-03T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: CPIC
products:
- category: GraphicalInterface
  description: Main CPIC website portal providing access to guidelines, genes-drugs
    tables, alleles, publications, resources, and implementation information
  format: http
  id: cpic.portal
  name: CPIC Website Portal
  original_source:
  - cpic
  product_url: https://cpicpgx.org/
- category: DocumentationProduct
  description: Peer-reviewed, evidence-based, updatable pharmacogenetic clinical practice
    guidelines translating genotype into prescribing recommendations
  id: cpic.guidelines
  is_public: true
  name: CPIC Clinical Practice Guidelines
  original_source:
  - cpic
  product_url: https://cpicpgx.org/guidelines/
- category: DataProduct
  description: "Curated gene\u2013drug pair tables linking pharmacogenes with affected\
    \ medications and guideline recommendations"
  id: cpic.genes_drugs
  is_public: true
  name: CPIC Genes-Drugs Tables
  original_source:
  - cpic
  product_url: https://cpicpgx.org/genes-drugs/
- category: DataProduct
  description: Allele function and diplotype-to-phenotype tables standardized for
    clinical pharmacogenetic test result interpretation
  id: cpic.alleles
  is_public: true
  name: CPIC Allele & Diplotype Function Tables
  original_source:
  - cpic
  product_url: https://cpicpgx.org/alleles/
- category: ProgrammingInterface
  description: "Structured data (database and API) for CPIC guideline-derived gene\u2013\
    drug relationships, allele function, and standardized terms"
  id: cpic.api
  is_public: true
  name: CPIC Database & API
  original_source:
  - cpic
  product_url: https://github.com/cpicpgx/cpic-data/wiki
- category: DocumentationProduct
  description: Standard operating procedure PDF for assigning allele function and
    translating diplotypes to phenotypes
  format: pdf
  id: cpic.sop
  name: CPIC Pharmacogene Curation SOP
  original_source:
  - cpic
  product_file_size: 812796
  product_url: https://github.com/cpicpgx/cpic-sop/raw/main/CPIC%20Pharmacogene%20Curation%20SOP.pdf
- category: DocumentationProduct
  description: Overview slide deck describing CPIC assumptions, development process,
    and implementation guidance (PowerPoint)
  id: cpic.overview.slides
  name: CPIC Overview Presentation Slides
  original_source:
  - cpic
  product_file_size: 8552272
  product_url: https://files.cpicpgx.org/resources/CPIC-overview-updates-02.2025.pptx
- category: DocumentationProduct
  description: One-page summary document providing concise overview of CPIC mission
    and guideline process (DOCX)
  format: docx
  id: cpic.onepager
  name: CPIC One-Page Summary
  original_source:
  - cpic
  product_file_size: 160131
  product_url: https://cpicpgx.org/wp-content/uploads/2025/07/CPIC-One-Page-CLEAN.docx
- category: DocumentationProduct
  description: Term standardization project resources for clinical pharmacogenetic
    test result terminology
  id: cpic.term_standardization
  name: CPIC Term Standardization Project
  original_source:
  - cpic
  product_url: https://cpicpgx.org/resources/term-standardization
- category: DocumentationProduct
  description: CYP2D6 genotype to phenotype translation project resources
  id: cpic.cyp2d6_translation
  name: CPIC CYP2D6 Genotype to Phenotype Project
  original_source:
  - cpic
  product_url: https://cpicpgx.org/resources/cyp2d6-genotype-to-phenotype-standardization-project/
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - epigraphdb
  - kg-monarch
  - vectology
  - ukbiobank
  - prsatlas
  - eqtlgen
  - mondo
  - gtex
  - ensembl
  - cpic
  - opentargets
  - efo
  - semmeddb
  - intact
  - string
  - reactome
  - mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
  secondary_source:
  - epigraphdb
taxon:
- NCBITaxon:9606
---
## Overview

The Clinical Pharmacogenetics Implementation Consortium (CPIC) facilitates the integration of pharmacogenetic test results into routine clinical care. CPIC develops and maintains evidence-based guidelines that translate patient genotype (or predicted phenotype) into prescribing recommendations, removing implementation barriers and standardizing clinical decision support for pharmacogenomics (PGx).

## Key Components

- Peer-reviewed clinical practice guidelines with standardized evidence grading
- Genes–drugs, alleles, and diplotype function tables
- Structured database and API for programmatic access to curated PGx relationships
- Standard operating procedures and terminology standardization initiatives
- Educational materials: overview slides, one-pager, videos, and implementation resources
- Community engagement via announcements, working groups, and discussion lists

## Licensing

CPIC resources are freely available under a Creative Commons public domain license (see licensing page). Users must ensure clinical application is accompanied by professional review; resources are not a substitute for medical judgment.

## Citation (example guideline reference format)

Caudle KE, Klein TE, Whirl-Carrillo M, et al. (CPIC® guideline citation – see specific guideline publication). Clinical Pharmacology & Therapeutics. (Refer to https://cpicpgx.org/publications/ for full list.)

## Contact

General inquiries: contact@cpicpgx.org. Additional forms and subscription options are available on the contact page for allele function questions, announcements, and discussion list enrollment.