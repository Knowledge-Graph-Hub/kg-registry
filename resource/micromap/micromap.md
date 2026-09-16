---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: vkhandavalli@graphomics.com
  - contact_type: github
    value: vkhangraphomics
  label: Varun Khandavalli
creation_date: '2026-09-16T00:00:00Z'
description: MicroMap is a microbiome knowledge graph platform built by Graphomics
  on Neo4j. It links microbial taxa to diseases, metabolites, pathways, drugs,
  genes, proteins, body sites and literature. The graph is populated through
  MapForge, a BioCypher-compatible ingestion pipeline that turns tabular source
  data into parameterized Cypher bundles that a reviewer approves before any node
  is written. Loaders cover NCBI Taxonomy, Disbiome, gutMDisorder, BugSigDB,
  GMrepo, mBodyMap, HMDB, KEGG, ChEMBL, Reactome, PubChem, PubMed and SemMedDB.
  The ingestion software, API code and graph schema are open source under the
  MIT license. The populated production graph is served to Graphomics customers
  through a REST API and an MCP server and is not distributed as a bulk download.
  This resource is unrelated to the MicroMap microbiome-metabolism visualization
  resource from the Thiele lab (University of Galway, 2025).
domains:
- biomedical
- microbiology
- systems biology
homepage_url: https://github.com/vkhangraphomics/micromap-oss
id: micromap
last_modified_date: '2026-09-16T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/license/mit/
  label: MIT
name: MicroMap
products:
- category: ProgrammingInterface
  description: REST API and MCP server over the production MicroMap Neo4j graph,
    with endpoints for taxa, diseases, metabolites, drugs, genes, proteins, pathways,
    biomarker signatures, papers, cross-feeding networks, provenance and graph
    traversal. Access requires a Graphomics API key. The API application code is
    in the open-source repository.
  format: http
  id: micromap.api
  is_neo4j: true
  is_public: false
  name: MicroMap API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: micromap
  - relation_type: prov:wasDerivedFrom
    source: ncbitaxon
  - relation_type: prov:wasDerivedFrom
    source: disbiome
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: chembl
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: semmeddb
  product_url: https://www.graphomics.com/docs
- category: ProcessProduct
  description: MapForge, the reviewable ingestion pipeline for MicroMap. It profiles
    tabular sources (CSV, TSV, JSON, JSONL, Parquet, SQL dumps), resolves entities
    against the graph, emits deterministic parameterized Cypher bundles and writes
    them to Neo4j 5.x only after a reviewer approves the bundle. BioCypher adapters
    are supported through the import-kg path. Distributed as a Python package in
    the micromap-oss repository.
  format: python
  id: micromap.mapforge
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: MicroMap MapForge
  original_source:
  - relation_type: prov:hadPrimarySource
    source: micromap
  product_url: https://github.com/vkhangraphomics/micromap-oss/tree/main/micromap-mapforge
  repository: https://github.com/vkhangraphomics/micromap-oss
- category: DataModelProduct
  description: Neo4j graph schema for MicroMap, defining the node labels (Taxon,
    Disease, Compound, Pathway, Gene, Drug, Protein, Paper, Study, BodySite,
    DrugClass), relationship types and indexes, as Cypher constraint and index
    statements.
  format: neo4j
  id: micromap.schema
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: MicroMap Neo4j Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: micromap
  product_url: https://github.com/vkhangraphomics/micromap-oss/blob/main/database/neo4j_microbiome_schema.cypher
  repository: https://github.com/vkhangraphomics/micromap-oss
publications:
- authors:
  - Varun Khandavalli
  doi: 10.5281/zenodo.22800749
  id: https://doi.org/10.5281/zenodo.22800749
  journal: Zenodo
  preferred: true
  title: MicroMap (Graphomics Knowledge Graph Platform)
  year: '2026'
repository: https://github.com/vkhangraphomics/micromap-oss
version: v0.1.4
---

MicroMap is a microbiome knowledge graph platform from Graphomics. It runs on
Neo4j and connects microbial taxa to diseases, metabolites, pathways, drugs,
genes, proteins, body sites and papers.

## Content and sources

The loader in the open-source repository has entry points for NCBI Taxonomy,
Disbiome, gutMDisorder, BugSigDB, GMrepo, mBodyMap, HMDB, KEGG, ChEMBL,
Reactome, PubChem, PubMed and SemMedDB, plus curated taxon-metabolite
production and gut-brain axis association tables. Release v0.1.3 removed the
loaders for three third-party sources whose commercial licensing terms were
under review at the time. The source list above reflects the v0.1.4 code.

Node labels: `Taxon`, `Disease`, `Compound`, `Pathway`, `Gene`, `Drug`,
`Protein`, `Paper`, `Study`, `BodySite`, `DrugClass`. Relationship types
include `ASSOCIATED_WITH_DISEASE`, `PRODUCES`, `PARTICIPATES_IN`, `TARGETS`,
`FOUND_IN`, `HAS_PARENT` and `IMPLICATED_IN`.

## Ingestion

Data enters the graph through MapForge. MapForge inspects a tabular source,
drafts a mapping, resolves source entities against the graph, emits a
parameterized Cypher bundle and submits it to Neo4j only after a reviewer
approves the bundle. Every submission records who contributed, who approved,
source-file hashes and resolved and unresolved counts.

## Access

The ingestion software, API code and graph schema are public at
https://github.com/vkhangraphomics/micromap-oss. The populated production
graph is served to Graphomics customers through a REST API (API key in the
`X-API-Key` header) and an MCP server. It is not distributed as a bulk
download. The code can be run against a local Neo4j instance to build a
graph from the supported sources.

## Licensing

The MIT license covers the ingestion software, the API code and the graph
schema. It does not cover the populated graph or the upstream data, which
carry their own terms.

## Name disambiguation

An unrelated resource named MicroMap, a microbiome-metabolism network
visualization tool from the Thiele lab at the University of Galway, was
published in *npj Biofilms and Microbiomes* in 2025 and is hosted on Harvard
Dataverse. The two projects share a name and a field and nothing else.
