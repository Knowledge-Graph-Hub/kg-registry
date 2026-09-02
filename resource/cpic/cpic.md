---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.clinpgx.org/cpic#contact
  - contact_type: email
    value: contact@cpicpgx.org
  label: Clinical Pharmacogenetics Implementation Consortium (CPIC)
creation_date: '2025-09-03T00:00:00Z'
description: The Clinical Pharmacogenetics Implementation Consortium (CPIC) creates,
  curates, and disseminates freely available, peer-reviewed, evidence-based, and updatable
  clinical practice guidelines that translate patient pharmacogenetic test results
  into actionable prescribing decisions. CPIC also publishes structured gene-drug
  annotations, allele function data, standardized terminology resources, and implementation
  tools (database, API, SOPs, educational materials). Since 2025-07-30 CPIC content
  is hosted within ClinPGx (registry id clinpgx) and cpicpgx.org pages redirect there;
  the CPIC name and guidelines continue under ClinPGx.
domains:
- biomedical
- clinical
- drug discovery
homepage_url: https://www.clinpgx.org/cpic
id: cpic
last_modified_date: '2026-09-02T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_url: https://www.clinpgx.org/cpic
- category: DocumentationProduct
  description: Peer-reviewed, evidence-based, updatable pharmacogenetic clinical practice
    guidelines translating genotype into prescribing recommendations
  format: http
  id: cpic.guidelines
  is_public: true
  name: CPIC Clinical Practice Guidelines
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_url: https://www.clinpgx.org/cpic/guidelines
- category: Product
  description: "Curated gene\u2013drug pair tables linking pharmacogenes with affected\
    \ medications and guideline recommendations"
  format: http
  id: cpic.genes_drugs
  is_public: true
  name: CPIC Genes-Drugs Tables
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_url: https://www.clinpgx.org/cpic/pairs
- category: Product
  description: Allele function and diplotype-to-phenotype tables standardized for
    clinical pharmacogenetic test result interpretation
  format: http
  id: cpic.alleles
  is_public: true
  name: CPIC Allele & Diplotype Function Tables
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_url: https://www.clinpgx.org/page/cpicResources#guideline-alleles
- category: ProgrammingInterface
  connection_url: https://api.cpicpgx.org/
  description: "Structured data (database and API) for CPIC guideline-derived gene\u2013\
    drug relationships, allele function, and standardized terms"
  format: json
  id: cpic.api
  is_public: true
  name: CPIC Database & API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_url: https://www.clinpgx.org/page/cpicResources#database-and-api
- category: DocumentationProduct
  description: Standard operating procedure PDF for assigning allele function and
    translating diplotypes to phenotypes
  format: pdf
  id: cpic.sop
  name: CPIC Pharmacogene Curation SOP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_file_size: 812796
  product_url: https://github.com/cpicpgx/cpic-sop/raw/main/CPIC%20Pharmacogene%20Curation%20SOP.pdf
- category: DocumentationProduct
  description: Overview slide deck describing CPIC assumptions, development process,
    and implementation guidance (PowerPoint)
  format: http
  id: cpic.overview.slides
  name: CPIC Overview Presentation Slides
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_file_size: 8552272
  product_url: https://files.cpicpgx.org/resources/CPIC-overview-updates-02.2025.pptx
- category: DocumentationProduct
  description: One-page summary document providing concise overview of CPIC mission
    and guideline process (DOCX)
  format: docx
  id: cpic.onepager
  name: CPIC One-Page Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_file_size: 160131
  product_url: https://cpicpgx.org/wp-content/uploads/2025/07/CPIC-One-Page-CLEAN.docx
- category: DocumentationProduct
  description: Term standardization project resources for clinical pharmacogenetic
    test result terminology
  format: http
  id: cpic.term_standardization
  name: CPIC Term Standardization Project
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_url: https://www.clinpgx.org/page/cpicTermStandardization
- category: DocumentationProduct
  description: CYP2D6 genotype to phenotype translation project resources
  format: http
  id: cpic.cyp2d6_translation
  name: CPIC CYP2D6 Genotype to Phenotype Project
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpic
  product_url: https://www.clinpgx.org/page/cpicCyp2d6Standardization
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epigraphdb
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: vectology
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  - relation_type: prov:hadPrimarySource
    source: eqtlgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: cpic
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
- category: GraphicalInterface
  description: ClinPGx web portal for browsing genes, variants, drugs, clinical annotations,
    drug labels, pathways and CPIC guidelines, integrating PharmGKB and CPIC content
  id: clinpgx.portal
  is_public: true
  name: ClinPGx Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinpgx
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: cpic
  product_url: https://www.clinpgx.org/
repository: https://github.com/cpicpgx/cpic-data
taxon:
- NCBITaxon:9606
---
## Overview

Since 2025-07-30 CPIC is delivered through [ClinPGx](clinpgx), which unifies PharmGKB,
CPIC and PharmCAT. The standalone cpicpgx.org site redirects into the CPIC section of
ClinPGx and is stated to be retiring. Product URLs on this page were repointed to their
ClinPGx targets on 2026-09-02, following the redirects the CPIC site issues. Three files
remain on CPIC hosts with no redirect and no known ClinPGx copy: the API at
api.cpicpgx.org, the overview slides on files.cpicpgx.org and the one-pager under
cpicpgx.org/wp-content. They answered normally on 2026-09-02 and will need repointing
when those hosts retire.

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

General inquiries: contact@cpicpgx.org (not re-verified since the ClinPGx move; feedback@clinpgx.org is the ClinPGx address). Additional forms and subscription options are available on the ClinPGx CPIC contact section for allele function questions, announcements, and discussion list enrollment.