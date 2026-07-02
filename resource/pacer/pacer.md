---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.uscourts.gov/
  label: Administrative Office of the U.S. Courts
creation_date: '2026-07-01T00:00:00Z'
description: PACER (Public Access to Court Electronic Records) is the U.S. federal
  judiciary's electronic public-access system for federal court case and docket records.
  Managed by the Administrative Office of the U.S. Courts, it provides case and docket
  information from U.S. district, bankruptcy, and appellate courts, including dockets,
  case summaries, and filed documents. Access is provided to the public for a per-page
  usage fee. PACER is the primary upstream source of federal court records used by
  downstream projects such as SCALES.
domains:
- general
homepage_url: https://pacer.uscourts.gov/
id: pacer
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: U.S. Government Work (public domain records; PACER access subject to per-page
    usage fees)
name: PACER (Public Access to Court Electronic Records)
products:
- category: Product
  description: The PACER Case Locator is the national index and access point for federal
    court case and docket records, allowing searches across U.S. district, bankruptcy,
    and appellate courts for dockets, case summaries, and filed documents. Access
    is subject to PACER per-page usage fees.
  format: http
  id: pacer.case-locator
  is_public: true
  name: PACER Case/Docket Records Access
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pacer
  product_url: https://pcl.uscourts.gov/pcl/index.jsf
---
# PACER (Public Access to Court Electronic Records)

## Overview

PACER (Public Access to Court Electronic Records) is the electronic public-access
service of the U.S. federal judiciary, managed by the Administrative Office of the
U.S. Courts. It provides case and docket information from U.S. federal district,
bankruptcy, and appellate courts.

## Data Content

- **Dockets**: Chronological records of filings and events for federal court cases.
- **Case summaries**: Party, filing-date, nature-of-suit, and disposition metadata.
- **Filed documents**: Court filings and opinions associated with cases.

## Access

Records are searched and retrieved through the PACER Case Locator and the individual
court CM/ECF systems. Public access is provided for a per-page usage fee set by the
Judicial Conference of the United States.

## Use in Knowledge Graphs

PACER is the primary upstream source of federal court records for the SCALES project,
which automatically downloads queries, dockets, and case summaries from PACER, then
organizes and enriches them for public analysis.

## License

Federal court records are works of the U.S. government and are generally in the
public domain, though access through PACER is subject to per-page usage fees.
