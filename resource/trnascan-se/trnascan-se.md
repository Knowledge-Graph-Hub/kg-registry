---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: trna@soe.ucsc.edu
  - contact_type: url
    value: https://trna.ucsc.edu/tRNAscan-SE/contact.html
  - contact_type: github
    value: UCSC-LoweLab
  label: Lowe Lab, Department of Biomolecular Engineering, University of California
    Santa Cruz
creation_date: '2026-11-12T00:00:00Z'
description: tRNAscan-SE is a program from the Lowe Lab at the University of California
  Santa Cruz that predicts transfer RNA (tRNA) genes in DNA or RNA sequences supplied
  in FASTA format. It pioneered the large-scale use of covariance models for tRNA
  annotation; version 2.0 uses Infernal 1.1 as its covariance model search engine,
  with models trained on tRNAs from the three domains of life, isotype-specific models
  for functional classification, and filters for pseudogenes and tRNA-derived SINEs.
  Output is available as a tabular report, secondary structure file, FASTA, BED, GTF
  and GFF3. The software is distributed under GPL-3.0 on GitHub and bioconda, and
  an online search server runs tRNAscan-SE 2.0 on queries of under 1 million nucleotides.
  tRNAscan-SE produces the tRNA gene predictions in the Genomic tRNA Database (GtRNAdb).
domains:
- genomics
- non-coding RNA
homepage_url: https://trna.ucsc.edu/tRNAscan-SE/
id: trnascan-se
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/gpl-3.0.html
  label: GPL-3.0
name: tRNAscan-SE
products:
- category: ProcessProduct
  description: tRNAscan-SE source code repository on GitHub, containing the tRNAscan-SE
    Perl program, the tRNA covariance models, and the bundled COVE 2.4.4, tRNAscan
    1.4 and EufindtRNA 1.0 programs used in legacy search mode. Requires Perl 5 and
    Infernal 1.1. Tagged releases are published on GitHub (latest v2.0.13, July 2026),
    and the package is also available from bioconda as trnascan-se.
  format: mixed
  id: trnascan-se.software
  latest_version: 2.0.13
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.html
    label: GPL-3.0
  name: tRNAscan-SE Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trnascan-se
  product_url: https://github.com/UCSC-LoweLab/tRNAscan-SE
  repository: https://github.com/UCSC-LoweLab/tRNAscan-SE
  secondary_source:
  - relation_type: prov:used
    source: infernal
- category: ProcessProduct
  compression: gzip
  description: tRNAscan-SE 2.0.12 source distribution (gzipped tar archive) linked
    from the tRNAscan-SE search server download section.
  format: mixed
  id: trnascan-se.source-tarball
  latest_version: 2.0.12
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.html
    label: GPL-3.0
  name: tRNAscan-SE Source Code Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trnascan-se
  product_file_size: 4430943
  product_url: https://trna.ucsc.edu/software/trnascan-se-2.0.12.tar.gz
- category: ProcessProduct
  description: tRNAscan-SE packaged for the conda package manager in the bioconda
    channel.
  format: mixed
  id: trnascan-se.bioconda
  latest_version: 2.0.13
  name: tRNAscan-SE Bioconda Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trnascan-se
  product_url: https://anaconda.org/bioconda/trnascan-se
- category: GraphicalInterface
  description: tRNAscan-SE On-line search server running tRNAscan-SE 2.0. Users paste
    or upload sequences (under 1 million nucleotides total), choose a sequence source
    model (general, eukaryotic, bacterial, archaeal or mitochondrial) and search mode,
    and receive tRNA predictions with secondary structures, optionally in BED format
    or by e-mail.
  format: http
  id: trnascan-se.web-server
  name: tRNAscan-SE Search Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trnascan-se
  product_url: https://trna.ucsc.edu/tRNAscan-SE/
  rrid: SCR_008637
