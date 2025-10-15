---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: MODOMICS is a comprehensive database of RNA modifications that provides detailed information about the chemical structures of modified ribonucleosides, their biosynthetic pathways, the location of modified residues in RNA sequences, RNA modifying enzymes, and associated human diseases.
domains:
  - genomics
  - biological systems
  - chemistry and biochemistry
id: modomics
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: MODOMICS
products:
  - category: GraphicalInterface
    name: MODOMICS Web Portal
    id: modomics.portal
    description: Web interface for browsing RNA modifications, pathways, reactions, sequences, proteins, and associated diseases.
    format: http
    product_url: https://genesilico.pl/modomics/
  - category: ProgrammingInterface
    name: MODOMICS API
    id: modomics.api
    description: Programmatic interface for accessing MODOMICS data.
    format: http
    product_url: https://genesilico.pl/modomics/api/
  - category: Product
    name: MODOMICS Modified Base Structures
    id: modomics.mol2
    description: Three-dimensional structures of modified bases in MOL2 format for computational chemistry applications.
    product_url: https://genesilico.pl/modomics/download/modification_mol/
  - category: Product
    name: MODOMICS Modified Base Images
    id: modomics.images
    description: Chemical structure images of modified bases for visualization and publication.
    product_url: https://genesilico.pl/modomics/download/modification_pics/
  - category: Product
    name: MODOMICS PDB Modified Positions
    id: modomics.pdb
    description: Modified positions in PDB structure files.
    product_url: https://genesilico.pl/modomics/download/modification_mol2/
  - category: Product
    name: MODOMICS Modified Positions List
    id: modomics.positions
    description: Comprehensive list of modified positions in RNA sequences.
    product_url: https://genesilico.pl/modomics/download/modified_positions/
  - category: OntologyProduct
    name: MODOMICS Ontology (OWL)
    id: modomics.owl
    description: Ontology of base modifications in OWL Lite format for semantic web applications.
    format: owl
    product_url: https://genesilico.pl/modomics/download/ModifiedBases.owl
  - category: OntologyProduct
    name: MODOMICS Ontology (N3)
    id: modomics.n3
    description: Ontology of base modifications in N3 format.
    product_url: https://genesilico.pl/modomics/download/Modifications.n3
  - category: Product
    name: MODOMICS SDF Files
    id: modomics.sdf
    description: Structure-data files for modified bases in SDF format.
    format: sdf
    product_url: https://genesilico.pl/modomics/download/sdf2/
  - category: GraphicalInterface
    name: MODOMICS Advanced Search
    id: modomics.search
    description: Advanced search interface for querying modifications, pathways, sequences, and proteins.
    format: http
    product_url: https://genesilico.pl/modomics/search/advance/
  - category: DocumentationProduct
    name: MODOMICS Help Documentation
    id: modomics.help
    description: User guide and documentation for using the MODOMICS database.
    format: http
    product_url: https://genesilico.pl/modomics/help
  - category: DocumentationProduct
    name: MODOMICS Data Annotation Information
    id: modomics.annotation
    description: Information about data annotation methods and standards used in MODOMICS.
    format: http
    product_url: https://genesilico.pl/modomics/data_information/
publications:
  - id: "https://doi.org/10.1093/nar/gkad1083"
    preferred: true
    title: "MODOMICS: a database of RNA modifications and related information. 2023 update"
    authors:
      - Cappannini A
      - Ray A
      - Purta E
      - Mukherjee S
      - Boccaletto P
      - Moafinejad SN
      - Lechner A
      - Barchet C
      - Klaholz BP
      - Stefaniak F
      - Bujnicki JM
    year: "2024"
    journal: "Nucleic Acids Research"
  - id: "https://doi.org/10.1093/nar/gkab1083"
    preferred: false
    title: "MODOMICS: a database of RNA modification pathways. 2021 update"
    authors:
      - Boccaletto P
      - Stefaniak F
      - Ray A
      - Cappannini A
      - Mukherjee S
      - Purta E
      - Kurkowska M
      - Shirvanizadeh N
      - Destefanis E
      - Groza P
    year: "2022"
    journal: "Nucleic Acids Research"
---

# MODOMICS

MODOMICS is a comprehensive database of RNA modifications developed by the Bujnicki Laboratory at the International Institute of Molecular and Cell Biology in Warsaw, Poland. The database provides detailed information about the chemical structures of modified ribonucleosides, their biosynthetic pathways, the location of modified residues in RNA sequences, and RNA modifying enzymes. MODOMICS covers modified residues, pathways, reactions, RNA sequences, alignments, proteins, human diseases associated with RNA modification defects, guide RNAs, and building blocks. The database offers multiple data formats including MOL2 structures, PDB files, ontologies in OWL and N3 formats, and SDF files. Users can access data through a web interface, API, and bulk downloads. For more information, visit the [MODOMICS portal](https://genesilico.pl/modomics/).
