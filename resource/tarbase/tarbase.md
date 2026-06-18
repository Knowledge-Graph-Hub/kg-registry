---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: TarBase v9.0 is a comprehensive database of experimentally supported
  miRNA targets on protein-coding transcripts. It contains interactions identified
  via high-throughput methods (HITS-CLIP, PAR-CLIP, CLASH) and low-throughput experimental
  validation, all uniformly analyzed and manually curated with rich metadata.
domains:
- genomics
- biological systems
homepage_url: https://dianalab.e-ce.uth.gr/tarbasev9
id: tarbase
last_modified_date: '2026-05-26T00:00:00Z'
layout: resource_detail
name: TarBase
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing experimentally supported miRNA-gene
    interactions
  format: http
  id: tarbase.portal
  name: TarBase Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9
- category: GraphicalInterface
  description: Interactive search interface for querying miRNA targets and gene miRNomes
    with advanced filtering options
  format: http
  id: tarbase.interactions
  name: Interactions Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/#/interactions
- category: GraphicalInterface
  description: Network visualization tool for assessing combinatorial effects of multiple
    miRNAs on common gene targets
  format: http
  id: tarbase.visualizations
  name: Visualizations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/#/visualizations
- category: GraphicalInterface
  description: Statistics page showing database content and coverage metrics
  format: http
  id: tarbase.statistics
  name: Statistics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/#/statistics
- category: GraphicalInterface
  description: Text-mining interface for literature-based interaction discovery
  format: http
  id: tarbase.textmining
  name: Text-Mining Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/#/textmining
- category: Product
  compression: gzip
  description: Experimentally validated miRNA-gene interactions for Homo sapiens in
    tab-delimited format
  format: tsv
  id: tarbase.homo-sapiens
  name: Homo sapiens Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_file_size: 111135987
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/data/Homo_sapiens_TarBase-v9.tsv.gz
- category: Product
  compression: gzip
  description: Experimentally validated miRNA-gene interactions for Mus musculus in
    tab-delimited format
  format: tsv
  id: tarbase.mus-musculus
  name: Mus musculus Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_file_size: 16498710
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/data/Mus_musculus_TarBase-v9.tsv.gz
- category: Product
  compression: gzip
  description: Experimentally validated viral miRNA-gene interactions in tab-delimited
    format
  format: tsv
  id: tarbase.viral
  name: Viral Species Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_file_size: 884524
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/data/Viral_species_TarBase-v9.tsv.gz
- category: Product
  compression: gzip
  description: Experimentally validated miRNA-gene interactions for other species
    in tab-delimited format
  format: tsv
  id: tarbase.other-species
  name: Other Species Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_file_size: 164821
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/data/Other_species_TarBase-v9.tsv.gz
- category: DocumentationProduct
  description: Comprehensive help documentation with query examples and filtering
    options
  format: http
  id: tarbase.help
  name: Help Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/#/help
  warnings: []
- category: DocumentationProduct
  description: Downloads page with file format specifications and field descriptions
  format: http
  id: tarbase.downloads-doc
  name: Downloads Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tarbase
  product_url: https://dianalab.e-ce.uth.gr/tarbasev9/downloads
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-16: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-13: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-17: HTTP 404 error
    when accessing file'
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
  - Skoufos
  - Kakoulidis
  - Tastsoglou
  - Zacharopoulou
  - Kotsira
  - Miliotis
  - Mavromati
  - Grigoriadis
  - Zioga
  - Velli
  - Koutou
  - Karagkouni
  - Stavropoulos
  - Kardaras
  - Lifousi
  - Vavalou
  - Ovsepian
  - Skoulakis
  - Tasoulis
  - Georgakopoulos
  - Plagianakos
  - Hatzigeorgiou
  doi: 10.1093/nar/gkad1071
  id: https://doi.org/10.1093/nar/gkad1071
  journal: Nucleic Acids Research
  preferred: true
  title: TarBase-v9.0 extends experimentally supported miRNA–gene interactions to
    cell-types and virally encoded miRNAs
  year: '2024'
---
# TarBase

TarBase v9.0 is the reference database of experimentally supported microRNA (miRNA) targets on protein-coding transcripts. Developed and maintained by the DIANA Lab at the University of Thessaly, TarBase provides researchers with a comprehensive, curated collection of validated miRNA-gene interactions.

## Overview

TarBase exclusively contains experimentally supported miRNA-gene interactions identified through both high-throughput and low-throughput methods. The database represents a critical resource for researchers studying post-transcriptional gene regulation mediated by microRNAs.

## Database Content

### Experimental Methods

TarBase integrates interactions from two main sources:

