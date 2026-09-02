---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: prabhagarg@niper.ac.in
  label: Prabha Garg
creation_date: '2025-03-24T00:00:00Z'
description: MedKG is a comprehensive and continuously updated knowledge graph designed
  to address challenges in precision medicine and drug discovery. MedKG integrates
  data from 35 authoritative sources, encompassing 34 node types and 79 relationships.
  A Continuous Integration/Continuous Update pipeline ensures MedKG remains current,
  addressing a critical limitation of static knowledge bases. The integration of molecular
  embeddings enhances semantic analysis capabilities, bridging the gap between chemical
  structures and biological entities.
domains:
- biomedical
- pharmacology
- chemistry and biochemistry
homepage_url: http://pitools.niper.ac.in/medkg/
id: medkg
last_modified_date: '2026-05-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.omim.org/help/agreement
  inferred_from:
  - omim
  - snomedct
  label: OMIM Use Agreement (research/educational use; license required for commercial/redistribution)
  restrictiveness: custom
  status: inferred
  unresolved_sources: []
name: MedKG
products:
- category: GraphicalInterface
  description: Graphical interface for MedKG
  id: medkg.site
  name: MedKG Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medkg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: http://pitools.niper.ac.in/medkg/
publications:
- authors:
  - Kumari M
  - Chauhan R
  - Garg P
  doi: 10.1007/s11030-025-11164-z
  id: doi:10.1007/s11030-025-11164-z
  journal: Molecular Diversity
  title: '''MedKG: enabling drug discovery through a unified biomedical knowledge
    graph'''
  year: '2025'
---
MedKG

## Automated Evaluation

- View the automated evaluation: [medkg automated evaluation](medkg_eval_automated.html)