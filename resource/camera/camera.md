---
activity_status: active
category: Aggregator
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://camera.od.nih.gov/contact
  - contact_type: url
    value: https://ntp.niehs.nih.gov/whatwestudy/niceatm
  label: NTP Interagency Center for the Evaluation of Alternative Toxicological Methods
    (NICEATM)
creation_date: '2026-10-28T00:00:00Z'
description: CAMERA (Collection of Alternative Methods for Regulatory Application) is
  a public, interactive NIH database and web interface that consolidates validated and
  qualified New Approach Methods (NAMs) for chemical safety testing into a single resource.
  It brings together validation study reports, data, protocols and SOPs, and regulatory
  guidance that were previously scattered across multiple agencies and organizations,
  and lets users filter by alternative method type, defined approach, test method endpoint,
  and regulatory guidance. CAMERA additionally uses standardized ontology vocabulary
  and large language models to identify validated NAMs that can measure the key events
  (KEs) of OECD-endorsed adverse outcome pathways (AOPs), linking methods to AOP-Wiki
  content to support next generation risk assessment. It currently holds 67 validated
  NAMs. CAMERA is supported by NICEATM and operates under the direction and oversight
  of the Interagency Coordinating Committee on the Validation of Alternative Methods
  (ICCVAM).
domains:
- toxicology
- adverse outcome pathways
- chemistry and biochemistry
- environment
homepage_url: https://camera.od.nih.gov/
id: camera
last_modified_date: '2026-10-28T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: CAMERA (Collection of Alternative Methods for Regulatory Application)
products:
- category: GraphicalInterface
  description: CAMERA Explore NAMs interface for searching and filtering validated and
    qualified New Approach Methods by alternative method type, defined approach, test
    method endpoint, chemical, and regulatory guidance, with links to validation study
    reports, data, protocols/SOPs, and the associated adverse outcome pathway key events.
    Chemical identity and data are drawn from the EPA CompTox Chemicals Dashboard.
  format: http
  id: camera.explore
  name: Explore NAMs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: camera
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: comptox-dashboard
  product_url: https://camera.od.nih.gov/explore
- category: DocumentationProduct
  description: CAMERA user guide, with help and FAQs for using the database and interface.
  format: http
  id: camera.user-guide
  name: CAMERA User Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: camera
  product_url: https://camera.od.nih.gov/user-guide
publications:
- authors:
  - Alexander Cole
  - Katie Needham
  - Prince Osei-Akyeampong
  - Tosho Agunloye
  - Jeremiah Mensah
  - Caleb DeGroote
  - Helena T. Hogberg
  doi: 10.6084/m9.figshare.34809921.v1
  id: doi:10.6084/m9.figshare.34809921.v1
  journal: figshare
  preferred: true
  title: 'CAMERA and AOP-Wiki: Building a NAMs Database with Integrated AOP Features
    to Support Next Generation Risk Assessment'
  year: '2026'
synonyms:
- Collection of Alternative Methods for Regulatory Application
---
# CAMERA (Collection of Alternative Methods for Regulatory Application)

## Overview

CAMERA is a public NIH database and web interface that consolidates validated and qualified New Approach Methods (NAMs) for chemical safety testing. It gathers validation study reports, data, protocols and SOPs, and regulatory guidance that were previously scattered across agencies and organizations, and presents them in one searchable interface, filterable by alternative method type, defined approach, test method endpoint, and regulatory guidance.

CAMERA also uses standardized ontology vocabulary and large language models to link validated NAMs to the key events of OECD-endorsed adverse outcome pathways, drawing on AOP-Wiki, so that methods can be found by the key event or AOP they inform. Chemical identity and data in the interface are drawn from the EPA CompTox Chemicals Dashboard. It currently holds 67 validated NAMs.

CAMERA is supported by NICEATM and operates under the direction and oversight of ICCVAM.

## Access

- Explore NAMs: search and filter the validated and qualified methods.
- User guide, help, and FAQs on the CAMERA site.

CAMERA content is a work of the U.S. federal government and is in the public domain. There is no public bulk download or API. Ongoing development is noted to expand method domains and strengthen interoperability with other resources such as the NIH Integrated Chemical Environment (ICE) and AOP-Wiki.

## Citation

Cole A, Needham K, Osei-Akyeampong P, et al. CAMERA and AOP-Wiki: Building a NAMs Database with Integrated AOP Features to Support Next Generation Risk Assessment. figshare; 2026. doi:10.6084/m9.figshare.34809921.v1
