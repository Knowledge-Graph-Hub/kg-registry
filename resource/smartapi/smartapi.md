---
activity_status: active
category: Aggregator
collection:
- translator
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: SmartAPI
  label: Su and Wu labs, Scripps Research
- category: Individual
  contact_details:
  - contact_type: email
    value: cwu@scripps.edu
  - contact_type: github
    value: newgene
  label: Chunlei Wu
creation_date: '2026-10-04T00:00:00Z'
description: SmartAPI is a registry of OpenAPI descriptions for biomedical web APIs,
  extended with semantic annotations of inputs and outputs. It hosts the x-translator
  and x-bte extensions used by the NCATS Biomedical Data Translator, and builds a
  Translator meta knowledge graph of the subject-predicate-object relations that registered
  APIs can answer, which BioThings Explorer uses to plan federated queries. It is
  developed by the Su and Wu labs at Scripps Research.
domains:
- biomedical
- information technology
- metadata
homepage_url: https://smart-api.info/
id: smartapi
infores_id: smart-api
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: SmartAPI
products:
- category: GraphicalInterface
  description: SmartAPI registry web portal for searching and browsing registered
    API metadata, with an interactive documentation page for each API.
  format: http
  id: smartapi.portal
  name: SmartAPI Registry Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://smart-api.info/registry
- category: GraphicalInterface
  description: SmartAPI Translator portal for browsing APIs registered with the NCATS
    Translator extensions and exploring the Translator meta knowledge graph.
  format: http
  id: smartapi.translator-portal
  name: SmartAPI Translator Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://smart-api.info/portal/translator
- category: ProgrammingInterface
  description: REST API returning registered SmartAPI metadata, with query, metadata
    retrieval and registration endpoints.
  format: http
  id: smartapi.api
  is_public: true
  name: SmartAPI Registry API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://smart-api.info/api
- category: ProgrammingInterface
  description: API endpoint returning the Translator meta knowledge graph, a set of
    subject-predicate-object edges (Biolink Model categories and predicates) built
    from the x-bte and TRAPI metadata of registered APIs, each linked to the APIs
    that provide it.
  format: http
  id: smartapi.metakg
  is_public: true
  name: SmartAPI Translator Meta Knowledge Graph API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://smart-api.info/api/metakg
- category: DocumentationProduct
  description: Interactive OpenAPI documentation for the SmartAPI registry API itself.
  format: http
  id: smartapi.api-docs
  name: SmartAPI API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://smart-api.info/ui/27a5b60716c3a401f2c021a5b718c5b1
- category: DocumentationProduct
  description: SmartAPI user guide covering how to write, annotate, validate and register
    SmartAPI metadata, including the Translator extensions.
  format: http
  id: smartapi.docs
  name: SmartAPI Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://smart-api.info/guide
- category: ProcessProduct
  description: Source code for the SmartAPI registry web application and API.
  format: http
  id: smartapi.code
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: SmartAPI Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://github.com/SmartAPI/smartAPI
- category: Product
  description: GitHub repository where API providers can host the SmartAPI metadata
    YAML files that they register in SmartAPI.
  format: http
  id: smartapi.metadata-repository
  license:
    id: https://opensource.org/licenses/Apache-2.0
    label: Apache-2.0
  name: SmartAPI Metadata Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: smartapi
  product_url: https://github.com/SmartAPI/smartapi_registry
- category: GraphProduct
  description: Bayesian-network knowledge graph served by the Connections Hypothesis
    Provider over the Translator TRAPI interface. Inference is computed over a breast
    cancer dataset from The Cancer Genome Atlas (TCGA), supporting queries relating
    genetic, therapeutic, and patient clinical features to patient survival.
  format: http
  id: connections-hypothesis-kp.graph
  name: Connections Hypothesis KP Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: connections-hypothesis-kp
  - relation_type: prov:hadPrimarySource
    source: tcga
  - relation_type: prov:wasInfluencedBy
    source: smartapi
  product_url: https://smart-api.info/registry?q=412af63e15b73e5a30778aac84ce313f
- category: DocumentationProduct
  description: SmartAPI registry listing for CHP service metadata and interface documentation.
  format: http
  id: connections-hypothesis-kp.smartapi
  name: Connections Hypothesis KP SmartAPI Entry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: connections-hypothesis-kp
  - relation_type: prov:wasInfluencedBy
    source: smartapi
  product_url: https://smart-api.info/registry?q=412af63e15b73e5a30778aac84ce313f
- category: DocumentationProduct
  description: SmartAPI registry entry for the Multiomics Clinical Trials KP TRAPI
    1.5 endpoint.
  format: http
  id: ctkp.smartapi
  name: Clinical Trials KP SmartAPI Registration
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:wasInfluencedBy
    source: smartapi
  product_url: https://smart-api.info/registry?q=e51073371d7049b9643e1edbdd61bcbd
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
- category: ProgrammingInterface
  description: REST API with endpoints that abstract common types of queries against
    a UBKG neo4j knowledge graph database. Requires UMLS API key to access.
  format: http
  id: ubkg.api
  is_public: false
  name: UBKG API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:wasInfluencedBy
    source: smartapi
  product_url: https://smart-api.info/ui/96e5b5c0b0efeef5b93ea98ac2794837
publications:
- authors:
  - Amrapali Zaveri
  - Shima Dastgheib
  - Chunlei Wu
  - Trish Whetzel
  - Ruben Verborgh
  - Paul Avillach
  - Gabor Korodi
  - Raymond Terryn
  - Kathleen Jagodnik
  - Pedro Assis
  - Michel Dumontier
  doi: 10.1007/978-3-319-58451-5_11
  id: doi:10.1007/978-3-319-58451-5_11
  journal: Lecture Notes in Computer Science
  preferred: true
  title: 'smartAPI: Towards a More Intelligent Network of Web APIs'
  year: '2017'
repository: https://github.com/SmartAPI/smartAPI
synonyms:
- smartAPI
- SmartAPI registry
---
# SmartAPI

SmartAPI is a registry of OpenAPI descriptions for web APIs, mostly in biomedicine, that adds semantic annotations to API metadata so that APIs can be found and chained by the data types they take and return. It was introduced at ESWC 2017 (Zaveri et al., *The Semantic Web*, Lecture Notes in Computer Science) and is developed by the Su and Wu labs at Scripps Research. When checked on 2026-10-04 the registry held 271 API entries.

## Translator

The NCATS Biomedical Data Translator uses SmartAPI as its service registry. Translator knowledge providers and ARAs register their APIs with the `x-translator` extension, and BioThings-style APIs add `x-bte` annotations mapping operations to Biolink Model categories and predicates. From these, SmartAPI builds a Translator meta knowledge graph (about 24,000 edges on 2026-10-04), served at https://smart-api.info/api/metakg, which BioThings Explorer uses to plan federated queries.

## Software

The registry application is open source under the MIT license at https://github.com/SmartAPI/smartAPI. A separate repository, https://github.com/SmartAPI/smartapi_registry (Apache-2.0), hosts metadata files for providers who do not keep them elsewhere.