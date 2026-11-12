---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cuiqinghua@hsc.pku.edu.cn
  - contact_type: url
    value: http://www.cuilab.cn/
  label: Qinghua Cui
creation_date: '2026-11-12T00:00:00Z'
description: The Human microRNA Disease Database (HMDD) is a manually curated database
  of experimentally supported associations between human microRNAs (miRNAs) and diseases,
  curated from the literature. Each entry records the miRNA, the disease, the supporting
  PubMed reference, and a description of the evidence, classified into evidence categories
  such as genetics, epigenetics, circulating miRNAs, miRNA-target interactions, tissue
  expression, exosomal miRNAs, and virus-encoded miRNAs. HMDD v4.0 (released June
  2023) contains 53,530 miRNA-disease association entries covering 1,817 human miRNA
  genes, 79 virus-derived miRNAs, and 2,360 diseases from 37,090 papers.
domains:
- genomics
- non-coding RNA
- gene regulation
- biomedical
homepage_url: http://www.cuilab.cn/hmdd
id: hmdd
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: http://www.cuilab.cn/hmdd
  label: Custom (free for academic use only; commercial use requires permission)
name: Human microRNA Disease Database (HMDD)
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching miRNA-disease associations,
    with tools for miRNA-target network visualization, causality annotations, and
    disease network analysis.
  format: http
  id: hmdd.portal
  is_public: true
  name: HMDD Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hmdd
  product_url: http://www.cuilab.cn/hmdd
- category: Product
  description: Tab-delimited table of all HMDD v4.0 miRNA-disease association entries,
    with evidence code, PubMed ID, miRNA name, disease name, and a description of
    the supporting evidence. MiRNA names follow miRBase nomenclature and disease names
    follow MeSH.
  format: tsv
  id: hmdd.alldata
  is_public: true
  latest_version: v4.0
  name: HMDD v4.0 All Association Data (text)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hmdd
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 12849414
  product_url: http://www.cuilab.cn/static/hmdd3/data/alldata_v4.txt
- category: Product
  description: Excel version of the full HMDD v4.0 miRNA-disease association table.
  format: xlsx
  id: hmdd.alldata-xlsx
  is_public: true
  latest_version: v4.0
  name: HMDD v4.0 All Association Data (Excel)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hmdd
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_file_size: 5674249
  product_url: http://www.cuilab.cn/static/hmdd3/data/alldata_v4.xlsx
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
  - Chunmei Cui
  - Bitao Zhong
  - Rui Fan
  - Qinghua Cui
  doi: 10.1093/nar/gkad717
  id: doi:10.1093/nar/gkad717
  journal: Nucleic Acids Research
  preferred: true
  title: 'HMDD v4.0: a database for experimentally supported human microRNA-disease
    associations'
  year: '2024'
- authors:
  - Zhou Huang
  - Jiangcheng Shi
  - Yuanxu Gao
  - Chunmei Cui
  doi: 10.1093/nar/gky1010
  id: doi:10.1093/nar/gky1010
  journal: Nucleic Acids Research
  title: 'HMDD v3.0: a database for experimentally supported human microRNA–disease
    associations'
  year: '2019'
taxon:
- NCBITaxon:9606
---
# Human microRNA Disease Database (HMDD)

HMDD is a manually curated database of experimentally supported associations between human microRNAs and diseases, maintained by the Qinghua Cui lab at Peking University Health Science Center. First released in December 2007, it records for each entry the miRNA, the disease, the PubMed reference, and the evidence from the original paper, grouped into evidence categories and codes (8 categories and 23 evidence codes in v4.0).

HMDD v4.0 (Cui et al., Nucleic Acids Research 2024; published online 2023) contains 53,530 miRNA-disease association entries, about 1.5 times as many as v3.0, and adds categories for exosomal miRNAs and virus-encoded miRNAs, along with disease network analysis and curation of sex-biased miRNAs. The full association table is available as tab-delimited text and Excel files. The site states that HMDD data are free only for academic use, and commercial use requires contacting Dr. Qinghua Cui.
