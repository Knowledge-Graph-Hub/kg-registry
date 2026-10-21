---
activity_status: inactive
category: DataModel
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ich.org/
  label: International Council for Harmonisation (ICH)
creation_date: '2026-10-19T00:00:00Z'
description: 'ICH M5, "Data Elements and Standards for Drug Dictionaries," was a multidisciplinary
  ICH topic that developed controlled vocabularies for dosage forms, routes of administration,
  and units of measurement to standardize drug dictionary data; a consensus (Step
  2) draft was issued in 2005. It was never finalized as a standalone ICH guideline:
  the M5 Expert Working Group was closed following finalisation of the ISO IDMP (Identification
  of Medicinal Products) standards, and the vocabulary substance now lives in ISO
  IDMP and the actively maintained EDQM Standard Terms. This registry entry records
  the historical ICH M5 vocabularies as a data model.'
domains:
- pharmacology
- clinical coding
- clinical
homepage_url: https://www.ema.europa.eu/en/scientific-guidelines/ich-m5-data-elements-standards-drug-dictionaries
id: ich-m5
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: ICH M5 controlled vocabularies
products:
- category: GraphicalInterface
  description: Web application for searching NHPID ingredients by name or CAS number
    and role (homeopathic, medicinal, non-medicinal, non-NHP, component), and for
    searching the NHP controlled vocabularies by category. Controlled vocabulary terms
    for dosage forms, routes of administration, and units are adapted from ICH M5
    lists, and ingredient naming conventions from the TGA approved terminology.
  format: http
  id: nhpid.web
  name: NHPID Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhpid
  product_url: https://webprod.hc-sc.gc.ca/nhpid-bdipsn/?lang=eng
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: tga-approved-terminology
  - relation_type: prov:wasDerivedFrom
    source: ich-m5
- category: DataModelProduct
  description: The 2005 ICH M5 consensus (Step 2) draft specifying data elements and
    standards for drug dictionaries, including controlled vocabularies for routes
    of administration and units.
  format: pdf
  id: ich-m5.guideline
  name: ICH M5 Drug Dictionaries Guideline (2005 draft)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ich-m5
  product_file_size: 0
  product_url: https://www.ema.europa.eu/en/documents/scientific-guideline/ich-guideline-m5-data-elements-and-standards-drug-dictionaries_en.pdf
- category: DataModelProduct
  description: The M5 Expert Working Group controlled vocabulary mapping route-of-administration
    terms, with regional equivalents and E2B codes.
  format: http
  id: ich-m5.routes-cv
  name: ICH M5 Routes of Administration Controlled Vocabulary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ich-m5
  product_url: https://www.ema.europa.eu/en/scientific-guidelines/ich-m5-ewg-routes-administration-controlled-vocabulary
- category: DataModelProduct
  description: The M5 Expert Working Group controlled vocabulary for units and measurements
    used in drug dictionaries.
  format: http
  id: ich-m5.units-cv
  name: ICH M5 Units and Measurements Controlled Vocabulary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ich-m5
  product_url: https://www.ema.europa.eu/en/scientific-guidelines/ich-m5-ewg-units-measurements-controlled-vocabulary
---
# ICH M5 controlled vocabularies

## Overview

ICH M5, "Data Elements and Standards for Drug Dictionaries," was an ICH topic that developed controlled vocabularies for dosage forms, routes of administration, and units of measurement. A consensus draft appeared in 2005, but the topic was never finalized as a standalone guideline: its Expert Working Group was closed once the ISO IDMP standards were finalized, and the vocabulary substance passed to ISO IDMP and the EDQM Standard Terms.

## Access

- The 2005 ICH M5 guideline draft (PDF).
- The routes-of-administration and units-and-measurements controlled vocabulary pages.

The actively maintained successor terminology is the EDQM Standard Terms (https://standardterms.edqm.eu/). This entry is recorded with an activity status of inactive.

## Citation

ICH M5 guideline "Data Elements and Standards for Drug Dictionaries" (consensus draft, EMEA/CHMP/ICH/168535/2005, 2005).