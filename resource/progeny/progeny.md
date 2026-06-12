---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://saezlab.org/
      - contact_type: email
        value: contact@saezlab.org
    id: saezlab
    label: Saez-Rodriguez Lab
creation_date: '2025-11-17T00:00:00Z'
description: PROGENy (Pathway RespOnsive GENes for activity inference) is a resource that leverages a large compendium of publicly available signaling perturbation experiments to yield a common core of pathway responsive genes for human and mouse. These pathway signatures, coupled with statistical methods, can be used to infer pathway activities from bulk or single-cell transcriptomics data. PROGENy is available as an R package on Bioconductor and supports analysis of both human and mouse data across 14 signaling pathways.
domains:
  - genomics
  - systems biology
  - biomedical
  - pathways
homepage_url: https://saezlab.github.io/progeny/
id: progeny
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: PROGENy
products:
  - category: ProgrammingInterface
    description: R package containing pathway signatures for 14 signaling pathways in human and mouse, available through Bioconductor
    format: mixed
    id: progeny.rpackage
    is_public: true
    name: PROGENy R Package
    original_source:
      - relation_type: prov:hadPrimarySource
        source: progeny
    product_url: https://www.bioconductor.org/packages/release/bioc/html/progeny.html
  - category: DocumentationProduct
    description: Documentation website for PROGENy with installation instructions, vignettes, and function reference
    format: http
    id: progeny.docs
    is_public: true
    name: PROGENy Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: progeny
    product_url: https://saezlab.github.io/progeny/
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
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
publications:
  - authors:
      - Michael Schubert
      - Bertram Klinger
      - "Martina Klünemann"
      - Anja Sieber
      - Florian Uhlitz
      - Sascha Sauer
      - Mathew J Garnett
      - "Nils Blüthgen"
      - Julio Saez-Rodriguez
    doi: 10.1038/s41467-017-02391-6
    id: PMID:29295995
    journal: Nature Communications
    title: Perturbation-response genes reveal signaling footprints in cancer gene expression
    year: '2018'
  - id: doi:10.1186/s13059-020-1949-z
    doi: 10.1186/s13059-020-1949-z
    title: Robustness and applicability of transcription factor and pathway analysis tools on single-cell RNA-seq data
    authors:
      - Christian H. Holland
      - Jovan Tanevski
      - Javier Perales-Patón
      - Jan Gleixner
      - Manu P. Kumar
      - Elisabetta Mereu
      - Brian A. Joughin
      - Oliver Stegle
      - Douglas A. Lauffenburger
      - Holger Heyn
      - Bence Szalai
      - Julio Saez-Rodriguez
    journal: Genome Biology
    year: '2020'
repository: https://github.com/saezlab/progeny
synonyms:
  - PROGENy
  - Pathway RespOnsive GENes
taxon:
  - NCBITaxon:9606
  - NCBITaxon:10090
warnings: []
---

# Progeny
