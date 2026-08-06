---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: CNECT-ECDORIS@ec.europa.eu
  - contact_type: url
    value: https://linkedopendata.eu/
  label: European Commission - Directorate-General for Communications Networks, Content
    and Technology (DG CONNECT)
creation_date: '2026-08-06T00:00:00Z'
description: The EU Knowledge Graph is a Wikibase-based knowledge graph of structured
  information about the European Union, deployed and maintained at the European Commission.
  It describes EU institutions, countries and their capitals, and Commission Directorates-General,
  and it carries the large project datasets that are its main content, namely 2,111,428
  projects financed by the European Union recorded through the Kohesio cohesion policy
  project,
  and 678,448 beneficiaries of those projects, roughly ten percent of which are linked
  to Wikidata so that Wikidata statements complement the Commission's own data. It also
  holds the 2021 Nomenclature of Territorial Units for Statistics (NUTS 2021) used by
  Eurostat, the multilingual European Science Vocabulary (EuroSciVoc) representing fields
  of science, and even Commission facilities such as buildings, canteens, cafeterias,
  and parkings. When queried on 2026-08-06 the query service reported 889,454,967 triples.
  The stated goal is to make EU project spending visible and navigable for citizens
  with no technical background; Kohesio is the main public application built on the graph.
  Because it runs on Wikibase, the graph supports multilingual labels, statement-level
  provenance, and curation by authorized editors, who sign in through EU Login and request
  editor rights.
domains:
- general
homepage_url: https://linkedopendata.eu/wiki/The_EU_Knowledge_Graph
id: eu-knowledge-graph
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
name: EU Knowledge Graph
products:
- category: ProgrammingInterface
  description: Public SPARQL endpoint of the EU Knowledge Graph query service. Verified
    queryable on 2026-08-06, when it reported 889,454,967 triples.
  format: http
  id: eu-knowledge-graph.sparql
  is_public: true
  name: EU Knowledge Graph SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-knowledge-graph
  product_url: https://query.linkedopendata.eu/sparql
- category: GraphicalInterface
  description: Query service interface for the EU Knowledge Graph, in the style of the
    Wikidata Query Service, providing an editor and result views over the SPARQL endpoint.
  format: http
  id: eu-knowledge-graph.query-service
  name: EU Knowledge Graph Query Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-knowledge-graph
  product_url: https://query.linkedopendata.eu/
- category: GraphicalInterface
  description: The Wikibase instance itself, where items and statements can be browsed
    and, for authorized editors signed in through EU Login, edited. The instance reported
    3,801,954 pages and more than 48 million edits on 2026-08-06, with edits from Commission
    services taking place the same day.
  format: http
  id: eu-knowledge-graph.wikibase
  name: EU Knowledge Graph Wikibase
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-knowledge-graph
  product_url: https://linkedopendata.eu/
- category: ProgrammingInterface
  description: MediaWiki and Wikibase action API of the EU Knowledge Graph instance,
    supporting entity retrieval, search, and change tracking. Verified responding on
    2026-08-06.
  format: json
  id: eu-knowledge-graph.api
  is_public: true
  name: EU Knowledge Graph Wikibase API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-knowledge-graph
  product_url: https://linkedopendata.eu/w/api.php
- category: GraphicalInterface
  description: Kohesio, the main public-facing application built on the EU Knowledge
    Graph. It presents EU cohesion policy projects and their beneficiaries to the public,
    with map and search based discovery. Kohesio won the European Ombudsman's 2023 award
    for good administration in the open administration category.
  format: http
  id: eu-knowledge-graph.kohesio
  name: Kohesio
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-knowledge-graph
  product_url: https://kohesio.ec.europa.eu/
- category: GraphicalInterface
  description: Question answering service over the EU Knowledge Graph, allowing natural
    language questions to be posed against the graph.
  format: http
  id: eu-knowledge-graph.qa
  name: EU Knowledge Graph Question Answering Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-knowledge-graph
  product_url: https://qa.linkedopendata.eu
- category: GraphProduct
  description: Data exports of the EU Knowledge Graph, advertised on the instance's main
    page as available from data.linkedopendata.eu.
  id: eu-knowledge-graph.exports
  name: EU Knowledge Graph Data Exports
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-knowledge-graph
  product_url: https://data.linkedopendata.eu
  warnings:
  - 'Checked on 2026-08-06: the export host returned HTTP 404 for its root and for the
    common Wikibase dump paths that were probed, so no dump file could be located or
    its format determined. The SPARQL endpoint and the Wikibase API were both working
    at the same time, so this appears specific to the export host.'
