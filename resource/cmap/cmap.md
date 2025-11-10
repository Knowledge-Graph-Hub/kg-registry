---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    label: Broad Institute
    contact_details:
      - contact_type: email
        value: cmap@broadinstitute.org
      - contact_type: url
        value: https://www.broadinstitute.org/connectivity-map-cmap
creation_date: '2025-01-10T00:00:00Z'
description: The Connectivity Map (CMap) is a groundbreaking genome-scale perturbation resource containing over 3 million gene expression profiles cataloging transcriptional responses to chemical, genetic, and disease perturbations across multiple cancer cell types. Developed by the Broad Institute as part of the NIH Library of Integrated Network-Based Cellular Signatures (LINCS) program, CMap addresses fundamental challenges in understanding protein function and small molecule mechanisms of action by creating a comprehensive catalog of cellular signatures representing systematic perturbation. The database employs the L1000 high-throughput gene expression assay, which directly measures ~978 landmark genes and computationally infers expression of ~11,350 additional genes using inference algorithms, providing a cost-effective reduced representation of the transcriptome. CMap contains signatures from approximately 5,000 small-molecule compounds, 3,000 genetic reagents including shRNAs, CRISPR knockdowns, and overexpression constructs, tested primarily across nine core cancer cell lines that include A375, A549, HA1E, HCC515, HT29, HEPG2, MCF7, PC3, and VCAP. The resource enables researchers to query with their own gene expression signatures to identify perturbagens that induce similar or opposing transcriptional responses, thereby discovering unexpected connections between diseases, drug mechanisms, and protein functions. CMap data is accessible through CLUE, a cloud-based unified environment providing user-friendly web applications including query tools, data browsers, metadata search, and visualization apps for exploring perturbation-driven gene expression patterns. The database supports diverse research applications including drug repurposing by identifying compounds with similar mechanisms, target identification by finding small molecules that mimic genetic perturbations, disease mechanism understanding by connecting disease signatures to perturbagen responses, and biomarker discovery through systematic analysis of transcriptional responses. While personalized support ended in July 2022, all data, tools, and extensive documentation through Connectopedia remain fully accessible, with over 1.5 million replicate-collapsed signatures and 3 million profiles available for download and programmatic access via Python libraries and APIs.
domains:
  - genomics
  - drug discovery
  - pharmacology
homepage_url: https://clue.io/
id: cmap
infores_id: cmap
last_modified_date: '2025-01-10T00:00:00Z'
layout: resource_detail
license:
  id: https://clue.io/connectopedia/terms
  label: CLUE Terms of Use
name: Connectivity Map
products:
  - category: GraphicalInterface
    description: Cloud-based user interface providing suite of apps for querying gene expression signatures, browsing perturbagen data, searching metadata, and visualizing connectivity results
    id: cmap.clue
    name: CLUE Platform
    original_source:
      - cmap
    product_url: https://clue.io/
  - category: ProgrammingInterface
    description: Python library cmapBQ for programmatic access to CMap data through Google BigQuery with query capabilities for signatures and metadata
    id: cmap.python_api
    is_public: true
    name: cmapBQ Python Library
    original_source:
      - cmap
    product_url: https://cmapbq.readthedocs.io/
  - category: GraphicalInterface
    description: Query app enabling users to search CMap database with custom gene expression signatures to find perturbagens with similar or opposing transcriptional effects
    id: cmap.query_app
    name: CLUE Query App
    original_source:
      - cmap
    product_url: https://clue.io/query
  - category: Product
    description: Data releases containing replicate-collapsed signatures and gene expression profiles in GCTx matrix format available for download
    format: hdf5
    id: cmap.data_downloads
    name: CMap Data Downloads
    original_source:
      - cmap
    product_url: https://clue.io/releases/data-dashboard
  - category: DocumentationProduct
    description: Comprehensive knowledge base containing glossary, tutorials, analytical methods, experimental protocols, and detailed documentation
    format: http
    id: cmap.connectopedia
    name: Connectopedia
    original_source:
      - cmap
    product_url: https://clue.io/connectopedia
publications:
  - id: https://doi.org/10.1016/j.cell.2017.10.049
    title: "A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles"
repository: https://github.com/cmap
synonyms:
  - CMap
  - Connectivity Map
  - LINCS L1000
---

# Connectivity Map

## Overview

The Connectivity Map (CMap) is a genome-scale library of cellular signatures that catalogs transcriptional responses to chemical, genetic, and disease perturbations, enabling systematic exploration of connections between diseases, drugs, and genes through over 3 million gene expression profiles.

## Information Resource ID

This resource has the Information Resource identifier: `infores:cmap`
