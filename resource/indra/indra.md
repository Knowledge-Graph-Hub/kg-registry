---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://indra.readthedocs.io/en/latest/
  - contact_type: github
    value: sorgerlab
  label: Sorger Lab, Harvard Medical School
- category: Organization
  contact_details:
  - contact_type: url
    value: https://gyorilab.github.io/
  label: Gyori Lab, Northeastern University
creation_date: '2025-07-19T00:00:00Z'
description: INDRA (Integrated Network and Dynamical Reasoning Assembler) is an automated
  model assembly system interfacing with NLP systems and databases to collect knowledge,
  and through a process of assembly, produce causal graphs and dynamical models.
domains:
- biomedical
- systems biology
homepage_url: https://www.indra.bio/
id: indra
last_modified_date: '2026-06-22T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/BSD-2-Clause
  label: BSD 2-Clause License
name: INDRA
products:
- category: GraphicalInterface
  description: Web interface for the INDRA Biomedical Discovery Engine
  format: http
  id: indra.discovery
  name: INDRA Biomedical Discovery Engine
  original_source:
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://discovery.indra.bio/
- category: ProgrammingInterface
  description: REST API for INDRA CoGEx queries
  format: http
  id: indra.api.cogex
  name: INDRA CoGEx Query API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://discovery.indra.bio/apidocs
- category: ProcessProduct
  description: Python library for automated model assembly from mechanistic knowledge
  format: python
  id: indra.python
  name: INDRA Python Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/sorgerlab/indra
  repository: https://github.com/sorgerlab/indra
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  format: python
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/gyorilab/indra_cogex
- category: GraphProduct
  description: Merged KG with ontology-grounded KG and literature-based graph as TSV
    file
  format: tsv
  id: np-kg.graph.tsv
  name: NP-KG TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: np-kg
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: dideo
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: indra
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: oae
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semrep
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1074149258
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.tsv?download=1
- category: GraphProduct
  description: Merged KG with ontology-grounded KG and literature-based graph as NetworkX
    multidigraph object
  dump_format: gpickle
  format: mixed
  id: np-kg.graph.networkx
  name: NP-KG gpickle
  original_source:
  - relation_type: prov:hadPrimarySource
    source: np-kg
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: dideo
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: indra
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: oae
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semrep
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 936065236
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.gpickle?download=1
repository: https://github.com/sorgerlab/indra
---
INDRA (Integrated Network and Dynamical Reasoning Assembler) is an automated
model assembly system that interfaces with natural language processing systems
and structured databases to collect mechanistic and causal assertions. It
represents them in a standardized form (INDRA Statements) and assembles them
into various modeling formalisms including causal graphs and dynamical models.

## Key Features

- **Knowledge Integration**: Aggregates mechanistic information from multiple
  sources including pathway databases, literature extraction via NLP, and
  curated databases
- **Standardized Representation**: Converts diverse knowledge into uniform
  INDRA Statements format
- **Assembly Procedures**: Applies knowledge-level assembly to correct
  systematic errors, resolve redundancies, and assess reliability
- **Multiple Output Formats**: Generates causal graphs, rule-based models
  (PySB), and network models

## Data Sources

INDRA integrates knowledge from numerous biomedical resources including:

### Pathway Databases
- BioPAX format databases
- SIGNOR
- BioGRID
- Human Protein Reference Database (HPRD)
- Phospho.ELM
- OmniPath

### Chemical Information
- DrugBank
- ChEMBL
- Comparative Toxicogenomics Database (CTD)

### Literature Mining
- Multiple NLP systems (REACH, TRIPS, Sparser, etc.)
- PubMed abstracts and full-text articles

## Applications

- Pathway analysis and modeling
- Drug discovery and mechanism elucidation
- Systems biology model construction
- Biomedical hypothesis generation
- Network-based discovery

## Access

INDRA is available as:
- Open-source Python library
- Web-based discovery interface
- REST API for programmatic access
- Docker containers for deployment