- category: ProcessProduct
  description: Wikibase configuration of the EU Knowledge Graph, published by the Commission's
    DORIS team, along with the issue tracker used for feature requests and bug reports.
  id: eu-knowledge-graph.wikibase-config
  name: EU Knowledge Graph Wikibase Configuration
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eu-knowledge-graph
  product_url: https://github.com/ec-doris/EuKnowledgeGraph
  repository: https://github.com/ec-doris/EuKnowledgeGraph
  warnings:
  - The repository was archived on GitHub in May 2026 and is read-only. The knowledge
    graph itself remains actively edited.
publications:
- authors:
  - Diefenbach D
  - De Wilde M
  - Alipio S
  doi: 10.1007/978-3-030-88361-4_37
  id: doi:10.1007/978-3-030-88361-4_37
  journal: Lecture Notes in Computer Science
  preferred: true
  title: 'Wikibase as an Infrastructure for Knowledge Graphs: The EU Knowledge Graph'
  year: '2021'
synonyms:
- EU KG
- EuKnowledgeGraph
- Linked Open Data EU
warnings:
- No license is declared for the graph. The Wikibase instance returns empty rights information
  through its API and no license statement was located on the instance or its export
  host, as checked on 2026-08-06. Wikibase deployments commonly place statement data
  under CC0, but that should not be assumed here.
---
# EU Knowledge Graph

## Overview

The EU Knowledge Graph is the European Commission's Wikibase deployment for structured
data about the European Union. Its stated purpose is public legibility: making the
projects the EU finances visible and navigable to citizens with no technical background.
The public-facing product of that goal is **Kohesio**, the cohesion policy project
explorer, which won the European Ombudsman's 2023 award for good administration in the
open administration category.

It is maintained by DG CONNECT, and edits come from Commission services directly — the
instance was being edited by DG REGIO on the day this entry was written.

## Contents

From the instance's own description, confirmed against the live query service on
2026-08-06 (**889,454,967 triples** total):

- **2,111,428 projects** financed by the European Union, recorded through Kohesio.
- **678,448 beneficiaries** of those projects, roughly 10% of them linked back to
  Wikidata so that Wikidata statements complement the Commission's data.
- EU **institutions**, world and EU **countries**, their **capitals**, and Commission
  **Directorates-General**.
- **NUTS 2021**, the Nomenclature of Territorial Units for Statistics used by Eurostat.
- **EuroSciVoc**, the multilingual European Science Vocabulary of scientific fields.
- Commission **facilities** — buildings, canteens, cafeterias, and parkings.

The Wikibase instance reported 3,801,954 pages and more than 48 million edits.

## Access

- **SPARQL endpoint:** `https://query.linkedopendata.eu/sparql`, with a Wikidata-style
  query interface at [query.linkedopendata.eu](https://query.linkedopendata.eu/).
- **Wikibase API:** `https://linkedopendata.eu/w/api.php` — verified responding.
- **Question answering service:** [qa.linkedopendata.eu](https://qa.linkedopendata.eu).
- **Editing:** authorized editors sign in through EU Login and request editor rights;
  an OpenRefine integration is documented on the instance.
- **Data exports** are advertised at `data.linkedopendata.eu`, but that host returned
  HTTP 404 for its root and for the common Wikibase dump paths when checked. The
  endpoint and API were both working at the same time, so this looks specific to the
  export host. Recorded as a product warning.

## Two things this entry deliberately does not claim

1. **A license.** The Wikibase instance returns empty rights information through its
   API, and no license statement was found on the instance or its export host. Wikibase
   deployments often use CC0 for statement data; that is not evidence, so it is not
   recorded.
2. **A dump format.** Since no export file could be located, the exports product
   carries no `format` value rather than a guessed one.

## Relationship to other registry entries

Distinct from `eurio`, the EURIO Knowledge Graph: EURIO is CORDIS research framework
programme data published by the Publications Office as RDF dumps and a Virtuoso
endpoint, while this graph is cohesion policy and general EU data on Wikibase. Both
are also distinct from `era-kg`, the EU Agency for Railways graph, which despite the
similar-sounding name is about railway infrastructure.

An earlier round of research put this graph at roughly 1.83M projects and 644k
beneficiaries, figures traceable to the 2021 ISWC paper. The counts above are current
as of 2026-08-06 and supersede them.
