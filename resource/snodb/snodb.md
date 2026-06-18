---
activity_status: active
category: DataSource
creation_date: '2025-10-27T00:00:00Z'
description: snoDB is a specialized database of human small nucleolar RNAs (snoRNAs),
  integrating data from established databases with manually curated literature. It
  provides comprehensive information on snoRNA genomic locations, sequences, conservation,
  host genes, snoRNA-RNA interactions, snoRNA-protein interactions, and abundance
  data across tissues and cancer cells.
domains:
- genomics
- biological systems
homepage_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
id: snodb
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
name: snoDB
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and analyzing human snoRNA data
    with interactive tables and visualization tools
  format: http
  id: snodb.portal
  name: snoDB 2.0 Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
- category: GraphicalInterface
  description: Interactive abundance viewer for visualizing snoRNA expression across
    tissues and cell lines
  format: http
  id: snodb.abundance-viewer
  name: Abundance Viewer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
- category: GraphicalInterface
  description: Browser for exploring rRNA chemical modification sites and their guide
    snoRNAs
  format: http
  id: snodb.rrna-modifications
  name: rRNA Chemical Modifications Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/rRNA_modifications/
- category: GraphicalInterface
  description: Statistics dashboard showing snoRNA type distributions, length distributions,
    and target biotypes
  format: http
  id: snodb.statistics
  name: Statistics Dashboard
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/statistics/
- category: GraphicalInterface
  description: Sequence similarity search tool for finding snoRNAs by sequence
  format: http
  id: snodb.sequence-search
  name: Sequence Search Tool
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/sequence_similarity_search/
- category: Product
  description: Database of human snoRNA sequences with GRCh38 genomic coordinates
  format: http
  id: snodb.sequences
  name: snoRNA Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: Conservation data including PhastCons scores for 100 vertebrates from
    UCSC genome browser
  format: http
  id: snodb.conservation
  name: Conservation Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: snoRNA motif sequences and guide regions (boxes C, D, C', D' for C/D
    box snoRNAs; H and ACA boxes for H/ACA snoRNAs)
  format: http
  id: snodb.motifs
  name: Motif and Guide Region Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: Host gene information with functional annotations from Gene Ontology
  format: http
  id: snodb.host-genes
  name: Host Gene Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: Canonical snoRNA-rRNA and snoRNA-snRNA interactions from multiple sources
  format: http
  id: snodb.canonical-interactions
  name: Canonical snoRNA-RNA Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: Non-canonical snoRNA-RNA interactions from RISE database
  format: http
  id: snodb.noncanonical-interactions
  name: Non-canonical snoRNA-RNA Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: snoRNA-protein interactions from ENCODE eCLIP data of 150 RNA binding
    proteins
  format: http
  id: snodb.protein-interactions
  name: snoRNA-Protein Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: snoRNA and host gene abundance data from TGIRT-Seq across tissues and
    cancer cell lines
  format: http
  id: snodb.abundance
  name: Abundance Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: rRNA modification positions with validation status and modification
    levels from multiple studies
  format: http
  id: snodb.rrna-mods
  name: rRNA Modification Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/rRNA_modifications/
  warnings: []
- category: Product
  description: snoRNA copy information based on RFAM classification
  format: http
  id: snodb.copies
  name: snoRNA Copy Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/
  warnings: []
- category: Product
  description: Exportable data tables with advanced search and filtering capabilities
  format: tsv
  id: snodb.export
  name: Data Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_file_size: 753930
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/download_all/
- category: ProcessProduct
  description: Tool for integrating snoDB snoRNAs into Ensembl or RefSeq GTF annotation
    files
  format: http
  id: snodb.snorupdate
  name: snoRupdate
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://github.com/scottgroup/snoRupdate
- category: DocumentationProduct
  description: Comprehensive documentation about data sources, methods, and curation
    processes
  format: http
  id: snodb.about
  name: About and Help Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/about/
  warnings: []
- category: DocumentationProduct
  description: Interactive tutorial for navigating and using snoDB features
  format: http
  id: snodb.tutorial
  name: Tutorial
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/tutorial/
  warnings: []
- category: DocumentationProduct
  description: Detailed information about TGIRT-Seq data processing and experimental
    methods
  format: http
  id: snodb.experiment-details
  name: Experiment Details
  original_source:
  - relation_type: prov:hadPrimarySource
    source: snodb
  product_url: https://bioinfo-scottgroup.med.usherbrooke.ca/snoDB/experiment_details/
  warnings: []
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
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
publications:
- authors:
  - Bergeron
  - Paraqindes
  - Fafard-Couture
  - Deschamps-Francoeur
  - "Faucher-Gigu\xE8re"
  - Bouchard-Bourelle
  - Abou Elela
  - Catez
  - Marcel
  - Scott
  doi: 10.1093/nar/gkac835
  id: https://pubmed.ncbi.nlm.nih.gov/36165892/
  journal: Nucleic Acids Res
  preferred: true
  title: 'snoDB 2.0: an enhanced interactive database, specializing in human snoRNAs'
  year: '2023'
