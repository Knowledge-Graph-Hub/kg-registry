---
activity_status: inactive
category: KnowledgeGraph
collection:
  - translator
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: balhoff@renci.org
    label: Jim Balhoff
    orcid: 0000-0001-7695-6090
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://renci.org/
    id: renci
    label: RENCI (Renaissance Computing Institute)
creation_date: '2025-12-18T00:00:00Z'
description: CAM-KP (Causal Activity Models Knowledge Provider) is a knowledge provider of the
  NCATS Biomedical Data Translator, developed at RENCI. Causal Activity Models (CAMs) are small
  OWL knowledge graphs that model interactions between instances of ontology concepts. The CAM
  database combines CAMs, including Gene Ontology CAMs (GO-CAMs) and models derived from Reactome
  and the Comparative Toxicogenomics Database (CTD), with a large merged bio-ontology. The knowledge
  graph is served through the RENCI Automat TRAPI service; the original SPARQL service and API
  are no longer maintained.
domains:
  - biomedical
  - pathways
homepage_url: https://automat.renci.org/#/cam-kp
id: cam-kp
infores_id: cam-kp
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License (Repository); Public Domain (Data)
name: CAM-KP (Causal Activity Models Knowledge Provider)
products:
  - category: ProgrammingInterface
    description: SPARQL endpoint for complex semantic queries on the RDF triplestore containing
      causal activity models, ontologies, and integrated biomedical knowledge
    format: http
    id: cam-kp.sparql
    is_public: true
    name: CAM-KP SPARQL Endpoint
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cam-kp
    product_url: https://stars-app.renci.org/cam/sparql
    warnings:
      - The endpoint returned HTTP 404 (with a self-signed certificate) when checked on 2026-11-24,
        and was unreachable on 2026-05-28. No replacement endpoint was found.
  - category: ProgrammingInterface
    description: TRAPI 1.5 API for the CAM-KP graph, served by RENCI Automat (build of 2024-07-22,
      Biolink 4.2.1; 119,917 nodes and 2,219,632 edges). The product URL is the OpenAPI document;
      it also lists Cypher and metadata routes.
    format: http
    id: cam-kp.api
    infores_id: automat-cam-kp
    is_public: true
    name: CAM-KP TRAPI API (Automat)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cam-kp
      - relation_type: prov:hadPrimarySource
        source: automat
    product_url: https://automat.renci.org/cam-kp/openapi.json
  - category: GraphicalInterface
    description: Interactive knowledge provider interface within RENCI's Automat platform for discovering and integrating CAM-KP with other biomedical data sources
    format: http
    id: cam-kp.automat
    is_public: true
    name: CAM-KP on Automat
    product_url: https://automat.renci.org/#/cam-kp
    original_source:
      - source: cam-kp
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Causal Activity Model graphs automatically generated from Reactome pathways using the Pathways2GO tool, translating pathway reactions to causal relationships
    id: cam-kp.reactome-cams
    format: owl
    name: Reactome Pathway CAMs
    original_source:
      - source: cam-kp
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Gene Ontology Causal Activity Model (GO-CAM) annotations manually curated by
      Gene Ontology biocurators linking genes, proteins, and biological processes. Distributed
      as the canonical noctua-models repository, where each model is stored as a Turtle (TTL)
      file.
    format: ttl
    id: cam-kp.go-cams
    name: Gene Ontology CAMs
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cam-kp
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: go-cam
    product_url: https://github.com/geneontology/noctua-models
  - category: Product
    description: Causal activity models of chemical-gene interactions derived from the Comparative
      Toxicogenomics Database (CTD).
    format: http
    id: cam-kp.ctd-interactions
    name: CTD Chemical-Gene Models
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cam-kp
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: doid
  - category: DocumentationProduct
    description: Comprehensive API documentation, SPARQL endpoint documentation, and developer guides for querying and integrating CAM-KP
    format: http
    id: cam-kp.documentation
    is_public: true
    name: CAM-KP Documentation
    product_url: https://github.com/ExposuresProvider/cam-kp-api/wiki
    original_source:
      - source: cam-kp
        relation_type: prov:hadPrimarySource
    warnings:
      - Repository was archived by the owner in 2024; documentation may be historical.
  - category: ProcessProduct
    description: Data loading pipeline that builds the CAM database.
    format: mixed
    id: cam-kp.pipeline
    name: cam-pipeline
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cam-kp
    product_url: https://github.com/ExposuresProvider/cam-pipeline
  - category: GraphProduct
    description: 'CAM-KP Automat: per-source KGX knowledge graph download (Biolink 4.2.1).'
    format: kgx-jsonl
    id: automat.camkp
    name: CAMKP_Automat
    original_source:
    - relation_type: prov:hadPrimarySource
      source: automat
    - relation_type: prov:hadPrimarySource
      source: cam-kp
    - relation_type: prov:wasInformedBy
      source: ubergraph
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/CAMKP_Automat/
  - category: GraphicalInterface
    description: JSON index of the ARS production relay server and its registered agent endpoints.
    format: http
    id: ars.portal
    name: ARS Production Portal
    original_source:
    - relation_type: prov:hadPrimarySource
      source: ars
    - relation_type: prov:wasInformedBy
      source: aragorn
    - relation_type: prov:wasInformedBy
      source: arax
    - relation_type: prov:wasInformedBy
      source: cqs
    - relation_type: prov:wasInformedBy
      source: molepro
    - relation_type: prov:wasInformedBy
      source: cam-kp
    - relation_type: prov:wasInformedBy
      source: openpredict
    - relation_type: prov:wasInformedBy
      source: cohd
    - relation_type: prov:wasInformedBy
      source: icees-kg
    - relation_type: prov:wasInformedBy
      source: genetics-kp
    - relation_type: prov:wasInformedBy
      source: connections-hypothesis-kp
    - relation_type: prov:wasInformedBy
      source: biothings-explorer
    product_url: https://ars-prod.transltr.io/
  - category: ProgrammingInterface
    connection_url: https://ars-prod.transltr.io/ars/api
    description: TRAPI-compatible ARS endpoint for asynchronous query submission.
    format: http
    id: ars.api
    is_public: true
    name: ARS API
    original_source:
    - relation_type: prov:hadPrimarySource
      source: ars
    - relation_type: prov:wasInformedBy
      source: aragorn
    - relation_type: prov:wasInformedBy
      source: arax
    - relation_type: prov:wasInformedBy
      source: cqs
    - relation_type: prov:wasInformedBy
      source: molepro
    - relation_type: prov:wasInformedBy
      source: cam-kp
    - relation_type: prov:wasInformedBy
      source: openpredict
    - relation_type: prov:wasInformedBy
      source: cohd
    - relation_type: prov:wasInformedBy
      source: icees-kg
    - relation_type: prov:wasInformedBy
      source: genetics-kp
    - relation_type: prov:wasInformedBy
      source: connections-hypothesis-kp
    - relation_type: prov:wasInformedBy
      source: biothings-explorer
    product_url: https://ars-prod.transltr.io/ars/api/
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
    description: RENCI-hosted TRAPI endpoint (/query, /asyncquery) for the ARAGORN ARA,
      with Swagger documentation. Queries are answered by Strider over the knowledge
      providers it has registered (here including the Automat ROBOKOP KG, CAM-KP, ICEES,
      Ubergraph, GeLiNEA, Genetics KP, MolePro, OpenPredict and Text Mining KP co-occurrence),
      plus direct ROBOKOP KG lookups for inferred queries, SRI Node Normalizer identifier
      normalization and OmniCorp literature co-occurrence overlays for scoring.
    format: http
    id: aragorn.api
    name: ARAGORN API
    original_source:
    - relation_type: prov:hadPrimarySource
      source: aragorn
    - relation_type: prov:hadPrimarySource
      source: robokop
    - relation_type: prov:hadPrimarySource
      source: automat
    - relation_type: prov:hadPrimarySource
      source: omnicorp
    - relation_type: prov:hadPrimarySource
      source: node-normalizer
    - relation_type: prov:hadPrimarySource
      source: cam-kp
    - relation_type: prov:hadPrimarySource
      source: icees-kg
    - relation_type: prov:hadPrimarySource
      source: ubergraph
    - relation_type: prov:hadPrimarySource
      source: gelinea
    - relation_type: prov:hadPrimarySource
      source: genetics-kp
    - relation_type: prov:hadPrimarySource
      source: molepro
    - relation_type: prov:hadPrimarySource
      source: openpredict
    - relation_type: prov:hadPrimarySource
      source: text-mining-kp
    - relation_type: prov:hadPrimarySource
      source: strider
    product_url: https://aragorn.renci.org/docs
  - category: ProgrammingInterface
    description: Production (NCATS ITRB) deployment of the ARAGORN TRAPI endpoint, with
      Swagger documentation. Like the RENCI deployment it queries knowledge providers
      through Strider, looks up the ROBOKOP KG via Automat, normalizes identifiers with
      the SRI Node Normalizer and scores answers with OmniCorp literature co-occurrence.
    format: http
    id: aragorn.api.itrb
    is_public: true
    name: ARAGORN Production API
    original_source:
    - relation_type: prov:hadPrimarySource
      source: aragorn
    - relation_type: prov:hadPrimarySource
      source: robokop
    - relation_type: prov:hadPrimarySource
      source: automat
    - relation_type: prov:hadPrimarySource
      source: omnicorp
    - relation_type: prov:hadPrimarySource
      source: node-normalizer
    - relation_type: prov:hadPrimarySource
      source: cam-kp
    - relation_type: prov:hadPrimarySource
      source: icees-kg
    - relation_type: prov:hadPrimarySource
      source: genetics-kp
    - relation_type: prov:hadPrimarySource
      source: molepro
    - relation_type: prov:hadPrimarySource
      source: cohd
    - relation_type: prov:hadPrimarySource
      source: connections-hypothesis-kp
    - relation_type: prov:hadPrimarySource
      source: ctkp
    - relation_type: prov:hadPrimarySource
      source: multiomics-kp
    - relation_type: prov:hadPrimarySource
      source: drug-approvals-kp
    - relation_type: prov:hadPrimarySource
      source: microbiomekg
    - relation_type: prov:hadPrimarySource
      source: service-kp
    - relation_type: prov:hadPrimarySource
      source: strider
    product_url: https://aragorn.transltr.io/aragorn/docs
