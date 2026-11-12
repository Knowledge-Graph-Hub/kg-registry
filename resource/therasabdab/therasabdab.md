---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: opig@stats.ox.ac.uk
  - contact_type: url
    value: https://opig.stats.ox.ac.uk/
  label: Oxford Protein Informatics Group (OPIG)
creation_date: '2026-11-12T00:00:00Z'
description: The Therapeutic Structural Antibody Database (Thera-SAbDab) tracks all
  antibody- and nanobody-derived therapeutics recognized by the World Health Organization
  International Nonproprietary Names (INN) programme, recording their variable domain
  sequences together with format, isotype, targets, companies, approved and investigated
  conditions, and highest clinical trial stage. Each therapeutic is linked to its
  exact (100% sequence identity) and near (95-99%) structural representatives in SAbDab,
  and these structural mappings are refreshed alongside SAbDab's weekly updates. New
  therapeutics are added with each WHO INN list, and clinical status is updated from
  AdisInsight.
domains:
- immunology
- pharmacology
- drug discovery
- proteomics
- protein structure
homepage_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/therasabdab
id: therasabdab
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: Therapeutic Structural Antibody Database (Thera-SAbDab)
products:
- category: GraphicalInterface
  description: Thera-SAbDab search interface for finding therapeutic antibodies by
    INN, target, format, clinical stage or sequence similarity, with summary pages
    linking each therapeutic to its matching SAbDab structures.
  format: http
  id: therasabdab.portal
  name: Thera-SAbDab Search Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: sabdab
  product_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/therasabdab/search/
- category: Product
  description: CSV table of all Thera-SAbDab therapeutics with format, isotype, clinical
    trial stage and status, heavy and light chain variable domain sequences, matching
    SAbDab structures at 100%, 99% and 95-98% sequence identity, INN proposal and
    recommendation years, targets, companies and conditions.
  format: csv
  id: therasabdab.sequences-structures
  name: Thera-SAbDab Sequences and Structures Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_file_size: 636357
  product_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/static/downloads/TheraSAbDab_SeqStruc_OnlineDownload.csv
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
  - Raybould MIJ
  - Marks C
  - Lewis AP
  - Shi J
  - Bujotzek A
  - Taddese B
  - Deane CM
  doi: 10.1093/nar/gkz827
  id: doi:10.1093/nar/gkz827
  journal: Nucleic Acids Research
  preferred: true
  title: 'Thera-SAbDab: the Therapeutic Structural Antibody Database'
  year: '2020'
rrid: SCR_022093
---
# Therapeutic Structural Antibody Database (Thera-SAbDab)

Thera-SAbDab is a database of antibody and nanobody therapeutics recognized by the WHO INN programme, built by the Oxford Protein Informatics Group (OPIG) under an open-innovation agreement. It records the variable domain sequences and clinical metadata of each therapeutic and maps them to exact and near-identical structures in the Structural Antibody Database (SAbDab), which in turn draws from the Protein Data Bank.

The full therapeutic table can be downloaded as CSV or Excel from the search page. The Thera-SAbDab pages state no data license.
