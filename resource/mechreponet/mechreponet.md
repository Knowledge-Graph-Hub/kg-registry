---
activity_status: active
category: KnowledgeGraph
creation_date: '2022-04-12T00:00:00Z'
description: MechRepoNet (Mechanistic Repositioning Network) is a knowledge graph that integrates multiple biomedical data sources to support drug repositioning via mechanistic inference.
domains:
- biomedical
- drug discovery
- pharmacology
- translational
homepage_url: https://github.com/SuLab/MechRepoNet
id: mechreponet
last_modified_date: '2025-07-17T00:00:00Z'
layout: resource_detail
name: MechRepoNet
repository: https://github.com/SuLab/MechRepoNet
publications:
- id: doi:10.1093/bioinformatics/btac205
  doi: 10.1093/bioinformatics/btac205
  title: Design and application of a knowledge network for automatic prioritization of drug mechanisms
products:
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  original_source:
  - ctd
  - do
  - go
  - chebi
  - reactome
  - interpro
  - hp
  - cl
  - pr
  - uberon
  - ncbitaxon
  - hetionet
  - complexportal
  - rnacentral
  - mirtarbase
  - unii
  - biolink
  secondary_source:
  - mechreponet
- description: Python code for building and analyzing the MechRepoNet knowledge graph
  id: mechreponet.code
  name: MechRepoNet Code
  product_url: https://github.com/SuLab/MechRepoNet
---

# MechRepoNet

MechRepoNet (Mechanistic Repositioning Network) is a knowledge graph created for the purpose of drug repositioning via mechanistic inference. It integrates multiple biomedical data sources to provide a comprehensive network of compounds, diseases, genes, pathways, and other biological entities.

## Description

MechRepoNet was developed by researchers at the Su Lab to enable mechanism-based drug repositioning. The knowledge graph integrates data from various sources including:

- Comparative Toxicogenomics Database (CTD)
- Disease Ontology (DOID)
- Gene Ontology (GO)
- Chemical Entities of Biological Interest (ChEBI)
- Reactome
- InterPro
- Human Phenotype Ontology (HPO)
- Cell Ontology (CL)
- UBERON
- NCBI Taxonomy

The graph contains relationships between compounds, genes, diseases, pathways, GO terms, and other biological entities, allowing for mechanistic inference for drug repositioning.

## References

The MechRepoNet knowledge graph is fully described in:

Mayers, M., Tu, R. (2022). MechRepoNet, a network-based tool for mechanism-based repositioning of small molecules. *Bioinformatics*, 38(15), 3746-3748. [https://doi.org/10.1093/bioinformatics/btac431](https://doi.org/10.1093/bioinformatics/btac431)
