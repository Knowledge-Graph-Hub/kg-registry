---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://cancer.sanger.ac.uk/cosmic/about
    label: COSMIC Team (Wellcome Sanger Institute)
description: COSMIC (Catalogue Of Somatic Mutations In Cancer) is a comprehensive resource for somatic mutations in human cancer. It curates, standardizes, and integrates mutation data across genes, cancer types, and samples, and provides access via a web portal and licensed downloads.
domains:
  - genomics
  - biomedical
homepage_url: https://cancer.sanger.ac.uk/cosmic
id: cosmic
last_modified_date: '2025-09-09T00:00:00Z'
layout: resource_detail
license:
  id: https://cancer.sanger.ac.uk/cosmic/license
  label: COSMIC License
name: COSMIC
products:
  - category: GraphicalInterface
    description: Web portal for exploring somatic mutations, gene pages, cancer types, and curated annotations
    format: http
    id: cosmic.portal
    name: COSMIC Portal
    original_source:
      - cosmic
    product_url: https://cancer.sanger.ac.uk/cosmic
  - category: Product
    description: Top-level downloads page with links to COSMIC release files (registration/license required)
    format: http
    id: cosmic.downloads
    name: COSMIC Downloads
    original_source:
      - cosmic
    product_url: https://cancer.sanger.ac.uk/cosmic/download/cosmic
  - category: DocumentationProduct
    description: COSMIC Knowledgebase overview and documentation pages
    format: http
    id: cosmic.kb.overview
    name: COSMIC-KB Portal overview
    original_source:
      - cosmic
    product_url: https://www.cosmickb.org/about/
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - chebi
      - cosmic
      - achilles
      - depmap
      - ccle
      - gdsc
      - cellosaurus
      - clue
      - ctd
      - pharmacodb
      - prism
      - drugbank
      - lincs
      - compartments
      - offsides
      - sider
      - drugcentral
      - repohub
      - chemicalchecker
      - repodb
      - disgenet
      - opentargets
      - creeds
      - interpro
      - reactome
      - tissues
      - dorothea
      - progeny
      - gtex
      - hpa
      - go
      - corum
      - huri
      - intact
      - omnipath
      - string
      - bto
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - bioteque
  - category: GraphProduct
    description: RNA-KG as a Neo4j Dump
    format: neo4j
    id: rna-kg.kg.neo4j
    name: RNA-KG Neo4j Dump
    original_source:
      - dbsnp
      - cosmic
      - rnacentral
      - ensembl
      - circbase
      - chebi
      - pr
      - ncbigene
      - cl
      - go
      - mondo
      - hp
      - uberon
      - vo
      - pw
      - reactome
      - wikipathways
    product_file_size: 3976840239
    product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
    secondary_source:
      - rna-kg
  - category: GraphProduct
    description: RNA-KG Nodes in CSV format
    format: csv
    id: rna-kg.kg.nodes
    name: RNA-KG Nodes
    original_source:
      - dbsnp
      - cosmic
      - rnacentral
      - ensembl
      - circbase
      - chebi
      - pr
      - ncbigene
      - cl
      - go
      - mondo
      - hp
      - uberon
      - vo
      - pw
      - reactome
      - wikipathways
    product_file_size: 4424633304
    product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
    secondary_source:
      - rna-kg
  - category: GraphProduct
    description: RNA-KG Edges in CSV format
    format: csv
    id: rna-kg.kg.edges
    name: RNA-KG Edges
    original_source:
      - dbsnp
      - cosmic
      - rnacentral
      - ensembl
      - circbase
      - chebi
      - pr
      - ncbigene
      - cl
      - go
      - mondo
      - hp
      - uberon
      - vo
      - pw
      - reactome
      - wikipathways
    product_file_size: 18370248815
    product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
    secondary_source:
      - rna-kg
warnings:
  - COSMIC data downloads for commercial users are provided by Qiagen.
infores_id: cosmic
---

# COSMIC

## Overview

COSMIC (Catalogue Of Somatic Mutations In Cancer) curates and integrates somatic mutation data across genes, cancer types, and samples. It provides searchable web pages and licensed bulk downloads for research and clinical interpretation.

## Access

- Portal: browse COSMIC at the main site
- Downloads: bulk release files (requires registration and acceptance of the COSMIC License)
- Login: register and authenticate to access downloads
- COSMIC‑KB: knowledge base overview and related content

## Citation & Licensing

Use of COSMIC data requires adherence to the COSMIC License. Please cite COSMIC according to guidance on the site.
