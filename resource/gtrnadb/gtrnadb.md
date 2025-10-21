---
activity_status: active
category: DataSource
creation_date: '2009-01-05T00:00:00Z'
description: The Genomic tRNA Database (GtRNAdb) is a comprehensive repository of
  transfer RNA (tRNA) gene predictions identified by tRNAscan-SE in complete and draft
  genomes across all domains of life. The database contains over 431,000 tRNA gene
  predictions from 4,867 genomes (609 eukaryotes, 220 archaea, and 4,038 bacteria)
  as of Data Release 22 (September 2024). GtRNAdb provides detailed annotations including
  tRNA sequences, predicted secondary structures, isotype-specific scoring, genomic
  context via UCSC Genome Browser integration, and functional data such as RNA modifications
  from MODOMICS, tRNA fragment expression profiles, genomic variants from dbSNP, epigenetic
  information from ENCODE, and evolutionary conservation across species. The database
  enables comparative analysis through search capabilities by phylogenetic domain,
  species, amino acid isotypes, anticodons, tRNA scores, structural features, and
  sequence similarity via BLAST.
domains:
- genomics
- biological systems
homepage_url: https://gtrnadb.org/
id: gtrnadb
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: GtRNAdb
products:
- category: GraphicalInterface
  description: Web portal for browsing tRNA gene predictions organized by phylogenetic
    domain and species
  format: http
  id: gtrnadb.portal
  name: GtRNAdb Web Portal
  product_url: https://gtrnadb.org/
- category: GraphicalInterface
  description: Browse tRNA predictions organized by phylogenetic taxonomy (Eukaryota,
    Archaea, Bacteria)
  format: http
  id: gtrnadb.browse
  name: Browse by Phylogeny
  product_url: https://gtrnadb.org/browse.html
- category: GraphicalInterface
  description: Search tRNAs by species, amino acid isotype, anticodon, intron count,
    tRNA score, and structural features
  format: http
  id: gtrnadb.sifter
  name: tRNA Sifter
  product_url: https://gtrnadb.org/search.html
- category: GraphicalInterface
  description: BLAST search interface for sequence similarity searches against all
    tRNAs in the database
  format: http
  id: gtrnadb.blast
  name: Search by Sequence (BLAST)
  product_url: https://gtrnadb.org/blast.html
- category: DocumentationProduct
  description: Frequently asked questions about GtRNAdb and tRNA gene predictions
  format: http
  id: gtrnadb.faq
  name: FAQ
  product_url: https://gtrnadb.org/faq.html
- category: DocumentationProduct
  description: Comprehensive user guide for GtRNAdb features and search capabilities
  format: http
  id: gtrnadb.docs
  name: User Guide
  product_url: https://gtrnadb.org/docs/
- category: Product
  description: Archive of previous GtRNAdb data releases with change logs
  format: http
  id: gtrnadb.archives
  name: Previous Releases Archive
  product_url: https://gtrnadb.org/archives.html
- category: GraphicalInterface
  description: Web portal for searching and browsing ncRNA sequences, structures,
    and annotations
  format: http
  id: rnacentral.portal
  name: RNAcentral Portal
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to RNAcentral data
  format: http
  id: rnacentral.api
  name: RNAcentral REST API
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/api
- category: Product
  description: FTP archive with current and archived release files (sequences and
    annotations)
  format: http
  id: rnacentral.ftp
  name: RNAcentral FTP Archive
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
- category: DataModelProduct
  description: Public PostgreSQL database for direct SQL access to RNAcentral data
  format: postgres
  id: rnacentral.public-db
  name: RNAcentral Public Postgres Database
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/help/public-database
publications:
- authors:
  - Patricia P. Chan
  - Todd M. Lowe
  id: https://doi.org/10.1093/nar/gkv1309
  journal: Nucleic Acids Research
  preferred: true
  title: 'GtRNAdb 2.0: an expanded database of transfer RNA genes identified in complete
    and draft genomes'
  year: '2016'
- authors:
  - Patricia P. Chan
  - Todd M. Lowe
  id: https://doi.org/10.1093/nar/gkn787
  journal: Nucleic Acids Research
  title: 'GtRNAdb: A database of transfer RNA genes detected in genomic sequence'
  year: '2009'
---
# GtRNAdb

The Genomic tRNA Database (GtRNAdb) is a comprehensive repository for transfer RNA gene predictions made by tRNAscan-SE on complete or nearly complete genomes across all three domains of life. Created and maintained by Todd Lowe and Patricia Chan at UC Santa Cruz, GtRNAdb has become the most commonly cited web-based source of tRNA gene information.

As of Data Release 22 (September 2024), the database contains 431,433 tRNA gene predictions from 4,867 genomes, including 609 eukaryotes (178,889 tRNAs), 220 archaea (10,476 tRNAs), and 4,038 bacteria (242,068 tRNAs). The database focuses on high-quality predictions, excluding predicted pseudogenes and, for large eukaryotes, primary and secondary filtered predictions.

GtRNAdb provides rich annotations for each tRNA gene, including primary sequences, predicted secondary structures (both from covariance model alignment and minimum free energy prediction), isotype-specific scoring, genomic coordinates with direct links to UCSC Genome Browsers, flanking sequences for regulatory motif identification, and detailed scoring breakdowns to identify potential pseudogenes.

The database integrates extensive functional data from external sources including RNA modification data from MODOMICS, tRNA fragment expression profiles from ARM-seq studies, single nucleotide polymorphisms from dbSNP with predicted structural impacts, epigenetic data from ENCODE showing RNA polymerase III transcription factor binding, and evolutionary conservation through multi-genome alignments.

Search capabilities include the tRNA Sifter for querying by phylogenetic domain, species name, chromosome, amino acid isotype, anticodon, number of introns, tRNA score thresholds, and structural mismatches. A BLAST server enables sequence similarity searches across all tRNAs in the database. Additional tools include tRNAscan-SE for custom predictions, tRAX for tRNA-derived RNA sequencing analysis, tDRnamer for standardized naming, and tRAP for predicting tRNA gene activity.

GtRNAdb serves as an indispensable platform for comparative genomics, tRNA biology research, and understanding the regulatory roles of tRNAs across all domains of life.