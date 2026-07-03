---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.npmjs.com/support
  label: npm, Inc. (GitHub)
creation_date: '2026-07-03T00:00:00Z'
description: The npm registry (Node Package Manager) is the public package registry
  for the JavaScript and Node.js ecosystem, hosting metadata and distributable artifacts
  for millions of open-source packages.
domains:
- information technology
homepage_url: https://www.npmjs.com/
id: npm
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: npm registry
products:
- category: GraphicalInterface
  description: Web interface and public registry for browsing and retrieving npm packages
  format: http
  id: npm.website
  name: npm registry website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npm
  product_url: https://www.npmjs.com/
- category: GraphProduct
  description: SecureChain knowledge graph of software supply-chain components, versions,
    dependencies, and vulnerabilities, served as RDF/Turtle via the project's SPARQL
    and Triple Pattern Fragments endpoints.
  format: ttl
  id: securechainkg.graph
  name: SecureChain KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: securechainkg
  - relation_type: prov:hadPrimarySource
    source: npm
  - relation_type: prov:hadPrimarySource
    source: pypi
  - relation_type: prov:hadPrimarySource
    source: maven-central
  - relation_type: prov:hadPrimarySource
    source: nuget
  - relation_type: prov:hadPrimarySource
    source: rubygems
  - relation_type: prov:hadPrimarySource
    source: cargo
  - relation_type: prov:hadPrimarySource
    source: osv
  product_url: https://purdue-hcss.github.io/nsf-software-supply-chain_security/
---
## npm registry

The npm registry is the default public package registry for the JavaScript and
Node.js ecosystem. It hosts package metadata, version histories, and distributable
artifacts for a large body of open-source software. Software-supply-chain knowledge
graphs use the npm registry as an upstream source of package identity, versions, and
dependency manifests.