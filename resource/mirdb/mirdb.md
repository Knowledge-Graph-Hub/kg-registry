---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://chicago.medicine.uic.edu/pharmacology/mcph-research/research-labs/wang-lab/
  - contact_type: url
    value: https://mirdb.org/comment.html
  label: Wang Lab, Department of Pharmacology and Regenerative Medicine, University
    of Illinois Chicago
- category: Individual
  contact_details:
  - contact_type: email
    value: xwang317@uic.edu
  label: Xiaowei Wang
creation_date: '2026-06-15T00:00:00Z'
description: miRDB is an online database for microRNA (miRNA) target prediction and
  functional annotations. Targets are predicted by MirTarget, a computational tool
  trained on thousands of miRNA-target interactions from high-throughput sequencing
  experiments. The database covers millions of predicted targets regulated by thousands
  of miRNAs across human, mouse, rat, dog, and chicken, and supports target prediction
  by miRNA, by gene, and for user-provided custom sequences.
domains:
- genomics
- non-coding RNA
funding:
- National Institutes of Health (NIH) (R01GM089784)
- National Institutes of Health (NIH) (R01DE026471)
homepage_url: https://mirdb.org/
id: mirdb
last_modified_date: '2026-11-12T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_url: https://mirdb.org/download.html
  warnings: []
- category: Product
  description: miRDB version 6.0 (June 2019) predicted miRNA targets for human, mouse,
    rat, dog and chicken, generated with MirTarget V4 using miRNA sequences from miRBase
    22, as a gzipped tab-delimited text file.
  format: txt
  id: mirdb.predicted-targets-v6
  name: miRDB v6.0 Predicted Targets File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 59483982
  product_url: https://mirdb.org/download/miRDB_v6.0_prediction_result.txt.gz
- category: GraphicalInterface
  description: Custom target prediction tool that runs MirTarget on a user-submitted
    miRNA sequence or mRNA target sequence for human, mouse, rat, dog or chicken.
  format: http
  id: mirdb.custom-prediction
  name: miRDB Custom Prediction
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirdb
  product_url: https://mirdb.org/custom.html
- category: GraphicalInterface
  description: FuncMir, a browsable collection of functional human and mouse precursor
    and mature miRNAs with links to their predicted targets.
  format: http
  id: mirdb.funcmir
  name: miRDB FuncMir Collection
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mirbase
  product_url: https://mirdb.org/FuncMir.html
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
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dailymed
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: fideo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: Product
  description: Downloadable gene set files in GMT, XML, and other formats for human
    collections including hallmarks, curated pathways, ontologies, and computational
    signatures; free registration is required for downloads
  format: mixed
  id: msigdb.downloads.human
  name: MSigDB Human Gene Sets Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: biocarta
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
  secondary_source:
  - relation_type: prov:used
    source: mirbase
  warnings:
  - Downloads redirect unauthenticated users to the GSEA/MSigDB login page; registration
    is free but required for direct file access.
- category: Product
  description: Downloadable gene set files for mouse collections including mouse-ortholog
    hallmarks, curated pathways, ontologies, and cell type signatures; free registration
    is required for downloads
  format: mixed
  id: msigdb.downloads.mouse
  name: MSigDB Mouse Gene Sets Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: gtrd
  - relation_type: prov:hadPrimarySource
    source: biocarta
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
  secondary_source:
  - relation_type: prov:used
    source: mirbase
  warnings:
  - Downloads redirect unauthenticated users to the GSEA/MSigDB login page; registration
    is free but required for direct file access.
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
- authors:
  - Liu W
  - Wang X
  doi: doi:10.1186/s13059-019-1629-z
  id: doi:10.1186/s13059-019-1629-z
  journal: Genome Biology
  title: Prediction of functional microRNA targets by integrative modeling of microRNA
    binding and target expression data
  year: '2019'
- authors:
  - Wong N
  - Wang X
  doi: doi:10.1093/nar/gku1104
  id: doi:10.1093/nar/gku1104
  journal: Nucleic Acids Research
  title: 'miRDB: an online resource for microRNA target prediction and functional
    annotations'
  year: '2015'
rrid: SCR_010848
synonyms:
- MicroRNA Target Prediction Database
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:10116
- NCBITaxon:9615
- NCBITaxon:9031
version: '6.0'
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

The current release (version 6.0, June 2019) was generated with MirTarget V4 using
miRNA sequences from miRBase 22 and contains about 3.5 million predicted targets
for 7,086 miRNAs. miRDB was created by Xiaowei Wang's lab, now in the Department of
Pharmacology and Regenerative Medicine at the University of Illinois Chicago.