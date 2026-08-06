---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.era.europa.eu/agency/contact-us_en
  - contact_type: url
    value: https://rinf.data.era.europa.eu/
  label: European Union Agency for Railways
creation_date: '2026-08-06T00:00:00Z'
description: The ERA Knowledge Graph is the RDF publication of the European Union Agency
  for Railways' Register of Infrastructure (RINF) and related registers, released as
  linked open data since 2021. It describes the European railway network as a graph
  of operational points, sections of line, tracks, tunnels, sidings, and platforms,
  together with the interoperability parameters attached to them, including load capability,
  maximum permitted speed, gauging and gradient profiles, braking systems, energy supply
  and contact line systems, train detection systems, and authorized vehicle types,
  with geospatial location data organized by EU member state. Source data supplied
  by infrastructure managers and national registration entities is converted to RDF
  using RML mappings. The graph is formalized by the ERA Vocabulary (ERA Ontology),
  which carries roughly 76 classes, 600 properties, 52 annotation properties, and more
  than 80 SKOS concept schemes for coded parameter values, and is accompanied by SHACL
  shapes used for validation. Entities are minted in the http://data.europa.eu/949/
  namespace. The graph is served from a public GraphDB deployment and dumped periodically
  to Zenodo; the infrastructure repository held roughly 53.7 million triples when checked
  in August 2026.
domains:
- transportation
homepage_url: https://www.era.europa.eu/domains/registers/era-knowlege-graph_en
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
id: era-kg
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: ERA Knowledge Graph
products:
- category: ProgrammingInterface
  description: Public SPARQL endpoint over the RINF+ repository, the infrastructure
    graph expressed with the ERA Ontology 3.1.x model, served from the Agency's GraphDB
    deployment. Verified queryable on 2026-08-06, when the repository reported 53,716,816
    triples. Companion repositories on the same deployment hold the ERA ontology itself
    (OWL, SKOS, and SHACL) and references to railway legislation.
  format: http
  id: era-kg.sparql
  is_public: true
  name: ERA Knowledge Graph SPARQL Endpoint (RINF+)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: era-kg
  product_url: https://graph.data.era.europa.eu/repositories/rinf-plus
- category: ProgrammingInterface
  description: SPARQL API path documented with the Agency's data releases as the public
    query interface to the RINF knowledge graph.
  format: http
  id: era-kg.api
  is_public: true
  name: ERA Knowledge Graph SPARQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: era-kg
  product_url: https://rinf.data.era.europa.eu/api/v1/sparql/rinf
  warnings:
  - 'Checked on 2026-08-06: this path returned HTTP 500 with the message "SPARQL upstream
    returned 500". The GraphDB endpoint at graph.data.era.europa.eu answered the same
    queries successfully, so this appears to be a fault in the API layer rather than
    in the graph.'
- category: GraphicalInterface
  description: GraphDB workbench for the Agency's linked data deployment, exposing the
    RINF+, ERA ontology, and legislation repositories for interactive exploration and
    query.
  format: http
  id: era-kg.graphdb
  name: ERA GraphDB Workbench
  original_source:
  - relation_type: prov:hadPrimarySource
    source: era-kg
  product_url: https://graph.data.era.europa.eu/
- category: GraphicalInterface
  description: RINF linked data portal, the Agency's entry point for the infrastructure
    knowledge graph, with documentation of the data model and access paths.
  format: http
  id: era-kg.portal
  name: RINF Linked Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: era-kg
  product_url: https://rinf.data.era.europa.eu/
- category: GraphProduct
  description: Periodic full dump of the infrastructure knowledge graph, archived on
    Zenodo under a versioned series with a concept DOI covering all releases. The most
    recent release identified is v9.0 of 2026-06-29, a 3.75 GB TriG file (rinfplus.trig);
    earlier releases were compressed N-Quads. The edge count recorded here is the triple
    count reported by the live RINF+ repository on 2026-08-06.
  edge_count: 53716816
  format: trig
  id: era-kg.dump
  latest_version: v9.0
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: ERA Knowledge Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: era-kg
  product_url: https://doi.org/10.5281/zenodo.14605743
- category: OntologyProduct
  description: The ERA Vocabulary (ERA Ontology), defined by the European Union Agency
    for Railways to describe European railway infrastructure and the vehicles authorized
    to operate over it. It carries roughly 76 classes, 600 properties, and 52 annotation
    properties, along with more than 80 SKOS concept schemes for coded parameter values,
    and is distributed with SHACL shapes for validating conforming data.
  format: owl
  id: era-kg.ontology
  name: ERA Vocabulary (ERA Ontology)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: era-kg
  product_url: https://data-interop.era.europa.eu/era-vocabulary/
  repository: https://gitlab.com/era-europa-eu/public/interoperable-data-programme/era-ontology/era-ontology
