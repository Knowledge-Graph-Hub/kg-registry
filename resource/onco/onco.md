---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: judegomila
      - contact_type: url
        value: https://judegomila.com
    label: Jude Gomila
creation_date: '2026-09-21T00:00:00Z'
description: OnCo is a public, cited knowledge graph of oncology. It holds one record per cancer, front, technology, target, treatment or test, company, institution, person, pathway, trial, key paper, journal, pairing, roadmap, bottleneck and idea, with links in every direction and a plain-English summary before the technical layer. Every record carries a date of last check and links to a primary source. The corpus is built from TypeScript records in a public repository and refreshed from PubChem, RCSB PDB, Wikidata, OpenAlex, GLOBOCAN, ClinicalTrials.gov, Europe PMC and openFDA. The same corpus ships as a website, a static JSON API with NDJSON, RDF N-Triples and JSON Schema downloads, per-record Markdown context files, a command-line tool and a Model Context Protocol server. The code is MIT and the data are CC BY-NC 4.0.
domains:
  - biomedical
  - clinical
  - drug discovery
  - precision medicine
  - cancer
homepage_url: https://onco.cc/
id: onco
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: CC-BY-NC-4.0
name: OnCo
products:
  - category: GraphProduct
    description: Every OnCo record in one JSON file, each with its plain-English summary, technical summary, dated facts, relationship fields and source links.
    format: json
    id: onco.all_json
    name: OnCo full corpus (JSON)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: onco
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: openalex
      - relation_type: prov:hadPrimarySource
        source: pdb
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: wikidata
    product_file_size: 31490277
    product_url: https://onco.cc/api/v1/all.json
  - category: GraphProduct
    description: Every OnCo record as newline-delimited JSON, one record per line.
    format: json
    id: onco.all_ndjson
    name: OnCo full corpus (NDJSON)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: onco
    product_file_size: 27503450
    product_url: https://onco.cc/api/v1/all.ndjson
  - category: GraphProduct
    description: The OnCo corpus as RDF N-Triples. Records are typed with schema.org classes and linked through the onco.cc namespace.
    format: ntriples
    id: onco.ntriples
    name: OnCo RDF triples
    original_source:
      - relation_type: prov:hadPrimarySource
        source: onco
    product_file_size: 31755993
    product_url: https://onco.cc/api/v1/onco.nt
  - category: DataModelProduct
    description: JSON Schema for OnCo entity records, covering every kind in the corpus and its relationship fields.
    format: json
    id: onco.schema
    name: OnCo entity JSON Schema
    original_source:
      - relation_type: prov:hadPrimarySource
        source: onco
    product_file_size: 78692
    product_url: https://onco.cc/api/v1/schema.json
  - category: ProgrammingInterface
    description: Static JSON API served with CORS. Provides per-kind JSON and CSV files, one JSON file per record with its neighbours, a search index, per-record Markdown context files, Atom feeds and an OpenAPI 3.1 description.
    format: http
    id: onco.api
    name: OnCo static API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: onco
    product_url: https://onco.cc/api/
  - category: ProgrammingInterface
    description: Model Context Protocol server (npm package onco-mcp) exposing search, entity lookup, listing by kind, question answering, context retrieval and comparison over the OnCo corpus to AI assistants. A command-line tool (npm package onco) offers the same operations from the shell.
    format: http
    id: onco.mcp
    name: OnCo MCP server and CLI
    original_source:
      - relation_type: prov:hadPrimarySource
        source: onco
    product_url: https://github.com/judegomila/OnCo/tree/main/packages
    repository: https://github.com/judegomila/OnCo
  - category: GraphicalInterface
    description: The OnCo website. One page per record with filterable tables, tooltips on technical terms, molecule and target renderings, a graph explorer, a body map, a timeline and question answering.
    format: http
    id: onco.site
    name: OnCo website
    original_source:
      - relation_type: prov:hadPrimarySource
        source: onco
    product_url: https://onco.cc/
repository: https://github.com/judegomila/OnCo
taxon:
  - NCBITaxon:9606
---

OnCo is a public, cited knowledge graph of oncology. Every cancer, front, technology, target, treatment and test, company, institution, person, pathway, trial, key paper, journal, pairing, roadmap, bottleneck and idea has one record. Each record opens with a plain-English summary. The technical layer follows. Records link to their neighbours in every direction, and backlinks are derived at build time.

The corpus is stored as TypeScript records in a public GitHub repository. A build step validates identifiers and references, derives backlinks, and emits the website and a static JSON API. Fetchers refresh molecule structures from PubChem and RCSB PDB, logos from Wikidata, research output from OpenAlex, incidence from GLOBOCAN, trial records from ClinicalTrials.gov and literature from Europe PMC, and a fact-check step cross-checks approvals against openFDA. Tagged releases attach the corpus as JSON, NDJSON, CSV, JSON Schema, OpenAPI and Markdown context files.

The code is released under the MIT License. The data are released under CC BY-NC 4.0, with attribution as "Data from OnCo (onco.cc)". Commercial use of the data requires a separate licence. The project states that its content is not medical advice and may be incomplete or out of date.
