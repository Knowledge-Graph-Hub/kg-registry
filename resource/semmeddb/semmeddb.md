---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@nlm.nih.gov
  id: ncbi
  label: National Library of Medicine
creation_date: '2025-05-30T00:00:00Z'
description: SemMedDB is a repository of semantic predications (subject-predicate-object
  triples) extracted from biomedical literature by SemRep, a natural language processing
  system. It contains over 130 million semantic predications extracted from more than
  37 million PubMed citations, supporting biomedical knowledge discovery, literature-based
  discovery, and clinical applications.
domains:
- biomedical
- literature
- clinical
- drug discovery
- genomics
- pharmacology
homepage_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemMedDB_download.html
id: semmeddb
infores_id: semmeddb
last_modified_date: '2026-01-23T00:00:00Z'
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/web_policies.html
  label: UMLS License
name: Semantic MEDLINE Database (SemMedDB)
products:
- category: ProcessProduct
  description: The SemRep natural language processing system that extracts semantic
    predications from biomedical literature to create SemMedDB
  id: semmeddb.semrep.tool
  name: SemRep NLP System
  original_source:
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  product_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemRep_download.html
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_file_size: 376501785
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  format: http
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_url: https://arax.ncats.io/
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epigraphdb
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: vectology
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  - relation_type: prov:hadPrimarySource
    source: eqtlgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: cpic
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for SemMedDB distributed via the NCATS Translator
    release site (release 2026_03_27; build semmeddb_semmeddb-2023-kg2.10.3_fe8e6340_2025sep1_4.3.6;
    source version semmeddb-2023-kg2.10.3; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 1412108
  format: kgx-jsonl
  id: translator.semmeddb.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator SemMedDB KGX Graph
  node_count: 69187
  original_source:
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/semmeddb/latest/
  versions:
  - '2026_03_27'
  - semmeddb_semmeddb-2023-kg2.10.3_fe8e6340_2025sep1_4.3.6
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
publications:
- authors:
  - Kilicoglu H
  - Shin D
  - Fiszman M
  - Rosemblat G
  - Rindflesch TC
  doi: 10.1093/bioinformatics/bts591
  id: https://doi.org/10.1093/bioinformatics/bts591
  journal: Bioinformatics
  preferred: true
  title: 'SemMedDB: a PubMed-scale repository of biomedical semantic predications'
  year: '2012'
- authors:
  - Kilicoglu H
  - Rosemblat G
  - Fiszman M
  - Shin D
  - Rindflesch TC
  doi: 10.1186/s12859-020-3517-7
  id: https://doi.org/10.1186/s12859-020-3517-7
  journal: BMC Bioinformatics
  title: Broad-coverage biomedical relation extraction with SemRep
  year: '2020'
- authors:
  - Kilicoglu H
  - Rosemblat G
  - Fiszman M
  - Rindflesch TC
  doi: 10.1186/1471-2105-12-486
  id: https://doi.org/10.1186/1471-2105-12-486
  journal: BMC Bioinformatics
  title: Constructing a semantic predication gold standard from the biomedical literature
  year: '2011'
- authors:
  - Rindflesch TC
  - Fiszman M
  doi: 10.1016/j.jbi.2003.11.003
  id: https://doi.org/10.1016/j.jbi.2003.11.003
  journal: Journal of Biomedical Informatics
  title: 'The interaction of domain knowledge and linguistic structure in natural
    language processing: interpreting hypernymic propositions in biomedical text'
  year: '2003'
taxon:
- NCBITaxon:9606
---
## Overview

The Semantic MEDLINE Database (SemMedDB) is a large-scale repository of semantic predications (subject-predicate-object triples) extracted from the biomedical literature by the SemRep natural language processing system. It provides a structured representation of biomedical knowledge contained in PubMed citations, where concepts are normalized to the Unified Medical Language System (UMLS) Metathesaurus, and their relationships are based on the UMLS Semantic Network.

SemMedDB version 43 (VER43_R) is the final update to the database (as of May 2024), containing data extracted from MEDLINE BASELINE 2022 with PubMed update files through May 8, 2024. The resource is being deprecated and will no longer be maintained as of December 31, 2024, though an archived version will remain available through the Internet Archive.

## Features

- Contains over 130 million semantic predications extracted from more than 37 million PubMed citations
- Uses UMLS Metathesaurus concepts as predication arguments (subjects and objects)
- Includes a wide range of semantic relationship types defined in the UMLS Semantic Network
- Supports various types of biomedical relationships including clinical medicine, molecular interactions, disease etiology, pharmacogenomics, and anatomical relationships
- Database schema includes tables for citations, sentences, entities, predications, and metadata

## Database Schema

SemMedDB has the following main tables:

1. **CITATIONS**: Contains metadata for each PubMed citation including PMID, publication date, and journal information
2. **SENTENCE**: Contains information about individual sentences from PubMed citations
3. **ENTITY**: Contains entity information with UMLS concept identifiers, names, and semantic types
4. **PREDICATION**: Contains semantic predications with subject-predicate-object triples and associated metadata
5. **PREDICATION_AUX**: Contains auxiliary information for predications with mention-level details
6. **GENERIC_CONCEPT**: Contains generic concepts as indicated by SemRep

## Applications

SemMedDB has been used for numerous biomedical knowledge discovery applications including:

- Clinical decision making and medical diagnosis
- Drug repurposing
- Literature-based discovery and hypothesis generation
- Adverse drug reaction identification
- Drug-drug interaction discovery
- Gene regulatory network inference
- Biomedical question answering
- Semantic relatedness assessment

## Availability

SemMedDB is available for download from the National Library of Medicine. A UMLS Terminology Services (UTS) account is required to access the downloads. SemMedDB version 43 (VER43_R) is the final update to the database (as of May 2024).

## SemRep System

SemRep is the underlying natural language processing system that extracts semantic predications for SemMedDB. It combines syntactic and semantic principles with structured biomedical domain knowledge contained in the Unified Medical Language System (UMLS) to extract semantic relations from biomedical text. SemRep has been developed at the U.S. National Library of Medicine.

## Note

These tools will no longer be maintained as of December 31, 2024. Archived webpage can be found at the [Internet Archive](https://wayback.archive-it.org/7867/20240404194159/https://lhncbc.nlm.nih.gov/ii/). The Indexing Initiative Github repository is under development. Contact NLM Customer Service if you have questions.