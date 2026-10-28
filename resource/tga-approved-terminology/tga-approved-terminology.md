---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.tga.gov.au/
  label: Therapeutic Goods Administration (Australia)
creation_date: '2026-10-19T00:00:00Z'
description: TGA Approved Terminology for Therapeutic Goods is the Australian Therapeutic
  Goods Administration's official, standardized vocabulary for describing therapeutic
  goods in applications for the Australian Register of Therapeutic Goods (ARTG) and
  on product labels. It defines Australian Approved Names for ingredients (active
  ingredients, excipients, components, and cells and tissues) together with code-table
  terms for presentation attributes such as dosage forms, routes of administration,
  and containers. The authoritative lists are maintained by the TGA and published
  through TGA Business Services. (The TGA website blocks automated requests, so the
  homepage URL was confirmed via web search rather than a direct fetch.)
domains:
- pharmacology
- natural products
- chemistry and biochemistry
homepage_url: https://www.tga.gov.au/publication/tga-approved-terminology-therapeutic-goods
id: tga-approved-terminology
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://www.tga.gov.au/about/website-copyright
  label: © Commonwealth of Australia (TGA website copyright; reuse by permission)
name: TGA Approved Terminology for Therapeutic Goods
products:
- category: GraphicalInterface
  description: Web application for searching NHPID ingredients by name or CAS number
    and role (homeopathic, medicinal, non-medicinal, non-NHP, component), and for
    searching the NHP controlled vocabularies by category. Controlled vocabulary terms
    for dosage forms, routes of administration, and units are adapted from ICH M5
    lists, and ingredient naming conventions from the TGA approved terminology.
  format: http
  id: nhpid.web
  name: NHPID Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhpid
  product_url: https://webprod.hc-sc.gc.ca/nhpid-bdipsn/?lang=eng
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: tga-approved-terminology
  - relation_type: prov:wasDerivedFrom
    source: ich-m5
- category: DocumentationProduct
  description: Official TGA publication landing page for the approved terminology
    guidance.
  format: http
  id: tga-approved-terminology.publication
  name: TGA Approved Terminology Publication Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tga-approved-terminology
  product_url: https://www.tga.gov.au/publication/tga-approved-terminology-therapeutic-goods
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-28: Timeout connecting
    to URL'
- category: DocumentationProduct
  description: Downloadable guidance document describing approved ingredient naming
    and presentation terminology.
  format: pdf
  id: tga-approved-terminology.guidance-pdf
  name: TGA Approved Terminology Guidance (PDF)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tga-approved-terminology
  product_url: https://www.tga.gov.au/sites/default/files/2024-10/tga-approved-terminology-therapeutic-goods.pdf
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-28: Timeout connecting
    to URL'
- category: GraphicalInterface
  description: TGA page directing users to the Ingredients Table and Code Tables (dosage
    forms, routes, containers) in TGA Business Services.
  format: http
  id: tga-approved-terminology.where-to-find
  name: Where to Find Approved Terminology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tga-approved-terminology
  product_url: https://www.tga.gov.au/where-find-approved-terminology
---
# TGA Approved Terminology for Therapeutic Goods

## Overview

This is the Therapeutic Goods Administration's official controlled terminology for describing therapeutic goods in Australia. It sets Australian Approved Names for ingredients and the code-table terms for presentation attributes — dosage forms, routes of administration, and containers — used in ARTG applications and on product labels.

## Access

- Publication page and downloadable guidance document (PDF).
- Ingredients Table and Code Tables via TGA Business Services (reached through the "Where to find approved terminology" page).

Note: the TGA website blocks automated requests, so URLs here were confirmed by web search rather than direct fetch and may warrant a manual check.

## Citation

Therapeutic Goods Administration. TGA Approved Terminology for Therapeutic Goods. Australian Government Department of Health, Disability and Ageing. https://www.tga.gov.au/publication/tga-approved-terminology-therapeutic-goods