---
activity_status: active
category: DataSource
creation_date: '2025-11-13T00:00:00Z'
description: iPTMnet is an integrated resource for protein post-translational modification
  (PTM) network discovery that employs an integrative bioinformatics approach combining
  text mining, data mining, and ontological representation to capture rich PTM information,
  including PTM enzyme-substrate-site relationships, PTM-specific protein-protein
  interactions (PPIs), and PTM conservation across species.
domains:
- proteomics
homepage_url: https://research.bioinformatics.udel.edu/iptmnet/
id: iptmnet
infores_id: iptmnet
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: iPTMnet
products:
- category: GraphicalInterface
  description: iPTMnet web portal for searching PTM proteins, enzymes, substrates,
    PTM sites, PTM-dependent interactions, literature evidence, and cross-species
    PTM conservation.
  format: http
  id: iptmnet.portal
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC BY-NC-SA 4.0
  name: iPTMnet Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_url: https://research.bioinformatics.udel.edu/iptmnet/
- category: GraphProduct
  description: Current iPTMnet PTM record table with PTM type, source, UniProt protein,
    organism, site, enzyme, relation identifiers, and publication evidence.
  format: tsv
  id: iptmnet.ptm
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC BY-NC-SA 4.0
  name: iPTMnet PTM Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_file_size: 44116546
  product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/ptm.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dbptm
  - relation_type: prov:wasDerivedFrom
    source: dbsno
  - relation_type: prov:wasDerivedFrom
    source: efip
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: nextprot
  - relation_type: prov:wasDerivedFrom
    source: p3db
  - relation_type: prov:wasDerivedFrom
    source: phosphoelm
  - relation_type: prov:wasDerivedFrom
    source: phosphogrid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: phosphat
  - relation_type: prov:wasDerivedFrom
    source: pombase
  - relation_type: prov:wasDerivedFrom
    source: pubtator
  - relation_type: prov:wasDerivedFrom
    source: rlims-p
  - relation_type: prov:wasDerivedFrom
    source: signor
  - relation_type: prov:wasDerivedFrom
    source: uniprot
- category: Product
  description: Current iPTMnet confidence score table for PTM site records.
  format: tsv
  id: iptmnet.score
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC BY-NC-SA 4.0
  name: iPTMnet Score Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_file_size: 26110370
  product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/score.txt
- category: Product
  description: Current iPTMnet protein table with UniProt accessions, names, organism
    labels, and reviewed/unreviewed status.
  format: tsv
  id: iptmnet.protein
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC BY-NC-SA 4.0
  name: iPTMnet Protein Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_file_size: 9324847
  product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/protein.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: uniprot
- category: DocumentationProduct
  description: README for the current iPTMnet downloadable PTM, score, and protein
    tables.
  format: txt
  id: iptmnet.download.readme
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC BY-NC-SA 4.0
  name: iPTMnet Download README
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_file_size: 1892
  product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/readme.txt
- category: ProgrammingInterface
  connection_url: https://research.bioinformatics.udel.edu/iptmnet/api/
  description: RESTful API for retrieving iPTMnet PTM data, with Swagger documentation
    and companion R/Python client packages.
  format: json
  id: iptmnet.api
  is_public: true
  name: iPTMnet REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_url: https://research.bioinformatics.udel.edu/iptmnet/api/doc/
