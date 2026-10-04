---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/center-development-therapeutics-cdot
  id: broad-cdot
  label: Broad Institute Center for the Development of Therapeutics (CDoT)
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/
  id: broad-institute
  label: Broad Institute
creation_date: '2025-09-09T00:00:00Z'
description: The Drug Repurposing Hub is a curated and annotated collection of FDA-approved
  drugs, clinical trial drugs, and selected pre-clinical tool compounds from the Broad
  Institute. The collection contains 7,423 unique compounds targeting 2,255 protein
  targets, with annotations for 775 drug indications and extensive metadata including
  structures, mechanisms, and therapeutic areas.
domains:
- drug discovery
- pharmacology
- biomedical
- drug repositioning
homepage_url: https://repo-hub.broadinstitute.org/repurposing
id: repohub
infores_id: drug-repurposing-hub
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
name: Drug Repurposing Hub
products:
- category: GraphicalInterface
  description: Web portal for exploring the Drug Repurposing Hub compound collection
    and annotations
  format: http
  id: repohub.portal
  name: Repurposing Hub Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#home
- category: GraphicalInterface
  description: Interactive data portal for searching and exploring compound annotations,
    targets, mechanisms, and indications
  format: http
  id: repohub.data-portal
  name: Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing-app
- category: Product
  description: Downloadable drug information file with compound metadata including
    names, structures, targets, mechanisms, and indications
  format: http
  id: repohub.drug-info
  name: Drug Information Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#download
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: Product
  description: Downloadable sample information file with compound library details
    and annotations
  format: http
  id: repohub.sample-info
  name: Sample Information Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#download
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: Product
  description: Physical screening library of 5,506 compounds (90% FDA-approved or
    in clinical trials) available as assay-ready plates
  id: repohub.screening-library
  name: Screening Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#about
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: Product
  description: REPO1 subset library available in 5-point, 10-fold dilution series
    as single-use assay-ready plates
  id: repohub.repo1-library
  name: REPO1 Dilution Series Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#about
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: Product
  description: Follow-up compound collection of approximately 2,400 compounds available
    for secondary studies
  id: repohub.followup-compounds
  name: Follow-up Compound Collection
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#about
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: DocumentationProduct
  description: About page with detailed information on the Drug Repurposing Hub history,
    team, and usage
  format: http
  id: repohub.about
  name: About the Repurposing Hub
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#about
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: DocumentationProduct
  description: Case studies demonstrating applications of the Drug Repurposing Hub
  format: http
  id: repohub.case-studies
  name: Case Studies
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#case-studies
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: DocumentationProduct
  description: Information about conducting screens with the Drug Repurposing Hub
    library
  format: http
  id: repohub.screening-info
  name: Screening Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_url: https://repo-hub.broadinstitute.org/repurposing#screen
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: DocumentationProduct
  description: Policy document for compound intake and donation to the collection
  format: pdf
  id: repohub.intake-policy
  name: Compound Intake Policy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_file_size: 57661
  product_url: https://repo-hub.broadinstitute.org/public/data/Compound_Intake_Policy.pdf
  warnings:
  - Automated HTTPS checks on 2026-05-23 still fail TLS certificate validation for
    repo-hub.broadinstitute.org, although the endpoint responds with HTTP 200 when
    certificate verification is bypassed.
- category: Product
  description: Latest drug-level annotations including compound names, clinical phase,
    mechanism of action, and protein targets (listed as version 2025-08-19 on the
    site).
  format: tsv
  id: repohub.drug-info.tsv
  name: Drug Repurposing Hub Drug Information TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_file_size: 661900
  product_url: https://repo-hub.broadinstitute.org/public/data/repo-drug-annotation-20200324.txt
  warnings:
  - 'File was not able to be retrieved with default certificate verification when
    checked on 2026-06-01: SSL certificate verification failed; file responded with
    HTTP 200 when checked without local certificate verification'
