---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.rd-alliance.org/groups/interoperable-descriptions-observable-property-terminology-wg-i-adopt-wg/
  - contact_type: github
    value: i-adopt
  label: RDA InteroperAble Descriptions of Observable Property Terminology (I-ADOPT)
    WG
- category: Individual
  label: Barbara Magagna
  orcid: 0000-0003-2195-3997
creation_date: '2026-10-05T00:00:00Z'
description: The I-ADOPT Framework ontology, developed by the Research Data Alliance
  I-ADOPT Working Group, decomposes descriptions of observable properties (variables)
  into atomic components such as the property, the object of interest, the matrix,
  the context object and constraints. These components can be mapped to terms in existing
  FAIR vocabularies, which helps align environmental and other scientific variable
  terminologies and supports machine-readable variable descriptions. The ontology
  is released under CC BY 4.0.
domains:
- environment
- information technology
- metadata
homepage_url: https://i-adopt.github.io/index.html
id: i-adopt
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: I-ADOPT Framework Ontology
products:
- category: OntologyProduct
  description: I-ADOPT Framework ontology in Turtle format, as published at the w3id.org/iadopt/ont
    namespace (version 1.1.0 when checked).
  format: ttl
  id: i-adopt.ttl
  name: I-ADOPT Framework Ontology (Turtle)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: i-adopt
  product_file_size: 21645
  product_url: https://i-adopt.github.io/ontology/ontology.ttl
- category: OntologyProduct
  description: I-ADOPT Framework ontology in OWL (RDF/XML) format, as published at
    the w3id.org/iadopt/ont namespace.
  format: owl
  id: i-adopt.owl
  name: I-ADOPT Framework Ontology (OWL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: i-adopt
  product_file_size: 20255
  product_url: https://i-adopt.github.io/ontology/ontology.owl
- category: OntologyProduct
  description: I-ADOPT Framework ontology in JSON-LD format, as published at the w3id.org/iadopt/ont
    namespace.
  format: jsonld
  id: i-adopt.jsonld
  name: I-ADOPT Framework Ontology (JSON-LD)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: i-adopt
  product_file_size: 14932
  product_url: https://i-adopt.github.io/ontology/ontology.jsonld
- category: OntologyProduct
  description: Extended version of the I-ADOPT Framework ontology in Turtle format,
    adding formal class definitions and logical restrictions.
  format: ttl
  id: i-adopt.extended.ttl
  name: I-ADOPT Framework Ontology Extended (Turtle)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: i-adopt
  product_file_size: 30446
  product_url: https://raw.githubusercontent.com/i-adopt/ontology/main/ontology/i-adopt_extended.ttl
- category: DocumentationProduct
  description: WIDOCO-generated HTML documentation of the I-ADOPT Framework ontology,
    with class and property descriptions, examples and a WebVOWL visualization.
  format: http
  id: i-adopt.docs
  name: I-ADOPT Framework Ontology Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: i-adopt
  product_file_size: 3227
  product_url: https://w3id.org/iadopt/ont
- category: DocumentationProduct
  description: RDA-endorsed I-ADOPT WG Outputs and Recommendations document (2022),
    describing the I-ADOPT Framework, its components and usage guidance, released
    under CC BY 4.0.
  format: pdf
  id: i-adopt.recommendations
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: I-ADOPT WG Outputs and Recommendations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: i-adopt
  product_file_size: 532093
  product_url: https://zenodo.org/records/6520132/files/I_ADOPT_recommendations.pdf
- category: ProcessProduct
  description: GitHub repository holding the I-ADOPT ontology sources, archived versions,
    extension proposals and the scripts and WIDOCO configuration used to build the
    documentation.
  format: http
  id: i-adopt.repo
  name: I-ADOPT Ontology GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: i-adopt
  product_url: https://github.com/i-adopt/ontology
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of I-ADOPT Framework Ontology (I-ADOPT), produced
    by KG-Bioportal from the BioPortal submission. The archive contains I-ADOPT_nodes.tsv
    and I-ADOPT_edges.tsv.
  edge_count: 48
  format: kgx
  id: i-adopt.kg-bioportal
  latest_version: 1.1.0
  name: I-ADOPT KGX graph (KG-Bioportal)
  node_count: 51
  original_source:
  - relation_type: prov:hadPrimarySource
    source: i-adopt
  product_file_size: 1514
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/I-ADOPT.tar.gz
publications:
- authors:
  - Barbara Magagna
  - Gwenaëlle Moncoiffé
  - Anusuriya Devaraju
  - Maria Stoica
  - Sirko Schindler
  - Alison Pamment
  doi: 10.15497/RDA00071
  id: doi:10.15497/RDA00071
  journal: Research Data Alliance
  preferred: true
  title: InteroperAble Descriptions of Observable Property Terminologies (I-ADOPT)
    WG Outputs and Recommendations
  year: '2022'
- authors:
  - Barbara Magagna
  - Ilaria Rosati
  - Maria Stoica
  - Sirko Schindler
  - Gwenaelle Moncoiffe
  - Anusuriya Devaraju
  - Johannes Peterseil
  - Robert Huber
  doi: 10.48550/arXiv.2107.06547
  id: doi:10.48550/arXiv.2107.06547
  journal: arXiv
  title: The I-ADOPT Interoperability Framework for FAIRer data descriptions of biodiversity
  year: '2021'
repository: https://github.com/i-adopt/ontology
synonyms:
- I-ADOPT
- iop
---
# I-ADOPT Framework Ontology

The I-ADOPT (InteroperAble Descriptions of Observable Property Terminology) Framework ontology was developed by a Research Data Alliance (RDA) Working Group formed in 2019 under the Vocabulary and Semantic Services Interest Group. Its recommendations were finalized in January 2022 and endorsed by RDA in April 2022. The group is now in maintenance mode but continues to refine the framework.

The ontology breaks a variable (observable property) description into atomic components: the property being observed, the object of interest, the matrix it sits in, any context objects, and constraints. Each component can be mapped to terms in existing vocabularies, so that variables described in different terminologies can be aligned.

## Products

- The current ontology (version 1.1.0 when checked on 2026-10-05) resolves from `https://w3id.org/iadopt/ont` and is available in Turtle, OWL (RDF/XML) and JSON-LD.
- An extended version adds formal class definitions and logical restrictions.
- WIDOCO-generated HTML documentation and the RDA recommendations document (DOI 10.15497/RDA00071) describe the framework.

The ontology is also hosted on ontology portals such as BioPortal and EcoPortal under the acronym I-ADOPT.