---
activity_status: inactive
category: Resource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: ben.elsworth@bristol.ac.uk
  label: Ben Elsworth
creation_date: '2025-09-03T00:00:00Z'
description: Vectology is a software platform and API for exploring relationships
  among biomedical variables using sentence embedding models derived from biomedical
  literature. It converts brief variable descriptions into vector representations
  enabling similarity search, recommendation, and relational insight without manual
  ontology annotation.
domains:
- biomedical
- genomics
- health
- investigations
homepage_url: http://vectology.mrcieu.ac.uk/
id: vectology
last_modified_date: '2025-09-03T00:00:00Z'
layout: resource_detail
name: Vectology
products:
- category: ProgrammingInterface
  description: Public API providing access to sentence embedding-based similarity
    endpoints and variable vector queries
  id: vectology.api
  is_public: true
  name: Vectology API
  original_source:
  - vectology
  product_url: http://vectology-api.mrcieu.ac.uk/
- category: DocumentationProduct
  description: Project information page including description, maintenance status,
    contacts, and publication reference
  format: http
  id: vectology.docs
  name: Vectology Project Page
  original_source:
  - vectology
  product_url: https://mrcieu.github.io/software/vectology/
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
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
  product_url: https://docs.epigraphdb.org/graph-database/
  secondary_source:
  - epigraphdb
---
## Overview

Vectology provides a data-driven alternative to manual expert annotation of short biomedical variable descriptions. Using precomputed sentence embedding models trained on biomedical literature, it maps each variable description to a dense vector. Vector similarity operations enable identification of conceptually related variables, recommendation, and exploration of relationships between sets of variables.

## Methodology

1. Ingest variable text descriptions from biomedical datasets.
2. Generate sentence embeddings using pretrained biomedical language models.
3. Store vector representations to support similarity and distance queries.
4. Provide API endpoints and a web UI for searching, comparing, and recommending related variables.

## Use Cases

- Rapidly find conceptually similar phenotypic or exposure variables.
- Recommend additional variables for inclusion in analyses.
- Cluster or visualize variable sets in embedding space.
- Support ontology mapping or curation triage by highlighting nearest neighbors.

## Abstract (from methods paper)

Many biomedical data sets contain variables that are identified by simple, and often short, descriptions. Traditionally these would either be manually annotated and/or assigned to ontologies using expert knowledge, facilitating interactions with other data sets and gaining an understanding of where these variables lie in the biomedical knowledge space. An alternative approach is to utilise sentence embedding methods and convert these variables into vectors, calculated from precomputed models derived from biomedical literature. This provides a data-driven alternative to manual expert annotation, automatically harnessing the expert knowledge captured in the existing literature. These vectors, representing the biomedical space embodied by each specific piece of text, enable us to apply methods for exploring relationships between variables in vector space, notably comparing distances between vectors. From here, it is possible to recommend a set of variables as the most conceptually similar to a given piece of text or existing vector, whilst also gaining insight into how a group of variables are related. Vectology is made available via an API (http://vectology-api.mrcieu.ac.uk/) and basic usage can be explored via a web application (http://vectology.mrcieu.ac.uk).

## Citation

Elsworth B, Liu Y, Gaunt TR. Vectology – exploring biomedical variable relationships using sentence embedding and vectors. MRC Integrative Epidemiology Unit, University of Bristol. (Manuscript PDF, DSRS Turing 2019 proceedings excerpt.)

## Contact

Feedback or issues can be submitted via the project page or by emailing the listed maintainers (ben.elsworth@bristol.ac.uk, yi6240.liu@bristol.ac.uk, Tom.Gaunt@bristol.ac.uk).