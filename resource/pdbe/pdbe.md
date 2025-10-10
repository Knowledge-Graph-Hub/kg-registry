---
activity_status: active
category: Aggregator
creation_date: '2025-09-09T00:00:00Z'
description: PDBe-KB (Protein Data Bank in Europe - Knowledge Base) is an open, collaborative
  consortium for integration and enrichment of 3D-structure data and functional annotations
  to enable basic and translational research. It provides comprehensive access to
  macromolecular structure data integrated with functional annotations from multiple
  sources.
domains:
- biomedical
- genomics
- proteomics
- anatomy and development
homepage_url: https://www.ebi.ac.uk/pdbe/pdbe-kb/
id: pdbe
last_modified_date: '2025-10-08T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: PDBe Knowledge Base
products:
- category: GraphicalInterface
  description: PDBe-KB web portal providing access to enriched 3D structure data with
    functional annotations, including protein structures, ligand superpositions, and
    biological context
  format: http
  id: pdbe.kb-portal
  name: PDBe-KB Web Portal
  product_url: https://www.ebi.ac.uk/pdbe/pdbe-kb/
- category: GraphProduct
  description: Neo4j graph database containing integrated PDBe-KB data with PDB entries,
    chains, entities, residues, and functional annotations. This version (graph.db.tgz)
    is for Neo4J 3.5.
  format: neo4j
  id: pdbe.kb-graph-database.neo4j3
  name: PDBe-KB Graph Database for Neo4J 3.5
  product_url: https://ftp.ebi.ac.uk/pub/databases/msd/graphdb/
- category: GraphProduct
  description: Neo4j graph database containing integrated PDBe-KB data with PDB entries,
    chains, entities, residues, and functional annotations. This version (neo4j.dump)
    is for Neo4J 4 and above.
  format: neo4j
  id: pdbe.kb-graph-database.neo4j4
  name: PDBe-KB Graph Database for Neo4J 4
  product_url: https://ftp.ebi.ac.uk/pub/databases/msd/graphdb/
- category: ProgrammingInterface
  description: RESTful API powered by the PDBe-KB graph database, providing programmatic
    access to structural data and functional annotations
  format: http
  id: pdbe.kb-api
  name: PDBe-KB Graph API
  product_url: https://www.ebi.ac.uk/pdbe/graph-api/pdbe_doc/
- category: Product
  description: FTP archive providing bulk download access to PDBe-KB data files and
    annotations
  format: http
  id: pdbe.kb-ftp
  name: PDBe-KB FTP Archive
  product_url: http://ftp.ebi.ac.uk/pub/databases/pdbe-kb/
- category: Product
  description: Downloadable coordinate files, experimental data files, validation
    reports, FASTA sequences, and small molecule data for PDB entries
  format: mixed
  id: pdbe.download-service
  name: PDBe Download Service
  product_url: https://www.ebi.ac.uk/pdbe/download/docs
- category: Product
  description: SIFTS (Structure Integration with Function, Taxonomy and Sequences)
    provides residue-level mapping between UniProt and PDB entries
  format: xml
  id: pdbe.sifts
  name: SIFTS Residue-level Mapping
  product_url: https://www.ebi.ac.uk/pdbe/download/docs
- category: DocumentationProduct
  description: User guides and documentation for PDBe-KB features and data access
  format: http
  id: pdbe.kb-manual
  name: PDBe-KB User Manual
  product_url: https://github.com/PDBe-KB/pdbe-kb-manual
- category: DocumentationProduct
  description: Interactive schema explorer for the PDBe-KB Neo4j graph database, showing
    nodes, relationships, and data structure
  format: http
  id: pdbe.kb-schema
  name: PDBe Graph Database Schema Explorer
  product_url: https://www.ebi.ac.uk/pdbe/pdbe-kb/schema
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
- category: Product
  description: Protein structure data from PDB Europe and other structural databases
  format: http
  id: genecards.protein.structures
  name: GeneCards Protein Structure Data
  original_source:
  - pdbe
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-10_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-10_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-10-10: HTTP 403 error
    when accessing file'
publications:
- id: https://doi.org/10.1093/nar/gkab988
  preferred: true
  title: 'PDBe-KB: collaboratively defining the biological context of structural data'
repository: https://github.com/PDBe-KB
---
# PDBe Knowledge Base

PDBe-KB (Protein Data Bank in Europe - Knowledge Base) is an open, collaborative consortium for integration and enrichment of 3D-structure data and functional annotations to enable basic and translational research.

## Mission

- Implement a comprehensive, FAIR infrastructure for macromolecular structures and their annotations
- Enrich macromolecular structure data with structural and functional annotations to establish their biological context
- Develop innovative tools for data access and visualisation

## Key Features

- **Experimental and Predicted Protein Structures**: Integration of experimental structures from PDB with predicted models
- **Superposition of Protein Chains and Ligands**: Visualization and analysis of structural superpositions
- **Graph Database**: Neo4j-based graph database with over 150 million residues linked to functional annotations
- **Unified Access**: Integration with UniProt through SIFTS residue-level mapping

## Graph Database

The PDBe-KB graph database is implemented in Neo4J and represents each PDB entry as a tree structure:
- Root: PDB entry
- Connected to: chains and entities
- Further connected to: residues (>150 million)
- Each residue is linked to:
  - Available annotations (e.g., catalytic sites, interaction interfaces)
  - Corresponding UniProt residues

This graph structure enables straightforward transfer of annotations between PDB entries mapping to the same UniProt accession and highly identical UniProt accessions.

## Access Methods

- **Web Portal**: Interactive browsing and visualization
- **Graph API**: RESTful API for programmatic access
- **FTP**: Bulk download of data files
- **Direct Database Access**: Query the Neo4j graph database
- **Download Service**: Structured download of specific data types

## Citation

If you use this resource, please cite:

PDBe-KB consortium. PDBe-KB: collaboratively defining the biological context of structural data. Nucleic Acids Research, Database Issue (2022). https://doi.org/10.1093/nar/gkab988

## License

All data is freely available for both academic and commercial use under Creative Commons Attribution 4.0 (CC BY 4.0) license.