---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://nfdi4culture.de/helpdesk.html
  - contact_type: url
    value: https://nfdi4culture.de/
  label: NFDI4Culture
creation_date: '2026-08-06T00:00:00Z'
description: The Culture Knowledge Graph (CKG) is the integrating linked open data
  graph of NFDI4Culture, the German National Research Data Infrastructure consortium
  for research data on material and immaterial cultural heritage. It acts as a single
  point of access, or data index, over decentralized research data collections, repositories,
  portals, software tools, infrastructures, and services across the NFDI4Culture subject
  areas of architecture, art history, media studies, musicology, and the performing
  arts. Beyond describing the consortium and its infrastructure, the graph indexes
  the content of contributed research data, including cultural heritage objects, persons,
  locations, and events, along with references to the external vocabularies used to
  identify and classify them, and access and reuse information such as legal statements,
  contact persons, and export formats. Contributing institutions supply metadata in
  the Culture Graph Interchange Format (CGIF), which is harvested through a dedicated
  ETL pipeline and integrated into the graph. The NFDI4Culture Ontology (CTO), a domain
  module of the NFDIcore mid-level ontology aligned with Basic Formal Ontology (BFO)
  2020, provides the semantic backbone. The graph is reported to hold roughly 106 million
  RDF triples and is queryable through a public SPARQL endpoint.
domains:
- humanities and cultural heritage
homepage_url: https://nfdi4culture.de/services/details/culture-knowledge-graph.html
id: culture-knowledge-graph
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
name: Culture Knowledge Graph
products:
- category: ProgrammingInterface
  description: Public SPARQL 1.1 endpoint over the Culture Knowledge Graph, with a
    browsable query interface and documented example queries covering research data
    repositories and portals, NFDI4Culture partner organizations with their Wikidata
    mappings, triple counts, and listings of types and properties in the graph.
  format: http
  id: culture-knowledge-graph.sparql
  is_public: true
  name: Culture Knowledge Graph SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: culture-knowledge-graph
  product_url: https://nfdi4culture.de/resources/knowledge-graph.html
- category: GraphicalInterface
  description: Culture Data Search, the faceted discovery interface over the Culture
    Knowledge Graph, served by the shmarql SPARQL exploration tool developed within
    NFDI4Culture.
  format: http
  id: culture-knowledge-graph.data-search
  name: Culture Data Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: culture-knowledge-graph
  product_url: https://nfdi4culture.de/shmarql/
- category: GraphProduct
  description: Full RDF dump of the Culture Knowledge Graph in N-Triples, referenced
    from the SPARQL endpoint page alongside the public query interface. NFDI4Culture
    describes the integrated resources as version controlled and regularly updated
    through a Git repository from which the data dump is offered.
  format: ntriples
  id: culture-knowledge-graph.dump
  name: Culture Knowledge Graph RDF Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: culture-knowledge-graph
  product_url: https://nfdi4culture.de/resources/knowledge-graph.html
  warnings:
  - A stable direct download URL for the dump was not located when this entry was
    created on 2026-08-06; the dump is reached through the SPARQL endpoint page.
- category: OntologyProduct
  description: The NFDI4Culture Ontology (CTO), the domain-specific module used to
    structure the Culture Knowledge Graph. CTO builds on the NFDIcore mid-level ontology
    v3 and is aligned with Basic Formal Ontology (BFO) 2020. It is developed in Task
    Area 5 of NFDI4Culture and published in OWL and Turtle, with base and full variants.
  format: ttl
  id: culture-knowledge-graph.cto
  name: NFDI4Culture Ontology (CTO)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: culture-knowledge-graph
  product_url: https://nfdi4culture.de/ontology/
  repository: https://github.com/ISE-FIZKarlsruhe/nfdi4culture
