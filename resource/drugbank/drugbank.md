---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@drugbank.com
  - contact_type: url
    value: https://www.drugbank.com/contact
  label: DrugBank
description: DrugBank Online is a comprehensive, publicly accessible database containing
  detailed information on drugs and drug targets, combining chemical, pharmacological,
  pharmaceutical data with drug target information including sequence, structure,
  and pathway details.
domains:
- health
- chemistry and biochemistry
- pharmacology
- genomics
- proteomics
homepage_url: https://www.drugbank.com/
id: drugbank
layout: resource_detail
license:
  id: https://go.drugbank.com/legal/terms_of_use
  label: Custom (free for academic research with license)
name: DrugBank
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching the DrugBank database
  format: http
  id: drugbank.web
  name: DrugBank Online
  original_source:
  - drugbank
  product_url: https://go.drugbank.com/
- category: DataModelProduct
  description: Academic access to DrugBank database dumps in XML and other formats
  format: xml
  id: drugbank.academic
  license:
    id: https://go.drugbank.com/legal/terms_of_use
    label: Academic License
  name: DrugBank Academic Downloads
  original_source:
  - drugbank
  product_url: https://go.drugbank.com/releases/latest
- category: ProgrammingInterface
  connection_url: https://www.drugbank.com/clinical
  description: Clinical API for integrating DrugBank data into healthcare applications
  id: drugbank.clinical.api
  is_public: true
  name: DrugBank Clinical API
  original_source:
  - drugbank
  product_url: https://www.drugbank.com/clinical
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
  - mesh
  - pid
  - do
  - diseases
  - drugcentral
  - go
  - gwas-catalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  secondary_source:
  - spoke
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
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2.code
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
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2.code
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
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2.code
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
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
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
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
publications:
- id: https://doi.org/10.1093/nar/gkad976
  journal: Nucleic Acids Research
  preferred: true
  title: DrugBank 6.0 - The DrugBank Knowledgebase for 2024
  year: '2024'
- id: https://doi.org/10.1093/nar/gkx1037
  journal: Nucleic Acids Research
  title: DrugBank 5.0 - A major update to the DrugBank database for 2018
  year: '2018'
repository: https://go.drugbank.com/releases/latest
tags:
- core
- biopragmatics
---
DrugBank is a comprehensive knowledge base combining detailed drug information (chemical, pharmacological, and pharmaceutical) with extensive drug target information (sequence, structure, and pathway). 

The database was started in 2006 in Dr. David Wishart's lab at the University of Alberta and is widely used by the pharmaceutical industry, medicinal chemists, pharmacists, physicians, researchers, and students.

## Content
As of version 5.1.13 (January 2025), DrugBank contains:
- 17,467 drug entries
- 2,992 approved small molecule drugs
- 1,729 approved biologics (proteins, peptides, vaccines, allergenics)
- 135 nutraceuticals
- 6,879+ experimental (discovery-phase) drugs
- 5,463 non-redundant protein sequences (drug targets, enzymes, transporters, carriers)
- 200+ data fields per entry

## Applications
DrugBank supports various research and clinical applications:
- Drug discovery and repurposing
- Precision medicine
- Pharmacovigilance
- In silico testing
- Clinical trial matching
- Electronic medical records
- Telehealth applications

## Access
DrugBank offers several access options:
- Free access to DrugBank Online for basic browsing and searching
- Free academic licenses for researchers meeting specific criteria
- Commercial licenses for industry users and developers
- Clinical API for healthcare software integration

All usage of DrugBank data requires proper citation in any resulting publications.