taxon:
- NCBITaxon:9606
---
# snoDB

snoDB 2.0 is a specialized database dedicated to human small nucleolar RNAs (snoRNAs), providing comprehensive and up-to-date information in an interactive format. Developed at the Université de Sherbrooke, snoDB integrates data from multiple established databases with extensive manual curation from the literature.

## Overview

The database was created to address the need for accurate, centralized information about human snoRNAs. snoDB removes redundancy by merging snoRNA entries from multiple sources based on genomic location, prioritizing data from Ensembl, RefSeq, snoRNA Atlas, snOPY, and literature-based annotations.

## Key Features

### Genomic and Sequence Data
- **Genomic Locations**: All coordinates based on GRCh38 human genome assembly
- **Sequences**: Complete snoRNA sequences with nucleotide-level detail
- **Conservation**: PhastCons conservation scores for 100 vertebrates from UCSC genome browser
- **Host Genes**: Comprehensive host gene information with Gene Ontology functional annotations
- **snoRNA Copies**: Classification based on RFAM families

### snoRNA Structure and Function
- **Motifs and Guide Regions**: Box C, D, C', D' for C/D box snoRNAs; H and ACA boxes for H/ACA snoRNAs
- **Predicted Elements**: Custom algorithms for predicting boxes when not available in literature
- **Target Identification**: Both canonical (rRNA/snRNA) and non-canonical RNA targets

### Interaction Data
- **snoRNA-RNA Interactions**:
  - Canonical interactions with rRNA and snRNA from multiple validated sources
  - Non-canonical interactions from RISE database
  - snoDB-predicted interactions for unannotated snoRNA copies

- **snoRNA-Protein Interactions**:
  - Data from ENCODE eCLIP experiments
  - 150 RNA binding proteins analyzed
  - Filtered for high-confidence interactions (p-value < 0.001)

### Expression and Abundance
- **Tissue Expression**: TGIRT-Seq data from multiple normal tissues (brain, liver, testis, skeletal muscle, ovary, breast, prostate)
- **Cancer Cell Lines**: Expression in HCT116, MCF7, PC3, TOV112D, SKOV
- **Reference Samples**: Universal Human RNA (UHR) and Human Brain Reference (HBR)
- **Host Gene Abundance**: Parallel abundance measurements for host genes

### rRNA Modifications
- **Modification Sites**: Comprehensive catalog of human rRNA modification positions
- **Guide Mapping**: Links between snoRNAs and their target modification sites
- **Validation Status**: Positions marked as validated or predicted
- **Modification Levels**: Quantitative data from RiboMethSeq, HydraPsiSeq, and mass spectrometry studies
- **Multiple rRNA Versions**: Support for snoRNABase, Ensembl, and RefSeq rRNA reference sequences

## Data Sources

snoDB integrates data from:
- **Databases**: Ensembl, RefSeq, snoRNA Atlas, snOPY, RFAM, RISE
- **Literature**: Manually curated from publications
- **Functional Data**: Gene Ontology, ENCODE eCLIP
- **Sequencing Data**: TGIRT-Seq from GEO and SRA repositories
- **Conservation**: UCSC genome browser PhastCons scores
- **Modifications**: RiboMethSeq, HydraPsiSeq, SILNAS studies

## Interactive Features

- **Advanced Search**: Filter and search across multiple snoRNA attributes
- **Column Visibility**: Customize table views
- **Data Export**: Download filtered datasets
- **Abundance Viewer**: Interactive visualization of expression patterns
- **Sequence Search**: Find snoRNAs by sequence similarity
- **Statistics Dashboard**: Overview of database contents with distribution charts

## Associated Tools

### snoRupdate
A C++ tool for integrating snoDB snoRNAs into genome annotations. Compatible with both Ensembl and RefSeq GTF files, enabling incorporation of up-to-date snoRNA annotations into RNA-Seq analysis pipelines.

## Data Processing

- **Unique Entries**: Merged based on genomic overlap with prioritized source order
- **Motif Prediction**: Custom algorithms with Hamming distance-based degenerate sequence matching
- **Structure Prediction**: RNAfold (ViennaRNA) for H/ACA snoRNA hairpin regions
- **Host Gene Assignment**: Overlap analysis with manual curation to remove pseudogenes
- **Interaction Filtering**: Statistical thresholds and replicate consistency requirements

## Version History

Current version: 2.0.0. The previous version remains accessible for legacy analyses.

## Contact

- **Database Inquiries**: Danny Bergeron (danny.bergeron@usherbrooke.ca)
- **Principal Investigator**: Michelle Scott (Michelle.Scott@USherbrooke.ca)
- **Institution**: Université de Sherbrooke, Department of Biochemistry and Functional Genomics