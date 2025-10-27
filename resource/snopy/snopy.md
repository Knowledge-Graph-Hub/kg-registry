---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: snOPY (snoRNA Orthological Gene Database) provides comprehensive information about small nucleolar RNAs (snoRNAs), their gene loci, and target RNAs across multiple species. The database focuses on orthologous relationships between snoRNAs using target RNA conservation rather than snoRNA sequence similarity.
domains:
  - genomics
  - biological systems
homepage_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi
id: "snopy"
last_modified_date: '2025-10-27T00:00:00Z'
layout: resource_detail
name: snOPY
products:
  - category: GraphicalInterface
    description: Web portal for browsing and searching snoRNA orthological gene information
    format: http
    id: "snopy.portal"
    name: snOPY Portal
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi
  - category: GraphicalInterface
    description: Search interface for querying snoRNAs by species, box type, target RNA, organization, keywords, and curation status
    format: http
    id: "snopy.search"
    name: Search Interface
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi
  - category: GraphicalInterface
    description: Ortholog browser for exploring snoRNA orthologous relationships across species
    format: http
    id: "snopy.orthologs"
    name: Ortholog Browser
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi?mode=orthologs
  - category: GraphicalInterface
    description: Target RNA viewer for exploring modification sites on rRNA and snRNA targets
    format: http
    id: "snopy.target-rna"
    name: Target RNA Viewer
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi?mode=target
  - category: ProgrammingInterface
    description: BLAST interface for sequence similarity searches against snoRNA sequences
    format: http
    id: "snopy.blast"
    name: BLAST Interface
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi?mode=blast
  - category: Product
    description: Curated snoRNA sequences for box C/D class guiding 2'-O-methylation
    format: http
    id: "snopy.box-cd-snornas"
    name: Box C/D snoRNAs
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi
  - category: Product
    description: Curated snoRNA sequences for box H/ACA class guiding pseudouridylation
    format: http
    id: "snopy.box-haca-snornas"
    name: Box H/ACA snoRNAs
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi
  - category: Product
    description: Information about intronic snoRNA gene loci within protein-coding host genes
    format: http
    id: "snopy.intronic-loci"
    name: Intronic snoRNA Loci
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi
  - category: Product
    description: Information about polycistronic snoRNA gene clusters with multiple genes
    format: http
    id: "snopy.polycistronic-loci"
    name: Polycistronic snoRNA Loci
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi
  - category: Product
    description: Information about monocistronic snoRNA gene loci with single genes
    format: http
    id: "snopy.monocistronic-loci"
    name: Monocistronic snoRNA Loci
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi
  - category: Product
    description: Mapped modification sites on rRNA targets
    format: http
    id: "snopy.rrna-modifications"
    name: rRNA Modification Sites
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi?mode=target
  - category: Product
    description: Mapped modification sites on snRNA targets
    format: http
    id: "snopy.snrna-modifications"
    name: snRNA Modification Sites
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi?mode=target
  - category: Product
    description: Orthologous snoRNA relationships identified through target RNA conservation
    format: http
    id: "snopy.ortholog-data"
    name: snoRNA Ortholog Data
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi?mode=orthologs
  - category: DocumentationProduct
    description: About page with database description, methods, and citation information
    format: http
    id: "snopy.about"
    name: About snOPY
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi?mode=about
  - category: DocumentationProduct
    description: Database statistics showing organism coverage and entry counts
    format: http
    id: "snopy.statistics"
    name: Statistics
    product_url: http://snoopy.med.miyazaki-u.ac.jp/snorna_db.cgi?mode=statistics
publications:
  - authors:
      - Yoshihama
      - Nakao
      - Kenmochi
    id: "doi:10.1186/1756-0500-6-426"
    doi: 10.1186/1756-0500-6-426
    journal: BMC Research Notes
    preferred: true
    title: 'snOPY: a small nucleolar RNA orthological gene database'
    year: "2013"
---

# snOPY

snOPY (snoRNA Orthological Gene Database) is a specialized database dedicated to small nucleolar RNAs (snoRNAs) and their orthologous relationships across multiple species. Developed and maintained by the Kenmochi Laboratory at the University of Miyazaki, Japan, snOPY provides comprehensive information about snoRNA sequences, gene organization, and target modifications.

## Overview

Small nucleolar RNAs (snoRNAs) are a class of small non-coding RNAs that guide chemical modifications of other RNAs, primarily ribosomal RNAs (rRNAs) and small nuclear RNAs (snRNAs). snOPY focuses on cataloging these important regulatory molecules and their evolutionary relationships.

## Database Content

### snoRNA Classes

snOPY contains information about two major classes of snoRNAs:

