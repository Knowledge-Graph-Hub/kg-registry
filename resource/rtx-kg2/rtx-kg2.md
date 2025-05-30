---
layout: resource_detail
activity_status: active
id: rtx-kg2
name: RTX-KG2
description: RTX-KG2 is a comprehensive biomedical knowledge graph that integrates information from over 80 structured knowledge sources into a semantically standardized model, supporting translational biomedicine and the ARAX biomedical reasoning system.
domains:
- health
- biomedical
- biological systems
- genomics
- pharmacology
contacts:
- category: Individual
  label: Stephen Ramsey
  orcid: 0000-0002-2168-5403
  contact_details:
  - contact_type: email
    value: ramseyst@oregonstate.edu
  - contact_type: github
    value: saramsey
homepage_url: https://github.com/RTXteam/RTX-KG2
repository: https://github.com/RTXteam/RTX-KG2
license:
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
  id: https://creativecommons.org/licenses/by/4.0/
products:
- id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  category: GraphProduct
  format: kgx-jsonl
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
  - rtx-kg2
  secondary_source:
  - rtx-kg2.code
- id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  category: GraphProduct
  format: kgx-jsonl
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
  - rtx-kg2
  secondary_source:
  - rtx-kg2.code
- id: rtx-kg2.code
  name: Code for building RTX-KG2
  description: Code for building RTX-KG2, in Python
  product_url: https://github.com/RTXteam/RTX-KG2
  category: ProcessProduct
  secondary_source:
  - rtx-kg2
- id: rtx-kg2.neo4j
  name: RTX-KG2 Neo4j
  description: Neo4j distribution of the RTX-KG2 as a graph database
  product_url: https://arax.ncats.io/
  category: ProgrammingInterface
  dump_format: neo4j
  original_source:
  - rtx-kg2
  secondary_source:
  - rtx-kg2.code
  is_neo4j: true
  is_public: false
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
  title: "RTX-KG2: a system for building a semantically standardized knowledge graph for translational biomedicine"
  year: '2022'
category: KnowledgeGraph
collection:
- translator
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
