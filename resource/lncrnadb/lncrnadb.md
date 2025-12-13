---
activity_status: inactive
category: DataSource
creation_date: '2010-11-25T00:00:00Z'
description: A reference database for long noncoding RNAs (lncRNAs) that have been
  shown to have, or be associated with, biological functions in eukaryotes. Contained
  over 150 lncRNAs from around 60 different species with comprehensive annotations
  including sequences, structural information, genomic context, expression, subcellular
  localization, conservation, and functional evidence.
domains:
- genomics
- biological systems
homepage_url: http://www.lncrnadb.org/
id: lncrnadb
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: lncRNAdb
products:
- category: GraphicalInterface
  description: Main web portal for searching and browsing long noncoding RNAs by name,
    sequence, species, or annotations
  format: http
  id: lncrnadb.portal
  name: lncRNAdb Portal
  product_url: http://www.lncrnadb.org/
- category: GraphicalInterface
  description: Search interface supporting queries by lncRNA name or alias, nucleotide
    sequence string, species, annotation status, and full-text search
  format: http
  id: lncrnadb.search
  name: Search Interface
  product_url: http://www.lncrnadb.org/
- category: Product
  description: Tab-delimited file download of search results
  format: tsv
  id: lncrnadb.export
  name: Export Results
  product_url: http://www.lncrnadb.org/
- category: GraphicalInterface
  description: Integration with UCSC Genome Browser for genomic context visualization
  format: http
  id: lncrnadb.ucsc-integration
  name: UCSC Genome Browser Integration
- category: GraphicalInterface
  description: Integration with Noncoding RNA Expression Database (NRED) for expression
    information from various sources
  format: http
  id: lncrnadb.nred-integration
  name: NRED Integration
- category: DocumentationProduct
  description: User submission interface for adding new entries and updating existing
    data with published information
  format: http
  id: lncrnadb.submit
  name: User Submission System
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
  - Paulo P Amaral
  - Michael B Clark
  - Dennis K Gascoigne
  - Marcel E Dinger
  - John S Mattick
  id: https://doi.org/10.1093/nar/gkq1138
  journal: Nucleic Acids Research
  preferred: true
  title: 'lncRNAdb: a reference database for long noncoding RNAs'
  year: '2011'
warnings:
- This database is no longer active and the website is no longer accessible.
taxon:
- NCBITaxon:2759
---
# lncRNAdb

lncRNAdb was a comprehensive reference database for long noncoding RNAs (lncRNAs) that have been shown to have, or be associated with, biological functions in eukaryotes. The database was developed to enable systematic compilation and updating of information about lncRNAs in response to the rapid increase in their identification and characterization across multiple species.

## Database Contents

The database contained over 150 lncRNAs identified from the literature in around 60 different species. Each entry included a comprehensive range of available information about the RNA, including:

- **Sequences and Structural Information**: Complete sequence data and structural annotations
- **Genomic Context**: Chromosomal location and genomic coordinates with hyperlinks to UCSC Genome Browser
- **Expression Profiles**: Tissue-specific and developmental expression patterns
- **Subcellular Localization**: Nuclear, cytoplasmic, or other subcellular locations
- **Conservation**: Evolutionary conservation across species
- **Functional Evidence**: Results from loss- or gain-of-function experiments
- **Literature References**: Hyperlinked to PubMed
- **Associated Biological Components**: Genomically-associated genes and interacting proteins

Approximately 100 entries had functions directly tested by in vitro and/or in vivo experiments, representing lncRNAs from vertebrates to single-celled eukaryotes.

## Database Categories

The database organized lncRNAs into several functional categories:

### Imprinted lncRNAs
LncRNAs prevalent in imprinted regions that function to control imprinting and expression of other genes, such as Air and Kcnq1ot1, as well as host genes for small RNAs.

### Disease-Associated lncRNAs
LncRNAs implicated in various diseases including cancer (NDM29, HOTAIR, H19), neurological conditions (BACE1AS in Alzheimer's disease), and complex disease susceptibility loci (ANRIL associated with coronary artery disease, type 2 diabetes, periodontitis, and cancer).

### Pathogen-Induced or Derived lncRNAs
LncRNAs produced and modulated by pathogens or host cells during infection, including eukaryotic parasite transcripts, virus-induced mammalian lncRNAs (Neat1/VINC), and lncRNAs encoded by oncogenic viruses (β2.7 from HCMV).

### Bifunctional RNAs
Genes encoding RNAs with multiple independent roles, acting as both regulatory lncRNAs and encoding proteins, such as SRA transcript isoforms and p53 transcripts.

### lncRNAs of Unknown Function
Well-described RNAs with characterized structural and expression properties but undiscovered functions, showing tissue specificity and dynamic expression during development.

## Technical Implementation

The database was built on Microsoft ASP.NET 3.5 presentation layer (C#), C# 4.0 data model and application layer, and MySQL persistent storage. Literature references and genomic coordinates were hyperlinked to PubMed and UCSC Genome Browser respectively.

## Integration with Other Resources

lncRNAdb was integrated with:
- **UCSC Genome Browser**: For genomic context visualization
- **Noncoding RNA Expression Database (NRED)**: Providing access to relative expression levels in various public microarray experiments including NCode data, GNF atlas, and Allen Brain Atlas (with in situ expression data for over 800 expressed lncRNAs)

## Database Definition

The database defined lncRNAs as noncoding RNAs that may have a function as either primary or spliced transcripts, independent of processing into known classes of small RNAs (miRNAs, piRNAs, snoRNAs), while excluding structural RNAs from classical housekeeping families (tRNAs, snoRNAs, spliceosomal RNAs). Some lncRNAs that are host genes for small RNA species but may also have roles as regulatory lncRNAs were included, such as GAS5.

## Historical Context

As of the publication date (2010), the database addressed a critical need for centralized cataloging of lncRNAs across all eukaryotic species, as previous databases like RNAdb were limited to mammals and included all classes of regulatory RNAs. lncRNAdb provided a dedicated resource specifically for long noncoding RNAs with the aim of decreasing instances of replication and unknown identity by including comprehensive alias information.

Most catalogued lncRNAs (~75%) were from mammals due to more available transcriptomic data and intensive study, but the database included lncRNAs from diverse eukaryotic species including yeast, Neurospora crassa, Caenorhabditis elegans, plants, frogs, and Drosophila.