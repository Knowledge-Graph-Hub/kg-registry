---
activity_status: active
category: KnowledgeGraph
creation_date: '2026-04-06T00:00:00Z'
description: PharMeBINet is a heterogeneous pharmacological medical biochemical network that integrates biomedical data sources into a graph for studying drugs, adverse drug reactions, genes, proteins, variants, diseases, and their relationships.
domains:
  - pharmacology
  - drug discovery
  - biomedical
  - health
homepage_url: https://pharmebi.net/
id: pharmebinet
last_modified_date: '2026-05-29T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: PharMeBINet
products:
  - category: GraphicalInterface
    description: Web application for browsing and querying PharMeBINet.
    format: http
    id: pharmebinet.browser
    name: PharMeBINet Web Application
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_url: https://pharmebi.net/
  - category: GraphProduct
    compression: gzip
    description: PharMeBINet V2 JSON release published on February 6, 2024.
    format: json
    id: pharmebinet.json
    latest_version: v2
    name: PharMeBINet JSON Release
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: adrecs
        relation_type: prov:wasDerivedFrom
      - source: aelous
        relation_type: prov:wasDerivedFrom
      - source: atc
        relation_type: prov:wasDerivedFrom
      - source: bindingdb
        relation_type: prov:wasDerivedFrom
      - source: biogrid
        relation_type: prov:wasDerivedFrom
      - source: cl
        relation_type: prov:wasDerivedFrom
      - source: chebi
        relation_type: prov:wasDerivedFrom
      - source: clinvar
        relation_type: prov:wasDerivedFrom
      - source: ctd
        relation_type: prov:wasDerivedFrom
      - source: dbsnp
        relation_type: prov:wasDerivedFrom
      - source: ddinter
        relation_type: prov:wasDerivedFrom
      - source: doid
        relation_type: prov:wasDerivedFrom
      - source: diseases
        relation_type: prov:wasDerivedFrom
      - source: disgenet
        relation_type: prov:wasDerivedFrom
      - source: drugbank
        relation_type: prov:wasDerivedFrom
      - source: drugcentral
        relation_type: prov:wasDerivedFrom
      - source: efo
        relation_type: prov:wasDerivedFrom
      - source: fideo
        relation_type: prov:wasDerivedFrom
      - source: foodon
        relation_type: prov:wasDerivedFrom
      - source: gencc
        relation_type: prov:wasDerivedFrom
      - source: go
        relation_type: prov:wasDerivedFrom
      - source: gwascatalog
        relation_type: prov:wasDerivedFrom
      - source: hetionet
        relation_type: prov:wasDerivedFrom
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: hippie
        relation_type: prov:wasDerivedFrom
      - source: hmdb
        relation_type: prov:wasDerivedFrom
      - source: hp
        relation_type: prov:wasDerivedFrom
      - source: iid
        relation_type: prov:wasDerivedFrom
      - source: iptmnet
        relation_type: prov:wasDerivedFrom
      - source: markerdb
        relation_type: prov:wasDerivedFrom
      - source: med-rt
        relation_type: prov:wasDerivedFrom
      - source: mirbase
        relation_type: prov:wasDerivedFrom
      - source: mondo
        relation_type: prov:wasDerivedFrom
      - source: ncbigene
        relation_type: prov:wasDerivedFrom
      - source: ndfrt
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: pathway-commons
        relation_type: prov:wasDerivedFrom
      - source: pharmgkb
        relation_type: prov:wasDerivedFrom
      - source: ptmd
        relation_type: prov:wasDerivedFrom
      - source: pubchem
        relation_type: prov:wasDerivedFrom
      - source: qptm
        relation_type: prov:wasDerivedFrom
      - source: reactome
        relation_type: prov:wasDerivedFrom
      - source: refseq
        relation_type: prov:wasDerivedFrom
      - source: rnadisease
        relation_type: prov:wasDerivedFrom
      - source: rnainter
        relation_type: prov:wasDerivedFrom
      - source: sider
        relation_type: prov:wasDerivedFrom
      - source: smpdb
        relation_type: prov:wasDerivedFrom
      - source: ttd
        relation_type: prov:wasDerivedFrom
      - source: uberon
        relation_type: prov:wasDerivedFrom
      - source: uniprot
        relation_type: prov:wasDerivedFrom
      - source: wikipathways
        relation_type: prov:wasDerivedFrom
    product_file_size: 1942958027
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.json.gz/content
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 TSV release published on February 6, 2024.
    format: tsv
    id: pharmebinet.tsv
    latest_version: v2
    name: PharMeBINet TSV Release
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: adrecs
        relation_type: prov:wasDerivedFrom
      - source: aelous
        relation_type: prov:wasDerivedFrom
      - source: atc
        relation_type: prov:wasDerivedFrom
      - source: bindingdb
        relation_type: prov:wasDerivedFrom
      - source: biogrid
        relation_type: prov:wasDerivedFrom
      - source: cl
        relation_type: prov:wasDerivedFrom
      - source: chebi
        relation_type: prov:wasDerivedFrom
      - source: clinvar
        relation_type: prov:wasDerivedFrom
      - source: ctd
        relation_type: prov:wasDerivedFrom
      - source: dbsnp
        relation_type: prov:wasDerivedFrom
      - source: ddinter
        relation_type: prov:wasDerivedFrom
      - source: doid
        relation_type: prov:wasDerivedFrom
      - source: diseases
        relation_type: prov:wasDerivedFrom
      - source: disgenet
        relation_type: prov:wasDerivedFrom
      - source: drugbank
        relation_type: prov:wasDerivedFrom
      - source: drugcentral
        relation_type: prov:wasDerivedFrom
      - source: efo
        relation_type: prov:wasDerivedFrom
      - source: fideo
        relation_type: prov:wasDerivedFrom
      - source: foodon
        relation_type: prov:wasDerivedFrom
      - source: gencc
        relation_type: prov:wasDerivedFrom
      - source: go
        relation_type: prov:wasDerivedFrom
      - source: gwascatalog
        relation_type: prov:wasDerivedFrom
      - source: hetionet
        relation_type: prov:wasDerivedFrom
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: hippie
        relation_type: prov:wasDerivedFrom
      - source: hmdb
        relation_type: prov:wasDerivedFrom
      - source: hp
        relation_type: prov:wasDerivedFrom
      - source: iid
        relation_type: prov:wasDerivedFrom
      - source: iptmnet
        relation_type: prov:wasDerivedFrom
      - source: markerdb
        relation_type: prov:wasDerivedFrom
      - source: med-rt
        relation_type: prov:wasDerivedFrom
      - source: mirbase
        relation_type: prov:wasDerivedFrom
      - source: mondo
        relation_type: prov:wasDerivedFrom
      - source: ncbigene
        relation_type: prov:wasDerivedFrom
      - source: ndfrt
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: pathway-commons
        relation_type: prov:wasDerivedFrom
      - source: pharmgkb
        relation_type: prov:wasDerivedFrom
      - source: ptmd
        relation_type: prov:wasDerivedFrom
      - source: pubchem
        relation_type: prov:wasDerivedFrom
      - source: qptm
        relation_type: prov:wasDerivedFrom
      - source: reactome
        relation_type: prov:wasDerivedFrom
      - source: refseq
        relation_type: prov:wasDerivedFrom
      - source: rnadisease
        relation_type: prov:wasDerivedFrom
      - source: rnainter
        relation_type: prov:wasDerivedFrom
      - source: sider
        relation_type: prov:wasDerivedFrom
      - source: smpdb
        relation_type: prov:wasDerivedFrom
      - source: ttd
        relation_type: prov:wasDerivedFrom
      - source: uberon
        relation_type: prov:wasDerivedFrom
      - source: uniprot
        relation_type: prov:wasDerivedFrom
      - source: wikipathways
        relation_type: prov:wasDerivedFrom
    product_file_size: 1922614551
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_tsv_24_02_06.zip/content
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 GraphML release published on February 6, 2024.
    format: mixed
    id: pharmebinet.graphml
    latest_version: v2
    name: PharMeBINet GraphML Release
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: adrecs
        relation_type: prov:wasDerivedFrom
      - source: aelous
        relation_type: prov:wasDerivedFrom
      - source: atc
        relation_type: prov:wasDerivedFrom
      - source: bindingdb
        relation_type: prov:wasDerivedFrom
      - source: biogrid
        relation_type: prov:wasDerivedFrom
      - source: cl
        relation_type: prov:wasDerivedFrom
      - source: chebi
        relation_type: prov:wasDerivedFrom
      - source: clinvar
        relation_type: prov:wasDerivedFrom
      - source: ctd
        relation_type: prov:wasDerivedFrom
      - source: dbsnp
        relation_type: prov:wasDerivedFrom
      - source: ddinter
        relation_type: prov:wasDerivedFrom
      - source: doid
        relation_type: prov:wasDerivedFrom
      - source: diseases
        relation_type: prov:wasDerivedFrom
      - source: disgenet
        relation_type: prov:wasDerivedFrom
      - source: drugbank
        relation_type: prov:wasDerivedFrom
      - source: drugcentral
        relation_type: prov:wasDerivedFrom
      - source: efo
        relation_type: prov:wasDerivedFrom
      - source: fideo
        relation_type: prov:wasDerivedFrom
      - source: foodon
        relation_type: prov:wasDerivedFrom
      - source: gencc
        relation_type: prov:wasDerivedFrom
      - source: go
        relation_type: prov:wasDerivedFrom
      - source: gwascatalog
        relation_type: prov:wasDerivedFrom
      - source: hetionet
        relation_type: prov:wasDerivedFrom
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: hippie
        relation_type: prov:wasDerivedFrom
      - source: hmdb
        relation_type: prov:wasDerivedFrom
      - source: hp
        relation_type: prov:wasDerivedFrom
      - source: iid
        relation_type: prov:wasDerivedFrom
      - source: iptmnet
        relation_type: prov:wasDerivedFrom
      - source: markerdb
        relation_type: prov:wasDerivedFrom
      - source: med-rt
        relation_type: prov:wasDerivedFrom
      - source: mirbase
        relation_type: prov:wasDerivedFrom
      - source: mondo
        relation_type: prov:wasDerivedFrom
      - source: ncbigene
        relation_type: prov:wasDerivedFrom
      - source: ndfrt
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: pathway-commons
        relation_type: prov:wasDerivedFrom
      - source: pharmgkb
        relation_type: prov:wasDerivedFrom
      - source: ptmd
        relation_type: prov:wasDerivedFrom
      - source: pubchem
        relation_type: prov:wasDerivedFrom
      - source: qptm
        relation_type: prov:wasDerivedFrom
      - source: reactome
        relation_type: prov:wasDerivedFrom
      - source: refseq
        relation_type: prov:wasDerivedFrom
      - source: rnadisease
        relation_type: prov:wasDerivedFrom
      - source: rnainter
        relation_type: prov:wasDerivedFrom
      - source: sider
        relation_type: prov:wasDerivedFrom
      - source: smpdb
        relation_type: prov:wasDerivedFrom
      - source: ttd
        relation_type: prov:wasDerivedFrom
      - source: uberon
        relation_type: prov:wasDerivedFrom
      - source: uniprot
        relation_type: prov:wasDerivedFrom
      - source: wikipathways
        relation_type: prov:wasDerivedFrom
    product_file_size: 2027519087
    product_url: https://zenodo.org/api/records/17814889/files/PharMeBiNet_graphml_24_02_06.zip/content
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 Neo4j database release published on February 6, 2024.
    format: neo4j
    id: pharmebinet.neo4j
    latest_version: v2
    name: PharMeBINet Neo4j Database
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: adrecs
        relation_type: prov:wasDerivedFrom
      - source: aelous
        relation_type: prov:wasDerivedFrom
      - source: atc
        relation_type: prov:wasDerivedFrom
      - source: bindingdb
        relation_type: prov:wasDerivedFrom
      - source: biogrid
        relation_type: prov:wasDerivedFrom
      - source: cl
        relation_type: prov:wasDerivedFrom
      - source: chebi
        relation_type: prov:wasDerivedFrom
      - source: clinvar
        relation_type: prov:wasDerivedFrom
      - source: ctd
        relation_type: prov:wasDerivedFrom
      - source: dbsnp
        relation_type: prov:wasDerivedFrom
      - source: ddinter
        relation_type: prov:wasDerivedFrom
      - source: doid
        relation_type: prov:wasDerivedFrom
      - source: diseases
        relation_type: prov:wasDerivedFrom
      - source: disgenet
        relation_type: prov:wasDerivedFrom
      - source: drugbank
        relation_type: prov:wasDerivedFrom
      - source: drugcentral
        relation_type: prov:wasDerivedFrom
      - source: efo
        relation_type: prov:wasDerivedFrom
      - source: fideo
        relation_type: prov:wasDerivedFrom
      - source: foodon
        relation_type: prov:wasDerivedFrom
      - source: gencc
        relation_type: prov:wasDerivedFrom
      - source: go
        relation_type: prov:wasDerivedFrom
      - source: gwascatalog
        relation_type: prov:wasDerivedFrom
      - source: hetionet
        relation_type: prov:wasDerivedFrom
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: hippie
        relation_type: prov:wasDerivedFrom
      - source: hmdb
        relation_type: prov:wasDerivedFrom
      - source: hp
        relation_type: prov:wasDerivedFrom
      - source: iid
        relation_type: prov:wasDerivedFrom
      - source: iptmnet
        relation_type: prov:wasDerivedFrom
      - source: markerdb
        relation_type: prov:wasDerivedFrom
      - source: med-rt
        relation_type: prov:wasDerivedFrom
      - source: mirbase
        relation_type: prov:wasDerivedFrom
      - source: mondo
        relation_type: prov:wasDerivedFrom
      - source: ncbigene
        relation_type: prov:wasDerivedFrom
      - source: ndfrt
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: pathway-commons
        relation_type: prov:wasDerivedFrom
      - source: pharmgkb
        relation_type: prov:wasDerivedFrom
      - source: ptmd
        relation_type: prov:wasDerivedFrom
      - source: pubchem
        relation_type: prov:wasDerivedFrom
      - source: qptm
        relation_type: prov:wasDerivedFrom
      - source: reactome
        relation_type: prov:wasDerivedFrom
      - source: refseq
        relation_type: prov:wasDerivedFrom
      - source: rnadisease
        relation_type: prov:wasDerivedFrom
      - source: rnainter
        relation_type: prov:wasDerivedFrom
      - source: sider
        relation_type: prov:wasDerivedFrom
      - source: smpdb
        relation_type: prov:wasDerivedFrom
      - source: ttd
        relation_type: prov:wasDerivedFrom
      - source: uberon
        relation_type: prov:wasDerivedFrom
      - source: uniprot
        relation_type: prov:wasDerivedFrom
      - source: wikipathways
        relation_type: prov:wasDerivedFrom
    product_file_size: 3847978577
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.zip/content
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 Neo4j dump release published on February 6, 2024.
    dump_format: neo4j
    format: neo4j
    id: pharmebinet.neo4j.dump
    latest_version: v2
    name: PharMeBINet Neo4j Dump
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: adrecs
        relation_type: prov:wasDerivedFrom
      - source: aelous
        relation_type: prov:wasDerivedFrom
      - source: atc
        relation_type: prov:wasDerivedFrom
      - source: bindingdb
        relation_type: prov:wasDerivedFrom
      - source: biogrid
        relation_type: prov:wasDerivedFrom
      - source: cl
        relation_type: prov:wasDerivedFrom
      - source: chebi
        relation_type: prov:wasDerivedFrom
      - source: clinvar
        relation_type: prov:wasDerivedFrom
      - source: ctd
        relation_type: prov:wasDerivedFrom
      - source: dbsnp
        relation_type: prov:wasDerivedFrom
      - source: ddinter
        relation_type: prov:wasDerivedFrom
      - source: doid
        relation_type: prov:wasDerivedFrom
      - source: diseases
        relation_type: prov:wasDerivedFrom
      - source: disgenet
        relation_type: prov:wasDerivedFrom
      - source: drugbank
        relation_type: prov:wasDerivedFrom
      - source: drugcentral
        relation_type: prov:wasDerivedFrom
      - source: efo
        relation_type: prov:wasDerivedFrom
      - source: fideo
        relation_type: prov:wasDerivedFrom
      - source: foodon
        relation_type: prov:wasDerivedFrom
      - source: gencc
        relation_type: prov:wasDerivedFrom
      - source: go
        relation_type: prov:wasDerivedFrom
      - source: gwascatalog
        relation_type: prov:wasDerivedFrom
      - source: hetionet
        relation_type: prov:wasDerivedFrom
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: hippie
        relation_type: prov:wasDerivedFrom
      - source: hmdb
        relation_type: prov:wasDerivedFrom
      - source: hp
        relation_type: prov:wasDerivedFrom
      - source: iid
        relation_type: prov:wasDerivedFrom
      - source: iptmnet
        relation_type: prov:wasDerivedFrom
      - source: markerdb
        relation_type: prov:wasDerivedFrom
      - source: med-rt
        relation_type: prov:wasDerivedFrom
      - source: mirbase
        relation_type: prov:wasDerivedFrom
      - source: mondo
        relation_type: prov:wasDerivedFrom
      - source: ncbigene
        relation_type: prov:wasDerivedFrom
      - source: ndfrt
        relation_type: prov:wasDerivedFrom
      - source: omim
        relation_type: prov:wasDerivedFrom
      - source: pathway-commons
        relation_type: prov:wasDerivedFrom
      - source: pharmgkb
        relation_type: prov:wasDerivedFrom
      - source: ptmd
        relation_type: prov:wasDerivedFrom
      - source: pubchem
        relation_type: prov:wasDerivedFrom
      - source: qptm
        relation_type: prov:wasDerivedFrom
      - source: reactome
        relation_type: prov:wasDerivedFrom
      - source: refseq
        relation_type: prov:wasDerivedFrom
      - source: rnadisease
        relation_type: prov:wasDerivedFrom
      - source: rnainter
        relation_type: prov:wasDerivedFrom
      - source: sider
        relation_type: prov:wasDerivedFrom
      - source: smpdb
        relation_type: prov:wasDerivedFrom
      - source: ttd
        relation_type: prov:wasDerivedFrom
      - source: uberon
        relation_type: prov:wasDerivedFrom
      - source: uniprot
        relation_type: prov:wasDerivedFrom
      - source: wikipathways
        relation_type: prov:wasDerivedFrom
    product_file_size: 3598325722
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_dump_24_02_06.zip/content
  - category: DocumentationProduct
    description: Data sources documentation page describing the upstream resources integrated into PharMeBINet.
    format: http
    id: pharmebinet.data-sources
    name: PharMeBINet Data Sources
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_url: https://pharmebi.net/#/datasources
publications:
  - doi: doi:10.1038/s41597-022-01510-3
    id: https://doi.org/10.1038/s41597-022-01510-3
    journal: Scientific Data
    preferred: true
    title: The heterogeneous pharmacological medical biochemical network PharMeBINet
    year: '2022'
repository: https://github.com/ckoenigs/PharMeBINet
---

# PharMeBINet

PharMeBINet is a large heterogeneous biomedical knowledge graph centered on pharmacology and adverse drug reaction analysis. The project integrates many biomedical resources into a graph database and provides both a public web interface and versioned releases in JSON, TSV, GraphML, and Neo4j formats for downstream analysis.
