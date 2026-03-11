---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.dbpedia.org/about/
  label: DBpedia Association
creation_date: '2026-03-11T00:00:00Z'
description: DBpedia is a community knowledge graph published as RDF and built from
  structured content extracted from Wikipedia and related Wikimedia data. It is
  accessible through linked data URIs, a public SPARQL endpoint, and continuously
  updated releases distributed through the DBpedia Databus.
domains:
- general
homepage_url: https://www.dbpedia.org/
id: dbpedia
layout: resource_detail
last_modified_date: '2026-03-11T00:00:00Z'
name: DBpedia
products:
- category: GraphicalInterface
  description: Main DBpedia website with documentation, service links, and access
    points for DBpedia datasets and tooling.
  format: http
  id: dbpedia.portal
  name: DBpedia Web Portal
  original_source:
  - dbpedia
  product_url: https://www.dbpedia.org/
- category: ProgrammingInterface
  description: Public SPARQL endpoint for querying the DBpedia knowledge graph.
  format: http
  id: dbpedia.sparql
  is_public: true
  name: DBpedia SPARQL Endpoint
  original_source:
  - dbpedia
  product_url: http://dbpedia.org/sparql
- category: Product
  description: Databus collection for the latest core DBpedia release used by the
    main SPARQL endpoint and linked data interface.
  format: http
  id: dbpedia.latest-core
  name: DBpedia Latest Core Collection
  original_source:
  - dbpedia
  - wikipedia
  - wikidata
  secondary_source:
  - dbpedia
  product_url: https://databus.dbpedia.org/dbpedia/collections/latest-core
synonyms:
- DBpedia
---

# DBpedia

## Overview

DBpedia is a large, general-domain knowledge graph published as RDF and derived
from Wikipedia-related content. It provides linked data access, a public SPARQL
endpoint, and downloadable releases through the DBpedia Databus.
