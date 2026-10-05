---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://jpostdb.org/contact/
  label: jPOST project
creation_date: '2026-10-04T00:00:00Z'
description: jPOST (Japan ProteOme STandard Repository/Database) is a Japanese proteomics
  data environment and a ProteomeXchange member. jPOSTrepo accepts raw and processed
  mass spectrometry datasets, and jPOSTdb reanalyzes public datasets with a unified
  workflow into a standardized database of peptides, proteins and post-translational
  modifications, also published as RDF. The FAQ states that all data in jPOSTrepo
  and jPOSTdb are released under CC0.
domains:
- proteomics
- biomedical
homepage_url: https://jpostdb.org/
id: jpost
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: jPOST
products:
- category: GraphicalInterface
  description: jPOST project portal with news, help, FAQ and links to the repository
    and database.
  format: http
  id: jpost.portal
  name: jPOST Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://jpostdb.org/
- category: GraphicalInterface
  description: jPOSTrepo, the jPOST data repository for submitting, browsing and downloading
    raw and processed mass spectrometry datasets (JPST and PXD accessions).
  format: http
  id: jpost.repository
  name: jPOST Repository (jPOSTrepo)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://repository.jpostdb.org/
- category: GraphicalInterface
  description: jPOSTdb, the jPOST database of public proteome datasets reanalyzed
    under unified criteria, with filtering ("Globe") and comparison ("Slice") views
    of peptides, proteins and modifications mapped to UniProt.
  format: http
  id: jpost.database
  name: jPOST Database (jPOSTdb)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://globe.jpostdb.org/
- category: Product
  compression: zip
  description: jPOSTdb identified protein table from the NBDC LSDB Archive, with UniProt
    accession, symbol, name, protein type and peptide and PSM counts for reanalyzed
    datasets (about 12 MB, file dated 2021-07-29).
  format: csv
  id: jpost.protein
  name: jPOSTdb Identified Protein Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://dbarchive.biosciencedbc.jp/data/jpostdb/LATEST/jpostdb_protein.zip
  secondary_source:
  - relation_type: prov:used
    source: uniprot
- category: Product
  compression: zip
  description: jPOSTdb peptide spectrum match (PSM) table from the NBDC LSDB Archive,
    with peptide sequence, UniProt accession, experimental and calculated m/z, charge
    and jPOST score (about 68 MB, file dated 2021-07-29).
  format: csv
  id: jpost.psm
  name: jPOSTdb PSM Peptide Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://dbarchive.biosciencedbc.jp/data/jpostdb/LATEST/jpostdb_psm.zip
  secondary_source:
  - relation_type: prov:used
    source: uniprot
- category: Product
  compression: zip
  description: jPOSTdb PSM peptide modification table from the NBDC LSDB Archive,
    with modification type, site and position for each PSM (about 17 MB, file dated
    2021-07-29).
  format: csv
  id: jpost.psm-modification
  name: jPOSTdb PSM Peptide Modification Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://dbarchive.biosciencedbc.jp/data/jpostdb/LATEST/jpostdb_psm_modification.zip
- category: Product
  description: Per-dataset Turtle files of the jPOST database RDF on the NBDC LSDB
    Archive, one directory per JPST dataset.
  format: ttl
  id: jpost.rdf
  name: jPOSTdb RDF Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://dbarchive.biosciencedbc.jp/data/jpostdb/data/rdf/
  secondary_source:
  - relation_type: prov:used
    source: uniprot
  - relation_type: prov:used
    source: ms
  - relation_type: prov:used
    source: faldo
- category: ProgrammingInterface
  description: SPARQL endpoint of the RDF Portal (DBCLS) serving the jPOST database
    RDF (version 202509, about 578 million triples) with the jPOST ontology. The RDF
    Portal lists this dataset under CC BY 4.0.
  format: http
  id: jpost.sparql
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: jPOST Database RDF SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://rdfportal.org/primary/sparql
  versions:
  - '202509'
- category: OntologyProduct
  description: jPOST ontology (Turtle serialization at an .owl URL) defining the classes
    and properties of the jPOST database RDF, importing SIO and reusing PSI-MS, UniProt
    core, Unimod and FALDO terms.
  format: ttl
  id: jpost.ontology
  name: jPOST Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: http://rdf.jpostdb.org/ontology/jpost.owl
  secondary_source:
  - relation_type: prov:used
    source: sio
  - relation_type: prov:used
    source: ms