- category: ProcessProduct
  description: RML mapping definitions used to generate the ERA Knowledge Graph from
    the source RINF data supplied by infrastructure managers and national registration
    entities.
  format: ttl
  id: era-kg.mappings
  name: ERA Knowledge Graph RML Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: era-kg
  product_url: https://gitlab.com/era-europa-eu/public/interoperable-data-programme/era-ontology/era-kg-mappings
  repository: https://gitlab.com/era-europa-eu/public/interoperable-data-programme/era-ontology/era-kg-mappings
- category: DocumentationProduct
  description: The Agency's ERA Knowledge Graph page, with a catalogue of curated SPARQL
    queries organized by infrastructure type, covering parameter completeness, infrastructure
    statistics, and comparisons between member states.
  format: http
  id: era-kg.documentation
  name: ERA Knowledge Graph Documentation and Query Catalogue
  original_source:
  - relation_type: prov:hadPrimarySource
    source: era-kg
  product_url: https://www.era.europa.eu/domains/registers/era-knowlege-graph_en
publications:
- authors:
  - Toledo J
  - Doña D
  - Ruckhaus E
  - Corcho O
  - Aguado M
  - Patru D
  - Atemezing G
  - Vasilopoulou P
  doi: 10.1007/978-3-032-09530-5_23
  id: doi:10.1007/978-3-032-09530-5_23
  journal: Lecture Notes in Computer Science
  preferred: true
  title: 'Using Semantic Technologies in the Railway Domain: The Register of Infrastructure
    (RINF) System'
  year: '2026'
repository: https://gitlab.com/era-europa-eu/public/interoperable-data-programme/era-ontology
synonyms:
- ERA-KG
- ERA RINF Knowledge Graph
- EU Rail Knowledge Graph
warnings:
- '"ERA" here is the European Union Agency for Railways, not the European Research Area.
  This graph describes railway infrastructure. For European research projects, organizations,
  and funding, see the EURIO Knowledge Graph and the EU Knowledge Graph.'
---
# ERA Knowledge Graph

## Overview

The ERA Knowledge Graph is the linked open data publication of the European Union
Agency for Railways' **Register of Infrastructure (RINF)**. RINF collects railway
infrastructure data from infrastructure managers and national registration entities
across EU member states; since 2021 the Agency has published that register as RDF,
converted from the source data with RML mappings and served from a public GraphDB
deployment.

The graph is part of the Agency's Interoperable Data Programme, whose broader purpose
is to make the registers underpinning railway interoperability queryable as data
rather than only as documents.

## Name disambiguation

This resource is frequently confused with the **European Research Area**. It is not
related: "ERA" here is the Agency, and the graph is about track, not about research
funding. The registry entries covering European research projects and funding are
`eurio` (the EURIO Knowledge Graph, CORDIS framework-programme data) and
`eu-knowledge-graph` (the Commission's Wikibase graph of EU-financed projects).

## Contents

Infrastructure entities include operational points, sections of line, tracks, tunnels,
sidings, and platforms, with interoperability parameters attached: load capability,
maximum permitted speed, gauging and gradient profiles, braking systems, energy supply
and contact line systems, train detection systems, and authorized vehicle types.
Geospatial locations are included and the data is organized by member state. Entities
are minted under `http://data.europa.eu/949/`.

The semantics come from the **ERA Vocabulary (ERA Ontology)** — roughly 76 classes,
600 properties, and 52 annotation properties, plus more than 80 SKOS concept schemes
for coded parameter values — distributed with SHACL shapes for validation.

## Access

Verified on 2026-08-06:

- The **GraphDB SPARQL endpoint** for the RINF+ repository
  (`graph.data.era.europa.eu/repositories/rinf-plus`) answers queries and reported
  **53,716,816 triples**. Sibling repositories on the same deployment hold the ERA
  ontology (OWL, SKOS, SHACL; ~1.15M triples) and railway legislation references.
- The **documented API path** (`rinf.data.era.europa.eu/api/v1/sparql/rinf`) returned
  HTTP 500 with `SPARQL upstream returned 500`. Since the GraphDB endpoint answered
  the same queries, this looks like an API-layer fault rather than a data problem, and
  it is recorded as a product warning.
- **Dumps** are archived on Zenodo as a versioned series under concept DOI
  [10.5281/zenodo.14605743](https://doi.org/10.5281/zenodo.14605743). The latest
  release identified is v9.0 (2026-06-29), a 3.75 GB TriG file; earlier releases were
  compressed N-Quads. All are CC BY 4.0.

## Notes on this entry

The domain is `transportation` and the current dump's format is `trig`. Both values
were added to the schema for this entry: `DomainEnum` had no term covering transport
infrastructure, and `FormatEnum` had neither a TriG value nor an `other` fallback.
