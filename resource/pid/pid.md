---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.cancer.gov/
  label: National Cancer Institute
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nature.com/
  label: Nature Publishing Group
creation_date: '2025-01-10T00:00:00Z'
description: The Pathway Interaction Database (PID) was a highly curated collection
  of human molecular signaling, regulatory pathways, and key cellular processes developed
  through a collaboration between the US National Cancer Institute and Nature Publishing
  Group. The database focused specifically on cancer-relevant signaling and regulatory
  pathways rather than metabolic processes, providing detailed network-level representations
  of molecular interactions with comprehensive literature citations and evidence codes
  for each event. PID contained three main data collections the NCI-Nature Curated
  pathways representing expert-curated cancer signaling networks, imported Reactome
  pathways in BioPAX format, and BioCarta pathway data, together comprising 77 expert-reviewed
  pathways with over 4,300 manually curated interactions involving more than 2,600
  proteins annotated with detailed posttranslational modifications including 7,400+
  phosphorylation events. Each interaction in the NCI-Nature curated collection was
  associated with specific literature references from over 3,100 distinct PubMed citations
  and annotated with evidence codes indicating the type of experimental support. The
  database employed a sophisticated data model distinguishing five types of molecular
  events including transcription, translocation, biochemical reactions, protein modifications,
  and macroprocesses, with molecules characterized by posttranslational modifications,
  cellular locations, and activity states. PID provided powerful query capabilities
  enabling users to search by molecule names, construct dynamic interaction networks
  connecting specified molecules, overlay experimental data from gene expression studies
  onto pathways using batch query tools with statistical enrichment analysis, and
  visualize both predefined expert-curated pathways and novel networks generated computationally
  from the interaction database. The resource was particularly valuable for cancer
  research, allowing identification of parallel signaling paths, elucidation of therapy
  resistance mechanisms, and integration of genomic abnormalities with pathway contexts.
  While the original NCI-hosted PID website is no longer actively maintained and was
  discontinued, the complete PID dataset has been preserved and remains accessible
  through Pathway Commons, NDEx Bioscience Network Exchange, and as BioPAX Level 2
  format exports, ensuring continued availability of this valuable curated knowledge
  for the research community.
domains:
- pathways
- biological systems
homepage_url: http://pid.nci.nih.gov/
id: pid
last_modified_date: '2025-12-13T00:00:00Z'
layout: resource_detail
name: Pathway Interaction Database
products:
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  format: mixed
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: Product
  description: pid.pathway Nodes TSV
  format: tsv
  id: obo-db-ingest.pid.pathway.tsv
  name: pid.pathway Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pid
  product_file_size: 3923
  product_url: https://w3id.org/biopragmatics/resources/pid.pathway/pid.pathway.tsv
- category: GraphicalInterface
  description: Browser for complete Hetionet v1.0 graph database in Neo4j
  format: http
  id: hetionet.neo4j
  name: Hetionet v1.0 Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://neo4j.het.io/browser/
