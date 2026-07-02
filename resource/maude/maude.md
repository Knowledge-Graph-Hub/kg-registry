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
homepage_url: https://www.fda.gov/medical-devices/mandatory-reporting-requirements-manufacturers-importers-and-device-user-facilities/manufacturer-and-user-facility-device-experience-database-maude
id: maude
last_modified_date: '2026-07-01T00:00:00Z'
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