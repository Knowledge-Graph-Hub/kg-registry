---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: A comprehensive database dedicated to long non-coding RNA (lncRNA) annotation
  in animals and plants, providing systematic nomenclature, sequence information,
  genome location, expression profiles, functional predictions, and conservation analysis
  across 39 species (16 animals and 23 plants)
domains:
- genomics
- biological systems
homepage_url: http://www.noncode.org/
id: noncode
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: NONCODE
products:
- category: GraphicalInterface
  description: Main web interface for searching, browsing, and analyzing lncRNA annotations
    across 39 species
  format: http
  id: noncode.portal
  name: NONCODE Web Portal
  product_url: http://www.noncode.org/
- category: GraphicalInterface
  description: Browse lncRNAs by species and RNA type
  format: http
  id: noncode.browse
  name: Browse NONCODE
  product_url: http://www.noncode.org/browse.php
- category: GraphicalInterface
  description: Search for specific genes or transcripts by identifier or keywords
  format: http
  id: noncode.search
  name: Search Gene/Transcript
  product_url: http://www.noncode.org/search.php
- category: GraphicalInterface
  description: Find similar sequences using BLAST alignment
  format: http
  id: noncode.blast
  name: BLAST Similarity Search
  product_url: http://www.noncode.org/blast.php
- category: GraphicalInterface
  description: Browse disease-related lncRNA information, especially cancer associations
  format: http
  id: noncode.disease
  name: Disease Information
  product_url: http://www.noncode.org/disease.php
- category: GraphicalInterface
  description: View transcript locations in genomic context (human hg38)
  format: http
  id: noncode.genome-browser
  name: Genome Browser
  product_url: http://www.noncode.org/genome.php
- category: Product
  description: Download complete lncRNA annotations and sequences
  format: http
  id: noncode.download
  name: Download Data
  product_url: http://www.noncode.org/download.php
  warnings:
  - File was not able to be retrieved when checked on 2025-12-18_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-18: HTTP 403 error
    when accessing file'
- category: GraphicalInterface
  description: Predicted functions for plant lncRNAs based on co-expression analysis
  format: http
  id: noncode.function
  name: Function Prediction
  product_url: http://www.noncode.org/function.php
- category: GraphicalInterface
  description: Cross-species conservation analysis for plant lncRNAs
  format: http
  id: noncode.conservation
  name: Conservation Analysis
  product_url: http://www.noncode.org/conservation.php
- category: GraphicalInterface
  description: Convert between NONCODE IDs and other database identifiers (Ensembl,
    RefSeq, etc.)
  format: http
  id: noncode.id-conversion
  name: ID Conversion Tool
  product_url: http://www.noncode.org/id_conversion.php
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
- doi: 10.1093/nar/gkaa1046
  id: zhao2021noncode
  preferred: true
  title: 'NONCODEV6: an updated database dedicated to long non-coding RNA annotation
    in both animals and plants'
  year: '2021'
synonyms:
- NONCODEV6
- NONCODE v6.0
- NONCODE 2021
taxon:
- NCBITaxon:33090
---
---

## NONCODE

NONCODE is a comprehensive database dedicated to the annotation of long non-coding RNAs (lncRNAs) in both animals and plants. NONCODE v6.0 contains 644,510 lncRNA transcripts from 39 species, including 16 animals and 23 plants.

### Human and Mouse lncRNAs

- **Human**: 173,112 lncRNA transcripts representing 96,411 genes
- **Mouse**: 131,974 lncRNA transcripts representing 87,890 genes
- Includes expression profiles and predicted functions
- Features 13,749 records of lncRNA-cancer associations from experimentally supported data

### Plant lncRNAs

- **23 plant species** with 94,697 lncRNAs from 68,808 genes
- Species include: *Arabidopsis thaliana*, *Cucumis sativus*, *Brassica napus*, *Brassica rapa*, *Chenopodium quinoa*, *Chlamydomonas reinhardtii*, *Glycine max*, *Gossypium raimondii*, *Malus domestica*, *Manihot esculenta*, *Medicago truncatula*, *Musa acuminata*, *Oryza rufipogon*, *Oryza sativa*, *Physcomitrella patens*, *Populus trichocarpa*, *Solanum lycopersicum*, *Solanum tuberosum*, *Triticum aestivum*, *Theobroma cacao*, *Trifolium pratense*, *Vitis vinifera*, *Zea mays*

### Database Features

#### Tissue Expression Profiles
NONCODE provides tissue-specific expression data for five model plants:
- *Arabidopsis thaliana* (10 tissues)
- *Zea mays* (9 tissues)
- *Solanum lycopersicum* (6 tissues)
- *Cucumis sativus* (8 tissues)
- *Oryza sativa* (11 tissues)

Expression levels quantified as transcripts per kilobase million (TPM) using STAR alignment and StringTie quantification.

#### Functional Annotation
For five plant species, co-expression analysis with coding genes enables functional prediction:
- Pearson correlation coefficients (Pcc) calculated using WGCNA
- Gene pairs with P-value < 0.05 and Pcc > 0.999 or < -0.999 considered co-expressed
- GO term annotation performed using PANTHER classification system

#### Conservation Analysis
- Transcript-level conservation assessment across 23 plant species
- BLASTn-based pairwise comparisons with E-value threshold of 1e-10
- 122 orthologous lncRNAs identified meeting ≥50% query coverage and E-value ≤1e-10
- Notable conservation in closely related pairs: *Brassica napus*/*Brassica rapa*, *O. rufipogon*/*O. sativa*, *S. lycopersicum*/*S. tuberosum*

#### Disease Associations
- Focus on lncRNA-cancer relationships in human
- Integration from six databases: LncSpA, LncTarD, Lnc2Cancer, LncRNADisease, LncRNAWiki, MNDR
- Only experimentally supported relationships included (computational predictions excluded)
- Top cancers by number of associated lncRNAs documented

### Data Processing Pipeline

1. **Format normalization**: All data converted to bed or gtf formats based on single assembly versions
2. **Multi-source combination**: Normalized data combined using Cuffcompare from Cufflinks suite
3. **Protein-coding filtration**: 
   - Comparison with RefSeq and Ensembl coding RNAs
   - CNIT (Coding-NonCoding Identifying Tool) validation with 99.3% accuracy on plant transcripts
4. **General information**: Location, exons, length, assembly sequence, and source documented
5. **Conservation analysis**: BLAST-based cross-species transcript comparisons
6. **Web presentation**: Comprehensive web interface with visualization tools

### Nomenclature System

NONCODE follows a systematic naming convention:
- **Transcripts**: NON + three species characters + T + six sequential numbers (e.g., NONATHT000001.1)
- **Genes**: NON + three species characters + G + six sequential numbers

### Data Sources

Integration from multiple sources:
- Previous NONCODE versions
- Public literature (57,872 plant articles, 51,771 new human/mouse articles since 2017)
- External lncRNA databases: Ensembl, RefSeq, lncRNAdb, LNCipedia, CANTATAdb, GREENC

### Key Statistics

- **Total transcripts**: 644,510 lncRNAs
- **Species coverage**: 16 animals, 23 plants
- **Plant lncRNAs**: Average length 462-1,033 bp; average 1.3-2.3 exons per lncRNA
- **Database growth**: Increased from 548,640 lncRNAs (v5, 2017) to 644,510 lncRNAs (v6, 2021)
---
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
warnings:
- This is an automatically generated stub page. Please replace with accurate information
  about this resource.
---
# Noncode

This is an automatically generated stub page for noncode. Please update with proper information.