- category: ProgrammingInterface
  description: R client documentation for accessing the iPTMnet REST API.
  format: http
  id: iptmnet.r_client
  is_public: true
  name: iPTMnetR
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_url: https://udel-cbcb.github.io/iPTMnetR/#/
- category: ProgrammingInterface
  description: Python client documentation for accessing the iPTMnet REST API.
  format: http
  id: iptmnet.python_client
  is_public: true
  name: pyiPTMnet
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_url: https://udel-cbcb.github.io/pyiPTMnet/
- category: GraphicalInterface
  description: Interactive Shiny web interface for exploring and visualizing human
    kinase-substrate interactions
  format: http
  id: kinace.portal
  name: KiNet Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kinace
  product_url: https://kinet.kinametrix.com/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: coralkinome
  - relation_type: prov:wasDerivedFrom
    source: darkkinasekb
  - relation_type: prov:wasDerivedFrom
    source: epsd
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: kinhub
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: uniprot
- category: GraphProduct
  description: iPTMnet protein has site edges
  format: csv
  id: prokn.iptmnet.protein.has_site.site.edges
  name: ProKN iPTMnet Protein Site Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 34132692
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/iPTMnet.Protein.HAS_SITE.Site.edges.csv
- category: GraphProduct
  description: iPTMnet protein catalyzes PTM site edges
  format: csv
  id: prokn.iptmnet.protein.catalyzes.ptmsite.edges
  name: ProKN iPTMnet Protein Catalyzes PTM Site Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4049194
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/iPTMnet.Protein.CATALYZES.PTMSite.edges.csv
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
    source: pathway-commons
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
    source: pathway-commons
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
    source: pathway-commons
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
    source: pathway-commons
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
    source: pathway-commons
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
- category: Product
  description: Download page for complete phosphorylation site datasets and annotation
    data from EPSD 2.0
  format: http
  id: epsd.download
  name: EPSD Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epsd
  product_url: https://epsd.biocuckoo.cn/Download.php
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
- category: GraphProduct
  description: CSV download of the full KiNet human kinase-substrate interaction dataset
    with source database, evidence, and PMID reference fields
  format: csv
  id: kinace.interactions
  name: KiNet Full Interaction Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kinace
  product_file_size: 5180792
  product_url: https://raw.githubusercontent.com/GauravPandeyLab/KiNet/master/data/ksi_source_full_dataset.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: epsd
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
publications:
- authors:
  - Hongzhan Huang
  - Cecilia N Arighi
  - Karen E Ross
  - Jia Ren
  - Gang Li
  - Sheng-Chih Chen
  - Qinghua Wang
  - Julie Cowart
  - K Vijay-Shanker
  - Cathy H Wu
  doi: 10.1093/nar/gkx1104
  id: doi:10.1093/nar/gkx1104
  journal: Nucleic Acids Research
  preferred: true
  title: 'iPTMnet: an integrated resource for protein post-translational modification
    network discovery'
  year: '2018'
synonyms: []
---
# iPTMnet

## Description
iPTMnet is an integrated resource for protein post-translational modification (PTM) network discovery that employs an integrative bioinformatics approach combining text mining, data mining, and ontological representation to capture rich PTM information, including PTM enzyme-substrate-site relationships, PTM-specific protein-protein interactions (PPIs), and PTM conservation across species.

## Coverage
As of Release 4.1 (August 2017), iPTMnet contains:

- **654,500+** unique PTM sites in over **62,100** modified proteins
- **1,200** PTM enzymes
- **12,700** distinct enzyme-substrate pairs
- **24,300** distinct enzyme-substrate-site combinations
- **1,470** PTM-dependent protein-protein interactions
- **30,500** publications describing PTM and/or PPI relations

### PTM Types Covered
Eight major PTM types:
1. Phosphorylation (primary)
2. Ubiquitination
3. Acetylation
4. Methylation
5. Glycosylation
6. S-nitrosylation
7. Sumoylation
8. Myristoylation

### Organisms
Top organisms represented:
- Human
- Mouse
- Rat
- Arabidopsis thaliana
- Saccharomyces cerevisiae
- Schizosaccharomyces pombe

## Data Sources

### Text Mining Systems
- **RLIMS-P**: Rule-based information extraction system for literature mining of protein phosphorylation information from PubMed abstracts and full-length articles
- **eFIP**: Full-scale mining of PubMed Central Open Access articles for phosphorylation information

### Curated Databases (11 sources integrated)
1. **PhosphoSitePlus (PSP)**: Phosphorylation, ubiquitination, acetylation, methylation (human, rat, mouse)
2. **Phospho.ELM**: Phosphorylation sites in animal proteins
3. **PhosPhAt**: Mass spectrometry phosphorylation sites in Arabidopsis thaliana
4. **PhosphoGrid**: In vivo phosphorylation sites in Saccharomyces cerevisiae
5. **PomBase**: Fission yeast (Schizosaccharomyces pombe) comprehensive database
6. **UniProtKB**: Comprehensive protein database with expert-annotated PTM features
7. **P3DB**: Plant protein phosphorylation data
8. **neXtProt**: Human protein knowledgebase with kinase focus
9. **HPRD**: Human protein PTMs and enzyme-substrate relationships
10. **Signor**: Causal relationships between biological entities including PTM-enzyme substrate relations
11. **dbSNO**: Experimentally verified cysteine S-nitrosylation sites

