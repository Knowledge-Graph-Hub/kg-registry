---
activity_status: active
category: Ontology
creation_date: '2026-06-15T00:00:00Z'
description: The BioAssay Ontology (BAO) is a formal OWL-DL ontology that establishes common reference metadata terms and definitions for describing low- and high-throughput drug and probe screening assays and their results. It captures assay design, screening formats, detection technologies, perturbagens, biological targets, endpoints, and measured results, enabling integration, aggregation, retrieval, and analysis of bioassay data across resources such as PubChem and ChEMBL. BAO is modularized into reusable components covering biology, properties, and controlled vocabularies.
domains:
  - drug discovery
  - pharmacology
  - biomedical
homepage_url: http://bioassayontology.org/
id: bao
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: BioAssay Ontology
products:
  - category: OntologyProduct
    description: The complete BioAssay Ontology in OWL format, integrating the core ontology with its biology, properties, and vocabulary modules.
    format: owl
    id: bao.complete-owl
    name: BAO complete OWL
    original_source:
      - relation_type: prov:hadPrimarySource
        source: bao
    product_url: https://raw.githubusercontent.com/BioAssayOntology/BAO/master/bao_complete.owl
  - category: OntologyProduct
    description: The core BioAssay Ontology module in OWL format, containing the foundational BAO classes and relations.
    format: owl
    id: bao.core-owl
    name: BAO core OWL
    original_source:
      - relation_type: prov:hadPrimarySource
        source: bao
    product_url: https://raw.githubusercontent.com/BioAssayOntology/BAO/master/bao_core.owl
  - category: GraphicalInterface
    description: The BioAssay Ontology project website, providing documentation, background, and access to BAO releases and tools.
    format: http
    id: bao.website
    name: BioAssay Ontology website
    original_source:
      - relation_type: prov:hadPrimarySource
        source: bao
    product_url: http://bioassayontology.org/
publications:
  - authors:
      - Ubbo Visser
      - Saminda Abeyruwan
      - Uma Vempati
      - Robin P Smith
      - Vance Lemmon
      - Stephan C Schürer
    doi: doi:10.1186/1471-2105-12-257
    id: doi:10.1186/1471-2105-12-257
    journal: BMC Bioinformatics
    preferred: true
    title: 'BioAssay Ontology (BAO): a semantic description of bioassays and high-throughput screening results'
    year: '2011'
  - authors:
      - Saminda Abeyruwan
      - Uma D Vempati
      - Hande Küçük-McGinty
      - Ubbo Visser
      - Amar Koleti
      - Ahsan Mir
      - Kunie Sakurai
      - Caty Chung
      - Joshua A Bittker
      - Paul A Clemons
      - Steve Brudz
      - Anosha Siripala
      - Arturo J Morales
      - Martin Romacker
      - David Twomey
      - Svetlana Bureeva
      - Vance Lemmon
      - Stephan C Schürer
    doi: doi:10.1186/2041-1480-5-S1-S5
    id: doi:10.1186/2041-1480-5-S1-S5
    journal: Journal of Biomedical Semantics
    title: 'Evolving BioAssay Ontology (BAO): modularization, integration and applications'
    year: '2014'
repository: https://github.com/BioAssayOntology/BAO
---

# BioAssay Ontology

The BioAssay Ontology (BAO) is a formal OWL-DL ontology that establishes common
reference metadata terms and definitions for describing low- and high-throughput
drug and probe screening assays and their results. It captures assay design,
screening formats, detection technologies, perturbagens, biological targets,
endpoints, and measured results.

BAO enables effective integration, aggregation, retrieval, and analysis of
bioassay data across resources such as PubChem and ChEMBL. The ontology is
modularized into reusable components covering biology, properties, and
controlled vocabularies, and is distributed as a complete OWL file alongside its
individual modules.
