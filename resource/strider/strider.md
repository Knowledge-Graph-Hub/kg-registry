---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://renci.org/
  - contact_type: github
    value: ranking-agent
  label: Renaissance Computing Institute (RENCI)
creation_date: '2026-10-27T00:00:00Z'
description: Strider is the knowledge-provider querying and answer-generating module
  of the ARAGORN autonomous relay agent in the NCATS Biomedical Data Translator. It
  accepts a biomedical question as a Translator Reasoner API (TRAPI) message, decomposes
  the query graph into one-hop subqueries, sends them to registered Translator knowledge
  providers (KPs), and assembles their responses into TRAPI results asynchronously.
  It is developed by RENCI in the ranking-agent GitHub organization.
domains:
- biomedical
- software
- information technology
homepage_url: https://strider.renci.org/docs
id: strider
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://github.com/ranking-agent/strider/blob/master/LICENSE
  label: MIT
name: Strider
products:
- category: ProgrammingInterface
  description: Strider TRAPI web service (RENCI deployment), with OpenAPI documentation;
    answers TRAPI query graphs by querying registered Translator knowledge providers.
  format: http
  id: strider.api
  name: Strider TRAPI API (RENCI)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: strider
  product_url: https://strider.renci.org/docs
- category: ProgrammingInterface
  description: Strider TRAPI web service on the NCATS Translator ITRB infrastructure.
  format: http
  id: strider.api.itrb
  name: Strider TRAPI API (ITRB)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: strider
  product_url: https://strider.transltr.io/docs
- category: ProcessProduct
  description: Strider source code (Python), with Docker-based development and test
    tooling.
  format: python
  id: strider.code
  name: Strider Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: strider
  product_url: https://github.com/ranking-agent/strider
repository: https://github.com/ranking-agent/strider
---
# Strider

## Overview

Strider is the module of the ARAGORN Translator reasoner that queries knowledge providers and builds answers. Given a TRAPI query graph, it breaks the graph into one-hop subqueries, sends each to the registered Translator knowledge providers that can answer it, and assembles the responses into TRAPI results.

## Access

- RENCI deployment: https://strider.renci.org/docs
- ITRB deployment: https://strider.transltr.io/docs
- Source code: https://github.com/ranking-agent/strider (MIT license)

Each deployment's `/kps` endpoint lists the knowledge providers it queries. The two deployments' lists differ.
