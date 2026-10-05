---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cadd.gs.washington.edu/contact
  label: University of Washington and Berlin Institute of Health at Charite (Kircher Lab)
creation_date: '2026-10-05T00:00:00Z'
description: CADD (Combined Annotation Dependent Depletion) scores the deleteriousness
  of single nucleotide variants and small insertions and deletions throughout the human
  genome. It integrates many diverse annotations (gene model consequences from Ensembl
  VEP, conservation, regulatory and epigenetic data, protein-level and splicing predictions)
  into one metric by training a model to distinguish simulated de novo variants from
  variants fixed in human populations since the split from the human-chimpanzee ancestor.
  CADD provides precomputed scores for all possible SNVs in GRCh37 and GRCh38, scored
  indel sets, a web service for scoring VCF files, a REST API, and offline scoring scripts.
  Scores are free for non-commercial use; commercial use requires a license from the
  University of Washington.
domains:
- biomedical
- genomics
- genetic variation
homepage_url: https://cadd.gs.washington.edu/
id: cadd
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://els2.comotion.uw.edu/product/cadd-scores
  label: Free for non-commercial use; commercial use requires a license from the University
    of Washington
name: CADD
products:
- category: GraphicalInterface
  description: CADD website with single-variant and range lookup of scores, news, release
    notes and links to related resources.
  format: http
  id: cadd.website
  name: CADD Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  product_url: https://cadd.gs.washington.edu/
- category: Product
  compression: gzip
  description: CADD v1.7 precomputed raw and PHRED-scaled scores for all possible single
    nucleotide variants in the GRCh38 human reference genome, tab-separated and bgzip-compressed
    with a tabix index. A larger version including all annotations is also offered.
  format: tsv
  id: cadd.snvs.grch38
  name: CADD v1.7 Whole-Genome SNV Scores (GRCh38)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  - relation_type: prov:wasInfluencedBy
    source: ensembl
  - relation_type: prov:wasInfluencedBy
    source: ucsc
  - relation_type: prov:wasInfluencedBy
    source: encode
  product_file_size: 87473403655
  product_url: https://krishna.gs.washington.edu/download/CADD/v1.7/GRCh38/whole_genome_SNVs.tsv.gz
- category: Product
  compression: gzip
  description: CADD v1.7 precomputed raw and PHRED-scaled scores for all possible single
    nucleotide variants in the GRCh37 human reference genome, tab-separated and bgzip-compressed
    with a tabix index.
  format: tsv
  id: cadd.snvs.grch37
  name: CADD v1.7 Whole-Genome SNV Scores (GRCh37)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  - relation_type: prov:wasInfluencedBy
    source: ensembl
  - relation_type: prov:wasInfluencedBy
    source: ucsc
  - relation_type: prov:wasInfluencedBy
    source: encode
  product_file_size: 85228947819
  product_url: https://krishna.gs.washington.edu/download/CADD/v1.7/GRCh37/whole_genome_SNVs.tsv.gz
- category: Product
  compression: gzip
  description: CADD v1.7 scores for small insertions and deletions observed in gnomAD
    v4.0 genomes, on GRCh38, tab-separated and bgzip-compressed with a tabix index.
  format: tsv
  id: cadd.gnomad-indels.grch38
  name: CADD v1.7 gnomAD v4.0 InDel Scores (GRCh38)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  - relation_type: prov:hadPrimarySource
    source: gnomad
  product_file_size: 1257151321
  product_url: https://krishna.gs.washington.edu/download/CADD/v1.7/GRCh38/gnomad.genomes.r4.0.indel.tsv.gz
- category: Product
  description: Download page listing all CADD releases (v1.0 to v1.7) with precomputed
    score files, scored variant sets, annotation files for offline scoring and release
    notes, mirrored at the University of Washington and the Berlin Institute of Health.
  format: http
  id: cadd.downloads
  name: CADD Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  product_url: https://cadd.gs.washington.edu/download
