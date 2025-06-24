---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: daniel.himmelstein@gmail.com
  - contact_type: github
    value: dhimmel
  label: Daniel Himmelstein
description: Hetionet is an integrative network of biomedical knowledge assembled
  from 29 different databases of genes, compounds, diseases, and more. It combines
  over 50 years of biomedical information into a single resource.
domains:
- biomedical
- drug discovery
- genomics
- health
- biological systems
homepage_url: https://het.io/
id: hetionet
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Hetionet
products:
- category: GraphicalInterface
  description: Browser for complete Hetionet v1.0 graph database in Neo4j
  format: http
  id: hetionet.neo4j
  name: Hetionet v1.0 Neo4j Database
  product_url: https://neo4j.het.io/browser/
- category: GraphProduct
  description: Hetionet v1.0 in JSON format
  format: json
  id: hetionet.data.json
  name: Hetionet v1.0 JSON
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/json/hetionet-v1.0.json.bz2
- category: GraphProduct
  description: Hetionet v1.0 as a Neo4j database
  id: hetionet.data.neo4j
  name: Hetionet v1.0 Neo4j
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/neo4j/hetionet-v1.0.db.tar.bz2
- category: GraphProduct
  description: Hetionet v1.0 as SIF edges
  format: sif
  id: hetionet.data.edges
  name: Hetionet v1.0 edges (SIF)
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-edges.sif.gz
- category: GraphProduct
  description: Hetionet v1.0 as TSV nodes
  format: tsv
  id: hetionet.data.nodes
  name: Hetionet v1.0 nodes (TSV)
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-nodes.tsv
- category: ProcessProduct
  description: Python package for creating, querying, and operating on hetnets (heterogeneous
    networks)
  id: hetnetpy
  name: hetnetpy
  product_url: https://github.com/hetio/hetnetpy
- category: GraphicalInterface
  description: Web application to search and explore connectivity between nodes in
    Hetionet
  format: http
  id: hetionet.search
  name: Hetnet Connectivity Search
  product_url: https://het.io/search
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
publications:
- authors:
  - Daniel S Himmelstein
  - Michael Zietz
  - Vincent Rubinetti
  - Kyle Kloster
  - Benjamin J Heil
  - Faisal Alquaddoomi
  - Dongbo Hu
  - David N Nicholson
  - Yun Hao
  - Blair D Sullivan
  - Michael W Nagle
  - Casey S Greene
  doi: doi:10.1093/gigascience/giad047
  id: https://doi.org/10.1093/gigascience/giad047
  journal: GigaScience
  title: Hetnet connectivity search provides rapid insights into how biomedical entities
    are related
  year: '2023'
repository: https://github.com/hetio/hetionet
---
# Hetionet

Hetionet is a heterogeneous information network (hetnet) of biomedical knowledge. It integrates data from 29 public databases into a single network, containing 47,031 nodes of 11 types and 2,250,197 edges of 24 types. The network unifies information on genes, compounds, diseases, anatomy, biological processes, molecular functions, cellular components, pathways, pharmacologic classes, side effects, and symptoms.

Hetionet was originally developed as part of Project Rephetio, a study that utilized hetnets to predict new uses for existing drugs. The network has since been used for a variety of biomedical research purposes, including prioritizing disease-associated genes and providing insights into biological relationships.

The network is maintained by Daniel Himmelstein and collaborators in the Greene Lab at the University of Pennsylvania and the Baranzini Lab at the University of California, San Francisco. All data and software associated with Hetionet are open-source and freely available.