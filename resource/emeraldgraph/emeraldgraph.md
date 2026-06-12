---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: github
        value: ai4greenwashing
      - contact_type: url
        value: https://github.com/ai4greenwashing
    label: ai4greenwashing
creation_date: '2026-06-12T00:00:00Z'
description: EmeraldGraph is the domain-specific knowledge graph used by EmeraldMind, a knowledge graph-augmented framework for greenwashing detection. It is built from corporate environmental, social, and governance reports to represent sustainability claims, organizations, goals, initiatives, metrics, evidence, and related relationships for retrieval-augmented claim assessment.
domains:
  - environment
  - information technology
homepage_url: https://github.com/ai4greenwashing/EmeraldMind
id: emeraldgraph
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: EmeraldGraph
products:
  - category: GraphProduct
    description: Pre-built EmeraldGraph JSON export containing sustainability-related triples extracted from corporate ESG reports.
    edge_count: 59921
    format: json
    id: emeraldgraph.graph-json
    name: EmeraldGraph JSON export
    original_source:
      - relation_type: prov:hadPrimarySource
        source: emeraldgraph
    product_url: https://github.com/ai4greenwashing/EmeraldMind/blob/main/graph_latest.json
  - category: DataModelProduct
    description: EmeraldGraph schema definitions used by the construction pipeline to validate relationship and classification logic.
    format: json
    id: emeraldgraph.schema
    name: EmeraldGraph schema
    original_source:
      - relation_type: prov:hadPrimarySource
        source: emeraldgraph
    product_url: https://github.com/ai4greenwashing/EmeraldMind/tree/main/schemas
  - category: ProcessProduct
    description: Source code for constructing EmeraldGraph, loading it into Neo4j, and using it in the EmeraldMind greenwashing-detection workflow.
    id: emeraldgraph.pipeline
    name: EmeraldGraph construction pipeline
    original_source:
      - relation_type: prov:hadPrimarySource
        source: emeraldgraph
    product_url: https://github.com/ai4greenwashing/EmeraldMind/tree/main/src/EmeraldKG
  - category: Product
    description: Processed greenwashing claim and EmeraldData datasets used by EmeraldMind experiments.
    id: emeraldgraph.datasets
    name: EmeraldMind processed datasets
    original_source:
      - relation_type: prov:hadPrimarySource
        source: emeraldgraph
    product_url: https://github.com/ai4greenwashing/EmeraldMind/tree/main/datasets
  - category: Product
    compression: zip
    description: Archived release of the EmeraldMind repository and associated EmeraldGraph artifacts on Zenodo.
    id: emeraldgraph.zenodo-archive
    name: EmeraldMind Zenodo archive
    original_source:
      - relation_type: prov:hadPrimarySource
        source: emeraldgraph
    product_url: https://zenodo.org/records/18339711
publications:
  - authors:
      - Georgios Kaoukis
      - Ioannis-Aris Koufopoulos
      - Eleni Psaroudaki
      - Danae Pla Karidi
      - Evaggelia Pitoura
      - George Papastefanatos
      - Panayiotis Tsaparas
    doi: 10.1145/3774904.3792997
    id: doi:10.1145/3774904.3792997
    journal: Proceedings of the ACM Web Conference 2026
    title: 'EmeraldMind: A Knowledge Graph-Augmented Framework for Greenwashing Detection'
    year: '2026'
repository: https://github.com/ai4greenwashing/EmeraldMind
---

EmeraldGraph is a sustainability and greenwashing-detection knowledge graph released
with EmeraldMind, together with schema files, construction scripts, benchmark datasets,
and an archived Zenodo release.
