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
  structured content extracted from Wikipedia and related Wikimedia data. It is accessible
  through linked data URIs, a public SPARQL endpoint, an entity lookup service, and
  releases distributed through the DBpedia Databus.
domains:
- general
homepage_url: https://www.dbpedia.org/
id: dbpedia
last_modified_date: '2026-10-09T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/3.0/
  label: CC BY-SA 3.0
name: DBpedia
products:
- category: GraphicalInterface
  description: Main DBpedia website with documentation, service links, and access
    points for DBpedia datasets and tooling.
  format: http
  id: dbpedia.portal
  name: DBpedia Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbpedia
  product_url: https://www.dbpedia.org/
- category: ProgrammingInterface
  description: Public SPARQL endpoint for querying the DBpedia knowledge graph.
  format: http
  id: dbpedia.sparql
  is_public: true
  name: DBpedia SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbpedia
  product_url: https://dbpedia.org/sparql
- category: GraphProduct
  description: Databus collection for the latest core DBpedia release used by the
    main SPARQL endpoint and linked data interface.
  format: http
  id: dbpedia.latest-core
  name: DBpedia Latest Core Collection
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbpedia
  - relation_type: prov:wasDerivedFrom
    source: wikipedia
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  product_file_size: 18605
  product_url: https://databus.dbpedia.org/dbpedia/collections/latest-core
- category: OntologyProduct
  description: DBpedia ontology T-box (RDF/XML) defining the cross-domain classes
    and properties used in DBpedia extraction releases, as published on the Databus
    ontology--DEV artifact.
  format: owl
  id: dbpedia.ontology
  latest_version: 2024.07.29-001000
  name: DBpedia Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbpedia
  product_file_size: 5960965
  product_url: https://databus.dbpedia.org/ontologies/dbpedia.org/ontology--DEV/2024.07.29-001000/ontology--DEV_type=parsed.owl
- category: GraphProduct
  compression: gzip
  description: Original extraction of structured Wikipedia data before enrichment,
    as Turtle files covering instance types, labels, geo-coordinates, links, infobox
    properties, abstracts, and categories for the English, German, and French editions.
  format: ttl
  id: dbpedia.wikipedia-kg-dump
  latest_version: '2025-12-01'
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: DBpedia Wikipedia KG Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbpedia
  - relation_type: prov:wasDerivedFrom
    source: wikipedia
  product_file_size: 5340
  product_url: https://databus.dbpedia.org/dbpedia/dbpedia-wikipedia-kg-dump
- category: GraphProduct
  compression: gzip
  description: Original extraction of structured Wikidata data before enrichment,
    as Turtle files.
  format: ttl
  id: dbpedia.wikidata-kg-dump
  latest_version: '2025-12-01'
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: DBpedia Wikidata KG Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbpedia
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  product_file_size: 5343
  product_url: https://databus.dbpedia.org/dbpedia/dbpedia-wikidata-kg-dump
- category: ProgrammingInterface
  description: DBpedia Lookup, a search service for finding DBpedia resource URIs
    by label or keyword.
  format: http
  id: dbpedia.lookup
  is_public: true
  name: DBpedia Lookup
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbpedia
  product_url: https://lookup.dbpedia.org/
publications:
- authors:
  - Jens Lehmann
  - Robert Isele
  - Max Jakob
  - Anja Jentzsch
  - Dimitris Kontokostas
  - Pablo N. Mendes
  - Sebastian Hellmann
  - Mohamed Morsey
  - Patrick van Kleef
  - Sören Auer
  - Christian Bizer
  doi: 10.3233/SW-140134
  id: https://doi.org/10.3233/SW-140134
  journal: Semantic Web
  preferred: true
  title: DBpedia - A large-scale, multilingual knowledge base extracted from Wikipedia
  year: '2015'
- authors:
  - Marvin Hofer
  - Sebastian Hellmann
  - Milan Dojchinovski
  - Johannes Frey
  doi: 10.1007/978-3-030-59833-4_1
  id: https://doi.org/10.1007/978-3-030-59833-4_1
  journal: Lecture Notes in Computer Science
  title: 'The New DBpedia Release Cycle: Increasing Agility and Efficiency in Knowledge
    Extraction Workflows'
  year: '2020'
- authors:
  - Sören Auer
  - Christian Bizer
  - Georgi Kobilarov
  - Jens Lehmann
  - Richard Cyganiak
  - Zachary Ives
  doi: 10.1007/978-3-540-76298-0_52
  id: https://doi.org/10.1007/978-3-540-76298-0_52
  journal: Lecture Notes in Computer Science
  title: 'DBpedia: A Nucleus for a Web of Open Data'
  year: '2007'
- authors:
  - Christian Bizer
  - Jens Lehmann
  - Georgi Kobilarov
  - Sören Auer
  - Christian Becker
  - Richard Cyganiak
  - Sebastian Hellmann
  doi: 10.1016/j.websem.2009.07.002
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

DBpedia introduced an automated extraction and release cycle over Wikipedia and
Wikidata dumps in 2020 (Hofer et al.). The "Latest Core" collection is the subset
loaded into the public SPARQL and linked data services; its Databus metadata was
last modified in June 2023, and the newest classic extraction releases on the
Databus are dated 2022-12-01. Newer extractions are published as the Wikipedia and
Wikidata "KG dump" groups (latest version 2025-12-01, CC BY-SA 4.0). The project
site states the data are offered under CC BY-SA 3.0 and the GNU Free
Documentation License.
DBpedia also maintains a cross-domain ontology and mappings wiki that define the
classes, properties, and extraction mappings used to normalize the published
graph.

## Evaluation

- View the evaluation: [dbpedia evaluation](dbpedia_eval_automated.html)