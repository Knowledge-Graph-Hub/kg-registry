---
activity_status: active
category: DataSource
description: The Metabolomics Workbench is a public repository for metabolomics data and metadata, serving as the National Metabolomics Data Repository (NMDR). It provides tools, protocols, training, and access to over 2,000 metabolomics studies containing data from more than 75,000 samples and 32,000 known metabolites. Funded by the NIH Common Fund from 2012-2022.
domains: []
id: "mw"
layout: resource_detail
name: Metabolomics Workbench
synonyms:
  - MW
  - NMDR
  - National Metabolomics Data Repository
homepage_url: https://www.metabolomicsworkbench.org/
last_modified_date: '2025-11-26T00:00:00Z'
contacts:
  - category: Person
    label: Oliver Fiehn
    contact_details:
      - contact_type: email
        value: "fiehn@ucdavis.edu"
  - category: Person
    label: Shankar Subramaniam
    contact_details:
      - contact_type: email
        value: "shankar@sdsc.edu"
publications:
  - id: "https://doi.org/10.1038/s41592-019-0694-2"
    title: "The Metabolomics program"
    journal: Nature Methods
    year: "2020"
products:
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: "ubkg.neo4j"
    name: UBKG Neo4j Docker Distribution
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: "ubkg.csv"
    name: UBKG Ontology CSV Files
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
warnings:
  - This is an automatically generated stub page. Please replace with accurate information about this resource.
creation_date: '2025-06-04T00:00:00Z'
---

# Mw

This is an automatically generated stub page for mw. Please update with proper information.
