---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: songlab-cal
  - contact_type: url
    value: https://github.com/songlab-cal/gpn/issues
  label: Song Lab, University of California, Berkeley
creation_date: '2026-11-12T00:00:00Z'
description: GPN-Star is a phylogeny-aware genomic language model from the Song lab
  at UC Berkeley that predicts functional constraint and variant effects across the
  genome from multispecies whole-genome alignments, using a phylogeny-informed attention
  design. It supersedes GPN-MSA. Three human (hg38) models were trained on vertebrate
  (100-way), mammalian (447-way) and primate (243-way) alignments, and further models
  cover mouse, chicken, Drosophila melanogaster, Caenorhabditis elegans and Arabidopsis
  thaliana. The authors distribute the trained models on Hugging Face (MIT license),
  genome-wide mutation-rate-calibrated constraint (entropy) and variant (log-likelihood
  ratio) scores as Parquet and BigWig files on Hugging Face (Apache 2.0), a multi-assembly
  UCSC Genome Browser track hub, and the gpn Python package for inference and training.
domains:
- biomedical
- genomics
- genetic variation
- molecular evolution
- organisms
- model organisms
- information technology
- machine learning
homepage_url: https://gpn.readthedocs.io/en/latest/models/gpn-star/
id: gpn-star
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://github.com/songlab-cal/gpn/blob/main/LICENSE
  label: MIT (code and models); Apache 2.0 (precomputed scores)
name: GPN-Star
products:
- category: Product
  description: GPN-Star genome-wide scores on Hugging Face, with mutation-rate-calibrated
    constraint (entropy) and variant (log-likelihood ratio) scores for eight score sets
    (human hg38 vertebrate, mammal and primate models; mouse mm39; chicken galGal6;
    D. melanogaster dm6; C. elegans ce11; A. thaliana TAIR10). Canonical scores are
    chromosome-sharded Parquet files; BigWig display tracks are also provided.
  format: parquet
  id: gpn-star.scores
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache 2.0
  name: GPN-Star Genome-wide Scores
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  product_url: https://huggingface.co/datasets/songlab/gpn-star-scores
- category: GraphicalInterface
  description: Multi-assembly UCSC Genome Browser track hub for GPN-Star scores, hosted
    in the Hugging Face scores dataset and showing per-base logo and log-likelihood
    ratio tracks for the eight GPN-Star score sets.
  format: http
  id: gpn-star.ucsc-hub
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache 2.0
  name: GPN-Star UCSC Track Hub
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  - relation_type: prov:wasInfluencedBy
    source: ucsc
  product_url: https://genome.ucsc.edu/cgi-bin/hgTracks?hubUrl=https%3A%2F%2Fhuggingface.co%2Fdatasets%2Fsonglab%2Fgpn-star-scores%2Fresolve%2Fmain%2Fucsc%2Fhub.txt
- category: Product
  description: Hugging Face collection of trained GPN-Star model checkpoints (safetensors
    weights with configuration and calibration tables), including the human vertebrate
    (v100), mammal (m447) and primate (p243) models at 25M, 85M and 200M parameters
    and models for mouse, chicken, D. melanogaster, C. elegans and A. thaliana. Loadable
    with Hugging Face Transformers through the gpn package.
  format: mixed
  id: gpn-star.models
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: GPN-Star Models
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  product_url: https://huggingface.co/collections/songlab/gpn-star-68c0c055acc2ee51d5c4f129
- category: ProcessProduct
  description: The gpn Python package and repository (songlab-cal/gpn), with code for
    GPN, GPN-MSA, PhyloGPN and GPN-Star, a command-line interface for variant effect
    prediction, logits and embeddings, training recipes, and Colab notebooks including
    one for querying the precomputed GPN-Star scores. Installable with pip install gpn.
  format: python
  id: gpn-star.software
  license:
    id: https://github.com/songlab-cal/gpn/blob/main/LICENSE
    label: MIT
  name: GPN Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  product_url: https://github.com/songlab-cal/gpn
- category: DocumentationProduct
  description: GPN documentation pages for GPN-Star, describing the models, published
    assets (models, alignments, scores and benchmark datasets) and usage.
  format: http
  id: gpn-star.docs
  name: GPN-Star Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  product_url: https://gpn.readthedocs.io/en/latest/models/gpn-star/
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
  - Chengzhong Ye
  - Gonzalo Benegas
  - Carlos Albors
  - Jianan Canal Li
  - Sebastian Prillo
  - Peter D. Fields
  - Brian Clarke
  - Yun S. Song
  doi: 10.1038/s41586-026-11005-5
  id: doi:10.1038/s41586-026-11005-5
  journal: Nature
  preferred: true
  title: Predicting genome-wide functional constraints with GPN-Star
  year: '2026'
- authors:
  - Chengzhong Ye
  - Gonzalo Benegas
  - Carlos Albors
  - Jianan Canal Li
  - Sebastian Prillo
  - Peter D. Fields
  - Brian Clarke
  - Yun S. Song
  doi: 10.1101/2025.09.21.677619
  id: doi:10.1101/2025.09.21.677619
  journal: bioRxiv
  title: Predicting functional constraints across evolutionary timescales with phylogeny-informed
    genomic language models
  year: '2025'
repository: https://github.com/songlab-cal/gpn
---
# GPN-Star

GPN-Star is a genomic language model developed in Yun Song's lab at the University of California, Berkeley. It learns from whole-genome alignments of many species and uses the species phylogeny in its attention design, so it can weigh evidence from closely and distantly related species. It predicts how constrained each position in a genome is and how damaging a nucleotide change is likely to be. GPN-Star supersedes the earlier GPN-MSA model.

Human models were trained on alignments of 100 vertebrates, 447 mammals and 243 primates. Additional models cover mouse, chicken, *Drosophila melanogaster*, *Caenorhabditis elegans* and *Arabidopsis thaliana*.

## Access

- **Precomputed scores**: genome-wide, mutation-rate-calibrated constraint and variant scores for eight score sets, as Parquet and BigWig files in the `songlab/gpn-star-scores` Hugging Face dataset (Apache 2.0).
- **UCSC track hub**: GPN-Star tracks for all supported assemblies in the UCSC Genome Browser.
- **Models**: trained checkpoints in the `songlab` Hugging Face organization (MIT).
- **Software**: the `gpn` Python package on GitHub and PyPI (MIT).