- category: DocumentationProduct
  description: Help page for the tRNAscan-SE search server, describing search modes,
    query sequence input, search options and result display.
  format: http
  id: trnascan-se.help
  name: tRNAscan-SE Search Server Help
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trnascan-se
  product_url: https://trna.ucsc.edu/tRNAscan-SE/help.html
- category: DocumentationProduct
  description: Change log listing the fixes and features added in each tRNAscan-SE
    2.0 release.
  format: txt
  id: trnascan-se.change-log
  name: tRNAscan-SE Change Log
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trnascan-se
  product_url: https://trna.ucsc.edu/tRNAscan-SE/change_log.txt
- category: Product
  description: Archive of previous GtRNAdb data releases with change logs
  format: http
  id: gtrnadb.archives
  name: Previous Releases Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  product_url: https://gtrnadb.org/archives.html
  secondary_source:
  - relation_type: prov:used
    source: trnascan-se
- category: Product
  compression: targz
  description: Per-genome tRNAscan-SE result archive for the human GRCh38/hg38 assembly,
    downloaded from the genome's GtRNAdb page. It contains detailed and high-confidence
    tRNAscan-SE output (.out) and secondary structure (.ss) files, a BED file of tRNA
    gene coordinates, FASTA files of genomic, mature and filtered tRNA sequences,
    and a tRNA name map. Equivalent archives are linked from each genome page in GtRNAdb.
  format: mixed
  id: gtrnadb.hg38_trnascan_results
  name: GtRNAdb Human (hg38) tRNAscan-SE Results
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: ucsc
  product_url: https://gtrnadb.org/genomes/eukaryota/Hsapi38/hg38-tRNAs.tar.gz
  secondary_source:
  - relation_type: prov:used
    source: trnascan-se
publications:
- authors:
  - Chan PP
  - Lin BY
  - Mak AJ
  - Lowe TM
  doi: 10.1093/nar/gkab688
  id: doi:10.1093/nar/gkab688
  journal: Nucleic Acids Research
  preferred: true
  title: 'tRNAscan-SE 2.0: improved detection and functional classification of transfer
    RNA genes'
  year: '2021'
- authors:
  - Chan PP
  - Lowe TM
  doi: 10.1007/978-1-4939-9173-0_1
  id: doi:10.1007/978-1-4939-9173-0_1
  journal: Methods in Molecular Biology
  title: 'tRNAscan-SE: Searching for tRNA Genes in Genomic Sequences'
  year: '2019'
- authors:
  - Lowe TM
  - Chan PP
  doi: 10.1093/nar/gkw413
  id: doi:10.1093/nar/gkw413
  journal: Nucleic Acids Research
  title: 'tRNAscan-SE On-line: integrating search and context for analysis of transfer
    RNA genes'
  year: '2016'
- authors:
  - Lowe TM
  - Eddy SR
  doi: 10.1093/nar/25.5.955
  id: doi:10.1093/nar/25.5.955
  journal: Nucleic Acids Research
  title: 'tRNAscan-SE: A Program for Improved Detection of Transfer RNA Genes in Genomic
    Sequence'
  year: '1997'
repository: https://github.com/UCSC-LoweLab/tRNAscan-SE
rrid: SCR_008637
version: 2.0.13
---
# tRNAscan-SE

tRNAscan-SE is a tRNA gene detection program developed by Todd Lowe's lab at the University of California Santa Cruz. It predicts tRNA genes in DNA or RNA sequences using covariance models, which combine primary sequence and secondary structure information. Version 2.0 uses Infernal 1.1 as the search engine with covariance models trained on tRNAs from the three domains of life, then classifies predictions with isotype-specific models, which improves annotation of atypical tRNAs, pseudogenes and tRNA-derived SINEs. The original COVE-based search with the tRNAscan and EufindtRNA prefilters remains available as a legacy mode.

The software is distributed under GPL-3.0 on GitHub and through bioconda. The Lowe Lab also runs the tRNAscan-SE On-line search server for queries of under 1 million nucleotides. tRNAscan-SE generates the tRNA gene predictions in the Genomic tRNA Database (GtRNAdb).
