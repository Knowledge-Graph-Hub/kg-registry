---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: sanyabt
    label: Sanya Bathla Taneja
creation_date: '2025-03-09T00:00:00Z'
description: NP-KG is a graph framework that creates a biomedical knowledge graph to identify and generate mechanistic hypotheses for pharmacokinetic natural product-drug interactions (NPDIs).
domains:
  - biomedical
  - pharmacology
  - drug discovery
homepage_url: https://doi.org/10.5281/zenodo.6814507
id: np-kg
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: NP-KG
products:
  - category: GraphProduct
    description: Merged KG with ontology-grounded KG and literature-based graph as TSV file
    format: tsv
    id: np-kg.graph.tsv
    name: NP-KG TSV
    original_source:
      - relation_type: prov:hadPrimarySource
        source: np-kg
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: dideo
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: indra
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: oae
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: pheknowlator
      - relation_type: prov:hadPrimarySource
        source: pmc
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: pw
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: semrep
      - relation_type: prov:hadPrimarySource
        source: so
      - relation_type: prov:hadPrimarySource
        source: uberon
    product_file_size: 1074149258
    product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.tsv?download=1
  - category: GraphProduct
    description: Merged KG with ontology-grounded KG and literature-based graph as NetworkX multidigraph object
    dump_format: gpickle
    format: mixed
    id: np-kg.graph.networkx
    name: NP-KG gpickle
    original_source:
      - relation_type: prov:hadPrimarySource
        source: np-kg
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: dideo
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: indra
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: oae
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: pheknowlator
      - relation_type: prov:hadPrimarySource
        source: pmc
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: pw
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: semrep
      - relation_type: prov:hadPrimarySource
        source: so
      - relation_type: prov:hadPrimarySource
        source: uberon
    product_file_size: 936065236
    product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.gpickle?download=1
publications:
  - authors:
      - Taneja SB
      - Callahan TJ
      - Paine MF
      - Kane-Gill SL
      - Kilicoglu H
      - Joachimiak MP
      - Boyce RD
    doi: 10.1016/j.jbi.2023.104341
    id: doi:10.1016/j.jbi.2023.104341
    journal: Journal of Biomedical Informatics
    preferred: true
    title: '''Developing a Knowledge Graph for Pharmacokinetic Natural Product-Drug Interactions'''
    year: '2023'
repository: https://github.com/sanyabt/np-kg
---

NP-KG is a graph framework that creates a biomedical knowledge graph (KG) to identify and generate mechanistic hypotheses for pharmacokinetic natural product-drug interactions (NPDIs). NP-KG uses the PheKnowLator ecosystem to create an ontology-grounded KG. It then uses two relation extraction systems to extract triples from full texts of natural product-related scientific literature to create a literature-based graph, and integrates the nodes and edges in the ontology-grounded KG.

## Automated Evaluation

- View the automated evaluation: [np-kg automated evaluation](np-kg_eval_automated.html)
