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
last_modified_date: '2026-09-16T00:00:00Z'
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
  format: python
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
  - 'File was not able to be retrieved when checked on 2026-10-04: HTTP 204 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-10-05: HTTP 204 error
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
- category: GraphicalInterface
  description: SmartAPI Translator portal for browsing registered Translator APIs.
  format: http
  id: service-kp.portal
  name: Service KP SmartAPI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://smart-api.info/portal/translator
- category: ProcessProduct
  description: BioThings API stack source repository used by the Service Provider
    team.
  format: http
  id: service-kp.code
  name: Service KP Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  product_url: https://github.com/biothings/biothings.api
- category: ProgrammingInterface
  description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
    querying the BioThings and other APIs registered to the team in SmartAPI.
  format: http
  id: service-kp.trapi
  is_public: true
  name: Service Provider TRAPI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: litvar
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: ddinter
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gtrx
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
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