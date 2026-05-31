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
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: OREGANO
products:
  - category: DocumentationProduct
    description: Project repository and README describing OREGANO's scope, statistics,
      integration workflow, and application context.
    format: http
    id: oregano.docs
    name: OREGANO Project Documentation
    product_url: https://gitub.u-bordeaux.fr/erias/oregano/-/blob/master/README.md
    original_source:
      - source: oregano
        relation_type: prov:hadPrimarySource
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
  - category: ProgrammingInterface
    description: Public SPARQL endpoint for querying OREGANO graph content.
    format: http
    id: oregano.sparql
    name: OREGANO SPARQL Endpoint
    product_url: http://91.121.148.199:8889/bigdata/#query
    original_source:
      - source: oregano
        relation_type: prov:hadPrimarySource
publications:
  - doi: doi:10.1038/s41597-023-02757-0
    id: https://doi.org/10.1038/s41597-023-02757-0
    journal: Scientific Data
    preferred: true
    title: 'OREGANO: a knowledge graph for biomedical relation prediction'
    year: '2023'
repository: https://gitub.u-bordeaux.fr/erias/oregano
---
# OREGANO

OREGANO is a biomedical knowledge graph built for drug repositioning and
drug-target relation discovery. It integrates drug, target, gene, disease,
pathway, phenotype, and related biomedical entities from multiple upstream data
sources into a single graph designed for link-prediction workflows.

The owned products on this page include the project documentation, graph
distribution folder, and published SPARQL endpoint for querying the resource.
The graph is explicitly assembled from many free biomedical databases, which are
represented in product provenance rather than duplicated as separate owned OREGANO
products.
