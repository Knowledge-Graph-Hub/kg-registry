---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.bristol.ac.uk/integrative-epidemiology/
  label: MRC Integrative Epidemiology Unit, University of Bristol
creation_date: '2026-06-02T00:00:00Z'
description: IEU OpenGWAS is a database and analytical platform that aggregates, curates,
  queries, and serves genome-wide association study summary datasets for Mendelian
  randomization, PheWAS, fine mapping, colocalisation, and related analyses.
domains:
- genomics
- biomedical
- precision medicine
homepage_url: https://opengwas.io/
id: opengwas
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: IEU OpenGWAS
products:
- category: GraphicalInterface
  description: IEU OpenGWAS browser for exploring the harmonized GWAS dataset catalog
    now used by MR-Base-related tooling
  format: http
  id: opengwas.portal
  is_public: true
  name: IEU OpenGWAS Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opengwas
  product_url: https://opengwas.io/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: mrbase
- category: ProgrammingInterface
  description: REST API for programmatic access to IEU OpenGWAS study information,
    top hits, association records, LD proxies, and related MR-Base analysis inputs
  format: http
  id: opengwas.api
  is_public: true
  name: IEU OpenGWAS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opengwas
  product_url: https://api.opengwas.io/api/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: mrbase
- category: Product
  description: OpenGWAS GWAS summary dataset catalog and downloadable files for curated
    genome-wide association studies.
  format: mixed
  id: opengwas.datasets
  name: IEU OpenGWAS Dataset Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: opengwas
  product_url: https://opengwas.io/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: mrbase
- category: ProgrammingInterface
  description: TwoSampleMR R package supporting data extraction, harmonization, instrument
    selection, MR analysis methods, diagnostics, and reproducible code generation
  format: http
  id: mrbase.twosamplemr
  is_public: true
  name: TwoSampleMR R Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://github.com/MRCIEU/TwoSampleMR
  secondary_source:
  - relation_type: prov:used
    source: opengwas
- category: DocumentationProduct
  description: TwoSampleMR package documentation with function reference, usage guides,
    and methodological notes
  format: http
  id: mrbase.twosamplemr.docs
  name: TwoSampleMR Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://mrcieu.github.io/TwoSampleMR/
  secondary_source:
  - relation_type: prov:used
    source: opengwas
- category: GraphicalInterface
  description: Two-sample Mendelian randomization analysis tooling for curated GWAS
    summary datasets, provided through the TwoSampleMR R package and its documentation
    site (successor to the retired MR-Base Shiny web application)
  format: http
  id: mrbase.webapp
  is_public: true
  name: MR-Base Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://mrcieu.github.io/TwoSampleMR/
  secondary_source:
  - relation_type: prov:used
    source: opengwas
  warnings:
  - The legacy MR-Base Shiny web application at app.mrbase.org was unreachable (no
    response) when checked on 2026-06-23 and has been retired; two-sample MR analysis
    is now performed via the TwoSampleMR R package against the OpenGWAS database.
- category: ProgrammingInterface
  description: Phenome-wide association study (PheWAS) functionality enabling exploration
    of SNP-trait associations across the OpenGWAS database, now delivered through
    the OpenGWAS API PheWAS endpoint (successor to the retired MR-Base PheWAS web
    interface)
  format: http
  id: mrbase.phewas
  is_public: true
  name: MR-Base PheWAS Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://api.opengwas.io/api/
  secondary_source:
  - relation_type: prov:used
    source: opengwas
  warnings:
  - The legacy MR-Base PheWAS web interface at gwas.mrcieu.ac.uk/phewas/ returned
    HTTP 404 when checked on 2026-06-23 and has been retired; PheWAS is now available
    as an endpoint of the OpenGWAS API.
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to harmonized GWAS summary
    statistics, LD proxy lookup, instruments, and MR result generation, now served
    by the OpenGWAS API (successor to the retired api.mrbase.org endpoint)
  format: http
  id: mrbase.api
  is_public: true
  name: MR-Base REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://api.opengwas.io/
  secondary_source:
  - relation_type: prov:used
    source: opengwas
publications:
- authors:
  - Ben Elsworth
  - Tom R Gaunt
  - Gibran Hemani
  doi: 10.1101/2020.08.10.244293
  id: doi:10.1101/2020.08.10.244293
  journal: bioRxiv
  preferred: true
  title: The MRC IEU OpenGWAS data infrastructure
  year: '2020'
repository: https://github.com/MRCIEU/opengwas-api
synonyms:
- OpenGWAS
- MRC IEU OpenGWAS
taxon:
- NCBITaxon:9606
---
# IEU OpenGWAS

IEU OpenGWAS provides a curated database of GWAS summary datasets with browser,
download, and API access. It supersedes and extends MR-Base data access for
Mendelian randomization and related genetic epidemiology analyses.