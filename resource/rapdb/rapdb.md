---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://rapdb.dna.affrc.go.jp/
  label: Rice Annotation Project / NARO
creation_date: '2026-06-18T00:00:00Z'
description: The Rice Annotation Project Database (RAP-DB) provides curated genome
  annotation for the rice species Oryza sativa (Nipponbare), built on the IRGSP-1.0
  reference assembly by the Rice Annotation Project together with the National
  Agriculture and Food Research Organization (NARO). It integrates gene structures,
  functional annotations, transcript and protein information, and supporting evidence
  through both an interactive web interface and bulk download files. A central
  resource is the RAP-MSU locus identifier mapping, which links RAP gene IDs to
  the corresponding MSU (Michigan State University) Rice Genome Annotation Project
  locus IDs. RAP-DB serves as the upstream primary source for eco-KG.
domains:
- genomics
- organisms
- agriculture
homepage_url: https://rapdb.dna.affrc.go.jp/
id: rapdb
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Rice Annotation Project Database
products:
- category: GraphicalInterface
  description: Interactive RAP-DB web portal for browsing and searching curated
    Oryza sativa genome annotation, gene structures, and functional information.
  format: http
  id: rapdb.portal
  name: RAP-DB Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rapdb
  product_url: https://rapdb.dna.affrc.go.jp/
- category: Product
  description: Bulk download area providing RAP-DB annotation files, including the
    RAP-MSU locus identifier mapping table and IRGSP-1.0-based gene annotation data.
  format: http
  id: rapdb.downloads
  name: RAP-DB Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rapdb
  product_url: https://rapdb.dna.affrc.go.jp/download/index.html
publications:
- authors:
  - Sakai H
  - Lee SS
  - Tanaka T
  - Numa H
  - Kim J
  - Kawahara Y
  - Wakimoto H
  - Yang CC
  - Iwamoto M
  - Abe T
  - Yamada Y
  - Muto A
  - Inokuchi H
  - Ikemura T
  - Matsumoto T
  - Sasaki T
  - Itoh T
  doi: 10.1093/pcp/pcs183
  id: https://www.ncbi.nlm.nih.gov/pubmed/23299411
  journal: Plant Cell Physiol
  preferred: true
  title: 'Rice Annotation Project Database (RAP-DB): an integrative and interactive
    database for rice genomics'
  year: '2013'
---
# Rice Annotation Project Database

## Overview

The Rice Annotation Project Database (RAP-DB) is a curated annotation resource for the rice genome (Oryza sativa, cultivar Nipponbare), built on the IRGSP-1.0 reference assembly. It is developed and maintained by the Rice Annotation Project in collaboration with the National Agriculture and Food Research Organization (NARO).

## Content

RAP-DB integrates gene structures, functional annotations, transcript and protein data, and supporting evidence, accessible through an interactive web interface and bulk download files. A key feature is the RAP-MSU mapping, which cross-references RAP locus identifiers with MSU (Michigan State University) Rice Genome Annotation Project locus IDs.

## Use in eco-KG

RAP-DB is an upstream primary source for eco-KG, contributing rice genome annotation and locus identifier mappings.
