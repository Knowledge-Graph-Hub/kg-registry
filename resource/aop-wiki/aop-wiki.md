---
activity_status: active
category: DataSource
collection:
- aop
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://aopwiki.org/info_pages/10
  label: AOP-Wiki Coordination Group
creation_date: '2025-09-04T00:00:00Z'
description: The AOP-Wiki is the primary collaborative authoring and curation interface
  for the Adverse Outcome Pathway Knowledge Base (AOP-KB). It enables the community
  to develop, review, browse, and export Adverse Outcome Pathways (AOPs) linking molecular
  initiating events through key events to adverse outcomes relevant to human and ecological
  risk assessment. Structured exports (XML and tabular subsets) support computational
  toxicology, ontology mapping, and integration into predictive assessment workflows.
domains:
- toxicology
- environment
- pathways
homepage_url: https://aopwiki.org/
id: aop-wiki
last_modified_date: '2026-05-26T00:00:00Z'
layout: resource_detail
license:
  id: https://aopwiki.org/
  label: Varies
name: AOP-Wiki
products:
- category: GraphicalInterface
  description: Web portal for browsing, authoring, and reviewing AOPs, key events
    (KEs), key event relationships (KERs), stressors, and supporting documentation
  format: http
  id: aop-wiki.portal
  name: AOP-Wiki Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: https://aopwiki.org/
- category: ProgrammingInterface
  connection_url: https://aopwiki-rdf.prod.openrisknet.org/
  description: OpenRiskNet SPARQL endpoint loaded with RDF converted from AOP-Wiki
    quarterly XML dumps for querying AOPs, key events, key event relationships, and
    stressors.
  format: http
  id: aop-wiki.sparql
  is_public: true
  name: AOP-Wiki SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: https://openrisknet.org/e-infrastructure/services/133/
- category: Product
  description: Quarterly permanent XML snapshot (versioned) of AOP-Wiki content suitable
    for citation and archival use
  format: xml
  id: aop-wiki.quarterly-xml
  latest_version: '2026-04-01'
  name: AOP-Wiki Quarterly XML Snapshot
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: https://aopwiki.org/downloads
- category: Product
  description: Nightly XML export (rolling) containing latest AOP-Wiki content (overwritten
    daily)
  format: xml
  id: aop-wiki.nightly-xml
  name: AOP-Wiki Nightly XML Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_file_size: 9933339
  product_url: https://aopwiki.org/downloads/aop-wiki-xml.gz
- category: Product
  description: Tab-delimited subset listing AOP to Key Event (including MIE, intermediate
    KE, and Adverse Outcome) associations
  format: tsv
  id: aop-wiki.ke-overview
  name: AOP-Wiki Key Events TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_file_size: 238066
  product_url: https://aopwiki.org/downloads/aop_ke_mie_ao.tsv
- category: Product
  description: Tab-delimited subset listing Key Event Relationships (KERs) with evidence
    and quantitative understanding indicators
  format: tsv
  id: aop-wiki.ker
  name: AOP-Wiki Key Event Relationships TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_file_size: 189389
  product_url: https://aopwiki.org/downloads/aop_ke_ker.tsv
- category: Product
  description: Tab-delimited subset of Key Event Components (actions, biological objects/processes
    with ontology references)
  format: tsv
  id: aop-wiki.ke-components
  name: AOP-Wiki Key Event Components TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_file_size: 291132
  product_url: https://aopwiki.org/downloads/aop_ke_ec.tsv
- category: Product
  description: Per-AOP dynamic XML feed accessible via each AOP page (XML button)
    for up-to-minute content retrieval
  format: xml
  id: aop-wiki.dynamic-aop-xml
  name: AOP-Wiki Dynamic AOP XML Feed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: https://aopwiki.org/aops
- category: DocumentationProduct
  description: This document is the AOP Developers' Handbook supplement to the Guidance
    Document for developing and assessing Adverse Outcome Pathways (AOPs). The Guidance
    Document provides a historical background for the AOP development programme, and
    outlines the elements required to construct an AOP as well as the principles of
    the AOP framework.
  format: http
  id: aop-wiki.devhandbook
  name: AOP Developers' Handbook
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: https://aopwiki.org/handbooks/4
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  format: http
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 1000genomes
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: toxcast
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
- category: ProgrammingInterface
  connection_url: https://aopdb.rdf.bigcat-bioinformatics.org/
  description: OpenRiskNet Virtuoso SPARQL endpoint loaded with RDF of the EPA AOP-DB
    for querying integrated AOP, gene, chemical, disease, tissue, pathway, orthology,
    ontology, and gene interaction relationships.
  format: http
  id: aop-db.sparql
  is_public: true
  name: AOP-DB SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: https://openrisknet.org/e-infrastructure/services/147/
- category: GraphProduct
  description: RDF knowledge graph (Turtle) repackaging AOP-Wiki data as an open knowledge
    graph
  format: ttl
  id: biobricks-aopwiki.graph
  name: BioBricks AOP-Wiki Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-aopwiki
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  product_url: https://github.com/biobricks-ai/aopwikirdf-kg
  warnings:
  - 'File was not able to be retrieved when checked on 2026-08-12: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-08-17: HTTP 404 error
    when accessing file'
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
taxon:
- NCBITaxon:9606
version: '2.8'
---
# AOP-Wiki

## Overview

The AOP-Wiki is the collaborative platform of the Adverse Outcome Pathway Knowledge Base (AOP-KB). It captures structured mechanistic knowledge describing how molecular initiating events propagate through measurable key events to adverse outcomes of regulatory relevance. The resource supports transparent evidence organization, peer review, and reuse across chemical safety evaluation, risk prioritization, and method development.

## Data & Exports

Multiple export modalities enable programmatic reuse:

- Quarterly XML snapshots (stable, citable)
- Nightly rolling XML (latest content)
- Dynamic XML feed per AOP (on-demand freshness)
- Targeted TSV subsets (key events, key event relationships, key event components)

## Use Cases

- Mechanistic evidence mapping and visualization
- Integrating AOP structures into predictive toxicology pipelines
- Identifying knowledge gaps in AOP development
- Ontology alignment and cross-resource linking

## Governance & Community

Content is community-authored and coordinated via the AOP-Wiki Coordination Group with international participation (academia, government, and NGOs). Peer review pathways align with OECD processes for AOP endorsement.

## Access Notes

Dynamic per-AOP XML feeds are obtained directly from individual AOP pages (XML button). Nightly and quarterly exports plus TSV subsets are documented on the Download Options page.

## Citation

When reusing AOP-Wiki content, cite the AOP-Wiki (access date), relevant quarterly snapshot (if used), and any underlying ontologies or complementary resources referenced in analyses.