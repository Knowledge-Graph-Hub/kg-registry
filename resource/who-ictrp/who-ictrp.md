---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://trialsearch.who.int/Contact.aspx
  label: World Health Organization
creation_date: '2026-10-05T00:00:00Z'
description: The WHO International Clinical Trials Registry Platform (ICTRP) Search
  Portal provides a single point of access to clinical trial registration records
  supplied by the registries of the WHO Registry Network, including the WHO primary
  registries and ClinicalTrials.gov. Records follow the WHO Trial Registration Data
  Set, are provided in English, link back to the original registry records, and are
  bridged (grouped) when several registries hold records for the same trial. Data
  sets are imported weekly or every four weeks depending on the data provider. The
  ICTRP is not itself a trial registry.
domains:
- clinical
- clinical trials
homepage_url: https://trialsearch.who.int/
id: who-ictrp
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://www.who.int/tools/clinical-trials-registry-platform/network/who-data-set/downloading-records-from-the-ictrp-database
  label: WHO ICTRP Terms and Conditions for Use of Data
name: WHO International Clinical Trials Registry Platform
products:
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
- category: DocumentationProduct
  description: List of the primary registries in the WHO Registry Network that meet
    WHO criteria for content, quality, accessibility, unique identification, technical
    capacity and administration, with registry profiles and website links.
  format: http
  id: who-ictrp.primary-registries
  name: WHO Primary Registries List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  product_url: https://www.who.int/tools/clinical-trials-registry-platform/network/primary-registries
- category: DocumentationProduct
  description: List of the data providers that supply trial records to the ICTRP Search
    Portal, including the primary registries and ClinicalTrials.gov.
  format: http
  id: who-ictrp.data-providers
  name: ICTRP Data Providers List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  product_url: https://www.who.int/tools/clinical-trials-registry-platform/network/data-providers
- category: DocumentationProduct
  description: Documentation of the WHO Trial Registration Data Set, the minimum set
    of items a trial record must contain to be included in the ICTRP, with archived
    earlier versions.
  format: http
  id: who-ictrp.who-data-set
  name: WHO Trial Registration Data Set
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  product_url: https://www.who.int/tools/clinical-trials-registry-platform/network/who-data-set
- category: DocumentationProduct
  description: WHO ICTRP website describing the platform, the registry network, the
    search portal and its services, trial registration standards, and the Universal
    Trial Number.
  format: http
  id: who-ictrp.docs
  name: ICTRP Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  product_url: https://www.who.int/tools/clinical-trials-registry-platform
- category: GraphicalInterface
  description: Web portal for searching clinical studies and their data objects by keyword,
    registry identifier, PubMed ID or country, with CSV and JSON export of results.
  format: http
  id: ecrin-mdr.portal
  name: ECRIN MDR Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  - relation_type: prov:hadPrimarySource
    source: isrctn
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  - relation_type: prov:hadPrimarySource
    source: biolincc
  - relation_type: prov:hadPrimarySource
    source: yoda
  product_url: https://newmdr.ecrin.org/
- category: ProgrammingInterface
  description: REST API behind the MDR portal (MDR_FuiPortal.Server), with endpoints for study
    search, lookup by registry ID or PubMed ID, full study and object details, summary statistics
    and an OmicsDI export feed. Documented with Swagger/OpenAPI.
  format: http
  id: ecrin-mdr.api
  name: ECRIN MDR API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: who-ictrp
  - relation_type: prov:hadPrimarySource
    source: isrctn
  - relation_type: prov:hadPrimarySource
    source: eu-ctr
  - relation_type: prov:hadPrimarySource
    source: biolincc
  - relation_type: prov:hadPrimarySource
    source: yoda
  product_url: https://newmdr.ecrin.org/swagger/index.html
publications:
- authors:
  - Ida Sim
  - An-Wen Chan
  - A Metin Gülmezoglu
  - Tim Evans
  - Tikki Pang
  doi: 10.1016/s0140-6736(06)68708-4
  id: doi:10.1016/s0140-6736(06)68708-4
  journal: The Lancet
  preferred: true
  title: 'Clinical trial registration: transparency is the watchword'
  year: '2006'
synonyms:
- ICTRP
- WHO ICTRP
- ICTRP Search Portal
---
# WHO International Clinical Trials Registry Platform

The WHO International Clinical Trials Registry Platform (ICTRP) aims to give a complete view of clinical research to everyone involved in health care decisions. Its Search Portal combines the trial registration data sets supplied by the registries in the WHO Registry Network into one searchable database. The ICTRP is not a registry: trials are registered with a primary registry or ClinicalTrials.gov, and the portal links back to those original records.

## Data providers

Data providers include the WHO primary registries (for example ANZCTR, ChiCTR, CRiS, CTIS, CTRI, DRKS, EU-CTR, IRCT, ISRCTN, jRCT, PACTR, ReBec, REPEC, RPCEC, SLCTR, TCTR, ITMCTR and LBCTR) and ClinicalTrials.gov. Records from ClinicalTrials.gov, CTIS, EU-CTR, ISRCTN, ANZCTR, ChiCTR and the Netherlands register are imported every week; most other registries are imported every four weeks. The portal bridges multiple records that describe the same trial.

## Access

- The Search Portal is free to use. Search results can be exported in XML or CSV.
- The web service (SOAP/XML) is offered to agreed partners for research use, and WHO may charge to recoup costs.
- The crawling service was listed as unavailable when checked on 2026-10-05.

ICTRP data are provided under WHO's terms for ICTRP data: users should attribute WHO ICTRP, keep the data current, show the date WHO ICTRP processed it, and not use it for marketing, promotional or commercial purposes or use the WHO name or emblem.