publications:
  - authors:
      - Karamarie Fecho
      - James P. Balhoff
      - Jon-Michael Beasley
      - Chris Bizon
      - Stephen W. Edwards
      - Ashok Krishnamurthy
      - Meisha Mandal
      - Evan Morris
      - Alexander Tropsha
      - Gaurav Vaidya
      - Max Wang
      - Hong Yi
      - David B. Peden
    doi: 10.1016/j.compbiomed.2026.111994
    id: doi:10.1016/j.compbiomed.2026.111994
    journal: Computers in Biology and Medicine
    preferred: true
    title: Integrated query of three open-source bioinformatics tools to reveal clinical and
      molecular insights into environmental determinants of disease
    year: '2026'
  - authors:
      - Karamarie Fecho
      - Chris Bizon
      - Frederick Miller
      - Shepherd Schurman
      - Charles Schmitt
      - William Xue
      - Kenneth Morton
      - Patrick Wang
      - Alexander Tropsha
    doi: 10.2196/26714
    id: doi:10.2196/26714
    journal: JMIR Medical Informatics
    title: A Biomedical Knowledge Graph System to Propose Mechanistic Hypotheses for Real-World
      Environmental Health Observations
    year: '2021'
repository: https://github.com/ExposuresProvider/cam-kp-api
taxon:
  - NCBITaxon:1
