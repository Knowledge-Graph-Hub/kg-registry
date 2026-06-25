---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: EPA's Distributed Structure-Searchable Toxicity (DSSTox) database provides
  high-quality chemical and chemistry data underpinning several publicly available
  computational toxicology applications. DSSTox contains curated chemical substances
  mapped to chemical identifiers including CAS Registry Numbers, IUPAC names, SMILES,
  and InChIKeys. The database currently exceeds 1.2 million substances which includes
  chemical lists of interest to EPA, other federal agencies, states, tribes, industry
  and stakeholder groups. DSSTox provides accurate linkages of chemical structures
  to source substance identifiers, allowing high-quality association of chemicals
  to existing toxicity data, bioactivity data, experimental chemical property data
  and enabling structure-based predictive modeling. The database supports the CompTox
  Chemicals Dashboard, EcoTox Knowledgebase, Chemical Exposure Knowledgebase, and
  other EPA tools.
domains:
- toxicology
- chemistry and biochemistry
- environment
homepage_url: https://www.epa.gov/comptox-tools/distributed-structure-searchable-toxicity-dsstox-database
id: dsstoxdb
infores_id: dsstoxdb
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0
name: Distributed Structure-Searchable Toxicity (DSSTox) Database
products:
- category: GraphicalInterface
  description: Web-based interface for searching over 1.2 million chemicals with integrated
    toxicity, bioactivity, and exposure data
  format: http
  id: dsstoxdb.dashboard
  name: CompTox Chemicals Dashboard
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  product_url: https://comptox.epa.gov/dashboard/
- category: MappingProduct
  description: Downloadable Excel and CSV files containing DSSTox identifiers mapped
    to CAS numbers, InChIKeys, SMILES, molecular formulas, and other chemical identifiers
    for over 1.2 million substances
  format: mixed
  id: dsstoxdb.downloads
  latest_version: 10.23645/epacomptox.5588566.v8
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0
  name: DSSTox Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  product_url: https://epa.figshare.com/articles/dataset/Chemistry_Dashboard_Data_DSSTox_Identifiers_Mapped_to_CAS_Numbers_and_Names/5588566
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: epa-srs
  - relation_type: prov:wasInformedBy
    source: chemid
  - relation_type: prov:wasInformedBy
    source: pubchem
- category: ProgrammingInterface
  description: Public CTX API documentation for programmatic access to DSSTox chemical
    data and computational toxicology information; individual API keys are required
  format: http
  id: dsstoxdb.api
  name: EPA CompTox API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  product_url: https://www.epa.gov/comptox-tools/computational-toxicology-and-exposure-apis
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
publications:
- authors:
  - Grulke CM
  - Williams AJ
  - Thillanadarajah I
  - Richard AM
  doi: 10.1016/j.comtox.2019.100096
  id: https://pubmed.ncbi.nlm.nih.gov/33426407
  journal: Comput Toxicol
  preferred: true
  title: 'EPA''s DSSTox database: History of development of a curated chemistry resource
    supporting computational toxicology research'
  year: '2019'
---
# Distributed Structure-Searchable Toxicity (DSSTox) Database

EPA's Distributed Structure-Searchable Toxicity (DSSTox) database is a comprehensive public resource for high-quality chemical and chemistry data. From its inception in 2004, DSSTox has focused on quality data curation to resolve chemical identifier errors and ensure accurate chemical structure alignment with data important to assessing chemical risk.

## Key Features

- **Over 1.2 million curated substances** with quality-controlled chemical identifiers
- **Accurate structure-identifier mappings** including CAS RNs, IUPAC names, SMILES, InChIKeys
- **Multi-tiered quality control** with five QC levels conveying curator confidence
- **Integration with EPA tools** including CompTox Chemicals Dashboard, EcoTox Knowledgebase, and Chemical Exposure Knowledgebase
- **Public data access** through web applications, API, and downloadable files

## Background

DSSTox started as a manual curation of 7,000 chemicals and expanded using auto-loads from EPA's Substance Registry Services (SRS), the National Library of Medicine's ChemID, and PubChem. The curation process requires uniquely mapped identifiers (CAS RN, name, and structure) for each substance, rejecting content where any two identifiers conflict either within or across datasets.

## Information Resource ID

This resource has the Information Resource identifier: `infores:dsstoxdb`