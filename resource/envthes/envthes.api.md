---
category: ProgrammingInterface
description: Skosmos REST API for EnvThes, with endpoints for vocabulary metadata,
  statistics, search and per-concept RDF (Turtle, RDF/XML or JSON-LD).
format: http
id: envthes.api
name: EnvThes Skosmos REST API
original_source:
- relation_type: prov:hadPrimarySource
  source: envthes
product_url: https://vocabs.lter-europe.net/rest/v1/EnvThes/
warnings:
- The whole-vocabulary download endpoint (https_//vocabs.lter-europe.net/rest/v1/EnvThes/data)
  returned HTTP 404 ("No download source URL known for vocabulary EnvThes") when checked
  on 2026-10-05. Per-concept data requests with a uri parameter worked.
layout: product_detail
---
