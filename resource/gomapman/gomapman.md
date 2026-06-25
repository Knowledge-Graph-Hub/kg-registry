---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.nib.si/eng
    label: National Institute of Biology (NIB), Slovenia
creation_date: '2026-06-18T00:00:00Z'
description: >-
  GoMapMan is a manually curated, open database that integrates, consolidates,
  and visualizes plant gene functional annotations organized within the MapMan
  ontology, a hierarchical scheme of functional "bins" tailored to plant
  biology. It maps genes to MapMan bins across several crop and model plant
  species, including Arabidopsis, potato, and tomato, and harmonizes annotations
  drawn from multiple sources into a single consolidated, expert-reviewed
  resource. The portal provides interactive browsing and visualization of the
  ontology and gene-to-bin mappings, and its curated mappings are widely reused
  to annotate genes in plant systems-biology and transcriptomics analyses. It is
  an upstream source for the Stress Knowledge Map (SKM).
domains:
  - genomics
  - pathways
  - agriculture
  - systems biology
homepage_url: https://gomapman.nib.si/
id: gomapman
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: GoMapMan
products:
  - category: GraphicalInterface
    description: >-
      Web portal for browsing, searching, and visualizing the MapMan ontology
      and manually curated plant gene functional annotations across supported
      crop and model plant species.
    format: http
    id: gomapman.portal
    name: GoMapMan Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: gomapman
    product_url: https://gomapman.nib.si/
publications:
  - authors:
      - Ramsak Z
      - Baebler S
      - Rotter A
      - Korbar M
      - Mozetic I
      - Usadel B
      - Gruden K
    doi: 10.1093/nar/gkt1056
    id: https://www.ncbi.nlm.nih.gov/pubmed/24194592
    journal: Nucleic Acids Res
    preferred: true
    title: 'GoMapMan: integration, consolidation and visualization of plant gene annotations within the MapMan ontology'
    year: '2014'
---

## Description

GoMapMan is a manually curated database developed at the National Institute of
Biology (NIB) in Slovenia that integrates, consolidates, and visualizes plant
gene functional annotations within the MapMan ontology. The MapMan ontology
organizes gene functions into a hierarchy of plant-oriented functional "bins,"
and GoMapMan assigns genes to these bins for a range of crop and model plant
species, including Arabidopsis, potato, and tomato. By bringing together
annotations from multiple upstream sources and subjecting them to expert
curation, GoMapMan produces a harmonized, high-quality set of gene-to-function
mappings that can be browsed and visualized interactively through its web
portal. These curated mappings are reused to annotate genes in plant
systems-biology and transcriptomics workflows, and GoMapMan serves as an
upstream source for the Stress Knowledge Map (SKM).

## Products

- **GoMapMan Web Portal** — a graphical web interface for browsing, searching,
  and visualizing the MapMan ontology and the curated gene functional
  annotations across supported plant species.
