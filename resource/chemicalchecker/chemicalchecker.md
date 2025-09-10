---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: miquel.duran@irbbarcelona.org
  label: Miquel Duran
- category: Individual
  contact_details:
  - contact_type: email
    value: patrick.aloy@irbbarcelona.org
  label: Patrick Aloy
description: The Chemical Checker (CC) is a data-driven resource of small molecule
  bioactivity data, organized into five levels of increasing complexity, ranging from
  chemical properties to clinical outcomes. It is designed to support computational
  drug discovery tasks.
domains:
- drug discovery
homepage_url: http://packages.sbnb-pages.irbbarcelona.org/chemical_checker/
id: chemicalchecker
layout: resource_detail
name: Chemical Checker
products:
- category: Product
  description: Precomputed signatures for small molecules, suitable for machine learning.
  format: hdf5
  id: chemicalchecker.signatures
  name: Chemical Checker Signatures
  product_url: http://packages.sbnb-pages.irbbarcelona.org/chemical_checker/signaturization.html
- category: ProcessProduct
  description: Software tool for producing bioactivity signature vectors.
  format: python
  id: chemicalchecker.signaturizer
  name: Signaturizer
  product_url: https://github.com/sbnb-irb/signaturizer
- category: ProgrammingInterface
  description: Programmatic interface for Chemical Checker data.
  id: chemicalchecker.api
  name: Chemical Checker RESTful API
  product_url: https://chemicalchecker.com/api/db/getSignature/
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
repository: https://github.com/sbnb-irb/chemical-checker
---
# Chemical Checker (CC)

The Chemical Checker (CC) is a data-driven resource of small molecule bioactivity data, organized into five levels of increasing complexity, ranging from chemical properties to clinical outcomes. It is designed to support computational drug discovery tasks.