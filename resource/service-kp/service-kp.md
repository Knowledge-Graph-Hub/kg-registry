---
activity_status: active
category: KnowledgeGraph
collection:
- translator
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cwu@scripps.edu
  - contact_type: github
    value: newgene
  label: Chunlei Wu
creation_date: '2025-03-09T00:00:00Z'
description: The NCATS Translator Service Provider KP, run by the Su and Wu labs at
  Scripps Research, builds and hosts BioThings-based knowledge provider APIs such
  as MyGene.info, MyChem.info, MyDisease.info and MyVariant.info, plus about 30 other
  wrapped data sources. They are exposed together as one TRAPI service through the
  BioThings Explorer Service Provider team endpoint.
domains:
- biomedical
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Service-Provider
id: service-kp
infores_id: service-provider-trapi
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/Apache-2.0
  label: Apache-2.0
name: Service KP
products:
- category: DocumentationProduct
  description: Team documentation for the Translator Service Provider.
  format: http
  id: service-kp.docs
  name: Service KP Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  product_url: https://github.com/NCATSTranslator/Translator-All/wiki/Service-Provider
- category: GraphicalInterface
  description: SmartAPI Translator portal for browsing registered Translator APIs.
  format: http
  id: service-kp.portal
  name: Service KP SmartAPI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  product_url: https://smart-api.info/portal/translator
- category: ProcessProduct
  description: BioThings API stack source repository used by the Service Provider
    team.
  format: http
  id: service-kp.code
  name: Service KP Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  product_url: https://github.com/biothings/biothings.api
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
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
- category: ProcessProduct
  description: Source code and templates implementing Curated Query Service inference
    logic.
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
  - As of 2026-10-04 no CQS deployment responded (the transltr.io production host
    was unreachable; ci, test and RENCI dev hosts returned HTTP 404) and the repository
    had no commits since 2024-11-15, although the ARS production configuration still
    lists ara-cqs as an active agent.
publications:
- authors:
  - Sebastien Lelong
  - Xinghua Zhou
  - Cyrus Afrasiabi
  - Zhongchao Qian
  - Marco Alvarado Cano
  - Ginger Tsueng
  - Jiwen Xin
  - Julia Mullen
  - Yao Yao
  - Ricardo Avila
  - Greg Taylor
  - Andrew I Su
  - Chunlei Wu
  doi: 10.1093/bioinformatics/btac017
  id: https://www.ncbi.nlm.nih.gov/pubmed/35020801
  journal: Bioinformatics
  preferred: true
  title: 'BioThings SDK: a toolkit for building high-performance data APIs in biomedical
    research'
  year: '2022'
- authors:
  - Jackson Callaghan
  - Colleen H Xu
  - Jiwen Xin
  - Marco Alvarado Cano
  - Anders Riutta
  - Eric Zhou
  - Rohan Juneja
  - Yao Yao
  - Madhumita Narayan
  - Kristina Hanspers
  - Ayushi Agrawal
  - Alexander R Pico
  - Chunlei Wu
  - Andrew I Su
  doi: 10.1093/bioinformatics/btad570
  id: doi:10.1093/bioinformatics/btad570
  journal: Bioinformatics
  title: 'BioThings Explorer: a query engine for a federated knowledge graph of biomedical
    APIs'
  year: '2023'
repository: https://github.com/biothings/biothings.api
---
The NCATS Translator Service Provider KP, run by the Su and Wu labs at Scripps Research, builds and hosts BioThings-based knowledge provider APIs such as MyGene.info, MyChem.info, MyDisease.info and MyVariant.info, plus about 30 other wrapped data sources. They are exposed together as one TRAPI service through the BioThings Explorer Service Provider team endpoint.

The team maintains the BioThings SDK and the SmartAPI registry. Its TRAPI endpoint is https://bte.transltr.io/v1/team/Service%20Provider, and its API list is defined in the BioThings Explorer `bte-server` configuration.

## Automated Evaluation

- View the automated evaluation: [service-kp automated evaluation](service-kp_eval_automated.html)