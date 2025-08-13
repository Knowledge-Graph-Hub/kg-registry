---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
- category: Organization
  contact_details:
  - contact_type: other
    contact_type_name: Monarch Initiative Community
    contact_type_url: https://groups.google.com/g/monarch-friends/
    value: monarch-friends
  label: Monarch Initiative
description: The Monarch Initiative is an international consortium that leads key
  global standards and semantic data integration technologies. To maximize utility
  and impact, the Monarch platform is composed of multiple open-source, open-access
  components.
domains:
- health
homepage_url: https://kghub.org/kg-monarch/index.html
id: kg-monarch
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: KG Monarch
products:
- category: GraphProduct
  description: KGX Distribution of KG-Monarch
  format: kgx
  id: kg-monarch.graph
  name: KGX Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_file_size: 230877741
  product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl
  name: KGX JSON-L Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-13: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: RDF Distribution of KG-Monarch
  format: rdfxml
  id: kg-monarch.graph.rdf
  name: RDF Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_file_size: 879238775
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch
  dump_format: neo4j
  id: kg-monarch.graph.neo4j
  name: Neo4j Dump of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-13: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: DuckDB database of KG-Monarch
  id: kg-monarch.graph.duckdb
  name: DuckDB database of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb.gz
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-13: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: HTTP 404 error
    when accessing file'
- category: ProcessProduct
  description: This repository is a code reference for the C-Path Knowledge Graph
    project, to increase discoverability of rare disease datasets through integration
    with the Monarch Knowlege Graph. Note that this is only a reference to scripts
    and queries associated with this project and is not provided as a runnable project
    because these workflows depend on an internal data catalog.
  id: cpathkg.code
  name: C-Path Knowledge Graph Integration
  original_source:
  - biolink
  - kg-monarch
  product_url: https://gitlab.c-path.org/c-pathontology/c-path-knowledge-graph-integration
  secondary_source:
  - cpathkg
repository: https://github.com/monarch-initiative/monarch-ingest
---
The Monarch Initiative is an international consortium that leads key global standards and semantic data integration technologies. Monarch resources and integrated data are also foundational to many downstream applications and contexts; we work closely with a variety of stakeholders and resource-development communities to capture feedback and make improvements. To maximize utility and impact, the Monarch platform is composed of multiple open-source, open-access components. We promote provenance and transparency, enhanced use of standards and new technologies and improved data accessibility, end-user utility, and data submission. Learn more about the complete suite of Monarch resources on our organization's [documentation pages](https://monarch-initiative.github.io/monarch-documentation/).

## Evaluation

- View the evaluation: [kg-monarch evaluation](kg-monarch_eval.html)