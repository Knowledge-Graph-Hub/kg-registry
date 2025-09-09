---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cancer.sanger.ac.uk/cosmic/about
  label: COSMIC Team (Wellcome Sanger Institute)
description: COSMIC (Catalogue Of Somatic Mutations In Cancer) is a comprehensive resource for somatic mutations in human cancer. It curates, standardizes, and integrates mutation data across genes, cancer types, and samples, and provides access via a web portal and licensed downloads.
warnings:
- COSMIC data downloads for commercial users are provided by Qiagen.
domains:
- genomics
- biomedical
homepage_url: https://cancer.sanger.ac.uk/cosmic
id: cosmic
last_modified_date: '2025-09-09T00:00:00Z'
layout: resource_detail
license:
  id: https://cancer.sanger.ac.uk/cosmic/license
  label: COSMIC License
name: COSMIC
products:
- category: GraphicalInterface
  description: Web portal for exploring somatic mutations, gene pages, cancer types, and curated annotations
  format: http
  id: cosmic.portal
  name: COSMIC Portal
  original_source:
  - cosmic
  product_url: https://cancer.sanger.ac.uk/cosmic
- category: Product
  description: Top-level downloads page with links to COSMIC release files (registration/license required)
  format: http
  id: cosmic.downloads
  name: COSMIC Downloads
  original_source:
  - cosmic
  product_url: https://cancer.sanger.ac.uk/cosmic/download/cosmic
- category: DocumentationProduct
  description: COSMIC Knowledgebase overview and documentation pages
  format: http
  id: cosmic.kb.overview
  name: COSMIC-KB Portal overview
  original_source:
  - cosmic
  product_url: https://www.cosmickb.org/about/
---
# COSMIC

## Overview

COSMIC (Catalogue Of Somatic Mutations In Cancer) curates and integrates somatic mutation data across genes, cancer types, and samples. It provides searchable web pages and licensed bulk downloads for research and clinical interpretation.

## Access

- Portal: browse COSMIC at the main site
- Downloads: bulk release files (requires registration and acceptance of the COSMIC License)
- Login: register and authenticate to access downloads
- COSMIC‑KB: knowledge base overview and related content

## Citation & Licensing

Use of COSMIC data requires adherence to the COSMIC License. Please cite COSMIC according to guidance on the site.