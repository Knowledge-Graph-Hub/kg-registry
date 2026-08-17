---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.imohealth.com/contact/
  - contact_type: url
    value: https://support.imohealth.com/
  label: IMO Health
creation_date: '2026-07-30T00:00:00Z'
description: The IMO Health Knowledge Graph is a commercial clinical knowledge graph
  developed by IMO Health (formerly Intelligent Medical Objects) that links clinical
  language, concepts, and codes into a shared context layer for healthcare data. It
  is built on IMO's clinical interface terminology, curated since 1994 by clinical
  informaticists and coding specialists, and contains millions of concepts, relationships,
  and cross-mappings derived from real-world clinical documentation. The graph encodes
  concept hierarchies, clinical relationships, and cross-maps among standard code
  systems including ICD-10-CM, ICD-9-CM, ICD-10-PCS, SNOMED CT, CPT, HCPCS, LOINC,
  RxNorm, and NDC. IMO reports that the underlying terminology is used by more than
  90% of U.S. clinicians across 4,500+ provider organizations and every major EHR,
  and that it supports roughly 12 billion terminology search transactions per year.
  In April 2026 IMO Health opened direct developer access to the graph through a GraphQL
  API and a Model Context Protocol (MCP) server that exposes graph traversal, hierarchy,
  and cross-mapping operations as tools for AI agents. The graph itself is proprietary,
  and access requires a commercial license and credentials; no public bulk download
  or open query endpoint is available.
domains:
- clinical
- biomedical
- pharmacology
homepage_url: https://www.imohealth.com/knowledge-graph/
id: imo-knowledge-graph
last_modified_date: '2026-07-30T00:00:00Z'
layout: resource_detail
license:
  id: https://www.imohealth.com/terms-of-use/
  label: IMO Health Terms of Use
name: IMO Health Knowledge Graph
products:
- category: Product
  description: The proprietary clinical knowledge graph content itself, comprising
    IMO clinical interface terminology concepts, hierarchies, clinical relationships,
    and cross-maps to standard code systems including ICD-10-CM, ICD-10, SNOMED CT,
    CPT, LOINC, and RxNorm. Delivered under commercial license through the IMO Health
    APIs, EHR integrations, or bulk data agreements.
  format: http
  id: imo-knowledge-graph.data
  name: IMO Health Knowledge Graph Content
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://www.imohealth.com/knowledge-graph/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cpt
  - relation_type: prov:wasDerivedFrom
    source: icd10
  - relation_type: prov:wasDerivedFrom
    source: icd10cm
  - relation_type: prov:wasDerivedFrom
    source: loinc
  - relation_type: prov:wasDerivedFrom
    source: rxnorm
  - relation_type: prov:wasDerivedFrom
    source: snomedct
  warnings:
  - The knowledge graph content is proprietary and is not available as a public bulk
    download. Access requires a commercial agreement with IMO Health.
- category: ProgrammingInterface
  description: GraphQL API providing direct query access to the IMO Health Knowledge
    Graph, supporting retrieval of clinical concepts, concept relationships, hierarchies,
    and code mappings across industry-standard code sets. Launched for external developers
    in April 2026.
  format: graphql
  id: imo-knowledge-graph.graphql_api
  is_public: false
  name: IMO Health Knowledge Graph GraphQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://developer.imohealth.com/api-catalog/knowledge-graph
  warnings:
  - Requires IMO Health developer credentials and a commercial license; no public
    or sandbox endpoint is documented.
- category: ProgrammingInterface
  connection_url: api.imohealth.com/mcp
  description: Model Context Protocol server that exposes the IMO Health Knowledge
    Graph and terminology services as tools for AI assistants and agents. Knowledge
    Graph Access tools include get_relationships, get_hierarchy, and cross_map; additional
    tools cover normalization (normalize_problem, normalize_procedure, normalize_code,
    batch_normalize) and search (search_problem, search_code, get_suggestions). Authentication
    uses a JWT bearer token.
  format: http
  id: imo-knowledge-graph.mcp_server
  is_public: false
  name: IMO Health MCP Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://developer.imohealth.com/mcp-server
  warnings:
  - Requires IMO Health credentials and a JWT token; the server is not openly accessible.
- category: ProgrammingInterface
  description: Terminology Server API providing endpoints for ingesting, searching,
    and managing healthcare terminology datasets backed by the IMO Health Knowledge
    Graph, with licensing controls on the underlying content.
  format: http
  id: imo-knowledge-graph.terminology_server_api
  is_public: false
  name: IMO Health Terminology Server API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://developer.imohealth.com/api-catalog/terminology-server-api
- category: ProgrammingInterface
  description: Crosswalks API supporting creation, update, deletion, and search of
    mappings from multiple source codes to target codes within or across code systems,
    drawing on the cross-mappings maintained in the IMO Health Knowledge Graph.
  format: http
  id: imo-knowledge-graph.crosswalks_api
  is_public: false
  name: IMO Health Crosswalks API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://developer.imohealth.com/api-catalog/crosswalks
- category: ProgrammingInterface
  description: GraphQL API for searching, creating, and retrieving IMO Precision Sets,
    pre-built clinical value sets assembled from the IMO Health Knowledge Graph that
    isolate codes across ICD-10-CM, ICD-9-CM, SNOMED CT, CPT, LOINC, NDC, and RxNorm
    for cohort identification, clinical decision support, and reporting. A companion
    Precision Sets InterOp API supports FHIR and generic responses.
  format: graphql
  id: imo-knowledge-graph.value_sets_api
  is_public: false
  name: IMO Precision Sets Value Sets GraphQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://developer.imohealth.com/api-catalog/value-sets-graphql
