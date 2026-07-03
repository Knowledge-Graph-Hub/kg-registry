---
activity_status: active
category: KnowledgeGraph
collection:
  - translator
contacts:
  - category: Individual
    label: "Gwênlyn Glusman"
  - category: Individual
    label: Guangrong Qin
description: A Translator Knowledge Provider incorporating multiomics data.
domains:
  - biomedical
id: multiomics-kp
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: Multiomics KP
products:
  - category: DocumentationProduct
    description: Team overview and interface links for the Multiomics Provider.
    format: http
    id: multiomics-kp.docs
    name: Multiomics KP Documentation
    original_source:
      - source: multiomics-kp
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NCATSTranslator/Translator-All/wiki/Multiomics-Provider
  - category: ProcessProduct
    description: Source repository for deployment and integration code used by the Multiomics Provider team.
    format: http
    id: multiomics-kp.code
    name: Multiomics KP Source Code
    original_source:
      - source: multiomics-kp
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/PriceLab/DOCKET
  - category: GraphProduct
    description: Live TRAPI/BioThings metadata endpoint for the Multiomics BigGIM-DrugResponse KP, exposing the multiomics knowledge graph served by the Multiomics Provider (built from GTEx, TCGA, and drug-response data, with additional clinical-trials, drug-approval and knowledge-resource inputs).
    format: json
    id: multiomics-kp.graph
    name: Multiomics KP Knowledge Graph
    original_source:
      - source: multiomics-kp
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: tcga
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: clinicaltrialsgov
        relation_type: prov:hadPrimarySource
      - source: dailymed
        relation_type: prov:hadPrimarySource
      - source: faers
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: aact
        relation_type: prov:wasInfluencedBy
      - source: biogrid
        relation_type: prov:wasInfluencedBy
      - source: huri
        relation_type: prov:wasInfluencedBy
      - source: cellmarker
        relation_type: prov:wasInfluencedBy
      - source: drugcentral
        relation_type: prov:wasInfluencedBy
      - source: ttd
        relation_type: prov:wasInfluencedBy
      - source: pubmed
        relation_type: prov:wasInfluencedBy
    product_url: https://biothings.transltr.io/biggim_drugresponse_kp/metadata
creation_date: '2025-03-09T00:00:00Z'
---

A Translator Knowledge Provider incorporating multiomics data.

## Automated Evaluation

- View the automated evaluation: [multiomics-kp automated evaluation](multiomics-kp_eval_automated.html)
