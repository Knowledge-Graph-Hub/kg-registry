---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: FANTOM5 (Functional Annotation of the Mammalian Genome 5) is a RIKEN-led
  international project that built a promoter-level mammalian expression atlas using
  Cap Analysis of Gene Expression (CAGE). It maps transcription start sites and quantifies
  promoter and enhancer activity across a broad collection of human and mouse primary
  cells, tissues, and cell lines. The resource provides genome-wide catalogues of
  CAGE peaks (promoters) and transcribed enhancers together with their expression
  profiles, supporting studies of gene regulation and cell-type-specific transcription.
domains:
- genomics
- systems biology
- anatomy and development
homepage_url: https://fantom.gsc.riken.jp/5/
id: fantom5
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: FANTOM5
products:
- category: Product
  description: Downloadable data files for the FANTOM5 promoter-level expression atlas,
    including CAGE peaks (promoters), transcribed enhancers, and associated expression
    matrices for human and mouse genome assemblies.
  format: tsv
  id: fantom5.atlas
  name: FANTOM5 Expression Atlas Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fantom5
  product_url: https://fantom.gsc.riken.jp/5/datafiles/
- category: GraphicalInterface
  description: SSTAR (Semantic catalogue of Samples, Transcription initiation, And
    Regulations) is the FANTOM5 web interface for browsing samples, CAGE peaks, co-expression
    clusters, and transcription factor annotations.
  format: http
  id: fantom5.sstar
  name: FANTOM5 SSTAR Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fantom5
  product_url: https://fantom.gsc.riken.jp/5/sstar/
- category: GraphicalInterface
  description: ZENBU is the interactive data integration and visualization system
    used to explore FANTOM5 promoter, enhancer, and time-course expression data in
    genomic context.
  format: http
  id: fantom5.zenbu
  name: FANTOM5 ZENBU Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fantom5
  product_url: https://fantom.gsc.riken.jp/zenbu/
- category: DocumentationProduct
  description: FANTOM5 project website with documentation, data access guidelines,
    tool descriptions, and citation information for the promoter-level mammalian expression
    atlas.
  format: http
  id: fantom5.docs
  name: FANTOM5 Project Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fantom5
  product_url: https://fantom.gsc.riken.jp/5/
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
  - The FANTOM Consortium and the RIKEN PMI and CLST (DGT)
  doi: doi:10.1038/nature13182
  id: doi:10.1038/nature13182
  journal: Nature
  preferred: true
  title: A promoter-level mammalian expression atlas
  year: '2014'
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# FANTOM5

FANTOM5 (Functional Annotation of the Mammalian Genome 5) is a RIKEN-led
international collaboration that produced a promoter-level mammalian expression
atlas. Using Cap Analysis of Gene Expression (CAGE), the project mapped
transcription start sites and quantified the activity of promoters and enhancers
across a large panel of human and mouse primary cells, tissues, and cell lines.

The resource provides genome-wide catalogues of CAGE peaks (promoters) and
transcribed enhancers, together with their expression profiles, and exposes the
data through downloadable files and interactive browsers (SSTAR and ZENBU). It is
a widely used reference for gene regulation, promoter and enhancer usage, and
cell-type-specific transcription. FANTOM5 data are distributed under a Creative
Commons Attribution 4.0 International (CC BY 4.0) license.