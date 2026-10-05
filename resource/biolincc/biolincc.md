---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: biolincc@imsweb.com
  - contact_type: url
    value: https://biolincc.nhlbi.nih.gov/contact/
  label: National Heart, Lung, and Blood Institute
creation_date: '2026-10-05T00:00:00Z'
description: BioLINCC (Biologic Specimen and Data Repository Information Coordinating
  Center) is the National Heart, Lung, and Blood Institute (NHLBI) program that coordinates
  access to the NHLBI Biologic Specimen Repository and the NHLBI Data Repository.
  It provides a searchable catalog of de-identified datasets and biospecimens from
  NHLBI-funded clinical trials and epidemiological studies in cardiovascular, pulmonary,
  sleep and hematologic research (316 studies when checked on 2026-10-05), with study
  documents and data dictionaries viewable without an account. Study datasets and
  biospecimens are released only to qualified investigators through a request process
  that requires login, IRB documentation and a signed Research Materials Distribution
  Agreement; teaching and public use datasets are also offered on request. BioLINCC
  was still posting new studies in October 2026, so access has not migrated to NHLBI
  BioData Catalyst, although some NHLBI studies are released through BioData Catalyst
  or dbGaP instead. When checked on 2026-10-05 the site carried a banner stating that
  the repository is under review for potential modification in compliance with Administration
  directives.
domains:
- biomedical
- clinical
homepage_url: https://biolincc.nhlbi.nih.gov/
id: biolincc
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: BioLINCC
products:
- category: GraphicalInterface
  description: BioLINCC web portal for browsing NHLBI repository resources, registering
    an account (Login.gov, ID.me or NIH login) and submitting requests for study datasets,
    biospecimens and teaching datasets.
  format: http
  id: biolincc.portal
  name: BioLINCC Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolincc
  product_url: https://biolincc.nhlbi.nih.gov/
- category: GraphicalInterface
  description: Searchable catalog of NHLBI studies with available datasets and/or
    biospecimens, filterable by available resources, collection type and condition,
    with per-study pages carrying study documents, data dictionaries and biospecimen
    counts. Access to the datasets and specimens themselves is controlled and requires
    an approved request and a Research Materials Distribution Agreement.
  format: http
  id: biolincc.studies
  name: BioLINCC Study Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolincc
  product_url: https://biolincc.nhlbi.nih.gov/studies/
