---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: NASA GeneLab / Open Science Data Repository (NASA Ames Research Center)
  contact_details:
  - contact_type: url
    value: https://genelab.nasa.gov/
creation_date: '2026-07-01T00:00:00Z'
description: NASA's Open Science Data Repository (OSDR), which incorporates the GeneLab
  data system, is a public repository that hosts spaceflight and space-relevant biological
  and omics experiment data. It provides curated multi-omics datasets (including
  transcriptomics, epigenomics, proteomics, metabolomics, and amplicon/metagenomics)
  from spaceflight and ground-based analog studies, along with associated experimental
  metadata, and offers programmatic access to these data through its APIs.
domains:
- genomics
- biomedical
- biological systems
- organisms
homepage_url: https://osdr.nasa.gov/
id: nasa-osdr
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: https://genelab.nasa.gov/genelab-open-source-license
  label: NASA Open Data (U.S. Government work / public domain)
name: NASA Open Science Data Repository (OSDR) / GeneLab
products:
- category: GraphicalInterface
  description: Web-based data repository for browsing and downloading NASA OSDR/GeneLab
    spaceflight and space-relevant biological and omics study datasets and their metadata.
  format: http
  id: nasa-osdr.repository
  name: NASA OSDR Data Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nasa-osdr
  product_url: https://osdr.nasa.gov/bio/repo/
- category: ProgrammingInterface
  description: OSDR Biodata API providing programmatic access to NASA OSDR/GeneLab
    study metadata and omics data.
  format: http
  id: nasa-osdr.api
  name: NASA OSDR Biodata API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nasa-osdr
  product_url: https://visualization.osdr.nasa.gov/biodata/api/
publications:
- authors:
  - Daniel C Berrios
  - Jonathan Galazka
  - Kirill Grigorev
  - Samrawit Gebre
  - Sylvain V Costes
  doi: 10.1093/nar/gkaa887
  id: doi:10.1093/nar/gkaa887
  journal: Nucleic Acids Research
  title: 'NASA GeneLab: interfaces for the exploration of space omics data'
  year: '2021'
---
# NASA Open Science Data Repository (OSDR) / GeneLab

## Overview

The NASA Open Science Data Repository (OSDR) is a public data repository maintained
by NASA (at Ames Research Center) that hosts spaceflight and space-relevant biological
and omics experiment data. OSDR incorporates the GeneLab data system, NASA's platform
for space omics (transcriptomics, epigenomics, proteomics, metabolomics, and
amplicon/metagenomics) data from spaceflight missions and ground-based analog studies.

## Access

Datasets and their experimental metadata can be browsed and downloaded through the
OSDR web repository, and accessed programmatically through the OSDR Biodata API.
