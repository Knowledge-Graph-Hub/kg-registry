---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: The encyclopedia of Rare disease Annotation for Precision Medicine (eRAM) is a standardized system providing computational annotations for rare diseases to support precision medicine. eRAM provides annotations for approximately 16,000 rare diseases, including detailed information on clinical phenotypes, symptoms, genes, and genotypes. The database contains over 6,100 human disease-related phenotype terms, 31,600 mammalian phenotype terms, 10,200 symptoms from UMLS, 18,800 genes and 92,500 genotypes. eRAM organizes diseases in a tree structure to systematically display relationships between diseases with similar pathogenesis, close anatomical sites, the same clinical symptoms or subtypes, facilitating both research into rare disease mechanisms and clinical diagnosis and treatment decisions.
domains:
  - clinical
  - biomedical
  - phenotype
  - precision medicine
  - rare disease
id: eram
infores_id: eram
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: http://119.3.41.228/eram/download.php
  label: Free of charge for non-profit (academic) institutions
name: 'eRAM: encyclopedia of rare disease annotations for precision medicine'
homepage_url: http://119.3.41.228/eram/
publications:
  - id: doi:10.1093/nar/gkx1062
    title: 'eRAM: encyclopedia of rare disease annotations for precision medicine'
    authors:
      - Jia J
      - An Z
      - Ming Y
      - Guo Y
      - Li W
      - Liang Y
      - Guo D
      - Li X
      - Tai J
      - Chen G
      - Jin Y
      - Liu Z
      - Ni X
      - Shi T
    journal: Nucleic Acids Research
    preferred: true
    year: '2018'
    doi: 10.1093/nar/gkx1062
products:
  - category: GraphicalInterface
    description: Web-based interface for browsing and querying rare disease annotations including phenotypes, symptoms, genes, and genotypes with tree-structured disease organization
    format: http
    id: eram.web
    name: eRAM Web Interface
    original_source:
      - source: eram
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: omim
        relation_type: prov:wasInformedBy
      - source: umls
        relation_type: prov:wasInformedBy
      - source: doid
        relation_type: prov:wasInformedBy
      - source: mesh
        relation_type: prov:wasInformedBy
      - source: orphanet
        relation_type: prov:wasInformedBy
      - source: hp
        relation_type: prov:wasInformedBy
      - source: mp
        relation_type: prov:wasInformedBy
    product_url: http://119.3.41.228/eram/
  - category: Product
    description: Downloadable data files containing rare disease annotations, phenotypes, symptoms, genes, and genotypes
    format: mixed
    id: eram.downloads
    name: eRAM Data Downloads
    original_source:
      - source: eram
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: umls
        relation_type: prov:wasDerivedFrom
      - source: doid
        relation_type: prov:wasDerivedFrom
      - source: mesh
        relation_type: prov:wasDerivedFrom
      - source: orphanet
        relation_type: prov:wasDerivedFrom
      - source: hp
        relation_type: prov:wasDerivedFrom
      - source: mp
        relation_type: prov:wasDerivedFrom
    product_url: http://119.3.41.228/eram/download.php
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
synonyms:
  - eRAM
taxon:
  - NCBITaxon:9606
  - NCBITaxon:40674
---

# eRAM: encyclopedia of rare disease annotations for precision medicine

The encyclopedia of Rare Disease Annotation for Precision Medicine (eRAM) provides computational annotations for rare diseases to support precision medicine applications. Developed to address the limited knowledge of rare diseases that forms a major obstacle to improving their treatment, eRAM focuses on detailed clinical phenotyping as a keystone for deciphering genes related to rare diseases and realizing precision medicine.

## Key Features

- **Comprehensive Coverage**: Annotations for approximately 16,000 rare diseases
- **Multi-source Phenotype Data**: 6,147 human disease-related phenotype terms, 31,661 mammalian phenotype terms, 10,202 symptoms from UMLS
- **Genetic Information**: 18,815 genes and 92,580 genotypes associated with rare diseases
- **Tree Structure Organization**: Systematic display of diseases and relationships between diseases with similar pathogenesis, close anatomical sites, or the same clinical symptoms
- **Clinical Support**: Provides clinical phenotypes with importance rankings and appropriate treatment strategies to facilitate timely diagnosis and treatment

## Data Sources

eRAM integrates information from multiple authoritative sources including the Human Disease Network, Online Mendelian Inheritance in Man (OMIM), the Unified Medical Language System (UMLS), the Disease Ontology, Medical Subject Headings (MeSH), and Orphanet.

## Information Resource ID

This resource has the Information Resource identifier: `infores:eram`
