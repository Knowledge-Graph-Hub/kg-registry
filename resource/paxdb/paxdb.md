---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://pax-db.org/
  - contact_type: email
    value: paxdb.team@gmail.com
  label: PaxDb
- category: Individual
  contact_details:
  - contact_type: email
    value: mering@imls.uzh.ch
  label: Christian von Mering
  orcid: 0000-0001-7734-9102
- category: Individual
  contact_details:
  - contact_type: email
    value: qingyao.huang@uzh.ch
  label: Qingyao Huang
creation_date: '2026-06-17T00:00:00Z'
description: PaxDb (Protein Abundance Database) is a meta-resource of whole-organism
  and tissue-specific protein abundance data, expressed in parts per million, for
  over 400 species across all kingdoms of life. It integrates published quantitative
  proteomics datasets and, since v6.0, raw mass spectrometry data from ProteomeXchange
  re-analyzed with a uniform FragPipe pipeline, mapped to STRING protein identifiers,
  scored for consistency against the STRING interaction network, and linked to UniProt,
  eggNOG orthologous groups, and tissue ontologies. It is developed by the von Mering
  group at the University of Zurich and the Swiss Institute of Bioinformatics.
domains:
- proteomics
funding:
- University of Zurich
- Swiss Institute of Bioinformatics
homepage_url: https://pax-db.org/
id: paxdb
last_modified_date: '2026-11-22T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: PaxDb
products:
- category: GraphicalInterface
  description: Web interface for searching proteins and browsing protein abundance
    datasets by species, tissue and dataset, with per-protein abundance profiles,
    orthologs and links to STRING and UniProt.
  format: http
  id: paxdb.site
  is_public: true
  name: PaxDb Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  product_url: https://pax-db.org/
- category: Product
  description: Directory of bulk downloads for the current PaxDb release (v6.1),
    including per-species abundance datasets, orthologs, protein sequences, SDRF
    metadata, mapped peptides and UniProt mappings. Previous releases back to 1.0
    are under https://pax-db.org/downloads/.
  format: mixed
  id: paxdb.downloads
  name: PaxDb Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  product_url: https://pax-db.org/downloads/latest/
- category: Product
  description: Protein abundance datasets, one directory per NCBI Taxonomy species
    ID, with one tab-delimited text file per dataset (integrated whole-organism, tissue,
    cell line or condition) giving gene name, STRING protein identifier and abundance
    in parts per million, with a header of dataset metadata, source publication and
    consistency score.
  format: txt
  id: paxdb.datasets
  name: PaxDb Protein Abundance Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  product_url: https://pax-db.org/downloads/latest/datasets/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: proteomexchange
  - relation_type: prov:used
    source: string
- category: MappingProduct
  compression: zip
  description: Ortholog files per eggNOG taxonomic level, grouping PaxDb proteins
    into eggNOG orthologous groups for cross-species abundance comparison (v6.1).
  format: txt
  id: paxdb.orthologs
  name: PaxDb Orthologs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: eggnog
  product_file_size: 51657471
  product_url: https://pax-db.org/downloads/latest/paxdb-orthologs-v6.1.zip
- category: Product
  compression: zip
  description: FASTA protein sequences per species used by PaxDb v6.1, following
    STRING genome versions and protein identifiers.
  format: fasta
  id: paxdb.protein-sequences
  name: PaxDb Protein Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: string
  product_file_size: 67240395
  product_url: https://pax-db.org/downloads/latest/paxdb-protein-sequences-v6.1.zip
- category: Product
  compression: zip
  description: Sample and Data Relationship Format (SDRF) metadata files for the
    ProteomeXchange projects reprocessed in PaxDb v6.1, one file per PXD project.
  format: tsv
  id: paxdb.sdrf
  name: PaxDb SDRF Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_file_size: 42426
  product_url: https://pax-db.org/downloads/latest/paxdb-sdrf-v6.1.zip
- category: Product
  compression: zip
  description: Peptide-level identification and quantity files mapped to PaxDb proteins,
    per species and dataset (v6.1).
  format: txt
  id: paxdb.mapped-peptides
  name: PaxDb Mapped Peptides
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  product_file_size: 231991110
  product_url: https://pax-db.org/downloads/latest/paxdb-mapped_peptides-v6.1.zip
- category: MappingProduct
  compression: zip
  description: Tab-delimited mapping of PaxDb (STRING) protein identifiers to UniProt
    accessions (v6.1).
  format: tsv
  id: paxdb.uniprot-links
  name: PaxDb UniProt Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: string
  product_file_size: 17181630
  product_url: https://pax-db.org/downloads/latest/paxdb-uniprot-links-v6.1.zip
