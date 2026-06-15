---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://digital.nhs.uk/services/terminology-and-classifications/dm-d
  label: NHS England
creation_date: '2026-06-02T00:00:00Z'
description: The NHS dictionary of medicines and devices is the national clinical
  vocabulary for identifying medicines and medical devices used across the NHS and
  for exchanging medicines information between clinical systems.
domains:
- clinical
- biomedical
- pharmacology
homepage_url: https://digital.nhs.uk/services/terminology-and-classifications/dm-d
id: dmd
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: NHS dictionary of medicines and devices
products:
- category: GraphicalInterface
  description: Official NHSBSA browser for searching and viewing dm+d medicines and
    device concepts.
  id: dmd.browser
  name: dm+d Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dmd
  product_url: https://services.nhsbsa.nhs.uk/dmd-browser/
- category: ProgrammingInterface
  description: NHS Terminology Server access route recommended by NHS England for
    integrating dm+d terminology into healthcare IT systems.
  id: dmd.terminology-server
  is_public: true
  name: dm+d Terminology Server Access
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dmd
  product_url: https://digital.nhs.uk/services/terminology-and-classifications/dm-d
- category: Product
  description: Raw dm+d data files distributed as XML for system implementation and
    terminology integration.
  format: xml
  id: dmd.raw-files
  name: dm+d Raw Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dmd
  product_url: https://digital.nhs.uk/services/terminology-and-classifications/dm-d
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-13: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
    when accessing file'
- category: DocumentationProduct
  description: Vision help documentation describing Gemscript as the integrated drug
    dictionary used in Vision 3 prescribing workflows
  format: http
  id: gemscript.documentation
  name: Gemscript Vision Help Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gemscript
  product_url: https://help.visionhealth.co.uk/Vision_Consultation_Manager_Help_Centre/Content/ConMgr/Gemscript/Gemscript_Drug_Dictionary.htm
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: dmd
- category: DocumentationProduct
  description: Monthly Gemscript bulletin summarizing additions, deletions, name changes,
    and drug class changes in the active dictionary
  format: pdf
  id: gemscript.bulletin
  latest_version: 2026 May v.01
  name: Gemscript Monthly Bulletin
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gemscript
  product_file_size: 173789
  product_url: https://help.visionhealth.co.uk/PDFs/Dictionaries/Gemscript/Gemscript_Bulletin_May_2026.pdf
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: dmd
synonyms:
- dm+d
- dmd
- Dictionary of Medicines and Devices
---
# NHS dictionary of medicines and devices

The NHS dictionary of medicines and devices (dm+d) provides shared identifiers,
descriptions, and product structures for medicines and devices used in NHS care.
It supports prescribing, dispensing, reimbursement, system interoperability, and
safe exchange of medicines information between clinical systems.