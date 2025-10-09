---
activity_status: active
category: DataSource
creation_date: '2025-08-13T00:00:00Z'
description: 'Xenbase is the Xenopus model organism knowledgebase, a web-accessible resource that integrates all the diverse biological, genomic, genotype and phenotype data available from Xenopus research. It provides comprehensive data on Xenopus laevis and Xenopus tropicalis, including genome assemblies, gene expression data, anatomy information, phenotypes, and developmental biology resources.'
domains:
  - anatomy and development
  - biomedical
  - genomics
  - organisms
  - phenotype
id: xenbase
homepage_url: https://xenbase.org/xenbase/
last_modified_date: '2025-10-09T00:00:00Z'
layout: resource_detail
name: Xenbase
publications:
  - id: https://doi.org/10.1093/genetics/iyad018
    title: 'Xenbase: key features and resources of the Xenopus model organism knowledgebase'
    preferred: true
repository: https://github.com/xenopus-anatomy
products:
  - category: GraphicalInterface
    description: 'Web-based interface for exploring Xenopus biological data including genome browsers, gene expression searches, anatomy atlases, and phenotype databases'
    format: http
    id: xenbase.web-portal
    name: Xenbase Web Portal
    product_url: https://xenbase.org/xenbase/
  - category: Product
    description: 'FTP site providing access to Xenopus genome assemblies, gene models, sequences, BLAST databases, and curated data reports'
    format: mixed
    id: xenbase.ftp-downloads
    name: Xenbase Data Downloads
    product_url: https://xenbase.org/xenbase/static-xenbase/ftpDatafiles.jsp
  - category: Product
    description: 'Complete genome assemblies and gene models for Xenopus laevis (v10.1) and Xenopus tropicalis (v10.0)'
    format: fasta
    id: xenbase.genomes
    name: Xenopus Genome Assemblies
    product_url: https://download.xenbase.org/xenbase
  - category: GraphicalInterface
    description: 'Genome browser for Xenopus laevis v10.1 with integrated genomic and expression data'
    format: http
    id: xenbase.jbrowse-laevis
    name: X. laevis JBrowse Genome Browser
    product_url: https://xenbase.org/xenbase/displayJBrowse.do?data=data/xl10_1
  - category: GraphicalInterface
    description: 'Genome browser for Xenopus tropicalis v10.0 with integrated genomic and expression data'
    format: http
    id: xenbase.jbrowse-tropicalis
    name: X. tropicalis JBrowse Genome Browser
    product_url: https://xenbase.org/xenbase/displayJBrowse.do?data=data/xt10_0
  - category: Product
    description: 'BLAST search interface for Xenopus nucleotide and protein sequences'
    format: http
    id: xenbase.blast
    name: Xenbase BLAST Services
    product_url: https://xenbase.org/xenbase/genomes/blast.do?database=Nucleotide/Xenla_10_1_Scaffolds
  - category: Product
    description: 'Curated gene expression data including RNA-seq, in situ hybridization, and microarray data from GEO datasets'
    format: http
    id: xenbase.expression-data
    name: Gene Expression Data
    product_url: https://xenbase.org/xenbase/geneExpression/geneExpressionSearch.do?method=display
  - category: Product
    description: 'Comprehensive phenotype and mutant data including disease models and morphant phenotypes'
    format: http
    id: xenbase.phenotype-data
    name: Phenotype and Mutant Data
    product_url: https://xenbase.org/xenbase/searchPhenotype.do?method=display
  - category: DocumentationProduct
    description: 'Community wiki with protocols, methods, and resources for Xenopus research'
    format: http
    id: xenbase.wiki
    name: Xenbase Community Wiki
    product_url: https://wiki.xenbase.org/xenwiki/index.php?title=Xenopus_Wiki_-_Home
  - category: ProgrammingInterface
    description: 'REST APIs and web services for programmatic access to Xenbase data'
    format: http
    id: xenbase.apis
    name: Xenbase APIs and Web Services
    product_url: https://xenbase.org/xenbase/static/apis-links.jsp
---

# Xenbase

Xenbase is the Xenopus model organism knowledgebase, serving as the primary repository for research data on the African clawed frog (Xenopus laevis) and Western clawed frog (Xenopus tropicalis). These amphibian species are widely used as model organisms in developmental biology, cell biology, and biomedical research.

## Key Features

- **Genome Resources**: Complete genome assemblies and gene models for X. laevis v10.1 and X. tropicalis v10.0
- **Gene Expression Data**: Comprehensive collection of RNA-seq, in situ hybridization, and microarray expression data
- **Anatomy & Development**: Detailed anatomical atlases, developmental staging information, and fate maps
- **Phenotype & Disease Models**: Curated phenotype data, mutant lines, and disease model information
- **Community Resources**: Protocols, reagents, stock centers, and research tools

## Data Types

Xenbase provides access to:
- **Genomic Data**: Genome assemblies, gene annotations, sequences, and BLAST databases
- **Expression Data**: Temporal and spatial gene expression patterns across development
- **Phenotype Data**: Morphological and functional phenotypes from experimental studies
- **Anatomical Data**: Standardized anatomy with developmental staging
- **Literature**: Curated bibliographic data and community contributions
- **Protocols & Reagents**: Research methodologies and available biological materials

## Supported Species

- **Primary**: Xenopus laevis (African clawed frog), Xenopus tropicalis (Western clawed frog)  
- **Additional**: Ambystoma mexicanum, Nanorana parkeri, Lithobates catesbeiana, Hymenochirus boettgeri

## Ontologies

Xenbase maintains several controlled vocabularies:
- **XAO**: Xenopus Anatomy Ontology for anatomical structures and development
- **XPO**: Xenopus Phenotype Ontology for standardized phenotype descriptions
- **XSMO**: Xenopus Small Molecules Ontology
- **XBED**: Xenbase Experimental Data Ontology

## Citation

If you use Xenbase in your research, please cite:

Karimi, K., et al. Xenbase: key features and resources of the Xenopus model organism knowledgebase. Genetics. 2023;224(1):iyad018. https://doi.org/10.1093/genetics/iyad018

## Funding

Major funding for Xenbase is provided by grant P41 HD064556: "Xenbase: The Xenopus Model Organism Knowledgebase" from the Eunice Kennedy Shriver National Institute of Child Health and Human Development (NICHD/NIH).

## Alliance Membership

Xenbase is a founding member of the Alliance of Genome Resources, collaborating with other model organism databases to provide integrated access to genomic and biological data.
