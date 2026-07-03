---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://pypi.org/
  label: Python Software Foundation
creation_date: '2026-07-03T00:00:00Z'
description: The Python Package Index (PyPI) is the official third-party software
  repository for the Python programming language, hosting metadata and distributable
  artifacts for Python packages.
domains:
- information technology
homepage_url: https://pypi.org/
id: pypi
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: Python Package Index (PyPI)
products:
- category: GraphicalInterface
  description: Web interface and public registry for browsing and retrieving Python
    packages
  format: http
  id: pypi.website
  name: PyPI website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pypi
  product_url: https://pypi.org/
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
## Python Package Index (PyPI)

The Python Package Index (PyPI) is the official repository for Python packages,
hosting package metadata, version histories, and distributable artifacts.
Software-supply-chain knowledge graphs use PyPI as an upstream source of Python
package identity, versions, and dependency requirements.