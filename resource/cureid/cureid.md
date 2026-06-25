---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://ncats.nih.gov/
    label: National Center for Advancing Translational Sciences (NCATS)
creation_date: '2026-06-18T00:00:00Z'
description: CURE ID is a crowdsourcing platform and mobile/web app developed by the U.S. National Center for Advancing Translational Sciences (NCATS) at NIH in collaboration with the U.S. Food and Drug Administration (FDA). It allows clinicians around the world to report and share real-world clinical experiences treating difficult-to-treat and rare diseases, with an emphasis on novel uses of existing (off-label) drugs. The collected case reports and treatment outcomes form a repository intended to surface promising therapies and inform clinical research. CURE ID serves as an upstream ingest source for the Monarch/SRI Reference Knowledge Graph.
domains:
  - clinical
  - drug discovery
  - public health
homepage_url: https://cure.ncats.io/
id: cureid
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: CURE ID
products:
  - category: GraphicalInterface
    description: Web application for exploring and contributing crowdsourced real-world clinical treatment cases for difficult-to-treat and rare diseases, including off-label drug use.
    format: http
    id: cureid.app
    name: CURE ID Web App
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cureid
    product_url: https://cure.ncats.io/
  - category: GraphicalInterface
    description: Browseable interface for exploring diseases, treatments, and submitted clinical case reports within the CURE ID platform.
    format: http
    id: cureid.explore
    name: CURE ID Explore
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cureid
    product_url: https://cure.ncats.io/explore
  - category: DocumentationProduct
    description: About page describing the CURE ID initiative, its NCATS/FDA partnership, and how clinicians can participate.
    id: cureid.about
    name: CURE ID About
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cureid
    product_url: https://cure.ncats.io/about
---

# CURE ID

## Description

CURE ID is an NIH/NCATS and FDA crowdsourcing platform and app that lets clinicians worldwide report and share real-world clinical experiences treating difficult-to-treat and rare diseases. It focuses especially on novel, off-label uses of existing approved drugs, building a community-driven repository of case reports and treatment outcomes. These data are intended to help identify promising therapies and prioritize candidates for formal clinical research. CURE ID is used as an upstream ingest source for the Monarch/SRI Reference Knowledge Graph.

## Products

- **CURE ID Web App** (GraphicalInterface) — the main web/mobile application for contributing and exploring crowdsourced clinical treatment cases.
- **CURE ID Explore** (GraphicalInterface) — interface for browsing diseases, drugs, and submitted case reports.
- **CURE ID About** (DocumentationProduct) — overview of the initiative and the NCATS/FDA partnership.
