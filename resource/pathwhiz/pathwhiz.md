---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: david.wishart@ualberta.ca
  - contact_type: url
    value: http://www.wishartlab.com/
  label: Wishart Lab
creation_date: '2025-10-31T00:00:00Z'
description: PathWhiz is a web-based pathway drawing and visualization tool designed
  for creating colorful, visually pleasing, and biologically accurate pathway diagrams
  that are machine-readable and interactive. PathWhiz supports a high level of biological
  detail including metabolites (with automated structure generation), protein complexes
  (with quaternary structures, covalent modifications, and cofactors), nucleic acids,
  membranes, subcellular structures, cells, tissues, and organs. PathWhiz has been
  used to generate over 700 pathway diagrams for popular databases including HMDB,
  DrugBank, and PathBank, and supports export to BioPAX, SBGN-ML, SBML, and PWML formats
  as well as high-resolution images.
domains:
- pathways
- biological systems
- biomedical
- drug discovery
homepage_url: https://pathbank.org/pathwhiz
id: pathwhiz
infores_id: pathwhiz
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: PathWhiz
products:
- category: GraphicalInterface
  description: Web interface for creating, editing, and visualizing biological pathway
    diagrams with automated metabolite structure generation and interactive features
  format: http
  id: pathwhiz.editor
  name: PathWhiz Pathway Editor
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwhiz
  product_url: https://pathbank.org/pathwhiz
- category: GraphicalInterface
  description: Public library of pathway diagrams that can be browsed, viewed, and
    used as templates for creating new pathways
  format: http
  id: pathwhiz.pathways
  name: PathWhiz Pathway Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwhiz
  product_url: https://pathbank.org/pathwhiz/pathways
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: drugbank
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pathbank
- category: GraphicalInterface
  description: Guest drawing interface for trying PathWhiz pathway creation without
    creating a private account
  format: http
  id: pathwhiz.guest_draw
  name: PathWhiz Guest Draw
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwhiz
  product_url: https://pathbank.org/pathwhiz/guest_login
- category: GraphicalInterface
  description: Private drawing interface for creating and managing PathWhiz pathway
    diagrams with an account
  format: http
  id: pathwhiz.private_draw
  name: PathWhiz Private Draw
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwhiz
  product_url: https://pathbank.org/lims
- category: DocumentationProduct
  description: User guide and help documentation for drawing pathways using PathWhiz
  format: http
  id: pathwhiz.guides
  name: PathWhiz User Guides
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathwhiz
  product_url: https://pathbank.org/pathwhiz/guides
  warnings: []
publications:
- authors:
  - Pon A
  - Jewison T
  - Su Y
  - Liang Y
  - Knox C
  - Maciejewski A
  - Wilson M
  - Wishart DS
  doi: 10.1093/nar/gkv399
  id: https://doi.org/10.1093/nar/gkv399
  journal: Nucleic Acids Research
  preferred: true
  title: Pathways with PathWhiz
  year: '2015'
synonyms:
- PathWhiz
- PathWhiz Pathway Editor
warnings:
- The former GitHub repository URL for PathWhiz returned 404 during 2026-06-02 curation,
  so no repository is listed.
- The live PathWhiz page states that commercial reuse of data requires explicit permission
  and acknowledgment; no standard open data license was asserted.
---
