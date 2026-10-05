---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ema.europa.eu/
  - contact_type: url
    value: https://servicedesk.ema.europa.eu/
  label: European Medicines Agency
creation_date: '2026-10-05T00:00:00Z'
description: The EU Clinical Trials Register (EU CTR) and the Clinical Trials Information
  System (CTIS) are the European Medicines Agency's public registries of interventional
  clinical trials of medicines in the European Union and European Economic Area. The
  EU Clinical Trials Register, established under Article 11 of Directive 2001/20/EC,
  gives public access to protocol and summary results information from the EudraCT
  database for trials started since May 2004, including paediatric trials run outside
  the EU/EEA as part of a paediatric investigation plan. CTIS, under Clinical Trials
  Regulation (EU) No 536/2014, has handled all new trial applications since 31 January
  2023 and became the single entry point for ongoing trials after the transition period
  ended in January 2025; its public portal publishes trial information, documents
  and results. The legacy register no longer accepts new trials but remains online
  as the source for trials authorised under the Directive.
domains:
- clinical
- clinical trials
- biomedical
- pharmacology
homepage_url: https://www.clinicaltrialsregister.eu/
id: eu-ctr
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://www.clinicaltrialsregister.eu/disclaimer.html
  label: EMA terms - reuse permitted with attribution to the EU Clinical Trials Register
    and the date of access; see also the EMA legal notice
name: EU Clinical Trials Register and Clinical Trials Information System
products:
- category: GraphicalInterface
  description: Web search interface for the EU Clinical Trials Register, covering
    protocol and results information for interventional trials authorised under Directive
    2001/20/EC, searchable by EudraCT number, condition, medicine, sponsor, country,
    phase, population age and other fields.
  format: http
  id: eu-ctr.search
  name: EU Clinical Trials Register Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  product_url: https://www.clinicaltrialsregister.eu/ctr-search/search
- category: Product
  description: Plain-text export of EU Clinical Trials Register search results, available
    as a summary or as full trial details (per member state), up to 20 trials per
    request.
  format: txt
  id: eu-ctr.download
  name: EU Clinical Trials Register Search Results Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  product_url: https://www.clinicaltrialsregister.eu/ctr-search/rest/download/full?query=&page=1&mode=current_page
- category: GraphicalInterface
  description: Summary results of EU Clinical Trials Register trials, including trial
    information, subject disposition, baseline characteristics, end points and adverse
    events, browsable from search results filtered to trials with results.
  format: http
  id: eu-ctr.results
  name: EU Clinical Trials Register Results
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  product_url: https://www.clinicaltrialsregister.eu/ctr-search/search?query=&resultsstatus=trials-with-results
- category: GraphicalInterface
  description: Public portal of the Clinical Trials Information System (CTIS), the
    EU registry for trials under Clinical Trials Regulation (EU) No 536/2014, with
    search over trial details, sponsors, therapeutic areas, recruitment status, documents
    and results, plus a clinical trial map searchable by medical condition.
  format: http
  id: eu-ctr.ctis
  name: CTIS Public Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  product_url: https://euclinicaltrials.eu/ctis-public/search
- category: DocumentationProduct
  description: Frequently asked questions for the EU Clinical Trials Register, covering
    register scope, search and download functions, and interpretation of trial and
    results records.
  format: pdf
  id: eu-ctr.faq
  name: EU Clinical Trials Register FAQ
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  product_url: https://www.clinicaltrialsregister.eu/doc/EU_CTR_FAQ.pdf
- category: DocumentationProduct
  description: European Medicines Agency documentation for CTIS, including the system
    overview, transition from the Clinical Trials Directive, transparency rules and
    links to training and support material.
  format: http
  id: eu-ctr.ctis.docs
  name: CTIS Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  product_url: https://www.ema.europa.eu/en/human-regulatory-overview/research-development/clinical-trials-human-medicines/clinical-trials-information-system-ctis
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
synonyms:
- EU CTR
- EU Clinical Trials Register
- Clinical Trials Information System
- CTIS
- euclinicaltrials.eu
---
## EU Clinical Trials Register and CTIS

The European Medicines Agency (EMA) operates two public registries of interventional
clinical trials of medicines in the EU/EEA. The EU Clinical Trials Register publishes
protocol and summary results information from the EudraCT database for trials authorised
under the Clinical Trials Directive (2001/20/EC) since 2004. The Clinical Trials Information
System (CTIS) replaced it for trials under the Clinical Trials Regulation (EU) No 536/2014:
all new applications have gone through CTIS since 31 January 2023, and ongoing Directive
trials had to transition to CTIS by January 2025.

Note that "EU CTR" is also a common abbreviation for the Clinical Trials Regulation itself.

Data may be reused provided the source is attributed and the access date is displayed;
email addresses in the register must not be used for marketing.