---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  label: Roger Tu
  orcid: 0000-0002-7899-1604
- category: Individual
  label: Meghamala Sinha
  orcid: 0000-0002-6422-3313
- category: Individual
  label: Andrew I. Su
  orcid: 0000-0002-9859-4104
description: 'Mechanistic Repositioning Network with Indications (MIND) is a knowledge
  graph incorporating two biomedical resources: MechRepoNet and DrugCentral. MechRepoNet
  is a knowledge graph comprising of 18 biomedical resources that reflects and expands
  on important drug mechanism relationships identified from a curated biomedical drug
  mechanism dataset. MIND was created by mapping DrugCentral edges to existing MechRepoNet
  nodes through the Unified Medical Language System (UMLS) and Medical Subject Headings
  (MeSH). The MIND training set has a total of 9,651,040 edges.'
domains:
- drug discovery
- biomedical
homepage_url: https://zenodo.org/records/8117748
id: mind
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: MIND
products:
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
  - File was not able to be retrieved when checked on 2025-12-17_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-17_ HTTP 429 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-17: No Content-Length
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
  - File was not able to be retrieved when checked on 2025-12-17_ HTTP 429 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-15_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-12-17: No Content-Length
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
  - File was not able to be retrieved when checked on 2025-12-17_ HTTP 429 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-15_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-10-30_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2025-12-17: No Content-Length
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
- authors:
  - Roger Tu
  - Meghamala Sinha
  - Carolina González
  - Eric Hu
  - Shehzaad Dhuliawala
  - Andrew McCallum
  - Andrew I. Su
  id: https://doi.org/10.1101/2023.05.12.540594
  journal: bioRxiv
  title: Drug Repurposing using consilience of Knowledge Graph Completion methods
  year: '2023'
repository: https://github.com/SuLab/KnowledgeGraphEmbedding
---
MIND (Mechanistic Repositioning Network with Indications) is a knowledge graph that combines MechRepoNet, a graph comprising 18 biomedical resources, with DrugCentral indications data. MechRepoNet contains 9,652,116 edges and 250,035 nodes covering drug mechanisms, while DrugCentral contributes 5,379 indication edges representing relationships between 1,308 unique compounds and 1,030 unique diseases. The resulting MIND knowledge graph contains 9,651,040 edges in its training set and is designed to support drug repositioning research through knowledge graph embeddings.