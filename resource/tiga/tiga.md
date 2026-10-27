---
activity_status: active
category: DataSource
collection:
  - translator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://datascience.unm.edu/tiga/"
    label: Translational Informatics Division, Department of Internal Medicine, School of Medicine, University of New Mexico
creation_date: '2025-12-03T00:00:00Z'
description: The Target Illumination GWAS Analytics (TIGA) database is a manually curated resource containing genotype-phenotype associations pulled from numerous genome-wide association studies (GWAS). TIGA provides bibliometric assessment of scientific consensus based on iCite Relative Citation Ratio and meanRank scores for aggregate multivariate evidence, supporting target illumination and validation in translational research. TIGA is part of the NCATS Translator Knowledge Provider ecosystem.
domains:
  - genomics
  - biomedical
  - genome-wide association studies
homepage_url: https://datascience.unm.edu/tiga/
id: "tiga"
infores_id: "tiga"
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: Target Illumination GWAS Analytics
synonyms:
  - TIGA
products:
  - category: GraphicalInterface
    description: Web application for exploring TIGA evidence-ranked gene-trait associations.
    format: http
    id: tiga.portal
    name: TIGA Web Application
    original_source:
      - source: tiga
        relation_type: prov:hadPrimarySource
    product_url: https://datascience.unm.edu/tiga/
  - category: Product
    description: Download directory for TIGA data exports and releases.
    format: mixed
    id: tiga.downloads
    name: TIGA Downloads
    original_source:
      - source: tiga
        relation_type: prov:hadPrimarySource
    product_url: https://unmtid-dbs.net/download/TIGA/
  - category: GraphicalInterface
    description: Web interface for searching, browsing, and analyzing protein target
      information with advanced filtering, visualizations, and data export capabilities
      across the druggable genome
    format: http
    id: pharos.portal
    name: Pharos Web Portal
    original_source:
    - relation_type: prov:hadPrimarySource
      source: pharos
    - relation_type: prov:hadPrimarySource
      source: tcrd
    - relation_type: prov:hadPrimarySource
      source: uniprot
    - relation_type: prov:hadPrimarySource
      source: ncbigene
    - relation_type: prov:hadPrimarySource
      source: hgnc
    - relation_type: prov:hadPrimarySource
      source: ensembl
    - relation_type: prov:hadPrimarySource
      source: chembl
    - relation_type: prov:hadPrimarySource
      source: drugcentral
    - relation_type: prov:hadPrimarySource
      source: gtopdb
    - relation_type: prov:hadPrimarySource
      source: pubchem
    - relation_type: prov:hadPrimarySource
      source: disgenet
    - relation_type: prov:hadPrimarySource
      source: diseases
    - relation_type: prov:hadPrimarySource
      source: compartments
    - relation_type: prov:hadPrimarySource
      source: tissues
    - relation_type: prov:hadPrimarySource
      source: omim
    - relation_type: prov:hadPrimarySource
      source: clinvar
    - relation_type: prov:hadPrimarySource
      source: ctd
    - relation_type: prov:hadPrimarySource
      source: doid
    - relation_type: prov:hadPrimarySource
      source: eram
    - relation_type: prov:hadPrimarySource
      source: monarchinitiative
    - relation_type: prov:hadPrimarySource
      source: gwascatalog
    - relation_type: prov:hadPrimarySource
      source: tiga
    - relation_type: prov:hadPrimarySource
      source: gtex
    - relation_type: prov:hadPrimarySource
      source: hpa
    - relation_type: prov:hadPrimarySource
      source: human-proteome-map
    - relation_type: prov:hadPrimarySource
      source: expressionatlas
    - relation_type: prov:hadPrimarySource
      source: archs4
    - relation_type: prov:hadPrimarySource
      source: ccle
    - relation_type: prov:hadPrimarySource
      source: cspa
    - relation_type: prov:hadPrimarySource
      source: harmonizome
    - relation_type: prov:hadPrimarySource
      source: lincs-l1000
    - relation_type: prov:hadPrimarySource
      source: go
    - relation_type: prov:hadPrimarySource
      source: reactome
    - relation_type: prov:hadPrimarySource
      source: kegg
    - relation_type: prov:hadPrimarySource
      source: wikipathways
    - relation_type: prov:hadPrimarySource
      source: pathwaycommons
    - relation_type: prov:hadPrimarySource
      source: panther
    - relation_type: prov:hadPrimarySource
      source: string
    - relation_type: prov:hadPrimarySource
      source: bioplex
    - relation_type: prov:hadPrimarySource
      source: impc
    - relation_type: prov:hadPrimarySource
      source: mgi
    - relation_type: prov:hadPrimarySource
      source: rgd
    - relation_type: prov:hadPrimarySource
      source: homologene
    - relation_type: prov:hadPrimarySource
      source: hcop
    - relation_type: prov:hadPrimarySource
      source: pdb
    - relation_type: prov:hadPrimarySource
      source: glygen
    - relation_type: prov:hadPrimarySource
      source: darkkinasekb
    - relation_type: prov:hadPrimarySource
      source: pubmed
    - relation_type: prov:hadPrimarySource
      source: pubtator
    product_url: https://pharos.nih.gov/
  - category: Product
    description: Target Central Resource Database (TCRD) downloadable database files
      containing comprehensive protein target information including druggability classifications,
      expression data, disease associations, and chemical probe information
    format: http
    id: pharos.tcrd.download
    name: TCRD Database Downloads
    original_source:
    - relation_type: prov:hadPrimarySource
      source: pharos
    - relation_type: prov:hadPrimarySource
      source: tcrd
    - relation_type: prov:hadPrimarySource
      source: uniprot
    - relation_type: prov:hadPrimarySource
      source: ncbigene
    - relation_type: prov:hadPrimarySource
      source: hgnc
    - relation_type: prov:hadPrimarySource
      source: ensembl
    - relation_type: prov:hadPrimarySource
      source: chembl
    - relation_type: prov:hadPrimarySource
      source: drugcentral
    - relation_type: prov:hadPrimarySource
      source: gtopdb
    - relation_type: prov:hadPrimarySource
      source: pubchem
    - relation_type: prov:hadPrimarySource
      source: disgenet
    - relation_type: prov:hadPrimarySource
      source: diseases
    - relation_type: prov:hadPrimarySource
      source: compartments
    - relation_type: prov:hadPrimarySource
      source: tissues
    - relation_type: prov:hadPrimarySource
      source: omim
    - relation_type: prov:hadPrimarySource
      source: clinvar
    - relation_type: prov:hadPrimarySource
      source: ctd
    - relation_type: prov:hadPrimarySource
      source: doid
    - relation_type: prov:hadPrimarySource
      source: eram
    - relation_type: prov:hadPrimarySource
      source: monarchinitiative
    - relation_type: prov:hadPrimarySource
      source: gwascatalog
    - relation_type: prov:hadPrimarySource
      source: tiga
    - relation_type: prov:hadPrimarySource
      source: gtex
    - relation_type: prov:hadPrimarySource
      source: hpa
    - relation_type: prov:hadPrimarySource
      source: human-proteome-map
    - relation_type: prov:hadPrimarySource
      source: expressionatlas
    - relation_type: prov:hadPrimarySource
      source: archs4
    - relation_type: prov:hadPrimarySource
      source: ccle
    - relation_type: prov:hadPrimarySource
      source: cspa
    - relation_type: prov:hadPrimarySource
      source: harmonizome
    - relation_type: prov:hadPrimarySource
      source: lincs-l1000
    - relation_type: prov:hadPrimarySource
      source: go
    - relation_type: prov:hadPrimarySource
      source: reactome
    - relation_type: prov:hadPrimarySource
      source: kegg
    - relation_type: prov:hadPrimarySource
      source: wikipathways
    - relation_type: prov:hadPrimarySource
      source: pathwaycommons
    - relation_type: prov:hadPrimarySource
      source: panther
    - relation_type: prov:hadPrimarySource
      source: string
    - relation_type: prov:hadPrimarySource
      source: bioplex
    - relation_type: prov:hadPrimarySource
      source: impc
    - relation_type: prov:hadPrimarySource
      source: mgi
    - relation_type: prov:hadPrimarySource
      source: rgd
    - relation_type: prov:hadPrimarySource
      source: homologene
    - relation_type: prov:hadPrimarySource
      source: hcop
    - relation_type: prov:hadPrimarySource
      source: pdb
    - relation_type: prov:hadPrimarySource
      source: glygen
    - relation_type: prov:hadPrimarySource
      source: darkkinasekb
    - relation_type: prov:hadPrimarySource
      source: pubmed
    - relation_type: prov:hadPrimarySource
      source: pubtator
    product_url: https://opendata.ncats.nih.gov/public/pharos/
    warnings:
    - The Pharos footer still links the historical Juniper TCRD download host, but the
      about page points Pharos data downloads to NCATS OpenData; the registry uses the
      NCATS OpenData URL.
  - category: ProgrammingInterface
    connection_url: https://pharos-api.ncats.io/graphql
    description: GraphQL API for programmatic access to Pharos and TCRD data enabling
      custom queries and integrations. The pharos.nih.gov/graphql page is the in-browser
      explorer; queries are served by the pharos-api.ncats.io/graphql endpoint used
      by the Pharos frontend.
    format: graphql
    id: pharos.api
    name: Pharos GraphQL API
    original_source:
    - relation_type: prov:hadPrimarySource
      source: pharos
    - relation_type: prov:hadPrimarySource
      source: tcrd
    - relation_type: prov:hadPrimarySource
      source: uniprot
    - relation_type: prov:hadPrimarySource
      source: ncbigene
    - relation_type: prov:hadPrimarySource
      source: hgnc
    - relation_type: prov:hadPrimarySource
      source: ensembl
    - relation_type: prov:hadPrimarySource
      source: chembl
    - relation_type: prov:hadPrimarySource
      source: drugcentral
    - relation_type: prov:hadPrimarySource
      source: gtopdb
    - relation_type: prov:hadPrimarySource
      source: pubchem
    - relation_type: prov:hadPrimarySource
      source: disgenet
    - relation_type: prov:hadPrimarySource
      source: diseases
    - relation_type: prov:hadPrimarySource
      source: compartments
    - relation_type: prov:hadPrimarySource
      source: tissues
    - relation_type: prov:hadPrimarySource
      source: omim
    - relation_type: prov:hadPrimarySource
      source: clinvar
    - relation_type: prov:hadPrimarySource
      source: ctd
    - relation_type: prov:hadPrimarySource
      source: doid
    - relation_type: prov:hadPrimarySource
      source: eram
    - relation_type: prov:hadPrimarySource
      source: monarchinitiative
    - relation_type: prov:hadPrimarySource
      source: gwascatalog
    - relation_type: prov:hadPrimarySource
      source: tiga
    - relation_type: prov:hadPrimarySource
      source: gtex
    - relation_type: prov:hadPrimarySource
      source: hpa
    - relation_type: prov:hadPrimarySource
      source: human-proteome-map
    - relation_type: prov:hadPrimarySource
      source: expressionatlas
    - relation_type: prov:hadPrimarySource
      source: archs4
    - relation_type: prov:hadPrimarySource
      source: ccle
    - relation_type: prov:hadPrimarySource
      source: cspa
    - relation_type: prov:hadPrimarySource
      source: harmonizome
    - relation_type: prov:hadPrimarySource
      source: lincs-l1000
    - relation_type: prov:hadPrimarySource
      source: go
    - relation_type: prov:hadPrimarySource
      source: reactome
    - relation_type: prov:hadPrimarySource
      source: kegg
    - relation_type: prov:hadPrimarySource
      source: wikipathways
    - relation_type: prov:hadPrimarySource
      source: pathwaycommons
    - relation_type: prov:hadPrimarySource
      source: panther
    - relation_type: prov:hadPrimarySource
      source: string
    - relation_type: prov:hadPrimarySource
      source: bioplex
    - relation_type: prov:hadPrimarySource
      source: impc
    - relation_type: prov:hadPrimarySource
      source: mgi
    - relation_type: prov:hadPrimarySource
      source: rgd
    - relation_type: prov:hadPrimarySource
      source: homologene
    - relation_type: prov:hadPrimarySource
      source: hcop
    - relation_type: prov:hadPrimarySource
      source: pdb
    - relation_type: prov:hadPrimarySource
      source: glygen
    - relation_type: prov:hadPrimarySource
      source: darkkinasekb
    - relation_type: prov:hadPrimarySource
      source: pubmed
    - relation_type: prov:hadPrimarySource
      source: pubtator
    product_url: https://pharos.nih.gov/graphql
publications:
  - authors:
      - Yang JJ
      - Grissa D
      - Lambert CG
      - Bologa CG
      - Mathias SL
      - Waller A
      - Wild DJ
      - Jensen LJ
      - Oprea TI
    doi: 10.1093/bioinformatics/btab427
    id: https://www.ncbi.nlm.nih.gov/pubmed/34086846
    journal: Bioinformatics
    preferred: true
    title: "TIGA: target illumination GWAS analytics"
    year: '2021'
---

# Target Illumination GWAS Analytics

TIGA is a database of manually curated genotype-phenotype associations derived from numerous genome-wide association studies, with bibliometric consensus assessment to support translational research and drug target identification.
