---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nlm.nih.gov/
  id: ncbi
  label: US National Library of Medicine
creation_date: '2025-10-30T00:00:00Z'
description: Consumer health resource about genetic conditions from the US National
  Library of Medicine. This resource has been merged into MedlinePlus Genetics as
  of 2020.
domains:
- biomedical
- genomics
- rare disease
homepage_url: https://medlineplus.gov/genetics/
id: ghr
infores_id: ghr
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: Genetics Home Reference
products:
- category: GraphicalInterface
  description: MedlinePlus Genetics portal containing migrated Genetics Home Reference
    content.
  format: http
  id: ghr.portal
  name: MedlinePlus Genetics Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ghr
  product_url: https://medlineplus.gov/genetics/
- category: GraphicalInterface
  description: Browse page for genetic conditions from the MedlinePlus Genetics migration.
  format: http
  id: ghr.conditions
  name: MedlinePlus Genetics Conditions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ghr
  product_url: https://medlineplus.gov/genetics/condition/
- category: GraphicalInterface
  description: Browse page for gene summaries from the MedlinePlus Genetics migration.
  format: http
  id: ghr.gene-catalog
  name: MedlinePlus Genetics Gene Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ghr
  product_url: https://medlineplus.gov/genetics/gene/
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing definitions and descriptions
    with gzip compression
  format: txt
  id: medgen.mgdef
  name: MGDEF (Definitions)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: clinpgx
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: genereviews
  product_file_size: 5305829
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGDEF.RRF.gz
- category: Product
  description: CSV format data files directory with additional data exports
  format: csv
  id: medgen.csv
  name: CSV Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: clinpgx
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: sty
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/csv/
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dailymed
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: fideo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
synonyms:
- GHR
---
# Genetics Home Reference

## Overview

Genetics Home Reference (GHR) was a consumer health resource provided by the US National Library of Medicine (NLM) that offered information about genetic conditions and the genes or chromosomes related to those conditions. GHR provided health information in plain language to help patients, families, and healthcare providers understand how genetic variations affect health.

**Important:** As of 2020, Genetics Home Reference has been merged into **MedlinePlus Genetics** (https://medlineplus.gov/genetics/), which now serves as the primary NLM consumer genetics resource.

## Historical Content

### Genetic Conditions
GHR provided consumer-friendly information about more than 1,300 genetic conditions, including:
- Signs and symptoms
- Frequency in populations
- Genetic causes
- Inheritance patterns
- Treatment and management

### Genes and Chromosomes
The resource offered information about:
- More than 1,400 genes
- Gene function and location
- How gene changes relate to health conditions
- All 23 pairs of human chromosomes
- Mitochondrial DNA (mtDNA)

### Educational Content

#### Help Me Understand Genetics
A comprehensive educational section covering:
- DNA structure and function
- What genes are and how they work
- Genetic mutations and variants
- Inheritance patterns
- Genetic testing and counseling
- Precision medicine and genomic research

## Key Features

- **Plain Language**: Written for patients and families without requiring scientific expertise
- **Comprehensive Coverage**: Covered common and rare genetic conditions
- **Evidence-Based**: Information reviewed by genetics professionals
- **Cross-Referenced**: Links to genes, chromosomes, and related conditions
- **Educational**: Explained complex genetic concepts accessibly

## Transition to MedlinePlus Genetics

In 2020, NLM integrated Genetics Home Reference into MedlinePlus Genetics to:
- Consolidate consumer genetics information
- Improve user experience through single portal
- Enhance searchability and navigation
- Integrate with broader MedlinePlus health resources
- Maintain and expand genetics content

### Current Access

All former GHR content is now available at:
- **Website**: https://medlineplus.gov/genetics/
- **Genetic Conditions**: https://medlineplus.gov/genetics/condition/
- **Genes**: https://medlineplus.gov/genetics/gene/
- **Chromosomes**: https://medlineplus.gov/genetics/chromosome/
- **Understanding Genetics**: https://medlineplus.gov/genetics/understanding/

## Legacy Impact

GHR served for many years as a trusted resource for:
- Patients and families learning about genetic conditions
- Healthcare providers seeking patient education materials
- Students and educators in genetics education
- Researchers needing plain-language genetic information

## Information Resource ID

This resource has the Information Resource identifier: `infores:ghr`

## Recommended Alternative

Users seeking genetics consumer health information should visit **MedlinePlus Genetics** at https://medlineplus.gov/genetics/, which maintains and expands upon the content formerly available in Genetics Home Reference.