---
activity_status: active
category: KnowledgeGraph
collection:
- aop
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: marvinm2
  - contact_type: url
    value: https://orcid.org/0000-0003-2230-0840
  label: Marvin Martens
- category: Individual
  contact_details:
  - contact_type: url
    value: https://orcid.org/0000-0001-7542-0286
  label: Egon Willighagen
creation_date: '2026-08-17T00:00:00Z'
description: AOP-Wiki RDF is an RDF representation of the AOP-Wiki, the authoring
  interface of the Adverse Outcome Pathway Knowledge Base. The AOP-Wiki XML export
  is converted to RDF/Turtle every week using the AOP Ontology (aopo) together with
  Dublin Core, CHEMINF and NCIT, and is enriched with gene mappings (gene names in
  key events matched to HGNC symbols and resolved to Ensembl, NCBI Gene, UniProt and
  Protein Ontology identifiers through BridgeDb) and chemical cross-references. AOPs,
  key events, key event relationships, biological events, stressors and chemicals
  get identifiers.org URIs and are linked to ChEBI, GO, PATO, UBERON, CL, NCBITaxon
  and HGNC. The 2026.08.15 release has about 340,000 triples, covering 595 AOPs, 1,595
  key events, 2,360 key event relationships, 754 stressors and 430 chemicals. The
  data is served from a public SPARQL endpoint with a SNORQL query interface on top
  of it. A grlc REST API built from the same curated query library, a second endpoint
  holding every quarterly AOP-Wiki snapshot since 2018 as named graphs, and a dashboard
  for version-over-version trends are also available.
domains:
- toxicology
- environment
- pathways
- chemistry and biochemistry
homepage_url: https://aopwiki.rdf.bigcat-bioinformatics.org/
id: aopwiki-rdf
language: en
last_modified_date: '2026-08-17T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: AOP-Wiki RDF
products:
- category: ProgrammingInterface
  connection_url: https://aopwiki.rdf.bigcat-bioinformatics.org/sparql
  description: Public SPARQL 1.1 endpoint (Virtuoso 7.2.11) serving the AOP-Wiki RDF
    graph, including the gene-mapping and cross-reference enrichments. Supports SELECT,
    CONSTRUCT, ASK and DESCRIBE over HTTP GET/POST with JSON, XML, CSV and Turtle
    result serializations, and federated queries via SERVICE. Reloaded weekly from
    the generated Turtle files.
  format: http
  id: aopwiki-rdf.sparql
  is_public: true
  name: AOP-Wiki RDF SPARQL Endpoint
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  product_url: https://aopwiki.rdf.bigcat-bioinformatics.org/sparql
- category: GraphicalInterface
  description: SNORQL web interface ("AOP-Wiki RDF Explorer") for interactive SPARQL
    querying of the AOP-Wiki RDF endpoint. Provides a CodeMirror SPARQL editor with
    syntax highlighting, a browsable library of curated and parameterized example
    queries, endpoint health indication, result browsing with dereferenceable URIs,
    and CSV/JSON/XML export.
  format: http
  id: aopwiki-rdf.snorql
  name: AOP-Wiki RDF SNORQL Interface
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  product_url: https://aopwiki.rdf.bigcat-bioinformatics.org/
  repository: https://github.com/marvinm2/AOP-Wiki-Snorql-UI
- category: GraphProduct
  description: The AOP-Wiki RDF dataset in RDF/Turtle, covering AOPs, key events,
    key event relationships, biological events, stressors and chemicals converted
    from the AOP-Wiki XML export, together with the gene mappings (HGNC approved symbols
    resolved to Ensembl, NCBI Gene, UniProt and Protein Ontology identifiers via BridgeDb)
    and the chemical and protein cross-reference enrichments. Distributed as Turtle
    files in the data/ directory of the conversion repository (AOPWikiRDF.ttl, AOPWikiRDF-Genes.ttl,
    AOPWikiRDF-Enriched.ttl); all of them are loaded together into the SPARQL endpoint
    and are meant to be used as one dataset. Regenerated weekly.
  format: ttl
  id: aopwiki-rdf.ttl
  latest_version: 2026.08.15
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: AOP-Wiki RDF Turtle Dataset
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  - relation_type: prov:used
    source: ensembl
  - relation_type: prov:used
    source: hgnc
  - relation_type: prov:used
    source: ncbigene
  - relation_type: prov:used
    source: pr
  - relation_type: prov:used
    source: uniprot
  product_url: https://github.com/marvinm2/AOPWikiRDF/tree/master/data
  repository: https://github.com/marvinm2/AOPWikiRDF
- category: Product
  description: VoID metadata describing the AOP-Wiki RDF dataset, its triple counts,
    licence, provenance, update frequency and SPARQL endpoint.
  format: ttl
  id: aopwiki-rdf.void
  name: AOP-Wiki RDF VoID Description
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  product_file_size: 1055
  product_url: https://raw.githubusercontent.com/marvinm2/AOPWikiRDF/master/data/AOPWikiRDF-Void.ttl
- category: ProcessProduct
  description: Python conversion pipeline that transforms the AOP-Wiki XML export
    into RDF/Turtle, performs the three-stage gene-mapping algorithm, and runs Turtle
    syntax and URI-resolvability quality control. Executed weekly by GitHub Actions
    (Saturdays 08:00 UTC). Code is MIT licensed.
  format: http
  id: aopwiki-rdf.converter
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT License
  name: AOP-Wiki XML to RDF Conversion Tool
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  product_url: https://github.com/marvinm2/AOPWikiRDF
  repository: https://github.com/marvinm2/AOPWikiRDF
