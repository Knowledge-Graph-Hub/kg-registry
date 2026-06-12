---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: patrick.aloy@irbbarcelona.org
    label: Patrick Aloy
    orcid: 0000-0002-3557-0236
  - category: Organization
    contact_details:
      - contact_type: url
        value: http://sbnb.irbbarcelona.org/
    label: Structural Bioinformatics and Network Biology Group, Institute for Research in Biomedicine (IRB Barcelona)
description: A knowledge graph of biological entities and their associations that integrates and formats biomedical data as pre-calculated knowledge graph embeddings
domains:
  - biomedical
homepage_url: https://bioteque.irbbarcelona.org/
id: bioteque
layout: resource_detail
name: Bioteque
products:
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - source: achilles
        relation_type: prov:hadPrimarySource
      - source: bioteque
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: ccle
        relation_type: prov:hadPrimarySource
      - source: cellosaurus
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: chemicalchecker
        relation_type: prov:hadPrimarySource
      - source: clue
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: creeds
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: depmap
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: dorothea
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: huri
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: offsides
        relation_type: prov:hadPrimarySource
      - source: omnipath
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: pharmacodb
        relation_type: prov:hadPrimarySource
      - source: prism
        relation_type: prov:hadPrimarySource
      - source: progeny
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: repodb
        relation_type: prov:hadPrimarySource
      - source: repohub
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  - category: ProcessProduct
    description: Scripts used to preprocess and accommodate biomedical datasets into the knowledge database behind the Bioteque repository
    id: bioteque.code
    license:
      id: https://opensource.org/licenses/MIT
      label: MIT License
    name: Bioteque code
    original_source:
      - source: bioteque
        relation_type: prov:hadPrimarySource
    product_url: https://gitlabsbnb.irbbarcelona.org/bioteque/bioteque
  - category: ProcessProduct
    description: BQsupports is a tool to uncover biomedical evidence behind experimental paired data.
    id: bioteque.bqsupports
    name: BQsupports
    original_source:
      - source: bioteque
        relation_type: prov:hadPrimarySource
    product_url: https://bioteque.irbbarcelona.org/bqsupports
publications:
  - id: doi:10.1038/s41467-022-33026-0
    doi: 10.1038/s41467-022-33026-0
    title: Integrating and formatting biomedical data as pre-calculated knowledge graph embeddings in the Bioteque
    authors:
      - Adrià Fernández-Torras
      - Miquel Duran-Frigola
      - Martino Bertoni
      - Martina Locatelli
      - Patrick Aloy
    journal: Nature Communications
    year: '2022'
repository: https://gitlabsbnb.irbbarcelona.org/bioteque/bioteque
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-06-12T00:00:00Z'
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

## Evaluation

- View the evaluation: [bioteque evaluation](bioteque_eval.html)
