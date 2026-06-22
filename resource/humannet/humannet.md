---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.inetbio.org/humannetv3/
  label: INetBio
creation_date: '2025-11-05T00:00:00Z'
description: HumanNet is a probabilistic functional gene network for Homo sapiens
  that integrates genomic and proteomic data from multiple sources to predict functional
  relationships between genes. The network uses a modified Bayesian integration approach
  to combine evidence from diverse data types including protein-protein interactions,
  gene co-expression, phylogenetic profiling, and literature mining. HumanNet provides
  confidence scores for gene-gene functional linkages and can be used for gene function
  prediction, disease gene prioritization, and pathway analysis.
domains:
- genomics
- systems biology
- biomedical
- biological systems
homepage_url: https://www.inetbio.org/humannetv3/
id: humannet
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: HumanNet
products:
- category: GraphicalInterface
  description: HumanNet v3 web interface for selecting PI, FN, or XC human gene networks
    and running disease gene or disease annotation prediction workflows.
  format: http
  id: humannet.web
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_url: https://www.inetbio.org/humannetv3/
- category: GraphProduct
  compression: gzip
  description: HumanNet-XC v3 functional gene network extended by co-citation, distributed
    with Entrez Gene identifiers.
  edge_count: 1125494
  format: tsv
  id: humannet.network
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Network File
  node_count: 18462
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_file_size: 12310221
  product_url: https://www.inetbio.org/humannetv3/networks/HumanNet-XC.tsv.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: metacyc
  - relation_type: prov:wasDerivedFrom
    source: reactome
- category: GraphProduct
  compression: gzip
  description: HumanNet-XC v3 functional gene network extended by co-citation, distributed
    with gene symbols.
  edge_count: 1125494
  format: tsv
  id: humannet.network.symbol
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Network File (Gene Symbols)
  node_count: 18462
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_file_size: 13925784
  product_url: https://www.inetbio.org/humannetv3/networks/HumanNet-XC.symbol.tsv.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: metacyc
  - relation_type: prov:wasDerivedFrom
    source: reactome
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  format: mixed
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: humannet
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharmkg
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://zenodo.org/record/4077338
publications:
- authors:
  - Chan Yeong Kim
  - Seungbyn Baek
  - Junha Cha
  - Sunmo Yang
  - Eiru Kim
  - Edward M Marcotte
  - Traver Hart
  - Insuk Lee
  doi: 10.1093/nar/gkab1048
  id: doi:10.1093/nar/gkab1048
  journal: Nucleic Acids Research
  preferred: true
  title: 'HumanNet v3: an improved database of human gene networks for disease research'
  year: '2022'
- authors:
  - Sohyun Hwang
  - Chan Yeong Kim
  - Sunmo Yang
  - Eiru Kim
  - Traver Hart
  - Edward M Marcotte
  - Insuk Lee
  doi: 10.1093/nar/gky1126
  id: doi:10.1093/nar/gky1126
  journal: Nucleic Acids Research
  title: 'HumanNet v2: human gene networks for disease research'
  year: '2019'
synonyms:
- HumanNet
- humannet
taxon:
- NCBITaxon:9606
---
# HumanNet

## Overview

HumanNet is a probabilistic functional gene network for Homo sapiens that integrates genomic and proteomic data from multiple sources to predict functional relationships between genes.

Using a modified Bayesian integration approach, HumanNet combines evidence from diverse data types including protein-protein interactions, gene co-expression patterns, phylogenetic profiling, and biomedical literature to construct a comprehensive functional network with confidence-weighted gene-gene linkages.

## Key Features

- **Comprehensive Coverage**: HumanNet-XC v3 covers 18,462 genes in the
  download table
- **Multi-Source Integration**: Combines protein interactions, co-expression, phylogeny, and literature
- **Confidence Scores**: Probabilistic scores for functional linkages
- **Multiple Network Tiers**: PI, FN, and XC networks for protein interaction,
  functional association, and co-citation-extended analyses
- **Web Tools**: Interactive visualization and analysis tools

## Research Applications

- Gene function prediction
- Disease gene prioritization
- Pathway analysis and enrichment
- Systems biology studies
- Network-based drug target discovery
- Functional module identification

## Products

### HumanNet Web Interface
Interactive platform for querying genes, visualizing network neighborhoods, and performing gene function predictions.

### HumanNet Network File
Downloadable network files containing gene-gene functional linkages with confidence scores in various formats.

## Publications

- [HumanNet v3: an improved database of human gene networks for disease research](https://doi.org/10.1093/nar/gkab1048) (2022)
- [HumanNet v2: human gene networks for disease research](https://doi.org/10.1093/nar/gky1126) (2019)

## Domains

- Genomics
- Systems Biology
- Biomedical
- Biological Systems

## Taxon Coverage

Human (NCBITaxon:9606)