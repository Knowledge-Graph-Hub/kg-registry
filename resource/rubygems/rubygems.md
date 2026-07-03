---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://rubygems.org/pages/contact
  label: Ruby Central
creation_date: '2026-07-03T00:00:00Z'
description: RubyGems.org is the community package registry for the Ruby ecosystem,
  hosting metadata and distributable artifacts (gems) for Ruby libraries.
domains:
- information technology
homepage_url: https://rubygems.org/
id: rubygems
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: RubyGems.org
products:
- category: GraphicalInterface
  description: Web interface and public registry for browsing and retrieving Ruby
    gems
  format: http
  id: rubygems.website
  name: RubyGems.org website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rubygems
  product_url: https://rubygems.org/
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
## RubyGems.org

RubyGems.org is the public package registry for the Ruby ecosystem, hosting gem
metadata, version histories, and distributable artifacts. Software-supply-chain
knowledge graphs use RubyGems.org as an upstream source of Ruby package identity,
versions, and declared dependencies.