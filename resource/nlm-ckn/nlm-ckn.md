---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: richard.scheuermann@nih.gov
    label: Richard Scheuermann
  - category: Individual
    contact_details:
      - contact_type: email
        value: matthew.diller@nih.gov
      - contact_type: github
        value: dillerm
    label: Matthew Diller
    orcid: 0000-0001-6378-1703
creation_date: '2025-04-17T00:00:00Z'
curators:
  - category: Individual
    contact_details:
      - contact_type: github
        value: caufieldjh
    label: Harry Caufield
    orcid: 0000-0001-5705-7831
  - category: Individual
    contact_details:
      - contact_type: email
        value: matthew.diller@nih.gov
      - contact_type: github
        value: dillerm
    label: Matthew Diller
    orcid: 0000-0001-6378-1703
description: The NLM Cell Knowledge Network, a knowledge graph that contains knowledge about cellular phenotypes (cell types and cell states) that has been gathered through single cell technologies and related experiments. NLM-CKN is populated using validated computational analysis pipelines and natural language processing of scientific literature and integrated with other public sources of relevant knowledge about genes, anatomical structures, diseases, and drugs.
domains:
  - biological systems
  - biomedical
  - phenotype
homepage_url: https://nlm-ckn.org
id: nlm-ckn
last_modified_date: '2026-07-14T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0-1.0
name: NLM-CKN
products:
  - category: GraphProduct
    description: The NLM-CKN knowledge graph of cellular phenotypes. It is built from triple assertions (subject-predicate-object) that link single-cell genomics experimental data (from the CELLxGENE Census) and computationally derived NS-Forest marker genes to the Cell Ontology and other reference ontologies, augmented with literature-derived assertions from text mining/NLP. The graph is produced by the NLM-CKN ETL pipeline as an ArangoDB archive and served via the web application at https://nlm-ckn.org.
    id: nlm-ckn.graph
    name: nlm-ckn-graph
    format: http
    original_source:
      - source: nlm-ckn
        relation_type: prov:hadPrimarySource
      - source: cellxgene
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: cl
        relation_type: prov:wasInfluencedBy
      - source: uberon
        relation_type: prov:wasInfluencedBy
      - source: pato
        relation_type: prov:wasInfluencedBy
      - source: mondo
        relation_type: prov:wasInfluencedBy
      - source: hsapdv
        relation_type: prov:wasInfluencedBy
    product_url: https://nlm-ckn.org
  - category: GraphicalInterface
    description: The NLM-CKN web application, a Django and React interface that loads a pre-built ArangoDB dataset produced by the ETL pipeline and lets researchers query, visualize, and explore the cell knowledge graph.
    id: nlm-ckn.ui
    name: nlm-ckn-ui
    format: http
    original_source:
      - source: nlm-ckn
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NIH-NLM/nlm-ckn-ui
  - category: DataModelProduct
    description: LinkML data model (schema) for cell phenotypes and the biological entities they relate to, defining the node and edge types used in the NLM-CKN knowledge graph.
    id: nlm-ckn.schema
    name: nlm-ckn-schema
    original_source:
      - source: nlm-ckn
        relation_type: prov:hadPrimarySource
    product_file_size: 75158
    product_url: https://github.com/NIH-NLM/nlm-ckn-schema/blob/main/ckn-schema.yaml
  - category: ProcessProduct
    description: The NLM-CKN ETL pipeline, which produces the knowledge graph as an ArangoDB archive from single-cell genomics results and source ontologies. It combines a data processing pipeline (DataFetcher, DataTransformer, TupleWriters, ResultsGraphBuilder) with an ontology processing pipeline (OntologyDownloader, OntologyGraphBuilder), then selects a relevant induced subgraph.
    id: nlm-ckn.etl
    name: nlm-ckn-etl
    original_source:
      - source: nlm-ckn
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NIH-NLM/nlm-ckn-etl
  - category: ProcessProduct
    description: The cellxgene-harvester package, which harvests, filters, and counts normal cells from the CELLxGENE Census using ontology-based filtering (UBERON tissue, PATO/MONDO disease, HsapDv age) to produce per-organ input datasets for the quality-control workflow.
    id: nlm-ckn.harvester
    name: cellxgene-harvester
    original_source:
      - source: nlm-ckn
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NIH-NLM/cellxgene-harvester
  - category: ProcessProduct
    description: The scsilhouette Python package, part of the NLM-CKN quality-control workflow. Together with NSForest F-scores it computes silhouette and summary quality metrics that characterize the single-cell clusters used in the knowledgebase.
    id: nlm-ckn.scsilhouette
    name: scsilhouette
    original_source:
      - source: nlm-ckn
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NIH-NLM/scsilhouette
  - category: ProcessProduct
    description: The sc-nsforest-qc-nf Nextflow workflow, which runs the scsilhouette package and the JCVI NSForest method over each harvested dataset to produce marker genes, F-scores, and silhouette quality metrics consumed downstream by the ETL pipeline.
    id: nlm-ckn.nsforest-qc
    name: sc-nsforest-qc-nf
    original_source:
      - source: nlm-ckn
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NIH-NLM/sc-nsforest-qc-nf
repository: https://github.com/NIH-NLM/nlm-ckn
---

A knowledge graph that contains knowledge about cellular phenotypes (cell types and cell states) that has been gathered through single cell technologies and related experiments. NLM-CKN is populated using validated computational analysis pipelines and natural language processing of scientific literature and integrated with other public sources of relevant knowledge about genes, anatomical structures, diseases, and drugs.

The NLM-CKN infrastructure spans several coordinated repositories: the [cellxgene-harvester](https://github.com/NIH-NLM/cellxgene-harvester) selects and filters single-cell datasets from the CELLxGENE Census; the [sc-nsforest-qc-nf](https://github.com/NIH-NLM/sc-nsforest-qc-nf) Nextflow workflow (using [scsilhouette](https://github.com/NIH-NLM/scsilhouette) and NSForest) generates marker genes and quality metrics; the [NLM-CKN ETL](https://github.com/NIH-NLM/nlm-ckn-etl) pipeline builds the ArangoDB knowledge graph from those results and source ontologies (following the [NLM-CKN schema](https://github.com/NIH-NLM/nlm-ckn-schema)); and the [NLM-CKN UI](https://github.com/NIH-NLM/nlm-ckn-ui) serves it at [nlm-ckn.org](https://nlm-ckn.org).

## Automated Evaluation

- View the automated evaluation: [nlm-ckn automated evaluation](nlm-ckn_eval_automated.html)
