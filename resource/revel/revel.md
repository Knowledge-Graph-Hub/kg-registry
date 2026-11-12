---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: joseph.rothstein@mssm.edu
  label: Joseph H. Rothstein
- category: Individual
  contact_details:
  - contact_type: email
    value: nilah@berkeley.edu
  label: Nilah M. Ioannidis
- category: Individual
  contact_details:
  - contact_type: email
    value: weiva.sieh@mssm.edu
  label: Weiva Sieh
creation_date: '2026-11-12T00:00:00Z'
description: REVEL (Rare Exome Variant Ensemble Learner) is an ensemble method for
  predicting the pathogenicity of missense variants in the human genome. It combines
  scores from 13 individual tools (including MutPred, FATHMM, VEST, PolyPhen, SIFT,
  PROVEAN, MutationAssessor, MutationTaster, LRT, GERP, SiPhy, phyloP and phastCons)
  with a random forest trained on recently discovered disease mutations and rare neutral
  variants, and reports a score from 0 to 1 where higher values indicate a greater
  likelihood of being disease-causing. REVEL scores are precomputed for all possible
  human missense variants and distributed as CSV files with hg19/GRCh37 and GRCh38
  positions and Ensembl transcript IDs. Scores are freely available for non-commercial
  use.
domains:
- biomedical
- genomics
- genetic variation
- rare disease
- information technology
- machine learning
homepage_url: https://sites.google.com/site/revelgenomics/
id: revel
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://sites.google.com/site/revelgenomics/downloads
  label: Free for non-commercial use; for other uses contact Weiva Sieh
name: REVEL
products:
- category: Product
  compression: zip
  description: REVEL v1.3 precomputed scores for all possible human missense variants
    in a single comma-separated file, with chromosome, hg19 and GRCh38 positions, reference
    and alternate nucleotides and amino acids, REVEL score, and Ensembl transcript IDs
    (released 2021-05-03).
  format: csv
  id: revel.all-chromosomes
  latest_version: '1.3'
  name: REVEL v1.3 Scores, All Chromosomes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: revel
  - relation_type: prov:wasInfluencedBy
    source: dbnsfp
  - relation_type: prov:wasInfluencedBy
    source: ensembl
  product_file_size: 667102707
  product_url: https://rothsj06.dmz.hpc.mssm.edu/revel-v1.3_all_chromosomes.zip
- category: Product
  description: Zenodo record of REVEL v1.3 scores, with the all-chromosome file and
    per-chromosome genome segment files (up to 500,000 variants per file) as zipped
    CSVs. The Zenodo record is labelled with the Open Data Commons Open Database License.
  format: http
  id: revel.zenodo
  latest_version: '1.3'
  license:
    id: https://opendatacommons.org/licenses/odbl/1-0/
    label: ODbL 1.0 (as labelled on the Zenodo record)
  name: REVEL Scores on Zenodo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: revel
  - relation_type: prov:wasInfluencedBy
    source: dbnsfp
  - relation_type: prov:wasInfluencedBy
    source: ensembl
  product_url: https://zenodo.org/records/7072866
- category: Product
  description: REVEL downloads page with the all-chromosome file, links to genome segment
    files, the Zenodo mirror, file format description and release notes.
  format: http
  id: revel.downloads
  name: REVEL Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: revel
  product_url: https://sites.google.com/site/revelgenomics/downloads
- category: DocumentationProduct
  description: REVEL website describing the method, score interpretation, and sensitivity,
    specificity and likelihood ratio threshold tables.
  format: http
  id: revel.docs
  name: REVEL Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: revel
  product_url: https://sites.google.com/site/revelgenomics/
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
  - Nilah M. Ioannidis
  - Joseph H. Rothstein
  - Vikas Pejaver
  - Sumit Middha
  - Shannon K. McDonnell
  - Saurabh Baheti
  - Anthony Musolf
  - Qing Li
  - Emily Holzinger
  - Danielle Karyadi
  - Lisa A. Cannon-Albright
  - Craig C. Teerlink
  - Janet L. Stanford
  - William B. Isaacs
  - Jianfeng Xu
  - Kathleen A. Cooney
  - Ethan M. Lange
  - Johanna Schleutker
  - John D. Carpten
  - Isaac J. Powell
  - Olivier Cussenot
  - Geraldine Cancel-Tassin
  - Graham G. Giles
  - Robert J. MacInnis
  - Christiane Maier
  - Chih-Lin Hsieh
  - Fredrik Wiklund
  - William J. Catalona
  - William D. Foulkes
  - Diptasri Mandal
  - Rosalind A. Eeles
  - Zsofia Kote-Jarai
  - Carlos D. Bustamante
  - Daniel J. Schaid
  - Trevor Hastie
  - Elaine A. Ostrander
  - Joan E. Bailey-Wilson
  - Predrag Radivojac
  - Stephen N. Thibodeau
  - Alice S. Whittemore
  - Weiva Sieh
  doi: 10.1016/j.ajhg.2016.08.016
  id: doi:10.1016/j.ajhg.2016.08.016
  journal: The American Journal of Human Genetics
  preferred: true
  title: 'REVEL: An Ensemble Method for Predicting the Pathogenicity of Rare Missense
    Variants'
  year: '2016'
synonyms:
- Rare Exome Variant Ensemble Learner
version: '1.3'
---
# REVEL

REVEL (Rare Exome Variant Ensemble Learner) predicts whether a missense variant is likely to be pathogenic. It was developed by Nilah Ioannidis, Joseph Rothstein, Weiva Sieh, Alice Whittemore and colleagues. REVEL combines 13 individual pathogenicity predictors and conservation scores in a random forest trained on rare disease mutations and rare neutral variants, so it performs well on rare variants. Scores range from 0 to 1, with higher values indicating a greater likelihood that the variant is disease-causing.

## Access

- **Precomputed scores**: REVEL v1.3 scores for all possible human missense variants, as one zipped CSV (about 667 MB) or per-chromosome genome segment files, with hg19/GRCh37 and GRCh38 (liftOver) positions and Ensembl transcript IDs.
- **Zenodo mirror**: the same files on Zenodo.

## License

REVEL scores are freely available for non-commercial use. For other uses, contact Weiva Sieh. The Zenodo mirror is labelled with the Open Data Commons Open Database License (ODbL).
