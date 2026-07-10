---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://gcmd.earthdata.nasa.gov/
  label: NASA Earth Science Data Systems (GCMD)
creation_date: '2026-07-03T00:00:00Z'
description: The Global Change Master Directory (GCMD) Keywords are NASA's hierarchical
  controlled vocabulary of Earth science keywords, covering science topics, instruments,
  platforms, data centers, locations, and related concepts. GCMD Keywords are widely
  used to describe and discover Earth science datasets and serve as the taxonomic
  backbone for climate metadata.
domains:
- environment
- information technology
- general
homepage_url: https://gcmd.earthdata.nasa.gov/
id: gcmd
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: NASA Global Change Master Directory (GCMD) Keywords
products:
- category: Product
  description: The GCMD Keyword Viewer provides browsable access to NASA's hierarchical
    Earth science controlled vocabulary, including science keywords, instruments,
    platforms, providers, and locations.
  format: http
  id: gcmd.keywords
  name: GCMD Keyword Viewer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gcmd
  product_url: https://gcmd.earthdata.nasa.gov/KeywordViewer/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-03: Error connecting
    to URL: HTTPSConnectionPool(host=''gcmd.earthdata.nasa.gov'', port=443): Max retries
    exceeded with url: /KeywordViewer/ (Caused by NewConnectionError("HTTPSConnection(host=''gcmd.earthdata.nasa.gov'',
    port=443): Failed to establish a new connection: [Errno 101] Network is unreachable"))'
  - 'File was not able to be retrieved when checked on 2026-07-10: Error connecting
    to URL: HTTPSConnectionPool(host=''gcmd.earthdata.nasa.gov'', port=443): Max retries
    exceeded with url: /KeywordViewer/ (Caused by NewConnectionError("HTTPSConnection(host=''gcmd.earthdata.nasa.gov'',
    port=443): Failed to establish a new connection: [Errno 101] Network is unreachable"))'
- category: GraphProduct
  description: RDF/Turtle knowledge graph integrating climate model and dataset metadata
    (from ESGF, CMIP controlled vocabularies, and the NASA GCMD keyword taxonomy)
    with entities and relationships extracted from climate-science publications. Served
    through the FRINK federation and the SPARQL and TPF endpoints.
  format: ttl
  id: climatemodelskg.graph
  name: Climate Models KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: climatemodelskg
  - relation_type: prov:hadPrimarySource
    source: esgf
  - relation_type: prov:hadPrimarySource
    source: cmip
  - relation_type: prov:hadPrimarySource
    source: gcmd
  product_url: https://frink.renci.org/registry/kgs/climatepub4-kg/
---
## Description

The Global Change Master Directory (GCMD) Keywords are NASA's hierarchical
controlled vocabulary for describing Earth science data. The vocabulary spans
science keywords, instruments, platforms, data centers/providers, locations, and
related concepts, and is maintained by NASA's Earth Science Data Systems program
through its Keyword Management System. GCMD Keywords are a standard basis for
tagging and discovering Earth science and climate datasets.

## Products

### GCMD Keyword Viewer

Browsable interface to NASA's hierarchical Earth science controlled vocabulary.

**URL**: [https://gcmd.earthdata.nasa.gov/KeywordViewer/](https://gcmd.earthdata.nasa.gov/KeywordViewer/)

**Format**: http
</content>
</invoke>