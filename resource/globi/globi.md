---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-09-14T00:00:00Z'
description: Global Biotic Interactions (GloBI) integrates and normalizes species
  interaction datasets (e.g., predation, pollination, parasitism, mutualism, host-pathogen)
  from many primary sources to provide open, queryable access to organism-to-organism
  interaction records with taxonomic resolution and provenance.
domains:
- environment
- biological systems
- public health
homepage_url: https://www.globalbioticinteractions.org/
id: globi
last_modified_date: '2025-09-14T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0 (data)
name: Global Biotic Interactions (GloBI)
products:
- category: GraphicalInterface
  description: Search and browse interface for interaction queries across integrated
    datasets
  format: http
  id: globi.portal
  name: GloBI Portal
  product_url: https://www.globalbioticinteractions.org/
- category: ProgrammingInterface
  description: REST-style API endpoints for programmatic species interaction queries
    (JSON/CSV)
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
- category: Product
  compression: gzip
  description: Tab-separated integrated species interaction pairs (interpreted names)
  format: tsv
  id: globi.interactions.tsv
  name: GloBI interpreted interactions (TSV)
  product_file_size: 3044531169
  product_url: https://zenodo.org/record/14640564/files/interactions.tsv.gz
- category: Product
  compression: gzip
  description: Comma-separated integrated species interaction pairs (interpreted names)
  format: csv
  id: globi.interactions.csv
  name: GloBI interpreted interactions (CSV)
  product_url: https://zenodo.org/record/14640564/files/interactions.csv.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-09-23_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-24_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-09-24: No Content-Length
    header found'
- category: Product
  compression: gzip
  description: Tab-separated verbatim species interaction pairs (original unresolved
    names)
  format: tsv
  id: globi.verbatim_interactions.tsv
  name: GloBI verbatim interactions (TSV)
  product_file_size: 825458639
  product_url: https://zenodo.org/record/14640564/files/verbatim-interactions.tsv.gz
- category: Product
  compression: gzip
  description: Comma-separated verbatim species interaction pairs (original unresolved
    names)
  format: csv
  id: globi.verbatim_interactions.csv
  name: GloBI verbatim interactions (CSV)
  product_url: https://zenodo.org/record/14640564/files/verbatim-interactions.csv.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-09-23_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-24_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-09-24: No Content-Length
    header found'
- category: Product
  compression: gzip
  description: Tab-separated refuted species interaction pairs (interpreted names)
  format: tsv
  id: globi.refuted_interactions.tsv
  name: GloBI refuted interactions (TSV)
  product_file_size: 17546643
  product_url: https://zenodo.org/record/14640564/files/refuted-interactions.tsv.gz
- category: Product
  compression: gzip
  description: Comma-separated refuted species interaction pairs (interpreted names)
  format: csv
  id: globi.refuted_interactions.csv
  name: GloBI refuted interactions (CSV)
  product_url: https://zenodo.org/record/14640564/files/refuted-interactions.csv.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-09-23_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-24_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-09-24: No Content-Length
    header found'
- category: Product
  compression: gzip
  description: Comma-separated refuted verbatim species interaction pairs (original
    names)
  format: csv
  id: globi.refuted_verbatim_interactions.csv
  name: GloBI refuted verbatim interactions (CSV)
  product_url: https://zenodo.org/record/14640564/files/refuted-verbatim-interactions.csv.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-09-23_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-24_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-09-24: No Content-Length
    header found'
- category: Product
  compression: gzip
  description: RDF N-Quads representation of interaction data
  format: nquads
  id: globi.interactions.nq
  name: GloBI interactions RDF (N-Quads)
  product_file_size: 13113796760
  product_url: https://zenodo.org/record/14640564/files/interactions.nq.gz
- category: Product
  compression: zip
  description: Neo4j graph database backup (v3.5.x) of interaction graph
  format: neo4j
  id: globi.neo4j.graphdb
  name: GloBI Neo4j graph database snapshot
  product_file_size: 9059233137
  product_url: https://zenodo.org/record/14640564/files/neo4j-graphdb.zip
- category: Product
  compression: gzip
  description: Tab-separated dataset namespace index
  format: tsv
  id: globi.datasets.tsv
  name: GloBI datasets index (TSV)
  product_file_size: 4373
  product_url: https://zenodo.org/record/14640564/files/datasets.tsv.gz
- category: Product
  compression: gzip
  description: Comma-separated dataset namespace index
  format: csv
  id: globi.datasets.csv
  name: GloBI datasets index (CSV)
  product_url: https://zenodo.org/record/14640564/files/datasets.csv.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-09-23_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-24_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-09-24: No Content-Length
    header found'
- category: Product
  compression: gzip
  description: Tab-separated taxonomic name mapping file
  format: tsv
  id: globi.taxon_map.tsv
  name: GloBI taxonomic name map
  product_file_size: 111241785
  product_url: https://zenodo.org/record/14640564/files/taxonMap.tsv.gz
- category: Product
  compression: gzip
  description: Tab-separated taxonomic hierarchy and identifier cache
  format: tsv
  id: globi.taxon_cache.tsv
  name: GloBI taxonomic hierarchy cache
  product_file_size: 310167049
  product_url: https://zenodo.org/record/14640564/files/taxonCache.tsv.gz
- category: Product
  compression: gzip
  description: Tab-separated data citations
  format: tsv
  id: globi.citations.tsv
  name: GloBI data citations (TSV)
  product_file_size: 40815688
  product_url: https://zenodo.org/record/14640564/files/citations.tsv.gz
- category: Product
  compression: gzip
  description: Comma-separated data citations
  format: csv
  id: globi.citations.csv
  name: GloBI data citations (CSV)
  product_url: https://zenodo.org/record/14640564/files/citations.csv.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-09-23_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-24_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-09-24: No Content-Length
    header found'
- category: Product
  compression: gzip
  description: Tab-separated refuted species interactions (original unresolved names)
  format: tsv
  id: globi.refuted_verbatim_interactions.tsv
  name: GloBI refuted verbatim interactions (TSV)
  product_file_size: 2467674
  product_url: https://zenodo.org/record/14640564/files/refuted-verbatim-interactions.tsv.gz
- category: Product
  description: Field (column) definitions JSON endpoint
  format: json
  id: globi.fields.json
  name: interactionFields.json
  product_url: https://api.globalbioticinteractions.org/interactionFields?type=json
  warnings:
  - File was not able to be retrieved when checked on 2025-09-23_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-24_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-09-24: No Content-Length
    header found'
- category: Product
  description: Field (column) definitions CSV endpoint
  format: csv
  id: globi.fields.csv
  name: interactionFields.csv
  product_file_size: 15860
  product_url: https://api.globalbioticinteractions.org/interactionFields?type=csv
- category: DocumentationProduct
  description: About and methodological documentation, contribution guidelines, and
    references
  format: http
  id: globi.docs
  name: GloBI Documentation
  product_url: https://www.globalbioticinteractions.org/about
- category: Product
  description: Zenodo DOI badge pointing to latest archived release snapshot of integrated
    datasets
  format: http
  id: globi.release
  name: GloBI Archived Release (Zenodo)
  product_url: https://zenodo.org/badge/latestdoi/2478263
publications:
- doi: 10.1016/j.ecoinf.2014.08.005
  id: doi:10.1016/j.ecoinf.2014.08.005
  journal: Ecological Informatics
  title: 'Global Biotic Interactions: An open infrastructure to share and analyze
    species-interaction datasets'
  year: '2014'
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