---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ntp.niehs.nih.gov/
  label: National Toxicology Program (NTP), NIEHS Division of Translational Toxicology
creation_date: '2026-10-27T00:00:00Z'
description: The National Toxicology Program (NTP) is a U.S. interagency program,
  established in 1978 and headquartered at the National Institute of Environmental
  Health Sciences (NIEHS), that evaluates the toxicity and carcinogenicity of chemicals
  and other agents of public health concern. NTP research and testing is carried out
  by the NIEHS Division of Translational Toxicology (DTT). NTP conducts rodent toxicology
  and carcinogenicity studies, genetic toxicity testing, and literature-based health
  effects assessments, and publishes the congressionally mandated Report on Carcinogens.
  Individual animal data and summaries from more than 2,000 NTP studies are distributed
  through the Chemical Effects in Biological Systems (CEBS) database, and NTP also
  provides historical control data from its rodent studies and, through NICEATM, data
  on alternative test methods.
domains:
- toxicology
- environmental exposure
- environment
- cancer
- biomedical
- public health
homepage_url: https://ntp.niehs.nih.gov/
id: ntp
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: National Toxicology Program (NTP)
products:
- category: DocumentationProduct
  description: NTP Technical Reports and other NTP report series describing the design
    and results of NTP toxicology and carcinogenicity studies.
  format: http
  id: ntp.reports
  name: NTP Technical Reports
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://ntp.niehs.nih.gov/publications/reports
- category: DocumentationProduct
  description: The 15th Report on Carcinogens, the congressionally mandated listing
    of substances known or reasonably anticipated to be human carcinogens, with substance
    profiles for each listing.
  format: http
  id: ntp.roc
  name: Report on Carcinogens (15th edition)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://ntp.niehs.nih.gov/research/assessments/cancer/roc
- category: GraphicalInterface
  description: Data exploration dashboard for the substances listed in the 15th Report
    on Carcinogens.
  format: http
  id: ntp.roc-data
  name: Report on Carcinogens Data Exploration Dashboard
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://ntp.niehs.nih.gov/research/assessments/cancer/roc/data
- category: Product
  description: Historical control data on growth, survival, and tumor incidence in
    control rodents from NTP studies, organized by study type, species, strain, and
    route.
  format: http
  id: ntp.historical-controls
  name: NTP Historical Controls
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://ntp.niehs.nih.gov/data/controls
- category: GraphicalInterface
  description: Web interface for searching and browsing CEBS toxicology data
  format: http
  id: cebs.web
  name: CEBS Search Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://cebs.niehs.nih.gov/cebs/search
- category: GraphicalInterface
  description: DTT Data Collections Guided Search, providing filterable, downloadable
    tables for curated NIEHS Division of Translational Toxicology (DTT) data collections
    (e.g., clinical chemistry, hematology, and other individual animal data; treatment-related
    findings; DTT publications; and a Tox21 p53 activator dataset)
  format: http
  id: cebs.dtt-data-collections
  name: DTT Data Collections Guided Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:hadPrimarySource
    source: tox21
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://cebs-ext.niehs.nih.gov/datasets
- category: Product
  description: Toxicology study data from NTP and other programs
  format: mixed
  id: cebs.data
  name: CEBS Study Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://cebs.niehs.nih.gov/cebs/
- category: ProgrammingInterface
  connection_url: https://manticore.niehs.nih.gov/cebsapi/v1
  description: Programmatic API access to CEBS data, documented by the CEBS API user
    help. Note that as of October 2026 the documented base URL (https://manticore.niehs.nih.gov/cebsapi/v1)
    and example requests returned HTTP 404.
  format: http
  id: cebs.api
  name: CEBS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cebs
  - relation_type: prov:hadPrimarySource
    source: ntp
  product_url: https://tools.niehs.nih.gov/cebs3/support/assets/docs/CEBS_API-User-Help.pdf
synonyms:
- NTP
- NIEHS Division of Translational Toxicology
- DTT
---
# National Toxicology Program (NTP)

## Overview

The National Toxicology Program is a U.S. interagency program, established in 1978 and headquartered at NIEHS, that evaluates the health effects of chemicals and other agents of public health concern. Its research and testing is carried out by the NIEHS Division of Translational Toxicology (DTT), and includes rodent toxicology and carcinogenicity studies, genetic toxicity testing, and literature-based health effects assessments.

## Access

- NTP Technical Reports and other report series.
- The 15th Report on Carcinogens and its data exploration dashboard.
- Historical control data from NTP rodent studies.
- Individual animal data and summaries from over 2,000 NTP studies, distributed through the Chemical Effects in Biological Systems (CEBS) database.
- Alternative test method data through NICEATM and the Integrated Chemical Environment (ICE).

NTP content is a work of the U.S. federal government and is in the public domain.
