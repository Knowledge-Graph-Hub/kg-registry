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
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: crd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: evlncrnas
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: greengenes
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadb
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: mgnify
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pirbase
  - relation_type: prov:hadPrimarySource
    source: plncdb
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: rdp
  - relation_type: prov:hadPrimarySource
    source: rediportal
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: ribocentre
  - relation_type: prov:hadPrimarySource
    source: ribovision
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: snornadatabase
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tmrnawebsite
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: zwd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  product_url: https://rnacentral.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to RNAcentral data
  format: http
  id: rnacentral.api
  name: RNAcentral REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: crd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: evlncrnas
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: greengenes
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadb
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: mgnify
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pirbase
  - relation_type: prov:hadPrimarySource
    source: plncdb
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: rdp
  - relation_type: prov:hadPrimarySource
    source: rediportal
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: ribocentre
  - relation_type: prov:hadPrimarySource
    source: ribovision
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: snornadatabase
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tmrnawebsite
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: zwd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  product_url: https://rnacentral.org/api
- category: Product
  description: FTP archive with current and archived release files (sequences and
    annotations)
  format: http
  id: rnacentral.ftp
  name: RNAcentral FTP Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: crd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: evlncrnas
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: greengenes
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadb
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: mgnify
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pirbase
  - relation_type: prov:hadPrimarySource
    source: plncdb
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: rdp
  - relation_type: prov:hadPrimarySource
    source: rediportal
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: ribocentre
  - relation_type: prov:hadPrimarySource
    source: ribovision
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: snornadatabase
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tmrnawebsite
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: zwd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
- category: DataModelProduct
  description: Public PostgreSQL database for direct SQL access to RNAcentral data
  format: postgres
  id: rnacentral.public-db
  name: RNAcentral Public Postgres Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: crd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: evlncrnas
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: greengenes
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadb
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: mgnify
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pirbase
  - relation_type: prov:hadPrimarySource
    source: plncdb
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: rdp
  - relation_type: prov:hadPrimarySource
    source: rediportal
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: ribocentre
  - relation_type: prov:hadPrimarySource
    source: ribovision
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: snornadatabase
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tmrnawebsite
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: zwd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  product_url: https://rnacentral.org/help/public-database
- category: Product
  description: Protein structure data from PDB Europe and other structural databases
  format: http
  id: genecards.protein.structures
  name: GeneCards Protein Structure Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 403 error
    when accessing file'
- category: Product
  description: GO annotations for PDB entries
  format: txt
  id: goa.pdb
  name: PDB GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-26_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/'
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/intact/ws
  description: IntAct web service and URL-based programmatic interface for retrieving
    molecular interaction networks in PSI-MI formats.
  format: http
  id: intact.api
  is_public: true
  name: IntAct Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://www.ebi.ac.uk/intact/ws
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: intact
- category: Product
  description: IntAct data in PSI-MI XML 2.5 format (directory)
  format: psi_mi_xml
  id: intact.ftp.psi25
  name: IntAct PSI-MI XML 2.5
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psi25/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: intact
- category: Product
  description: IntAct data in PSI-MI XML 3.0 format (directory)
  format: psi_mi_xml
  id: intact.ftp.psi30
  name: IntAct PSI-MI XML 3.0
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psi30/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: intact
- category: Product
  description: IntAct data in PSI-MI MITAB format (directory)
  format: psi_mi_mitab
  id: intact.ftp.psimitab
  name: IntAct PSI-MI MITAB 2.7
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: intact
- category: Product
  description: Entire MITAB export of the database as a single archive (intact.zip)
  format: psi_mi_mitab
  id: intact.ftp.psimitab.all
  name: IntAct MITAB Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_file_size: 846305671
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/intact.zip
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: intact
- category: Product
  description: Curated and computational datasets (disease-, method-, and species-specific)
    with per-dataset downloads
  format: http
  id: intact.datasets
  name: IntAct Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcs
  - relation_type: prov:hadPrimarySource
    source: hpidb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://www.ebi.ac.uk/intact/download/datasets
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: intact
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