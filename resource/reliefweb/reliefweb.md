---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://reliefweb.int/"
    label: UN OCHA / ReliefWeb
creation_date: '2026-06-18T00:00:00Z'
description: ReliefWeb is the humanitarian information service operated by the United Nations Office for the Coordination of Humanitarian Affairs (UN OCHA). It aggregates situation reports, disaster and crisis updates, maps, infographics, and humanitarian job and training announcements from thousands of trusted sources worldwide. Its content is openly accessible through the ReliefWeb website and a public REST API covering reports, disasters, jobs, and training records. ReliefWeb is an upstream data source for the KnowWhereGraph project.
domains:
  - public health
  - environment
  - general
homepage_url: https://reliefweb.int/
id: reliefweb
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: "https://creativecommons.org/licenses/by/4.0/"
  label: CC BY 4.0
name: ReliefWeb
products:
  - category: GraphicalInterface
    description: The ReliefWeb website, providing browsable and searchable access to humanitarian situation reports, disaster updates, maps, infographics, jobs, and training announcements.
    format: http
    id: "reliefweb.site"
    is_public: true
    name: ReliefWeb Website
    product_url: https://reliefweb.int/
    original_source:
      - source: reliefweb
        relation_type: prov:hadPrimarySource
  - category: ProgrammingInterface
    description: The ReliefWeb API, a public REST interface exposing all ReliefWeb content (reports, disasters, jobs, training, and reference data) as JSON, with full-text search and faceted filtering. Requires a registered appname; limited to 1,000 entries per call and 1,000 calls per day at no cost.
    format: http
    id: "reliefweb.api"
    is_public: true
    name: ReliefWeb API
    product_url: https://api.reliefweb.int/v2/
    original_source:
      - source: reliefweb
        relation_type: prov:hadPrimarySource
---

# ReliefWeb

## Overview

ReliefWeb is the leading humanitarian information source on global crises and disasters, operated by the United Nations Office for the Coordination of Humanitarian Affairs (UN OCHA). It has been collecting and curating humanitarian content since 1996, drawing from thousands of governments, UN agencies, non-governmental organizations, research institutions, and media outlets.

## Content

ReliefWeb publishes situation reports, news and press releases, analyses and evaluations, maps and infographics, and a calendar of humanitarian jobs and training opportunities. Content spans natural disasters, complex emergencies, public health crises, and ongoing humanitarian operations across all regions of the world.

## Data Access

Content is available through the ReliefWeb website and the ReliefWeb API. The API is a REST service based at `https://api.reliefweb.int/v2/` that returns JSON and provides endpoints for reports, disasters, jobs, training, and supporting reference taxonomies. Use of the API is free but requires registering an application name (`appname`) and is subject to rate limits of 1,000 entries per call and 1,000 calls per day. Most ReliefWeb content is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license, though the intellectual property rights of original contributing sources must be respected.

## Relationship to KnowWhereGraph

ReliefWeb serves as an upstream data source for the KnowWhereGraph project, contributing humanitarian and disaster information used in geospatial knowledge integration.
