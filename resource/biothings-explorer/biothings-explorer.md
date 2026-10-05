---
activity_status: active
category: Aggregator
collection:
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cwu@scripps.edu
  - contact_type: github
    value: newgene
  label: Chunlei Wu
- category: Organization
  contact_details:
  - contact_type: url
    value: https://biothings.io/
  label: Su and Wu Labs, Scripps Research
creation_date: '2026-10-04T00:00:00Z'
description: BioThings Explorer (BTE) is a query engine for a federated knowledge
  graph of biomedical APIs, developed by the Su and Wu labs at Scripps Research. It
  plans and runs multi-hop queries across APIs annotated in the SmartAPI registry
  with the x-bte extension, as well as TRAPI knowledge providers, and returns ranked
  results through the Translator Reasoner API (TRAPI). BTE is an Autonomous Relay
  Agent (ARA) in the NCATS Biomedical Data Translator and also serves team endpoints
  such as the Service Provider TRAPI endpoint.
domains:
- biomedical
- information technology
homepage_url: https://explorer.biothings.io/
id: biothings-explorer
infores_id: biothings-explorer
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/Apache-2.0
  label: Apache-2.0
name: BioThings Explorer
products:
- category: ProgrammingInterface
  description: Production TRAPI 1.5 endpoint of BioThings Explorer for federated multi-hop
    queries over SmartAPI-registered biomedical APIs, with synchronous, asynchronous
    and pathfinder query support.
  format: http
  id: biothings-explorer.trapi
  is_public: true
  name: BioThings Explorer TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biothings-explorer
  - relation_type: prov:wasInformedBy
    source: service-kp
  product_url: https://bte.transltr.io/v1
- category: Product
  description: Meta knowledge graph of the subject category, predicate and object
    category combinations BTE can answer, as JSON (49 node categories and 3014 edge
    types when checked on 2026-10-04).
  format: json
  id: biothings-explorer.meta-kg
  name: BioThings Explorer Meta Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biothings-explorer
  product_url: https://bte.transltr.io/v1/meta_knowledge_graph
- category: GraphicalInterface
  description: BioThings Explorer website with an overview of the query engine and
    links to its endpoints.
  format: http
  id: biothings-explorer.portal
  name: BioThings Explorer Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biothings-explorer
  product_url: https://explorer.biothings.io/
- category: ProcessProduct
  description: Source code workspace for the TRAPI implementation of BioThings Explorer,
    written in TypeScript and JavaScript.
  format: mixed
  id: biothings-explorer.code
  license:
    id: https://opensource.org/licenses/Apache-2.0
    label: Apache-2.0
  name: BioThings Explorer Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biothings-explorer
  product_url: https://github.com/biothings/biothings_explorer
- category: DocumentationProduct
  description: Documentation of the x-bte extension to the OpenAPI specification,
    which annotates SmartAPI registry entries so that BTE can call them.
  format: http
  id: biothings-explorer.x-bte-docs
  name: x-bte Extension Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biothings-explorer
  product_url: https://x-bte-extension.readthedocs.io/en/latest/index.html
- category: GraphicalInterface
  description: JSON index of the ARS production relay server and its registered agent
    endpoints.
  format: http
  id: ars.portal
  name: ARS Production Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ars
  - relation_type: prov:wasInformedBy
    source: aragorn
  - relation_type: prov:wasInformedBy
    source: arax
  - relation_type: prov:wasInformedBy
    source: cqs
  - relation_type: prov:wasInformedBy
    source: molepro
  - relation_type: prov:wasInformedBy
    source: cam-kp
  - relation_type: prov:wasInformedBy
    source: openpredict
  - relation_type: prov:wasInformedBy
    source: cohd
  - relation_type: prov:wasInformedBy
    source: icees-kg
  - relation_type: prov:wasInformedBy
    source: genetics-kp
  - relation_type: prov:wasInformedBy
    source: connections-hypothesis-kp
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  product_url: https://ars-prod.transltr.io/
- category: ProgrammingInterface
  connection_url: https://ars-prod.transltr.io/ars/api
  description: TRAPI-compatible ARS endpoint for asynchronous query submission.
  format: http
  id: ars.api
  is_public: true
  name: ARS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ars
  - relation_type: prov:wasInformedBy
    source: aragorn
  - relation_type: prov:wasInformedBy
    source: arax
  - relation_type: prov:wasInformedBy
    source: cqs
  - relation_type: prov:wasInformedBy
    source: molepro
  - relation_type: prov:wasInformedBy
    source: cam-kp
  - relation_type: prov:wasInformedBy
    source: openpredict
  - relation_type: prov:wasInformedBy
    source: cohd
  - relation_type: prov:wasInformedBy
    source: icees-kg
  - relation_type: prov:wasInformedBy
    source: genetics-kp
  - relation_type: prov:wasInformedBy
    source: connections-hypothesis-kp
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  product_url: https://ars-prod.transltr.io/ars/api/
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
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: mychem
  - relation_type: prov:hadPrimarySource
    source: mydisease
  - relation_type: prov:hadPrimarySource
    source: fooddata-central
  - relation_type: prov:hadPrimarySource
    source: myvariant
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
- category: ProgrammingInterface
  description: TRAPI query endpoint for the BioThings Explorer (BTE) ARA implementation
    within Shepherd (/query and /asyncquery), over knowledge from Retriever.
  format: http
  id: shepherd.bte.api
  infores_id: shepherd-bte
  name: Shepherd BTE TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  - relation_type: prov:wasInfluencedBy
    source: biothings-explorer
  - relation_type: prov:wasDerivedFrom
    source: retriever
  product_url: https://shepherd.transltr.io/bte/docs
publications:
- authors:
  - Jackson Callaghan
  - Colleen H Xu
  - Jiwen Xin
  - Marco Alvarado Cano
  - Anders Riutta
  - Eric Zhou
  - Rohan Juneja
  - Yao Yao
  - Madhumita Narayan
  - Kristina Hanspers
  - Ayushi Agrawal
  - Alexander R Pico
  - Chunlei Wu
  - Andrew I Su
  doi: 10.1093/bioinformatics/btad570
  id: doi:10.1093/bioinformatics/btad570
  journal: Bioinformatics
  preferred: true
  title: 'BioThings Explorer: a query engine for a federated knowledge graph of biomedical
    APIs'
  year: '2023'
repository: https://github.com/biothings/biothings_explorer
synonyms:
- BTE
- BioThings Explorer TRAPI
---
# BioThings Explorer

BioThings Explorer (BTE) is a query engine that treats a collection of biomedical web APIs as one federated knowledge graph. Each API is described in the [SmartAPI registry](https://smart-api.info/) with semantically precise inputs and outputs using the x-bte extension to OpenAPI. BTE combines these descriptions into a meta knowledge graph, then plans each query as a series of API calls, merges the records and scores the results.

BTE is an Autonomous Relay Agent (ARA) in the NCATS Biomedical Data Translator. It is registered with the Translator Autonomous Relay System as `ara-bte` and answers queries in the Translator Reasoner API (TRAPI) format. It also hosts team TRAPI endpoints, such as the Service Provider endpoint (`/v1/team/Service Provider`), which exposes the BioThings APIs of the Service Provider KP.

## Endpoints

- Production TRAPI: https://bte.transltr.io/v1 (TRAPI 1.5, version 3.0.0 in SmartAPI)
- SmartAPI also lists testing (`bte.test.transltr.io`) and staging (`bte.ci.transltr.io`) servers. Neither responded when checked on 2026-10-04.

An earlier Python implementation of BTE is archived at https://github.com/biothings/biothings_explorer_archived.