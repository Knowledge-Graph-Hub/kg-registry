---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: The Research Organization Registry is a global, community-led registry of open persistent identifiers and metadata for research and funding organizations.
domains:
- research funding
- literature
- scholarly communication
- general
homepage_url: https://ror.org/
id: "ror"
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
license:
  id: "https://creativecommons.org/publicdomain/zero/1.0/"
  label: CC0-1.0
name: Research Organization Registry
contacts:
  - category: Organization
    label: ROR
    contact_details:
      - contact_type: email
        value: "support@ror.org"
      - contact_type: github
        value: ror-community
repository: https://github.com/ror-community
rrid: SCR_021891
synonyms:
  - ROR
publications:
  - authors:
      - Lammey R
    doi: 10.6087/kcse.192
    id: doi:10.6087/kcse.192
    journal: Science Editing
    title: 'Solutions for identification problems: a look at the Research Organization Registry'
    year: '2020'
products:
  - category: GraphicalInterface
    description: Web interface for searching and browsing ROR organization records by name, identifier, location, and other attributes.
    format: http
    id: "ror.search"
    name: ROR Search
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ror
    product_url: https://ror.org/search
  - category: ProgrammingInterface
    description: Open REST API (v2) for searching and retrieving ROR organization records, including keyword and external identifier search (GRID, ISNI, Wikidata, Crossref Funder ID), advanced filtering, and matching of free-text affiliation strings to ROR IDs. No registration is required; requests are rate-limited per IP address.
    format: http
    id: "ror.api"
    name: ROR REST API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ror
      - relation_type: prov:wasInformedBy
        source: wikidata
    product_url: https://api.ror.org/v2/organizations
    repository: https://github.com/ror-community/ror-api
  - category: Product
    description: Full ROR registry data dump, released on Zenodo at least monthly as a zip containing JSON (format of record) and CSV files in ROR Schema 2.x.
    format: mixed
    id: "ror.data-dump"
    name: ROR Data Dump
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ror
    product_url: https://doi.org/10.5281/zenodo.6347574
  - category: DocumentationProduct
    description: Technical documentation for ROR, covering the REST API, affiliation matching, the data dump, and the ROR record schema.
    format: http
    id: "ror.docs"
    name: ROR Technical Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ror
    product_url: https://ror.readme.io/
    repository: https://github.com/ror-community/ror-docs
  - category: Product
    description: ror Nodes TSV
    format: tsv
    id: "obo-db-ingest.ror.tsv"
    license:
      id: "https://creativecommons.org/publicdomain/zero/1.0/"
      label: CC0-1.0
    name: ror Nodes TSV
    original_source:
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
      - relation_type: prov:hadPrimarySource
        source: ror
    product_file_size: 5381101
    product_url: https://w3id.org/biopragmatics/resources/ror/ror.tsv

  - category: Product
    description: ror OBO
    format: obo
    id: obo-db-ingest.ror.obo
    license:
      id: https://creativecommons.org/publicdomain/zero/1.0/
      label: CC0-1.0
    name: ror OBO
    original_source:
    - relation_type: prov:hadPrimarySource
      source: obo-db-ingest
    - relation_type: prov:hadPrimarySource
      source: ror
    product_file_size: 9684743
    product_url: https://w3id.org/biopragmatics/resources/ror/ror.obo
  - category: Product
    compression: gzip
    description: ror OWL
    format: owl
    id: obo-db-ingest.ror.owl
    license:
      id: https://creativecommons.org/publicdomain/zero/1.0/
      label: CC0-1.0
    name: ror OWL
    original_source:
    - relation_type: prov:hadPrimarySource
      source: obo-db-ingest
    - relation_type: prov:hadPrimarySource
      source: ror
    product_file_size: 14168326
    product_url: https://w3id.org/biopragmatics/resources/ror/ror.owl.gz
  - category: Product
    compression: gzip
    description: ror OBO Graph JSON
    format: json
    id: obo-db-ingest.ror.json
    license:
      id: https://creativecommons.org/publicdomain/zero/1.0/
      label: CC0-1.0
    name: ror OBO Graph JSON
    original_source:
    - relation_type: prov:hadPrimarySource
      source: obo-db-ingest
    - relation_type: prov:hadPrimarySource
      source: ror
    product_file_size: 13799938
    product_url: https://w3id.org/biopragmatics/resources/ror/ror.json.gz
  - category: MappingProduct
    description: ror SSSOM
    format: sssom
    id: obo-db-ingest.ror.sssom.tsv
    license:
      id: https://creativecommons.org/publicdomain/zero/1.0/
      label: CC0-1.0
    name: ror SSSOM
    original_source:
    - relation_type: prov:hadPrimarySource
      source: obo-db-ingest
    - relation_type: prov:hadPrimarySource
      source: ror
    product_file_size: 2333177
    product_url: https://w3id.org/biopragmatics/resources/ror/ror.sssom.tsv
---

# Research Organization Registry

The Research Organization Registry (ROR) is a community-led registry of open, persistent identifiers for research organizations, including universities, research institutes, facilities, government agencies, and funders. Each record carries a ROR ID along with metadata such as names and aliases, location, organization type, website, relationships to other organizations, and cross-references to other identifier systems (GRID, ISNI, Wikidata, and Crossref Funder ID).

ROR is operated jointly by the California Digital Library, Crossref, and DataCite. It launched in 2019 with seed data from the Global Research Identifier Database (GRID) and has been the successor to GRID for open organization identifiers since 2022. It is designed primarily for the affiliation use case: linking researchers and research outputs to the organizations they are associated with, in place of free-text affiliation strings.

## Access

- **Search**: web interface at https://ror.org/search
- **REST API**: `https://api.ror.org/v2/organizations`, with query, advanced query, and affiliation-matching parameters. No registration is required; documentation is at https://ror.readme.io/docs/rest-api
- **Data dump**: the full registry is released on Zenodo (https://doi.org/10.5281/zenodo.6347574) at least monthly. JSON is the format of record; CSV is provided as a convenience subset. Releases after v1.74 use Schema 2.x only.
- **Source code and curation**: https://github.com/ror-community. Requests to add or update records are tracked in the `ror-updates` repository and reviewed through a community curation process.

All ROR IDs and metadata are released under CC0 1.0.
