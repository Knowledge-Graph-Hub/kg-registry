---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: MontageBai
    label: Xuefeng Bai
creation_date: '2026-06-02T00:00:00Z'
description: KG-FM is a Neo4j knowledge graph for framework materials, including metal-organic frameworks, covalent-organic frameworks, and hydrogen-bonded organic frameworks. It was constructed with large language model extraction over more than 100,000 Web of Science articles and covers synthesis, properties, applications, publications, and other framework-material relationships.
domains:
  - chemistry and biochemistry
  - information technology
  - other
homepage_url: https://github.com/MontageBai/KGFM
id: kg-fm
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: KG-FM
products:
  - category: GraphProduct
    description: Neo4j framework-materials knowledge graph constructed from Web of Science abstracts and publication metadata with LLM-assisted information extraction. The paper reports 2.53 million nodes and 4.01 million relationships covering materials, properties, structures, applications, and related literature.
    edge_count: 4010000
    id: kg-fm.graph
    name: KG-FM Neo4j Knowledge Graph
    node_count: 2530000
    original_source:
      - source: kg-fm
        relation_type: prov:hadPrimarySource
      - source: web-of-science
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/MontageBai/KGFM
    warnings:
      - No standalone Neo4j database dump, public graph endpoint, or versioned graph release was identified in the GitHub repository when curated on 2026-06-02; the repository provides source text, JSON extraction files, and Python scripts for constructing and using the graph.
  - category: ProcessProduct
    description: Python scripts for splitting abstract text, converting LLM-extracted JSON records into Neo4j Cypher imports, loading title metadata, and integrating KG-FM with LLM-based question answering.
    format: http
    id: kg-fm.workflow
    name: KG-FM Construction and QA Code
    original_source:
      - source: kg-fm
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/MontageBai/KGFM
    repository: https://github.com/MontageBai/KGFM
    warnings:
      - The GitHub repository did not expose a machine-readable license record and no explicit license file was identified when curated on 2026-06-02.
  - category: Product
    compression: zip
    description: Zipped abstract-text corpora for COF, HOF, and MOF literature used as input to KG-FM extraction and graph construction.
    id: kg-fm.abstract_text
    name: KG-FM Abstract Text Files
    original_source:
      - source: kg-fm
        relation_type: prov:hadPrimarySource
      - source: web-of-science
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/MontageBai/KGFM/tree/main/Abstract%20Text
  - category: Product
    compression: zip
    description: Zipped JSON extraction files for COF, HOF, and MOF literature, produced from framework-material abstracts and used to import KG-FM nodes and relationships.
    id: kg-fm.json_extractions
    name: KG-FM JSON Extraction Files
    original_source:
      - source: kg-fm
        relation_type: prov:hadPrimarySource
      - source: web-of-science
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/MontageBai/KGFM/tree/main/Json%20File
  - category: Product
    description: CSV file containing framework-material questions and reference answers used to evaluate KG-enhanced LLM question answering.
    format: csv
    id: kg-fm.question_answer
    name: KG-FM Question and Answer Benchmark
    original_source:
      - source: kg-fm
        relation_type: prov:hadPrimarySource
    product_file_size: 22859
    product_url: https://raw.githubusercontent.com/MontageBai/KGFM/main/Question%20and%20Answer.csv
  - category: Product
    compression: zip
    description: Zipped answer-reference material for the KG-FM question-answering benchmark.
    id: kg-fm.answer_references
    name: KG-FM Answer References
    original_source:
      - source: kg-fm
        relation_type: prov:hadPrimarySource
    product_file_size: 118366
    product_url: https://raw.githubusercontent.com/MontageBai/KGFM/main/Answer%20Reference.zip
  - category: DocumentationProduct
    description: Demonstration video for the KG-FM project.
    id: kg-fm.demonstration_video
    name: KG-FM Demonstration Video
    original_source:
      - source: kg-fm
        relation_type: prov:hadPrimarySource
    product_file_size: 4578745
    product_url: https://raw.githubusercontent.com/MontageBai/KGFM/main/demonstration%20video.mp4
publications:
  - authors:
      - Xuefeng Bai
      - Song He
      - Yi Li
      - Yabo Xie
      - Xin Zhang
      - Wenli Du
      - Jian-Rong Li
    doi: 10.1038/s41524-025-01540-6
    id: doi:10.1038/s41524-025-01540-6
    journal: npj Computational Materials
    preferred: true
    title: Construction of a knowledge graph for framework material enabled by large language models and its application
    year: '2025'
repository: https://github.com/MontageBai/KGFM
synonyms:
  - KGFM
  - KG-FM
  - Framework Materials Knowledge Graph
warnings:
  - The GitHub repository did not expose a machine-readable license record and no explicit license file was identified when curated on 2026-06-02.
---

# KG-FM

KG-FM is a knowledge graph for framework materials, including MOFs, COFs, and HOFs. The graph was built from Web of Science literature records using large language model extraction and loaded into Neo4j for Cypher querying, visualization, data mining, and KG-enhanced question answering.

The public repository provides the construction scripts, abstract text archives, JSON extraction outputs, benchmark question-answer files, answer references, and a demonstration video. A standalone graph dump or hosted graph endpoint was not identified at curation time.
