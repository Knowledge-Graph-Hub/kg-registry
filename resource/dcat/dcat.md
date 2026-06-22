---
activity_status: active
category: DataModel
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.w3.org/
  label: World Wide Web Consortium
creation_date: '2026-06-02T00:00:00Z'
description: The Data Catalog Vocabulary (DCAT) is a W3C RDF vocabulary designed to
  support interoperability between data catalogs published on the Web.
domains:
- information technology
- general
homepage_url: https://www.w3.org/TR/vocab-dcat-3/
id: dcat
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Data Catalog Vocabulary
products:
- category: DataModelProduct
  description: Turtle serialization of the W3C Data Catalog Vocabulary namespace.
  id: dcat.ttl
  latest_version: '3'
  name: DCAT Turtle Vocabulary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dcat
  product_file_size: 200345
  product_url: https://www.w3.org/ns/dcat.ttl
- category: DocumentationProduct
  description: W3C Recommendation for Data Catalog Vocabulary version 3.
  format: http
  id: dcat.spec
  latest_version: '3'
  name: DCAT Version 3 Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dcat
  product_url: https://www.w3.org/TR/vocab-dcat-3/
- category: GraphProduct
  description: RDF knowledge graph materialized by the MetaBoKG workflow from public
    metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence,
    sample metadata, and environmental and taxonomic context. The repository documents
    generated per-job Turtle files under mapping/kg and loading into Virtuoso named
    graphs.
  format: mixed
  id: metabokg.graph
  latest_version: arXiv v1 demonstration
  name: MetaboKG RDF Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: redu
  product_url: https://github.com/HolobiomicsLab/MetaBoKG
  secondary_source:
  - relation_type: prov:used
    source: ms
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
  - relation_type: prov:used
    source: envo
  - relation_type: prov:used
    source: ncit
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: chmo
  - relation_type: prov:used
    source: sio
  - relation_type: prov:used
    source: prov-o
  - relation_type: prov:used
    source: dcat
  - relation_type: prov:used
    source: afo
  warnings:
  - No static public graph release or hosted endpoint was available in the GitHub
    repository when curated on 2026-06-02; the repository documents local Turtle materialization
    and Virtuoso loading.
- category: DataModelProduct
  description: Turtle schema files defining MetaBoKG classes, properties, and ReDU
    class hierarchies used by the generated knowledge graph.
  format: ttl
  id: metabokg.schema
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache License 2.0
  name: MetaBoKG RDF Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  product_url: https://github.com/HolobiomicsLab/MetaBoKG/tree/main/Schema
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: ms
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: envo
  - relation_type: prov:wasInformedBy
    source: ncit
  - relation_type: prov:wasInformedBy
    source: uberon
  - relation_type: prov:wasInformedBy
    source: chmo
  - relation_type: prov:wasInformedBy
    source: sio
  - relation_type: prov:wasInformedBy
    source: prov-o
  - relation_type: prov:wasInformedBy
    source: dcat
  - relation_type: prov:wasInformedBy
    source: afo
publications:
- authors:
  - Riccardo Albertoni
  - David Browning
  - Simon Cox
  - Alejandra Gonzalez Beltran
  - Andrea Perego
  - Peter Winstanley
  id: https://www.w3.org/TR/vocab-dcat-3/
  journal: W3C Recommendation
  preferred: true
  title: Data Catalog Vocabulary (DCAT) - Version 3
  year: '2024'
synonyms:
- DCAT
---
# Data Catalog Vocabulary

DCAT is a W3C RDF vocabulary for describing datasets, data services, and catalogs so that data catalogs can interoperate on the Web.