- category: GraphProduct
  description: Hetionet v1.0 in JSON format
  format: json
  id: hetionet.data.json
  name: Hetionet v1.0 JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 131
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/json/hetionet-v1.0.json.bz2
- category: GraphProduct
  description: Hetionet v1.0 as a Neo4j database
  format: neo4j
  id: hetionet.data.neo4j
  name: Hetionet v1.0 Neo4j
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 132
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/neo4j/hetionet-v1.0.db.tar.bz2
- category: GraphProduct
  description: Hetionet v1.0 as SIF edges
  format: sif
  id: hetionet.data.edges
  name: Hetionet v1.0 edges (SIF)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 131
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-edges.sif.gz
- category: GraphProduct
  description: Hetionet v1.0 as TSV nodes
  format: tsv
  id: hetionet.data.nodes
  name: Hetionet v1.0 nodes (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 427128
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-nodes.tsv
- category: ProcessProduct
  description: Python package for creating, querying, and operating on hetnets (heterogeneous
    networks)
  id: hetnetpy
  name: hetnetpy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://github.com/hetio/hetnetpy
- category: GraphicalInterface
  description: Web application to search and explore connectivity between nodes in
    Hetionet
  format: http
  id: hetionet.search
  name: Hetnet Connectivity Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://het.io/search
- category: Product
  description: Downloadable gene set files in GMT, XML, and other formats for human
    collections including hallmarks, curated pathways, ontologies, and computational
    signatures; free registration is required for downloads
  format: mixed
  id: msigdb.downloads.human
  name: MSigDB Human Gene Sets Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
  secondary_source:
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mirbase
  - relation_type: prov:used
    source: pid
  - relation_type: prov:used
    source: reactome
  - relation_type: prov:used
    source: wikipathways
  warnings:
  - Downloads redirect unauthenticated users to the GSEA/MSigDB login page; registration
    is free but required for direct file access.
- category: Product
  description: Downloadable gene set files for mouse collections including mouse-ortholog
    hallmarks, curated pathways, ontologies, and cell type signatures; free registration
    is required for downloads
  format: mixed
  id: msigdb.downloads.mouse
  name: MSigDB Mouse Gene Sets Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
  secondary_source:
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mirbase
  - relation_type: prov:used
    source: pid
  - relation_type: prov:used
    source: reactome
  - relation_type: prov:used
    source: wikipathways
  warnings:
  - Downloads redirect unauthenticated users to the GSEA/MSigDB login page; registration
    is free but required for direct file access.
- category: Product
  compression: gzip
  description: PC v14 integrated BioPAX Level 3 unified model containing normalized
    pathway data, molecular interactions, cross-database entity mappings, and metadata-derived
    content from 26 datasource rows.
  format: biopax
  id: pathwaycommons.biopax
  name: Integrated BioPAX Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 1700903742
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-biopax.owl.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: Product
  description: Download directory for Pathway Commons PC v14 integrated pathway and
    molecular interaction datasets, including BioPAX, SIF, GMT, TXT, and JSON-LD products.
  format: mixed
  id: pathwaycommons.downloads
  name: Pathway Commons Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 Simple Interaction Format network file representing binary pairwise
    molecular relationships integrated from Pathway Commons upstream datasource rows.
  format: sif
  id: pathwaycommons.sif
  name: SIF Network Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 9810179
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.sif.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 Gene Matrix Transposed gene sets for pathway enrichment analysis,
    derived from the integrated Pathway Commons pathway archive.
  format: tsv
  id: pathwaycommons.gmt
  name: GMT Gene Set Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 262513
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.gmt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: Product
  compression: gzip
  description: PC v14 tab-delimited extended SIF node and edge file using HGNC-oriented
    identifiers for integrated Pathway Commons interactions.
  format: txt
  id: pathwaycommons.txt
  name: Extended SIF TXT Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  product_file_size: 115608500
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-hgnc.txt.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: unichem
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: humancyc
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: reconx
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: inoh
  - relation_type: prov:wasDerivedFrom
    source: netpath
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: biofactoid
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
- category: GraphProduct
  description: RDF graph converting NCI Pathway Interaction Database version 2.0 networks
    into RDF, enriched with INDRA evidence metadata.
  format: ttl
  id: ncipidkg.graph.ttl
  name: NCI-PID 2.0 KG RDF graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncipidkg
  - relation_type: prov:wasDerivedFrom
    source: pid
  product_url: https://www.ndexbio.org/index.html#/networkset/7bc65b82-2a2f-11ed-ac45-0ac135e8bacf
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: indra
- category: GraphProduct
  description: The SPOKE-OKN knowledge graph, an OKN-hosted RDF publication of the
    SPOKE biomedical and environmental health knowledge graph, served through FRINK
    query services.
  format: ttl
  id: spoke-okn.graph
  name: SPOKE-OKN Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke-okn
  - relation_type: prov:wasDerivedFrom
    source: spoke
  product_url: https://spoke.ucsf.edu
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bgee
  - relation_type: prov:wasInfluencedBy
    source: bindingdb
  - relation_type: prov:wasInfluencedBy
    source: bv-brc
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: civic
  - relation_type: prov:wasInfluencedBy
    source: cl
  - relation_type: prov:wasInfluencedBy
    source: clinicaltrialsgov
  - relation_type: prov:wasInfluencedBy
    source: diseases
  - relation_type: prov:wasInfluencedBy
    source: doid
  - relation_type: prov:wasInfluencedBy
    source: drugbank
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: foodb
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: gwascatalog
  - relation_type: prov:wasInfluencedBy
    source: hpa
  - relation_type: prov:wasInfluencedBy
    source: interpro
  - relation_type: prov:wasInfluencedBy
    source: kegg
  - relation_type: prov:wasInfluencedBy
    source: lincs-l1000
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: metacyc
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: ncbitaxon
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pathophenodb
  - relation_type: prov:wasInfluencedBy
    source: pfam
  - relation_type: prov:wasInfluencedBy
    source: pid
  - relation_type: prov:wasInfluencedBy
    source: protcid
  - relation_type: prov:wasInfluencedBy
    source: pubmed
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: sider
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: uberon
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
publications:
- authors:
  - Carl F. Schaefer
  - Kira Anthony
  - Shiva Krupa
  - Jeffrey Buchoff
  - Matthew Day
  - Timo Hannay
  - Kenneth H. Buetow
  doi: 10.1093/nar/gkn653
  id: https://doi.org/10.1093/nar/gkn653
  journal: Nucleic Acids Research
  title: 'PID: the Pathway Interaction Database'
  year: '2009'
repository: https://github.com/NCIP/pathway-interaction-database
synonyms:
- PID
- Pathway Interaction Database
- NCI-Nature PID
taxon:
- NCBITaxon:9606
---
# Pathway Interaction Database

## Overview

The Pathway Interaction Database (PID) was a highly curated collection of human signaling and regulatory pathways focused on cancer biology, developed by the National Cancer Institute and Nature Publishing Group. Though no longer actively maintained at its original NCI site, PID data remains accessible through Pathway Commons and NDEx.