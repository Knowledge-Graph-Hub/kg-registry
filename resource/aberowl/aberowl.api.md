---
category: ProgrammingInterface
description: REST API (FastAPI, documented with Swagger UI) for listing ontologies,
  retrieving classes, full-text search and DL queries (subclass, superclass, equivalent)
  across the AberOWL repository.
format: http
id: aberowl.api
is_public: true
name: AberOWL REST API
original_source:
- relation_type: prov:hadPrimarySource
  source: aberowl
- relation_type: prov:hadPrimarySource
  source: bioportal
product_url: https://aber-owl.net/api/docs
warnings:
- When checked on 2026-10-04, listing, search and statistics endpoints responded,
  but DL query endpoints (/api/dlquery, /api/dlquery_all) returned "API server is
  down!".
layout: product_detail
---
