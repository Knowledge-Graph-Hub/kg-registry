---
layout: resource_detail
activity_status: active
id: orcid
name: ORCID
description: >-
  ORCID is a free, unique, persistent identifier (PID)
  for individuals to use as they engage in research,
  scholarship, and innovation activities.
domains:
  - other
contacts:
  - category: Organization
    label: ORCID
homepage_url: https://orcid.org/
repository: https://github.com/ORCID
category: DataSource
last_modified_date: '2026-05-30T00:00:00Z'
publications:
  - preferred: true
    id: doi:10.1087/20120404
    title: "ORCID: a system to uniquely identify researchers"
    journal: Learned Publishing
    year: "2012"
    doi: 10.1087/20120404
products:
  - category: GraphicalInterface
    description: Web interface for searching ORCID records and viewing researcher profiles.
    format: http
    id: orcid.portal
    name: ORCID Registry Portal
    original_source:
      - source: orcid
        relation_type: prov:hadPrimarySource
    product_url: https://orcid.org/
  - category: ProgrammingInterface
    connection_url: https://pub.orcid.org/v3.0/
    description: Public API documentation and access information for ORCID record retrieval.
    format: http
    id: orcid.api
    is_public: true
    name: ORCID Public API
    original_source:
      - source: orcid
        relation_type: prov:hadPrimarySource
    product_url: https://info.orcid.org/what-is-orcid/services/public-api/
  - category: DocumentationProduct
    description: ORCID documentation, support, and integration guidance for researcher
      records, API clients, and institutional workflows.
    format: http
    id: orcid.docs
    name: ORCID Documentation
    original_source:
      - source: orcid
        relation_type: prov:hadPrimarySource
    product_url: https://info.orcid.org/documentation/
license:
  label: CC0 1.0
  id: https://creativecommons.org/publicdomain/zero/1.0/
creation_date: '2025-03-09T00:00:00Z'
---

ORCID is a free, unique, persistent identifier (PID) for individuals
to use as they engage in research, scholarship, and innovation
activities.

The ORCID registry is used across publishers, funders, universities, and data
repositories to distinguish researchers with a stable identifier and portable
profile. Researchers can manage public record content, connect trusted systems,
reuse profile data across workflows, and expose public metadata through ORCID's
web interface and REST API.

For integrators, ORCID provides public API access for reading public records,
searching the registry, and collecting validated ORCID identifiers in external
systems. The broader ORCID documentation site also covers member integrations,
record management, and adoption guidance for institutional and infrastructure
partners.
