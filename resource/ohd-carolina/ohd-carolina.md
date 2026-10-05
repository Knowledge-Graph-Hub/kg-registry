---
activity_status: active
category: KnowledgeGraph
collection:
- translator
- omop
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://renci.org/
  label: RENCI
- category: Individual
  contact_details:
  - contact_type: email
    value: kebedey@renci.org
  - contact_type: github
    value: YaphetKG
  label: Yaphet Kebede
creation_date: '2026-10-04T00:00:00Z'
description: Open Health Data @ Carolina (OHD@Carolina) is a statistical association
  knowledge graph of concept prevalence and co-occurrence in electronic health records,
  derived from UNC Health's OMOP database on a five-year cohort of about 6 million
  patients (2018 through 2022). Edges link conditions, drugs, procedures and phenotypes
  with positive or negative correlation predicates and carry chi-squared p-values,
  log odds ratios and sample sizes. Concepts and pairs with counts of 10 or fewer
  were excluded and counts were randomized with a Poisson distribution to protect
  patient privacy. RENCI builds it with ORION and serves it as an Automat TRAPI knowledge
  provider for the NCATS Biomedical Data Translator.
domains:
- biomedical
- clinical
- electronic health records
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Open-Health-Data-at-Carolina
id: ohd-carolina
infores_id: automat-openhealthdata-carolina
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (permissive) among its sources: automat, translator.'
  id: https://opensource.org/license/mit/
  inferred_from:
  - automat
  - translator
  label: MIT
  restrictiveness: permissive
  status: inferred
  unresolved_sources: []
name: Open Health Data @ Carolina
products:
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.2.1
  description: KGX JSONL nodes and edges files for the OHD@Carolina Automat graph
    (build f627ebbefd242454, source version 2024-11-18, published 2025-10-06), with
    27,356 nodes and 22,732,570 edges. Edges use biolink:positively_correlated_with
    (22,352,823) and biolink:negatively_correlated_with (379,747).
  edge_count: 22732570
  format: kgx-jsonl
  id: ohd-carolina.graph
  infores_id: automat-openhealthdata-carolina
  name: OHD@Carolina Automat KGX Graph
  node_categories:
  - biolink:Disease
  - biolink:PhenotypicFeature
  - biolink:Drug
  - biolink:SmallMolecule
  - biolink:MolecularMixture
  - biolink:ChemicalEntity
  - biolink:Protein
  - biolink:OrganismTaxon
  - biolink:ComplexMolecularMixture
  - biolink:Gene
  - biolink:InformationContentEntity
  node_count: 27356
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ohd-carolina
  - relation_type: prov:wasInfluencedBy
    source: ohdsi
  predicates:
  - biolink:positively_correlated_with
  - biolink:negatively_correlated_with
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/OHD_Carolina_Automat/f627ebbefd242454/
  versions:
  - f627ebbefd242454
- category: GraphProduct
  description: Neo4j database dump of the OHD@Carolina Automat graph (build f627ebbefd242454,
    about 1.7 GB).
  dump_format: neo4j
  format: neo4j
  id: ohd-carolina.neo4j
  name: OHD@Carolina Automat Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ohd-carolina
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/OHD_Carolina_Automat/f627ebbefd242454/graph_f627ebbefd242454.db.dump
- category: ProgrammingInterface
  description: Automat TRAPI endpoint for OHD@Carolina, with query, meta knowledge
    graph, Cypher and node lookup operations (Biolink 4.2.1).
  format: http
  id: ohd-carolina.trapi
  infores_id: automat-openhealthdata-carolina
  name: OHD@Carolina Automat TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ohd-carolina
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://automat.renci.org/ohd/docs
- category: Product
  description: Meta knowledge graph JSON listing the node categories, predicates and
    edge attributes in the OHD@Carolina Automat graph.
  format: json
  id: ohd-carolina.metadata
  name: OHD@Carolina Meta Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ohd-carolina
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/OHD_Carolina_Automat/f627ebbefd242454/meta_knowledge_graph.json
- category: Product
  compression: zip
  description: Source edge table (unc_omop_2018_2022_kg.csv, about 2 GB zipped) of
    concept pair associations from the UNC Health OMOP cohort, with chi-squared p-values,
    log odds ratios, scores and sample sizes, as ingested by the ORION OHD parser
    (build 2024-11-18).
  format: csv
  id: ohd-carolina.source-edges
  infores_id: openhealthdata-carolina
  name: OHD@Carolina Source Edge Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ohd-carolina
  - relation_type: prov:wasInfluencedBy
    source: ohdsi
  product_url: https://stars.renci.org/var/data_services/ohd/unc_omop_2018_2022_kg.zip
  versions:
  - '2024-11-18'
- category: GraphProduct
  description: 'OHD Carolina Automat: per-source KGX knowledge graph download (Biolink
    4.2.1).'
  format: kgx-jsonl
  id: automat.ohd-carolina
  name: OHD_Carolina_Automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: ohd-carolina
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/OHD_Carolina_Automat/
synonyms:
- OHD@Carolina
- OHD Carolina
- Openhealth Data at Carolina
- Automat Openhealth Data at Carolina
---
# Open Health Data @ Carolina

Open Health Data @ Carolina (OHD@Carolina) exposes counts, frequencies and co-occurrence statistics of clinical concepts from UNC Health's OMOP database. The cohort covers about 6 million UNC Health patients over 2018 through 2022, including inpatient and outpatient visits. Concepts are coded by their OMOP standard concept IDs and normalized to Biolink-compatible identifiers (RxNorm, UMLS, MONDO, ChEBI, HP and others) in the knowledge graph.

It follows the approach of [COHD](cohd.html), the Columbia Open Health Data service, applied to UNC Health data. Counts for each concept include patients from all descendant concepts. To protect patient privacy, concepts and concept pairs with counts of 10 or fewer were excluded and counts were randomized with a Poisson distribution.

## Graph

The Automat graph built on 2025-09-28 (build `f627ebbefd242454`, published 2025-10-06) holds 27,356 nodes and 22,732,570 edges, all from `infores:openhealthdata-carolina`. Every edge is a statistical association (`biolink:positively_correlated_with` or `biolink:negatively_correlated_with`) with `p_value`, `log_odds_ratio`, `log_odds_ratio_95_ci` and `total_sample_size` attributes.

## Access

- TRAPI: https://automat.renci.org/ohd/
- KGX and Neo4j downloads: https://stars.renci.org/var/plater/bl-4.2.1/OHD_Carolina_Automat/
- Source data: https://stars.renci.org/var/data_services/ohd/

The source infores is `infores:openhealthdata-carolina`. The Automat graph is `infores:automat-openhealthdata-carolina`, consumed by ARAGORN.