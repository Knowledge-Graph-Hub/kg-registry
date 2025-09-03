---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: feedback@epigraphdb.org
  - contact_type: url
    value: https://docs.epigraphdb.org/
  - contact_type: github
    value: https://github.com/MRCIEU/epigraphdb
  label: EpiGraphDB Team (MRC Integrative Epidemiology Unit, University of Bristol)
creation_date: '2025-09-03T00:00:00Z'
description: EpiGraphDB is an analytical platform and graph database for health data science that integrates Mendelian randomization causal estimates across a wide range of phenotypes with diverse bioinformatic and epidemiological resources. It supports systematic causal inference, data mining, and exploration through a web application, API, R package, and curated graph knowledge base.
domains:
- health
- biomedical
- genomics
- investigations
homepage_url: https://epigraphdb.org/
id: epigraphdb
last_modified_date: '2025-09-03T00:00:00Z'
layout: resource_detail
license:
  id: https://github.com/MRCIEU/epigraphdb
  label: Mixed
name: EpiGraphDB
products:
- category: GraphicalInterface
  description: Web application for interactive exploration of EpiGraphDB including search, causal estimates, pathways, literature evidence, ontology, and visualization gallery
  format: http
  id: epigraphdb.web
  name: EpiGraphDB Web UI
  original_source:
  - epigraphdb
  product_url: https://epigraphdb.org/
- category: ProgrammingInterface
  description: Public REST API for programmatic access to EpiGraphDB graph entities, relationships, causal estimates, and metadata
  id: epigraphdb.api
  is_public: true
  name: EpiGraphDB REST API
  original_source:
  - epigraphdb
  product_url: https://api.epigraphdb.org/
- category: ProgrammingInterface
  description: R client package providing higher-level access to EpiGraphDB API endpoints and analysis workflows
  id: epigraphdb.rpackage
  is_public: true
  name: epigraphdb R Package
  original_source:
  - epigraphdb
  product_url: https://mrcieu.github.io/epigraphdb-r/
  secondary_source:
  - epigraphdb
- category: DocumentationProduct
  description: Example notebooks demonstrating EpiGraphDB use cases, including causal inference, pleiotropy assessment, drug target identification, literature triangulation, and metadata queries
  id: epigraphdb.examples
  name: EpiGraphDB Example Notebooks
  original_source:
  - epigraphdb
  product_url: https://github.com/MRCIEU/epigraphdb/tree/master/paper-case-studies
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - epigraphdb
  - kg-monarch
  - vectology
  - ukbiobank
  - prsatlas
  - eqtlgen
  - mondo
  - gtex
  - ensembl
  - cpic
  - opentargets
  - efo
  - semmeddb
  - intact
  - string
  - reactome
  - mrbase
  secondary_source:
  - epigraphdb
  product_url: https://docs.epigraphdb.org/graph-database/
- category: DocumentationProduct
  description: Documentation hub containing conceptual overviews, API endpoint references, data integration details, metrics, and research study links
  format: http
  id: epigraphdb.docs
  name: EpiGraphDB Documentation
  original_source:
  - epigraphdb
  product_url: https://docs.epigraphdb.org/
---

## Overview

EpiGraphDB integrates causal inference results generated via Mendelian randomization across numerous phenotypes with complementary bioinformatic and epidemiological datasets. The platform enables hypothesis generation, pleiotropy assessment, pathway and drug target prioritization, literature triangulation, and ontology mapping within a unified graph structure. Access pathways include a rich web UI, REST API, R package, documentation, and example notebooks.

## Key Features

- Systematic integration of Mendelian randomization causal estimates
- Graph-based representation of multi-source biomedical relationships
- Interactive exploration (search, pathways, MR, literature, ontology, COVID-19, drugs)
- Programmatic access via REST API and R package
- Reproducible example notebooks and case studies
- Documentation on data integration, meta-nodes, relationships, metrics, and studies

## Citation

Liu Y, Elsworth B, Erola P, Haberland V, Hemani G, Lyon M, Zheng J, Lloyd O, Vabistsevits M, Gaunt TR. EpiGraphDB: a database and data mining platform for health data science. Bioinformatics. 2020. doi:10.1093/bioinformatics/btaa961

## Contact

Submit issues via the GitHub repository or email feedback@epigraphdb.org. Follow updates on Twitter (@epigraphdb).
