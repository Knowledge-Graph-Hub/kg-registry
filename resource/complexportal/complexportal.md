---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: intact-help@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/support/complexportal
  label: EMBL-EBI
creation_date: '2025-07-17T00:00:00Z'
description: The Complex Portal is an encyclopaedic resource of macromolecular complexes
  from model organisms, providing manually curated and high-confidence machine-learning
  predicted protein complexes with comprehensive structural and functional annotation.
domains:
- proteomics
- systems biology
funding:
- EMBL-EBI
homepage_url: https://www.ebi.ac.uk/complexportal/home
id: complexportal
last_modified_date: '2025-10-09T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Complex Portal
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing macromolecular
    complexes with detailed annotations and structural information
  format: http
  id: complexportal.portal
  name: Complex Portal Web Interface
  product_url: https://www.ebi.ac.uk/complexportal/home
- category: Product
  description: Complete Complex Portal dataset in PSI-MI XML 2.5 format, organized
    by species
  format: psi_mi_xml
  id: complexportal.psi25
  name: Complex Portal PSI-MI XML 2.5
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/psi25/
- category: Product
  description: Complete Complex Portal dataset in PSI-MI XML 3.0 format, organized
    by species
  format: psi_mi_xml
  id: complexportal.psi30
  name: Complex Portal PSI-MI XML 3.0
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/psi30/
- category: Product
  description: Complex Portal data in ComplexTAB flat-file format for easy parsing
    and Excel compatibility, organized by species
  format: tsv
  id: complexportal.complextab
  name: Complex Portal ComplexTAB
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/complextab/
- category: Product
  description: Human complexes dataset from Complex Portal in PSI-MI XML 2.5 format
  format: psi_mi_xml
  id: complexportal.human.psi25
  name: Complex Portal Human PSI-MI XML 2.5
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/psi25/homo_sapiens.xml
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-04: HTTP 404 error
    when accessing file'
- category: Product
  description: Human complexes dataset from Complex Portal in PSI-MI XML 3.0 format
  format: psi_mi_xml
  id: complexportal.human.psi30
  name: Complex Portal Human PSI-MI XML 3.0
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/psi30/homo_sapiens.xml
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-04: HTTP 404 error
    when accessing file'
- category: Product
  description: Human complexes dataset from Complex Portal in ComplexTAB format
  format: tsv
  id: complexportal.human.complextab
  name: Complex Portal Human ComplexTAB
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/complextab/homo_sapiens.tsv
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-04: HTTP 404 error
    when accessing file'
- category: Product
  description: Mouse complexes dataset from Complex Portal in PSI-MI XML 2.5 format
  format: psi_mi_xml
  id: complexportal.mouse.psi25
  name: Complex Portal Mouse PSI-MI XML 2.5
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/psi25/mus_musculus.xml
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-04: HTTP 404 error
    when accessing file'
- category: Product
  description: Mouse complexes dataset from Complex Portal in ComplexTAB format
  format: tsv
  id: complexportal.mouse.complextab
  name: Complex Portal Mouse ComplexTAB
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/complextab/mus_musculus.tsv
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-04: HTTP 404 error
    when accessing file'
- category: Product
  description: Yeast complexes dataset from Complex Portal in PSI-MI XML 2.5 format
  format: psi_mi_xml
  id: complexportal.yeast.psi25
  name: Complex Portal Yeast PSI-MI XML 2.5
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/psi25/saccharomyces_cerevisiae.xml
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-04: HTTP 404 error
    when accessing file'
- category: Product
  description: Yeast complexes dataset from Complex Portal in ComplexTAB format
  format: tsv
  id: complexportal.yeast.complextab
  name: Complex Portal Yeast ComplexTAB
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/complex/current/complextab/saccharomyces_cerevisiae.tsv
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-04: HTTP 404 error
    when accessing file'
- category: ProgrammingInterface
  description: RESTful web service API for programmatic access to Complex Portal data
  format: http
  id: complexportal.webservice
  name: Complex Portal Web Service
  product_url: https://www.ebi.ac.uk/complexportal/webservice
- category: DocumentationProduct
  description: Comprehensive documentation covering data formats, API usage, and complex
    annotation guidelines
  format: http
  id: complexportal.documentation
  name: Complex Portal Documentation
  product_url: https://www.ebi.ac.uk/complexportal/documentation
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - ctd
  - doid
  - go
  - chebi
  - reactome
  - interpro
  - hp
  - cl
  - pr
  - uberon
  - ncbitaxon
  - hetionet
  - complexportal
  - rnacentral
  - mirtarbase
  - unii
  - biolink
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  secondary_source:
  - mechreponet
