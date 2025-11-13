---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: snoRNABase (also known as snoRNA-LBME-db) is a comprehensive database
  of human C/D box and H/ACA box small nucleolar RNAs (snoRNAs) and small Cajal body-specific
  RNAs (scaRNAs). The database contains 361 entries including 257 C/D box snoRNAs,
  86 H/ACA snoRNAs, and 18 scaRNAs. It provides detailed information on snoRNA sequences,
  their genomic locations, host genes, target RNAs (rRNAs and spliceosomal RNAs),
  predicted base-pairing interactions with target nucleotides, and modification sites
  (2'-O-ribose methylation and pseudouridylation). Each entry includes literature
  references, GenBank accession numbers, and links to the UCSC Genome Browser. The
  database features search, browse, and "Find guide RNA" functions to identify snoRNAs
  that guide modifications of specific nucleotides in rRNAs (28S, 18S, 5.8S) and
  spliceosomal RNAs (U1, U2, U4, U5, U6, U12).
domains:
- genomics
homepage_url: https://www-snorna.biotoul.fr/
id: snornadatabase
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: snoRNABase
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing human snoRNA and scaRNA sequences,
    targets, and modifications
  format: http
  id: snornadatabase.portal
  name: snoRNABase Web Portal
  original_source:
  - snornadatabase
  product_url: https://www-snorna.biotoul.fr/
- category: GraphicalInterface
  description: Search engine for finding snoRNAs by name, length, GenBank accession,
    or target RNA
  format: http
  id: snornadatabase.search
  name: snoRNABase Search
  original_source:
  - snornadatabase
  product_url: https://www-snorna.biotoul.fr/cherche.php
- category: GraphicalInterface
  description: Tool for finding snoRNAs that guide modification of specific nucleotides
    in rRNAs and spliceosomal RNAs
  format: http
  id: snornadatabase.find_guide
  name: snoRNABase Find Guide RNA
  original_source:
  - snornadatabase
  product_url: https://www-snorna.biotoul.fr/guide.php
- category: GraphicalInterface
  description: Browse function for viewing and downloading snoRNA sequences in FASTA
    format
  format: http
  id: snornadatabase.browse
  name: snoRNABase Browse
  original_source:
  - snornadatabase
  product_url: https://www-snorna.biotoul.fr/browse.php
- category: ProgrammingInterface
  description: BLAST search interface for sequence similarity searches against human
    sno/scaRNAs
  format: http
  id: snornadatabase.blast
  name: snoRNABase BLAST
  original_source:
  - snornadatabase
  product_url: https://www-snorna.biotoul.fr/blast/
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
  - Laurent Lestrade
  - Michel J. Weber
  doi: 10.1093/nar/gkj002
  id: doi:10.1093/nar/gkj002
  journal: Nucleic Acids Research
  preferred: true
  title: 'snoRNA-LBME-db, a comprehensive database of human H/ACA and C/D box snoRNAs'
  year: '2006'
synonyms:
- snoRNA-LBME-db
- snoRNA database
---
# snoRNABase

## Overview

snoRNABase (formerly known as snoRNA-LBME-db) is a comprehensive database dedicated to human small nucleolar RNAs (snoRNAs) and small Cajal body-specific RNAs (scaRNAs). The database provides detailed annotations of modification guide RNAs that direct post-transcriptional modifications of ribosomal RNAs and spliceosomal RNAs.

## Database Content

Current version contains:

- **257 C/D box snoRNAs** (149 unique, accounting for large clusters)
- **86 H/ACA box snoRNAs**
- **18 scaRNAs** (composite guide RNAs)
- **Total: 361 entries**

### Functional Categories:
- Modification guide RNAs (targeting rRNAs and snRNAs)
- RNA chaperones (involved in pre-rRNA processing)
- Orphan snoRNAs (114 entries without documented target RNAs)

## snoRNA Biology

### C/D Box snoRNAs
- Guide 2'-O-ribose methylation of target RNAs
- Characterized by conserved boxes C (RUGAUGA) and D (CUGA)
- Contain 10-21 nt antisense elements upstream of D/D' boxes
- Part of snoRNPs with NOP1/fibrillarin, NOP56, NOP58, and NHP2L1

### H/ACA Box snoRNAs
- Guide pseudouridylation (isomerization of uridine to pseudouridine)
- Characterized by two hairpin structures with H box (ANANNA) and ACA motif
- Target uridine located 14-15 bp upstream of H/ACA box
- Associated with dyskerin, NOLA1 (GAR1), NOLA2 (NHP2), and NOLA3 (NOP10)

### scaRNAs (Small Cajal Body-Specific RNAs)
- Composite guide RNAs with C/D and/or H/ACA domains
- Guide modifications of RNA polymerase II transcribed snRNAs (U1, U2, U4, U5, U12)
- Accumulate in Cajal bodies rather than nucleoli

## Target RNAs

snoRNAs guide modifications in:
- **Ribosomal RNAs**: 28S, 18S, and 5.8S rRNA
- **Spliceosomal RNAs**: U1, U2, U4, U5, U6, and U12 snRNA

## Key Features

### Detailed Annotations
For each snoRNA entry:
- Sequence information and length
- GenBank accession number with hyperlink
- Host gene information and genomic location
- Target RNA(s) and nucleotide(s)
- Predicted base-pairing interactions (unique feature)
- Literature references with PubMed links
- UCSC Genome Browser integration
- FASTA format sequence download

### Search Functions

**Search Page**: Find snoRNAs by:
- Name (e.g., U85, ACA17, mgU12-22/U4-8)
- Partial names (e.g., "mg", "HBII-")
- Length
- GenBank accession number
- Target RNA (e.g., "28S" for 28S guides, "no" for orphan snoRNAs)

**Find Guide RNA**: Interactive tool showing:
- Which snoRNAs guide modification of specific nucleotides
- Base-pairing predictions for each modification site
- Coverage for 28S, 18S, 5.8S rRNAs and U1-U6, U12 snRNAs

**Browse**: Select and download snoRNA sequences in FASTA format

**BLAST**: Sequence similarity search against human sno/scaRNA database

## Reference Sequences

The database uses standardized reference sequences:
- **18S rRNA**: GenBank X03205
- **28S rRNA**: GenBank U13369 (nt 7935-12969)
- **5.8S rRNA**: GenBank U13369 (nt 6623-6779)

## UCSC Genome Browser Integration

snoRNAs from the database are included in the UCSC Genome Browser sno/miRNA track with:
- Color-coded display (C/D box, H/ACA box, scaRNAs)
- Clickable entries linking back to snoRNABase
- Integration with other genomic annotations

## Genomic Organization

- **Intronic localization**: Most sno/scaRNAs encoded in introns of host genes
- **Host gene diversity**: Range from ribosome biogenesis genes to non-coding genes
- **Independent transcription**: Some snoRNAs (U3, U8, U13, mgU2-25/61, mgU2-19/30, mgU12-22/U4-8) transcribed independently

## Special Features

### Large snoRNA Clusters
- **HBII-52 cluster**: 47 members (SNORD115@) from imprinted locus
- **HBII-85 cluster**: 27 members (SNORD116@) from Prader-Willi/Angelman syndrome locus
- **14q(I) cluster**: 9 members from chromosome 14 imprinted locus
- **14q(II) cluster**: 31 members from chromosome 14 imprinted locus

### Nomenclature
Database integrates various naming conventions:
- En, Un, ACAn, Zn nomenclature
- HBII-n, HBI-n (human orthologs of mouse snoRNAs)
- mgU-n (methylation guide) notation
- HUGO approved names for all human snoRNAs

## Data Sources

Database built through:
- Comprehensive literature compilation
- Experimentally verified snoRNAs
- Human orthologs of vertebrate snoRNAs
- Bioinformatic predictions from imprinted loci

## Citation

If using snoRNABase, please cite:

Lestrade, L., and Weber, M. J. (2006). snoRNA-LBME-db, a comprehensive database of human H/ACA and C/D box snoRNAs. *Nucleic Acids Research*, 34(Database issue), D158-162. doi:10.1093/nar/gkj002