- category: ProgrammingInterface
  connection_url: https://aopwiki-multirdf.vhp4safety.nl/sparql
  description: Companion SPARQL endpoint holding every quarterly AOP-Wiki snapshot
    from 2018-04-01 onwards as separate named graphs (http://aopwiki.org/graph/YYYY-MM-DD),
    33 versions at present, for tracking how AOP-Wiki content evolves over time.
  format: http
  id: aopwiki-rdf.multiversion-sparql
  is_public: true
  name: AOP-Wiki RDF Multi-Version SPARQL Endpoint
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  product_url: https://aopwiki-multirdf.vhp4safety.nl/sparql
  repository: https://github.com/marvinm2/AOP-Wiki_multi-endpoint
- category: GraphicalInterface
  description: Web dashboard visualizing the content and growth of AOP-Wiki RDF across
    all quarterly versions, with entity counts, key event component and ontology usage
    breakdowns, network statistics, completeness metrics and an interactive AOP network
    view. Every plot exposes the SPARQL query behind it and offers CSV export.
  format: http
  id: aopwiki-rdf.dashboard
  name: AOP-Wiki RDF Dashboard
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  product_url: https://aopwiki-dashboard.vhp4safety.nl
  repository: https://github.com/marvinm2/AOP-Wiki-RDF-dashboard
- category: ProgrammingInterface
  connection_url: https://aopwiki.api.bigcat-bioinformatics.org/
  description: grlc-generated REST API that exposes the curated AOP-Wiki SPARQL example
    queries as parameterized HTTP endpoints with a Swagger/OpenAPI description, for
    users who prefer REST over writing SPARQL.
  format: http
  id: aopwiki-rdf.grlc-api
  is_public: true
  name: AOP-Wiki RDF grlc REST API
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  product_url: https://aopwiki.api.bigcat-bioinformatics.org/
  repository: https://github.com/marvinm2/AOP-Wiki-Queries
- category: DocumentationProduct
  description: Curated library of documented SPARQL example queries for AOP-Wiki RDF,
    organised by category (metadata, AOPs, key events, KERs, stressors, chemicals,
    data export, federated queries). Consumed by both the SNORQL interface and the
    grlc REST API.
  format: http
  id: aopwiki-rdf.queries
  name: AOP-Wiki SPARQL Query Library
  original_source:
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: aopwiki-rdf
  product_url: https://github.com/marvinm2/AOP-Wiki-Queries
  repository: https://github.com/marvinm2/AOP-Wiki-Queries
publications:
- authors:
  - Marvin Martens
  - Chris T. Evelo
  - Egon L. Willighagen
  doi: 10.1089/aivt.2021.0010
  id: doi:10.1089/aivt.2021.0010
  journal: Applied In Vitro Toxicology
  preferred: true
  title: Providing Adverse Outcome Pathways from the AOP-Wiki in a Semantic Web Format
    to Increase Usability and Accessibility of the Content
  year: '2022'
- authors:
  - Marvin Martens
  - Egon Willighagen
  - Chris Evelo
  doi: 10.5281/zenodo.13353286
  id: doi:10.5281/zenodo.13353286
  journal: Zenodo
  title: Adverse Outcome Pathway Wiki RDF
  year: '2026'
repository: https://github.com/marvinm2/AOPWikiRDF
synonyms:
- AOPWikiRDF
- AOP-Wiki RDF Explorer
version: 2026.08.15
---
# AOP-Wiki RDF

## Overview

AOP-Wiki RDF is a semantic web representation of the AOP-Wiki, the community
authoring and curation interface of the Adverse Outcome Pathway Knowledge Base
(AOP-KB). The weekly AOP-Wiki XML export is converted to RDF/Turtle
using the AOP Ontology (aopo) alongside Dublin Core, CHEMINF and NCIT, making the
mechanistic toxicology content of the AOP-Wiki queryable with SPARQL.

## Content

The 2026.08.15 release contains roughly 340,000 triples across three Turtle files
that are loaded together as a single dataset:

- `AOPWikiRDF.ttl` — triples derived directly from the AOP-Wiki XML export
- `AOPWikiRDF-Genes.ttl` — gene mapping enrichment
- `AOPWikiRDF-Enriched.ttl` — chemical and protein cross-reference enrichment

This covers 595 AOPs, 1,595 key events, 2,360 key event relationships, 754 stressors
and 430 chemicals. AOPs, key events, key event relationships, biological events,
stressors and chemicals receive identifiers.org URIs and are linked out to ChEBI, GO,
PATO, UBERON, CL, NCBITaxon and HGNC. Gene names appearing in key events are matched
to HGNC approved symbols and resolved to Ensembl, NCBI Gene, UniProt and Protein
Ontology identifiers through BridgeDb.

## Access

- A public Virtuoso SPARQL endpoint, reloaded weekly, with a SNORQL query interface
  ("AOP-Wiki RDF Explorer") on top of it
- A grlc-generated REST API built from the same curated SPARQL query library, for
  users who prefer REST over writing SPARQL
- A companion multi-version endpoint holding every quarterly AOP-Wiki snapshot since
  2018-04-01 as separate named graphs, for tracking content change over time
- A dashboard visualizing content and growth across all quarterly versions

## Licensing

The generated RDF dataset files are released under CC BY-SA 4.0. The conversion code
in the AOPWikiRDF repository is separately licensed under the MIT License.