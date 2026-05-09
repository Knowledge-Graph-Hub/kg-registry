---
activity_status: inactive
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://string-db.org/help/
      - contact_type: email
        value: string-db@embl.de
    id: stringdb
    label: STRING/EMBL Team
creation_date: '2025-11-17T00:00:00Z'
description: STITCH (Search Tool for Interactions of Chemicals) is a database of known and predicted interactions between chemicals and proteins across 2,031 organisms. The resource integrates chemical-protein interactions from five main sources - genomic context predictions, high-throughput experimental data, conserved co-expression patterns, automated text mining, and curated knowledge from databases. STITCH covers 9.6 million proteins and 500,000 chemicals with 1.6 billion interactions, combining direct physical and indirect functional associations. Version 5 was released in 2016 and is no longer actively maintained (marked as unsupported).
domains:
  - drug discovery
  - systems biology
  - biomedical
homepage_url: http://stitch-db.org/
id: stitch
infores_id: stitch
last_modified_date: '2026-01-15T00:00:00Z'
layout: resource_detail
license:
  id: http://stitch-db.org/download/STITCHacademiclicense.pdf
  label: STITCH Academic License (free for academic use; commercial licensing available)
name: STITCH
products:
  - category: Product
    description: Web interface for searching and visualizing chemical-protein interactions across organisms
    format: http
    id: stitch.portal
    is_public: true
    name: STITCH Web Portal
    original_source:
      - source: stitch
        relation_type: prov:hadPrimarySource
    product_url: http://stitch-db.org/
  - category: Product
    description: Downloadable data files containing chemical-protein interaction networks
    format: tsv
    id: stitch.downloads
    is_public: true
    name: STITCH Data Downloads
    original_source:
      - source: stitch
        relation_type: prov:hadPrimarySource
    product_url: http://stitch-db.org/cgi/download.pl
  - category: ProgrammingInterface
    description: API for programmatic access to STITCH chemical-protein interaction data
    format: http
    id: stitch.api
    is_public: true
    name: STITCH API
    original_source:
      - source: stitch
        relation_type: prov:hadPrimarySource
    product_url: http://stitch-db.org/cgi/access.pl?footer_active_subpage=apis
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
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
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: Core UniBioMap graph edges file.
    format: csv
    id: unibiomap.links
    name: UniBioMap Graph Links
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 1406201678
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
  - category: GraphProduct
    description: Auxiliary UniBioMap graph annotations and metadata.
    format: tsv
    id: unibiomap.auxs
    name: UniBioMap Graph Auxiliaries
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 591290539
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
  - category: GraphProduct
    description: Predicted UniBioMap graph edges with confidence scores.
    format: csv
    id: unibiomap.pred
    name: UniBioMap Predicted Graph
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 2484982268
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
  - category: GraphProduct
    description: Full unfiltered UniBioMap predicted graph edges file.
    format: csv
    id: unibiomap.pred.full
    name: UniBioMap Predicted Graph (Full)
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 6303875907
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
  - category: GraphProduct
    description: Graph database dump and additional relationship files for the Clinical Knowledge Graph.
    format: neo4j
    id: ckg.graph
    name: CKG Graph Database Dump
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
  - authors:
      - Damian Szklarczyk
      - Alberto Santos
      - Christian von Mering
      - Lars Juhl Jensen
      - Peer Bork
      - Michael Kuhn
    doi: 10.1093/nar/gkv1277
    id: PMID:26590256
    journal: Nucleic Acids Res
    title: 'STITCH 5: augmenting protein-chemical interaction networks with tissue and affinity data'
    year: '2016'
taxon:
  - NCBITaxon:1
warnings:
  - STITCH v5 (2016) is marked unsupported on the homepage; data and APIs may be outdated.
---

# Stitch
