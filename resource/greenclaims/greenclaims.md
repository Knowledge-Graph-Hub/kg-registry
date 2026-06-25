---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: GreenClaims is a third-party-verified dataset of corporate environmental
  claims and greenwashing cases, compiled from reputable news sources and regulatory
  records such as advertising-standards (e.g., ASA) rulings. Each record pairs a company's
  environmental claim with documented greenwashing allegations, company descriptions,
  certificates, and source URLs. It was introduced in Mattia Fornasiero's work on
  greenwashing detection and is used by knowledge-graph frameworks such as EmeraldGraph
  and EmeraldMind for explainable greenwashing detection.
domains:
- environment
- public health
- literature
homepage_url: https://github.com/DizzyPanda1/GreenwashingDetectionDataset
id: greenclaims
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: GreenClaims
products:
- category: DataDump
  description: CSV dataset of company environmental claims, greenwashing accusations,
    company descriptions, environmental certificates, and source URLs, hosted in the
    GreenwashingDetectionDataset GitHub repository. No further commits have been pushed
    since September 2024.
  format: csv
  id: greenclaims.dataset
  name: Greenwashing Detection Dataset (GitHub)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: greenclaims
  product_url: https://github.com/DizzyPanda1/GreenwashingDetectionDataset
---

GreenClaims is the principal openly available dataset for greenwashing detection. It
collects third-party-verified environmental claims and greenwashing allegations drawn
from news coverage and regulatory bodies (such as advertising-standards rulings),
linking each claim to its supporting evidence and source. The dataset is small in
scale (on the order of dozens of curated claim cases) but is notable for its grounded,
human-verified labels.

The dataset was introduced in Mattia Fornasiero's 2024 work, *Exploring the
effectiveness of Large Language Models in greenwashing detection* (Erasmus University
thesis, https://thesis.eur.nl/pub/72537/). It is cited as a primary source by
knowledge-graph-augmented greenwashing-detection frameworks including EmeraldMind
(arXiv:2512.11506).
