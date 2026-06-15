---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: AlphaMissense is a deep learning model from Google DeepMind that predicts
  the pathogenicity of missense variants across the human proteome. It provides precomputed
  pathogenicity scores and classifications (likely benign, likely pathogenic, or ambiguous)
  for all approximately 71 million possible single amino acid substitutions in the
  human genome, as well as substitution effect scores for the entire proteome. The
  predictions are distributed via bulk download and accessible through hosted viewers
  and genome browsers.
domains:
- genomics
- clinical
- proteomics
- precision medicine
- biomedical
homepage_url: https://deepmind.google/science/alphamissense/
id: alphamissense
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: AlphaMissense
products:
- category: Product
  description: Precomputed AlphaMissense pathogenicity predictions for all possible
    human missense variants and amino acid substitutions, including per-variant pathogenicity
    scores and class labels. Distributed as tab-separated value files via Zenodo and
    Google Cloud Storage.
  format: tsv
  id: alphamissense.predictions
  name: AlphaMissense Variant Predictions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  product_url: https://zenodo.org/records/10813168
- category: ProcessProduct
  description: Open-source implementation of the AlphaMissense model used to predict
    the pathogenicity of missense variants, released for academic reproducibility.
  format: python
  id: alphamissense.software
  name: AlphaMissense Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  product_url: https://github.com/google-deepmind/alphamissense
- category: GraphicalInterface
  description: Web-based viewer for exploring AlphaMissense pathogenicity predictions,
    allowing users to look up genes and variants and inspect per-residue pathogenicity
    scores.
  format: http
  id: alphamissense.viewer
  name: AlphaMissense Hosted Viewer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  product_url: https://alphamissense.hegelab.org/
- category: DocumentationProduct
  description: Project overview, methodology, and links to data resources for AlphaMissense,
    provided by Google DeepMind.
  format: http
  id: alphamissense.docs
  name: AlphaMissense Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  product_url: https://deepmind.google/science/alphamissense/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 404 error
    when accessing file'
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
  - Jun Cheng
  - Guido Novati
  - Joshua Pan
  - Clare Bycroft
  - Akvilė Žemgulytė
  - Taylor Applebaum
  - Alexander Pritzel
  - Lai Hong Wong
  - Michal Zielinski
  - Tobias Sargeant
  - Rosalia G. Schneider
  - Andrew W. Senior
  - John Jumper
  - Demis Hassabis
  - Pushmeet Kohli
  - Žiga Avsec
  doi: doi:10.1126/science.adg7492
  id: doi:10.1126/science.adg7492
  journal: Science
  preferred: true
  title: Accurate proteome-wide missense variant effect prediction with AlphaMissense
  year: '2023'
repository: https://github.com/google-deepmind/alphamissense
taxon:
- NCBITaxon:9606
---
# AlphaMissense

AlphaMissense is a deep learning model developed by Google DeepMind that predicts
the pathogenicity of missense variants across the human proteome. Building on the
protein structure modeling approach of AlphaFold, it classifies single amino acid
substitutions as likely benign, likely pathogenic, or ambiguous, and assigns a
continuous pathogenicity score to each variant.

The resource provides precomputed predictions for all approximately 71 million
possible human missense variants, distributed as bulk download files via Zenodo
and Google Cloud Storage and accessible through hosted viewers and genome
browsers. In KG-Registry, the AlphaMissense products point to the variant
prediction dataset, the open-source prediction software, a hosted exploration
viewer, and project documentation.