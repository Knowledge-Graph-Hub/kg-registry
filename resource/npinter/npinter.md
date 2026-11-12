---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: heshunmin@ibp.ac.cn
  label: Shunmin He
- category: Organization
  contact_details:
  - contact_type: email
    value: zhengyu181@mails.ucas.ac.cn
  - contact_type: url
    value: http://bigdata.ibp.ac.cn/npinter5/about/
  label: Key Laboratory of RNA Biology, Institute of Biophysics, Chinese Academy of
    Sciences
creation_date: '2026-11-12T00:00:00Z'
description: NPInter is a database of functional interactions between non-coding RNAs
  (excluding tRNAs and rRNAs) and other biomolecules, including proteins, RNAs and
  genomic DNA. Version 5.0 holds about 2.6 million ncRNA interactions across 60 species,
  drawn from manual curation of the literature and from high-throughput experiments
  such as CLIP-seq in GEO, plus over 8 million RNA-DNA interaction pairs from iMARGI,
  ChAR-seq and GRID-seq data. It adds an RNA-binding protein module covering 277 human
  RBPs, a panel of SARS-CoV-2-related RNA interactions, and cell-type-specific lncRNA
  interactions inferred from single-cell RNA-seq. Molecules are identified with NONCODE,
  miRBase, circBase, Ensembl, RefSeq and UniProt identifiers.
domains:
- genomics
- non-coding RNA
- proteomics
- protein interactions
homepage_url: http://bigdata.ibp.ac.cn/npinter5/
id: npinter
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: NPInter
products:
- category: GraphicalInterface
  description: NPInter v5.0 web portal for browsing and searching ncRNA interactions,
    ncRNA-genome bindings, RBPs, SARS-CoV-2 RNA interactions and single-cell lncRNA
    interactions, with functional search and BLAST.
  format: http
  id: npinter.portal
  name: NPInter v5.0 Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npinter
  product_url: http://bigdata.ibp.ac.cn/npinter5/
- category: Product
  description: Download page for NPInter interaction, binding site and RNA-DNA interaction
    files, including files from earlier NPInter versions.
  format: http
  id: npinter.downloads
  name: NPInter Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npinter
  product_url: http://bigdata.ibp.ac.cn/npinter5/download/
- category: GraphProduct
  compression: gzip
  description: All NPInter v5.0 ncRNA interactions (literature-curated, high-throughput
    and computational) as a gzipped tab-delimited table of ncRNA, partner, interaction
    class, level, experiment, data source, organism, tissue or cell, and PubMed IDs.
  format: tsv
  id: npinter.interactions
  latest_version: '5.0'
  name: NPInter v5.0 All Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ensembl
  product_file_size: 43319525
  product_url: http://bigdata.ibp.ac.cn/npinter5/download/file/interaction_NPInterv5.txt.gz
- category: GraphProduct
  compression: gzip
  description: Experimentally validated NPInter v5.0 ncRNA interactions as a gzipped
    tab-delimited table.
  format: tsv
  id: npinter.interactions-experimental
  latest_version: '5.0'
  name: NPInter v5.0 Experimentally Validated Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  product_file_size: 704301
  product_url: http://bigdata.ibp.ac.cn/npinter5/download/file/interaction_NPInterv5.expr.txt.gz
- category: GraphProduct
  compression: gzip
  description: Computationally predicted NPInter v5.0 ncRNA interactions as a gzipped
    tab-delimited table.
  format: tsv
  id: npinter.interactions-predicted
  latest_version: '5.0'
  name: NPInter v5.0 Computationally Predicted Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npinter
  product_file_size: 42613351
  product_url: http://bigdata.ibp.ac.cn/npinter5/download/file/interaction_NPInterv5.comp.txt.gz
- category: Product
  compression: gzip
  description: NPInter v5.0 ncRNA binding sites as a gzipped tab-delimited table.
  format: tsv
  id: npinter.binding-sites
  latest_version: '5.0'
  name: NPInter v5.0 Binding Sites
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npinter
  product_url: http://bigdata.ibp.ac.cn/npinter5/download/file/bindingsite_NPInterv5.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-11-12: Error connecting
    to URL: (''Connection aborted.'', RemoteDisconnected(''Remote end closed connection
    without response''))'
- category: GraphProduct
  compression: gzip
  description: Genome-wide RNA-DNA interactions collected by NPInter v5.0 from iMARGI,
    ChAR-seq and GRID-seq datasets, as a gzipped tab-delimited table.
  format: tsv
  id: npinter.rna-dna-interactions
  latest_version: '5.0'
  name: NPInter v5.0 RNA-DNA Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  product_url: http://bigdata.ibp.ac.cn/npinter5/download/file/dna_interactions.npinter5.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-11-12: Error connecting
    to URL: (''Connection aborted.'', RemoteDisconnected(''Remote end closed connection
    without response''))'
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
    source: alliance
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
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: civic
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
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: drugcentral
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
    source: faers
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hmdd
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mavedb
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
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panelapp
  - relation_type: prov:hadPrimarySource
    source: pangolin
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
    source: revel
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: saprot
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://sugi.bio/biobtree/api/
publications:
- authors:
  - Zheng Y
  - Luo H
  - Teng X
  - Hao X
  - Yan X
  - Tang Y
  - Zhang W
  - Wang Y
  - Zhang P
  - Li Y
  - Zhao Y
  - Chen R
  - He S
  doi: 10.1093/nar/gkac1002
  id: doi:10.1093/nar/gkac1002
  journal: Nucleic Acids Research
  preferred: true
  title: 'NPInter v5.0: ncRNA interaction database in a new era'
  year: '2023'
- authors:
  - Teng X
  - Chen X
  - Xue H
  - Tang Y
  - Zhang P
  - Kang Q
  - Hao Y
  - Chen R
  - Zhao Y
  - He S
  doi: 10.1093/nar/gkz969
  id: doi:10.1093/nar/gkz969
  journal: Nucleic Acids Research
  title: 'NPInter v4.0: an integrated database of ncRNA interactions'
  year: '2019'
rrid: SCR_007825
---
# NPInter

NPInter documents experimentally supported functional interactions between non-coding RNAs (other than tRNAs and rRNAs) and proteins, RNAs and DNA. It is maintained by the Key Laboratory of RNA Biology at the Institute of Biophysics, Chinese Academy of Sciences, and has been released in versions since 2006; version 5.0 (2022) roughly doubled the interaction count and added RNA-DNA interactions, an RBP module, SARS-CoV-2 RNA interactions and single-cell lncRNA interactions.

All interaction files are freely downloadable as gzipped tab-delimited text. The website and papers state no data license (the v5.0 paper itself is CC BY 4.0).