- category: Product
  description: Open source data package of IMO clinical terminology and related maps
    for COVID-19, covering problem, lab, and procedure concepts, released in 2020
    under the Creative Commons Attribution 4.0 International Public License along
    with an integration best practice guide. This is the only openly licensed subset
    of IMO content identified.
  format: http
  id: imo-knowledge-graph.covid19_open_data
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: IMO Open Source COVID-19 Terminology and Value Set Data Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://go.imohealth.com/CT-NA-200506-Open-source-terminology-and-value-set-data-COVID-19-01-Landing-page.html
  warnings:
  - Released in May 2020 and not known to be updated since; the landing page is archival
    and current availability of the download was not confirmed.
- category: Product
  description: Public GitHub repositories from IMO Health containing implementation
    samples for integrating with IMO APIs, including Normalize-Samples, snowflake-normalize-integration,
    NLP-sample, and solution-accelerators. These are code examples rather than data
    products and carry no explicit license.
  format: python
  id: imo-knowledge-graph.code_samples
  name: IMO Health API Integration Code Samples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://github.com/imohealth
  repository: https://github.com/imohealth
  warnings:
  - The repositories do not declare a license.
- category: DocumentationProduct
  description: IMO Developer Portal with the API catalog, MCP server documentation,
    authentication guidance, and reference documentation for the Knowledge Graph and
    related services.
  format: http
  id: imo-knowledge-graph.developer_portal
  name: IMO Developer Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://developer.imohealth.com/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-08-06: HTTP 406 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-08-17: HTTP 406 error
    when accessing file'
- category: DocumentationProduct
  description: Product page describing the IMO Health Knowledge Graph, its clinical
    context layer, curation model, and use in grounding clinical AI.
  format: http
  id: imo-knowledge-graph.documentation
  name: IMO Health Knowledge Graph Product Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://www.imohealth.com/knowledge-graph/
synonyms:
- IMO Knowledge Graph
- IMO Clinical Knowledge Graph
- Intelligent Medical Objects Knowledge Graph
taxon:
- NCBITaxon:9606
---
# IMO Health Knowledge Graph

## Overview

The IMO Health Knowledge Graph is the clinical context layer underlying IMO Health's
commercial terminology and clinical AI products. IMO Health, founded in 1994 as
Intelligent Medical Objects and headquartered in Rosemont, Illinois, develops and
licenses clinical interface terminology: the clinician-facing problem, procedure,
and lab terms that sit between free-text documentation and administrative code sets.

The graph organizes those terms into concept hierarchies, clinical relationships,
and cross-maps to standard vocabularies. IMO describes it as containing millions of
concepts, relationships, and mappings derived from real-world clinical data and
maintained by a team of clinical informaticists and coding experts, with continuous
updates to track evolving coding standards and regulatory requirements.

Unlike most entries in this registry, this is a proprietary resource. There is no
public dump, no open SPARQL or Cypher endpoint, and no openly licensed release of
the graph. The entry is included to document what is known about its scope, its
access paths, and the small number of publicly available artifacts associated with it.

## Access

In April 2026 IMO Health opened direct developer access to the graph. Two access
paths are documented on the IMO Developer Portal:

- A **GraphQL API** for querying concepts, relationships, hierarchies, and
  cross-mappings.
- An **MCP server** at `api.imohealth.com/mcp` that exposes graph traversal
  (`get_relationships`, `get_hierarchy`, `cross_map`), normalization, and search
  operations as tools for AI agents. Authentication is by JWT bearer token.

Both require credentials issued under a commercial agreement. The broader API catalog
also includes a Terminology Server API, a Crosswalks API, a Value Sets (Precision
Sets) GraphQL API, a Coding Intelligence API, and clinical NLP services for
context-aware extraction and de-identification.

## Publicly available artifacts

Public resources associated with IMO Health are limited:

- The **open source COVID-19 terminology and value set data package**, released in
  May 2020 under CC BY 4.0, containing COVID-19 problem, lab, and procedure
  terminology with maps and an integration guide. This appears to be the only
  openly licensed subset of IMO content.
- **GitHub repositories** under [imohealth](https://github.com/imohealth), which
  hold API integration samples (`Normalize-Samples`, `snowflake-normalize-integration`,
  `NLP-sample`, `solution-accelerators`) rather than data. None declare a license.
- The **IMO code system registration in HL7 Terminology**
  (`http://imohealth.com/ontology/`, OID `urn:oid:2.16.840.1.113883.3.247`), which
  identifies IMO as a clinical interface terminology for FHIR and related standards
  but does not distribute its content.
- A **research publication list** covering IMO's clinical NLP and knowledge graph
  work, including the KnowledgeSphere drug repurposing framework built over PubMed
  abstracts. These publications describe research systems distinct from the
  commercial clinical knowledge graph described here.

## Source vocabularies

The graph cross-maps IMO's interface terminology to ICD-10-CM, ICD-9-CM, ICD-10-PCS,
SNOMED CT, CPT, HCPCS, LOINC, RxNorm, and NDC. Several of these are separately
registered in KG-Registry and are recorded as secondary sources of the graph content.