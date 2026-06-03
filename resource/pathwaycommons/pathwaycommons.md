---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.mskcc.org/
    id: mskcc
    label: Memorial Sloan Kettering Cancer Center
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.utoronto.ca/
    id: utoronto
    label: University of Toronto
creation_date: '2026-06-02T00:00:00Z'
description: Pathway Commons is a centralized web resource that aggregates biological pathway and molecular interaction data from pathway, interaction, protein, chemical, and identifier-mapping sources into BioPAX and related network formats. Its PC v14 metadata lists 26 datasource rows, 6,692 pathways, 3,579,336 molecular interactions, and 4,168,535 physical entities.
domains:
  - pathways
  - systems biology
  - biomedical
homepage_url: https://www.pathwaycommons.org/
id: pathwaycommons
infores_id: pathway-commons
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0 (aggregated content)
name: Pathway Commons
products:
  - category: ProgrammingInterface
    description: RESTful web service API for programmatic access to Pathway Commons PC v14 data with search, pathway retrieval, graph traversal, and network analysis operations.
    format: http
    id: pathwaycommons.api
    is_public: true
    name: Pathway Commons REST API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pathwaycommons
    product_url: https://www.pathwaycommons.org/pc2/
  - category: GraphicalInterface
    description: Interactive Pathway Commons web interface for browsing, searching, and visualizing integrated biological pathways and molecular interactions.
    format: http
    id: pathwaycommons.web
    is_public: true
    name: Pathway Commons Web Interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pathwaycommons
    product_url: https://www.pathwaycommons.org/
  - category: Product
    description: Download directory for Pathway Commons PC v14 integrated pathway and molecular interaction datasets, including BioPAX, SIF, GMT, TXT, and JSON-LD products.
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
    description: PC v14 integrated BioPAX Level 3 unified model containing normalized pathway data, molecular interactions, cross-database entity mappings, and metadata-derived content from 26 datasource rows.
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
    compression: gzip
    description: PC v14 Simple Interaction Format network file representing binary pairwise molecular relationships integrated from Pathway Commons upstream datasource rows.
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
    description: PC v14 Gene Matrix Transposed gene sets for pathway enrichment analysis, derived from the integrated Pathway Commons pathway archive.
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
    description: PC v14 tab-delimited extended SIF node and edge file using HGNC-oriented identifiers for integrated Pathway Commons interactions.
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
  - category: DocumentationProduct
    description: Comprehensive API documentation, data format specifications, and tutorials for using Pathway Commons data and services
    format: http
    id: pathwaycommons.documentation
    is_public: true
    name: Pathway Commons Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pathwaycommons
    product_url: https://www.pathwaycommons.org/pc2/swagger-ui.html
  - category: GraphProduct
    compression: gzip
    description: PharMeBINet V2 JSON release published on February 6, 2024.
    format: json
    id: pharmebinet.json
    latest_version: v2
    name: PharMeBINet JSON Release
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pharmebinet
    product_file_size: 1942958027
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.json.gz/content
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: adrecs
      - relation_type: prov:wasDerivedFrom
        source: aelous
      - relation_type: prov:wasDerivedFrom
        source: atc
      - relation_type: prov:wasDerivedFrom
        source: bindingdb
      - relation_type: prov:wasDerivedFrom
        source: biogrid
      - relation_type: prov:wasDerivedFrom
        source: cl
      - relation_type: prov:wasDerivedFrom
        source: chebi
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: ctd
      - relation_type: prov:wasDerivedFrom
        source: dbsnp
      - relation_type: prov:wasDerivedFrom
        source: ddinter
      - relation_type: prov:wasDerivedFrom
        source: doid
      - relation_type: prov:wasDerivedFrom
        source: diseases
      - relation_type: prov:wasDerivedFrom
        source: disgenet
      - relation_type: prov:wasDerivedFrom
        source: drugbank
      - relation_type: prov:wasDerivedFrom
        source: drugcentral
      - relation_type: prov:wasDerivedFrom
        source: efo
      - relation_type: prov:wasDerivedFrom
        source: fideo
      - relation_type: prov:wasDerivedFrom
        source: foodon
      - relation_type: prov:wasDerivedFrom
        source: gencc
      - relation_type: prov:wasDerivedFrom
        source: go
      - relation_type: prov:wasDerivedFrom
        source: gwascatalog
      - relation_type: prov:wasDerivedFrom
        source: hetionet
      - relation_type: prov:wasDerivedFrom
        source: hgnc
      - relation_type: prov:wasDerivedFrom
        source: hippie
      - relation_type: prov:wasDerivedFrom
        source: hmdb
      - relation_type: prov:wasDerivedFrom
        source: hp
      - relation_type: prov:wasDerivedFrom
        source: iid
      - relation_type: prov:wasDerivedFrom
        source: iptmnet
      - relation_type: prov:wasDerivedFrom
        source: markerdb
      - relation_type: prov:wasDerivedFrom
        source: med-rt
      - relation_type: prov:wasDerivedFrom
        source: mirbase
      - relation_type: prov:wasDerivedFrom
        source: mondo
      - relation_type: prov:wasDerivedFrom
        source: ncbigene
      - relation_type: prov:wasDerivedFrom
        source: ndfrt
      - relation_type: prov:wasDerivedFrom
        source: omim
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: pharmgkb
      - relation_type: prov:wasDerivedFrom
        source: ptmd
      - relation_type: prov:wasDerivedFrom
        source: pubchem
      - relation_type: prov:wasDerivedFrom
        source: qptm
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: refseq
      - relation_type: prov:wasDerivedFrom
        source: rnadisease
      - relation_type: prov:wasDerivedFrom
        source: rnainter
      - relation_type: prov:wasDerivedFrom
        source: sider
      - relation_type: prov:wasDerivedFrom
        source: smpdb
      - relation_type: prov:wasDerivedFrom
        source: ttd
      - relation_type: prov:wasDerivedFrom
        source: uberon
      - relation_type: prov:wasDerivedFrom
        source: uniprot
      - relation_type: prov:wasDerivedFrom
        source: wikipathways
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 TSV release published on February 6, 2024.
    format: tsv
    id: pharmebinet.tsv
    latest_version: v2
    name: PharMeBINet TSV Release
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pharmebinet
    product_file_size: 1922614551
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_tsv_24_02_06.zip/content
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: adrecs
      - relation_type: prov:wasDerivedFrom
        source: aelous
      - relation_type: prov:wasDerivedFrom
        source: atc
      - relation_type: prov:wasDerivedFrom
        source: bindingdb
      - relation_type: prov:wasDerivedFrom
        source: biogrid
      - relation_type: prov:wasDerivedFrom
        source: cl
      - relation_type: prov:wasDerivedFrom
        source: chebi
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: ctd
      - relation_type: prov:wasDerivedFrom
        source: dbsnp
      - relation_type: prov:wasDerivedFrom
        source: ddinter
      - relation_type: prov:wasDerivedFrom
        source: doid
      - relation_type: prov:wasDerivedFrom
        source: diseases
      - relation_type: prov:wasDerivedFrom
        source: disgenet
      - relation_type: prov:wasDerivedFrom
        source: drugbank
      - relation_type: prov:wasDerivedFrom
        source: drugcentral
      - relation_type: prov:wasDerivedFrom
        source: efo
      - relation_type: prov:wasDerivedFrom
        source: fideo
      - relation_type: prov:wasDerivedFrom
        source: foodon
      - relation_type: prov:wasDerivedFrom
        source: gencc
      - relation_type: prov:wasDerivedFrom
        source: go
      - relation_type: prov:wasDerivedFrom
        source: gwascatalog
      - relation_type: prov:wasDerivedFrom
        source: hetionet
      - relation_type: prov:wasDerivedFrom
        source: hgnc
      - relation_type: prov:wasDerivedFrom
        source: hippie
      - relation_type: prov:wasDerivedFrom
        source: hmdb
      - relation_type: prov:wasDerivedFrom
        source: hp
      - relation_type: prov:wasDerivedFrom
        source: iid
      - relation_type: prov:wasDerivedFrom
        source: iptmnet
      - relation_type: prov:wasDerivedFrom
        source: markerdb
      - relation_type: prov:wasDerivedFrom
        source: med-rt
      - relation_type: prov:wasDerivedFrom
        source: mirbase
      - relation_type: prov:wasDerivedFrom
        source: mondo
      - relation_type: prov:wasDerivedFrom
        source: ncbigene
      - relation_type: prov:wasDerivedFrom
        source: ndfrt
      - relation_type: prov:wasDerivedFrom
        source: omim
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: pharmgkb
      - relation_type: prov:wasDerivedFrom
        source: ptmd
      - relation_type: prov:wasDerivedFrom
        source: pubchem
      - relation_type: prov:wasDerivedFrom
        source: qptm
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: refseq
      - relation_type: prov:wasDerivedFrom
        source: rnadisease
      - relation_type: prov:wasDerivedFrom
        source: rnainter
      - relation_type: prov:wasDerivedFrom
        source: sider
      - relation_type: prov:wasDerivedFrom
        source: smpdb
      - relation_type: prov:wasDerivedFrom
        source: ttd
      - relation_type: prov:wasDerivedFrom
        source: uberon
      - relation_type: prov:wasDerivedFrom
        source: uniprot
      - relation_type: prov:wasDerivedFrom
        source: wikipathways
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 GraphML release published on February 6, 2024.
    format: mixed
    id: pharmebinet.graphml
    latest_version: v2
    name: PharMeBINet GraphML Release
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pharmebinet
    product_file_size: 2027519087
    product_url: https://zenodo.org/api/records/17814889/files/PharMeBiNet_graphml_24_02_06.zip/content
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: adrecs
      - relation_type: prov:wasDerivedFrom
        source: aelous
      - relation_type: prov:wasDerivedFrom
        source: atc
      - relation_type: prov:wasDerivedFrom
        source: bindingdb
      - relation_type: prov:wasDerivedFrom
        source: biogrid
      - relation_type: prov:wasDerivedFrom
        source: cl
      - relation_type: prov:wasDerivedFrom
        source: chebi
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: ctd
      - relation_type: prov:wasDerivedFrom
        source: dbsnp
      - relation_type: prov:wasDerivedFrom
        source: ddinter
      - relation_type: prov:wasDerivedFrom
        source: doid
      - relation_type: prov:wasDerivedFrom
        source: diseases
      - relation_type: prov:wasDerivedFrom
        source: disgenet
      - relation_type: prov:wasDerivedFrom
        source: drugbank
      - relation_type: prov:wasDerivedFrom
        source: drugcentral
      - relation_type: prov:wasDerivedFrom
        source: efo
      - relation_type: prov:wasDerivedFrom
        source: fideo
      - relation_type: prov:wasDerivedFrom
        source: foodon
      - relation_type: prov:wasDerivedFrom
        source: gencc
      - relation_type: prov:wasDerivedFrom
        source: go
      - relation_type: prov:wasDerivedFrom
        source: gwascatalog
      - relation_type: prov:wasDerivedFrom
        source: hetionet
      - relation_type: prov:wasDerivedFrom
        source: hgnc
      - relation_type: prov:wasDerivedFrom
        source: hippie
      - relation_type: prov:wasDerivedFrom
        source: hmdb
      - relation_type: prov:wasDerivedFrom
        source: hp
      - relation_type: prov:wasDerivedFrom
        source: iid
      - relation_type: prov:wasDerivedFrom
        source: iptmnet
      - relation_type: prov:wasDerivedFrom
        source: markerdb
      - relation_type: prov:wasDerivedFrom
        source: med-rt
      - relation_type: prov:wasDerivedFrom
        source: mirbase
      - relation_type: prov:wasDerivedFrom
        source: mondo
      - relation_type: prov:wasDerivedFrom
        source: ncbigene
      - relation_type: prov:wasDerivedFrom
        source: ndfrt
      - relation_type: prov:wasDerivedFrom
        source: omim
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: pharmgkb
      - relation_type: prov:wasDerivedFrom
        source: ptmd
      - relation_type: prov:wasDerivedFrom
        source: pubchem
      - relation_type: prov:wasDerivedFrom
        source: qptm
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: refseq
      - relation_type: prov:wasDerivedFrom
        source: rnadisease
      - relation_type: prov:wasDerivedFrom
        source: rnainter
      - relation_type: prov:wasDerivedFrom
        source: sider
      - relation_type: prov:wasDerivedFrom
        source: smpdb
      - relation_type: prov:wasDerivedFrom
        source: ttd
      - relation_type: prov:wasDerivedFrom
        source: uberon
      - relation_type: prov:wasDerivedFrom
        source: uniprot
      - relation_type: prov:wasDerivedFrom
        source: wikipathways
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 Neo4j database release published on February 6, 2024.
    format: neo4j
    id: pharmebinet.neo4j
    latest_version: v2
    name: PharMeBINet Neo4j Database
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pharmebinet
    product_file_size: 3847978577
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.zip/content
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: adrecs
      - relation_type: prov:wasDerivedFrom
        source: aelous
      - relation_type: prov:wasDerivedFrom
        source: atc
      - relation_type: prov:wasDerivedFrom
        source: bindingdb
      - relation_type: prov:wasDerivedFrom
        source: biogrid
      - relation_type: prov:wasDerivedFrom
        source: cl
      - relation_type: prov:wasDerivedFrom
        source: chebi
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: ctd
      - relation_type: prov:wasDerivedFrom
        source: dbsnp
      - relation_type: prov:wasDerivedFrom
        source: ddinter
      - relation_type: prov:wasDerivedFrom
        source: doid
      - relation_type: prov:wasDerivedFrom
        source: diseases
      - relation_type: prov:wasDerivedFrom
        source: disgenet
      - relation_type: prov:wasDerivedFrom
        source: drugbank
      - relation_type: prov:wasDerivedFrom
        source: drugcentral
      - relation_type: prov:wasDerivedFrom
        source: efo
      - relation_type: prov:wasDerivedFrom
        source: fideo
      - relation_type: prov:wasDerivedFrom
        source: foodon
      - relation_type: prov:wasDerivedFrom
        source: gencc
      - relation_type: prov:wasDerivedFrom
        source: go
      - relation_type: prov:wasDerivedFrom
        source: gwascatalog
      - relation_type: prov:wasDerivedFrom
        source: hetionet
      - relation_type: prov:wasDerivedFrom
        source: hgnc
      - relation_type: prov:wasDerivedFrom
        source: hippie
      - relation_type: prov:wasDerivedFrom
        source: hmdb
      - relation_type: prov:wasDerivedFrom
        source: hp
      - relation_type: prov:wasDerivedFrom
        source: iid
      - relation_type: prov:wasDerivedFrom
        source: iptmnet
      - relation_type: prov:wasDerivedFrom
        source: markerdb
      - relation_type: prov:wasDerivedFrom
        source: med-rt
      - relation_type: prov:wasDerivedFrom
        source: mirbase
      - relation_type: prov:wasDerivedFrom
        source: mondo
      - relation_type: prov:wasDerivedFrom
        source: ncbigene
      - relation_type: prov:wasDerivedFrom
        source: ndfrt
      - relation_type: prov:wasDerivedFrom
        source: omim
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: pharmgkb
      - relation_type: prov:wasDerivedFrom
        source: ptmd
      - relation_type: prov:wasDerivedFrom
        source: pubchem
      - relation_type: prov:wasDerivedFrom
        source: qptm
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: refseq
      - relation_type: prov:wasDerivedFrom
        source: rnadisease
      - relation_type: prov:wasDerivedFrom
        source: rnainter
      - relation_type: prov:wasDerivedFrom
        source: sider
      - relation_type: prov:wasDerivedFrom
        source: smpdb
      - relation_type: prov:wasDerivedFrom
        source: ttd
      - relation_type: prov:wasDerivedFrom
        source: uberon
      - relation_type: prov:wasDerivedFrom
        source: uniprot
      - relation_type: prov:wasDerivedFrom
        source: wikipathways
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 Neo4j dump release published on February 6, 2024.
    dump_format: neo4j
    format: neo4j
    id: pharmebinet.neo4j.dump
    latest_version: v2
    name: PharMeBINet Neo4j Dump
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pharmebinet
    product_file_size: 3598325722
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_dump_24_02_06.zip/content
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: adrecs
      - relation_type: prov:wasDerivedFrom
        source: aelous
      - relation_type: prov:wasDerivedFrom
        source: atc
      - relation_type: prov:wasDerivedFrom
        source: bindingdb
      - relation_type: prov:wasDerivedFrom
        source: biogrid
      - relation_type: prov:wasDerivedFrom
        source: cl
      - relation_type: prov:wasDerivedFrom
        source: chebi
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: ctd
      - relation_type: prov:wasDerivedFrom
        source: dbsnp
      - relation_type: prov:wasDerivedFrom
        source: ddinter
      - relation_type: prov:wasDerivedFrom
        source: doid
      - relation_type: prov:wasDerivedFrom
        source: diseases
      - relation_type: prov:wasDerivedFrom
        source: disgenet
      - relation_type: prov:wasDerivedFrom
        source: drugbank
      - relation_type: prov:wasDerivedFrom
        source: drugcentral
      - relation_type: prov:wasDerivedFrom
        source: efo
      - relation_type: prov:wasDerivedFrom
        source: fideo
      - relation_type: prov:wasDerivedFrom
        source: foodon
      - relation_type: prov:wasDerivedFrom
        source: gencc
      - relation_type: prov:wasDerivedFrom
        source: go
      - relation_type: prov:wasDerivedFrom
        source: gwascatalog
      - relation_type: prov:wasDerivedFrom
        source: hetionet
      - relation_type: prov:wasDerivedFrom
        source: hgnc
      - relation_type: prov:wasDerivedFrom
        source: hippie
      - relation_type: prov:wasDerivedFrom
        source: hmdb
      - relation_type: prov:wasDerivedFrom
        source: hp
      - relation_type: prov:wasDerivedFrom
        source: iid
      - relation_type: prov:wasDerivedFrom
        source: iptmnet
      - relation_type: prov:wasDerivedFrom
        source: markerdb
      - relation_type: prov:wasDerivedFrom
        source: med-rt
      - relation_type: prov:wasDerivedFrom
        source: mirbase
      - relation_type: prov:wasDerivedFrom
        source: mondo
      - relation_type: prov:wasDerivedFrom
        source: ncbigene
      - relation_type: prov:wasDerivedFrom
        source: ndfrt
      - relation_type: prov:wasDerivedFrom
        source: omim
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: pharmgkb
      - relation_type: prov:wasDerivedFrom
        source: ptmd
      - relation_type: prov:wasDerivedFrom
        source: pubchem
      - relation_type: prov:wasDerivedFrom
        source: qptm
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: refseq
      - relation_type: prov:wasDerivedFrom
        source: rnadisease
      - relation_type: prov:wasDerivedFrom
        source: rnainter
      - relation_type: prov:wasDerivedFrom
        source: sider
      - relation_type: prov:wasDerivedFrom
        source: smpdb
      - relation_type: prov:wasDerivedFrom
        source: ttd
      - relation_type: prov:wasDerivedFrom
        source: uberon
      - relation_type: prov:wasDerivedFrom
        source: uniprot
      - relation_type: prov:wasDerivedFrom
        source: wikipathways
  - category: GraphProduct
    description: Downloadable GeneMANIA interaction network data organized by release and organism, with individual networks, combined default networks, metadata, and identifier mapping tables in plain tab-delimited text files
    format: txt
    id: genemania.networks
    latest_version: current
    name: GeneMANIA Interaction Network Archive
    original_source:
      - relation_type: prov:hadPrimarySource
        source: genemania
    product_url: https://genemania.org/data/current/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: geo
      - relation_type: prov:wasDerivedFrom
        source: biogrid
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: intact
      - relation_type: prov:wasDerivedFrom
        source: mint
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: hprd
publications:
  - authors:
      - Rodchenkov I
      - Babur O
      - Luna A
      - et al.
    doi: 10.1093/nar/gkz946
    id: doi:10.1093/nar/gkz946
    journal: Nucleic Acids Research
    preferred: true
    title: 'Pathway Commons 2019 Update: integration, analysis and exploration of pathway data'
    year: '2020'
  - authors:
      - Cerami EG
      - Gross BE
      - Demir E
      - et al.
    doi: 10.1093/nar/gkq1016
    id: doi:10.1093/nar/gkq1016
    journal: Nucleic Acids Research
    title: Pathway Commons, a web resource for biological pathway data
    year: '2011'
  - authors:
      - Cerami E
      - Bader GD
      - Gross BE
      - Sander C
    doi: 10.1186/1471-2105-7-497
    id: doi:10.1186/1471-2105-7-497
    journal: BMC Bioinformatics
    title: 'cPath: open source software for collecting, storing, and querying biological pathways'
    year: '2006'
repository: https://github.com/PathwayCommons
synonyms:
  - Pathway Commons
  - PathwayCommons
  - PC
taxon:
  - NCBITaxon:9606
version: PC v14
---

# Pathway Commons

Pathway Commons aggregates biological pathway and molecular interaction data for
systems biology reuse. The canonical KG-Registry identifier for this resource is
`pathwaycommons`; the previous alternate entry has been merged into this page.

The PC v14 metadata describes 26 datasource rows, including ChEBI, UniProt,
UniChem, Reactome, PID, PhosphoSitePlus, HumanCyc, HPRD, PANTHER, DIP, BioGRID,
IntAct, BIND, CORUM, MSigDB, miRTarBase, DrugBank, Recon X, CTD, KEGG, INOH,
NetPath, PathBank, InnateDB, and Biofactoid. These upstream sources are recorded
as provenance for the integrated Pathway Commons download products.
