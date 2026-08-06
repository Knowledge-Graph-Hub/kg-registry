---
activity_status: orphaned
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: url
    value: https://sztaki.hun-ren.hu/en/science/services/courage-knowledge-graph
  label: András Micsik
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cultural-opposition.eu/
  label: COURAGE Project Consortium
creation_date: '2026-08-06T00:00:00Z'
description: The COURAGE knowledge graph is the linked data registry produced by the
  COURAGE project (Cultural Opposition - Understanding the Cultural Heritage of Dissent
  in the Former Socialist Countries). It describes public and private collections documenting
  cultural opposition under socialism, roughly 1950 to 1990, across the member and
  candidate states of the European Union that were part of the former socialist bloc.
  Alongside collections it describes persons, person roles, organizations, groups,
  events, and featured collection items, covering material such as dissident literature,
  samizdat and other unofficial publications, underground music scenes, avant-garde
  art, and religious and civic movements. Content was contributed by researchers from
  more than fifteen countries, and descriptions are held simultaneously in fifteen
  languages, which the project cited as a motivation for its RDF-based design. The
  schema is the COURAGE Ontology, published in OWL; a separate effort re-expressed
  the dataset in CIDOC-CRM and validated the conversion with SPARQL and SHACL, and
  another linked COURAGE entities to Wikidata.
domains:
- humanities and cultural heritage
homepage_url: https://cultural-opposition.eu/
id: courage
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://opendatacommons.org/licenses/by/1-0/
  label: ODC-By 1.0
name: COURAGE Knowledge Graph
products:
- category: GraphicalInterface
  description: The COURAGE registry web interface, providing browsable and searchable
    access to collections, persons, organizations, groups, events, and featured items,
    with descriptions available in multiple languages.
  format: http
  id: courage.registry
  name: COURAGE Registry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: courage
  product_url: https://cultural-opposition.eu/registry/
- category: GraphProduct
  description: Open data release of the COURAGE registry as linked data, covering collections,
    featured items, groups, organizations, and persons. Published as a Zenodo archive
    of RDF data, version 1.1 dated 2019-07-12.
  format: rdfxml
  id: courage.dump
  latest_version: '1.1'
  license:
    id: https://opendatacommons.org/licenses/by/1-0/
    label: ODC-By 1.0
  name: COURAGE Registry Open Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: courage
  product_url: https://doi.org/10.5281/zenodo.3333540
  versions:
  - '1.0'
  - '1.1'
- category: ProgrammingInterface
  description: SPARQL endpoint over the COURAGE triple store, historically served from
    the Hungarian Academy of Sciences infrastructure. The project reported that the
    graph database and SPARQL made it practical to express complex queries over the
    registry and to manage descriptions in fifteen languages at once.
  format: http
  id: courage.sparql
  is_public: true
  name: COURAGE SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: courage
  product_url: http://courage.btk.mta.hu:3030/courage/query
  warnings:
  - 'Checked on 2026-08-06: the documented endpoint path returned HTTP 404. The endpoint
    may have moved or been retired following the reorganization of the Hungarian Academy
    of Sciences research network (MTA to HUN-REN). Use the Zenodo data dump instead,
    or contact SZTAKI for current access.'
- category: OntologyProduct
  description: The COURAGE Ontology, the schema of the COURAGE registry, published
    as an OWL file. It models collections, collection items, persons and their roles,
    groups, organizations, and events in the domain of cultural opposition.
  format: owl
  id: courage.ontology
  name: COURAGE Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: courage
  warnings:
  - A stable public URL for the OWL file was not located when this entry was created
    on 2026-08-06. The ontology is described in the project publications and was distributed
    with the registry.
- category: DocumentationProduct
  description: Service page for the COURAGE knowledge graph at HUN-REN SZTAKI, the
    institute that built and hosted the graph, summarizing its contents and technical
    basis.
  format: http
  id: courage.sztaki-page
  name: COURAGE Knowledge Graph Service Page (SZTAKI)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: courage
  product_url: https://sztaki.hun-ren.hu/en/science/services/courage-knowledge-graph
publications:
- authors:
  - Faraj G
  - Micsik A
  doi: 10.3390/fi13110277
  id: doi:10.3390/fi13110277
  journal: Future Internet
  preferred: true
  title: Representing and Validating Cultural Heritage Knowledge Graphs in CIDOC-CRM
    Ontology
  year: '2021'
- authors:
  - Faraj G
  - Micsik A
  doi: 10.1007/978-3-030-36599-8_37
  id: doi:10.1007/978-3-030-36599-8_37
  journal: Communications in Computer and Information Science
  title: Enriching Wikidata with Cultural Heritage Data from the COURAGE Project
  year: '2019'
synonyms:
- COURAGE
- COURAGE Registry
- 'Cultural Opposition: Understanding the Cultural Heritage of Dissent in the Former
  Socialist Countries'
warnings:
- The COURAGE project ran from February 2016 to January 2019 and the graph is no longer
  actively extended. The registry interface and the archived data dump remain available,
  but the documented SPARQL endpoint did not respond when checked on 2026-08-06.
---
# COURAGE Knowledge Graph

## Overview

COURAGE — *Cultural Opposition: Understanding the Cultural Heritage of Dissent in the
Former Socialist Countries* — built a registry of the scattered collections that
document cultural opposition under socialism in Central and Eastern Europe. The
project ran from February 2016 to January 2019 with twelve partner institutions,
funded by the European Union's Horizon 2020 programme under grant agreement 692919
(approximately €2.48M), and was led from the Hungarian Academy of Sciences
(MTA BTK Research Centre for the Humanities) with the Institute of Philosophy and
Sociology of the Polish Academy of Sciences (IFIS PAN) among the partners.

The registry is a knowledge graph rather than a document collection: it describes
collections and the people, groups, organizations, and events around them, linking
private archives, institutional holdings, and individual estates that had never been
described together.

## Contents

Entity types in the graph include collections, featured collection items, persons and
person roles, groups, organizations, and events. Subject matter spans dissident
literature and samizdat, underground and punk music scenes, avant-garde and
unofficial art, religious movements, and civic and environmental opposition, roughly
covering 1950 to 1990.

Content was contributed by researchers in more than fifteen countries, and
descriptions are maintained in fifteen languages simultaneously. The project reported
that RDF made this multilingual text management straightforward and that SPARQL was
what made the relationship-heavy queries over persons, collections, and organizations
practical.

## Access

- The **registry web interface** at [cultural-opposition.eu/registry](https://cultural-opposition.eu/registry/)
  remains available.
- The **open data release** is archived on Zenodo
  ([10.5281/zenodo.3333540](https://doi.org/10.5281/zenodo.3333540)), version 1.1
  dated July 2019, under the Open Data Commons Attribution License 1.0.
- The **SPARQL endpoint** documented by the project did not respond when checked for
  this entry. The graph was hosted at SZTAKI, and the institutional reorganization of
  the Hungarian research network (MTA to HUN-REN) is a plausible cause; the dump is
  the reliable route to the data today.

## Related work

Two follow-on efforts are worth noting, both from SZTAKI:

- A **CIDOC-CRM rendering** of the COURAGE data, with SPARQL and SHACL used to
  validate the converted dataset — see the *Future Internet* paper below and the
  [courage-crm repository](https://github.com/dsd-sztaki-hu/courage-crm).
- An effort to **enrich Wikidata** with COURAGE cultural heritage entities.

## Status

Recorded as `orphaned`: the project has concluded, the graph is not being extended,
and part of its documented infrastructure is no longer responding, but the registry
and the archived dump are still usable.
