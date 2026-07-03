---
activity_status: active
category: KnowledgeGraph
collection:
  - ber
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://ufokn.com/"
      - contact_type: github
        value: "UFOKN"
    label: UF Open Knowledge Network (UF-OKN)
description: The Urban Flooding Open Knowledge Network (UF-OKN) is an informational infrastructure built with knowledge graphs to connect urban infrastructure with hydrologic forecasts, delivering actionable, real-time and historical flood-risk information as Linked Data for exploration and app development.
domains:
  - environment
homepage_url: https://ufokn.com/
id: "uf-okn"
last_modified_date: '2026-07-02T00:00:00Z'
layout: resource_detail
name: UF-OKN
repository: https://github.com/UFOKN/Knowledge-Graph
products:
  - category: GraphProduct
    description: The UF-OKN knowledge graph, published as Linked Data (RDF/Turtle), that
      links urban infrastructure features to hydrologic forecasts so that flood risk can
      be explored as connected data. It relates OpenStreetMap building footprints and road
      networks to their nearest river (via the NHD/NHDPlus reach network) and to the
      streamflow forecasts from the NOAA National Water Model that would inundate them.
    format: ttl
    id: "uf-okn.graph"
    name: UF-OKN Knowledge Graph
    original_source:
      - source: uf-okn
        relation_type: prov:hadPrimarySource
      - source: noaa-nwm
        relation_type: prov:hadPrimarySource
      - source: openstreetmap
        relation_type: prov:hadPrimarySource
      - source: usgs-nhd
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/UFOKN/Knowledge-Graph
  - category: GraphicalInterface
    description: Public UF-OKN web portal for project information and application context.
    format: http
    id: "uf-okn.portal"
    name: UF-OKN Portal
    original_source:
      - source: uf-okn
        relation_type: prov:hadPrimarySource
    product_url: https://ufokn.com/
  - category: ProcessProduct
    description: Source repository for UF-OKN knowledge graph construction and maintenance.
    format: http
    id: "uf-okn.code"
    name: UF-OKN Source Code
    original_source:
      - source: uf-okn
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/UFOKN/Knowledge-Graph
creation_date: '2025-08-07T00:00:00Z'
---

UF-OKN

## Overview

UF-OKN links open geospatial infrastructure data to hydrologic forecasts so that flood risk can be explored as linked data rather than as disconnected maps and files.

Its project materials emphasize Risk-Point modeling, urban-systems interdependence, and the combination of real-time, forecast, and historical flood information to support planning, response, and application development.

## Automated Evaluation

- View the automated evaluation: [uf-okn automated evaluation](uf-okn_eval_automated.html)
