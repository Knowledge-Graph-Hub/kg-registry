---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@isrctn.com
  - contact_type: url
    value: https://www.isrctn.com/page/contact
  label: ISRCTN Registry, BioMed Central
creation_date: '2026-10-05T00:00:00Z'
description: ISRCTN is a primary clinical study registry recognised by the World Health
  Organization International Clinical Trials Registry Platform (WHO ICTRP) and the
  ICMJE. Launched in 2000 as the International Standard Randomised Controlled Trial
  Number scheme, it now registers any interventional or observational study that assesses
  health interventions in humans, and is positioned as the UK's clinical study registry.
  Each record carries a unique ISRCTN identifier, the WHO 24-item minimum trial registration
  dataset, plain English summaries, results and IPD sharing plans. The registry is
  run by ISRCTN, a non-profit, through BioMed Central (Springer Nature), and its records
  are available through a web search interface and a public XML API.
domains:
- biomedical
- clinical
- clinical trials
- public health
homepage_url: https://www.isrctn.com/
id: isrctn
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://www.isrctn.com/page/terms
  label: CC BY for narrative record fields; CC0 for other metadata (records submitted
    on or after 2019-01-01)
name: ISRCTN Registry
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing and viewing ISRCTN study records,
    with basic and advanced search by condition, intervention, funder, recruitment
    country and other fields, plus the Transparency Tracker view of results reporting.
  format: http
  id: isrctn.portal
  name: ISRCTN Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: isrctn
  product_url: https://www.isrctn.com/
- category: ProgrammingInterface
  description: Public, unauthenticated XML API for retrieving single trials (/api/trial/<isrctn>/format/<format>)
    or querying multiple trials (/api/query/format/<format>?q=<query>&limit=<limit>)
    with keyword and field constraints. Output formats include the ISRCTN default
    format and the WHO ICTRP trial format.
  format: xml
  id: isrctn.api
  name: ISRCTN XML API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: isrctn
  product_url: https://www.isrctn.com/api/query/format/default?q=
- category: DocumentationProduct
  description: API documentation (PDF, prepared by 67 Bricks for Springer Nature)
    describing the ISRCTN API endpoints, query constraints and output formats.
  format: pdf
  id: isrctn.api-docs
  name: ISRCTN API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: isrctn
  product_file_size: 450273
  product_url: https://www.isrctn.com/editorial/retrieveFile/81786542-9920-48a0-8fce-09f8428ab843/37855
- category: DocumentationProduct
  description: Definitions of the fields in ISRCTN study records and the registration
    application form.
  format: http
  id: isrctn.definitions
  name: ISRCTN Field Definitions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: isrctn
  product_url: https://www.isrctn.com/page/definitions
- category: GraphicalInterface
  description: ICTRP Search Portal for searching trial registration records from all
    ICTRP data providers, with basic and advanced search, filters for phase, results,
    children, COVID-19, rare diseases and genome editing, browsing by health topic
    and country, and links to the original registry records.
  format: http
  id: who-ictrp.portal
  name: ICTRP Search Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  - relation_type: prov:hadPrimarySource
    source: isrctn
  product_url: https://trialsearch.who.int/
- category: Product
  description: Export of ICTRP search results (selected records or all records of
    a search) from the Search Portal in XML or CSV format, free of charge under the
    WHO ICTRP data terms and conditions.
  format: xml
  id: who-ictrp.search-export
  name: ICTRP Search Results Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  - relation_type: prov:hadPrimarySource
    source: isrctn
  product_url: https://www.who.int/tools/clinical-trials-registry-platform/network/who-data-set/downloading-records-from-the-ictrp-database
- category: ProgrammingInterface
  connection_url: https://trialsearch.who.int/TrialService.asmx
  description: ICTRP Search Portal Web Service, a SOAP/XML web service (operations
    include GetTrials and GetTrialDetails) for querying the ICTRP database in real
    time. Access is granted to agreed partners for research purposes, and WHO may
    charge to recoup costs.
  format: xml
  id: who-ictrp.web-service
  is_public: false
  name: ICTRP Search Portal Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  - relation_type: prov:hadPrimarySource
    source: isrctn
  product_url: https://www.who.int/tools/clinical-trials-registry-platform/the-ictrp-search-portal/ictrp-search-portal-web-service
publications:
- authors:
  - Helene Faure
  - Iain Hrynaszkiewicz
  doi: 10.1111/j.1756-5391.2011.01138.x
  id: doi:10.1111/j.1756-5391.2011.01138.x
  journal: Journal of Evidence-Based Medicine
  preferred: true
  title: 'The ISRCTN Register: achievements and challenges 8 years on'
  year: '2011'
synonyms:
- ISRCTN
- International Standard Randomised Controlled Trial Number
- The UK's Clinical Study Registry
---
# ISRCTN Registry

The ISRCTN registry is a WHO ICTRP primary registry and ICMJE-recognised registry for clinical studies. It was launched in 2000 for randomised controlled trials and has since widened to any study assessing the efficacy of health interventions in humans, both interventional and observational. Since 2022 the UK Health Research Authority automatically registers clinical trials of investigational medicinal products with ISRCTN through IRAS.

Each record includes the WHO 24-item minimum registration dataset, along with protocol summaries, plain English summaries, results, statistical analysis plans and individual participant data sharing plans. ISRCTN data are uploaded weekly to the WHO trial search portal and to the NIHR Be Part of Research service.

## Access

- **Web search**: basic and advanced search at https://www.isrctn.com/.
- **XML API**: a public API at `https://www.isrctn.com/api/` supports single-trial retrieval and queries, returning XML in the ISRCTN default or WHO format.

## License

Under the ISRCTN terms and conditions, narrative fields (plain English summary, study objectives, intervention, outcome measures, results and similar) are covered by CC BY. All other record content counts as metadata that can be used without attribution, and metadata for records submitted on or after 1 January 2019 can be reused on a CC0 basis. The general site terms otherwise restrict bulk copying of site content.