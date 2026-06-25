---
activity_status: active
category: Ontology
contacts:
  - category: Organization
    label: Indiana University Cyberinfrastructure for Network Science Center (CNS)
    contact_details:
      - contact_type: url
        value: "https://cns.iu.edu/"
description: The Common Coordinate Framework (CCF) Ontology is the spatial and semantic framework that underpins the Human Reference Atlas (HRA) developed within the NIH Human BioMolecular Atlas Program (HuBMAP). It encodes the relationships among anatomical structures, cell types, and biomarkers captured in the ASCT+B (Anatomical Structures, Cell Types, plus Biomarkers) tables, linking them to established ontologies such as Uberon, FMA, and Cell Ontology. The CCF also provides a spatial component that supports 3D spatial registration of tissue samples to reference organs via the CCF Registration User Interface, giving each sample a defined location in a common coordinate system. Together these clinical, semantic, and spatial layers serve as a primary upstream source for the HRA Knowledge Graph (HRA-KG).
domains:
  - anatomy and development
  - biomedical
homepage_url: https://humanatlas.io/ccf-ontology
id: "ccf"
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: "https://creativecommons.org/licenses/by/4.0/"
  label: CC BY 4.0
name: Common Coordinate Framework Ontology
products:
  - category: OntologyProduct
    description: The Common Coordinate Framework (CCF) Ontology in OWL (RDF/XML) format, integrating ASCT+B anatomical structures, cell types, and biomarkers with the CCF spatial model for the Human Reference Atlas.
    format: owl
    id: "ccf.owl"
    name: CCF Ontology (OWL)
    product_url: https://cdn.humanatlas.io/digital-objects/graph/ccf/latest/assets/ccf.owl
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ccf
publications:
  - authors:
      - "Börner K"
      - "Teichmann SA"
      - "Quardokus EM"
      - "Gee JC"
    doi: "10.1038/s41556-021-00788-6"
    id: "https://pubmed.ncbi.nlm.nih.gov/34750582"
    journal: Nat Cell Biol
    preferred: true
    title: Anatomical structures, cell types and biomarkers of the Human Reference Atlas
    year: "2021"
creation_date: '2026-06-18T00:00:00Z'
---

## Description

The **Common Coordinate Framework (CCF) Ontology** is the spatial and semantic backbone
of the **Human Reference Atlas (HRA)**, built within the NIH **Human BioMolecular Atlas
Program (HuBMAP)**. It brings together three complementary layers: a semantic layer that
describes anatomical structures, cell types, and biomarkers via the **ASCT+B** tables
(linked to Uberon, FMA, Cell Ontology, HGNC, and related ontologies); a spatial layer
that places tissue blocks and organs in a shared 3D coordinate system; and clinical
metadata about specimens and donors. Spatial registration of tissue samples to reference
organs is performed through the **CCF Registration User Interface**.

As an upstream source for the **HRA Knowledge Graph (HRA-KG)**, the CCF Ontology supplies
the standardized terms and spatial relationships that allow cross-scale biological queries
spanning whole organs down to individual cells.

## Products

- **CCF Ontology (OWL)** — the ontology in OWL (RDF/XML) format, served from the Human
  Reference Atlas CDN at
  `https://cdn.humanatlas.io/digital-objects/graph/ccf/latest/assets/ccf.owl`.
