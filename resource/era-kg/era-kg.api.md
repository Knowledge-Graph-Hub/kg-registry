---
category: ProgrammingInterface
description: SPARQL API path documented with the Agency's data releases as the public
  query interface to the RINF knowledge graph.
format: http
id: era-kg.api
is_public: true
name: ERA Knowledge Graph SPARQL API
original_source:
- relation_type: prov:hadPrimarySource
  source: era-kg
product_url: https://rinf.data.era.europa.eu/api/v1/sparql/rinf
warnings:
- Checked on 2026-08-06_ this path returned HTTP 500 with the message "SPARQL upstream
  returned 500". The GraphDB endpoint at graph.data.era.europa.eu answered the same
  queries successfully, so this appears to be a fault in the API layer rather than
  in the graph.
layout: product_detail
---
