---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cordis.europa.eu/contact/en
  - contact_type: url
    value: https://op.europa.eu
  label: Publications Office of the European Union
creation_date: '2026-08-06T00:00:00Z'
description: The EURIO (EUropean Research Information Ontology) Knowledge Graph publishes
  CORDIS data about research projects funded by the European Union's framework programmes
  for research and innovation - FP7, Horizon 2020, and Horizon Europe - as linked
  data. It covers projects together with their grants, payments, and monetary amounts;
  the organizations that participate in them and the roles those organizations play;
  and project outputs including deliverables, publications, journal papers, and proceedings
  papers, alongside SKOS reference data for countries, funding schemes, programmes,
  and topics. When queried on 2026-08-06 the graph held 26,429,912 triples, including
  80,208 projects, 72,534 organizations, and 696,156 results. Entities are minted
  in the http://data.europa.eu/s66# namespace. The graph is published by the Publications
  Office of the European Union both as a full dump and as per-entity named graph subsets,
  each available in RDF/XML, Turtle, N-Quads, N-Triples, and JSON-LD, and is queryable
  through a public Virtuoso SPARQL endpoint on the CORDIS Datalab. Its schema, the
  EURIO ontology, is aligned with EU ontologies such as DINGO and FRAPO and with widely
  used vocabularies including schema.org and the W3C Organization Ontology.
domains:
- research funding
- literature
homepage_url: https://cordis.europa.eu/datalab
id: eurio
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
name: EURIO Knowledge Graph
products:
- category: ProgrammingInterface
  description: Public Virtuoso SPARQL endpoint over the EURIO Knowledge Graph. Verified
    queryable on 2026-08-06, when the graph reported 26,429,912 triples. The CORDIS
    Datalab provides a query interface over the same endpoint at https://cordis.europa.eu/datalab/sparql-endpoint/en.
  format: http
  id: eurio.sparql
  is_public: true
  name: EURIO SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eurio
  product_url: https://cordis.europa.eu/datalab/sparql
- category: GraphicalInterface
  description: CORDIS Datalab, the Publications Office's interface for exploring CORDIS
    data, including the SPARQL query interface over the EURIO Knowledge Graph and
    its catalogue of example queries.
  format: http
  id: eurio.datalab
  name: CORDIS Datalab
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eurio
  product_url: https://cordis.europa.eu/datalab/sparql-endpoint/en
- category: GraphProduct
  compression: zip
  description: Full dump of the EURIO Knowledge Graph, containing all CORDIS data
    about research projects funded under FP7, Horizon 2020, and Horizon Europe. Distributed
    as a zipped N-Quads file of approximately 1.19 GB; the same dump is also published
    in RDF/XML, Turtle, N-Triples, and JSON-LD. The edge count recorded here is the
    triple count reported by the live SPARQL endpoint on 2026-08-06.
  edge_count: 26429912
  format: nquads
  id: eurio.dump
  name: EURIO Knowledge Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eurio
  product_file_size: 1190300961
  product_url: https://cordis.europa.eu/data/cordis-EURIOKnowledgeGraph-nq.zip
- category: GraphProduct
  compression: zip
  description: Projects named graph, the subset of the EURIO Knowledge Graph covering
    all projects funded under the FP7, Horizon 2020, and Horizon Europe framework
    programmes. Distributed as a zipped N-Quads file of approximately 373 MB, and
    also available in RDF/XML, Turtle, N-Triples, and JSON-LD.
  format: nquads
  id: eurio.projects-graph
  name: EURIO Projects Named Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eurio
  product_file_size: 372749888
  product_url: https://cordis.europa.eu/data/cordis-projectNamedGraph-nq.zip
- category: GraphProduct
  compression: zip
  description: Organisations named graph, the subset of the EURIO Knowledge Graph
    covering the organizations participating in funded projects. Distributed as a
    zipped N-Quads file of approximately 100 MB, and also available in RDF/XML, Turtle,
    N-Triples, and JSON-LD.
  format: nquads
  id: eurio.organisations-graph
  name: EURIO Organisations Named Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eurio
  product_file_size: 100174043
  product_url: https://cordis.europa.eu/data/cordis-organisationNamedGraph-nq.zip
- category: GraphProduct
  compression: zip
  description: Results named graph, the subset of the EURIO Knowledge Graph covering
    project results, including deliverables and publications. Distributed as a zipped
    N-Quads file of approximately 577 MB, and also available in RDF/XML, Turtle, N-Triples,
    and JSON-LD.
  format: nquads
  id: eurio.results-graph
  name: EURIO Results Named Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eurio
  product_file_size: 577116349
  product_url: https://cordis.europa.eu/data/cordis-resultNamedGraph-nq.zip
