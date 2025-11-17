---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: Gene-List Network Enrichment Analysis (GeLiNEA) is a computational tool that evaluates the significance of connections between a gene list (e.g., from screening experiments) and curated gene sets (e.g., MSigDB) within protein-protein association networks (e.g., STRING). It uses a null model of degree-preserving random gene lists to assess statistical significance of network connections, supporting pathway enrichment analysis and functional interpretation of experimental gene lists.
domains:
  - genomics
  - systems biology
  - biomedical
id: gelinea
infores_id: gelinea
last_modified_date: '2025-11-17T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: GeLiNEA
homepage_url: https://github.com/broadinstitute/GeLiNEA
products:
  - category: Product
    description: Command-line tool for performing gene-list network enrichment analysis using degree-preserving random gene list null models
    format: python
    id: gelinea.tool
    name: GeLiNEA Tool
    original_source:
      - gelinea
    product_url: https://github.com/broadinstitute/GeLiNEA
publications:
  - authors:
      - Yilong Zou
      - Whitney S Henry
      - Emily L Ricq
      - Emily T Graham
      - Vasant V Phadnis
      - Peter Maretich
      - Sanchari Paradkar
      - Natalie Boehnke
      - Amy A Deik
      - Frederik Reinhardt
      - Jennifer K Eaton
      - Brittany Ferguson
      - Wan Wang
      - Jocelyn Fairman
      - Hillary R Keys
      - Vlado Dančík
      - Clary B Clish
      - Paul A Clemons
      - Paula T Hammond
      - Laurie A Boyer
      - Robert A Weinberg
      - Stuart L Schreiber
    doi: 10.1038/s41586-020-2732-8
    id: "PMID:32939090"
    journal: Nature
    title: Plasticity of ether lipids promotes ferroptosis susceptibility and evasion
    year: "2020"
repository: https://github.com/broadinstitute/GeLiNEA
synonyms:
  - GeLiNEA
  - Gene-List Network Enrichment Analysis
---

# GeLiNEA

## Overview

Gene-List Network Enrichment Analysis (GeLiNEA) is a computational tool developed at the Broad Institute for evaluating the significance of connections between gene lists and curated gene sets within protein-protein association networks. It provides a rigorous statistical framework for functional interpretation of experimental gene lists.

## Key Features

- **Network-Based Enrichment**: Evaluates gene list enrichment in the context of protein-protein interaction networks
- **Statistical Rigor**: Uses degree-preserving random gene list null models to assess significance
- **Flexible Input**: Accepts gene lists from screening experiments and curated gene sets from resources like MSigDB
- **Network Agnostic**: Compatible with any protein-protein association network (e.g., STRING)
- **Multiple Testing Correction**: Provides p-values for statistical significance assessment

## Methodology

GeLiNEA takes three inputs:
1. **Gene List**: From experimental sources such as CRISPR screens or expression studies
2. **Gene Sets**: Curated collections (e.g., pathways, biological processes from MSigDB)
3. **Network**: Protein-protein association network (e.g., STRING database)

The tool evaluates the significance of connections between the gene list and each gene set in the network using a null model of degree-preserving random gene lists, which accounts for network topology biases.

## Input File Formats

- **Network file**: Tab-separated text file with header row, node IDs in first two columns
- **Gene-sets file**: GMT file format (Gene Matrix Transposed), IDs must match network file
- **Gene-list file**: Text file with header row containing one node ID per row

## Output

Results are provided in a tab-separated text file with columns:
- **geneSet**: Name of the gene set
- **overlap**: Number of genes common to the gene list and gene set
- **nConnections**: Number of connections between the gene list and gene set in the network
- **pValue**: Statistical significance of connections under the null model

## Running GeLiNEA

GeLiNEA is implemented in Scala and uses sbt (Scala Build Tool):

```
sbt> run -n <network_file> -s <gene_sets_file> -l <gene_list_file> -o <results_file> -b <bin_size>
```

Recommended bin size: 50

## Use Cases

- Pathway enrichment analysis for CRISPR screening hits
- Functional interpretation of differential gene expression results
- Network-based analysis of disease gene associations
- Systems biology investigations of gene function

## Citation

Zou Y, Henry WS, Ricq EL, Graham ET, Phadnis VV, Maretich P, Paradkar S, Boehnke N, Deik AA, Reinhardt F, Eaton JK, Ferguson B, Wang W, Fairman J, Keys HR, Dančík V, Clish CB, Clemons PA, Hammond PT, Boyer LA, Weinberg RA, Schreiber SL. "Plasticity of ether lipids promotes ferroptosis susceptibility and evasion." *Nature*. 2020 Sep;585(7826):603-608. PMID: 32939090

## Source Code

- **Repository**: https://github.com/broadinstitute/GeLiNEA
- **License**: MIT License
- **Language**: Scala
