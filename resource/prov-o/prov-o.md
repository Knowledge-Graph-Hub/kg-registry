---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.w3.org/
  label: World Wide Web Consortium
creation_date: '2026-06-02T00:00:00Z'
description: PROV-O is the W3C PROV Ontology, an OWL2 ontology for representing provenance
  information and mapping the PROV data model into RDF/OWL.
domains:
- information technology
- general
homepage_url: https://www.w3.org/TR/prov-o/
id: prov-o
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: PROV-O
products:
- category: OntologyProduct
  description: OWL serialization of the W3C PROV Ontology.
  format: owl
  id: prov-o.owl
  name: PROV-O OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prov-o
  product_file_size: 112346
  product_url: https://www.w3.org/ns/prov-o.owl
- category: DocumentationProduct
  description: W3C Recommendation for PROV-O, the PROV Ontology.
  format: http
  id: prov-o.spec
  latest_version: W3C Recommendation 2013-04-30
  name: PROV-O Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prov-o
  product_url: https://www.w3.org/TR/prov-o/
- category: GraphProduct
  description: RDF knowledge graph materialized by the MetaBoKG workflow from public
    metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence,
    sample metadata, and environmental and taxonomic context. The repository documents
    generated per-job Turtle files under mapping/kg and loading into Virtuoso named
    graphs.
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
  - Timothy Lebo
  - Satya Sahoo
  - Deborah McGuinness
  id: https://www.w3.org/TR/prov-o/
  journal: W3C Recommendation
  preferred: true
  title: 'PROV-O: The PROV Ontology'
  year: '2013'
synonyms:
- PROV Ontology
- W3C PROV Ontology
---
# PROV-O

PROV-O is the W3C ontology for expressing provenance in RDF and OWL.