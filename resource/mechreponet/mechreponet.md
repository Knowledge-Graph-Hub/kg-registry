---
activity_status: active
category: KnowledgeGraph
creation_date: '2022-04-12T00:00:00Z'
description: MechRepoNet (Mechanistic Repositioning Network) is a knowledge graph
  that integrates multiple biomedical data sources to support drug repositioning via
  mechanistic inference.
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
products:
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
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
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  secondary_source:
  - mechreponet
- description: Python code for building and analyzing the MechRepoNet knowledge graph
  id: mechreponet.code
  name: MechRepoNet Code
  product_url: https://github.com/SuLab/MechRepoNet
- category: GraphProduct
  description: Training data for the MIND knowledge graph containing 9,651,040 edges
  format: tsv
  id: mind.train
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Training Data
  original_source:
  - drugcentral
  - mechreponet
  product_url: https://zenodo.org/records/8117748/files/train.txt
  secondary_source:
  - mind
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-01: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-09-02: No Content-Length
    header found'
- category: GraphProduct
  description: Test data for the MIND knowledge graph containing DrugCentral indications
  format: tsv
  id: mind.test
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Test Data
  original_source:
  - drugcentral
  - mechreponet
  product_url: https://zenodo.org/records/8117748/files/test.txt
  secondary_source:
  - mind
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-01: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-09-02: No Content-Length
    header found'
- category: GraphProduct
  description: Validation data for the MIND knowledge graph containing DrugCentral
    indications
  format: tsv
  id: mind.valid
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Validation Data
  original_source:
  - drugcentral
  - mechreponet
  product_url: https://zenodo.org/records/8117748/files/valid.txt
  secondary_source:
  - mind
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-01: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2025-09-02: No Content-Length
    header found'
- category: Product
  description: Dictionary of entities in the MIND knowledge graph
  format: tsv
  id: mind.entities
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Entities Dictionary
  original_source:
  - drugcentral
  - mechreponet
  product_file_size: 5629618
  product_url: https://zenodo.org/records/8117748/files/entities.dict
  secondary_source:
  - mind
- category: Product
  description: Dictionary of relations in the MIND knowledge graph
  format: tsv
  id: mind.relations
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Relations Dictionary
  original_source:
  - drugcentral
  - mechreponet
  product_file_size: 1648
  product_url: https://zenodo.org/records/8117748/files/relations.dict
  secondary_source:
  - mind
publications:
- doi: 10.1093/bioinformatics/btac205
  id: doi:10.1093/bioinformatics/btac205
  title: Design and application of a knowledge network for automatic prioritization
    of drug mechanisms
repository: https://github.com/SuLab/MechRepoNet
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