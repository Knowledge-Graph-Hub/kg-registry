---
activity_status: active
category: Aggregator
collection:
- translator
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: BioPack-team
  - contact_type: url
    value: https://github.com/BioPack-team/shepherd
  label: BioPack Team
- category: Individual
  contact_details:
  - contact_type: email
    value: max@covar.com
  - contact_type: github
    value: maximusunc
  label: Max Wang
creation_date: '2026-10-04T00:00:00Z'
description: Shepherd is a shared platform for NCATS Biomedical Data Translator Autonomous
  Relay Agents (ARAs), developed by the BioPack team. It runs the reasoning workflows
  of several ARAs (ARAGORN, ARAX, BioThings Explorer and SIPR) as operations on common
  infrastructure built from a message broker, a shared response store and per-operation
  workers, and it gets knowledge from Knowledge Providers through Retriever. Each hosted
  ARA has its own TRAPI endpoint and infores identifier.
domains:
- biomedical
- information technology
homepage_url: https://github.com/BioPack-team/shepherd
id: shepherd
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (permissive) among its sources: retriever.'
  id: https://www.apache.org/licenses/LICENSE-2.0
  inferred_from:
  - retriever
  label: Apache License 2.0
  restrictiveness: permissive
  status: inferred
  unresolved_sources: []
name: BioPack Shepherd
products:
- category: ProgrammingInterface
  description: Production Shepherd service (TRAPI 1.5.0, version 1.1.7 when checked
    on 2026-10-04), with endpoints to check the status of asynchronous queries and
    fetch stored responses for all hosted ARAs.
  format: http
  id: shepherd.api
  name: Shepherd TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  - relation_type: prov:wasDerivedFrom
    source: retriever
  product_url: https://shepherd.transltr.io/docs
- category: ProgrammingInterface
  description: TRAPI query endpoint for the ARAGORN ARA implementation within Shepherd
    (/query and /asyncquery), which answers queries with lookup, Omnicorp literature
    co-occurrence support and scoring operations over knowledge from Retriever.
  format: http
  id: shepherd.aragorn.api
  infores_id: shepherd-aragorn
  name: Shepherd ARAGORN TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  - relation_type: prov:wasInfluencedBy
    source: aragorn
  - relation_type: prov:wasDerivedFrom
    source: retriever
  product_url: https://shepherd.transltr.io/aragorn/docs
- category: ProgrammingInterface
  description: TRAPI query endpoint for the ARAX ARA implementation within Shepherd
    (/query and /asyncquery), an in-process port of ARAX's expand, overlay, pathfinding
    and ranking steps over knowledge from Retriever.
  format: http
  id: shepherd.arax.api
  infores_id: shepherd-arax
  name: Shepherd ARAX TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  - relation_type: prov:wasInfluencedBy
    source: arax
  - relation_type: prov:wasDerivedFrom
    source: retriever
  product_url: https://shepherd.transltr.io/arax/docs
- category: ProgrammingInterface
  description: TRAPI query endpoint for the BioThings Explorer (BTE) ARA implementation
    within Shepherd (/query and /asyncquery), over knowledge from Retriever.
  format: http
  id: shepherd.bte.api
  infores_id: shepherd-bte
  name: Shepherd BTE TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  - relation_type: prov:wasInfluencedBy
    source: biothings-explorer
  - relation_type: prov:wasDerivedFrom
    source: retriever
  product_url: https://shepherd.transltr.io/bte/docs
- category: ProgrammingInterface
  description: TRAPI query endpoint for the SIPR ARA within Shepherd (/query and /asyncquery),
    which uses a PageRank algorithm to answer set input queries over knowledge from
    Retriever.
  format: http
  id: shepherd.sipr.api
  infores_id: shepherd-sipr
  name: Shepherd SIPR TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  - relation_type: prov:wasDerivedFrom
    source: retriever
  product_url: https://shepherd.transltr.io/sipr/docs
- category: ProcessProduct
  description: Shepherd source code, with the server, broker, response store and the
    workers for each ARA operation, deployed as Docker containers.
  format: python
  id: shepherd.code
  name: Shepherd Source Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  product_url: https://github.com/BioPack-team/shepherd
- category: DocumentationProduct
  description: Project README describing Shepherd's TRAPI handling, local development
    with Docker Compose and the data downloads its workers need.
  format: http
  id: shepherd.docs
  name: Shepherd Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: shepherd
  product_url: https://github.com/BioPack-team/shepherd#readme
repository: https://github.com/BioPack-team/shepherd
synonyms:
- Shepherd
- Translator Shepherd Service
---
# BioPack Shepherd

Shepherd is a shared platform for Translator ARA implementation. Hosted ARAs share common functionality, such as query intake, response storage, merging, filtering and sorting of results, and they keep the ability to implement their own operations. Workers for each operation run as separate Docker services connected through a message broker.

## Hosted ARAs

Each ARA has its own TRAPI endpoint under the production host and its own Information Resource identifier:

| ARA | Endpoint | infores |
|---|---|---|
| ARAGORN | https://shepherd.transltr.io/aragorn/ | `infores:shepherd-aragorn` |
| ARAX | https://shepherd.transltr.io/arax/ | `infores:shepherd-arax` |
| BioThings Explorer | https://shepherd.transltr.io/bte/ | `infores:shepherd-bte` |
| SIPR | https://shepherd.transltr.io/sipr/ | `infores:shepherd-sipr` |

The infores catalog lists each of these as consuming `infores:retriever` and being consumed by the ARS. Shepherd's own OpenAPI document declares `infores:shepherd`, which was not in the infores catalog when checked on 2026-10-04.

## Deployments

When checked on 2026-10-04, the production (https://shepherd.transltr.io/) and test (https://shepherd.test.transltr.io/) deployments ran version 1.1.7 with TRAPI 1.5.0, and the CI deployment (https://shepherd.ci.transltr.io/) ran version 1.2.1. The main branch of the repository targets TRAPI 2.0.

## License

The repository had no license file when checked on 2026-10-04.
