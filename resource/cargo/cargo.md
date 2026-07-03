---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://crates.io/policies
  label: Rust Foundation
creation_date: '2026-07-03T00:00:00Z'
description: crates.io is the official package registry for the Rust ecosystem, hosting
  metadata and distributable artifacts (crates) for Rust libraries.
domains:
- information technology
homepage_url: https://crates.io/
id: cargo
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: crates.io (Cargo)
products:
- category: GraphicalInterface
  description: Web interface and public registry for browsing and retrieving Rust
    crates
  format: http
  id: cargo.website
  name: crates.io website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cargo
  product_url: https://crates.io/
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
## crates.io (Cargo)

crates.io is the official package registry for the Rust ecosystem, hosting crate
metadata, version histories, and distributable artifacts consumed by the Cargo
package manager. Software-supply-chain knowledge graphs use crates.io as an
upstream source of Rust package identity, versions, and declared dependencies.