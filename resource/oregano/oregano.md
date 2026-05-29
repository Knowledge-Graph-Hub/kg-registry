---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://gitub.u-bordeaux.fr/erias/oregano
    label: ERIAS Team, University of Bordeaux
creation_date: '2026-02-22T00:00:00Z'
description: The OREGANO knowledge graph integrates free biomedical databases focused on drugs, proteins, genes, and diseases to support link prediction approaches for drug repositioning and drug-target relation discovery.
domains:
  - pharmacology
  - drug discovery
  - biomedical
homepage_url: https://gitub.u-bordeaux.fr/erias/oregano
id: oregano
last_modified_date: '2026-05-29T00:00:00Z'
layout: resource_detail
name: OREGANO
products:
  - category: GraphProduct
    description: The OREGANO knowledge graph dataset integrating drug, protein, gene, and disease information for drug repositioning.
    format: http
    id: oregano.graph
    name: OREGANO Knowledge Graph
    product_url: https://gitub.u-bordeaux.fr/erias/oregano/-/tree/master/Data_OREGANO/Graphs
    original_source:
      - source: oregano
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: cmaup
        relation_type: prov:wasDerivedFrom
      - source: ctd
        relation_type: prov:wasDerivedFrom
      - source: drugbank
        relation_type: prov:wasDerivedFrom
      - source: go
        relation_type: prov:wasDerivedFrom
      - source: hp
        relation_type: prov:wasDerivedFrom
      - source: npass
        relation_type: prov:wasDerivedFrom
      - source: orphanet
        relation_type: prov:wasDerivedFrom
      - source: pharmgkb
        relation_type: prov:wasDerivedFrom
      - source: reactome
        relation_type: prov:wasDerivedFrom
      - source: sider
        relation_type: prov:wasDerivedFrom
      - source: ttd
        relation_type: prov:wasDerivedFrom
      - source: umls
        relation_type: prov:wasDerivedFrom
      - source: uniprot
        relation_type: prov:wasDerivedFrom
      - source: bio2rdf
        relation_type: prov:wasDerivedFrom
publications:
  - doi: doi:10.1038/s41597-023-02757-0
    id: https://doi.org/10.1038/s41597-023-02757-0
    journal: Scientific Data
    preferred: true
    title: 'OREGANO: a knowledge graph for biomedical relation prediction'
    year: '2023'
repository: https://gitub.u-bordeaux.fr/erias/oregano
---

OREGANO is a holistic knowledge graph on drugs built to support link prediction approaches for the discovery of possible drug-target relations for the purpose of drug repositioning. Free biomedical databases are integrated in the knowledge graph, covering drugs, proteins, genes, and diseases.
