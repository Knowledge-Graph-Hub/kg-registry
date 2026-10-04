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
  - genomics
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Multiomics-Provider
id: multiomics-kp
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: gtex. Not accounted for, no known license:
    dailymed, faers, tcga.'
  id: https://www.gtexportal.org/home/license
  inferred_from:
  - gtex
  label: GTEx Portal Data License
  restrictiveness: custom
  status: inferred
  unresolved_sources:
  - dailymed
  - faers
  - tcga
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
  - category: GraphProduct
    description: 'EHR Clinical Connections Automat: per-source KGX knowledge graph download
      (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.ehr-clinical-connections
    name: EHR_Clinical_Connections_Automat
    original_source:
    - relation_type: prov:hadPrimarySource
      source: automat
    - relation_type: prov:hadPrimarySource
      source: multiomics-kp
    - relation_type: prov:wasInformedBy
      source: ubergraph
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/EHR_Clinical_Connections_Automat/
  - category: GraphProduct
    description: 'EHR May Treat KP Automat: per-source KGX knowledge graph download
      (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.maytreatkp
    name: MayTreatKP_Automat
    original_source:
    - relation_type: prov:hadPrimarySource
      source: automat
    - relation_type: prov:hadPrimarySource
      source: multiomics-kp
    - relation_type: prov:wasInformedBy
      source: ubergraph
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/MayTreatKP_Automat/
  - category: ProcessProduct
    description: Source code and templates implementing Curated Query Service inference logic.
    format: http
    id: cqs.code
    name: CQS Source Repository
    original_source:
    - relation_type: prov:hadPrimarySource
      source: cqs
    - relation_type: prov:wasInformedBy
      source: aragorn
    - relation_type: prov:wasInformedBy
      source: cohd
    - relation_type: prov:wasInformedBy
      source: molepro
    - relation_type: prov:wasInformedBy
      source: openpredict
    - relation_type: prov:wasInformedBy
      source: rtx-kg2
    - relation_type: prov:wasInformedBy
      source: cam-kp
    - relation_type: prov:wasInformedBy
      source: icees-kg
    - relation_type: prov:wasInformedBy
      source: text-mining-kp
    - relation_type: prov:wasInformedBy
      source: service-kp
    - relation_type: prov:wasInformedBy
      source: ctkp
    - relation_type: prov:wasInformedBy
      source: multiomics-kp
    product_url: https://github.com/TranslatorSRI/CQS
    warnings:
    - As of 2026-10-04 no CQS deployment responded (the transltr.io production host was unreachable;
      ci, test and RENCI dev hosts returned HTTP 404) and the repository had no commits since
      2024-11-15, although the ARS production configuration still lists ara-cqs as an active
      agent.
  - category: ProgrammingInterface
    description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
      querying the BioThings and other APIs registered to the team in SmartAPI.
    format: http
    id: service-kp.trapi
    is_public: true
    name: Service Provider TRAPI
    original_source:
    - relation_type: prov:hadPrimarySource
      source: service-kp
    - relation_type: prov:hadPrimarySource
      source: biothings
    - relation_type: prov:hadPrimarySource
      source: monarchinitiative
    - relation_type: prov:hadPrimarySource
      source: ctd
    - relation_type: prov:hadPrimarySource
      source: complexportal
    - relation_type: prov:hadPrimarySource
      source: uniprot
    - relation_type: prov:hadPrimarySource
      source: litvar
    - relation_type: prov:hadPrimarySource
      source: go
    - relation_type: prov:hadPrimarySource
      source: ols
    - relation_type: prov:hadPrimarySource
      source: alliance
    - relation_type: prov:hadPrimarySource
      source: bindingdb
    - relation_type: prov:hadPrimarySource
      source: bioplanet
    - relation_type: prov:hadPrimarySource
      source: ddinter
    - relation_type: prov:hadPrimarySource
      source: dgidb
    - relation_type: prov:hadPrimarySource
      source: diseases
    - relation_type: prov:hadPrimarySource
      source: gene2phenotype
    - relation_type: prov:hadPrimarySource
      source: foodb
    - relation_type: prov:hadPrimarySource
      source: gtrx
    - relation_type: prov:hadPrimarySource
      source: hp
    - relation_type: prov:hadPrimarySource
      source: idisk
    - relation_type: prov:hadPrimarySource
      source: innatedb
    - relation_type: prov:hadPrimarySource
      source: mgi
    - relation_type: prov:hadPrimarySource
      source: pfocr
    - relation_type: prov:hadPrimarySource
      source: repodb
    - relation_type: prov:hadPrimarySource
      source: rhea
    - relation_type: prov:hadPrimarySource
      source: semmeddb
    - relation_type: prov:hadPrimarySource
      source: suppkg
    - relation_type: prov:hadPrimarySource
      source: ttd
    - relation_type: prov:hadPrimarySource
      source: uberon
    - relation_type: prov:hadPrimarySource
      source: ncbigene
    - relation_type: prov:hadPrimarySource
      source: clingen
    - relation_type: prov:hadPrimarySource
      source: cpdb
    - relation_type: prov:hadPrimarySource
      source: panther
    - relation_type: prov:hadPrimarySource
      source: reactome
    - relation_type: prov:hadPrimarySource
      source: aeolus
    - relation_type: prov:hadPrimarySource
      source: chebi
    - relation_type: prov:hadPrimarySource
      source: chembl
    - relation_type: prov:hadPrimarySource
      source: drugcentral
    - relation_type: prov:hadPrimarySource
      source: disgenet
    - relation_type: prov:hadPrimarySource
      source: mondo
    - relation_type: prov:hadPrimarySource
      source: civic
    - relation_type: prov:hadPrimarySource
      source: clinvar
    - relation_type: prov:hadPrimarySource
      source: dbsnp
    - relation_type: prov:hadPrimarySource
      source: doid
    - relation_type: prov:hadPrimarySource
      source: multiomics-kp
    - relation_type: prov:hadPrimarySource
      source: text-mining-kp
    - relation_type: prov:hadPrimarySource
      source: gdsc
    - relation_type: prov:hadPrimarySource
      source: pubmed
    - relation_type: prov:hadPrimarySource
      source: mygene
    - relation_type: prov:hadPrimarySource
      source: mychem
    product_url: https://bte.transltr.io/v1/team/Service%20Provider
creation_date: '2025-03-09T00:00:00Z'
---

A Translator Knowledge Provider incorporating multiomics data.

## Automated Evaluation

- View the automated evaluation: [multiomics-kp automated evaluation](multiomics-kp_eval_automated.html)