- category: MappingProduct
  description: Two-column text file of UniProt accessions and the corresponding PaxDb
    (STRING) protein identifiers.
  format: txt
  id: paxdb.uniprot-crossreferences
  name: PaxDb UniProt Cross-references
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 85554748
  product_url: https://pax-db.org/downloads/latest/paxdb-uniprot-crossreferences.txt
- category: ProgrammingInterface
  connection_url: https://api.pax-db.org/v6
  description: REST API (OpenAPI, v6.1) for protein, dataset, species and tissue
    metadata, abundance values by protein, dataset or ortholog group, eggNOG orthology
    lookups, and identifier disambiguation.
  format: http
  id: paxdb.api
  is_public: true
  name: PaxDb API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  product_url: https://api.pax-db.org/docs
  warnings:
  - Requests need an x-api-key header; a free key is available from https://api.pax-db.org/request-api-key,
    and keyless requests fall back to a rate-limited shared test scope.
- category: GraphicalInterface
  description: Web tool for uploading peptide counts or intensities to compute protein
    abundances with the PaxDb pipeline, score the dataset by STRING interaction consistency,
    and compare it with PaxDb reference datasets for the same species.
  format: http
  id: paxdb.compute
  is_public: true
  name: PaxDb Abundance Computation Tool
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  product_url: https://pax-db.org/compute
  secondary_source:
  - relation_type: prov:used
    source: string
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
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - Qingyao Huang
  - Damian Szklarczyk
  - John Oehninger
  - Christian von Mering
  doi: 10.1093/nar/gkaf1066
  id: https://doi.org/10.1093/nar/gkaf1066
  journal: Nucleic Acids Research
  preferred: true
  title: 'PaxDb v6.0: reprocessed, LLM-selected, curated protein abundance data across
    organisms'
  year: '2026'
- authors:
  - Qingyao Huang
  - Damian Szklarczyk
  - Mingcong Wang
  - Milan Simonovic
  - Christian von Mering
  doi: 10.1016/j.mcpro.2023.100640
  id: https://doi.org/10.1016/j.mcpro.2023.100640
  journal: Molecular & Cellular Proteomics
  title: 'PaxDb 5.0: Curated Protein Quantification Data Suggests Adaptive Proteome
    Changes in Yeasts'
  year: '2023'
- authors:
  - Mingcong Wang
  - Christina J. Herrmann
  - Milan Simonovic
  - Damian Szklarczyk
  - Christian von Mering
  doi: 10.1002/pmic.201400441
  id: https://doi.org/10.1002/pmic.201400441
  journal: PROTEOMICS
  title: 'Version 4.0 of PaxDb: Protein abundance data, integrated across model organisms,
    tissues, and cell‐lines'
  year: '2015'
- authors:
  - M. Wang
  - M. Weiss
  - M. Simonovic
  - G. Haertinger
  - S.P. Schrimpf
  - M.O. Hengartner
  - C. von Mering
  doi: 10.1074/mcp.o111.014704
  id: https://doi.org/10.1074/mcp.o111.014704
  journal: Molecular & Cellular Proteomics
  title: PaxDb, a Database of Protein Abundance Averages Across All Three Domains
    of Life
  year: '2012'
rrid: SCR_018910
synonyms:
- PaxDB
- Protein Abundance Database
version: '6.1'
---
# PaxDb

PaxDb (Protein Abundance Database) is a meta-resource of protein abundance data
spanning more than 400 species. It does not accept direct submissions; instead it
draws on published experiments and primary proteomics repositories, re-processes them
through a unified pipeline, and maps them to STRING protein identifiers so that
abundance values (in parts per million) can be compared within and across species.

The v6.0 release (2025) integrated 1,639 datasets from 392 species. It added an
end-to-end reprocessing pipeline that re-analyzes raw ProteomeXchange mass spectrometry
files with FragPipe, large-language-model classifiers that help curators select relevant
ProteomeXchange projects, SDRF sample metadata, and a web tool for computing and scoring
abundances from user data. The current release is v6.1.

Content includes:

- Integrated whole-organism and tissue, cell-line and condition-specific abundance datasets
- A consistency score for each dataset, based on co-abundance of STRING interaction partners
- eggNOG ortholog groups for cross-species comparison
- Tissue and sample annotation with UBERON, PO, CL, CLO and BTO
- Mappings to UniProt accessions
- Bulk downloads for every release since 1.0 and a REST API

All copyrightable parts of the database are licensed under CC BY 4.0.

GeneCards and OmicsDI integrate protein abundance data from PaxDb.