- category: DocumentationProduct
  description: jPOST help pages covering jPOSTrepo submission, jPOSTdb use, the reanalysis
    workflow and COVID-19 data.
  format: http
  id: jpost.help
  name: jPOST Help
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://jpostdb.org/help/
- category: DocumentationProduct
  description: RDF Portal dataset page for the jPOST database RDF, with dataset statistics,
    schema diagram and example SPARQL queries.
  format: http
  id: jpost.rdf-docs
  name: jPOST Database RDF Dataset Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jpost
  product_url: https://rdfportal.org/dataset/jpostdb/
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
  - Shujiro Okuda
  - Akiyasu C Yoshizawa
  - Daiki Kobayashi
  - Yushi Takahashi
  - Yu Watanabe
  - Yuki Moriya
  - Atsushi Hatano
  - Tomoyo Takami
  - Masaki Matsumoto
  - Norie Araki
  - Tsuyoshi Tabata
  - Mio Iwasaki
  - Naoyuki Sugiyama
  - Yoshio Kodera
  - Satoshi Tanaka
  - Susumu Goto
  - Shin Kawano
  - Yasushi Ishihama
  doi: 10.1093/nar/gkae1032
  id: doi:10.1093/nar/gkae1032
  journal: Nucleic Acids Research
  preferred: true
  title: jPOST environment accelerates the reuse and reanalysis of public proteome
    mass spectrometry data
  year: '2025'
- authors:
  - Yuki Moriya
  - Shin Kawano
  - Shujiro Okuda
  - Yu Watanabe
  - Masaki Matsumoto
  - Tomoyo Takami
  - Daiki Kobayashi
  - Yoshinori Yamanouchi
  - Norie Araki
  - Akiyasu C Yoshizawa
  - Tsuyoshi Tabata
  - Mio Iwasaki
  - Naoyuki Sugiyama
  - Satoshi Tanaka
  - Susumu Goto
  - Yasushi Ishihama
  doi: 10.1093/nar/gky899
  id: doi:10.1093/nar/gky899
  journal: Nucleic Acids Research
  title: 'The jPOST environment: an integrated proteomics data repository and database'
  year: '2019'
- authors:
  - Shujiro Okuda
  - Yu Watanabe
  - Yuki Moriya
  - Shin Kawano
  - Tadashi Yamamoto
  - Masaki Matsumoto
  - Tomoyo Takami
  - Daiki Kobayashi
  - Norie Araki
  - Akiyasu C. Yoshizawa
  - Tsuyoshi Tabata
  - Naoyuki Sugiyama
  - Susumu Goto
  - Yasushi Ishihama
  doi: 10.1093/nar/gkw1080
  id: doi:10.1093/nar/gkw1080
  journal: Nucleic Acids Research
  title: 'jPOSTrepo: an international standard data repository for proteomes'
  year: '2017'
synonyms:
- Japan ProteOme STandard Repository/Database
- jPOSTrepo
- jPOSTdb
---
# jPOST

jPOST (Japan ProteOme STandard Repository/Database) is a proteomics data environment run by the jPOST project, with support from JST and the National Bioscience Database Center (NBDC). It is a member of the ProteomeXchange consortium.

## Components

- **jPOSTrepo** ([repository.jpostdb.org](https://repository.jpostdb.org/)) accepts raw and processed mass spectrometry data and issues JPST and PXD accessions.
- **jPOSTdb** ([globe.jpostdb.org](https://globe.jpostdb.org/)) reanalyzes public datasets with a unified workflow and presents identified peptides, proteins and modifications mapped to UniProt.
- **jPOST database RDF** is served through the DBCLS RDF Portal SPARQL endpoint and as per-dataset Turtle files on the NBDC LSDB Archive. The jPOST ontology defines its schema.

## Data access

The NBDC LSDB Archive offers protein, PSM and PSM modification tables as zip files. These files are dated 2021-07-29, so they lag behind the live database and the RDF (version 202509).

## License

The jPOST FAQ states that all data in jPOSTrepo and jPOSTdb, including COVID-19 data, are released under CC0, and the LSDB Archive README says the same. The RDF Portal dataset page lists the jPOST database RDF under CC BY 4.0. This page uses CC0 for the resource and records the RDF Portal license on the SPARQL product.