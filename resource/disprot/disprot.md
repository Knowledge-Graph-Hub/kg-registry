---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: info@disprot.org
    label: DisProt Team
  - category: Individual
    contact_details:
      - contact_type: email
        value: biocomp@bio.unipd.it
    label: Damiano Piovesan
creation_date: '2025-10-30T00:00:00Z'
description: DisProt is a manually curated database of experimentally validated intrinsically disordered proteins (IDPs) and intrinsically disordered regions (IDRs), providing annotations for structural disorder and functional aspects of protein disorder.
domains:
  - proteomics
  - biological systems
homepage_url: https://www.disprot.org
id: disprot
infores_id: disprot
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: Creative Commons Attribution 4.0 International (CC BY 4.0)
name: DisProt
products:
  - category: GraphicalInterface
    description: Web interface for browsing and searching intrinsically disordered protein annotations with search filters and organism browsing
    format: http
    id: disprot.browser
    name: DisProt Browser
    original_source:
      - source: disprot
        relation_type: prov:hadPrimarySource
    product_url: https://www.disprot.org/browse
  - category: Product
    description: Bulk download of DisProt data in multiple formats including JSON, TSV, FASTA, and GAF
    format: json
    id: disprot.downloads
    name: DisProt Downloads
    original_source:
      - source: disprot
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: uniprot
        relation_type: prov:wasInformedBy
      - source: interpro
        relation_type: prov:wasInformedBy
      - source: go
        relation_type: prov:wasInformedBy
      - source: eco
        relation_type: prov:wasInformedBy
    product_url: https://www.disprot.org/download
  - category: ProgrammingInterface
    connection_url: https://www.disprot.org/api/search
    description: RESTful API for programmatic access to DisProt data
    format: json
    id: disprot.api
    is_public: true
    name: DisProt API
    original_source:
      - source: disprot
        relation_type: prov:hadPrimarySource
    product_url: https://www.disprot.org/api
  - category: GraphicalInterface
    description: Deposition system for submitting experimental data on intrinsically disordered proteins
    format: http
    id: disprot.deposition
    name: DisProt Deposition System
    original_source:
      - source: disprot
        relation_type: prov:hadPrimarySource
    product_url: https://deposition.disprot.org/
  - category: OntologyProduct
    description: IDP Ontology (IDPO) for representing functional aspects of intrinsically disordered proteins
    format: owl
    id: disprot.idpo
    name: IDP Ontology (IDPO)
    original_source:
      - source: disprot
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: go
        relation_type: prov:wasInformedBy
      - source: eco
        relation_type: prov:wasInformedBy
    product_file_size: 50945
    product_url: https://www.disprot.org/assets/data/IDPO_v0.3.0.owl
publications:
- authors:
  - Aspromonte MC
  - Nugnes MV
  - Quaglia F
  - Bouharoua A
  - DisProt Consortium
  - Tosatto SCE
  - Piovesan D
  doi: 10.1093/nar/gkad928
  id: PMID:37904585
  journal: Nucleic Acids Res
  preferred: true
  title: 'DisProt in 2024: improving function annotation of intrinsically disordered proteins.'
  year: '2024'
- authors:
  - Quaglia F
  - Mészáros B
  - Salladini E
  - Hatos A
  - Pancsa R
  - Chemes LB
  - Pajkos M
  - Lazar T
  - Peña-Díaz S
  - Santos J
  - Ács V
  - Farahi N
  - Fichó E
  - Aspromonte MC
  - Bassot C
  - Chasapi A
  - Davey NE
  - Davidović R
  - Dobson L
  - Elofsson A
  - Erdős G
  - Gaudet P
  - Giglio M
  - Glavina J
  - Iserte J
  - Iglesias V
  - Kálmán Z
  - Lambrughi M
  - Leonardi E
  - Longhi S
  - Macedo-Ribeiro S
  - Maiani E
  - Marchetti J
  - Marino-Buslje C
  - Mészáros A
  - Monzon AM
  - Minervini G
  - Nadendla S
  - Nilsson JF
  - Novotný M
  - Ouzounis CA
  - Palopoli N
  - Papaleo E
  - Pereira PJB
  - Pozzati G
  - Promponas VJ
  - Pujols J
  - Rocha ACS
  - Salas M
  - Sawicki LR
  - Schad E
  - Shenoy A
  - Szaniszló T
  - Tsirigos KD
  - Veljkovic N
  - Parisi G
  - Ventura S
  - Dosztányi Z
  - Tompa P
  - Tosatto SCE
  - Piovesan D
  doi: 10.1093/nar/gkab1082
  id: PMID:34850135
  journal: Nucleic Acids Res
  title: 'DisProt in 2022: improved quality and accessibility of protein intrinsic disorder annotation.'
  year: '2022'
