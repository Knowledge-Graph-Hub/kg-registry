---
id: maude
name: MAUDE (Manufacturer and User Facility Device Experience)
description: The U.S. FDA database of medical device adverse event reports. It houses
  mandatory reports submitted by device manufacturers, importers, and device user
  facilities, along with voluntary reports from healthcare professionals, patients,
  and consumers. The data are searchable through a public web interface and are also
  released as downloadable data files and via an API.
activity_status: active
category: DataSource
homepage_url: https://www.fda.gov/medical-devices/mandatory-reporting-requirements-manufacturers-importers-and-device-user-facilities/manufacturer-and-user-facility-device-experience-database-maude
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (Public Domain)
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.fda.gov/about-fda/fda-organization/center-devices-and-radiological-health
  label: U.S. Food and Drug Administration, Center for Devices and Radiological Health
products:
- id: maude.data
  name: MAUDE Database and Downloadable Data Files
  description: The MAUDE medical device adverse event reports, accessible through
    the searchable web database and as downloadable data files, including via the
    openFDA device adverse event API endpoint.
  category: Product
  format: http
  product_url: https://open.fda.gov/apis/device/event/
  original_source:
  - source: maude
    relation_type: prov:hadPrimarySource
domains:
- clinical
- biomedical
layout: resource_detail
creation_date: '2026-07-01T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
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
