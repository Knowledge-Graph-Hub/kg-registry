---
activity_status: active
category: Aggregator
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/support/intact
  id: ebi
  label: IntAct Team (EMBL-EBI)
description: IntAct is an open, curated molecular interaction database maintained
  at EMBL‑EBI. It aggregates experimentally-derived interaction evidence from literature
  curation and direct submissions, and distributes data in PSI‑MI XML and MITAB formats
  along with curated datasets and documentation.
domains:
- proteomics
- systems biology
homepage_url: https://www.ebi.ac.uk/intact/home
id: intact
infores_id: intact
last_modified_date: '2025-09-09T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: IntAct
products:
- category: GraphicalInterface
  description: Web portal for browsing, searching, and accessing IntAct molecular
    interaction data
  format: http
  id: intact.portal
  name: IntAct Portal
  original_source:
  - intact
  product_url: https://www.ebi.ac.uk/intact/home
- category: Product
  description: IntAct data in PSI-MI XML 2.5 format (directory)
  format: psi_mi_xml
  id: intact.ftp.psi25
  name: IntAct PSI-MI XML 2.5
  original_source:
  - intact
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psi25/
- category: Product
  description: IntAct data in PSI-MI XML 3.0 format (directory)
  format: psi_mi_xml
  id: intact.ftp.psi30
  name: IntAct PSI-MI XML 3.0
  original_source:
  - intact
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psi30/
- category: Product
  description: IntAct data in PSI-MI MITAB format (directory)
  format: psi_mi_mitab
  id: intact.ftp.psimitab
  name: IntAct PSI-MI MITAB 2.7
  original_source:
  - intact
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/
- category: Product
  description: Entire MITAB export of the database as a single archive (intact.zip)
  format: psi_mi_mitab
  id: intact.ftp.psimitab.all
  name: IntAct MITAB Archive
  original_source:
  - intact
  product_file_size: 846305671
  product_url: https://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/intact.zip
- category: Product
  description: Curated and computational datasets (disease-, method-, and species-specific)
    with per-dataset downloads
  format: http
  id: intact.datasets
  name: IntAct Datasets
  original_source:
  - intact
  product_url: https://www.ebi.ac.uk/intact/download/datasets
- category: DocumentationProduct
  description: User guide and documentation for search, exports, data sources, and
    submission
  format: http
  id: intact.docs.user-guide
  name: IntAct User Guide
  original_source:
  - intact
  product_url: https://www.ebi.ac.uk/intact/documentation/user-guide
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
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
  - pharmacodb
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
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - epigraphdb
  - kg-monarch
  - vectology
  - ukbiobank
  - prsatlas
  - eqtlgen
  - mondo
  - gtex
  - ensembl
  - cpic
  - opentargets
  - efo
  - semmeddb
  - intact
  - string
  - reactome
  - mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
  secondary_source:
  - epigraphdb
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
- category: GraphProduct
  description: IntAct Automat
  format: kgx-jsonl
  id: automat.intact
  infores_id: automat-intact
  name: intact_automat
  original_source:
  - intact
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/IntAct_Automat/e5b936f966a02c2c/
  secondary_source:
  - automat
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: Product
  description: Protein interaction data aggregated from IntAct, STRING, BioGRID and
    other interaction databases
  format: http
  id: genecards.protein.interactions
  name: GeneCards Protein Interactions
  original_source:
  - intact
  - string
  - biogrid
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-18_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-20: HTTP 403 error
    when accessing file'
- category: Product
  description: Historical consolidated protein interaction index in PSI-MITAB 2.5
    format aggregating data from BIND, BioGrid, DIP, HPRD, IntAct, MINT, MPact, MPPI
    and OPHID
  format: psi_mi_mitab
  id: irefindex.database
  name: iRefIndex Database
  original_source:
  - bind
  - biogrid
  - dip
  - hprd
  - intact
  - mint
- category: GraphProduct
  description: KGX graph package for IntAct molecular interactions (build intact_2025_08_28_1.0_2025sep1_4.3.6;
    release 2025_12_15)
  format: kgx
  id: translator.intact.graph
  name: Translator IntAct KGX Graph
  original_source:
  - intact
  product_url: https://stars.renci.org/var/translator/releases/intact/2025_12_15/
  secondary_source:
  - translator
- category: GraphProduct
  description: Core UniBioMap graph edges file.
  format: csv
  id: unibiomap.links
  name: UniBioMap Graph Links
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 1406201678
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
- category: GraphProduct
  description: Auxiliary UniBioMap graph annotations and metadata.
  format: tsv
  id: unibiomap.auxs
  name: UniBioMap Graph Auxiliaries
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 591290539
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
- category: GraphProduct
  description: Predicted UniBioMap graph edges with confidence scores.
  format: csv
  id: unibiomap.pred
  name: UniBioMap Predicted Graph
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 2484982268
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
- category: GraphProduct
  description: Full unfiltered UniBioMap predicted graph edges file.
  format: csv
  id: unibiomap.pred.full
  name: UniBioMap Predicted Graph (Full)
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, scored links between proteins)
  format: txt
  id: string.protein.links
  name: STRING Protein Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 138154280240
  product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, incl. subscores per channel)
  format: txt
  id: string.protein.links.detailed
  name: STRING Protein Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 203534412387
  product_url: https://stringdb-downloads.org/download/protein.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (full network, incl. distinction: direct vs.
    interologs)'
  format: txt
  id: string.protein.links.full
  name: STRING Protein Links Full
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 214269334954
  product_url: https://stringdb-downloads.org/download/protein.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, scored links between proteins)
  format: txt
  id: string.protein.physical.links
  name: STRING Protein Physical Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 11867396121
  product_url: https://stringdb-downloads.org/download/protein.physical.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, incl. subscores per channel)
  format: txt
  id: string.protein.physical.links.detailed
  name: STRING Protein Physical Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 14859366689
  product_url: https://stringdb-downloads.org/download/protein.physical.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (physical subnetwork, incl. distinction: direct
    vs. interologs)'
  format: txt
  id: string.protein.physical.links.full
  name: STRING Protein Physical Links Full
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 15528028374
  product_url: https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores between orthologous groups
  format: txt
  id: string.cog.links
  name: STRING COG Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 185338269
  product_url: https://stringdb-downloads.org/download/COG.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores (incl. subscores per channel)
  format: txt
  id: string.cog.links.detailed
  name: STRING COG Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 250279091
  product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'full database, part II: the networks (nodes, edges, scores,...)'
  id: string.database
  name: STRING Database Network Schema
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 281505096430
  product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
- category: GraphProduct
  description: ProteomeHD data files
  id: proteomehd.data
  name: ProteomeHD Data
  original_source:
  - proteomehd
  - uniprot
  - reactome
  - intact
  - go
  - goa
  product_url: https://github.com/Rappsilber-Laboratory/ProteomeHD/tree/master/Data
---
# IntAct

## Overview

IntAct is a curated molecular interaction database, aggregating experimental evidence from the literature and direct submissions and distributing data in PSI‑MI XML and MITAB formats. It is part of the IMEx consortium and a Global Core Biodata Resource.

## Access

- Portal: browse and search interactions via the IntAct web interface
- FTP: bulk downloads in PSI‑MI XML (2.5, 3.0) and MITAB (2.7)
- Datasets: curated and computational datasets with themed collections
- Documentation: user guide covering data sources, formats, export, and submission

## Citation

Please cite IntAct and any specific datasets used, and refer to the Apache 2.0 license terms for data reuse.