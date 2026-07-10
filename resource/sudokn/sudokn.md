---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  label: Farhad Ameri
  contact_details:
  - contact_type: email
    value: farhad.ameri@asu.edu
  - contact_type: github
    value: fameri
- category: Individual
  contact_details:
  - contact_type: email
    value: farhad.ameri@asu.edu
  label: Farhad Ameri
description: Supply and Demand Open Knowledge Network is an interconnected network
  of publicly available manufacturing capability data focused on Small and Medium-Sized
  Manufacturers.
domains:
- other
homepage_url: https://projects.engineering.asu.edu/sudokn/
id: sudokn
layout: resource_detail
name: SUDOKN
repository: https://github.com/SUDOKN
products:
- category: GraphProduct
  id: sudokn.graph
  name: SUDOKN Manufacturing Capability Graph
  description: The SUDOKN manufacturing capability knowledge graph in RDF (Turtle),
    representing the capabilities of small and medium-sized U.S. manufacturers.
    Company profiles (manufacturing processes, materials, industries served,
    certifications, NAICS classification, and locations) are built by web-scraping
    raw text from manufacturer company websites and extracting triples with an
    LLM-based ETL pipeline, using terms from the SUDOKN application ontology (built
    on the Industrial Ontology Foundry and Basic Formal Ontology). Served through
    the SUDOKN SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  product_url: https://github.com/SUDOKN/graph
  original_source:
  - source: sudokn
    relation_type: prov:hadPrimarySource
  secondary_source:
  - source: us-census
    relation_type: prov:wasInfluencedBy
- category: ProgrammingInterface
  description: SPARQL endpoint for SUDOKN
  format: http
  id: sudokn.sparql
  name: SUDOKN SPARQL
  original_source:
  - source: sudokn
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/sudokn/sparql
- id: sudokn.tpf
  name: SUDOKN TPF
  description: Triple Pattern Fragments endpoint for SUDOKN
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/sudokn
  original_source:
  - source: sudokn
    relation_type: prov:hadPrimarySource
publications:
- id: https://doi.org/10.1007/978-3-031-71637-9_21
  authors:
  - Farhad Ameri
  - Mukund Shenoy
  - Ali Hasanzadeh
  - Sambhav Kapoor
  doi: 10.1007/978-3-031-71637-9_21
  journal: Advances in Production Management Systems (APMS 2024), IFIP AICT 732
  preferred: true
  title: Open Manufacturing Capability Network Supported by Formal Ontologies
  year: '2024'
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-03T00:00:00Z'
---
# SUDOKN

The Supply and Demand Open Knowledge Network (SUDOKN) is an NSF-funded open knowledge network (NSF Award 2333801) that represents the capabilities of small and medium-sized U.S. manufacturers as an interconnected RDF knowledge graph. It is developed at Arizona State University to improve supplier discovery, capability and capacity analysis, and supply-chain resilience.

## Upstream sources

- **Manufacturer company websites (primary).** The knowledge graph is constructed by web-scraping raw text from individual manufacturer websites and extracting manufacturing triples with an LLM-based ETL pipeline (see the `SUDOKN/data-ETL-pipeline` repository), following the SUDOKN application ontology. These sources are many individual company sites rather than a single named dataset, so they are represented via SUDOKN's own primary-source provenance rather than a discrete registry resource.
- **NAICS classification (reference).** Manufacturer records are classified with the North American Industry Classification System (visible in the graph as `NAICSClassifier` entries). NAICS is maintained by the U.S. Census Bureau, so this reference influence is recorded via the `us-census` resource.
- **Ontology basis.** Semantics come from the Industrial Ontology Foundry (IOF) core and supply-chain ontologies and the Basic Formal Ontology (BFO); these are schema vocabularies rather than data sources.

The project page also displays a "Manufacturing Facilities in the U.S." map credited to HIFLD, but HIFLD is not documented as a data input to the knowledge graph itself and is therefore not recorded as a source.

## Automated Evaluation

- View the automated evaluation: [sudokn automated evaluation](sudokn_eval_automated.html)
