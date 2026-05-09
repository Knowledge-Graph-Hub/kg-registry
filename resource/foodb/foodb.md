---
activity_status: active
category: DataSource
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: shhan@ualberta.ca
    label: Scott Han
  - category: Organization
    label: The Metabolomics Innovation Centre (TMIC)
creation_date: '2025-05-29T00:00:00Z'
description: The Food Database (FooDB) is the world's largest and most comprehensive resource on food constituents, chemistry, and biology. It provides detailed information about the chemical constituents found in food, designed for applications in nutrition, food science, dietary planning, and general education.
domains:
  - biomedical
  - food science
  - nutrition
  - health
homepage_url: https://foodb.ca/
id: foodb
infores_id: foodb
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: CC-BY-NC-4.0
name: FooDB
products:
  - category: GraphicalInterface
    description: Web interface that allows searching, browsing, and exploring food compounds and their properties.
    id: foodb.web
    name: FooDB Web Interface
    product_url: https://foodb.ca/
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: targz
    description: Complete FooDB database in CSV format
    format: csv
    id: foodb.data.csv
    name: FooDB CSV Data
    product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_csv.tar.gz
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-05_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: targz
    description: Complete FooDB database in XML format
    format: xml
    id: foodb.data.xml
    name: FooDB XML Data
    product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_xml.tar.gz
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: zip
    description: Complete FooDB database in JSON format
    format: json
    id: foodb.data.json
    name: FooDB JSON Data
    product_url: https://foodb.ca/public/system/downloads/foodb_2020_04_07_json.zip
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: targz
    description: Complete FooDB database as MySQL dump
    id: foodb.data.mysql
    name: FooDB MySQL Dump
    product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_mysql.tar.gz
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: zip
    description: Experimental C-MS Spectra data from FooDB
    id: foodb.data.experimental_cms
    name: FooDB Experimental C-MS Spectra
    product_url: https://foodb.ca/public/system/downloads/foodb_experimental_cms_spectra.zip
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-05_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: zip
    description: Predicted C-MS Spectra data from FooDB
    id: foodb.data.predicted_cms
    name: FooDB Predicted C-MS Spectra
    product_url: https://foodb.ca/public/system/downloads/foodb_predicted_cms_spectra.zip
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-05_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: zip
    description: Experimental MS-MS Spectra data from FooDB
    id: foodb.data.experimental_msms
    name: FooDB Experimental MS-MS Spectra
    product_url: https://foodb.ca/public/system/downloads/foodb_experimental_msms_spectra.zip
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: zip
    description: Predicted MS-MS Spectra data from FooDB
    id: foodb.data.predicted_msms
    name: FooDB Predicted MS-MS Spectra
    product_url: https://foodb.ca/public/system/downloads/foodb_predicted_msms_spectra.zip
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: zip
    description: NMR Spectra data from FooDB
    id: foodb.data.nmr
    name: FooDB NMR Spectra
    product_url: https://foodb.ca/public/system/downloads/foodb_nmr_spectra.zip
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: zip
    description: Free Induction Decay (FID) files from FooDB
    id: foodb.data.fid
    name: FooDB FID Files
    product_url: https://foodb.ca/public/system/downloads/foodb_fid_files.zip
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-12-04_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 404 error when accessing file'
      - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 404 error when accessing file'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: Product
    compression: zip
    description: Image files of compounds, foods, and chemical structures
    id: foodb.data.images
    name: FooDB Image Files
    product_url: https://foodb.ca/public/system/downloads/foodb_image_files.zip
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
      - File was not able to be retrieved when checked on 2025-12-11_ HTTP 502 error when accessing file
      - File was not able to be retrieved when checked on 2025-11-26_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2025-08-07_ HTTP 500 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - 'File was not able to be retrieved when checked on 2026-05-09: No Content-Length header found'
    original_source:
      - source: foodb
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: The SPOKE knowledge graph containing nodes and edges from multiple biomedical data sources.
    id: spoke.graph
    name: SPOKE Graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: pid
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: drugcentral
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: lincs-l1000
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: omim
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: civic
      - relation_type: prov:hadPrimarySource
        source: gdsc
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: metacyc
      - relation_type: prov:hadPrimarySource
        source: bv-brc
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: pathophenodb
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: interpro
      - relation_type: prov:hadPrimarySource
        source: protcid
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: spoke
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: cancer-genome-interpreter.clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: Core UniBioMap graph edges file.
    format: csv
    id: unibiomap.links
    name: UniBioMap Graph Links
    original_source:
      - relation_type: prov:hadPrimarySource
        source: unibiomap
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: tcdb
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: batman
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: compath
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: inchikey
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: omim
    product_file_size: 1406201678
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
  - category: GraphProduct
    description: Auxiliary UniBioMap graph annotations and metadata.
    format: tsv
    id: unibiomap.auxs
    name: UniBioMap Graph Auxiliaries
    original_source:
      - relation_type: prov:hadPrimarySource
        source: unibiomap
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: tcdb
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: batman
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: compath
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: inchikey
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: omim
    product_file_size: 591290539
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
  - category: GraphProduct
    description: Predicted UniBioMap graph edges with confidence scores.
    format: csv
    id: unibiomap.pred
    name: UniBioMap Predicted Graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: unibiomap
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: tcdb
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: batman
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: compath
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: inchikey
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: omim
    product_file_size: 2484982268
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
  - category: GraphProduct
    description: Full unfiltered UniBioMap predicted graph edges file.
    format: csv
    id: unibiomap.pred.full
    name: UniBioMap Predicted Graph (Full)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: unibiomap
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bindingdb
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: tcdb
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: batman
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: compath
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: inchikey
      - relation_type: prov:hadPrimarySource
        source: unichem
      - relation_type: prov:hadPrimarySource
        source: omim
    product_file_size: 6303875907
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
  - category: GraphProduct
    description: Graph database dump and additional relationship files for the Clinical Knowledge Graph.
    format: neo4j
    id: ckg.graph
    name: CKG Graph Database Dump
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
  - authors:
      - Wishart DS
      - Knox C
      - Guo AC
      - Eisner R
      - Young N
      - Gautam B
      - Hau DD
      - Psychogios N
      - Dong E
      - Bouatra S
      - Mandal R
      - Sinelnikov I
      - Xia J
      - Jia L
      - Cruz JA
      - Lim E
      - Sobsey CA
      - Shrivastava S
      - Huang P
      - Liu P
      - Fang L
      - Peng J
      - Fradette R
      - Cheng D
      - Tzur D
      - Clements M
      - Lewis A
      - De Souza A
      - Zuniga A
      - Dawe M
      - Xiong Y
      - Clive D
      - Greiner R
      - Nazyrova A
      - Shaykhutdinov R
      - Li L
      - Vogel HJ
      - Forsythe I
    doi: doi:10.1093/nar/gkn810
    id: https://doi.org/10.1093/nar/gkn810
    journal: Nucleic Acids Research
    preferred: true
    title: HMDB - a knowledgebase for the human metabolome
    year: '2009'
  - authors:
      - Wishart DS
      - Feunang YD
      - Marcu A
      - Guo AC
      - Liang K
      - Vázquez-Fresno R
      - Sajed T
      - Johnson D
      - Li C
      - Karu N
      - Sayeeda Z
      - Lo E
      - Assempour N
      - Berjanskii M
      - Singhal S
      - Arndt D
      - Liang Y
      - Badran H
      - Grant J
      - Serra-Cayuela A
      - Liu Y
      - Mandal R
      - Neveu V
      - Pon A
      - Knox C
      - Wilson M
      - Manach C
      - Scalbert A
    id: https://doi.org/10.1093/nar/gkx1089
    journal: Nucleic Acids Research
    title: HMDB 4.0 - The Human Metabolome Database for 2018
    year: '2018'
---

FooDB (The Food Database) is the world's largest and most comprehensive resource on food constituents, chemistry, and biology. It is maintained by The Metabolomics Innovation Centre (TMIC), a nationally-funded research and core facility in Canada.

The database contains extensive data on food compounds, including their chemical properties, biological activities, dietary sources, and health effects. Each chemical entry in FooDB contains more than 100 separate data fields covering detailed compositional, biochemical, and physiological information obtained from the literature.

FooDB integrates information from multiple sources, linking food compound data to other relevant databases such as HMDB, PubChem, CHEBI, KEGG, and NCBI_Taxonomy. This integration provides a comprehensive view of food composition and its impact on nutrition and health.

The database offers information about both macronutrients and micronutrients, including many of the constituents that give foods their flavor, color, taste, texture, and aroma. It classifies food compounds based on their chemical nature and biological relevance, helping users better understand the role of these compounds in nutrition and health.

Users can browse or search FooDB by food source, name, descriptors, function, or concentrations. The database supports a wide range of search functionalities, allowing users to perform text, sequence, chemical structure, and relational queries.
