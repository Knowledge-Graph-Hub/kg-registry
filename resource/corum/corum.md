---
activity_status: active
category: DataSource
description: CORUM (Comprehensive Resource of Mammalian Protein Complexes) is a curated database of experimentally characterized protein complexes from mammalian organisms, particularly human, mouse, and rat, with a focus on manually annotated information from scientific literature.
domains:
- proteomics
- biomedical
- chemistry and biochemistry
homepage_url: https://mips.helmholtz-muenchen.de/corum/
repository: https://mips.helmholtz-muenchen.de/corum/download
id: corum
layout: resource_detail
name: CORUM
creation_date: '2025-07-22T00:00:00Z'
last_modified_date: '2025-07-22T00:00:00Z'
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: CC BY-NC 4.0
contacts:
- category: Organization
  label: Helmholtz Zentrum München
  contact_details:
  - contact_type: url
    value: https://www.helmholtz-munich.de/
  - contact_type: email
    value: corum@helmholtz-muenchen.de
publications:
- id: doi:10.1093/nar/gkac1015
  title: "CORUM: the comprehensive resource of mammalian protein complexes—2023"
  authors:
  - Stefanie Gößler
  - Gisela Fobo
  - Barbara Wankerl
  - Christopher J. Mann
  - Hans-Werner Mewes
  - Andreas Ruepp
  doi: 10.1093/nar/gkac1015
  journal: Nucleic Acids Research
  year: "2023"
  preferred: true
- id: doi:10.1093/nar/gky973
  title: "CORUM: the comprehensive resource of mammalian protein complexes—2019"
  authors:
  - Andreas Giurgiu
  - Julian Reinhard
  - Barbara Brauner
  - Irmtraud Dunger-Kaltenbach
  - Gisela Fobo
  - Goar Frishman
  - Corinna Montrone
  - Andreas Ruepp
  doi: 10.1093/nar/gky973
  journal: Nucleic Acids Research
  year: "2019"
- id: doi:10.1093/nar/gkp914
  title: "CORUM: the comprehensive resource of mammalian protein complexes—2009"
  authors:
  - Andreas Ruepp
  - Barbara Brauner
  - Irmtraud Dunger-Kaltenbach
  - Goar Frishman
  - Corinna Montrone
  - Michael Stransky
  - Brigitte Waegele
  - Thorsten Schmidt
  - Octave Noubibou Doudieu
  - Volker Stümpflen
  - Hans-Werner Mewes
  doi: 10.1093/nar/gkp914
  journal: Nucleic Acids Research
  year: "2010"
products:
- category: Product
  description: Complete dataset of all curated protein complexes in CORUM in tab-delimited format
  id: corum.all_complexes
  name: CORUM All Complexes
  format: tsv
  product_url: https://mips.helmholtz-muenchen.de/corum/download/allComplexes.txt.zip
  license:
    id: https://creativecommons.org/licenses/by-nc/4.0/
    label: CC BY-NC 4.0
- category: Product
  description: Core dataset of manually curated, non-redundant protein complexes in CORUM in tab-delimited format
  id: corum.core_complexes
  name: CORUM Core Complexes
  format: tsv
  product_url: https://mips.helmholtz-muenchen.de/corum/download/coreComplexes.txt.zip
  license:
    id: https://creativecommons.org/licenses/by-nc/4.0/
    label: CC BY-NC 4.0
- category: Product
  description: Dataset of all CORUM protein complexes in PSI-MI XML format (Proteomics Standards Initiative)
  id: corum.psi_mi
  name: CORUM PSI-MI
  format: psi_mi_xml
  product_url: https://mips.helmholtz-muenchen.de/corum/download/psi.zip
  license:
    id: https://creativecommons.org/licenses/by-nc/4.0/
    label: CC BY-NC 4.0
- category: Product
  description: Dataset of all CORUM protein complexes in PSI-MI MITAB 2.5 format
  id: corum.mitab
  name: CORUM MITAB
  format: psi_mi_mitab
  product_url: https://mips.helmholtz-muenchen.de/corum/download/mitab.zip
  license:
    id: https://creativecommons.org/licenses/by-nc/4.0/
    label: CC BY-NC 4.0
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmdb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
---
# CORUM - Comprehensive Resource of Mammalian Protein Complexes

CORUM is a manually curated database of experimentally characterized protein complexes from mammalian organisms. It serves as a comprehensive and high-quality resource for researchers studying protein-protein interactions, cellular functions, and disease mechanisms.

## Overview

The CORUM database focuses on protein complexes from human, mouse, and rat, with a particular emphasis on human complexes. The database is distinguished by its commitment to manual curation from scientific literature, ensuring high data quality. Every entry in CORUM is based on experimental evidence from published research papers, providing reliable information about the composition and function of protein complexes.

As of the 2023 update, CORUM contains:
- Over 4,700 protein complexes
- More than 3,300 different genes
- Approximately 20,000 protein-protein interactions

## Key Features

CORUM provides comprehensive information about each protein complex, including:

- Complex name and synonyms
- Organism source
- Protein composition (with UniProt IDs)
- Associated diseases
- Biological functions (GO terms)
- Cellular localization
- PubMed references to experimental evidence
- Tissue distribution
- Protein complex purification methods

## Data Sources and Curation

All entries in CORUM are manually extracted from scientific literature by expert curators. This manual curation approach ensures high-quality data and allows for the inclusion of detailed information that may not be captured by automated text mining approaches. The curation process focuses on:

1. Identifying experimentally verified protein complexes from peer-reviewed publications
2. Mapping protein components to standardized identifiers (UniProt)
3. Annotating complexes with functional information and disease associations
4. Cross-referencing with other databases and ontologies

## Applications

CORUM serves as a valuable resource for various research applications:

- **Proteomics**: Interpretation of mass spectrometry data and analysis of protein-protein interactions
- **Systems Biology**: Study of cellular pathways and network analysis
- **Disease Research**: Investigation of disease mechanisms and identification of therapeutic targets
- **Computational Biology**: Training and validation of protein interaction prediction algorithms
- **Functional Genomics**: Functional annotation of genes and proteins

## Data Access

CORUM data is freely available for academic and non-commercial use under a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license. The database can be accessed through:

- Web interface at [https://mips.helmholtz-muenchen.de/corum/](https://mips.helmholtz-muenchen.de/corum/)
- Bulk downloads in various formats (PSI-MI XML, MITAB, plain text)
- Programmatic access via web services