- category: OntologyProduct
  description: The EURIO (EUropean Research Information Ontology) ontology, which
    defines the structure of the EURIO Knowledge Graph and its named graphs. Developed
    by CORDIS on the basis of data about EU framework programme projects, following
    Semantic Web standards, and aligned with EU ontologies such as DINGO and FRAPO
    as well as schema.org and the W3C Organization Ontology. Published through EU
    Vocabularies at the Publications Office.
  format: owl
  id: eurio.ontology
  name: EURIO Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eurio
  product_url: https://op.europa.eu/en/web/eu-vocabularies/eurio
- category: DocumentationProduct
  description: Dataset record on the EU Open Data Portal for the EURIO Knowledge Graph
    dump and named graphs, giving the distributions, formats, publisher, and an annual
    update frequency.
  format: http
  id: eurio.dataset-record
  name: EURIO Knowledge Graph Dataset Record
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eurio
  product_url: https://data.europa.eu/data/datasets/named-graphs-from-eurio-knowledge-graph
synonyms:
- EURIO
- EUropean Research Information Ontology Knowledge Graph
- CORDIS EURIO Knowledge Graph
warnings:
- No license is stated for this data. The DCAT records on the EU Open Data Portal
  carry no license field for the EURIO dataset or for its distributions, at either
  dataset or distribution level, as verified through the data.europa.eu search API
  on 2026-08-06. Reuse is presumably governed by the European Commission's general
  reuse policy, but that should be confirmed against the CORDIS legal notice before
  the data is redistributed.
---
# EURIO Knowledge Graph

## Overview

EURIO — the **EUropean Research Information Ontology** — is the linked data
publication of CORDIS, the European Commission's research project information
service. The knowledge graph covers projects funded by the EU's framework programmes
for research and innovation: FP7, Horizon 2020, and Horizon Europe. It is published by
the Publications Office of the European Union and queryable through the CORDIS Datalab.

This is the graph that descriptions of an "ERA Knowledge Graph" covering European
research institutions, projects, and funding are usually reaching for; the resource
actually named ERA Knowledge Graph (`era-kg`) is the EU Agency for Railways'
infrastructure graph and is unrelated.

## Contents

Measured against the live endpoint on 2026-08-06 (26,429,912 triples total), the
largest entity types are:

| Type | Count |
| --- | --- |
| `eurio:Result` | 696,156 |
| `eurio:MonetaryAmount` | 580,939 |
| `eurio:GrantPayment` | 422,007 |
| `eurio:ProjectPublication` | 419,740 |
| `eurio:OrganisationRole` | 398,584 |
| `eurio:JournalPaper` | 283,136 |
| `eurio:ProjectDeliverable` | 211,188 |
| `eurio:Grant` | 80,222 |
| `eurio:Project` | 80,208 |
| `eurio:Organisation` | 72,534 |

Entities are minted under `http://data.europa.eu/s66#`. Reference data for countries,
funding schemes, programmes, and topics is carried as SKOS concepts (207,637 of them).

The shape of the graph is worth noting for registry purposes: it links **funding** to
**organizations** to **research outputs**, which makes it usable as a provenance and
funding-context source for resources catalogued elsewhere in this registry, not only
as a project directory.

## Access

- **SPARQL endpoint:** `https://cordis.europa.eu/datalab/sparql` (Virtuoso), with a
  query interface and example queries at
  [cordis.europa.eu/datalab/sparql-endpoint/en](https://cordis.europa.eu/datalab/sparql-endpoint/en).
- **Full dump:** ~1.19 GB zipped N-Quads, plus RDF/XML, Turtle, N-Triples, and JSON-LD.
- **Named graph subsets:** projects (~373 MB), organisations (~100 MB), and results
  (~577 MB), each in the same five serializations. Sizes confirmed from response
  headers on 2026-08-06.
- The DCAT record gives an **annual** accrual periodicity; Horizon Europe data was
  added to the graph after the initial FP7/H2020 release.

Non-RDF tabular releases of the same underlying CORDIS data (xlsx, csv) are published
as separate datasets per framework programme on the EU Open Data Portal.

## Licensing gap

No license is stated for this data anywhere the entry could find it: the DCAT records
on data.europa.eu carry no license field for the EURIO dataset or for any of its
distributions. Reuse is presumably covered by the Commission's general reuse policy,
but the entry records this as a warning rather than asserting CC BY 4.0 on the graph's
behalf.