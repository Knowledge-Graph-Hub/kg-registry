---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.era.nih.gov/need-help
  label: NIH Office of Extramural Research, eRA Service Desk
creation_date: '2026-10-04T00:00:00Z'
description: eRA (electronic Research Administration) is the NIH system for managing
  the grants lifecycle, from application receipt and peer review through award, post-award
  reporting and closeout, for NIH and other federal agencies. It combines IMPAC II,
  the internal system of record for NIH grant applications and awards since 2002,
  with eRA Commons, the external interface for applicants, recipients and reviewers.
  eRA itself is access-controlled, but its data feed public resources such as NIH
  RePORTER and the ExPORTER bulk files.
domains:
- research funding
- biomedical
homepage_url: https://www.era.nih.gov/
id: nih-era
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: NIH eRA (electronic Research Administration)
products:
- category: GraphicalInterface
  description: eRA Commons, the login-protected web interface where applicants, grant
    recipients, signing officials and reviewers track applications, view review outcomes
    and notices of award, and submit progress reports, invention reports and closeout
    documents.
  format: http
  id: nih-era.commons
  name: eRA Commons
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nih-era
  product_url: https://public.era.nih.gov/commons/
- category: GraphicalInterface
  description: ASSIST (Application Submission System and Interface for Submission
    Tracking), the login-protected eRA module for preparing and submitting grant applications
    to NIH and other agencies.
  format: http
  id: nih-era.assist
  name: eRA ASSIST
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nih-era
  product_url: https://public.era.nih.gov/assist/
- category: DocumentationProduct
  description: eRA help and tutorials, including online help for eRA Commons, ASSIST
    and the other eRA modules, video tutorials and FAQs.
  format: http
  id: nih-era.help
  name: eRA Help and Tutorials
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nih-era
  product_url: https://www.era.nih.gov/help-tutorials
- category: DocumentationProduct
  description: Description of the eRA reporting and analytics modules, including the
    public RePORT and RePORTER tools and the internal QVR, SPIRES and iRePORT modules
    built on IMPAC II data.
  format: http
  id: nih-era.reporting-docs
  name: eRA Reporting and Analytics Modules
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nih-era
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  product_url: https://www.era.nih.gov/about-era/services-for-agency-staff/reporting-analytics
- category: GraphicalInterface
  description: Web-based search interface for exploring NIH-funded research projects
    with advanced search capabilities
  format: http
  id: nihreporter.portal
  name: NIH Reporter Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/
- category: Product
  compression: zip
  description: Bulk download of NIH research project data in structured format
  format: csv
  id: nihreporter.projects
  name: NIH Reporter Exporter Projects
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/projects
- category: ProgrammingInterface
  description: Public REST API (no key required) returning JSON for searching projects
    (v2 projects endpoint) and project-linked publications
  format: http
  id: nihreporter.api
  name: NIH Reporter API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://api.reporter.nih.gov/
- category: Product
  compression: zip
  description: Database of abstracts linked to NIH-funded research projects
  format: csv
  id: nihreporter.abstracts
  name: NIH-Funded Project Abstracts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/abstracts
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
- category: Product
  description: Database of clinical studies linked to NIH-funded research projects
  format: csv
  id: nihreporter.clinicalstudies
  name: NIH-Funded Project Clinical Studies
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/clinicalstudies
- category: Product
  compression: zip
  description: Database of publications linked to NIH-funded research projects
  format: csv
  id: nihreporter.publications
  name: NIH-Funded Publications Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/publications
- category: Product
  description: Database of publication link tables for NIH-funded research projects
  format: csv
  id: nihreporter.linktables
  name: NIH-Funded Publications Link Tables
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/linktables
- category: Product
  compression: zip
  description: Legacy CRISP (Computer Retrieval of Information on Scientific Projects)
    project and abstract data for fiscal years 1970 to 2009, in CSV and XML.
  format: csv
  id: nihreporter.crisp
  name: NIH Reporter Legacy CRISP Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:wasDerivedFrom
    source: nih-era
  product_url: https://reporter.nih.gov/exporter/crisp
synonyms:
- eRA
- NIH eRA
- electronic Research Administration
- IMPAC II
- eRA Commons
---
# NIH eRA (electronic Research Administration)

eRA is the electronic Research Administration system of the NIH Office of Extramural Research. It supports the full grants lifecycle for NIH and partner federal agencies: funding opportunities, application submission, receipt and referral, peer review, award, post-award management and closeout. eRA describes itself as the largest federal grants management system, handling over half of the grant applications received by Grants.gov.

## History and components

eRA grew out of IMPAC (Information for Management, Planning, Analysis and Coordination), begun in the late 1960s to track NIH research applications from receipt to closeout. IMPAC I, a COBOL mainframe system, was replaced by IMPAC II, which became the system of record for application records in 2002. eRA Commons was developed in 1999 and brought into the Office of Extramural Research in 2001, and eRA was formed by combining IMPAC II and Commons.

- **IMPAC II**: the internal modules and database used by NIH and partner agency staff. The IMPAC II Reporting Database (IRDB) supports internal reporting.
- **eRA Commons**: the external interface for applicants, recipients and reviewers.
- **ASSIST**: the web system for preparing and submitting applications.
- **Internet Assisted Review (IAR)** and other modules for peer review.

## Data access

eRA systems require an account, and IMPAC II and IRDB are not publicly accessible. Public data derived from eRA are released through the RePORT suite, notably [NIH RePORTER](https://reporter.nih.gov/), its API and the ExPORTER bulk downloads. The SPIRES module maps PubMed publications to the grants that supported them, and those links are published through RePORTER.