---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@nlm.nih.gov
  label: National Library of Medicine
description: SemMedDB is a repository of semantic predications (subject-predicate-object
  triples) extracted from biomedical literature by SemRep, a natural language processing
  system. It contains over 130 million semantic predications extracted from more than
  37 million PubMed citations, supporting biomedical knowledge discovery, literature-based
  discovery, and clinical applications.
domains:
- biomedical
- literature
- health
- clinical
- drug discovery
- genomics
- pharmacology
homepage_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemMedDB_download.html
id: semmeddb
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/web_policies.html
  label: UMLS License
name: Semantic MEDLINE Database (SemMedDB)
products:
- category: Product
  description: MySQL database containing over 130 million semantic predications extracted
    from more than 37 million PubMed citations (processed using MEDLINE BASELINE 2022
    + PubMed Update Files through May 8, 2024)
  id: semmeddb.mysql
  name: SemMedDB MySQL Database
  product_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemMedDB_MySQL_database.html
  warnings:
  - File was not able to be retrieved when checked on 2025-09-05_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-09-09: HTTP 403 error
    when accessing file'
- category: Product
  description: CSV file containing citation information for all PubMed articles in
    SemMedDB
  format: csv
  id: semmeddb.citations.csv
  name: SemMedDB Citations CSV
  product_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemMedDB_tables/CITATIONS.csv
  warnings:
  - File was not able to be retrieved when checked on 2025-09-05_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-09-09: HTTP 403 error
    when accessing file'
- category: Product
  description: CSV file containing entity information with UMLS concept identifiers,
    names, and semantic types
  format: csv
  id: semmeddb.entity.csv
  name: SemMedDB Entity CSV
  product_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemMedDB_tables/ENTITY.csv
  warnings:
  - File was not able to be retrieved when checked on 2025-09-05_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-09-09: HTTP 403 error
    when accessing file'
- category: Product
  description: CSV file containing semantic predications with subject-predicate-object
    triples and associated metadata
  format: csv
  id: semmeddb.predication.csv
  name: SemMedDB Predication CSV
  product_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemMedDB_tables/PREDICATION.csv
  warnings:
  - File was not able to be retrieved when checked on 2025-09-05_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-09-09: HTTP 403 error
    when accessing file'
- category: Product
  description: CSV file containing sentence information from PubMed citations
  format: csv
  id: semmeddb.sentence.csv
  name: SemMedDB Sentence CSV
  product_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemMedDB_tables/SENTENCE.csv
  warnings:
  - File was not able to be retrieved when checked on 2025-09-05_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-09-09: HTTP 403 error
    when accessing file'
- category: ProcessProduct
  description: The SemRep natural language processing system that extracts semantic
    predications from biomedical literature to create SemMedDB
  id: semmeddb.semrep.tool
  name: SemRep NLP System
  product_url: https://lhncbc.nlm.nih.gov/temp/SemRep_SemMedDB_SKR/SemRep_download.html
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
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - epigraphdb
  - kg-monarch
  - vectology
  - ukbiobank
  - prsatlas
  - eqtlgen
  - mondo
  - gtex
  - ensembl
  - cpic
  - opentargets
  - efo
  - semmeddb
  - intact
  - string
  - reactome
  - mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
  secondary_source:
  - epigraphdb
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