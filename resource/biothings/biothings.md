---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://biothings.io/
  label: BioThings
creation_date: '2026-06-02T00:00:00Z'
description: BioThings is an ecosystem and Python SDK for building high-performance
  biomedical annotation APIs from one or more data sources.
domains:
- biomedical
- information technology
homepage_url: https://biothings.io/
id: biothings
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/Apache-2.0
  label: Apache-2.0
name: BioThings
products:
- category: GraphicalInterface
  description: BioThings homepage describing the BioThings API ecosystem, major public
    APIs, SDK, Studio, and related community resources.
  format: http
  id: biothings.portal
  name: BioThings Homepage
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biothings
  product_url: https://biothings.io/
- category: Product
  description: Python-based BioThings SDK for aggregating biomedical annotations and
    exposing them as high-performance APIs.
  id: biothings.sdk
  name: BioThings SDK
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biothings
  product_url: https://docs.biothings.io/
  repository: https://github.com/biothings/biothings.api
- category: DocumentationProduct
  description: BioThings API specifications describing common endpoints, versioning,
    HTTP methods, formats, and shared request parameters for BioThings APIs.
  format: http
  id: biothings.api-specs
  name: BioThings API Specifications
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biothings
  product_url: https://biothings.io/specs/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-01: HTTP 204 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 204 error
    when accessing file'
- category: ProgrammingInterface
  connection_url: https://biothings.ncats.io/gtrx/query
  description: BioThings API for querying Genome-to-Treatment association records
    through `/query`, `/metadata`, and related BioThings endpoints
  format: json
  id: gtrx.api
  infores_id: biothings-gtrx
  is_public: true
  latest_version: '2022-02-01'
  name: gTRx API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrx
  product_url: https://biothings.ncats.io/gtrx
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biothings
publications:
- authors:
  - Sebastien Lelong
  - Xinghua Zhou
  - Cyrus Afrasiabi
  - Zhongchao Qian
  - Chunlei Wu
  doi: 10.1093/bioinformatics/btac017
  id: doi:10.1093/bioinformatics/btac017
  journal: Bioinformatics
  preferred: true
  title: 'BioThings SDK: a toolkit for building high-performance data APIs in biomedical
    research'
  year: '2022'
repository: https://github.com/biothings/biothings.api
---
# BioThings

BioThings provides a reusable SDK and API conventions for turning biomedical data
sources into scalable annotation web services. Public BioThings APIs include
services for genes, variants, chemicals, diseases, taxa, and Translator knowledge
providers built with the same framework.