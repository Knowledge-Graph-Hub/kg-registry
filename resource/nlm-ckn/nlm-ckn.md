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
id: nlm-ckn
last_modified_date: '2026-07-01T00:00:00Z'
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
    product_url: https://github.com/NIH-NLM/cell-kn-mvp
  - category: DataModelProduct
    description: Data model for cell phenotypes and biological entities they relate to.
    id: nlm-ckn.schema
    name: nlm-ckn-schema
    original_source:
      - source: nlm-ckn
        relation_type: prov:hadPrimarySource
    product_file_size: 4262
    product_url: https://github.com/NIH-NLM/cell-kn-schema/blob/main/ckn-schema.yaml
repository: https://github.com/NIH-NLM/cell-kn-mvp
---

A knowledge graph that contains knowledge about cellular phenotypes (cell types and cell states) that has been gathered through single cell technologies and related experiments. NLM-CKN is populated using validated computational analysis pipelines and natural language processing of scientific literature and integrated with other public sources of relevant knowledge about genes, anatomical structures, diseases, and drugs.

## Automated Evaluation

- View the automated evaluation: [nlm-ckn automated evaluation](nlm-ckn_eval_automated.html)
