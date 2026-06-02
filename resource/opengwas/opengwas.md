---
activity_status: active
category: DataSource
creation_date: '2026-06-02T00:00:00Z'
description: Stub Resource page for opengwas. This page was automatically generated
  because it was referenced by other resources.
domains:
- stub
id: opengwas
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Opengwas
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
- category: ProgrammingInterface
  description: TwoSampleMR R package supporting data extraction, harmonization, instrument
    selection, MR analysis methods, diagnostics, and reproducible code generation
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
warnings:
- This is an automatically generated stub page. Please replace with accurate information
  about this resource.
---
# Opengwas

This is an automatically generated stub page for opengwas. Please update with proper information.