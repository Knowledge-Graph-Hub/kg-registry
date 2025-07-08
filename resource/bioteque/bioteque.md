---
layout: resource_detail
activity_status: active
id: bioteque
name: Bioteque
description: A knowledge graph of biological entities and their associations that integrates and formats biomedical data as pre-calculated knowledge graph embeddings
domains:
- health
contacts:
- category: Individual
  label: Patrick Aloy
  orcid: 0000-0002-3557-0236
  contact_details:
  - contact_type: email
    value: patrick.aloy@irbbarcelona.org
- category: Organization
  label: Structural Bioinformatics and Network Biology Group, Institute for Research in Biomedicine (IRB Barcelona)
  contact_details:
  - contact_type: url
    value: http://sbnb.irbbarcelona.org/
homepage_url: https://bioteque.irbbarcelona.org/
repository: https://gitlabsbnb.irbbarcelona.org/bioteque/bioteque
products:
- id: bioteque.embeddings
  name: Bioteque Embeddings
  description: Network embeddings of the Bioteque graph that represent biological entities and their associations
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  category: Product
  secondary_source:
  - bioteque
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmdb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
- id: bioteque.code
  name: Bioteque code
  description: Scripts used to preprocess and accommodate biomedical datasets into the knowledge database behind the Bioteque repository
  product_url: https://gitlabsbnb.irbbarcelona.org/bioteque/bioteque
  category: ProcessProduct
  license:
    label: MIT License
    id: https://opensource.org/licenses/MIT
  secondary_source:
  - bioteque
  original_source:
  - bioteque
- id: bioteque.bqsupports
  name: BQsupports
  description: BQsupports is a tool to uncover biomedical evidence behind experimental paired data.
  product_url: https://bioteque.irbbarcelona.org/bqsupports
  category: ProcessProduct
  secondary_source:
  - bioteque
  original_source:
  - bioteque
publications:
- authors:
  - "Fern\xE1ndez-Torras A"
  - Duran-Frigola M
  - Bertoni M
  - Locatelli M
  - Aloy P
  doi: doi:10.1038/s41467-022-33026-0
  id: doi:10.1038/s41467-022-33026-0
  title: Integrating and formatting biomedical data as pre-calculated knowledge graph embeddings in the Bioteque
  year: '2022'
category: KnowledgeGraph
---

## Bioteque Knowledge Graph

Bioteque is a knowledge graph that integrates multiple biomedical data sources into a comprehensive resource for biomedical research. It combines various types of biomedical data, including:

- Chemical and pharmaceutical data
- Gene and protein information
- Disease and phenotype data
- Cell line information
- Tissue-specific data
- Pathway information
- Molecular interactions

The knowledge graph is structured around biological entities and their associations, with nodes representing entities (compounds, genes, diseases, etc.) and edges representing relationships between them. These relationships include regulatory interactions, physical interactions, genetic interactions, and other biological associations.

### Embeddings

A key feature of Bioteque is the provision of pre-calculated knowledge graph embeddings. These embeddings represent the biological entities and their associations in a continuous vector space, allowing for computational analyses such as:

- Similarity searches between biological entities
- Prediction of novel associations
- Drug repurposing
- Multi-omics data integration

The embeddings are available for download and can be used for various computational biology applications without the need to process the raw data or construct the knowledge graph from scratch.

### Data Sources

Bioteque integrates data from over 35 different biomedical resources, including:

- Chemical databases (ChEBI, PubChem, DrugBank)
- Genomic resources (CCLE, COSMIC, Depmap)
- Protein interaction databases (STRING, IntAct, HuRI)
- Pathway resources (Reactome, PROGENy)
- Regulatory information (DoRothEA)
- Disease associations (DisGeNET, Open Targets)
- Tissue-specific data (GTEx, Human Protein Atlas)

This integration provides a unified view of biomedical knowledge that can be accessed through the Bioteque portal or used programmatically through the available embeddings.