last_modified_date: '2026-11-24T00:00:00Z'
warnings:
  - The cam-kp-api repository was archived in 2024, and the original services at stars-app.renci.org
    now return HTTP 404 (checked 2026-11-24). The graph is still served by Automat from a build
    dated 2024-07-22.
---

# CAM-KP (Causal Activity Models Knowledge Provider)

CAM-KP is a knowledge provider of the NCATS Biomedical Data Translator program, developed at RENCI.
Causal Activity Models (CAMs) are small knowledge graphs built in OWL. Each one describes instances
of ontology concepts in a particular context, and models the interactions among them as an
interlinked representation of a biological or environmental process. The CAM database combines many
CAMs with a large merged bio-ontology that holds the vocabulary they use.

## Content

The build currently served by Automat is dated 2024-07-22 (source version 2024-03-21, Biolink 4.2.1)
and has 119,917 nodes and 2,219,632 edges. Its metadata names three primary knowledge sources:
`infores:go-cam`, `infores:aop-cam`, and `infores:ctd`.

## Access

- TRAPI API: <https://automat.renci.org/cam-kp/openapi.json>
- KGX download: see the `automat.camkp` product of Automat
- Pipeline: <https://github.com/ExposuresProvider/cam-pipeline>
- Archived API code: <https://github.com/ExposuresProvider/cam-kp-api>

The SPARQL endpoint and API formerly at `stars-app.renci.org` now return HTTP 404, and the
`cam-kp-api` repository was archived by its owner in 2024.

## Automated Evaluation

- View the automated evaluation: [cam-kp automated evaluation](cam-kp_eval_automated.html)
