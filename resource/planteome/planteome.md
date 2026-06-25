---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://planteome.org
  id: planteome
  label: Planteome (Oregon State University)
creation_date: '2026-06-18T00:00:00Z'
description: Planteome is an integrated resource that develops and hosts a suite of
  reference plant ontologies (including the Plant Ontology, Plant Trait Ontology,
  and Plant Experimental Conditions Ontology) alongside species-specific crop ontologies.
  It aggregates and cross-references genome and phenotype annotations from many plant
  species against these common ontologies, enabling comparative genomics and phenomics
  across taxa. The resource is maintained at Oregon State University and provides
  an AmiGO-based browser for searching ontology terms, bioentities, and annotations.
  Planteome serves as the upstream source for derived knowledge graphs such as eco-KG.
domains:
- genomics
- organisms
- agriculture
- phenotype
homepage_url: https://planteome.org
id: planteome
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Planteome
products:
- category: GraphicalInterface
  description: AmiGO-based Planteome ontology browser for searching reference and
    species-specific plant ontology terms, bioentities, and aggregated genome and
    phenotype annotations.
  format: http
  id: planteome.browser
  name: Planteome Ontology Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: planteome
  product_url: https://browser.planteome.org/amigo
- category: OntologyProduct
  description: The Plant Ontology (PO), a Planteome reference ontology describing
    plant anatomy, morphology, and developmental stages, available as an OWL download.
  format: owl
  id: planteome.po
  name: Plant Ontology (PO)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: planteome
  product_file_size: 360811
  product_url: http://purl.obolibrary.org/obo/po.owl
- category: GraphProduct
  compression: tar
  description: Knowledge graph containing plant traits data from Planteome and EOL
    TraitBank
  format: kgx
  id: eco-kg.graph
  name: eco-KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eco-kg
  - relation_type: prov:hadPrimarySource
    source: eol-traitbank
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: maizegdb
  - relation_type: prov:hadPrimarySource
    source: planteome
  - relation_type: prov:hadPrimarySource
    source: rapdb
  product_url: https://github.com/Knowledge-Graph-Hub/eco-kg
publications:
- authors:
  - Cooper L
  - Meier A
  - Laporte MA
  - Elser JL
  - Mungall C
  - Sinn BT
  - Cavaliere D
  - Carbon S
  - Dunn NA
  - Smith B
  doi: 10.1093/nar/gkx1152
  id: https://www.ncbi.nlm.nih.gov/pubmed/29186578
  journal: Nucleic Acids Res
  preferred: true
  title: 'The Planteome database: an integrated resource for reference ontologies,
    plant genomics and phenomics'
  year: '2018'
---
# Planteome

## Description

Planteome is an integrated resource that develops reference plant ontologies and aggregates genome and phenotype annotations across many plant species against those common ontologies. The reference ontologies include the Plant Ontology (PO), Plant Trait Ontology (TO), and Plant Experimental Conditions Ontology (PECO), complemented by species-specific crop ontologies. By mapping annotations from diverse taxa onto shared vocabularies, Planteome supports comparative plant genomics and phenomics. The resource is hosted at Oregon State University (planteome.org) and is the upstream source for derived knowledge graphs such as eco-KG.

## Products

- **Planteome Ontology Browser**: An AmiGO-based web interface for searching ontology terms, bioentities, and aggregated annotations.
- **Plant Ontology (PO)**: A downloadable OWL reference ontology covering plant anatomy, morphology, and developmental stages.