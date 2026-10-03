---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.fda.gov/about-fda/fda-organization/center-devices-and-radiological-health
  label: U.S. Food and Drug Administration, Center for Devices and Radiological Health
creation_date: '2026-07-01T00:00:00Z'
description: The U.S. FDA database of medical device adverse event reports. It houses
  mandatory reports submitted by device manufacturers, importers, and device user
  facilities, along with voluntary reports from healthcare professionals, patients,
  and consumers. The data are searchable through a public web interface and are also
  released as downloadable data files and via an API.
domains:
- clinical
- biomedical
- pharmacology
- pharmacovigilance
homepage_url: https://www.fda.gov/medical-devices/mandatory-reporting-requirements-manufacturers-importers-and-device-user-facilities/about-manufacturer-and-user-facility-device-experience-maude-database
id: maude
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (Public Domain)
name: MAUDE (Manufacturer and User Facility Device Experience)
products:
- category: Product
  description: The MAUDE medical device adverse event reports, accessible through
    the searchable web database and as downloadable data files, including via the
    openFDA device adverse event API endpoint.
  format: http
  id: maude.data
  name: MAUDE Database and Downloadable Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: openfda
  product_url: https://open.fda.gov/apis/device/event/
- category: GraphProduct
  description: RDF knowledge graph constructed from FDA MAUDE medical-device adverse
    event reports using standardized FDA product codes.
  format: ttl
  id: maudekg.graph
  name: FDA MAUDE Adverse Event Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maudekg
  - relation_type: prov:wasDerivedFrom
    source: maude
  product_url: https://frink.renci.org/maudekg
- category: ProgrammingInterface
  connection_url: https://api.fda.gov/
  description: JSON REST APIs (Elasticsearch query syntax) for FDA drug, device, food,
    animal and veterinary, cosmetic, tobacco and other datasets, including drug adverse
    events (FAERS), device adverse events (MAUDE), the National Drug Code directory,
    the Orange Book, UNII substance data, labeling, recalls and enforcement reports.
  format: http
  id: openfda.apis
  is_public: true
  name: openFDA APIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://open.fda.gov/apis/
- category: Product
  compression: zip
  description: Bulk downloads of every openFDA endpoint as zipped JSON files, split
    into partitions for large datasets such as drug adverse events (FAERS) and device
    adverse events (MAUDE), with a machine-readable manifest at https://api.fda.gov/download.json
    listing each endpoint's export date and file partitions.
  format: json
  id: openfda.downloads
  name: openFDA Bulk Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://open.fda.gov/data/downloads/
---
# MAUDE (Manufacturer and User Facility Device Experience)

## Description

MAUDE is the U.S. Food and Drug Administration's database of medical device adverse
event reports. It captures mandatory reports from device manufacturers, importers,
and device user facilities, together with voluntary reports from healthcare
professionals, patients, and consumers.

The database supports post-market surveillance of medical devices by documenting
suspected device-associated deaths, serious injuries, and malfunctions. Records are
searchable through the FDA's public web interface and are also distributed as
downloadable data files and through the openFDA device adverse event API.