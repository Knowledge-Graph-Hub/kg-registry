---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: JASPAR is an open-access database of curated, non-redundant transcription factor (TF) binding profiles stored as position frequency matrices (PFMs). The profiles span multiple species across six taxonomic groups and are derived from published collections of experimentally defined TF binding sites. JASPAR provides web-based browsing and visualization, programmatic access through a RESTful API, and bulk downloads of the profiles in several standard matrix formats.
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
    description: Bulk downloads of the curated, non-redundant transcription factor binding profiles (position frequency matrices) for all JASPAR collections, available in JASPAR, TRANSFAC, MEME, PFM, and other standard matrix formats.
    format: txt
    id: jaspar.matrices
    name: JASPAR Binding Profile Matrices
    original_source:
      - relation_type: prov:hadPrimarySource
        source: jaspar
    product_url: https://jaspar.elixir.no/downloads/
  - category: ProgrammingInterface
    description: RESTful API for programmatic retrieval of JASPAR transcription factor binding profiles and associated metadata, returning individual matrices in formats such as JASPAR, TRANSFAC, MEME, PFM, and YAML.
    format: http
    id: jaspar.api
    name: JASPAR RESTful API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: jaspar
    product_url: https://jaspar.elixir.no/api/v1/
  - category: GraphicalInterface
    description: Web interface for searching, browsing, and visualizing all JASPAR transcription factor binding profiles and their metadata.
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
publications:
  - authors:
      - Ieva Rauluseviciute
      - Rafael Riudavets-Puig
      - Romain Blanc-Mathieu
      - Jaime A Castro-Mondragon
      - Katalin Ferenc
      - Vipin Kumar
      - Roza Berhanu Lemma
      - Jérémy Lucas
      - Jeanne Chèneby
      - Damir Baranasic
      - Aziz Khan
      - Oriol Fornes
      - Sveinung Gundersen
      - Morten Johansen
      - Eivind Hovig
      - Boris Lenhard
      - Albin Sandelin
      - Wyeth W Wasserman
      - François Parcy
      - Anthony Mathelier
    doi: doi:10.1093/nar/gkad1059
    id: doi:10.1093/nar/gkad1059
    journal: Nucleic Acids Research
    preferred: true
    title: 'JASPAR 2024: 20th anniversary of the open-access database of transcription factor binding profiles'
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
