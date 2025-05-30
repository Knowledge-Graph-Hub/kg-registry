---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: helpdesk@ensembl.org
  label: Ensembl Help Desk
description: A genome browser for vertebrate genomes that supports research in comparative
  genomics, evolution, sequence variation, and transcriptional regulation
domains:
- genomics
homepage_url: https://www.ensembl.org
id: ensembl
infores_id: ensembl
layout: resource_detail
license:
  id: http://www.apache.org/licenses/LICENSE-2.0
  label: Apache License, Version 2.0
name: Ensembl
products:
- category: GraphicalInterface
  description: A web-based platform for browsing and analyzing vertebrate genomes,
    including gene annotations, comparative genomics, and variation data.
  id: ensembl.browser
  name: Ensembl Genome Browser
  product_url: https://www.ensembl.org
- category: GraphicalInterface
  description: A data mining tool that allows extraction of data without programming
    knowledge or understanding of the underlying database structure.
  id: ensembl.biomart
  name: BioMart
  product_url: https://www.ensembl.org/biomart/martview
- category: ProcessProduct
  description: A tool to analyze variants and predict the functional consequences
    of known and unknown variants.
  id: ensembl.vep
  name: Variant Effect Predictor (VEP)
  product_url: https://www.ensembl.org/info/docs/tools/vep/
- category: ProcessProduct
  description: Tool to search Ensembl genomes for DNA or protein sequences.
  id: ensembl.blast
  name: BLAST/BLAT
  product_url: https://www.ensembl.org/Multi/Tools/Blast
- category: ProgrammingInterface
  description: Programmatic access to all Ensembl data using Perl scripts.
  id: ensembl.api.perl
  name: Ensembl Perl API
  product_url: https://github.com/Ensembl/
  repository: https://github.com/Ensembl/
- category: ProgrammingInterface
  description: RESTful API that allows access to Ensembl data using various programming
    languages.
  id: ensembl.api.rest
  name: Ensembl REST API
  product_url: https://rest.ensembl.org
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2.code
publications:
- authors:
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
  doi: doi:10.1093/nar/gkae1071
  id: https://doi.org/10.1093/nar/gkae1071
  journal: Nucleic Acids Research
  preferred: true
  title: Ensembl 2025
  year: '2025'
repository: https://github.com/Ensembl/
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