1. **High-Throughput Interactome Mapping**: Raw datasets from state-of-the-art methods including:
   - HITS-CLIP (High-throughput sequencing of RNA isolated by crosslinking immunoprecipitation)
   - PAR-CLIP (Photoactivatable ribonucleoside-enhanced crosslinking and immunoprecipitation)
   - CLASH (Crosslinking, ligation and sequencing of hybrids)
   - microCLIP (with super learner framework scoring)

2. **Low-Throughput Validation**: miRNA targets verified through manual curation of published literature and traditional experimental methods

All datasets are uniformly analyzed to maintain consistently high-quality standards across the database.

### Species Coverage

TarBase v9.0 provides interaction data for multiple species, organized into separate downloadable files:
- **Homo sapiens** (Human)
- **Mus musculus** (Mouse)
- **Viral species** (Including EBV and other virally-encoded miRNAs)
- **Other species**

### Annotations and Standards

TarBase uses standardized nomenclatures for consistency:
- **miRNA annotations**: miRBase v22
- **Gene annotations**: Ensembl 109
- **Genomic coordinates**: Absolute coordinate system relative to the entire genome

## Key Features

### Advanced Query Interface

Users can perform sophisticated searches with:
- **miRNA-to-target queries**: Find all experimentally validated targets for specific miRNAs
- **Gene-to-miRNA queries**: Identify all miRNAs that target specific genes
- **Autofill functionality**: Reduces mistyped entries when entering miRNA names/IDs or gene symbols/IDs

### Comprehensive Filtering Options

Refine searches based on:
- miRNA confidence level (according to miRBase annotation)
- DIANA-microT-CDS prediction scores
- Cell line, cell type, and tissue
- Experimental conditions and methods
- Species
- miRNA expression levels
- Binding site information
- microCLIP super learner framework scores

### Rich Metadata

Each miRNA-gene interaction includes detailed information:
- **Experimental context**: Method, technique, cell line, cell type, tissue, treatment conditions
- **Genomic details**: Binding site coordinates, transcript region (3'UTR, CDS, etc.), chromosome, strand
- **Validation details**: Regulation type (up/down-regulation), validation type, phenotype
- **Publication information**: PubMed ID linking to source literature
- **Confidence metrics**: Biological replicate consistency, interaction group rankings
- **Prediction scores**: DIANA-microT-CDS 2023 scores for experimental interactions

### Interactive Visualizations

TarBase provides network graph visualizations to explore:
- Combinatorial effects of multiple miRNAs on common targets
- Network structure requires genes interacting with at least two selected miRNAs
- Visual representation with miRNAs and target genes as distinct node types

### Integration with External Resources

TarBase is interconnected with:
- **PubMed**: Direct links to supporting publications
- **Ensembl**: Gene and transcript coordinate links
- **miRBase**: miRNA sequence and annotation details
- **DIANA-microT 2023**: Over 86 million in-silico predicted miRNA targets for complementary analysis

## Data Downloads

Complete interaction datasets are freely available in tab-delimited format (gzip-compressed) for:
- Homo sapiens
- Mus musculus
- Viral species
- Other species

Each download file includes 22 fields per interaction, providing comprehensive details about:
- Species, miRNA, and gene identifiers
- Binding site genomic coordinates
- Experimental methodology and conditions
- Regulation type and confidence metrics
- DIANA-microT-CDS prediction scores

## Accessibility

TarBase v9.0 is completely free and open to all users without any registration or login requirements, supporting the principles of open science and data sharing.

## Citation

If TarBase is helpful for your research, please cite:

Giorgos Skoufos, Panos Kakoulidis, Spyros Tastsoglou, Elissavet Zacharopoulou, Vasiliki Kotsira, Marios Miliotis, Galatea Mavromati, Dimitris Grigoriadis, Maria Zioga, Angeliki Velli, Ioanna Koutou, Dimitra Karagkouni, Steve Stavropoulos, Filippos S Kardaras, Anna Lifousi, Eustathia Vavalou, Armen Ovsepian, Anargyros Skoulakis, Sotiris K Tasoulis, Spiros V Georgakopoulos, Vassilis P Plagianakos, Artemis G Hatzigeorgiou (2023). "TarBase-v9.0 extends experimentally supported miRNA–gene interactions to cell-types and virally encoded miRNAs." Nucleic Acids Research, DOI: 10.1093/nar/gkad1071

## Funding

This research has been co-financed by the European Regional Development Fund of the European Union and Greek national funds through the Operational Program Competitiveness, Entrepreneurship and Innovation, under the call RESEARCH – CREATE – INNOVATE (project code: T2EDK-00391).

## Contact

TarBase is developed and maintained by the DIANA Lab at the University of Thessaly, Greece.