- category: DataModelProduct
  description: The Culture Graph Interchange Format (CGIF), the specification and workflow
    that data providers follow to contribute research data metadata for harvesting
    into the Culture Knowledge Graph.
  format: ttl
  id: culture-knowledge-graph.cgif
  name: Culture Graph Interchange Format (CGIF)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: culture-knowledge-graph
  product_url: https://docs.nfdi4culture.de/ta5-cgif-specification/introduction
- category: DocumentationProduct
  description: NFDI4Culture service page for the Culture Knowledge Graph, describing
    its scope, the technologies and ontologies used, the data integration workflow,
    and the team responsible for it.
  format: http
  id: culture-knowledge-graph.documentation
  name: Culture Knowledge Graph Service Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: culture-knowledge-graph
  product_url: https://nfdi4culture.de/services/details/culture-knowledge-graph.html
- category: DocumentationProduct
  description: Documentation for the NFDI4Culture Ontology (CTO), generated from the
    ontology source and published by FIZ Karlsruhe.
  format: http
  id: culture-knowledge-graph.cto-documentation
  name: NFDI4Culture Ontology Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: culture-knowledge-graph
  - relation_type: prov:hadPrimarySource
    source: culture-knowledge-graph.cto
  product_url: https://nfdi.fiz-karlsruhe.de/4culture/
repository: https://github.com/ISE-FIZKarlsruhe/nfdi4culture
synonyms:
- CKG
- NFDI4Culture Knowledge Graph
warnings:
- No license statement for the graph data was located when this entry was created
  on 2026-08-06. NFDI4Culture describes the graph as linked open data, but the specific
  license for the dump and endpoint should be confirmed with the NFDI4Culture helpdesk.
---
# Culture Knowledge Graph

## Overview

The Culture Knowledge Graph (CKG) is the linked open data backbone of
[NFDI4Culture](https://nfdi4culture.de/), the consortium within Germany's National
Research Data Infrastructure (NFDI) that serves research on material and immaterial
cultural heritage. Its purpose is integration rather than collection: the graph is a
data index over research data that remains distributed across the repositories,
portals, and institutional collections of the culture community, giving a single
queryable entry point to material that would otherwise have to be discovered site by
site.

The covered subject areas are architecture, art history, media studies, musicology,
and the performing arts.

## What the graph describes

Following the scope of the NFDI4Culture Ontology, the graph covers three broad areas:

- **The consortium and its infrastructure** — persons and organizations involved in
  research processes, along with services, guidelines, standards, and events.
- **The content of contributed research data** — cultural heritage objects, and the
  persons, locations, and events referenced in that data, together with associated
  media and references to the external vocabularies used for identification and
  classification.
- **Access and reuse** — legal statements, contact persons, standards, and export
  formats for the indexed resources.

## Data integration

Data providers contribute metadata in the **Culture Graph Interchange Format
(CGIF)**, which is harvested by a dedicated ETL pipeline and mapped into the graph.
The semantic backbone is the **NFDI4Culture Ontology (CTO)**, a domain module of the
**NFDIcore** mid-level ontology (v3) aligned with Basic Formal Ontology (BFO) 2020.
Integrated resources are version controlled and updated through a Git repository,
from which a full RDF dump is offered.

## Access

The graph is queryable through a public SPARQL 1.1 endpoint, presented with example
queries for common tasks such as listing indexed repositories and portals or
retrieving NFDI4Culture partner organizations with their Wikidata mappings. A faceted
discovery interface, Culture Data Search, is served by *shmarql*, a SPARQL
exploration tool developed within the project.

## Notes on this entry

Two details could not be confirmed from public documentation at the time of curation
and are flagged as warnings above: the license applying to the graph data, and a
stable direct download URL for the N-Triples dump. The reported figure of roughly
106 million triples comes from NFDI4Culture's own description of the graph; an earlier
release announcement described a much smaller initial index, so the figure should be
read as a snapshot of a growing resource rather than a fixed size.

NFDI4Culture is funded by the Deutsche Forschungsgemeinschaft (DFG) and operated with
partner institutions including FIZ Karlsruhe, whose Information Service Engineering
group maintains the ontology and knowledge graph tooling.
