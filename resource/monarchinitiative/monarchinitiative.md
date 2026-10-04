---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@monarchinitiative.org
  id: monarchinitiative
  label: Monarch Initiative
creation_date: '2025-10-30T00:00:00Z'
description: The Monarch Initiative is an international consortium that integrates,
  aligns, and redistributes cross-species gene, genotype, variant, disease, and phenotype
  data to improve understanding of genetic disease and support translational research.
domains:
- genomics
- organisms
- model organisms
homepage_url: https://monarchinitiative.org/
id: monarchinitiative
infores_id: monarchinitiative
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: Monarch Initiative
products:
- category: GraphProduct
  description: Monarch Knowledge Graph integrating phenotype, disease, gene data across
    species
  format: mixed
  id: monarchinitiative.kg
  name: Monarch Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  product_url: https://monarchinitiative.org/
- category: ProgrammingInterface
  description: Monarch API for programmatic access to integrated data
  format: http
  id: monarchinitiative.api
  name: Monarch API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  product_url: https://api.monarchinitiative.org/api/
- category: GraphicalInterface
  description: Web interface for browsing genes, diseases, phenotypes across species
  format: http
  id: monarchinitiative.portal
  name: Monarch Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  product_url: https://monarchinitiative.org/
- category: GraphProduct
  compression: targz
  description: KGX Distribution of KG-Alzheimers
  format: kgx
  id: kg-alzheimers.graph
  name: KGX Distribution of KG-Alzheimers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-alzheimers
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_file_size: 210868256
  product_url: https://kg-hub.berkeleybop.io/kg-alzheimers/current/kg-alzheimers.tar.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-07-01; no live download
    location was found (GitHub releases, kghub.io/current, and Zenodo all return 404
    or have no published artifact).
- category: GraphProduct
  description: Robokop KG (Automat)
  format: kgx-jsonl
  id: automat.robokopkg
  name: robokopkg
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: robokop
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugmechdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/RobokopKG/4901b2bc764444ea/
- category: GraphProduct
  description: 'Biolink Automat: graph based on the Monarch API, from the SRI Reference
    KG (2021 data, Biolink 3.1.2; legacy).'
  format: kgx-jsonl
  id: automat.biolink
  name: biolink_automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: sri-reference-kg
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  product_url: https://stars.renci.org/var/plater/bl-3.1.2/Biolink_Automat/329f8c92051c18d4/
- category: ProgrammingInterface
  description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
    querying the BioThings and other APIs registered to the team in SmartAPI.
  format: http
  id: service-kp.trapi
  is_public: true
  name: Service Provider TRAPI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: litvar
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: ddinter
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gtrx
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
publications:
- authors:
  - Christopher J. Mungall
  - Julie A. McMurry
  - Sebastian Köhler
  - James P. Balhoff
  - Charles Borromeo
  - Matthew Brush
  - Seth Carbon
  - Tom Conlin
  - Nathan Dunn
  - Mark Engelstad
  - Erin Foster
  - J.P. Gourdine
  - Julius O.B. Jacobsen
  - Dan Keith
  - Bryan Laraway
  - Suzanna E. Lewis
  - Jeremy NguyenXuan
  - Kent Shefchek
  - Nicole Vasilevsky
  - Zhou Yuan
  - Nicole Washington
  - Harry Hochheiser
  - Tudor Groza
  - Damian Smedley
  - Peter N. Robinson
  - Melissa A. Haendel
  doi: 10.1093/nar/gkw1128
  id: https://doi.org/10.1093/nar/gkw1128
  journal: Nucleic Acids Research
  title: 'The Monarch Initiative: an integrative data and analytic platform connecting
    phenotypes to genotypes across species'
  year: '2017'
repository: https://github.com/monarch-initiative
synonyms:
- Monarch
- The Monarch Initiative
---
# Monarch Initiative

## Overview

The Monarch Initiative is an international consortium dedicated to improving the understanding of genetic disease through the integration, alignment, and redistribution of cross-species data. The platform connects phenotypes to genotypes across species, enabling researchers to leverage comparative genomics for translational medicine and rare disease research.

## Key Features

- **Cross-Species Integration**: Connects human disease with model organism data
- **Knowledge Graph**: Comprehensive graph integrating genes, diseases, phenotypes, variants
- **Ontologies**: Uses and develops standardized ontologies (Mondo, HPO, Uberon, Phenio)
- **Open Data**: All data freely available with CC-BY licenses
- **Tools Ecosystem**: Suite of interoperable tools for data integration and analysis
- **API Access**: Programmatic access to all integrated data

## Core Components

### Ontologies
- **Mondo Disease Ontology**: Harmonized disease definitions across resources
- **Human Phenotype Ontology (HPO)**: Standardized phenotypic features
- **Uberon**: Multi-species anatomy ontology
- **Phenio**: Cross-species phenotype ontology
- **Gene Ontology (GO)**: Gene function annotations

### Tools & Infrastructure
- **Exomiser**: Variant prioritization tool
- **LinkML**: Data modeling framework
- **SSSOM**: Simple Standard for Sharing Ontology Mappings
- **OAK (Ontology Access Kit)**: Toolkit for ontology access and processing
- **Biolink Model**: Data model for biomedical knowledge graphs

### Data Integration
- Integrates data from multiple sources:
  - Human genetics databases (OMIM, ClinVar)
  - Model organism databases (MGI, ZFIN, FlyBase, WormBase)
  - Phenotype databases
  - Gene-disease associations
  - Variant annotations

## Applications

- **Rare Disease Diagnosis**: Phenotype-driven differential diagnosis
- **Variant Prioritization**: Identifying pathogenic variants in genomic data
- **Model Organism Research**: Finding relevant animal models for human disease
- **Drug Repurposing**: Identifying therapeutic candidates based on phenotype similarity
- **Translational Research**: Bridging basic research with clinical applications
- **Phenotype Analysis**: Cross-species phenotype comparison

## Technical Infrastructure

### Knowledge Graph
- Neo4j graph database for complex queries
- SPARQL endpoint for semantic web queries
- Regular data releases with versioning
- Extensive cross-references and mappings

### APIs and Access
- RESTful API for programmatic access
- Python and R client libraries
- Bulk downloads available
- GraphQL interface in development

## Development & Governance

### Organization
- International collaborative consortium
- Partner institutions across North America, Europe, and beyond
- Open development via GitHub
- Community-driven governance

### Funding
- NIH National Center for Advancing Translational Sciences (NCATS)
- NIH National Human Genome Research Institute (NHGRI)
- NIH Office of the Director (OD)
- Additional support from multiple agencies and institutions

## Citation

McMurry et al. The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species. Nucleic Acids Research (2017) 45 (D1): D712-D722.

## Information Resource ID

This resource has the Information Resource identifier: `infores:monarchinitiative`