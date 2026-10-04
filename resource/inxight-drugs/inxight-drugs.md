---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ncats.nih.gov/
  id: ncats
  label: NCATS
creation_date: '2026-06-18T00:00:00Z'
description: Inxight Drugs is a comprehensive and curated drug database developed
  by the National Center for Advancing Translational Sciences (NCATS) to support translational
  research. It provides rigorously curated information on drug substances, including
  their regulatory approval and development status, ingredient definitions, mechanisms
  of action, biological targets, and pharmacological class. The resource resolves
  ambiguity in substance identity by applying the FDA Global Substance Registration
  System (GSRS) and links each substance to detailed marketing, regulatory, and clinical
  development metadata. Inxight Drugs serves as an upstream primary source for downstream
  knowledge resources such as the Molecular Data Provider (MolePro) and the Molecular
  Data Knowledge Provider.
domains:
- pharmacology
- drug discovery
- clinical
- chemistry and biochemistry
homepage_url: https://drugs.ncats.io
id: inxight-drugs
infores_id: inxight-drugs
last_modified_date: '2026-09-08T00:00:00Z'
layout: resource_detail
license:
  id: https://drugs.ncats.io/
  label: Public Domain (NCATS states all facts in these datasets are in the public domain)
name: 'Inxight: Drugs'
products:
- category: ProgrammingInterface
  description: Public REST API providing programmatic access to curated drug substances,
    approval and development status, mechanisms, targets, and related metadata in
    the Inxight Drugs database.
  format: http
  id: inxight-drugs.api
  name: 'Inxight: Drugs REST API'
  original_source:
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  product_file_size: 39857
  product_url: https://drugs.ncats.io/api/v1/substances
- category: GraphicalInterface
  description: Web portal interface for browsing and searching the curated Inxight
    Drugs database of drug substances, including approval status, mechanisms, and
    targets.
  format: http
  id: inxight-drugs.portal
  name: 'Inxight: Drugs Web Portal'
  original_source:
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  product_url: https://drugs.ncats.io
  warnings: []
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
publications:
- authors:
  - Vishal B. Siramshetty
  - Ivan Grishagin
  - Ðức-Trung Nguyễn
  - Tyler Peryea
  - Yulia Skovpen
  - Oleg Stroganov
  - Daniel Katzel
  - Timothy Sheils
  - Ajit Jadhav
  - Ewy A. Mathé
  - Noel T. Southall
  doi: 10.1093/nar/gkab918
  id: https://pubmed.ncbi.nlm.nih.gov/34648031
  journal: Nucleic Acids Res
  preferred: true
  title: 'NCATS Inxight Drugs: a comprehensive and curated portal for translational
    research'
  year: '2022'
---
# Inxight: Drugs

## Overview

Inxight: Drugs is a comprehensive and curated drug database developed by the National Center for Advancing Translational Sciences (NCATS). It is designed to support translational research by providing high-quality, manually curated information about drug substances and their development across the discovery-to-market pipeline.

## Curated Content

The resource provides detailed information for each drug substance, including:

- **Substance identity**: Rigorous ingredient definitions based on the FDA Global Substance Registration System (GSRS), resolving ambiguity in chemical and biological substance identity.
- **Approval and development status**: Regulatory approval status and the stage of clinical or commercial development.
- **Mechanisms and targets**: Mechanisms of action and associated biological targets.
- **Pharmacology and class**: Pharmacological class and related drug metadata.
- **Marketing and regulatory metadata**: Information on marketing status and regulatory history.

## Role as an Upstream Source

Inxight: Drugs acts as an upstream primary source (transformer input) for downstream knowledge resources, including the Molecular Data Provider (MolePro) and the molecular-data knowledge provider, which transform and integrate its curated drug data into knowledge-graph form.

## Access

- **Web portal**: Browse and search the database at [drugs.ncats.io](https://drugs.ncats.io).
- **REST API**: Programmatic access is available through the public Inxight Drugs API.

## Automated Evaluation

- View the automated evaluation: [inxight-drugs automated evaluation](inxight-drugs_eval_automated.html)