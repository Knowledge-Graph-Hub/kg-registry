---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://genome.ucsc.edu/contacts.html
  label: UCSC Genome Browser Group
creation_date: '2026-06-17T00:00:00Z'
description: The UCSC Genome Browser is a web-based tool and data resource providing
  access to reference genome assemblies and an extensive collection of aligned
  annotation tracks for human and many other organisms. It supports interactive
  visualization, bulk data download, and programmatic access to genomic annotations.
domains:
- genomics
- biomedical
homepage_url: https://genome.ucsc.edu/
id: ucsc
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
license:
  id: https://genome.ucsc.edu/license/
  label: Free for academic, non-profit, and personal use; commercial use requires
    a license
name: UCSC Genome Browser
products:
- category: GraphicalInterface
  description: Interactive web browser for viewing reference genomes and annotation
    tracks.
  format: http
  id: ucsc.browser
  is_public: true
  name: UCSC Genome Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ucsc
  product_url: https://genome.ucsc.edu/
- category: GraphicalInterface
  description: Tool for extracting and downloading subsets of annotation track data.
  format: http
  id: ucsc.tablebrowser
  is_public: true
  name: UCSC Table Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ucsc
  product_url: https://genome.ucsc.edu/cgi-bin/hgTables
- category: Product
  description: Bulk downloads of genome assemblies and annotation tracks.
  format: mixed
  id: ucsc.downloads
  name: UCSC Genome Browser Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ucsc
  product_url: https://hgdownload.soe.ucsc.edu/downloads.html
- category: ProgrammingInterface
  description: REST API for programmatic access to genome assemblies and annotation
    tracks.
  format: http
  id: ucsc.api
  is_public: true
  name: UCSC Genome Browser REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ucsc
  product_url: https://api.genome.ucsc.edu/
publications:
- authors:
  - W. James Kent
  - Charles W. Sugnet
  - Terrence S. Furey
  - Krishna M. Roskin
  - Tom H. Pringle
  - Alan M. Zahler
  - and David Haussler
  doi: 10.1101/gr.229102
  id: https://doi.org/10.1101/gr.229102
  journal: Genome Research
  preferred: true
  title: The human genome browser at UCSC
  year: '2002'
---
# UCSC Genome Browser

The UCSC Genome Browser, developed and maintained at the University of California, Santa
Cruz, is one of the most widely used resources for the visualization and analysis of
genomic data. It provides reference genome assemblies for human and a large number of
other species, together with thousands of annotation tracks contributed by UCSC and the
wider community.

Key components include:

- The interactive Genome Browser for visualizing annotation tracks against a reference
  assembly
- The Table Browser for retrieving and filtering underlying track data
- Bulk downloads of assemblies and annotations via hgdownload
- A REST API for programmatic access

GeneCards integrates genomic annotation and mapping information from the UCSC Genome
Browser.
