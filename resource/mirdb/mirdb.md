---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: miRDB is an online database for microRNA (miRNA) target prediction and
  functional annotations. Targets are predicted by MirTarget, a computational tool
  trained on thousands of miRNA-target interactions from high-throughput sequencing
  experiments. The database covers millions of predicted targets regulated by thousands
  of miRNAs across human, mouse, rat, dog, and chicken, and supports target prediction
  by miRNA, by gene, and for user-provided custom sequences.
domains:
- genomics
homepage_url: https://mirdb.org/
id: mirdb
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
name: miRDB
products:
- category: Product
  description: Compressed plain-text file of all predicted miRNA targets generated
    with the MirTarget prediction tool, covering the miRNAs and genes in the current
    miRDB release.
  format: txt
  id: mirdb.predicted-targets
  name: miRDB Predicted Targets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirdb
  product_url: https://mirdb.org/download.html
- category: GraphicalInterface
  description: Web interface for searching predicted miRNA targets by miRNA name or
    gene, performing custom target prediction on user-provided sequences, and browsing
    functional annotations.
  format: http
  id: mirdb.search
  name: miRDB Search Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirdb
  product_url: https://mirdb.org/
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
publications:
- authors:
  - Yuhao Chen
  - Xiaowei Wang
  doi: doi:10.1093/nar/gkz757
  id: doi:10.1093/nar/gkz757
  journal: Nucleic Acids Research
  preferred: true
  title: 'miRDB: an online database for prediction of functional microRNA targets'
  year: '2020'
---
# miRDB

miRDB is an online database for microRNA (miRNA) target prediction and functional
annotations. Predicted targets are generated by MirTarget, a computational tool
developed by analyzing thousands of miRNA-target interactions derived from
high-throughput sequencing experiments.

The database provides millions of predicted targets regulated by thousands of
miRNAs across human, mouse, rat, dog, and chicken. Users can search for predicted
targets by miRNA name or by gene, run custom target prediction on their own
sequences, and download the full set of predicted miRNA-target interactions.