### Ontological Framework
- **Protein Ontology (PRO)**: Organizes proteins and PTM proteoforms with hierarchical representation (family→gene→sequence→modification) enabling representation of experimentally validated PTM combinations

## Key Features

### Unique Capabilities
1. **Proteoform Representation**: Shows experimentally validated combinations of PTMs on proteins (unique feature)
2. **PTM Conservation Analysis**: Alignment of orthologous proteoforms across species enabling PTM site and proteoform prediction
3. **Confidence Scoring**: Quality scores (0-4 stars) for PTM information based on source quality, multiple source support, and publication evidence
4. **Network Visualization**: Cytoscape-based PTM sites and proteoforms as nodes with enzyme-site and PPI relationships as edges
5. **Integrated Text Mining**: Up-to-date PTM information from automated monthly processing of all PubMed abstracts and PMC Open Access full-text articles

### Search & Browse Functionality
- Search by UniProtKB AC/ID, protein/gene name, PRO ID, PMID
- Restrict by PTM type, enzyme/substrate role, organism
- **Batch Retrieval**: Process up to 500 PTM sites at once to obtain PTM enzyme or PTM-dependent PPI information
- **Literature Search**: Dual search modes (protein database search + phosphorylation literature search)
- Interactive Entry Reports with multiple data tables (substrate, PTM enzyme, proteoform, PPI)

### Visualization Tools
1. **Cytoscape Network View**: Interactive network visualization of PTM enzyme-substrate-site, proteoform-site, and PPI relationships
2. **Sequence Alignment Viewer**: Multiple sequence alignment (MUSCLE algorithm) showing PTM conservation across species with color-coded modifications
3. **Overlapping PTMs**: Highlights residues with multiple modification types (potential PTM cross-talk sites)

### RESTful API
- Programmatic access to iPTMnet data
- Documented in Methods Mol Biol (2022) and Database (Oxford) (2020)
- Enables automated integration with external analysis workflows

## Quality Control
- Monthly updates of text mining results
- Integrity checks on kinase information (verification against UniProtKB 'kinase' keyword)
- PTM type validation (conformance to known residue types)
- PTM site sequence validation (residue at expected position in UniProtKB sequence)
- Monitoring for retracted articles with correction/removal of affected data

## Applications
- Functional interpretation of phosphoproteomic data
- Kinase signaling pathway analysis (e.g., connecting phosphosites from mass spec experiments to kinase pathways)
- PTM-dependent PPI discovery
- Cross-species PTM conservation studies
- Drug target identification (e.g., EGFR inhibitor erlotinib response analysis)
- Hypothesis generation for PTM cross-talk and proteoform biology

## Maintenance & Support
- Maintained by Protein Information Resource (PIR)
- University of Delaware: 15 Innovation Way, Suite 205, Newark, DE 19711
- Georgetown University Medical Center: 3300 Whitehaven Street, NW, Suite 1200, Washington, DC 20007
- Funding: NSF grant ABI-1062520, NIH/NIGMS grant U01GM120953
- Website traffic: >6 million hits from >16,000 unique IPs (first half of 2017)

## Technical Implementation
- Database: Oracle 12c release 1, dimensional model design
- Front-end: Django (Python Web Framework)
- Visualization: Cytoscape.js (version 2.4.2 graph theory library)
- Sequence Alignment: MUSCLE algorithm
- Text Mining: PubTator for NCBI gene ID mapping
- ID Mapping: UniProt Protein ID and gene name mapping tools

## Access & Documentation
- Main Portal: [https://research.bioinformatics.udel.edu/iptmnet/](https://research.bioinformatics.udel.edu/iptmnet/)
- Statistics: [http://research.bioinformatics.udel.edu/iptmnet/stat](http://research.bioinformatics.udel.edu/iptmnet/stat)
- Help Documentation: Available online (PDF)
- Tutorial: [http://research.bioinformatics.udel.edu/iptmnet/static/iptmnet/files/iPTMnet_Help.pdf](http://research.bioinformatics.udel.edu/iptmnet/static/iptmnet/files/iPTMnet_Help.pdf)
- API Documentation: See publications PMID:35696082 and PMID:32395768
- Europe PubMed Central Integration: External link tab connection for literature cross-referencing