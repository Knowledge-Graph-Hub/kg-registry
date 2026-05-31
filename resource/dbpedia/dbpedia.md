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
description: DBpedia is a community knowledge graph published as RDF and built from structured content extracted from Wikipedia and related Wikimedia data. It is accessible through linked data URIs, a public SPARQL endpoint, and continuously updated releases distributed through the DBpedia Databus.
domains:
  - general
homepage_url: https://www.dbpedia.org/
id: dbpedia
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: DBpedia
products:
  - category: GraphicalInterface
    description: Main DBpedia website with documentation, service links, and access points for DBpedia datasets and tooling.
    format: http
    id: dbpedia.portal
    name: DBpedia Web Portal
    original_source:
      - source: dbpedia
        relation_type: prov:hadPrimarySource
    product_url: https://www.dbpedia.org/
  - category: ProgrammingInterface
    description: Public SPARQL endpoint for querying the DBpedia knowledge graph.
    format: http
    id: dbpedia.sparql
    is_public: true
    name: DBpedia SPARQL Endpoint
    original_source:
      - source: dbpedia
        relation_type: prov:hadPrimarySource
    product_url: http://dbpedia.org/sparql
  - category: GraphProduct
    description: Databus collection for the latest core DBpedia release used by the main SPARQL endpoint and linked data interface.
    format: http
    id: dbpedia.latest-core
    name: DBpedia Latest Core Collection
    original_source:
      - source: dbpedia
        relation_type: prov:hadPrimarySource
      - source: wikipedia
        relation_type: prov:wasDerivedFrom
      - source: wikidata
        relation_type: prov:wasDerivedFrom
    product_file_size: 18605
    product_url: https://databus.dbpedia.org/dbpedia/collections/latest-core
  - category: OntologyProduct
    description: DBpedia ontology T-box download used to define the cross-domain schema and mappings applied during DBpedia extraction releases.
    format: owl
    id: dbpedia.ontology
    name: DBpedia Ontology
    original_source:
      - source: dbpedia
        relation_type: prov:hadPrimarySource
    product_url: http://archivo.dbpedia.org/download?o=http%3A//dbpedia.org/ontology/&f=owl
publications:
  - authors:
      - Soren Auer
      - Christian Bizer
      - Georgi Kobilarov
      - Jens Lehmann
      - Richard Cyganiak
      - Zachary Ives
    id: https://doi.org/10.1007/978-3-540-76298-0_52
    journal: The Semantic Web
    preferred: true
    title: 'DBpedia: A Nucleus for a Web of Open Data'
    year: '2007'
  - authors:
      - Christian Bizer
      - Jens Lehmann
      - Georgi Kobilarov
      - Soren Auer
      - Christian Becker
      - Richard Cyganiak
      - Sebastian Hellmann
    id: https://doi.org/10.1016/j.websem.2009.07.002
    journal: Journal of Web Semantics
    title: DBpedia - A crystallization point for the Web of Data
    year: '2009'
repository: https://github.com/dbpedia/extraction-framework
synonyms:
  - DBpedia
---

# DBpedia

## Overview

DBpedia is a large, general-domain knowledge graph published as RDF and derived
from structured content extracted from Wikipedia together with related Wikimedia
and Wikidata inputs. It provides linked data access, a public SPARQL endpoint,
and downloadable releases through the DBpedia Databus.

The current DBpedia release workflow follows an automated monthly extraction
cycle over Wikipedia and Wikidata dumps, with the "Latest Core" collection
serving as the subset loaded into the public SPARQL and linked data services.
DBpedia also maintains a cross-domain ontology and mappings wiki that define the
classes, properties, and extraction mappings used to normalize the published
graph.

## Evaluation

- View the evaluation: [dbpedia evaluation](dbpedia_eval_automated.html)
