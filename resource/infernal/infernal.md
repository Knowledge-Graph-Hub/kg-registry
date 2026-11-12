---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: sean@eddylab.org
  - contact_type: url
    value: http://eddylab.org/
  - contact_type: github
    value: EddyRivasLab
  label: Eddy/Rivas Lab, Department of Molecular and Cellular Biology, Harvard University
creation_date: '2026-11-12T00:00:00Z'
description: Infernal ("INFERence of RNA ALignment") is software from the Eddy/Rivas
  lab for searching DNA sequence databases for RNA structure and sequence similarities.
  It implements covariance models (CMs), a special case of profile stochastic context-free
  grammars that score a combination of sequence consensus and RNA secondary structure
  consensus, so it can find structural RNA homologs that conserve secondary structure
  more than primary sequence. cmbuild builds a CM from a structure-annotated multiple
  sequence alignment, cmsearch and cmscan search sequence databases with CMs, cmalign
  aligns sequences to a CM, and cmcalibrate calibrates E-values. Infernal 1.1 added
  an HMM filter pipeline that made searches about 100-fold faster than version 1.0.
  Infernal is the software engine underlying the Rfam database of RNA families and
  the covariance model search engine of tRNAscan-SE 2.0. It uses the HMMER package
  and the Easel library, and is distributed as open source under the BSD three-clause
  license.
domains:
- genomics
- non-coding RNA
- information technology
- software
funding:
- National Library of Medicine (NLM), NIH Intramural Research Program
- National Human Genome Research Institute (NHGRI) (R01HG009116)
homepage_url: http://eddylab.org/infernal/
id: infernal
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/BSD-3-Clause
  label: BSD-3-Clause
name: Infernal
products:
- category: ProcessProduct
  description: Infernal source code repository on GitHub, used for Infernal development.
    Building from the repository also requires the HMMER and Easel repositories
    from EddyRivasLab. Release tags up to infernal-1.1.5 are kept in the repository.
  format: mixed
  id: infernal.software
  latest_version: 1.1.5
  license:
    id: https://opensource.org/licenses/BSD-3-Clause
    label: BSD-3-Clause
  name: Infernal Software Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: infernal
  product_url: https://github.com/EddyRivasLab/infernal
  repository: https://github.com/EddyRivasLab/infernal
  rrid: SCR_011809
- category: ProcessProduct
  compression: gzip
  description: Infernal 1.1.5 (7 Sep 2023) source code distribution, a gzipped tar
    archive that includes the bundled HMMER and Easel sources. Older releases from
    0.1 onward are linked from the Infernal homepage.
  format: mixed
  id: infernal.source-tarball
  latest_version: 1.1.5
  license:
    id: https://opensource.org/licenses/BSD-3-Clause
    label: BSD-3-Clause
  name: Infernal Source Code Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: infernal
  product_file_size: 31300142
  product_url: http://eddylab.org/infernal/infernal-1.1.5.tar.gz
- category: ProcessProduct
  compression: gzip
  description: Infernal 1.1.5 source distribution with precompiled Linux/Intel binaries.
    Equivalent archives with binaries for macOS on Apple Silicon and macOS on Intel
    are linked from the Infernal homepage.
  format: mixed
  id: infernal.linux-binaries
  latest_version: 1.1.5
  license:
    id: https://opensource.org/licenses/BSD-3-Clause
    label: BSD-3-Clause
  name: Infernal Linux/Intel Binaries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: infernal
  product_file_size: 48407521
  product_url: http://eddylab.org/infernal/infernal-1.1.5-linux-intel-gcc.tar.gz
- category: ProcessProduct
  description: Infernal packaged for the conda package manager in the bioconda channel.
    Infernal is also packaged for Debian (infernal, infernal-doc) and Homebrew (brewsci/bio).
  format: mixed
  id: infernal.bioconda
  latest_version: 1.1.5
  name: Infernal Bioconda Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: infernal
  product_url: https://anaconda.org/bioconda/infernal
- category: DocumentationProduct
  description: Infernal User's Guide (PDF, 119 pages), with installation instructions,
    a tutorial, descriptions of the search pipeline, file formats and manual pages
    for each program.
  format: pdf
  id: infernal.userguide
  name: Infernal User's Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: infernal
  product_file_size: 933447
  product_url: http://eddylab.org/infernal/Userguide.pdf
- category: DocumentationProduct
  description: Release notes for Infernal 1.1.5, listing the changes from 1.1.4.
  format: markdown
  id: infernal.release-notes
  name: Infernal 1.1.5 Release Notes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: infernal
  product_url: http://eddylab.org/infernal/RELEASE-1.1.5.md
- category: Product
  compression: gzip
  description: Files for reproducing the internal RMARK3 benchmark of RNA homology
    search reported in the Infernal 1.1 Bioinformatics publication.
  format: mixed
  id: infernal.rmark3-benchmark
  name: Infernal 1.1 RMARK3 Benchmark
  original_source:
  - relation_type: prov:hadPrimarySource
    source: infernal
  product_file_size: 11469486
  product_url: http://eddylab.org/infernal/i1.1-benchmark-rmark3.tar.gz
- category: Product
  description: Covariance models for all RNA families in CM format
  format: txt
  id: rfam.cm-models
  name: Rfam Covariance Models
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rfam
  product_file_size: 45111170
  product_url: https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/Rfam.cm.gz
  secondary_source:
  - relation_type: prov:used
    source: infernal
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
publications:
- authors:
  - Nawrocki EP
  - Eddy SR
  doi: 10.1093/bioinformatics/btt509
  id: doi:10.1093/bioinformatics/btt509
  journal: Bioinformatics
  preferred: true
  title: 'Infernal 1.1: 100-fold faster RNA homology searches'
  year: '2013'
- authors:
  - Nawrocki EP
  - Kolbe DL
  - Eddy SR
  doi: 10.1093/bioinformatics/btp157
  id: doi:10.1093/bioinformatics/btp157
  journal: Bioinformatics
  title: 'Infernal 1.0: inference of RNA alignments'
  year: '2009'
repository: https://github.com/EddyRivasLab/infernal
rrid: SCR_011809
synonyms:
- INFERence of RNA ALignment
version: 1.1.5
---
# Infernal

Infernal ("INFERence of RNA ALignment") is software from Sean Eddy's lab (Eddy/Rivas Lab, Harvard University) for finding structural RNA homologs in DNA sequence databases. It implements covariance models (CMs), profile stochastic context-free grammars that score both sequence consensus and RNA secondary structure consensus. `cmbuild` builds a CM from a structure-annotated multiple sequence alignment, `cmsearch` and `cmscan` search sequence databases, `cmalign` aligns sequences to a model, and `cmcalibrate` calibrates E-values. Infernal 1.1 (Nawrocki and Eddy, 2013) added an HMM filter pipeline that made searches about 100-fold faster than version 1.0.

Infernal is the software engine behind the Rfam database of RNA families and is the covariance model search engine used by tRNAscan-SE 2.0. The current release is 1.1.5 (September 2023), distributed under the BSD three-clause license as a source tarball, as prebuilt Linux and macOS binaries, and through bioconda, Debian and Homebrew. Development happens on GitHub.
