---
layout: resource_detail
id: ensembl
name: Ensembl
description: A genome browser for vertebrate genomes that supports research in comparative genomics, evolution, sequence variation, and transcriptional regulation
domains:
  - genomics
  - bioinformatics
  - sequence variation
  - comparative genomics
  - translational
contacts:
  - category: Organization
    label: Ensembl Help Desk
    contact_details:
      - contact_type: email
        value: helpdesk@ensembl.org
license:
  id: http://www.apache.org/licenses/LICENSE-2.0
  label: Apache License, Version 2.0
homepage_url: https://www.ensembl.org
repository: https://github.com/Ensembl/
category: DataSource
activity_status: active
infores_id: ensembl
products:
  - id: ensembl.browser
    name: Ensembl Genome Browser
    description: A web-based platform for browsing and analyzing vertebrate genomes, including gene annotations, comparative genomics, and variation data.
    product_url: https://www.ensembl.org
    category: GraphicalInterface
  - id: ensembl.biomart
    name: BioMart
    description: A data mining tool that allows extraction of data without programming knowledge or understanding of the underlying database structure.
    product_url: https://www.ensembl.org/biomart/martview
    category: GraphicalInterface
  - id: ensembl.vep
    name: Variant Effect Predictor (VEP)
    description: A tool to analyze variants and predict the functional consequences of known and unknown variants.
    product_url: https://www.ensembl.org/info/docs/tools/vep/
    category: ProcessProduct
  - id: ensembl.blast
    name: BLAST/BLAT
    description: Tool to search Ensembl genomes for DNA or protein sequences.
    product_url: https://www.ensembl.org/Multi/Tools/Blast
    category: ProcessProduct
  - id: ensembl.api.perl
    name: Ensembl Perl API
    description: Programmatic access to all Ensembl data using Perl scripts.
    product_url: https://github.com/Ensembl/
    repository: https://github.com/Ensembl/
    category: ProgrammingInterface
  - id: ensembl.api.rest
    name: Ensembl REST API
    description: RESTful API that allows access to Ensembl data using various programming languages.
    product_url: https://rest.ensembl.org
    category: ProgrammingInterface
publications:
  - id: https://doi.org/10.1093/nar/gkae1071
    preferred: true
    title: Ensembl 2025
    authors:
        - Dyer SC
        - Austine-Orimoloye O
        - Azov AG
        - Barba M
        - Barnes I
        - Barrera-Enriquez VP
        - Becker A
        - Bennett R
        - Beracochea M
        - Berry A
        - Ensembl team
    journal: Nucleic Acids Research
    year: 2025
    doi: doi:10.1093/nar/gkae1071
---

## Ensembl

Ensembl is a genome browser for vertebrate genomes that supports research in comparative genomics, evolution, sequence variation, and transcriptional regulation. It provides comprehensive annotation of genes, computes multiple alignments, predicts regulatory function, and collects disease data.

### Overview

Ensembl annotates genes, computes multiple alignments, predicts regulatory function, and collects disease data across a wide range of vertebrate species. The project is based at EMBL-EBI (European Molecular Biology Laboratory's European Bioinformatics Institute) and its software and data are freely available.

### Key Features

- **Genome Browser**: Interactive visualization of genomic regions with annotations
- **Gene Annotation**: Comprehensive gene models and transcripts
- **Comparative Genomics**: Tools for comparing genomes across species
- **Variation Data**: Information on genetic variants and their effects
- **Regulatory Features**: Prediction and annotation of regulatory elements
- **Data Export**: Custom data extraction through BioMart and APIs

### Tools and Services

#### BioMart

BioMart is a highly customizable data mining tool that allows extraction of data without any programming knowledge. Users can create complex queries to extract specific datasets across various Ensembl databases.

#### Variant Effect Predictor (VEP)

VEP analyzes variants and predicts their functional consequences. It can be used both through a web interface and as a command-line tool for larger datasets. VEP supports various input formats and provides detailed annotations for variants.

#### BLAST/BLAT

Tools for searching Ensembl genomes with DNA or protein sequences to identify similar regions or homologs.

#### Ensembl REST API

A RESTful API that provides programmatic access to Ensembl data, allowing developers to integrate Ensembl data into their own applications using any programming language.

#### Ensembl Perl API

A comprehensive set of Perl modules for programmatic access to all Ensembl data, enabling complex queries and data manipulation.

### Sister Resources

Ensembl has several specialized sister resources focused on specific taxonomic groups:

- Ensembl Bacteria
- Ensembl Fungi
- Ensembl Plants
- Ensembl Protists
- Ensembl Metazoa

### Data Access

Ensembl data can be accessed through:

1. **Web Interface**: The primary way to browse and visualize genomic data
2. **BioMart**: For custom data extraction and filtering
3. **REST API**: For programmatic access from any language
4. **Perl API**: For more complex programmatic access
5. **FTP Downloads**: For bulk data download

### Versioning and Updates

Ensembl follows a regular release cycle, with each release bringing updated genome assemblies, gene annotations, and new features. Archives of previous releases are maintained to ensure reproducibility of research based on specific versions.
