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
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
name: OREGANO
products:
  - category: DocumentationProduct
    description: Project repository and README describing OREGANO's scope, statistics, integration workflow, and application context.
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
  - category: GraphProduct
    description: OREGANO knowledge graph data download on Zenodo (record 10103842, v3). Provides the integrated graph as TSV triples (OREGANO_V2.1.tsv) plus per-entity TSV files and a Turtle (.ttl) metadata file with entity names and cross-references. This download replaces the former public SPARQL endpoint, which is no longer available.
    format: tsv
    id: oregano.sparql
    name: OREGANO Knowledge Graph Data Download (Zenodo)
    product_url: https://zenodo.org/records/10103842
    original_source:
      - source: oregano
        relation_type: prov:hadPrimarySource
publications:
  - preferred: true
    id: doi:10.1038/s41597-023-02757-0
    doi: 10.1038/s41597-023-02757-0
    title: The OREGANO knowledge graph for computational drug repurposing
    authors:
      - Marina Boudin
      - Gayo Diallo
      - Martin Drancé
      - Fleur Mougin
    journal: Scientific Data
    year: '2023'
repository: https://gitub.u-bordeaux.fr/erias/oregano
---

# OREGANO

OREGANO is a biomedical knowledge graph built for drug repositioning and
drug-target relation discovery. It integrates drug, target, gene, disease,
pathway, phenotype, and related biomedical entities from multiple upstream data
sources into a single graph designed for link-prediction workflows.

The owned products on this page include the project documentation, the graph
distribution folder in the project repository, and a Zenodo data download of the
integrated graph (TSV triples plus a Turtle metadata file). OREGANO is now
distributed primarily as downloadable graph files; the project's former public
SPARQL endpoint is no longer reachable and has been replaced here by the Zenodo
download. The graph is explicitly assembled from many free biomedical databases,
which are represented in product provenance rather than duplicated as separate
owned OREGANO products.
