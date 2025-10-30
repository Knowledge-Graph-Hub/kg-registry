---
activity_status: active
category: KnowledgeGraph
collection:
  - translator
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: ramseyst@oregonstate.edu
      - contact_type: github
        value: saramsey
    label: Stephen Ramsey
    orcid: 0000-0002-2168-5403
description: RTX-KG2 is a comprehensive biomedical knowledge graph that integrates information from over 80 structured knowledge sources into a semantically standardized model, supporting translational biomedicine and the ARAX biomedical reasoning system.
domains:
  - health
  - biomedical
  - biological systems
  - genomics
  - pharmacology
homepage_url: https://github.com/RTXteam/RTX-KG2
id: rtx-kg2
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: RTX-KG2
products:
  - category: GraphProduct
    description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
    format: kgx-jsonl
    id: rtx-kg2.graph.nodes
    name: RTX-KG2.10.1c KGX JSONL Nodes
    original_source:
      - chembl
      - drugbank
      - kegg
      - reactome
      - go
      - drugcentral
      - uniprot
      - mondo
      - hp
      - chebi
      - uberon
      - ncbitaxon
      - dgidb
      - disgenet
      - ensembl
      - gtopdb
      - rtx-kg2
      - semmeddb
    product_file_size: 376501785
    product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
    secondary_source:
      - rtx-kg2
  - category: GraphProduct
    description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
    format: kgx-jsonl
    id: rtx-kg2.graph.edges
    name: RTX-KG2.10.1c KGX JSONL Edges
    original_source:
      - chembl
      - drugbank
      - kegg
      - reactome
      - go
      - drugcentral
      - uniprot
      - mondo
      - hp
      - chebi
      - uberon
      - ncbitaxon
      - dgidb
      - disgenet
      - ensembl
      - gtopdb
      - rtx-kg2
      - semmeddb
    product_file_size: 1807360397
    product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
    secondary_source:
      - rtx-kg2
  - category: ProcessProduct
    description: Code for building RTX-KG2, in Python
    id: rtx-kg2.code
    name: Code for building RTX-KG2
    product_url: https://github.com/RTXteam/RTX-KG2
    secondary_source:
      - rtx-kg2
  - category: ProgrammingInterface
    description: Neo4j distribution of the RTX-KG2 as a graph database
    dump_format: neo4j
    id: rtx-kg2.neo4j
    is_neo4j: true
    is_public: false
    name: RTX-KG2 Neo4j
    original_source:
      - chembl
      - drugbank
      - kegg
      - reactome
      - go
      - drugcentral
      - uniprot
      - mondo
      - hp
      - chebi
      - uberon
      - ncbitaxon
      - dgidb
      - disgenet
      - ensembl
      - gtopdb
      - rtx-kg2
      - semmeddb
    product_url: https://arax.ncats.io/
    secondary_source:
      - rtx-kg2
publications:
  - authors:
      - Wood EC
      - Glen AK
      - Kvarfordt LG
      - Colby LA
      - Unni DR
      - Himmelstein DS
      - Lee AY
      - Ramsey SA
    doi: doi:10.1186/s12859-022-04932-3
    id: https://doi.org/10.1186/s12859-022-04932-3
    journal: BMC Bioinformatics
    preferred: true
    title: 'RTX-KG2: a system for building a semantically standardized knowledge graph for translational biomedicine'
    year: '2022'
repository: https://github.com/RTXteam/RTX-KG2
infores_id: rtx-kg2
---

## RTX-KG2: A Semantically Standardized Knowledge Graph for Translational Biomedicine

RTX-KG2 is the second-generation knowledge graph for the [ARAX](https://github.com/RTXteam/RTX) biomedical reasoning system, developed by the Reasoning Tool X (RTX) team. It integrates information from over 80 biomedical knowledge sources, including ontologies, drug databases, gene-disease associations, protein interactions, and more.

### Key Features

- **Comprehensive Integration**: Combines data from diverse sources including ChEMBL, DrugBank, DisGeNET, UMLS, Gene Ontology, and many others
- **Semantic Standardization**: All entities and relationships are mapped to the [Biolink Model](https://biolink.github.io/biolink-model/) framework
- **Rich Connectivity**: Contains millions of nodes and edges representing biomedical entities and their relationships
- **Multiple Formats**: Available in JSON, KGX format, and as a Neo4j graph database
- **Supporting Translational Medicine**: Designed to enable advanced reasoning across complex biomedical knowledge

### Knowledge Sources

RTX-KG2 integrates data from numerous biomedical knowledge sources, including but not limited to:

#### Data Sources
- ChEMBL: A manually curated database of bioactive molecules with drug-like properties
- DrugBank: A comprehensive database containing detailed drug and drug target information
- KEGG: The Kyoto Encyclopedia of Genes and Genomes
- Reactome: A curated pathway database
- DisGeNET: A database of gene-disease associations
- SemMedDB: A repository of semantic predications extracted from biomedical literature
- UMLS: The Unified Medical Language System
- UniProtKB: Universal Protein Resource Knowledgebase
- HMDB: Human Metabolome Database
- IntAct: Molecular interaction database
- NCBIGene: NCBI's gene database
- SMPDB: Small Molecule Pathway Database

#### Ontologies
- Gene Ontology (GO): Comprehensive compendium of gene and gene product attributes
- MONDO: Monarch Disease Ontology
- Human Phenotype Ontology (HP): Standardized vocabulary of phenotypic abnormalities
- ChEBI: Chemical Entities of Biological Interest
- UBERON: Integrated cross-species anatomy ontology
- NCBITaxon: NCBI Taxonomy
- Disease Ontology (DO): Standardized ontology for human disease

### Applications

RTX-KG2 serves as the foundation for biomedical reasoning systems, drug repurposing research, and knowledge discovery in the NCATS Biomedical Data Translator project. The knowledge graph enables complex question answering about drugs, diseases, genes, and their relationships.

## Evaluation

- View the evaluation: [rtx-kg2 evaluation](rtx-kg2_eval.html)
