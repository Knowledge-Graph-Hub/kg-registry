---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/support/intact
  label: IntAct Team (EMBL-EBI)
description: IntAct is an open, curated molecular interaction database maintained at EMBL‑EBI. It aggregates experimentally-derived interaction evidence from literature curation and direct submissions, and distributes data in PSI‑MI XML and MITAB formats along with curated datasets and documentation.
domains:
- proteomics
- systems biology
homepage_url: https://www.ebi.ac.uk/intact/home
id: intact
last_modified_date: '2025-09-09T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: IntAct
products:
- category: GraphicalInterface
  description: Web portal for browsing, searching, and accessing IntAct molecular interaction data
  format: http
  id: intact.portal
  name: IntAct Portal
  original_source:
  - intact
  product_url: https://www.ebi.ac.uk/intact/home
- category: Product
  description: IntAct data in PSI-MI XML 2.5 format (directory)
  format: psi_mi_xml
  id: intact.ftp.psi25
  name: IntAct PSI-MI XML 2.5
  original_source:
  - intact
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psi25/
- category: Product
  description: IntAct data in PSI-MI XML 3.0 format (directory)
  format: psi_mi_xml
  id: intact.ftp.psi30
  name: IntAct PSI-MI XML 3.0
  original_source:
  - intact
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psi30/
- category: Product
  description: IntAct data in PSI-MI MITAB format (directory)
  format: psi_mi_mitab
  id: intact.ftp.psimitab
  name: IntAct PSI-MI MITAB 2.7
  original_source:
  - intact
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/
- category: Product
  description: Entire MITAB export of the database as a single archive (intact.zip)
  format: psi_mi_mitab
  id: intact.ftp.psimitab.all
  name: IntAct MITAB Archive
  original_source:
  - intact
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/intact.zip
- category: Product
  description: Curated and computational datasets (disease-, method-, and species-specific) with per-dataset downloads
  format: http
  id: intact.datasets
  name: IntAct Datasets
  original_source:
  - intact
  product_url: https://www.ebi.ac.uk/intact/download/datasets
- category: DocumentationProduct
  description: User guide and documentation for search, exports, data sources, and submission
  format: http
  id: intact.docs.user-guide
  name: IntAct User Guide
  original_source:
  - intact
  product_url: https://www.ebi.ac.uk/intact/documentation/user-guide
---
# IntAct

## Overview

IntAct is a curated molecular interaction database, aggregating experimental evidence from the literature and direct submissions and distributing data in PSI‑MI XML and MITAB formats. It is part of the IMEx consortium and a Global Core Biodata Resource.

## Access

- Portal: browse and search interactions via the IntAct web interface
- FTP: bulk downloads in PSI‑MI XML (2.5, 3.0) and MITAB (2.7)
- Datasets: curated and computational datasets with themed collections
- Documentation: user guide covering data sources, formats, export, and submission

## Citation

Please cite IntAct and any specific datasets used, and refer to the Apache 2.0 license terms for data reuse.