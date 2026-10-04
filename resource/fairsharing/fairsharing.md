---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: contact@fairsharing.org
  - contact_type: url
    value: https://fairsharing.org/
  label: FAIRsharing team, University of Oxford
creation_date: '2026-10-04T00:00:00Z'
description: FAIRsharing is a curated, community-driven registry of data and metadata
  standards (terminologies, models, formats, reporting guidelines and identifier schemas),
  databases and repositories, and data policies from funders, journals and other organizations,
  across all disciplines. Records are interlinked, carry persistent FAIRsharing identifiers
  and DOIs, and are maintained by the FAIRsharing team at the University of Oxford
  together with record owners. Content is available through a web portal and an authenticated
  REST API under CC BY-SA 4.0.
domains:
- information technology
- metadata
homepage_url: https://fairsharing.org/
id: fairsharing
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: FAIRsharing
products:
- category: GraphicalInterface
  description: Searchable web portal for browsing and querying FAIRsharing records
    on standards, databases, policies and collections, with filters by record type,
    subject, domain, taxonomy and country, and links between related records.
  format: http
  id: fairsharing.portal
  name: FAIRsharing Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairsharing
  product_url: https://fairsharing.org/
- category: ProgrammingInterface
  description: REST/JSON API for reading and writing FAIRsharing records. Access requires
    a FAIRsharing account; clients sign in to obtain a JWT token that is sent with
    each request.
  format: http
  id: fairsharing.api
  name: FAIRsharing REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairsharing
  product_url: https://api.fairsharing.org/
  warnings:
  - When checked on 2026-10-04, the API root redirected to the FAIRsharing licence
    page; endpoints require login with a JWT token, so no anonymous data access was
    tested.
- category: DocumentationProduct
  description: Documentation for the FAIRsharing API, describing authentication and
    the available record endpoints.
  format: http
  id: fairsharing.api-docs
  name: FAIRsharing API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairsharing
  product_url: https://fairsharing.org/API_doc
- category: DocumentationProduct
  description: User guide for FAIRsharing covering record types, curation, searching,
    collections, and how to register and maintain records.
  format: http
  id: fairsharing.docs
  name: FAIRsharing User Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairsharing
  product_url: https://fairsharing.gitbook.io/fairsharing/
- category: ProcessProduct
  description: Source code for the FAIRsharing web application front end (Vue.js),
    released under AGPL-3.0.
  format: http
  id: fairsharing.code
  license:
    id: https://www.gnu.org/licenses/agpl-3.0.html
    label: AGPL-3.0
  name: FAIRsharing Web Application Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairsharing
  product_url: https://github.com/FAIRsharing/fairsharing.github.io
- category: ProgrammingInterface
  description: Model Context Protocol (MCP) server providing access to FAIRsharing
    content for LLM-based tools, released under GPL-3.0.
  format: http
  id: fairsharing.mcp
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.html
    label: GPL-3.0
  name: FAIRsharing MCP Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairsharing
  product_url: https://github.com/FAIRsharing/fairsharing-mcp
publications:
- authors:
  - Susanna-Assunta Sansone
  - Peter McQuilton
  - Philippe Rocca-Serra
  - Alejandra Gonzalez-Beltran
  - Massimiliano Izzo
  - Allyson L. Lister
  - Milo Thurston
  doi: 10.1038/s41587-019-0080-8
  id: doi:10.1038/s41587-019-0080-8
  journal: Nature Biotechnology
  preferred: true
  title: FAIRsharing as a community approach to standards, repositories and policies
  year: '2019'
synonyms:
- BioSharing
---
# FAIRsharing

FAIRsharing (formerly BioSharing) is a curated registry of data and metadata standards, databases and repositories, and data policies, run by the Data Readiness Group at the University of Oxford. It began in the life sciences and now covers all disciplines.

## Content

- **Standards**: terminology artifacts (ontologies, controlled vocabularies), models and formats, reporting guidelines, and identifier schemas.
- **Databases**: repositories and knowledge bases, with links to the standards they implement.
- **Policies**: data policies from funders, journals, publishers and other organizations, with links to recommended standards and databases.
- **Collections**: curated groupings of records for a project, community or organization.

Each record has a stable FAIRsharing identifier (for example `FAIRsharing.3b36hk`) and a DOI. Many KG-Registry pages carry these identifiers in their `fairsharing_id` field.

## Access

Records can be browsed and searched on the web portal. Programmatic access is through a REST/JSON API that requires a FAIRsharing account and a JWT token. Content is licensed under CC BY-SA 4.0. A complete database export is deposited with the Oxford University Research Archive as a backup, but it was under embargo when checked on 2026-10-04.
