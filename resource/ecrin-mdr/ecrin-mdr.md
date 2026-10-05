---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ecrin.org/
  - contact_type: github
    value: ecrin-github
  label: European Clinical Research Infrastructure Network (ECRIN)
creation_date: '2026-10-04T00:00:00Z'
description: The ECRIN Clinical Research Metadata Repository (MDR) aggregates metadata
  on clinical studies and their associated data objects (registry entries, protocols,
  results, publications and datasets) from trial registries and data repositories
  into one schema, providing a single search point for clinical research data. It
  is run by the European Clinical Research Infrastructure Network. On 2026-10-04 its
  API reported 971,303 studies and 1,542,181 data objects.
domains:
- clinical
- clinical trials
- information technology
- metadata
homepage_url: https://newmdr.ecrin.org/
id: ecrin-mdr
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (public domain) among its sources: clinicaltrialsgov, pubmed.'
  id: https://clinicaltrials.gov/about-site/terms-conditions
  inferred_from:
  - clinicaltrialsgov
  - pubmed
  label: Public Domain
  restrictiveness: public domain
  status: inferred
  unresolved_sources: []
name: ECRIN Clinical Research Metadata Repository
products:
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
  product_url: https://newmdr.ecrin.org/swagger/index.html
- category: DataModelProduct
  description: ECRIN Metadata Schemas for Clinical Research, version 8 (September
    2023), the common metadata model for studies and data objects used by the MDR,
    distributed as a Word document on Zenodo.
  format: docx
  id: ecrin-mdr.schema
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: ECRIN Metadata Schemas for Clinical Research
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  product_url: https://zenodo.org/records/8368709
  versions:
  - '8'
- category: ProcessProduct
  description: ECRIN GitHub organization holding the MDR code, including the downloader,
    harvester, importer, coder and aggregator pipeline, the Blazor portal and API
    (MDR_FuiPortal), and MDRMine, an InterMine-based successor that also loads EU
    CTR, CTIS, WHO ICTRP, BioLINCC and BBMRI-ERIC data.
  format: mixed
  id: ecrin-mdr.code
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: ECRIN MDR Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  product_url: https://github.com/ecrin-github
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - Christian Ohmann
  - Steve Canham
  - Kurt Majcen
  - Vittorio Meloni
  - Luca Pireddu
  - Alessandro Sulis
  - Giovanni Delussu
  - Francesca Frexia
  - Petr Holub
  doi: 10.12688/openreseurope.17131.2
  id: doi:10.12688/openreseurope.17131.2
  journal: Open Research Europe
  preferred: true
  title: Linking the ECRIN Metadata Repository with the BBMRI-ERIC Directory to connect
    clinical studies with related biobanks and collections
  year: '2024'
- authors:
  - Steve Canham
  - Christian Ohmann
  doi: 10.1186/s13063-016-1686-5
  id: doi:10.1186/s13063-016-1686-5
  journal: Trials
  title: A metadata schema for data objects in clinical research
  year: '2016'
repository: https://github.com/ecrin-github
synonyms:
- ECRIN MDR
- MDR
- Clinical Research Metadata Repository
---
# ECRIN Clinical Research Metadata Repository

The ECRIN MDR collects metadata about clinical studies and the data objects linked to them, such as registry entries, protocols, results summaries, journal articles and individual participant datasets. It maps records from many sources into one schema (the ECRIN metadata schema) so that users can find everything known about a study in one place.

## Sources

The MDR pipeline (`MDR_Downloader` and related repositories) obtains data from:

- ClinicalTrials.gov, through its API
- PubMed, through its API
- ISRCTN, through its XML API
- EU Clinical Trials Register (EU CTR), Yoda and BioLINCC, by scraping
- WHO ICTRP, from its CSV export

MDRMine, the InterMine-based successor under development in the same GitHub organization, also loads CTIS (the EU Clinical Trials Information System) and BBMRI-ERIC Directory data, as described in the 2024 Open Research Europe paper. ISRCTN, EU CTR, CTIS, WHO ICTRP, Yoda and BioLINCC have no KG-Registry pages yet, so only ClinicalTrials.gov and PubMed are cited as sources.

## Access

- The portal at https://newmdr.ecrin.org/ is a Blazor web application.
- Its API is documented at https://newmdr.ecrin.org/swagger/index.html (OpenAPI at `/swagger/v1/swagger.json`). For example, `/api/Study/ByRegId/NCT00000102` returns the MDR record for a ClinicalTrials.gov study, and `/api/Study/stats/total-studies-and-objects` returns record counts.
- OmicsDI indexes a subset of MDR studies through the `/api/Study/OmicsDIdata` feed.

The project wiki formerly at `ecrin-mdr.online` did not respond on 2026-10-04. The domain `crmdr.org` is unrelated to ECRIN and now hosts spam.

## License

The MDR site states no license for its aggregated metadata. The metadata schema is CC BY 4.0, and most of the code is MIT-licensed.