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
creation_date: '2025-07-08T00:00:00Z'
description: The Chemical Checker (CC) is a data-driven resource of small molecule
  bioactivity data, organized into five levels of increasing complexity, ranging from
  chemical properties to clinical outcomes. It is designed to support computational
  drug discovery tasks.
domains:
- drug discovery
homepage_url: https://chemicalchecker.com/
id: chemicalchecker
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: Chemical Checker
products:
- category: Product
  description: Precomputed signatures for small molecules, suitable for machine learning.
  format: hdf5
  id: chemicalchecker.signatures
  name: Chemical Checker Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  product_url: https://chemicalchecker.com/downloads/root
- category: ProcessProduct
  description: Software tool for producing bioactivity signature vectors.
  format: python
  id: chemicalchecker.signaturizer
  name: Signaturizer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  product_url: https://github.com/sbnb-irb/signaturizer
- category: ProgrammingInterface
  description: Programmatic interface for Chemical Checker data.
  format: http
  id: chemicalchecker.api
  name: Chemical Checker RESTful API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  product_url: https://chemicalchecker.com/api/db/getSignature/
- category: DocumentationProduct
  description: Main Chemical Checker portal for searching molecules, browsing statistics, help, and downloads.
  format: http
  id: chemicalchecker.portal
  name: Chemical Checker Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  product_url: https://chemicalchecker.com/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: http
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
repository: https://github.com/sbnb-irb/chemical-checker
taxon:
- NCBITaxon:9606
---
# Chemical Checker (CC)

The Chemical Checker (CC) is a data-driven resource of small-molecule similarity
and bioactivity signatures organized across multiple levels of biological
evidence, from chemistry and targets to pathways, cells, indications, side
effects, and clinical outcomes. It is designed to support computational drug
discovery, repositioning, and systematic comparison of compounds from many
biological viewpoints.

In KG-Registry, the owned Chemical Checker products point to the live portal,
downloads surface, signaturization tooling, and API. The Bioteque embeddings
product is retained as a downstream derivative that reuses Chemical Checker among
many other upstream resources.