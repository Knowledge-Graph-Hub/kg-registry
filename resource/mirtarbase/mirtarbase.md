---
activity_status: active
category: DataSource
creation_date: '2025-07-17T00:00:00Z'
description: miRTarBase is a comprehensive database of experimentally validated microRNA-target
  interactions (MTIs). It collects and curates miRNA-target interactions with experimental
  evidence from the literature, including data from reporter assays, western blot,
  qPCR, microarray, and high-throughput experiments such as CLIP-Seq.
domains:
- genomics
- biological systems
id: mirtarbase
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: miRTarBase
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing experimentally validated microRNA-target
    interactions across multiple species.
  format: http
  id: mirtarbase.portal
  name: miRTarBase Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/index.php
- category: Product
  description: Complete dataset of microRNA-target interactions (MTI) in CSV format
    containing all experimentally validated interactions.
  format: csv
  id: mirtarbase.mti
  name: miRTarBase Complete MTI Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-08_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-12: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1028)'')))'
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-17: HTTP 412 error
    when accessing file'
- category: Product
  description: Dataset of microRNA target sites with detailed binding site information
    in CSV format.
  format: csv
  id: mirtarbase.target_sites
  name: miRTarBase Target Sites Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-12: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1028)'')))'
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-17: HTTP 412 error
    when accessing file'
- category: Product
  description: Species-specific microRNA-target interaction datasets in CSV format
    for human, mouse, rat, and 25+ other species.
  format: csv
  id: mirtarbase.species_mti
  name: miRTarBase Species-Specific MTI Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-04_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-12: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1028)'')))'
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-17: HTTP 412 error
    when accessing file'
- category: Product
  description: Curated datasets filtered for strong experimental evidence including
    reporter assays, western blot, qPCR, and CLIP-Seq data.
  format: csv
  id: mirtarbase.strong_evidence
  name: miRTarBase Strong Evidence Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-25_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-12: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1028)'')))'
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-17: HTTP 412 error
    when accessing file'
- category: Product
  description: Archive of previous miRTarBase releases for reproducibility and historical
    comparisons.
  format: http
  id: mirtarbase.archive
  name: miRTarBase Previous Releases Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  product_url: https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/download.php
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1028)')))
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-13_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-15_ Error connecting
    to URL_ HTTPSConnectionPool(host='mirtarbase.cuhk.edu.cn', port=443)_ Max retries
    exceeded with url_ /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    '[SSL_ SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c_1017)')))
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-12: Error connecting
    to URL: HTTPSConnectionPool(host=''mirtarbase.cuhk.edu.cn'', port=443): Max retries
    exceeded with url: /~miRTarBase/miRTarBase_2025/php/download.php (Caused by SSLError(SSLError(1,
    ''[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1028)'')))'
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-17: HTTP 412 error
    when accessing file'
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
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
publications:
- authors:
  - Cui S
  - Yu S
  - Huang HY
  - Lin YCD
  - Huang Y
  - Zhang B
  - Xiao J
  - Zuo H
  - Wang J
  - Li Z
  doi: 10.1093/nar/gkae1072
  id: https://doi.org/10.1093/nar/gkae1072
  journal: Nucleic Acids Research
  preferred: true
  title: 'miRTarBase 2025: updates to the collection of experimentally validated microRNA-target
    interactions'
  year: '2025'
- authors:
  - Huang HY
  - Lin YCD
  - Cui S
  - Huang Y
  - Tang Y
  - Xu J
  - Bao J
  - Li Y
  - Wen J
  - Zuo H
  doi: 10.1093/nar/gkab1079
  id: https://doi.org/10.1093/nar/gkab1079
  journal: Nucleic Acids Research
  preferred: false
  title: 'miRTarBase update 2022: an informative resource for experimentally validated
    miRNA-target interactions'
  year: '2022'
---
# miRTarBase

miRTarBase is a comprehensive database that curates experimentally validated microRNA-target interactions (MTIs) from published literature. Developed by the Warshel Institute for Computational Biology at The Chinese University of Hong Kong, Shenzhen, miRTarBase collects MTIs with experimental evidence from various methods including reporter assays, western blot, qPCR, microarray, and next-generation sequencing experiments such as CLIP-Seq and degradome sequencing. The database covers over 28 species and provides detailed information about target sites, experimental evidence, and validation methods. Users can browse and download complete datasets in CSV format, including species-specific files and subsets filtered by evidence strength. For more information, visit the [miRTarBase portal](https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/php/index.php).