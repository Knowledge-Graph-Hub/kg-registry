---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@re3data.org
  - contact_type: url
    value: https://www.re3data.org/contact
  label: DataCite
creation_date: '2026-10-04T00:00:00Z'
description: re3data (Registry of Research Data Repositories) is a global registry
  of research data repositories from all academic disciplines, launched in 2012 and
  operated by DataCite. Each repository is described with a detailed metadata schema
  covering its subjects, content types, access and upload conditions, data licenses,
  persistent identifier systems, certification and responsible institutions, and receives
  a re3data identifier and DOI. Metadata are available through a web portal, a REST
  API returning XML and a daily bulk XML export, all released under CC0.
domains:
- metadata
- information technology
- scholarly communication
- literature
homepage_url: https://www.re3data.org/
id: re3data
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: re3data
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing re3data repository records by
    subject, country, content type and other facets, and for suggesting new repositories.
  format: http
  id: re3data.portal
  name: re3data Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: re3data
  product_url: https://www.re3data.org/
- category: ProgrammingInterface
  description: Versioned REST API (with a separate OpenSearch implementation) returning
    re3data repository metadata as XML; for example, /api/v1/repositories lists all
    repositories and /api/v1/repository/{id} returns a full record in the re3data
    metadata schema.
  format: http
  id: re3data.api
  name: re3data API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: re3data
  product_url: https://www.re3data.org/api/doc
- category: Product
  compression: zip
  description: Daily export of all online re3data repository records as XML files
    in a single zip archive (about 7 MB), with monthly archived snapshots also listed
    on the data download page.
  format: xml
  id: re3data.export
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: re3data Repositories XML Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: re3data
  product_file_size: 7358935
  product_url: https://www.re3data.org/export/re3data-repositories.zip
- category: DataModelProduct
  description: XML Schema (XSD) for version 4.0 of the re3data Metadata Schema for
    the Description of Research Data Repositories, released in 2023.
  format: xml
  id: re3data.schema
  name: re3data Metadata Schema 4.0 XSD
  original_source:
  - relation_type: prov:hadPrimarySource
    source: re3data
  product_file_size: 160310
  product_url: https://schema.re3data.org/4-0/re3dataV4-0.xsd
- category: DocumentationProduct
  description: Documentation of version 4.0 of the re3data Metadata Schema for the
    Description of Research Data Repositories, describing each property and its controlled
    vocabularies (DOI 10.48440/re3.014).
  format: http
  id: re3data.schema-docs
  name: re3data Metadata Schema 4.0 Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: re3data
  product_url: https://doi.org/10.48440/re3.014
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-05: Timeout connecting
    to URL'
- category: DocumentationProduct
  description: re3data API documentation describing the OpenSearch and RESTful interfaces,
    versioning and the metadata schema versions served.
  format: http
  id: re3data.api-docs
  name: re3data API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: re3data
  product_url: https://www.re3data.org/api/doc
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including
    names, synonyms, URI formats, local identifier patterns, providers and mappings
    to the prefixes of other registries.
  format: json
  id: bioregistry.registry.json
  name: Bioregistry JSON Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes
    in other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology
    registry, Cellosaurus, UniProt and NCBI.
  format: sssom
  id: bioregistry.sssom
  name: Bioregistry SSSOM Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
publications:
- authors:
  - Heinz Pampel
  - Paul Vierkant
  - Frank Scholze
  - Roland Bertelmann
  - Maxi Kindling
  - Jens Klump
  - Hans-Jürgen Goebelbecker
  - Jens Gundlach
  - Peter Schirmbacher
  - Uwe Dierolf
  doi: 10.1371/journal.pone.0078080
  id: doi:10.1371/journal.pone.0078080
  journal: PLoS ONE
  preferred: true
  title: 'Making Research Data Repositories Visible: The re3data.org Registry'
  year: '2013'
- authors:
  - Heinz Pampel
  - Nina Leonie Weisweiler
  - Dorothea Strecker
  - Michael Witt
  - Paul Vierkant
  - Kirsten Elger
  - Roland Bertelmann
  - Matthew Buys
  - Lea Maria Ferguson
  - Maxi Kindling
  - Rachael Kotarski
  - Vivien Petras
  doi: 10.1038/s41597-023-02462-y
  id: doi:10.1038/s41597-023-02462-y
  journal: Scientific Data
  title: re3data – Indexing the Global Research Data Repository Landscape Since 2012
  year: '2023'
synonyms:
- re3data.org
- Registry of Research Data Repositories
---
# re3data

re3data (Registry of Research Data Repositories) is a global, cross-disciplinary index of research data repositories. It started in 2012 as a German Research Foundation (DFG) funded project and is now a DataCite service. Each repository record gets a re3data identifier (such as `r3d100000001`) and a DOI, and is described using the re3data Metadata Schema, currently version 4.0.

Records cover a repository's subjects, content and data types, access and upload conditions, data licenses, persistent identifier systems, certifications, APIs and responsible institutions. Version 4.0 of the schema added properties for related repositories and funding information.

## Access

- **Web portal**: search and browse at [re3data.org](https://www.re3data.org/).
- **API**: an OpenSearch interface and a versioned REST API returning XML (for example `https://www.re3data.org/api/v1/repositories`).
- **Bulk export**: a daily zip of all online repository records as XML, plus monthly archived snapshots, from the [data download page](https://www.re3data.org/data).

Database metadata are released under CC0; other site content is under CC BY 4.0.