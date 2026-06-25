---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.lungmap.net/contact/
  label: LungMAP Consortium
creation_date: '2026-06-18T00:00:00Z'
description: The LungMAP Human Anatomy (LMHA) ontology is a controlled vocabulary
  of human lung anatomy developed by the NHLBI Molecular Atlas of Lung Development
  Program (LungMAP) consortium. It provides structured terms and relationships
  covering anatomical structures and cell types of the developing (fetal and
  postnatal) and adult human lung, organized for use in lung development research
  and tissue annotation. LMHA is used by the Human Reference Atlas (HRA) to link
  lung cell-type terms in its ASCT+B tables and is integrated as an upstream
  vocabulary in the HRA Knowledge Graph (HRA-KG). The ontology was authored by
  the LungMAP Ontology Subcommittee and is distributed in OWL/RDF.
domains:
- anatomy and development
- biomedical
- organisms
homepage_url: https://github.com/duke-lungmap-team/lung_ontology
id: lmha
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: LungMAP Human Anatomy Ontology
products:
- category: OntologyProduct
  description: The LMHA (LungMAP Human Anatomy) ontology graph data, v1.4, as
    integrated and published by the Human Reference Atlas Knowledge Graph, in
    Turtle format. Licensed CC BY 4.0; publisher HuBMAP.
  format: ttl
  id: lmha.graph.ttl
  name: LMHA ontology graph data, v1.4, Turtle format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lmha
  product_url: https://cdn.humanatlas.io/digital-objects/vocab/lmha/latest/graph.ttl
- category: OntologyProduct
  description: The LMHA (LungMAP Human Anatomy) ontology graph data, v1.4, as
    published by the Human Reference Atlas Knowledge Graph, in RDF/XML format.
  format: rdfxml
  id: lmha.graph.xml
  name: LMHA ontology graph data, v1.4, RDF/XML format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lmha
  product_url: https://cdn.humanatlas.io/digital-objects/vocab/lmha/latest/graph.xml
- category: OntologyProduct
  description: The source LungMAP lung ontology OWL file maintained by the
    Duke LungMAP team, the upstream artifact from which the LMHA anatomy terms
    are derived.
  format: owl
  id: lmha.source.owl
  name: LungMAP lung ontology OWL source file
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lmha
  product_url: https://raw.githubusercontent.com/duke-lungmap-team/lung_ontology/master/lung_ontology.owl
- category: GraphicalInterface
  description: The LungMAP Ontology Browser, a web interface for browsing the
    LungMAP human lung anatomy and cell-type ontology terms.
  format: http
  id: lmha.browser
  name: LungMAP Ontology Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lmha
  product_url: https://www.lungmap.net/resources/ontology-browser/
---

## Description

The **LungMAP Human Anatomy (LMHA)** ontology is a controlled vocabulary of
human lung anatomy created by the **NHLBI Molecular Atlas of Lung Development
Program (LungMAP)** consortium. It captures anatomical structures and cell
types of the **developing (fetal and postnatal) and adult human lung**, with
defined relationships suited to lung development research and tissue
annotation.

LMHA is an **upstream source of the Human Reference Atlas Knowledge Graph
(HRA-KG)**: the HRA uses LMHA to link lung cell-type terms in its ASCT+B
tables, and the HRA-KG republishes LMHA as a versioned vocabulary (currently
v1.4) under a CC BY 4.0 license. The underlying ontology is authored by the
LungMAP Ontology Subcommittee and maintained in OWL/RDF by the Duke LungMAP
team.

## Products

- **LMHA ontology graph data (Turtle, RDF/XML)** — the HRA-published v1.4 LMHA
  graph, served from the Human Reference Atlas CDN.
- **LungMAP lung ontology OWL source file** — the upstream OWL artifact
  maintained by the Duke LungMAP team on GitHub.
- **LungMAP Ontology Browser** — a web interface for exploring LungMAP lung
  anatomy and cell-type terms.
</content>
</invoke>