publications:
- authors:
  - Birgit H M Meldal
  - Hema Bye-A-Jee
  - Lukáš Gajdoš
  - Zuzana Hammerová
  - Aneta Horáčková
  - Filip Melicher
  - Livia Perfetto
  - Daniel Pokorný
  - Milagros Rodriguez Lopez
  - Alžběta Türková
  - Edith D Wong
  - Zengyan Xie
  - Elisabeth Barrera Casanova
  - Noemi del-Toro
  - Maximilian Koch
  - Pablo Porras
  - Henning Hermjakob
  - Sandra Orchard
  doi: 10.1093/nar/gky1001
  id: doi:10.1093/nar/gky1001
  journal: Nucleic Acids Research
  preferred: true
  title: 'Complex Portal 2018: extended content and enhanced visualization tools for
    macromolecular complexes'
  year: '2019'
- authors:
  - Birgit H M Meldal
  - Sandra Orchard
  doi: 10.1093/nar/gku975
  id: doi:10.1093/nar/gku975
  journal: Nucleic Acids Research
  title: The complex portal–an encyclopaedia of macromolecular complexes
  year: '2015'
repository: https://github.com/EBI-IntAct/intact-data-exchange
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:4932
- NCBITaxon:7227
- NCBITaxon:6239
- NCBITaxon:83333
- NCBITaxon:559292
---
# Complex Portal

## Overview

The Complex Portal is a comprehensive, manually curated resource of macromolecular complexes from key model organisms. It serves as an authoritative aggregator that combines expert manual curation with high-confidence machine-learning predictions to provide detailed annotations for protein complexes that have been experimentally characterized.

## Data Content

The Complex Portal defines complexes as assemblies of two or more proteins and/or nucleic acids that are stable enough to be reconstituted in vitro and have demonstrated specific molecular functions. The resource covers multiple organisms:

- **Human** (*Homo sapiens*) - Most comprehensive coverage
- **Mouse** (*Mus musculus*) - Key model organism
- **Yeast** (*Saccharomyces cerevisiae*) - Well-studied unicellular model
- **Fruit fly** (*Drosophila melanogaster*) - Developmental biology model
- **Worm** (*Caenorhabditis elegans*) - Simple multicellular model
- **E. coli** (*Escherichia coli*) - Bacterial model

### Complex Annotation Features

Each complex entry provides:

- **Protein composition** with UniProt identifiers and stoichiometry
- **Functional annotation** using Gene Ontology terms
- **Cellular localization** and tissue distribution
- **Structural information** and cross-references to PDB
- **Disease associations** and clinical relevance
- **Experimental evidence** with literature references
- **Complex assembly pathways** and regulatory mechanisms

### High-Confidence Predictions

In addition to manually curated complexes, the portal includes:

- **hu.MAP 3.0 predictions** - Machine learning-derived human protein complexes
- **MuSIC predictions** - Multi-species interaction complexes
- Quality scores and confidence metrics for computational predictions

## Data Formats and Access

### File Formats

1. **PSI-MI XML 2.5/3.0** - Proteomics Standards Initiative format with comprehensive metadata
2. **ComplexTAB** - Flat-file format designed for easy parsing and Excel compatibility
3. **Web Service API** - RESTful interface for programmatic access

### Data Organization

Data is systematically organized by:
- **Species-specific files** for targeted organism studies
- **Complete datasets** for comprehensive analyses
- **Monthly releases** with version control and change logs
- **FTP access** for bulk downloads and automated processing

## Applications

### Research Applications

- **Systems biology** modeling of cellular networks
- **Drug discovery** targeting specific protein complexes
- **Structural biology** studies of macromolecular assemblies
- **Proteomics** analysis of complex compositions
- **Disease research** investigating complex dysfunction

### Integration Partners

The Complex Portal integrates with and contributes to:

- **IntAct** molecular interaction database
- **UniProt** protein sequence and annotation
- **PDBe** structural biology database
- **Gene Ontology** functional annotation
- **Reactome** pathway database

## Quality Assurance

### Curation Standards

- Manual curation from peer-reviewed literature
- Expert biocurator review and validation
- Cross-referencing with multiple evidence sources
- Regular updates incorporating new experimental data
- Community feedback and correction mechanisms

### Data Reliability

- Experimental evidence requirements for all entries
- Confidence scoring for computational predictions
- Version tracking and change documentation
- Quality metrics and validation procedures

## Citations and Usage

The Complex Portal is freely available under CC BY 4.0 license. Users should cite both the database and specific datasets used. The resource serves as a Global Core Biodata Resource and is part of the ELIXIR infrastructure for biological data management.