- category: Product
  description: Latest physical sample-level metadata including Broad sample IDs, vendor
    catalog numbers, SMILES, InChIKey, and PubChem IDs (listed as version 2025-08-19
    on the site).
  format: tsv
  id: repohub.sample-info.tsv
  name: Drug Repurposing Hub Sample Information TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  product_file_size: 4072927
  product_url: https://repo-hub.broadinstitute.org/public/data/repo-sample-annotation-20240610.txt
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubchem
  warnings:
  - 'File was not able to be retrieved with default certificate verification when
    checked on 2026-06-01: SSL certificate verification failed; file responded with
    HTTP 200 when checked without local certificate verification'
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
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
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
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
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
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
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Drug Repurposing Hub distributed via the
    NCATS Translator release site (release 2026_03_06; build drug_rep_hub_2025-08-19_99c18ef1_2025sep1_4.3.6;
    source version 2025-08-19; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 19389
  format: kgx-jsonl
  id: translator.drug_rep_hub.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Drug Repurposing Hub KGX Graph
  node_count: 8842
  original_source:
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/drug_rep_hub/latest/
  versions:
  - '2026_03_06'
  - drug_rep_hub_2025-08-19_99c18ef1_2025sep1_4.3.6
publications:
- authors:
  - Corsello
  - Bittker
  - Liu
  - Gould
  - McCarren
  - Hirschman
  - Johnston
  - Vrcic
  - Wong
  - Khan
  - Asiedu
  - Narayan
  - Mader
  - Subramanian
  - Golub
  doi: 10.1038/nm.4306
  id: https://doi.org/10.1038/nm.4306
  journal: Nature Medicine
  preferred: true
  title: 'The Drug Repurposing Hub: a next-generation drug library and information
    resource'
  year: '2017'
taxon:
- NCBITaxon:9606
---
# Drug Repurposing Hub

The Drug Repurposing Hub is a curated and annotated collection of compounds developed and maintained by the Broad Institute's Center for the Development of Therapeutics (CDoT). The Hub represents a powerful resource for drug discovery, enabling researchers to explore known biological targets and pathways, discover new biological insights, and identify new therapeutic applications for existing drugs.

## Overview

Drug repurposing—finding new uses for existing drugs—offers significant advantages over traditional drug development. By testing thousands of already-approved or clinically-tested drugs for their ability to treat different diseases, researchers can potentially accelerate therapeutic development while leveraging existing safety and pharmacokinetic data.

The Broad Institute launched the Drug Repurposing Hub in 2015, initially to accelerate cancer treatments. Since then, the resource has expanded to support research across dozens of disease areas, including tuberculosis, kidney disease, infectious diseases, and many others.

## Collection Statistics

The Drug Repurposing Hub contains:
- **7,423 unique compounds**
- **2,255 protein targets**
- **775 drug indications**
- **5,506 compounds** in the screening library (90% FDA-approved or in clinical trials)
- **~2,400 additional compounds** available for follow-up studies

## Compound Categories

The collection includes three main categories of compounds:

1. **FDA-Approved Drugs**: Compounds already approved for clinical use
2. **Clinical Trial Drugs**: Compounds currently in various phases of clinical development
3. **Pre-clinical Tool Compounds**: Selected compounds useful for target validation and biological research

All compounds are:
- Curated and annotated with extensive metadata
- Characterized for structure, targets, mechanisms, and indications
- Quality-controlled (>85% purity by UPLC-MS)
- Well-characterized with known biological activities

## Key Features

### Comprehensive Annotations

Each compound in the Hub is annotated with:
- **Chemical structure**: Structural information and identifiers
- **Targets**: Known protein targets and binding interactions
- **Mechanisms of action**: How the compounds work at the molecular level
- **Indications**: Diseases and conditions the compounds are used to treat
- **Clinical development phase**: FDA approval status or clinical trial phase
- **Therapeutic areas**: Disease areas and biological systems

### Screening Library Access

The physical library is available for screening through two formats:

1. **Full Library**: 5,506 compounds at single concentration as assay-ready plates
2. **REPO1 Subset**: Multi-dose format with 5-point, 10-fold dilution series

Libraries are available to:
- Academic and research institutions
- Non-profit organizations worldwide
- Both on-site at Broad Institute and remote locations
- On a cost-recovery basis for non-profit institutions

**Note**: Individual compounds are not sold separately. A small subset of controlled substances is only available for screening at the Broad Institute.

### Data Portal

The interactive data portal allows users to:
- Search compounds by name, structure, target, or indication
- Explore relationships between compounds, targets, and diseases
- Filter by clinical development phase, therapeutic area, or mechanism
- Access downloadable batch data files

### Integration with Other Projects

The Drug Repurposing Hub compounds are profiled by multiple complementary projects:
- **Connectivity Map (CMap)**: Gene expression profiles
- **Cancer Dependency Map/PRISM**: Cancer cell line vulnerability data
- **NIH LINCS**: Library of Integrated Network-Based Cellular Signatures
- **JUMP Cell Painting Consortium**: Morphological profiling

## Evolution of the Hub

**2015**: Initial launch with 4,707 compounds at single dose
**Expansion**: Grew to 6,801 compounds with multi-dose formats through philanthropic support
**Current**: 5,506-compound screening library plus ~2,400 follow-up compounds

The expansion enabled:
- Significant data informatics buildout
- Increased compound stock for multiple replatings
- ML-enabled dataset creation through curated metadata
- Discovery of novel connections across diseases, cell lines, and compounds

## Applications

The Drug Repurposing Hub supports multiple research approaches:

### Target-Based Discovery
- Explore compounds with known activities against specific biological targets
- Understand pathways and biological mechanisms
- Validate new therapeutic targets

### Phenotypic Screening
- Screen compounds in disease-relevant cellular assays
- Identify new indications when disease mechanisms are poorly understood
- Discover unexpected biological activities

### Biological Insights
- Pair experimental screening results with curated metadata
- Generate ML-enabled datasets for computational analysis
- Uncover disease characteristics and mechanisms

## Data Availability and Licensing

- **Metadata Access**: Freely available for research use without registration
- **License**: Compound metadata available under CC-BY 4.0 license
- **Usage**: Generated for research purposes only
- **Restrictions**: Cannot be repackaged or redistributed for commercial purposes without permission
- **Clinical Use**: Not intended for clinical treatment or commercial marketing

**Note**: Downstream experimental data using the library may have different license terms.

## Collaboration Opportunities

The Broad Institute collaborates with many groups for screening:
- Academic institutions
- Research organizations
- Non-profit entities

The Center for the Development of Therapeutics (CDoT) offers:
- Decades of screening experience
- Cost-effective screening services
- Wide range of cellular assays
- Expert support for assay development and execution

Contact: repurposing@broadinstitute.org

## Compound Submission

Researchers can contribute to the collection by:
1. Reviewing the Compound Intake Policy
2. Submitting compounds through the online form
3. Working with the team to integrate valuable compounds

The original collection was made possible through philanthropic support, and the Hub continues to grow through community contributions.

## Quality Control

All small molecule compounds in the library are:
- Confirmed for >85% purity by UPLC-MS at time of addition
- Stored under appropriate conditions
- Tracked for stability and quality over time

## Citation

If you use the Drug Repurposing Hub in your research, please cite:

Corsello SM, Bittker JA, Liu Z, Gould J, McCarren P, Hirschman JE, Johnston SE, Vrcic A, Wong B, Khan M, Asiedu J, Narayan R, Mader CC, Subramanian A, Golub TR (2017). "The Drug Repurposing Hub: a next-generation drug library and information resource." Nature Medicine, 23:405–408.

## Team

The Drug Repurposing Hub is developed and maintained by:
- **Steven Corsello** - Founder of REPO Hub
- **Todd Golub** - Core Institute Member
- **Sandy Gould** - Senior Director, Head of Drug Discovery, CDoT
- And dedicated team members from CDoT

## Acknowledgements

Funding support from:
- Anonymous donor (primary support for collection subsidy)
- NIH LINCS Program (grant 3U54 HG006093)
- NIH BD2K Program (grant 5U01HG008699)
- NIH training grant T32 CA009172
- NIH/Harvard Catalyst training award KL2 TR001100
- Conquer Cancer Foundation of ASCO Young Investigator Award

Special thanks to curators of public drug databases, chemical vendors, and assay teams.

## Contact

For screening inquiries, compound submissions, or general information:
- Email: repurposing@broadinstitute.org
- Website: https://repo-hub.broadinstitute.org/repurposing

**Developed by**: Center for the Development of Therapeutics (CDoT)
**Institution**: Broad Institute of MIT and Harvard