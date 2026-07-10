---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: tianyi@purdue.edu
  label: Tianyi Zhang
description: SecureChain is a knowledge graph for resilient, trustworthy, and secure
  software supply chains.
domains:
- information technology
homepage_url: https://purdue-hcss.github.io/nsf-software-supply-chain_security/
id: securechainkg
layout: resource_detail
license:
  id: https://opensource.org/licenses/Apache-2.0
  label: Apache-2.0
name: SecureChain KG
repository: https://github.com/purdue-hcss/SecureChain
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for SecureChain KG
  format: http
  id: securechainkg.sparql
  name: SecureChain KG SPARQL
  original_source:
  - source: securechainkg
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/securechainkg/sparql
- id: securechainkg.tpf
  name: SecureChain KG TPF
  description: Triple Pattern Fragments endpoint for SecureChain KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/securechainkg
  original_source:
  - source: securechainkg
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: SecureChain knowledge graph of software supply-chain components,
    versions, dependencies, and vulnerabilities, served as RDF/Turtle via the
    project's SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: securechainkg.graph
  name: SecureChain KG Graph
  product_url: https://purdue-hcss.github.io/nsf-software-supply-chain_security/
  original_source:
  - source: securechainkg
    relation_type: prov:hadPrimarySource
  - source: npm
    relation_type: prov:hadPrimarySource
  - source: pypi
    relation_type: prov:hadPrimarySource
  - source: maven-central
    relation_type: prov:hadPrimarySource
  - source: nuget
    relation_type: prov:hadPrimarySource
  - source: rubygems
    relation_type: prov:hadPrimarySource
  - source: cargo
    relation_type: prov:hadPrimarySource
  - source: osv
    relation_type: prov:hadPrimarySource
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-03T00:00:00Z'
---
SecureChain KG

## Automated Evaluation

- View the automated evaluation: [securechainkg automated evaluation](securechainkg_eval_automated.html)
