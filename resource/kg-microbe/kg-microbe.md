---
activity_status: active
category: KnowledgeGraph
collection:
  - ber
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: MJoachimiak@lbl.gov
      - contact_type: github
        value: realmarcin
    label: Marcin P. Joachimiak
description: A Knowledge Graph about microbes. The KG is designed to integrate diverse knowledge about microbes from a variety of structured and unstructured sources.
domains:
  - microbiology
  - organisms
  - phenotype
  - biological systems
homepage_url: https://kghub.org/kg-microbe/index.html
id: kg-microbe
layout: resource_detail
license:
  id: https://opensource.org/license/bsd-3-clause
  label: BSD3
name: KG Microbe
products:
  - category: GraphProduct
    compression: targz
    description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
    format: kgx
    id: kg-microbe.graph.raw
    license:
      id: https://creativecommons.org/publicdomain/zero/1.0/
      label: CC0 1.0
    name: KG-Microbe KGX Graph - Raw
    original_source:
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: kg-microbe
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  - category: GraphProduct
    compression: targz
    description: The core KG KG-Microbe-Core with ontologies, organismal traits, and growth preferences.
    format: kgx
    id: kg-microbe.graph.core
    name: KG-Microbe KGX Graph - Core
    original_source:
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: kg-microbe
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  - category: GraphProduct
    compression: targz
    description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
    format: kgx
    id: kg-microbe.graph.biomedical
    name: KG-Microbe KGX Graph - Biomedical
    original_source:
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: kg-microbe
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  - category: GraphProduct
    compression: targz
    description: Core plus Uniprot genome annotations
    format: kgx
    id: kg-microbe.graph.function
    name: KG-Microbe KGX Graph - Function
    original_source:
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: kg-microbe
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  - category: GraphProduct
    compression: targz
    description: Biomedical plus Uniprot genome annotations
    format: kgx
    id: kg-microbe.graph.biomedical-function
    name: KG-Microbe KGX Graph - Biomedical-Function
    original_source:
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: kg-microbe
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 4640682152
    product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
  - category: GraphProduct
    compression: targz
    description: UniProt proteins from microbes, as graph nodes and edges
    format: kgx
    id: kg-microbe.graph.uniprot
    name: KG-Microbe UniProt microbe transform
    original_source:
      - source: kg-microbe
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
repository: https://github.com/Knowledge-Graph-Hub/kg-microbe
taxon:
  - NCBITaxon:2
  - NCBITaxon:2759
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-06-22T00:00:00Z'
---

KG-Microbe.

## Automated Evaluation

- View the automated evaluation: [kg-microbe automated evaluation](kg-microbe_eval_automated.html)
