---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nuget.org/policies/Contact
  label: Microsoft / .NET Foundation
creation_date: '2026-07-03T00:00:00Z'
description: NuGet is the package registry for the .NET ecosystem, hosting metadata
  and distributable artifacts for .NET libraries and tools.
domains:
- information technology
homepage_url: https://www.nuget.org/
id: nuget
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: NuGet Gallery
products:
- category: GraphicalInterface
  description: Web interface and public registry for browsing and retrieving .NET
    packages
  format: http
  id: nuget.website
  name: NuGet Gallery website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nuget
  product_url: https://www.nuget.org/
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
## NuGet Gallery

NuGet is the public package registry for the .NET ecosystem, hosting package
metadata, version histories, and distributable artifacts. Software-supply-chain
knowledge graphs use NuGet as an upstream source of .NET package identity,
versions, and declared dependencies.