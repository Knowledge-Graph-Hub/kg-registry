---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://biofactoid.org/
    label: Bader Lab, University of Toronto (Pathway Commons)
creation_date: '2026-06-03T00:00:00Z'
description: Biofactoid is a web-based system that empowers authors to capture and share machine-readable summaries of the molecular-level interactions between genes, gene products, and chemical compounds described in their publications. Author-sourced pathway knowledge is grounded to standard identifiers and made openly available in computable formats for reuse in pathway and network analysis.
domains:
  - pathways
  - biological systems
  - systems biology
homepage_url: https://biofactoid.org/
id: biofactoid
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Biofactoid
products:
  - category: GraphicalInterface
    description: Web application where authors create a digital profile of their article's molecular interactions and browse shared pathway documents.
    format: http
    id: biofactoid.webapp
    name: Biofactoid Web Application
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biofactoid
    product_url: https://biofactoid.org/
  - category: Product
    description: Openly downloadable author-contributed pathway documents, exportable in Biofactoid's native JSON format as well as BioPAX and SBGNML standards.
    format: json
    id: biofactoid.documents
    name: Biofactoid Pathway Documents
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biofactoid
    product_url: https://biofactoid.org/
  - category: ProgrammingInterface
    description: Public API (documented via Swagger UI) for programmatic access to Biofactoid pathway documents.
    format: http
    id: biofactoid.api
    is_public: true
    name: Biofactoid API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biofactoid
    product_url: https://biofactoid.org/api
publications:
  - id: https://doi.org/10.7554/eLife.68292
    journal: eLife
    title: 'Science Forum: Author-sourced capture of pathway knowledge in computable form using Biofactoid'
    year: '2021'
repository: https://github.com/PathwayCommons/factoid
synonyms:
  - Factoid
tags:
  - biopragmatics
---

# Biofactoid

## Overview

Biofactoid is a web-based system that lets authors capture and share machine-readable
summaries of the molecular interactions described in their own publications. Authors
specify networks of interactions among genes, gene products, and chemical compounds,
which Biofactoid grounds to standard identifiers and makes openly available in
computable form for downstream pathway and network analysis.

## Key Features

- **Author-sourced curation**: Researchers directly capture the interactions from their
  own papers rather than relying on third-party curators.
- **Machine-readable output**: Documents are exportable in a native JSON format as well
  as the BioPAX and SBGNML community standards.
- **Open data**: Contributed pathway data is released under CC0 (public domain).
- **Open source**: The software is developed in the open under the MIT license.

## Access

- Web application at [biofactoid.org](https://biofactoid.org/)
- Public API documented through Swagger UI
- Source code on [GitHub](https://github.com/PathwayCommons/factoid)

## Development

Biofactoid is developed and maintained by the Bader Lab at the University of Toronto
as part of the Pathway Commons project.

## Citation

Wong JV, Franz M, Siper MC, et al. Science Forum: Author-sourced capture of pathway
knowledge in computable form using Biofactoid. eLife (2021). doi:10.7554/eLife.68292
