---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.gdeltproject.org/
  label: The GDELT Project
creation_date: '2026-10-21T00:00:00Z'
description: The GDELT Project (Global Database of Events, Language, and Tone) is
  an open platform that monitors print, broadcast, and web news worldwide in over
  100 languages and renders it into structured, machine-readable data about global
  society. Its two core datasets are the Event Database, which records physical activities
  across 300+ CAMEO-coded categories with georeferencing and about 60 attributes per
  event, and the Global Knowledge Graph (GKG), which extracts people, organizations,
  locations, themes, and emotions to provide context and tone. The GDELT 2.0 data
  streams update every 15 minutes, are supported by Google Jigsaw, and are free and
  open.
domains:
- human populations
- natural language processing
- geographic information systems
- organisms
- literature
- environment
homepage_url: https://www.gdeltproject.org/
id: gdelt
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gdeltproject.org/about.html#termsofuse
  label: GDELT Terms of Use (free and open; attribution and link-back required)
name: GDELT Project (Global Database of Events, Language, and Tone)
products:
- category: Product
  description: Master file list indexing every 15-minute GDELT 2.0 Event, Mentions,
    and Global Knowledge Graph update file (size, MD5, URL); the payload files are
    tab-delimited despite a .CSV extension.
  format: tsv
  id: gdelt.raw-data
  name: GDELT 2.0 Raw Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gdelt
  product_file_size: 128756658
  product_url: https://data.gdeltproject.org/gdeltv2/masterfilelist.txt
  secondary_source:
  - relation_type: prov:used
    source: cameo
- category: ProgrammingInterface
  description: Live JSON API for full-text search across GDELT's global online news
    coverage, returning articles, timelines, and aggregations.
  format: http
  id: gdelt.doc-api
  is_public: true
  name: GDELT DOC 2.0 API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gdelt
  product_url: https://api.gdeltproject.org/api/v2/doc/doc
- category: Product
  description: The full GDELT datasets in Google BigQuery (project gdelt-bq), queryable
    with standard SQL and refreshed every 15 minutes.
  format: http
  id: gdelt.bigquery
  name: GDELT BigQuery Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gdelt
  product_url: https://console.cloud.google.com/bigquery?project=gdelt-bq
- category: DocumentationProduct
  description: Data format documentation, column headers, and codebooks for the Event
    Database and GKG, including the CAMEO code reference.
  format: http
  id: gdelt.documentation
  name: GDELT Documentation and Codebooks
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gdelt
  product_url: https://www.gdeltproject.org/data.html#documentation
synonyms:
- GDELT
- Global Knowledge Graph
- GKG
version: GDELT 2.0
---
# GDELT Project (Global Database of Events, Language, and Tone)

## Overview

The GDELT Project monitors world news across print, broadcast, and web in over 100 languages and turns it into structured data. Its Event Database records CAMEO-coded events with georeferencing, and its Global Knowledge Graph (GKG) connects people, organizations, locations, themes, and emotions across world news, updated every 15 minutes. It is supported by Google Jigsaw and is free and open.

## Access

- Raw data: the GDELT 2.0 master file list of Event, Mentions, and GKG update files (tab-delimited).
- DOC 2.0 API: full-text news search returning articles, timelines, and aggregations.
- BigQuery: the full datasets as queryable tables (project gdelt-bq).
- Documentation and codebooks, including the CAMEO code reference.

The Event Database is coded with the CAMEO (Conflict and Mediation Event Observations) taxonomy, recorded here as an upstream source.

## Citation

Leetaru K, Schrodt PA. GDELT: Global Data on Events, Location, and Tone, 1979–2012. Paper presented at the International Studies Association (ISA) Annual Convention, 2013 (no DOI).