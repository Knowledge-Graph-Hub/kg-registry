---
activity_status: active
category: KnowledgeGraph
collection:
  - ber
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://mangal.io/
    label: Mangal
creation_date: '2025-12-15T00:00:00Z'
description: mangal.io is a collaborative database and analysis platform for ecological networks, providing a comprehensive collection of species interaction networks (food webs, pollination networks, plant-herbivore networks) with tools for visualization, analysis, and reuse of published ecological data.
domains:
  - environment
  - biological systems
homepage_url: https://mangal.io/
id: mangal
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: mangal.io
products:
  - category: GraphicalInterface
    description: Web interface for browsing, querying, and visualizing ecological networks
    format: http
    id: mangal.portal
    name: mangal.io Web Portal
    product_url: https://mangal.io/
    original_source:
      - source: mangal
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: catalogue-of-life
        relation_type: prov:used
      - source: gbif
        relation_type: prov:used
      - source: itis
        relation_type: prov:used
  - category: ProgrammingInterface
    description: RESTful API for programmatic access to network data and metadata
    format: http
    id: mangal.api
    is_public: true
    name: mangal.io API
    product_url: https://mangal.io/api/v2/
    original_source:
      - source: mangal
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: catalogue-of-life
        relation_type: prov:used
      - source: gbif
        relation_type: prov:used
      - source: itis
        relation_type: prov:used
  - category: DocumentationProduct
    description: API documentation, user guides, and data model specification
    format: http
    id: mangal.docs
    name: mangal.io Documentation
    product_url: https://mangal.io/documentation
    original_source:
      - source: mangal
        relation_type: prov:hadPrimarySource
  - category: ProcessProduct
    description: R package for retrieving and exploring data from the Mangal ecological interactions database
    format: http
    id: mangal.rmangal
    name: rmangal R Client
    product_url: https://docs.ropensci.org/rmangal/
    original_source:
      - source: mangal
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: catalogue-of-life
        relation_type: prov:used
      - source: gbif
        relation_type: prov:used
      - source: itis
        relation_type: prov:used
publications:
- authors:
  - Steve Vissault
  - Dominique Gravel
  - Timothee Poisot
  doi: 10.3897/biss.3.37037
  id: doi:10.3897/biss.3.37037
  journal: Biodiversity Information Science and Standards
  preferred: true
  title: 'Mangal: An open infrastructure for ecological interactions'
  year: '2019'
- authors:
  - Timothee Poisot
  - Benjamin Baiser
  - Jennifer A. Dunne
  - Sonia Kefi
  - Francois Massol
  - Nicolas Mouquet
  - Tamara N. Romanuk
  - Daniel B. Stouffer
  - Spencer A. Wood
  - Dominique Gravel
  doi: 10.1111/ecog.00976
  id: doi:10.1111/ecog.00976
  journal: Ecography
  title: mangal - making ecological network analysis simple
  year: '2016'
taxon:
  - NCBITaxon:33208
  - NCBITaxon:33090
---

# mangal.io

## Overview

mangal.io is a collaborative platform dedicated to ecological network data. It provides a centralized database of published food webs, pollination networks, plant-herbivore networks, and other species interaction networks from the scientific literature.

## Features

- **Network Database**: Collection of ecological interaction networks from peer-reviewed studies
- **Visualization Tools**: Interactive visualization and exploration of network structures
- **Analysis Platform**: Tools for analyzing network properties and metrics
- **Data Interoperability**: Standardized data formats for network data exchange
- **API Access**: Programmatic access to network data and metadata

## Data Types

The platform includes various types of ecological networks:
- Food webs and trophic networks
- Pollination networks
- Plant-herbivore interaction networks
- Parasite-host networks
- Mutualistic networks
- Other biotic interaction networks

## Citation

When using mangal.io data, please cite the original studies associated with each network along with the mangal.io platform.

## Automated Evaluation

- View the automated evaluation: [mangal automated evaluation](mangal_eval_automated.html)
