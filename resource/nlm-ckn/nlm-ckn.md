---
layout: resource_detail
activity_status: active
id: nlm-ckn
name: NLM-CKN
creation_date: 2025-04-17T00:00:00Z
last_modified_date: 2025-06-12T20:33:29Z
description: The NLM Cell Knowledge Network, a knowledge graph that contains knowledge about cellular phenotypes (cell types and cell states) that has been gathered through single cell technologies and related experiments. NLM-CKN is populated using validated computational analysis pipelines and natural language processing of scientific literature and integrated with other public sources of relevant knowledge about genes, anatomical structures, diseases, and drugs.
domains:
- biological systems
- health
- phenotype
contacts:
- category: Individual
  label: Richard Scheuermann
  contact_details:
  - contact_type: email
    value: richard.scheuermann@nih.gov
- category: Individual
  label: Matthew Diller
  orcid: 0000-0001-6378-1703
  contact_details:
  - contact_type: email
    value: matthew.diller@nih.gov
  - contact_type: github
    value: dillerm
repository: https://github.com/NIH-NLM/cell-kn-mvp
products:
- id: nlm-ckn.schema
  name: nlm-ckn-schema
  description: Data model for cell phenotypes and biological entities they relate to.
  product_url: https://github.com/NIH-NLM/cell-kn-schema/blob/main/ckn-schema.yaml
  category: DataModelProduct
  secondary_source:
  - nlm-ckn
  original_source:
  - nlm-ckn
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0-1.0
category: KnowledgeGraph
curators:
- category: Individual
  label: Harry Caufield
  orcid: 0000-0001-5705-7831
  contact_details:
  - contact_type: github
    value: caufieldjh
- category: Individual
  label: Matthew Diller
  orcid: 0000-0001-6378-1703
  contact_details:
  - contact_type: email
    value: matthew.diller@nih.gov
  - contact_type: github
    value: dillerm
---

A knowledge graph that contains knowledge about cellular phenotypes (cell types and cell states) that has been gathered through single cell technologies and related experiments. NLM-CKN is populated using validated computational analysis pipelines and natural language processing of scientific literature and integrated with other public sources of relevant knowledge about genes, anatomical structures, diseases, and drugs.