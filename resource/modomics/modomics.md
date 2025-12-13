---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: MODOMICS is a comprehensive database of RNA modifications that provides
  detailed information about the chemical structures of modified ribonucleosides,
  their biosynthetic pathways, the location of modified residues in RNA sequences,
  RNA modifying enzymes, and associated human diseases.
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
  description: Web interface for browsing RNA modifications, pathways, reactions,
    sequences, proteins, and associated diseases.
  format: http
  id: modomics.portal
  name: MODOMICS Web Portal
  product_url: https://genesilico.pl/modomics/
- category: ProgrammingInterface
  description: Programmatic interface for accessing MODOMICS data.
  format: http
  id: modomics.api
  name: MODOMICS API
  product_url: https://genesilico.pl/modomics/api/
- category: Product
  description: Three-dimensional structures of modified bases in MOL2 format for computational
    chemistry applications.
  id: modomics.mol2
  name: MODOMICS Modified Base Structures
  product_file_size: 1194876
  product_url: https://genesilico.pl/modomics/download/modification_mol/
- category: Product
  description: Chemical structure images of modified bases for visualization and publication.
  id: modomics.images
  name: MODOMICS Modified Base Images
  product_file_size: 11835390
  product_url: https://genesilico.pl/modomics/download/modification_pics/
- category: Product
  description: Modified positions in PDB structure files.
  id: modomics.pdb
  name: MODOMICS PDB Modified Positions
  product_file_size: 1194876
  product_url: https://genesilico.pl/modomics/download/modification_mol2/
- category: Product
  description: Comprehensive list of modified positions in RNA sequences.
  id: modomics.positions
  name: MODOMICS Modified Positions List
  product_file_size: 146558
  product_url: https://genesilico.pl/modomics/download/modified_positions/
- category: OntologyProduct
  description: Ontology of base modifications in OWL Lite format for semantic web
    applications.
  format: owl
  id: modomics.owl
  name: MODOMICS Ontology (OWL)
  product_url: https://genesilico.pl/modomics/download/ModifiedBases.owl
- category: OntologyProduct
  description: Ontology of base modifications in N3 format.
  id: modomics.n3
  name: MODOMICS Ontology (N3)
  product_url: https://genesilico.pl/modomics/download/Modifications.n3
- category: Product
  description: Structure-data files for modified bases in SDF format.
  format: sdf
  id: modomics.sdf
  name: MODOMICS SDF Files
  product_file_size: 271038
  product_url: https://genesilico.pl/modomics/download/sdf2/
- category: GraphicalInterface
  description: Advanced search interface for querying modifications, pathways, sequences,
    and proteins.
  format: http
  id: modomics.search
  name: MODOMICS Advanced Search
  product_url: https://genesilico.pl/modomics/search/advance/
- category: DocumentationProduct
  description: User guide and documentation for using the MODOMICS database.
  format: http
  id: modomics.help
  name: MODOMICS Help Documentation
  product_url: https://genesilico.pl/modomics/help
- category: DocumentationProduct
  description: Information about data annotation methods and standards used in MODOMICS.
  format: http
  id: modomics.annotation
  name: MODOMICS Data Annotation Information
  product_url: https://genesilico.pl/modomics/data_information/
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
  id: https://doi.org/10.1093/nar/gkad1083
  journal: Nucleic Acids Research
  preferred: true
  title: 'MODOMICS: a database of RNA modifications and related information. 2023
    update'
  year: '2024'
- authors:
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
  id: https://doi.org/10.1093/nar/gkab1083
  journal: Nucleic Acids Research
  preferred: false
  title: 'MODOMICS: a database of RNA modification pathways. 2021 update'
  year: '2022'
taxon:
- NCBITaxon:9606
---
# MODOMICS

MODOMICS is a comprehensive database of RNA modifications developed by the Bujnicki Laboratory at the International Institute of Molecular and Cell Biology in Warsaw, Poland. The database provides detailed information about the chemical structures of modified ribonucleosides, their biosynthetic pathways, the location of modified residues in RNA sequences, and RNA modifying enzymes. MODOMICS covers modified residues, pathways, reactions, RNA sequences, alignments, proteins, human diseases associated with RNA modification defects, guide RNAs, and building blocks. The database offers multiple data formats including MOL2 structures, PDB files, ontologies in OWL and N3 formats, and SDF files. Users can access data through a web interface, API, and bulk downloads. For more information, visit the [MODOMICS portal](https://genesilico.pl/modomics/).