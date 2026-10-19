---
activity_status: inactive
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://joint-research-centre.ec.europa.eu/eu-reference-laboratory-alternatives-animal-testing-eurl-ecvam_en
  label: EU Reference Laboratory for Alternatives to Animal Testing (EURL ECVAM),
    European Commission Joint Research Centre (JRC)
creation_date: '2026-10-19T00:00:00Z'
description: The JRC QSAR Model Database is an inventory of (Q)SAR models submitted
  to the EU Reference Laboratory for Alternatives to Animal Testing (EURL ECVAM) at
  the European Commission Joint Research Centre (JRC), each documented in the harmonised
  QSAR Model Reporting Format (QMRF), which is structured according to the OECD (Q)SAR
  validation principles. It was intended to help identify valid (Q)SARs for regulatory
  use, particularly under REACH. The database is now a historical archive published
  as a static dataset in the JRC Data Catalogue; its most recent QMRF updates date
  from 2019.
domains:
- toxicology
- chemistry and biochemistry
- cheminformatics
homepage_url: https://data.jrc.ec.europa.eu/dataset/e4ef8d13-d743-4524-a6eb-80e18b58cba4
id: jrc-qsar-model-database
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: JRC QSAR Model Database
products:
- category: GraphicalInterface
  description: Static browsable index of the QMRF documents in the JRC QSAR Model
    Database, listing QMRF number, model title, endpoint, and last update date, with
    links to each QMRF as PDF and XML.
  format: http
  id: jrc-qsar-model-database.index
  name: JRC QSAR Model Database Index
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jrc-qsar-model-database
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/QSARDB/LATEST/qsardb.html
- category: Product
  description: Individual QMRF (QSAR Model Reporting Format) documents in XML, one
    per model, as distributed in the JRC open data repository.
  format: xml
  id: jrc-qsar-model-database.qmrf-xml
  name: JRC QSAR Model Database QMRF XML Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jrc-qsar-model-database
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/QSARDB/LATEST/XML/
- category: Product
  compression: zip
  description: Complete archive of the JRC QSAR Model Database (QMRF documents in
    PDF and XML with attachments) for download.
  format: mixed
  id: jrc-qsar-model-database.download
  name: JRC QSAR Model Database Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jrc-qsar-model-database
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/QSARDB/LATEST/qsardb.zip
synonyms:
- QMRF Inventory
- JRC QSAR Model Database (QMRF Inventory)
---
# JRC QSAR Model Database

## Overview

The JRC QSAR Model Database is an inventory of quantitative structure-activity relationship ((Q)SAR) models maintained by the EU Reference Laboratory for Alternatives to Animal Testing (EURL ECVAM) at the European Commission Joint Research Centre (JRC). Each model is described in a QSAR Model Reporting Format (QMRF) document, a harmonised template for summarising key information on a (Q)SAR model, including the results of any validation studies, organised according to the OECD (Q)SAR validation principles. The database was intended to help identify valid (Q)SARs for regulatory purposes, especially under the EU REACH Regulation. Inclusion of a model does not imply endorsement of its validity by the JRC.

The former online application (qsardb.jrc.ec.europa.eu) now redirects to the JRC Data Catalogue, and the content is distributed as a static historical dataset (released in 2020) in the JRC open data repository.

## Data Content

- About 150 QMRF documents, each with a QMRF number, model title, endpoint, and last update date.
- Endpoints span human health and environmental properties, including carcinogenicity, in vitro mutagenicity, acute fish toxicity, and abiotic degradation / persistence.
- QMRFs are provided as PDF and XML, with supplementary attachments where available.

## Access

- JRC Data Catalogue entry: https://data.jrc.ec.europa.eu/dataset/e4ef8d13-d743-4524-a6eb-80e18b58cba4
- Static index: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/QSARDB/LATEST/qsardb.html
- Full archive: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EURL-ECVAM/datasets/QSARDB/LATEST/qsardb.zip

## License

The dataset is (c) European Union and licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence under the Commission's reuse policy (Commission Decision 2011/833/EU), per the copyright notice distributed with the dataset.
