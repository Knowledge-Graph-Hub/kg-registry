---
activity_status: active
category: Aggregator
collection:
- translator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: translator@broadinstitute.org
  id: broad
  label: Broad Institute Translator Team
- category: Individual
  label: Sandrine Muller
  orcid: 0000-0001-5998-3003
creation_date: '2025-10-30T00:00:00Z'
description: The Molecular Data Provider (MolePro) is part of the NCATS Biomedical
  Data Translator project, integrating diverse chemical biology data sources into
  a curated framework for chemical entities and their effects on biological targets.
  MolePro consolidates information from over two dozen public chemical biology datasets,
  portals, and tools, providing comprehensive insights into compounds, protein targets,
  and similarity-based connections through both a custom API and TRAPI interface.
domains:
- drug discovery
- chemistry and biochemistry
- biomedical
- pharmacology
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Molecular-Data-Provider
id: molepro
infores_id: molepro
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: Molecular Data Provider
products:
- category: ProgrammingInterface
  description: MolePro API providing access to the knowledge graph of chemical entities
    and biological targets
  format: http
  id: molepro.api
  name: MolePro API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  product_url: https://molepro.transltr.io/molecular_data_provider/api
- category: ProgrammingInterface
  description: TRAPI-compliant interface for MolePro knowledge graph following the
    Translator Reasoner API standard
  format: http
  id: molepro.trapi
  name: MolePro TRAPI Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  product_url: https://molepro-trapi.transltr.io/molepro/trapi/v1.5/ui/
- category: Product
  description: Catalog of MolePro knowledge sources in JSON format
  format: json
  id: molepro.catalog
  name: MolePro Knowledge Sources Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  product_file_size: 2127877
  product_url: https://translator.broadinstitute.org/molecular_data_provider/transformers
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molepro.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molepro.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
- category: GraphProduct
  description: 'MolePro Automat: per-source KGX knowledge graph download (Biolink
    4.2.1).'
  format: kgx-jsonl
  id: automat.molepro
  name: MolePro_Automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:wasInformedBy
    source: ubergraph
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/MolePro_Automat/
- category: GraphicalInterface
  description: JSON index of the ARS production relay server and its registered agent
    endpoints.
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
  product_url: https://ars-prod.transltr.io/ars/api/
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
repository: https://github.com/broadinstitute/molecular-data-provider
synonyms:
- MolePro
- Molecular Data Provider
tags:
- translator
---
# Molecular Data Provider

## Overview

The Molecular Data Provider (MolePro) is part of the NCATS Biomedical Data Translator project, serving as a Knowledge Provider that integrates diverse chemical biology data sources into a unified framework. MolePro enhances understanding of chemical entities and their effects on biological targets through comprehensive data integration and curation.

## Key Features

- **Data Integration**: Consolidates information from over two dozen public chemical biology datasets, portals, and tools
- **Unbiased Approach**: Adheres to stringent policies to avoid expert bias, ensuring impartial data scouting and meticulous data provenance
- **Unified Framework**: Provides a cohesive framework for compounds and targets, facilitating "guilt-by-association" inferences
- **Chemical Biology Expertise**: Contributes expertise in drug discovery, probe development, toxicity flagging, and small-molecule mechanism of action elucidation
- **Similarity-Based Connections**: Includes connections based on chemical and biological similarity

## Interfaces

MolePro provides the same molecular data knowledge through two APIs:

### MolePro API
- **NCATS Translator server**: https://molepro.transltr.io/molecular_data_provider/api
- **Broad Institute server**: https://translator.broadinstitute.org/molecular_data_provider/api

### Translator Reasoner API (TRAPI)
MolePro implements the standardized Translator Reasoner API, integrating query graphs, knowledge graphs, and results into a single HTTP message:
- **NCATS Translator server**: https://molepro-trapi.transltr.io/molepro/trapi/v1.5/ui/
- **Broad Institute server**: https://translator.broadinstitute.org/molepro/trapi/v1.5/ui/

## Knowledge Sources

MolePro's knowledge graph integrates information from over two dozen sources, including:

- BiGG Models, BigGIM, BindingDB
- ChEBI, ChemBank, ChEMBL, CMAP
- CTD, CTRP, DepMap
- DGIdb, DrugBank, DrugCentral, Drug Repurposing Hub
- DSSTox, Gelinea, GtoPdb
- HGNC, HMDB, Inxight:Drugs
- Kinomescan, MSigDB, PharmGKB
- Pharos, ProbeMiner, PubChem
- Reactome, RxNorm, SIDER
- STITCH, STRING

For complete details, see the [Catalog of MolePro knowledge sources](https://translator.broadinstitute.org/molecular_data_provider/transformers).

## Source Code

MolePro is open source and available on GitHub: https://github.com/broadinstitute/molecular-data-provider

## Team Contact

- Email: translator@broadinstitute.org
- Team Lead: Vlado Dancik (@vdancik)