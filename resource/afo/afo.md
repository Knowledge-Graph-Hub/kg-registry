---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.allotrope.org/
  label: Allotrope Foundation
creation_date: '2026-06-02T00:00:00Z'
description: The Allotrope Foundation Ontology (AFO) is a suite of ontologies and
  controlled vocabularies from the Allotrope Foundation for representing laboratory
  analytical instruments, processes, materials, results, and related scientific data.
domains:
- chemistry and biochemistry
- information technology
homepage_url: https://www.allotrope.org/product-releases
id: afo
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Allotrope Foundation Ontology
products:
- category: OntologyProduct
  description: Allotrope Foundation Ontology release information and access page for
    current AFO product releases.
  format: http
  id: afo.release
  latest_version: 2026/03
  name: AFO Release Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afo
  product_url: https://www.allotrope.org/product-releases
- category: GraphicalInterface
  description: Ontobee browser page for the Allotrope Foundation Ontology.
  format: http
  id: afo.ontobee
  name: AFO Ontobee Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afo
  product_url: https://ontobee.org/ontology/AFO
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
synonyms:
- AFO
warnings:
- Allotrope release packages may require access through Allotrope Foundation release
  pages rather than stable direct public ontology-file URLs.
---
# Allotrope Foundation Ontology

AFO provides controlled vocabulary and ontology terms for Allotrope laboratory data models, including analytical instruments, processes, materials, and measurement results.