- authors:
  - Hatos A
  - Hajdu-Soltész B
  - Monzon AM
  - Palopoli N
  - Álvarez L
  - Aykac-Fas B
  - Bassot C
  - Benítez GI
  - Bevilacqua M
  - Chasapi A
  - Chemes L
  - Davey NE
  - Davidović R
  - Dunker AK
  - Elofsson A
  - Gobeill J
  - Foutel NSG
  - Sudha G
  - Guharoy M
  - Horvath T
  - Iglesias V
  - Kajava AV
  - Kovacs OP
  - Lamb J
  - Lambrughi M
  - Lazar T
  - Leclercq JY
  - Leonardi E
  - Macedo-Ribeiro S
  - Macossay-Castillo M
  - Maiani E
  - Manso JA
  - Marino-Buslje C
  - Martínez-Pérez E
  - Mészáros B
  - Mičetić I
  - Minervini G
  - Murvai N
  - Necci M
  - Ouzounis CA
  - Pajkos M
  - Paladin L
  - Pancsa R
  - Papaleo E
  - Parisi G
  - Pasche E
  - Barbosa Pereira PJ
  - Promponas VJ
  - Pujols J
  - Quaglia F
  - Ruch P
  - Salvatore M
  - Schad E
  - Szabo B
  - Szaniszló T
  - Tamana S
  - Tantos A
  - Veljkovic N
  - Ventura S
  - Vranken W
  - Dosztányi Z
  - Tompa P
  - Tosatto SCE
  - Piovesan D
  doi: 10.1093/nar/gkz975
  id: PMID:31713636
  journal: Nucleic Acids Res
  title: 'DisProt: intrinsic protein disorder annotation in 2020.'
  year: '2020'
---

# DisProt

## Overview

DisProt is the major manually curated repository of intrinsically disordered proteins (IDPs), covering both structural and functional aspects. Expert curators collect experimentally confirmed biological data on protein disorder, making it a valuable resource for the scientific community. DisProt is part of the ELIXIR infrastructure and serves the IDP Community.

## Data Content

DisProt provides comprehensive annotations for:

- **Intrinsically Disordered Regions (IDRs)**: Experimentally validated regions of structural disorder in proteins
- **Functional Annotations**: Biological functions associated with disordered regions
- **Experimental Evidence**: Curated experimental data supporting disorder and function annotations
- **Cross-references**: Integration with UniProt, InterPro, Gene Ontology, and Evidence Ontology

Current release statistics are available from the DisProt download and browse pages.

## Key Features

- Manual curation by expert biocurators following standardized guidelines
- Daily updates and maintenance
- Experimentally validated annotations from published scientific literature
- Thematic datasets on specific topics (e.g., age-related disorders)
- Integration with major biological databases
- Training materials and courses for biocuration

## Access Methods

- **Web Browser**: Interactive search and browse interface
- **Bulk Downloads**: Complete database exports in JSON, TSV, FASTA, and GAF formats
- **REST API**: Programmatic data access for computational workflows
- **Deposition System**: Portal for submitting new experimental data

## Use Cases

- Training and validation of disorder prediction methods (CAID - Critical Assessment of Protein Intrinsic Disorder Prediction)
- Studying structure-function relationships in disordered proteins
- Analyzing disease-associated protein disorder
- Developing computational tools for IDP analysis
- Meta-analyses of protein disorder across organisms

## IDP Ontology

DisProt maintains the IDP Ontology (IDPO) v0.3.0, which represents functional aspects of intrinsically disordered proteins. Available in JSON, OWL, and OBO formats with mappings to Gene Ontology and Evidence & Conclusion Ontology terms.

## Management

DisProt is maintained by the BioComputing UP group at the University of Padua, Italy, led by:
- Prof. Silvio C.E. Tosatto (Team Leader)
- Prof. Damiano Piovesan (Team Leader & Software Developer)
- Dr. Maria Cristina Aspromonte (DisProt Manager)

The project operates with an international Scientific Advisory Board and is funded by the European Union's Horizon 2020 programme (grant agreement No. 778247).

## Funding

European Union's Horizon 2020 research and innovation programme under grant agreement No. 778247.
