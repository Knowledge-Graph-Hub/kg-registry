---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: open@fda.hhs.gov
  - contact_type: url
    value: https://open.fda.gov/
  label: openFDA, U.S. Food and Drug Administration
creation_date: '2026-10-03T00:00:00Z'
description: openFDA is the U.S. Food and Drug Administration's platform for public
  access to FDA datasets through Elasticsearch-based JSON APIs and bulk downloads.
  It covers drugs, devices, foods, animal and veterinary products, cosmetics and tobacco,
  serving adverse event reports (FAERS for drugs, MAUDE for devices, CAERS for foods),
  product labeling, recalls and enforcement reports, the National Drug Code directory,
  Drugs@FDA, the Orange Book, drug shortages, device 510(k), PMA, classification,
  registration and UDI data, and substance and UNII data.
domains:
- pharmacovigilance
- pharmacology
- public health
- biomedical
- clinical
- food
- nutrition
homepage_url: https://open.fda.gov/
id: openfda
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  id: https://open.fda.gov/license/
  label: CC0 1.0 Universal
name: openFDA
products:
- category: ProgrammingInterface
  connection_url: https://api.fda.gov/
  description: JSON REST APIs (Elasticsearch query syntax) for FDA drug, device, food,
    animal and veterinary, cosmetic, tobacco and other datasets, including drug adverse
    events (FAERS), device adverse events (MAUDE), the National Drug Code directory,
    the Orange Book, UNII substance data, labeling, recalls and enforcement reports.
  format: http
  id: openfda.apis
  is_public: true
  name: openFDA APIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://open.fda.gov/apis/
- category: Product
  compression: zip
  description: Bulk downloads of every openFDA endpoint as zipped JSON files, split
    into partitions for large datasets such as drug adverse events (FAERS) and device
    adverse events (MAUDE), with a machine-readable manifest at https://api.fda.gov/download.json
    listing each endpoint's export date and file partitions.
  format: json
  id: openfda.downloads
  name: openFDA Bulk Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://open.fda.gov/data/downloads/
- category: GraphicalInterface
  description: openFDA website with API documentation, interactive query explorers
    and dataset overviews for each endpoint.
  format: http
  id: openfda.portal
  name: openFDA Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  product_url: https://open.fda.gov/
- category: Product
  description: The MAUDE medical device adverse event reports, accessible through
    the searchable web database and as downloadable data files, including via the
    openFDA device adverse event API endpoint.
  format: http
  id: maude.data
  name: MAUDE Database and Downloadable Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: openfda
  product_url: https://open.fda.gov/apis/device/event/
- category: GraphicalInterface
  description: MPS-Db web portal for browsing, analyzing and sharing microphysiology
    system study data alongside reference compound, bioactivity, preclinical and clinical
    data drawn from ChEMBL, PubChem, DrugBank, UniChem and FAERS (via OpenFDA).
  format: http
  id: mps-db.portal
  name: MPS-Db Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mps-db
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: openfda
  product_url: https://mps.csb.pitt.edu/
  warnings:
  - As of 2026-10-03 this URL redirects (HTTP 302) to EveAnalytics (eveanalytics.com),
    the commercial successor platform; the Pitt-hosted portal is no longer available.
- category: ProgrammingInterface
  description: REST API providing programmatic access to National Drug Code data through
    the openFDA platform
  format: http
  id: ndcd.api
  name: NDC API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: openfda
  product_url: https://open.fda.gov/apis/drug/ndc/
- category: GraphProduct
  description: Every OnCo record in one JSON file, each with its plain-English summary,
    technical summary, dated facts, relationship fields and source links.
  format: json
  id: onco.all_json
  name: OnCo full corpus (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: onco
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: openalex
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: wikidata
  - relation_type: prov:hadPrimarySource
    source: openfda
  product_file_size: 31490277
  product_url: https://onco.cc/api/v1/all.json
publications:
- authors:
  - Taha A Kass-Hout
  - Zhiheng Xu
  - Matthew Mohebbi
  - Hans Nelsen
  - Adam Baker
  - Jonathan Levine
  - Elaine Johanson
  - Roselie A Bright
  doi: 10.1093/jamia/ocv153
  id: doi:10.1093/jamia/ocv153
  journal: Journal of the American Medical Informatics Association
  preferred: true
  title: 'OpenFDA: an innovative platform providing access to a wealth of FDA''s publicly
    available data'
  year: '2016'
repository: https://github.com/FDA/openfda
synonyms:
- OpenFDA
---
# openFDA

openFDA is the U.S. Food and Drug Administration's platform for public access to FDA
datasets. It serves them through Elasticsearch-based JSON APIs and as bulk downloads,
covering drugs, devices, foods, animal and veterinary products, cosmetics and tobacco.

## Endpoints

On 2026-10-03 the download manifest (https://api.fda.gov/download.json) listed 31
endpoints, most exported within the previous week. They include:

- Drugs: adverse events (FAERS), labeling, NDC directory, Drugs@FDA, Orange Book,
  enforcement reports and drug shortages
- Devices: adverse events (MAUDE), 510(k), PMA, classification, registration and
  listing, recalls, enforcement reports, UDI and COVID-19 serology
- Foods: adverse events (CAERS) and enforcement reports
- Animal and veterinary adverse events, cosmetic adverse events and tobacco problem
  reports
- Other: substance data, UNII, NSDE and historical documents, plus several research
  and transparency datasets

The `drug/event` endpoint reported 20,692,690 adverse event reports (last updated
2026-07-30); its bulk download is split into 1,767 files.

## License

Per https://open.fda.gov/license/, unless otherwise noted, openFDA content, data,
documentation and code are public domain and made available under the Creative
Commons CC0 1.0 Universal dedication. Use of the service is subject to the openFDA
Terms of Service (https://open.fda.gov/terms/).
