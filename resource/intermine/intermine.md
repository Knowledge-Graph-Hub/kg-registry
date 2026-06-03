---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://intermine.org/
    label: InterMine
creation_date: '2026-06-02T00:00:00Z'
description: InterMine is an open-source biological data warehouse system for integrating heterogeneous biological data sources and exposing them through customizable web interfaces, query templates, and RESTful web-service APIs.
domains:
  - biomedical
  - genomics
  - information technology
homepage_url: https://intermine.org/
id: intermine
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
  label: LGPL-2.1
name: InterMine
products:
  - category: DocumentationProduct
    description: InterMine server documentation describing the biological data warehouse system, BlueGenes interface, data integration model, and web-service API.
    id: intermine.documentation
    name: InterMine Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: intermine
    product_url: https://intermine.org/im-docs/docs/introduction/index
  - category: Product
    description: Open-source InterMine codebase for building biological data warehouses and deploying InterMine instances.
    id: intermine.software
    name: InterMine Software
    original_source:
      - relation_type: prov:hadPrimarySource
        source: intermine
    product_url: https://github.com/intermine/intermine
    repository: https://github.com/intermine/intermine
  - category: GraphicalInterface
    description: Public InterMine Registry listing deployed InterMine instances across organisms and life-science research areas.
    id: intermine.registry
    name: InterMine Registry
    original_source:
      - relation_type: prov:hadPrimarySource
        source: intermine
    product_url: https://registry.intermine.org/
  - category: ProgrammingInterface
    description: InterMine Registry Swagger API for programmatically discovering public InterMine instances.
    id: intermine.registry-api
    is_public: true
    name: InterMine Registry API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: intermine
    product_url: https://intermine.org/developers/registry/
  - category: GraphicalInterface
    description: Web-based interface for searching, querying, and analyzing mouse data from MGI through MouseMine
    format: http
    id: mousemine.web
    name: MouseMine Web Interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: mousemine
    product_url: https://www.mousemine.org/mousemine/begin.do
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: mgi
      - relation_type: prov:wasInfluencedBy
        source: intermine
  - category: ProgrammingInterface
    description: Programmatic access to MouseMine data via RESTful web services with client libraries for Perl, Python, Ruby, and Java
    format: http
    id: mousemine.api
    is_public: true
    name: MouseMine API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: mousemine
    product_url: https://www.mousemine.org/mousemine/api.do
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: mgi
      - relation_type: prov:wasInfluencedBy
        source: intermine
  - category: GraphicalInterface
    description: Pre-built query templates for common data retrieval tasks covering genome features, proteins, expression, interactions, phenotypes, diseases, and more
    format: http
    id: mousemine.templates
    name: MouseMine Query Templates
    original_source:
      - relation_type: prov:hadPrimarySource
        source: mousemine
    product_url: https://www.mousemine.org/mousemine/templates.do
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: mgi
      - relation_type: prov:wasInfluencedBy
        source: intermine
  - category: GraphicalInterface
    description: Custom query construction tool for building complex, iterative queries across multiple data types
    format: http
    id: mousemine.querybuilder
    name: MouseMine QueryBuilder
    original_source:
      - relation_type: prov:hadPrimarySource
        source: mousemine
    product_url: https://www.mousemine.org/mousemine/customQuery.do
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: mgi
      - relation_type: prov:wasInfluencedBy
        source: intermine
publications:
  - authors:
      - Richard N Smith
      - Jelena Aleksic
      - Daniela Butano
      - Adrian Carr
      - Sergio Contrino
      - Fengyuan Hu
    doi: 10.1093/bioinformatics/bts577
    id: doi:10.1093/bioinformatics/bts577
    journal: Bioinformatics
    preferred: true
    title: 'InterMine: a flexible data warehouse system for the integration and analysis of heterogeneous biological data'
    year: '2012'
  - authors:
      - Alex Kalderimis
      - Mike Lyne
      - Daniela Butano
      - Sergio Contrino
      - Kim Rutherford
      - Paul Flicek
    doi: 10.1093/nar/gku301
    id: doi:10.1093/nar/gku301
    journal: Nucleic Acids Research
    preferred: false
    title: 'InterMine: extensive web services for modern biology'
    year: '2014'
repository: https://github.com/intermine/intermine
---

# InterMine

InterMine is an open-source system for building integrated biological data
warehouses. It provides reusable web interfaces, query tools, and APIs that power
public data mines such as MouseMine and many other organism- and domain-specific
InterMine instances.