1. **Box C/D snoRNAs**:
   - Contain conserved sequence motifs: Box C (TGATGA) and Box D (CTGA)
   - Guide 2'-O-methylation of target RNAs
   - Modification occurs 5 nucleotides upstream of box D or D'
   - Complementary region upstream of boxes pairs with target RNA

2. **Box H/ACA snoRNAs**:
   - Contain conserved sequence motifs: Box H (ANANNA) and Box ACA (ACA)
   - Guide pseudouridylation (conversion of uridine to pseudouridine)
   - Modification site located in pseudouridylation pocket
   - Formed by RNA:RNA antisense interaction with target

### snoRNA Gene Organization

snOPY catalogs three types of snoRNA gene loci:

- **Intronic**: snoRNA gene located within intron of protein-coding host gene; transcribed using host gene promoter
- **Polycistronic**: Multiple snoRNA genes organized in cluster; transcribed from single promoter
- **Monocistronic**: Single snoRNA gene expressed using its own promoter

### Target RNAs

The database provides information about:
- **rRNA targets**: Modified nucleotides in ribosomal RNA
- **snRNA targets**: Modified nucleotides in small nuclear RNA
- **Orphan snoRNAs**: snoRNAs whose targets remain to be determined

## Species Coverage

snOPY contains snoRNA data for over 50 organisms across multiple domains of life, including:

### Mammals
- Homo sapiens (760 entries)
- Mus musculus (968 entries)
- Rattus norvegicus (1,065 entries)
- Gorilla gorilla (1,083 entries)
- Macaca mulatta (655 entries)
- And many other mammalian species

### Other Vertebrates
- Gallus gallus (chicken)
- Danio rerio (zebrafish)
- Xenopus tropicalis (frog)

### Invertebrates
- Drosophila melanogaster (248 entries)
- Caenorhabditis elegans (91 entries)
- Ciona intestinalis and C. savignyi (tunicates)

### Fungi
- Saccharomyces cerevisiae (77 entries)
- Schizosaccharomyces pombe (58 entries)

### Plants
- Arabidopsis thaliana (220 entries)
- Oryza sativa (rice, 236 entries)
- Triticum aestivum (wheat, 741 entries)
- Hordeum vulgare (barley, 455 entries)
- Physcomitrium patens (moss, 75 entries)

## Key Features

### Ortholog Identification

snOPY uses a unique approach to identify snoRNA orthologs:
- Traditional sequence similarity methods (e.g., BLAST) often fail due to low sequence conservation between snoRNAs from different species
- Instead, snOPY focuses on conservation of **target RNA sequences** (rRNA, snRNA)
- Target RNAs are aligned across species using ClustalW
- Modification sites are mapped onto alignments
- If modified nucleotides align at the same position, corresponding snoRNAs are considered orthologs

This target-based approach is more reliable than direct snoRNA sequence comparison for identifying evolutionary relationships.

### Data Curation

- snoRNA data collected from public databases
- Manual curation according to sequence annotation
- Curation status tracking for data quality assurance

### Search and Browse Capabilities

Users can search and filter by:
- **Species**: Over 50 organisms
- **Box type**: C/D or H/ACA class
- **Target RNA**: Specific rRNA or snRNA targets
- **Organization**: Intronic, polycistronic, or monocistronic
- **Keywords**: Free-text search
- **Curation status**: Quality filtering

### BLAST Interface

Sequence similarity searches against snOPY snoRNA sequences for:
- Identifying novel snoRNAs in new sequences
- Finding homologous snoRNAs across species
- Characterizing unidentified snoRNA candidates

## Integration with External Resources

snOPY is integrated with RNAcentral, contributing yeast and other organism snoRNA data to this comprehensive non-coding RNA database. Updates are regularly synchronized with RNAcentral releases.

## Sister Database

snOPY is part of a suite of databases from the Kenmochi Laboratory:
- **RPG (Ribosomal Protein Gene Database)**: Complementary resource for ribosomal protein genes

## Citation

If snOPY assists your research, please cite:

Yoshihama M, Nakao A, Kenmochi N (2013). "snOPY: a small nucleolar RNA orthological gene database." BMC Research Notes, 6:426.

## Copyright and Usage

- **Academic users**: May freely use and link to the snOPY website
- **Non-academic users**: May use as end users for academic purposes; other uses require permission

snOPY is an original database product, copyright Kenmochi Laboratories.

## Contact

Contact address available at the snOPY website.

Developed and maintained by:
**Medical Biology, Faculty of Medicine, University of Miyazaki**

**Last Database Updates**:
- 2024-06-01: Triticum dicoccoides data updated
- 2024-03-26: RNAcentral release 24 integration
- 2023-11-30: RNAcentral release 23 integration
- 2023-08-01: Triticum aestivum data updated
- 2022-12-01: Gorilla gorilla data available
