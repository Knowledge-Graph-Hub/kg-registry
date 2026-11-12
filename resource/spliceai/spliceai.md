---
activity_status: inactive
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: kjaganathan@illumina.com
  label: Kishore Jaganathan
- category: Organization
  contact_details:
  - contact_type: email
    value: AI_licensing@illumina.com
  - contact_type: github
    value: Illumina
  label: Illumina
creation_date: '2026-11-12T00:00:00Z'
description: SpliceAI is a deep residual neural network from Illumina that predicts
  splice junctions from pre-mRNA sequence and scores the effect of genetic variants
  on splicing. For each variant it reports delta scores (0 to 1) for acceptor gain,
  acceptor loss, donor gain and donor loss, with the position of each predicted change.
  Illumina distributes precomputed SpliceAI scores for all possible substitutions,
  1-base insertions and 1-4 base deletions within genes, and Ensembl distributes precomputed
  SpliceAI scores for all GRCh38 SNVs in MANE Select transcripts for use with the VEP
  SpliceAI plugin. The source code is under the PolyForm Strict License 1.0.0, the
  trained models under CC BY-NC 4.0, and the precomputed scores are free for academic
  and not-for-profit use. The GitHub repository was archived on 2026-04-20 at release
  v1.3.1.
domains:
- biomedical
- genomics
- genetic variation
- information technology
- machine learning
homepage_url: https://github.com/Illumina/SpliceAI
id: spliceai
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://polyformproject.org/licenses/strict/1.0.0/
  label: PolyForm Strict License 1.0.0 (code); CC BY-NC 4.0 (models); precomputed scores
    free for academic and not-for-profit use
name: SpliceAI
products:
- category: ProcessProduct
  description: SpliceAI source code and trained models, a Python package that annotates
    variants in a VCF file with SpliceAI delta scores and positions. Installable with
    pip or bioconda (requires TensorFlow). The repository was archived on 2026-04-20
    at release v1.3.1.
  format: python
  id: spliceai.software
  latest_version: 1.3.1
  license:
    id: https://polyformproject.org/licenses/strict/1.0.0/
    label: PolyForm Strict License 1.0.0 (code); CC BY-NC 4.0 (models)
  name: SpliceAI Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spliceai
  product_url: https://github.com/Illumina/SpliceAI
- category: Product
  description: Illumina precomputed SpliceAI scores for all possible substitutions,
    1-base insertions and 1-4 base deletions within genes, on GRCh37 and GRCh38, raw
    and masked, distributed as VCF files through Illumina BaseSpace (login required).
    Free for academic and not-for-profit use; other uses require a commercial license.
  format: http
  id: spliceai.precomputed
  license:
    id: https://basespace.illumina.com/s/otSPW8hnhaZR
    label: Free for academic and not-for-profit use; commercial use requires a license
      from Illumina
  name: SpliceAI Precomputed Scores (Illumina BaseSpace)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:wasInfluencedBy
    source: gencode
  product_url: https://basespace.illumina.com/s/otSPW8hnhaZR
- category: Product
  compression: gzip
  description: Ensembl precomputed raw SpliceAI scores for all possible SNVs on GRCh38,
    calculated against one MANE Select transcript per protein-coding gene (MANE v1.4)
    with a maximum distance of 50 bases, as a bgzip-compressed VCF with a tabix index.
    Prepared for the Ensembl VEP SpliceAI plugin.
  format: vcf
  id: spliceai.ensembl-mane-raw
  name: SpliceAI Raw SNV Scores, Ensembl MANE v1.4 (GRCh38)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: ensembl
  product_file_size: 28926367953
  product_url: https://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38/variation_plugins/spliceai_scores.raw.snv.ensembl_mane_v1.4.grch38.vcf.gz
- category: Product
  compression: gzip
  description: Ensembl precomputed masked SpliceAI scores for all possible SNVs on GRCh38,
    calculated against one MANE Select transcript per protein-coding gene (MANE v1.4)
    with a maximum distance of 50 bases, as a bgzip-compressed VCF with a tabix index.
    Prepared for the Ensembl VEP SpliceAI plugin.
  format: vcf
  id: spliceai.ensembl-mane-masked
  name: SpliceAI Masked SNV Scores, Ensembl MANE v1.4 (GRCh38)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: ensembl
  product_file_size: 28643031420
  product_url: https://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38/variation_plugins/spliceai_scores.masked.snv.ensembl_mane_v1.4.grch38.vcf.gz
- category: Product
  description: Ensembl directory of precomputed SpliceAI score files for the VEP SpliceAI
    plugin, with raw and masked SNV scores computed against Ensembl/MANE transcript
    sets (Ensembl 107 and 110, MANE v1.0 and v1.4) on GRCh38, plus a README.
  format: http
  id: spliceai.ensembl-downloads
  name: Ensembl SpliceAI Score Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: ensembl
  product_url: https://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38/variation_plugins/
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
  - Kishore Jaganathan
  - Sofia Kyriazopoulou Panagiotopoulou
  - Jeremy F. McRae
  - Siavash Fazel Darbandi
  - David Knowles
  - Yang I. Li
  - Jack A. Kosmicki
  - Juan Arbelaez
  - Wenwu Cui
  - Grace B. Schwartz
  - Eric D. Chow
  - Efstathios Kanterakis
  - Hong Gao
  - Amirali Kia
  - Serafim Batzoglou
  - Stephan J. Sanders
  - Kyle Kai-How Farh
  doi: 10.1016/j.cell.2018.12.015
  id: doi:10.1016/j.cell.2018.12.015
  journal: Cell
  preferred: true
  title: Predicting Splicing from Primary Sequence with Deep Learning
  year: '2019'
repository: https://github.com/Illumina/SpliceAI
version: 1.3.1
---
# SpliceAI

SpliceAI is a deep learning model developed at Illumina that predicts splice junctions directly from pre-mRNA sequence. Given a variant, it scores the predicted change in splice site usage (acceptor gain, acceptor loss, donor gain and donor loss) within a window around the variant, along with the position of each change. It is widely used to flag cryptic splice variants in rare disease and clinical genomics.

## Access

- **Software**: the `spliceai` Python package (pip or bioconda) annotates VCF files. The GitHub repository was archived on 2026-04-20 at v1.3.1.
- **Illumina precomputed scores**: all possible substitutions and small indels within genes on GRCh37 and GRCh38, via Illumina BaseSpace.
- **Ensembl precomputed scores**: raw and masked scores for all GRCh38 SNVs on MANE Select transcripts, as tabix-indexed VCFs for the VEP SpliceAI plugin.
- **SpliceAI-lookup**: a Broad Institute web tool for single-variant SpliceAI and Pangolin predictions.

## License

The source code is provided under the PolyForm Strict License 1.0.0 and the trained models under CC BY-NC 4.0 for academic and non-commercial use. Precomputed scores are free for academic and not-for-profit use; other uses require a commercial license from Illumina.
