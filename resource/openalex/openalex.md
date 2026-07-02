---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ourresearch.org/
  label: OurResearch
creation_date: '2026-07-01T00:00:00Z'
description: OpenAlex is a free, open catalog of the global research system. It indexes
  scholarly works together with their authors, sources (venues such as journals and
  repositories), institutions, publishers, funders, and concepts/topics, and captures
  the relationships among them. Built and maintained by the nonprofit OurResearch,
  it is the successor to the discontinued Microsoft Academic Graph and is available
  through an open API and a full downloadable data snapshot.
domains:
- literature
- information technology
- general
homepage_url: https://openalex.org/
id: openalex
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: OpenAlex
products:
- category: ProgrammingInterface
  description: The OpenAlex REST API provides open programmatic access to the full
    OpenAlex catalog of works, authors, sources, institutions, publishers, funders,
    and concepts/topics.
  format: http
  id: openalex.api
  name: OpenAlex API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openalex
  product_url: https://docs.openalex.org/
- category: Product
  description: The OpenAlex data snapshot is a complete downloadable copy of the OpenAlex
    dataset, updated regularly and distributed as JSON Lines files via a public Amazon
    S3 bucket for bulk use.
  format: mixed
  id: openalex.snapshot
  name: OpenAlex Data Snapshot
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openalex
  product_url: https://docs.openalex.org/download-all-data/openalex-snapshot
- category: GraphProduct
  description: RDF graph representation of the OpenAlex scholarly data as Linked Open
    Data, distributed as Turtle (TTL) snapshots via the SemOpenAlex code and data
    repository.
  format: ttl
  id: semopenalex.graph
  name: SemOpenAlex RDF Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: semopenalex
  - relation_type: prov:wasDerivedFrom
    source: openalex
  product_url: https://github.com/metaphacts/semopenalex
publications:
- authors:
  - Jason Priem
  - Heather Piwowar
  - Richard Orr
  doi: 10.48550/arXiv.2205.01833
  id: doi:10.48550/arXiv.2205.01833
  journal: arXiv
  preferred: true
  title: 'OpenAlex: A fully-open index of scholarly works, authors, venues, institutions,
    and concepts'
  year: '2022'
---
## Description

OpenAlex is a free and open catalog of the global research system, built and
maintained by the nonprofit OurResearch. It describes scholarly works and the
entities connected to them, including authors, sources (venues such as journals
and repositories), institutions, publishers, funders, and concepts/topics, along
with the relationships among them. OpenAlex is the successor to the discontinued
Microsoft Academic Graph and is offered through a fully open REST API and a
complete downloadable data snapshot, all released under a CC0 public-domain
dedication.

## Products

### OpenAlex API

Open REST API providing programmatic access to the full OpenAlex catalog.

**URL**: [https://docs.openalex.org/](https://docs.openalex.org/)

**Format**: http

### OpenAlex Data Snapshot

Complete downloadable copy of the OpenAlex dataset, distributed as JSON Lines
files via a public Amazon S3 bucket.

**URL**: [https://docs.openalex.org/download-all-data/openalex-snapshot](https://docs.openalex.org/download-all-data/openalex-snapshot)

**Format**: mixed
</content>
</invoke>