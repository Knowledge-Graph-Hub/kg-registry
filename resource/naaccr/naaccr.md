---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.naaccr.org/
  label: North American Association of Central Cancer Registries (NAACCR)
creation_date: '2026-06-18T00:00:00Z'
description: The North American Association of Central Cancer Registries (NAACCR)
  is a collaborative umbrella organization for cancer registries, governmental agencies,
  and professional associations across North America. NAACCR develops and maintains
  the standardized NAACCR data standards and data dictionary used for the consistent
  collection, coding, and exchange of cancer incidence records by central cancer registries.
  These standards define the data items, codes, and record layouts used to capture
  cancer surveillance data across registries.
domains:
- clinical
- public health
- biomedical
- information technology
homepage_url: https://www.naaccr.org/
id: naaccr
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.naaccr.org/data-standards-data-dictionary/
  label: NAACCR copyright; see terms
name: North American Association of Central Cancer Registries
products:
- category: GraphicalInterface
  description: Interactive NAACCR Data Dictionary providing browsable access to the
    standardized data items, codes, and definitions used in cancer registry records.
  format: http
  id: naaccr.data-dictionary
  name: NAACCR Data Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: naaccr
  product_url: https://apps.naaccr.org/data-dictionary/
- category: DocumentationProduct
  description: NAACCR Standards for Cancer Registries documentation and data standards
    version archive describing the data dictionary releases and record specifications.
  format: http
  id: naaccr.standards
  name: NAACCR Data Standards and Data Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: naaccr
  product_url: https://www.naaccr.org/data-standards-data-dictionary-version-archive/
- category: GraphProduct
  description: RDF-based knowledge graph containing 374,682 unique tumor records from
    Louisiana Tumor Registry (2000-2016) with 240 columns of NAACCR-standardized cancer
    data including demographics, tumor characteristics, treatment, and outcomes. Contains
    90,673,527 triples stored in Virtuoso triplestore with SPARQL endpoint access.
  id: cancer-registry-kg.ltr
  name: Louisiana Tumor Registry Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cancer-registry-kg
  - relation_type: prov:hadPrimarySource
    source: louisiana-tumor-registry
  - relation_type: prov:hadPrimarySource
    source: naaccr
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 405 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: GraphProduct
  description: RDF-based knowledge graph containing 207,766 unique tumor records from
    Kentucky Cancer Registry (2010-2016) with 232 columns of cancer data. Contains
    48,409,945 triples demonstrating the framework's ability to dynamically integrate
    multiple registry datasets without code changes.
  id: cancer-registry-kg.kcr
  name: Kentucky Cancer Registry Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cancer-registry-kg
  - relation_type: prov:hadPrimarySource
    source: kentucky-cancer-registry
  - relation_type: prov:hadPrimarySource
    source: naaccr
  product_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8324069/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 405 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
---
# North American Association of Central Cancer Registries

The North American Association of Central Cancer Registries (NAACCR) maintains
the standardized cancer registry data dictionary and data standards used for the
coding and exchange of cancer incidence records. These standards are an upstream
data source for the Cancer Registry Knowledge Graph.