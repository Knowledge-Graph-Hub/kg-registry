---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: support@kidsfirstdrc.org
      - contact_type: url
        value: https://kidsfirstdrc.org/
    label: Kids First Data Resource Center
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://d3b.center/
    label: Children's Hospital of Philadelphia
description: The Gabriella Miller Kids First Pediatric Research Program Data Resource Center (Kids First DRC) provides researchers access to genomic and clinical data from pediatric cancer and structural birth defect cohorts to accelerate discovery and development of more effective treatments.
domains:
  - health
  - biomedical
  - genomics
  - clinical
homepage_url: https://kidsfirstdrc.org/
id: kidsfirst
layout: resource_detail
name: Kids First Data Resource Center
products:
  - category: GraphicalInterface
    description: Centralized platform providing access to harmonized clinical and genomic data from childhood cancer and congenital disorder cohorts, supporting cohort discovery and analysis.
    id: kidsfirst.portal
    name: Kids First Data Resource Portal
    product_url: https://portal.kidsfirstdrc.org/
    original_source:
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Cloud-based analysis platform for Kids First data, allowing researchers to analyze and integrate genomic and clinical data in a secure environment.
    id: kidsfirst.cavatica
    name: CAVATICA Platform
    product_url: https://cavatica.sbgenomics.com/
    original_source:
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Web-based tool for exploring and visualizing pediatric cancer genomic datasets, integrated with clinical data.
    id: kidsfirst.pedcbioportal
    name: PedcBioPortal
    product_url: https://pedcbioportal.kidsfirstdrc.org/
    original_source:
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
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
    id: ubkg.csv
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
repository: https://github.com/kids-first/
taxon:
  - NCBITaxon:9606
creation_date: '2025-06-04T00:00:00Z'
last_modified_date: '2025-12-13T00:00:00Z'
---

## Kids First Data Resource Center

The Gabriella Miller Kids First Pediatric Research Program Data Resource Center (Kids First DRC) is a collaborative pediatric research effort with the goal to understand the genetic causes and links between childhood cancer and structural birth defects. The Kids First DRC accelerates data-driven discoveries by providing researchers with access to one of the largest pediatric data collections available.

### Background

The Kids First DRC is funded by the NIH Common Fund as part of the Gabriella Miller Kids First Pediatric Research Program, named after 10-year-old Gabriella Miller who advocated for increased pediatric research funding before her death from cancer in 2013. The Gabriella Miller Kids First Research Act was signed into law in 2014, authorizing $12.6 million each year for 10 years to support pediatric research.

### Data Resources

Kids First DRC provides researchers with:

- Harmonized genomic and clinical data from multiple childhood cancer and structural birth defect cohorts
- Access to data from over 36,000 patient and family participants across 36 studies
- A variety of data modalities including:
  - Whole Genome Sequencing
  - RNA Sequencing
  - Whole Exome Sequencing
  - Linked-Read Whole Genome Sequencing
  - Long Reads Sequencing

All clinical data is standardized using ontologies such as the Human Phenotype Ontology (HPO) for phenotypes and MONDO Disease Ontology for diagnoses, enabling cross-condition analyses and discovery.

### Data Access

Access to Kids First data requires approved access through the NIH Database of Genotypes and Phenotypes (dbGaP). The data is not publicly downloadable but is accessible to qualified researchers who have obtained appropriate approvals. The Kids First Data Resource Portal allows researchers to explore and analyze data within a secure environment.

### Partner Institutions

The Kids First DRC comprises a collaborative network of leading institutions:

- Children's Hospital of Philadelphia
- University of North Carolina Health
- Velsera
- CHU Sainte-Justine University Hospital Centre
- The University of Chicago Center for Data Intensive Science
- Vanderbilt University Medical Center

Sequencing partners include Hudson Alpha, Broad Institute, Baylor College of Medicine Human Genome Sequencing Center, and Washington University in St. Louis.