- category: Product
  description: CSV export of the BioLINCC study search results, listing study name,
    acronym, available resources (study datasets, specimens or both) and collection
    type for each study (316 rows when checked on 2026-10-05).
  format: csv
  id: biolincc.study-list
  name: BioLINCC Study List Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolincc
  product_url: https://biolincc.nhlbi.nih.gov/studies/?_export
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-05: Error connecting
    to URL: HTTPSConnectionPool(host=''biolincc.nhlbi.nih.gov'', port=443): Max retries
    exceeded with url: /studies/?_export (Caused by NewConnectionError("HTTPSConnection(host=''biolincc.nhlbi.nih.gov'',
    port=443): Failed to establish a new connection: [Errno 101] Network is unreachable"))'
- category: Product
  description: Teaching datasets derived from the Framingham Heart Study, the Digitalis
    Investigation Group trial and the Childhood Asthma Management Program, anonymized
    for biostatistics instruction and available free on request, plus public use datasets
    from the National Longitudinal Mortality Study. Teaching datasets are not suitable
    for publication.
  format: http
  id: biolincc.teaching-datasets
  name: BioLINCC Teaching and Public Use Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolincc
  product_url: https://biolincc.nhlbi.nih.gov/teaching/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-05: Error connecting
    to URL: HTTPSConnectionPool(host=''biolincc.nhlbi.nih.gov'', port=443): Max retries
    exceeded with url: /teaching/ (Caused by NewConnectionError("HTTPSConnection(host=''biolincc.nhlbi.nih.gov'',
    port=443): Failed to establish a new connection: [Errno 101] Network is unreachable"))'
- category: DocumentationProduct
  description: BioLINCC Users Guide describing how to search for and request study
    datasets and biospecimens, the review process, required IRB documentation and
    the Research Materials Distribution Agreement.
  format: pdf
  id: biolincc.users-guide
  name: BioLINCC Users Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolincc
  product_url: https://biolincc.nhlbi.nih.gov/media/BioLINCC_User_Guide_05Jan2026.pdf
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-05: Error connecting
    to URL: HTTPSConnectionPool(host=''biolincc.nhlbi.nih.gov'', port=443): Max retries
    exceeded with url: /media/BioLINCC_User_Guide_05Jan2026.pdf (Caused by NewConnectionError("HTTPSConnection(host=''biolincc.nhlbi.nih.gov'',
    port=443): Failed to establish a new connection: [Errno 101] Network is unreachable"))'
- category: DocumentationProduct
  description: Frequently asked questions on account registration, request requirements,
    costs, de-identification and redaction, request timelines and terms of use for
    BioLINCC materials.
  format: http
  id: biolincc.faq
  name: BioLINCC FAQ
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolincc
  product_url: https://biolincc.nhlbi.nih.gov/faq/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-05: Error connecting
    to URL: HTTPSConnectionPool(host=''biolincc.nhlbi.nih.gov'', port=443): Max retries
    exceeded with url: /faq/ (Caused by NewConnectionError("HTTPSConnection(host=''biolincc.nhlbi.nih.gov'',
    port=443): Failed to establish a new connection: [Errno 101] Network is unreachable"))'
- category: GraphicalInterface
  description: Web portal for searching clinical studies and their data objects by
    keyword, registry identifier, PubMed ID or country, with CSV and JSON export of
    results.
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
  description: REST API behind the MDR portal (MDR_FuiPortal.Server), with endpoints
    for study search, lookup by registry ID or PubMed ID, full study and object details,
    summary statistics and an OmicsDI export feed. Documented with Swagger/OpenAPI.
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
  - Carol A. Giffen
  - Leslie E. Carroll
  - John T. Adams
  - Sean P. Brennan
  - Sean A. Coady
  - Elizabeth L. Wagner
  doi: 10.1089/bio.2014.0050
  id: doi:10.1089/bio.2014.0050
  journal: Biopreservation and Biobanking
  preferred: true
  title: 'Providing Contemporary Access to Historical Biospecimen Collections: Development
    of the NHLBI Biologic Specimen and Data Repository Information Coordinating Center
    (BioLINCC)'
  year: '2015'
- authors:
  - Carol A. Giffen
  - Elizabeth L. Wagner
  - John T. Adams
  - Denise M. Hitchcock
  - Lisbeth A. Welniak
  - Sean P. Brennan
  - Leslie E. Carroll
  doi: 10.1371/journal.pone.0178141
  id: doi:10.1371/journal.pone.0178141
  journal: PLOS ONE
  title: 'Providing researchers with online access to NHLBI biospecimen collections:
    The results of the first six years of the NHLBI BioLINCC program'
  year: '2017'
synonyms:
- Biologic Specimen and Data Repository Information Coordinating Center
- NHLBI Biologic Specimen and Data Repository
---
# BioLINCC

BioLINCC is the NHLBI's coordinating center for its Biologic Specimen Repository
and Data Repository. It catalogs de-identified study datasets and biospecimens from
NHLBI-funded clinical trials and cohort studies (for example ARIC, CARDIA, the
Cardiovascular Health Study, the Framingham Heart Study and the Jackson Heart Study)
and manages controlled-access requests for them.

## Access

Study pages, documents and data dictionaries are public. Datasets and biospecimens
require a registered account, IRB documentation and a signed Research Materials
Distribution Agreement. Data are provided at no cost; biospecimen requests may incur
shipping and processing costs.