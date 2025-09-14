---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-09-14T00:00:00Z'
description: Global Biotic Interactions (GloBI) integrates and normalizes species interaction datasets (e.g., predation, pollination, parasitism, mutualism, host-pathogen) from many primary sources to provide open, queryable access to organism-to-organism interaction records with taxonomic resolution and provenance.
domains:
  - environment
  - biological systems
  - public health
homepage_url: https://www.globalbioticinteractions.org/
id: globi
last_modified_date: '2025-09-14T00:00:00Z'
layout: resource_detail
name: Global Biotic Interactions (GloBI)
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0 (data)
publications:
  - id: doi:10.1016/j.ecoinf.2014.08.005
    title: "Global Biotic Interactions: An open infrastructure to share and analyze species-interaction datasets"
    year: '2014'
    journal: Ecological Informatics
    doi: 10.1016/j.ecoinf.2014.08.005
products:
  - category: GraphicalInterface
    description: Search and browse interface for interaction queries across integrated datasets
    format: http
    id: globi.portal
    name: GloBI Portal
    product_url: https://www.globalbioticinteractions.org/
  - category: ProgrammingInterface
    description: REST-style API endpoints for programmatic species interaction queries (JSON/CSV)
    format: http
    id: globi.api
    name: GloBI API
    product_url: https://www.globalbioticinteractions.org/how-to
  - category: Product
    description: Bulk data export and dataset listing (downloads and dataset metadata)
    format: http
    id: globi.datasets
    name: GloBI Datasets
    product_url: https://www.globalbioticinteractions.org/datasets
  - category: DocumentationProduct
    description: About and methodological documentation, contribution guidelines, and references
    format: http
    id: globi.docs
    name: GloBI Documentation
    product_url: https://www.globalbioticinteractions.org/about
  - category: Product
    description: Zenodo DOI badge pointing to latest archived release snapshot of integrated datasets
    format: http
    id: globi.release
    name: GloBI Archived Release (Zenodo)
    product_url: https://zenodo.org/badge/latestdoi/2478263
---

# Global Biotic Interactions (GloBI)

## Overview

GloBI provides harmonized access to species interaction data (predation, parasitism, pollination, host-pathogen, mutualism and more) aggregated from many source datasets. Each record links interacting taxa with interaction type, source citation, and provenance, enabling ecological network construction, food web analysis, and biodiversity informatics.

## Access

- Portal: interactive search and browse for interaction records
- API: REST endpoints returning JSON/CSV for integration into analyses
- Datasets: catalog of contributing datasets with metadata and attribution
- Archived Releases: DOI versioned snapshots for reproducible research

## Data Model

Interaction records contain subject taxon, object taxon, interaction type (e.g., eats, pollinates), and references to original dataset sources. Normalization includes taxonomic resolution and mapping of interaction predicates.

## Citation

Please cite the 2014 Ecological Informatics paper when using GloBI and acknowledge primary data sources listed in dataset metadata.
