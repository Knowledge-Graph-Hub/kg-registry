---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: JASPAR is an open-access database of curated, non-redundant transcription
  factor (TF) binding profiles stored as position frequency matrices (PFMs). The profiles
  span multiple species across six taxonomic groups and are derived from published
  collections of experimentally defined TF binding sites. JASPAR provides web-based
  browsing and visualization, programmatic access through a RESTful API, and bulk
  downloads of the profiles in several standard matrix formats.
domains:
- genomics
- systems biology
- biological systems
homepage_url: https://jaspar.elixir.no/
id: jaspar
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: JASPAR
products:
- category: Product
  description: Bulk downloads of the curated, non-redundant transcription factor binding
    profiles (position frequency matrices) for all JASPAR collections, available in
    JASPAR, TRANSFAC, MEME, PFM, and other standard matrix formats.
  format: txt
  id: jaspar.matrices
  name: JASPAR Binding Profile Matrices
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jaspar
  product_url: https://jaspar.elixir.no/downloads/
- category: ProgrammingInterface
  description: RESTful API for programmatic retrieval of JASPAR transcription factor
    binding profiles and associated metadata, returning individual matrices in formats
    such as JASPAR, TRANSFAC, MEME, PFM, and YAML.
  format: http
  id: jaspar.api
  name: JASPAR RESTful API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jaspar
  product_url: https://jaspar.elixir.no/api/v1/
- category: GraphicalInterface
  description: Web interface for searching, browsing, and visualizing all JASPAR transcription
    factor binding profiles and their metadata.
  format: http
  id: jaspar.web
  name: JASPAR Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jaspar
  product_url: https://jaspar.elixir.no/
- category: DocumentationProduct
  description: Source code for the JASPAR web portal and REST API.
  format: http
  id: jaspar.docs
  name: JASPAR Source Code Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jaspar
  product_url: https://github.com/asntech/jaspar
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
publications:
- authors:
  - Ieva Rauluseviciute
  - Rafael Riudavets-Puig
  - Romain Blanc-Mathieu
  - Jaime A Castro-Mondragon
  - Katalin Ferenc
  - Vipin Kumar
  - Roza Berhanu Lemma
  - "J\xE9r\xE9my Lucas"
  - "Jeanne Ch\xE8neby"
  - Damir Baranasic
  - Aziz Khan
  - Oriol Fornes
  - Sveinung Gundersen
  - Morten Johansen
  - Eivind Hovig
  - Boris Lenhard
  - Albin Sandelin
  - Wyeth W Wasserman
  - "Fran\xE7ois Parcy"
  - Anthony Mathelier
  doi: doi:10.1093/nar/gkad1059
  id: doi:10.1093/nar/gkad1059
  journal: Nucleic Acids Research
  preferred: true
  title: 'JASPAR 2024: 20th anniversary of the open-access database of transcription
    factor binding profiles'
  year: '2024'
repository: https://github.com/asntech/jaspar
---
# JASPAR

JASPAR is an open-access database of curated, non-redundant transcription factor
(TF) binding profiles represented as position frequency matrices (PFMs). The
profiles capture the binding preferences of transcription factors and are
derived from published collections of experimentally defined binding sites,
spanning multiple species across six taxonomic groups.

JASPAR offers a web interface for searching, browsing, and visualizing all
profiles and their metadata, a RESTful API for programmatic access, and bulk
downloads in several standard matrix formats. The database is hosted by ELIXIR
Norway at https://jaspar.elixir.no/ (formerly jaspar.genereg.net).
</content>
</invoke>