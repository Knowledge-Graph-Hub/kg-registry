---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://epd.expasy.org/epd/
  label: Swiss Institute of Bioinformatics
creation_date: '2026-06-17T00:00:00Z'
description: The Eukaryotic Promoter Database (EPD) is an annotated, non-redundant
  collection of experimentally validated eukaryotic POL II promoters. Its EPDnew
  components provide high-quality, automatically derived promoter collections for
  selected organisms, with tools for promoter analysis.
domains:
- genomics
- systems biology
homepage_url: https://epd.expasy.org/epd/
id: epd
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: Eukaryotic Promoter Database
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching experimentally validated
    eukaryotic promoters.
  format: http
  id: epd.site
  is_public: true
  name: EPD Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epd
  product_url: https://epd.expasy.org/epd/
- category: Product
  description: FTP archive of EPDnew promoter collections and annotation files.
  format: mixed
  id: epd.downloads
  name: EPD Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epd
  product_url: https://epd.expasy.org/ftp/epdnew/
publications:
- authors:
  - René Dreos
  - Giovanna Ambrosini
  - Rouayda Cavin Périer
  - Philipp Bucher
  doi: 10.1093/nar/gku1111
  id: https://doi.org/10.1093/nar/gku1111
  journal: Nucleic Acids Research
  preferred: true
  title: 'The eukaryotic promoter database: expansion of EPDnew and new promoter analysis tools'
  year: '2015'
---
# Eukaryotic Promoter Database

The Eukaryotic Promoter Database (EPD) is a curated, non-redundant collection of
experimentally characterized eukaryotic RNA polymerase II promoters, hosted at the Swiss
Institute of Bioinformatics. Its EPDnew components extend the original database with
high-confidence, automatically derived promoter collections for selected model organisms.

Content and features include:

- Experimentally validated transcription start sites and promoter regions
- EPDnew high-quality promoter collections for human and other organisms
- Promoter analysis and visualization tools
- FTP downloads of promoter collections and annotations

GeneCards integrates promoter annotations from the Eukaryotic Promoter Database.