- category: ProcessProduct
  description: Web service for scoring uploaded VCF files of SNVs, MNVs and indels with
    a selected CADD version and genome build.
  format: http
  id: cadd.score
  name: CADD Scoring Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  product_url: https://cadd.gs.washington.edu/score
- category: ProgrammingInterface
  description: REST API returning CADD raw and PHRED scores as JSON for a single position,
    a specific variant, or a genomic range, for a chosen CADD version and genome build.
  format: http
  id: cadd.api
  name: CADD API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  product_url: https://cadd.gs.washington.edu/api
- category: ProcessProduct
  description: CADD-scripts, a Snakemake-based pipeline for scoring variants offline
    with CADD, including annotation and model files for each release.
  id: cadd.scripts
  license:
    id: https://github.com/kircherlab/CADD-scripts/blob/master/LICENSE
    label: Free for non-commercial users and licensees of CADD
  name: CADD-scripts
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  product_url: https://github.com/kircherlab/CADD-scripts
- category: DocumentationProduct
  description: CADD information pages describing the method, annotations, score interpretation
    and how to cite CADD.
  format: http
  id: cadd.docs
  name: CADD Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cadd
  product_url: https://cadd.gs.washington.edu/info
publications:
- authors:
  - Philipp Rentzsch
  - Daniela Witten
  - Gregory M Cooper
  - Jay Shendure
  - Martin Kircher
  doi: 10.1093/nar/gky1016
  id: doi:10.1093/nar/gky1016
  journal: Nucleic Acids Research
  preferred: true
  title: 'CADD: predicting the deleteriousness of variants throughout the human genome'
  year: '2019'
- authors:
  - Martin Kircher
  - Daniela M Witten
  - Preti Jain
  - Brian J O'Roak
  - Gregory M Cooper
  - Jay Shendure
  doi: 10.1038/ng.2892
  id: doi:10.1038/ng.2892
  journal: Nature Genetics
  title: A general framework for estimating the relative pathogenicity of human genetic
    variants
  year: '2014'
- authors:
  - Max Schubach
  - Thorben Maass
  - Lusiné Nazaretyan
  - Sebastian Röner
  - Martin Kircher
  doi: 10.1093/nar/gkad989
  id: doi:10.1093/nar/gkad989
  journal: Nucleic Acids Research
  title: 'CADD v1.7: using protein language models, regulatory CNNs and other nucleotide-level
    scores to improve genome-wide variant predictions'
  year: '2024'
synonyms:
- Combined Annotation Dependent Depletion
---
# CADD

CADD (Combined Annotation Dependent Depletion) is a framework for scoring the deleteriousness of single nucleotide variants (SNVs) and small insertions and deletions (indels) anywhere in the human genome. It was developed at the University of Washington and HudsonAlpha and is now maintained by the Kircher lab at the Berlin Institute of Health at Charite with the University of Washington.

CADD combines many annotations into a single score. The model is trained to separate variants that survived natural selection (fixed in humans since the human-chimpanzee ancestor) from simulated variants that did not face selection. Annotations include Ensembl VEP gene model consequences, conservation scores, regulatory and epigenetic data, splicing predictions and, since v1.7, protein language model and regulatory CNN scores. Each variant gets a raw score and a PHRED-scaled score, where 10 marks the top 10% of all possible SNVs and 20 the top 1%.

## Access

- **Precomputed scores**: all possible SNVs for GRCh37 and GRCh38 (about 85 to 87 GB each for v1.7), plus scored gnomAD indel sets, as bgzip-compressed TSV files with tabix indexes. Older releases (v1.0 to v1.6) remain available.
- **Web service**: upload a VCF to score new variants, including indels and MNVs.
- **API**: JSON lookup by position, variant or range.
- **Offline scoring**: the CADD-scripts pipeline on GitHub.

## License

CADD scores are freely available for non-commercial applications. Commercial use requires a license from the University of Washington (UW CoMotion).
