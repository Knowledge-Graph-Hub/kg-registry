---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: JRC-TSAR-CONTACT@ec.europa.eu
  - contact_type: url
    value: https://joint-research-centre.ec.europa.eu/eu-reference-laboratory-alternatives-animal-testing-eurl-ecvam_en
  label: EU Reference Laboratory for Alternatives to Animal Testing (EURL ECVAM),
    European Commission Joint Research Centre (JRC)
creation_date: '2026-10-19T00:00:00Z'
description: TSAR (EURL ECVAM Tracking System for Alternative methods towards Regulatory
  acceptance) is a database maintained by the European Commission Joint Research Centre
  (JRC) that tracks the progress of alternative test methods for chemicals and biological
  agents such as vaccines toward recognition for regulatory use. For each method it
  records the submission, validation, peer review, recommendation, and regulatory
  acceptance (including international standards such as OECD Test Guidelines) stages,
  with links to supporting documents where available. It covers methods validated
  by governmental organisations affiliated with the International Cooperation on
  Alternative Test Methods (ICATM).
domains:
- toxicology
homepage_url: https://tsar.jrc.ec.europa.eu/
id: tsar
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://commission.europa.eu/legal-notice_en
  label: European Commission Legal Notice
name: TSAR (Tracking System for Alternative methods towards Regulatory acceptance)
products:
- category: GraphicalInterface
  description: Searchable listing of test methods tracked in TSAR, filterable by
    topic (for example skin sensitisation, endocrine disruption, genotoxicity, eye
    irritation), responsible organisation, current stage, and status, with per-method
    records of submission, validation, peer review, recommendation, and regulatory
    acceptance and links to associated documents.
  format: http
  id: tsar.test-methods
  name: TSAR Test Methods Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tsar
  product_url: https://tsar.jrc.ec.europa.eu/test-methods
- category: DocumentationProduct
  description: Description of the scope, stages, partners, and update policy of
    TSAR.
  format: http
  id: tsar.about
  name: About TSAR
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tsar
  product_url: https://tsar.jrc.ec.europa.eu/content/about-tsar
synonyms:
- TSAR
---
# TSAR (Tracking System for Alternative methods towards Regulatory acceptance)

## Overview

TSAR is a database developed by the EU Reference Laboratory for Alternatives to Animal Testing (EURL ECVAM) at the European Commission Joint Research Centre (JRC). It indicates how far each tracked alternative test method has progressed toward acceptance as a recognised test method, for chemicals and for biological agents such as vaccines. TSAR shares information on methods considered by members and observers of the International Cooperation on Alternative Test Methods (ICATM): EURL ECVAM (EU), Health Canada, ICCVAM/NICEATM (US), JaCVAM (Japan), and KoCVAM (Republic of Korea), with ad hoc participation from Brazil (BraCVAM), Singapore, China, and Taiwan.

## Data Content

- Records for about 150 test methods, each identified by a TSAR test method number (for example TM2009-14).
- Stages tracked per method: submission, validation, peer review, recommendation, and regulatory acceptance / standards, each with a status (for example planning, ongoing, finalised, stopped, published).
- Topic areas including skin sensitisation, skin corrosion and irritation, eye irritation, genotoxicity, endocrine disruption, and quality control of vaccines.
- Links to documents produced at each stage; these are the versions used during validation and may not be the most current SOPs.
- Methods with no activity for five years, or whose submitter can no longer be contacted, are marked as on hold.

## Access

- Homepage: https://tsar.jrc.ec.europa.eu/
- Test method listing: https://tsar.jrc.ec.europa.eu/test-methods
- About page: https://tsar.jrc.ec.europa.eu/content/about-tsar

## License

TSAR does not state a content-specific license. The site is governed by the European Commission legal notice, under which reuse of Commission content is generally authorised under the Commission's reuse policy unless otherwise indicated.
