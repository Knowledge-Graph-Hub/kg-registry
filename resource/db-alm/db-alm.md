---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: JRC-DBALM-CONTACT@ec.europa.eu
  - contact_type: url
    value: https://joint-research-centre.ec.europa.eu/eu-reference-laboratory-alternatives-animal-testing-eurl-ecvam_en
  label: EU Reference Laboratory for Alternatives to Animal Testing (EURL ECVAM),
    European Commission Joint Research Centre (JRC)
creation_date: '2026-10-19T00:00:00Z'
description: The EURL ECVAM DataBase service on ALternative Methods to animal experimentation
  (DB-ALM) is a collection of method summaries and standardised protocols for alternative
  methods in toxicology and biomedical science, maintained by the EU
  Reference Laboratory for Alternatives to Animal Testing (EURL ECVAM) at the European
  Commission Joint Research Centre (JRC). It covers methods submitted to EURL ECVAM
  for validation and methods identified through literature reviews and end users.
  The former interactive online database has been replaced by a versioned open dataset
  published through the JRC Data Catalogue, with a browsable static index of documents
  and a complete downloadable archive.
domains:
- toxicology
- biomedical
homepage_url: https://data.jrc.ec.europa.eu/dataset/b7597ada-148d-4560-9079-ab0a5539cad3
id: db-alm
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: DB-ALM (EURL ECVAM DataBase service on ALternative Methods to animal experimentation)
products:
- category: GraphicalInterface
  description: Browsable static index of DB-ALM documents (method summaries, protocols,
    and EU project descriptions), filterable by topic area, models and strategies,
    biological endpoints, experimental systems, and regulatory information, with
    links to the individual PDF documents.
  format: http
  id: db-alm.online
  name: DB-ALM Online Index
  original_source:
  - relation_type: prov:hadPrimarySource
    source: db-alm
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/DBALM/LATEST/online/dbalm.html
- category: Product
  compression: zip
  description: Complete downloadable DB-ALM dataset archive (latest release) from
    the JRC open data repository, containing the method summaries, protocols, and
    supporting documents for local use.
  format: mixed
  id: db-alm.download
  name: DB-ALM Dataset Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: db-alm
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/DBALM/LATEST/downloadable/
synonyms:
- DB-ALM
- DBALM
---
# DB-ALM (EURL ECVAM DataBase service on ALternative Methods to animal experimentation)

## Overview

DB-ALM is a collection of information on alternative methods maintained by the EU Reference Laboratory for Alternatives to Animal Testing (EURL ECVAM) at the European Commission Joint Research Centre (JRC). It was launched in its online form in 2006 and covers methods submitted to EURL ECVAM for validation as well as methods identified through literature reviews and from end users in specific application areas. The original interactive database application has been retired; DB-ALM content is now published as a versioned open dataset through the JRC Data Catalogue, and the legacy DB-ALM web address redirects to a static index of the latest release.

## Data Content

The latest release indexes about 370 documents:

- Method summaries (about 180) describing the scientific basis and status of alternative methods.
- Standardised protocols (about 186) with step-by-step procedures.
- A small number of EU-funded project descriptions.

Documents are annotated by topic area (for example eye irritation, hepatotoxicity and metabolism-mediated toxicity, developmental toxicity, systemic toxicity, basal cytotoxicity, skin irritation and corrosivity, neurotoxicity, genotoxicity, skin sensitisation), models and strategies, biological endpoints, experimental systems (cell lines, primary cells, tissue models), and regulatory information.

## Access

- JRC Data Catalogue entry: https://data.jrc.ec.europa.eu/dataset/b7597ada-148d-4560-9079-ab0a5539cad3
- Browsable index of the latest release: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/DBALM/LATEST/online/dbalm.html
- Full dataset download: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/DBALM/LATEST/downloadable/

## License

The dataset is (c) European Union and licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence under the Commission's reuse policy (Commission Decision 2011/833/EU), per the copyright notice distributed with the dataset.
