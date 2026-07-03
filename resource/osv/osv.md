---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://osv.dev/
  label: Google Open Source Security Team
creation_date: '2026-07-03T00:00:00Z'
description: OSV (Open Source Vulnerabilities) is an open, distributed vulnerability
  database and API providing standardized information about known vulnerabilities
  in open-source software, including affected version ranges and fix metadata.
domains:
- information technology
homepage_url: https://osv.dev/
id: osv
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: OSV (Open Source Vulnerabilities)
products:
- category: GraphicalInterface
  description: Web interface and API for the OSV open-source vulnerability database
  format: http
  id: osv.website
  name: OSV website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: osv
  product_url: https://osv.dev/
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
## OSV (Open Source Vulnerabilities)

OSV is an open, distributed vulnerability database for open-source software. It
provides standardized, machine-readable records describing known vulnerabilities,
the package versions they affect, and fix metadata, served through a public API and
web interface. Software-supply-chain knowledge graphs use OSV as an upstream source
of vulnerability data linking packages and versions to known security issues.