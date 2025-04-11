---
activity_status: active
category: DataModel
contacts:
- category: Individual
  email: smoxon@lbl.gov
  github: sierra-moxon
  label: Sierra Taylor Moxon
  orcid: 0000-0002-8719-7760
description: Entity and association taxonomy and datamodel for life-sciences data
domains:
- upper
homepage_url: https://biolink.github.io/biolink-model/
id: biolink
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Biolink-Model
products:
- category: DataModelProduct
  compatibility:
  - standard: biolink
    version: 4.2.5
  description: OWL release of Biolink Model
  format: owl
  id: biolink.model.owl
  name: Biolink Model OWL release
  original_source:
  - biolink
  product_url: https://w3id.org/biolink/biolink-model.owl.ttl
  secondary_source:
  - biolink
- category: DataModelProduct
  compatibility:
  - standard: biolink
    version: 4.2.5
  description: JSON schema release of Biolink Model
  format: json
  id: biolink.model.json
  name: Biolink Model JSON release
  original_source:
  - biolink
  product_url: https://w3id.org/biolink/biolink-model.json
  secondary_source:
  - biolink
- category: DataModelProduct
  compatibility:
  - standard: biolink
    version: 4.2.5
  description: GraphQL release of Biolink Model
  format: graphql
  id: biolink.model.graphql
  name: Biolink Model GraphQL release
  original_source:
  - biolink
  product_url: https://w3id.org/biolink/biolink-model.graphql
  secondary_source:
  - biolink
- category: DataModelProduct
  compatibility:
  - standard: biolink
    version: 4.2.5
  description: Protobuf release of Biolink Model
  format: protobuf
  id: biolink.model.proto
  name: Biolink Model Protobuf release
  original_source:
  - biolink
  product_url: https://raw.githubusercontent.com/biolink/biolink-model/refs/heads/master/project/protobuf/biolink_model.proto
  secondary_source:
  - biolink
- category: DataModelProduct
  compatibility:
  - standard: biolink
    version: 4.2.5
  description: SHACL release of Biolink Model
  format: shacl
  id: biolink.model.shacl
  name: Biolink Model SHACL release
  original_source:
  - biolink
  product_url: https://raw.githubusercontent.com/biolink/biolink-model/refs/heads/master/project/shacl/biolink_model.shacl.ttl
  secondary_source:
  - biolink
- category: DataModelProduct
  compatibility:
  - standard: biolink
    version: 4.2.5
  description: ShEx release of Biolink Model
  format: shex
  id: biolink.model.shex
  name: Biolink Model ShEx release
  original_source:
  - biolink
  product_url: https://raw.githubusercontent.com/biolink/biolink-model/refs/heads/master/project/shex/biolink_model.shex
  secondary_source:
  - biolink
- category: GraphProduct
  description: Biolink Automat
  format: kgx-jsonl
  id: automat.biolink
  name: biolink_automat
  original_source:
  - biolink
  product_url: https://stars.renci.org/var/plater/bl-3.1.2/Biolink_Automat/latest/kgx_files
  secondary_source:
  - automat
- category: ProcessProduct
  description: This repository is a code reference for the C-Path Knowledge Graph
    project, to increase discoverability of rare disease datasets through integration
    with the Monarch Knowlege Graph. Note that this is only a reference to scripts
    and queries associated with this project and is not provided as a runnable project
    because these workflows depend on an internal data catalog.
  id: cpathkg.code
  name: C-Path Knowledge Graph Integration
  original_source:
  - biolink
  - kg-monarch
  product_url: https://gitlab.c-path.org/c-pathontology/c-path-knowledge-graph-integration
  secondary_source:
  - cpathkg
publications:
- authors:
  - Unni DR
  - Moxon SAT
  - Bada M
  - Brush M
  - Bruskiewich R
  - Caufield JH
  - Clemons PA
  - Dancik V
  - Dumontier M
  - Fecho K
  - Glusman G
  - Hadlock JJ
  - Harris NL
  - Joshi A
  - Putman T
  - Qin G
  - Ramsey SA
  - Shefchek KA
  - Solbrig H
  - Soman K
  - Thessen AE
  - Haendel MA
  - Bizon C
  - Mungall CJ
  - The Biomedical Data Translator Consortium
  doi: doi:10.1111/cts.13302
  id: doi:10.1111/cts.13302
  preferred: true
  title: '''Biolink Model: A universal schema for knowledge graphs in clinical, biomedical,
    and translational science'''
  year: '2022'
repository: https://github.com/biolink/biolink-model/
---
Entity and association taxonomy and datamodel for life-sciences data.