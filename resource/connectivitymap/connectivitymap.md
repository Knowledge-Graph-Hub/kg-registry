---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/connectivity-map-cmap
  label: Broad Institute of MIT and Harvard
creation_date: '2025-08-12T00:00:00Z'
description: The Connectivity Map (CMap) is a collection of genome-wide transcriptional
  expression data from cultured human cells treated with bioactive small molecules
  and simple pattern-matching algorithms that together enable the discovery of functional
  connections between drugs, genes, and diseases through common gene-expression changes.
  The original CMap resource is now integrated into the CLUE platform.
domains:
- drug discovery
- genomics
- biomedical
homepage_url: https://www.broadinstitute.org/connectivity-map-cmap
id: connectivitymap
last_modified_date: '2025-10-07T00:00:00Z'
layout: resource_detail
name: Connectivity Map
products:
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  product_url: https://zenodo.org/record/4077338
  secondary_source:
  - pharmkg
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
publications:
- id: https://doi.org/10.1126/science.1132939
  title: 'The Connectivity Map: Using Gene-Expression Signatures to Connect Small
    Molecules, Genes, and Disease'
repository: https://clue.io/about
---
# Connectivity Map

The Connectivity Map (CMap) is a pioneering resource that uses genome-wide transcriptional expression data to discover functional connections between drugs, genes, and diseases. Developed at the Broad Institute, CMap analyzes gene-expression signatures from cultured human cells treated with various bioactive small molecules to identify unexpected therapeutic relationships and mechanisms of action.

## Overview

The Connectivity Map project revolutionized drug discovery by enabling researchers to:
- Connect small molecules with similar mechanisms of action
- Identify potential therapeutic uses for existing drugs
- Discover molecular pathways affected by drugs
- Find compounds that mimic or reverse disease-related gene expression patterns

## Current Status

The original Connectivity Map resource has been superseded by and integrated into the [CLUE platform](https://clue.io/about), which provides expanded data and enhanced tools for exploring connections between genes, drugs, and diseases.

## Key Publication

Lamb J, Crawford ED, Peck D, et al. [The Connectivity Map: Using Gene-Expression Signatures to Connect Small Molecules, Genes, and Disease](https://doi.org/10.1126/science.1132939). Science. 2006;313(5795):1929-1935.