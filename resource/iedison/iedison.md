---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://contact.iedison.gov/
  label: National Institute of Standards and Technology (NIST) Technology Partnerships
    Office
creation_date: '2026-10-04T00:00:00Z'
description: iEdison (Interagency Edison) is the U.S. federal online reporting system
  that recipients of federal funding agreements use to report subject inventions,
  patents and utilization to the funding agency, as required by the Bayh-Dole Act
  and its implementing regulations. NIH built the original Edison system in 1995 and
  opened it to other agencies in 1997; NIST took over operation in 2022. Many agencies,
  including NIH, DOD components, EPA, USDA and NNSA, accept reports through it. Records
  are not public, but NIH RePORTER uses iEdison to link patents to NIH grants.
domains:
- research funding
homepage_url: https://www.nist.gov/iedison
id: iedison
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: iEdison
products:
- category: GraphicalInterface
  description: Web system, requiring an account, in which funding recipients and federal
    agencies create and manage invention, patent and utilization reports.
  format: http
  id: iedison.portal
  name: iEdison Web System
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iedison
  product_url: https://iedison.nist.gov/
- category: ProgrammingInterface
  description: RESTful JSON web services for creating, updating and querying invention,
    patent and utilization reports. Access is limited to registered agencies and awardee
    organizations with certificate-based authentication.
  format: http
  id: iedison.api
  name: iEdison API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iedison
  product_url: https://iedison.nist.gov/iedison/swagger.json
  repository: https://github.com/usnistgov/iEdison-API-Documentation
- category: DocumentationProduct
  description: Documentation for the current version of the iEdison invention, patent
    and utilization API.
  format: http
  id: iedison.api-docs
  name: iEdison API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iedison
  product_url: https://pages.nist.gov/iEdison-API-Documentation/
- category: Product
  description: Database of patents linked to NIH-funded research projects
  format: csv
  id: nihreporter.patents
  name: NIH-Funded Project Patents
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  - relation_type: prov:wasDerivedFrom
    source: iedison
  product_url: https://reporter.nih.gov/exporter/patents
synonyms:
- Interagency Edison
- Edison
---
# iEdison

iEdison (Interagency Edison) is the federal system for reporting inventions made with federal funding. Under the Bayh-Dole Act, grantees and contractors must disclose subject inventions, elect title, report patent filings and submit utilization reports to the agency that made the award. iEdison is where they do this.

NIH developed the system as Edison in 1995 and offered it to other agencies from 1997. Operation moved to the National Institute of Standards and Technology (NIST) in summer 2022, and agencies continue to join it.

## Access

iEdison records are confidential and the web system and API require registered accounts. The API uses certificate-based authentication. Public views of the data come through other resources: [NIH RePORTER](https://reporter.nih.gov/) uses iEdison, among other sources, to link patents to NIH-funded grants.