---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: tkzeng
  label: Tony Zeng
- category: Individual
  contact_details:
  - contact_type: url
    value: https://zenodo.org/records/15649338
  label: Nils Wagner (Technical University of Munich; precomputed scores)
creation_date: '2026-11-12T00:00:00Z'
description: Pangolin is a deep learning model that predicts splice site usage from
  DNA sequence and the effect of genetic variants on splicing. Trained on splice site
  usage measured in RNA-seq from multiple tissues of human, rhesus macaque, mouse and
  rat, it reports, for a window around each variant, the maximum increase (gain) and
  decrease (loss) in splice site usage and their positions, optionally masked using
  a gene annotation. The Pangolin software is distributed on GitHub under GPL-3.0.
  Precomputed hg38 scores for all SNVs in protein-coding genes, masked using GENCODE
  splice site annotations, were computed with default parameters by researchers at
  the Technical University of Munich and published on Zenodo under CC BY 4.0.
domains:
- biomedical
- genomics
- genetic variation
- information technology
- machine learning
homepage_url: https://github.com/tkzeng/Pangolin
id: pangolin
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/gpl-3.0.html
  label: GPL-3.0
name: Pangolin
products:
- category: ProcessProduct
  description: Pangolin source code and trained models, a Python (PyTorch) tool that
    annotates variants in a VCF or CSV file with splice gain and loss scores, using
    a gene annotation database (GENCODE-based databases are provided) for masking.
    A Google Colab notebook is also provided.
  format: python
  id: pangolin.software
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.html
    label: GPL-3.0
  name: Pangolin Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pangolin
  - relation_type: prov:wasInfluencedBy
    source: gencode
  product_url: https://github.com/tkzeng/Pangolin
- category: Product
  compression: zip
  description: Pangolin precomputed scores for all SNVs in protein-coding genes on hg38,
    computed with default parameters (window size 50 nt) and masked using GENCODE splice
    site annotations, as per-gene TSV files with chromosome, position, reference and
    alternate alleles, gain and loss scores and their relative positions. Computed by
    Nils Wagner and Aleksandr Neverov (Technical University of Munich) and published
    on Zenodo on 2025-06-12.
  format: tsv
  id: pangolin.hg38-snvs-masked
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Pangolin Precomputed hg38 SNV Scores (Masked)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pangolin
  - relation_type: prov:wasInfluencedBy
    source: gencode
  product_file_size: 12988141317
  product_url: https://zenodo.org/records/15649338
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
- category: GraphicalInterface
  description: SpliceAI-lookup, a web tool maintained by the Broad Institute TGG that
    computes SpliceAI and Pangolin splicing predictions for a single variant (using
    modified versions supporting multi-nucleotide variants and raw scores) and shows
    other variant scores alongside. Source code is on GitHub (broadinstitute/SpliceAI-lookup,
    MIT license) for running a local API server.
  format: http
  id: spliceai.lookup
  name: SpliceAI-lookup
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: pangolin
  - relation_type: prov:wasInfluencedBy
    source: alphamissense
  product_url: https://spliceailookup.broadinstitute.org/
  repository: https://github.com/broadinstitute/SpliceAI-lookup
  rrid: SCR_026278
publications:
- authors:
  - Tony Zeng
  - Yang I Li
  doi: 10.1186/s13059-022-02664-4
  id: doi:10.1186/s13059-022-02664-4
  journal: Genome Biology
  preferred: true
  title: Predicting RNA splicing from DNA sequence using Pangolin
  year: '2022'
repository: https://github.com/tkzeng/Pangolin
---
# Pangolin

Pangolin is a deep learning model for predicting RNA splicing from DNA sequence, developed by Tony Zeng and Yang I. Li at the University of Chicago. It was trained on splice site usage quantified from RNA-seq data across four tissues in four mammalian species (human, rhesus macaque, mouse and rat), and predicts both whether a position is a splice site and how strongly it is used. For a variant, Pangolin reports the largest predicted gain and loss in splice site usage within a window around the variant.

## Access

- **Software**: the Pangolin Python package on GitHub (GPL-3.0), which scores VCF or CSV input and can mask scores using a GENCODE-based annotation database. A Colab notebook is provided.
- **Precomputed scores**: masked Pangolin scores for all hg38 SNVs in protein-coding genes, as a 13 GB zip of per-gene TSV files on Zenodo (CC BY 4.0). These were computed by Nils Wagner and Aleksandr Neverov at the Technical University of Munich, not by the original authors.
- Pangolin predictions are also available for single variants through the Broad Institute SpliceAI-lookup web tool (see the SpliceAI page).
