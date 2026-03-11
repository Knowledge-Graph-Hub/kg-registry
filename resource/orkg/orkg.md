---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://orkg.org/about
  label: Open Research Knowledge Graph Team
creation_date: '2026-03-11T00:00:00Z'
description: The Open Research Knowledge Graph (ORKG) aims to describe research papers
  in a structured manner. It represents research papers and their contributions as
  structured, machine-readable descriptions that can be explored, compared, and
  reused through the ORKG portal and API.
domains:
- literature
homepage_url: https://orkg.org/
id: orkg
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
last_modified_date: '2026-03-11T00:00:00Z'
name: Open Research Knowledge Graph
repository: https://gitlab.com/TIBHannover/orkg/orkg-frontend/
products:
- category: GraphicalInterface
  description: Web portal for browsing papers, creating structured research descriptions,
    and comparing research contributions in ORKG.
  format: http
  id: orkg.portal
  name: ORKG Web Portal
  original_source:
  - orkg
  product_url: https://orkg.org/
- category: ProgrammingInterface
  description: Public REST API for programmatic access to ORKG resources, comparisons,
    papers, and other structured scholarly content.
  format: http
  id: orkg.api
  is_public: true
  name: ORKG REST API
  original_source:
  - orkg
  product_url: https://orkg.org/api
- category: DocumentationProduct
  description: Static reference documentation for the ORKG REST API published via
    GitLab Pages.
  format: http
  id: orkg.api-docs
  name: ORKG API Documentation
  original_source:
  - orkg.api
  product_url: http://tibhannover.gitlab.io/orkg/orkg-backend/api-doc/
- category: ProcessProduct
  description: Python package wrapping the ORKG API for programmatic access from
    Python workflows.
  format: python
  id: orkg.python
  name: ORKG Python Package
  original_source:
  - orkg.api
  product_url: https://pypi.org/project/orkg/
- category: DocumentationProduct
  description: Official ORKG documentation covering tutorials, reference material,
    and REST API model documentation.
  format: http
  id: orkg.docs
  name: ORKG Documentation
  original_source:
  - orkg
  product_url: https://docs.orkg.org/
- category: GraphicalInterface
  description: Virtuoso-based SPARQL query editor for querying ORKG RDF data.
  format: http
  id: orkg.triplestore
  name: ORKG Virtuoso Query Editor
  original_source:
  - orkg
  product_url: https://orkg.org/triplestore
- category: GraphicalInterface
  description: Visual SPARQL editor for exploring ORKG data with query examples.
  format: http
  id: orkg.sparql
  name: ORKG Visual SPARQL Editor
  original_source:
  - orkg
  product_url: https://orkg.org/sparql/
- category: GraphProduct
  description: RDF dump of the Open Research Knowledge Graph distributed in N-Triples
    format.
  format: ntriples
  id: orkg.dump
  name: ORKG RDF Dump
  original_source:
  - orkg
  - wikidata
  - geonames
  - ncit
  - chebi
  - ncbitaxon
  - go
  - clo
  - omit
  - iao
  - uo
  - stato
  - obi
  secondary_source:
  - orkg
  product_file_size: 642902930
  product_url: https://orkg.org/api/rdf/dump
publications:
- authors:
  - Mohamad Yaser Jaradeh
  - Allard Oelen
  - Kheir Eddine Farfar
  - Manuel Prinz
  - Jennifer D'Souza
  - "Gábor Kismihók"
  - Markus Stocker
  - "Sören Auer"
  doi: 10.1145/3360901.3364435
  id: doi:10.1145/3360901.3364435
  journal: Proceedings of the 10th International Conference on Knowledge Capture
  preferred: true
  title: Open Research Knowledge Graph
  year: '2019'
synonyms:
- ORKG
---

# Open Research Knowledge Graph (ORKG)

## Overview

The Open Research Knowledge Graph (ORKG) is a scholarly knowledge graph for representing research papers and their contributions as structured descriptions rather than only free text. It provides a web portal for curation and comparison plus a public REST API for programmatic access.

## Key Features

- **Structured Research Descriptions**: Papers and contributions are represented in machine-readable form
- **Comparisons**: ORKG supports side-by-side comparison of research contributions across papers
- **Multiple Scholarly Views**: The platform documents dedicated models for comparisons, visualizations, smart reviews, templates, and literature lists
- **Programmatic Access**: ORKG exposes a public REST API and official documentation for developers and integrators

## Applications

- **Literature Search**: Find papers using structured scholarly metadata
- **Research Comparison**: Compare methods, datasets, results, and other contribution details
- **Knowledge Discovery**: Explore reusable scholarly entities and relationships captured in ORKG
- **Integration**: Reuse ORKG content through the public REST API and documentation
