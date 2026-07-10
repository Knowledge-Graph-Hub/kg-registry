---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: asu@scripps.edu
  - contact_type: github
    value: andrewsu
  label: Andrew Su
- category: Individual
  contact_details:
  - contact_type: email
    value: plwhetzel@gmail.com
  - contact_type: github
    value: twhetzel
  label: Trish Whetzel
description: The nde (NIAID Data Ecosystem) KG contains infectious and immune-mediated
  disease datasets. These include datasets from NIAID-funded repositories as well
  as globally-relevant infectious and immune-mediated disease (IID) repositories from
  NIH and beyond. The datasets include -omics data, clinical data, epidemiological
  data, pathogen-host interaction data, flow cytometry, and imaging.
domains:
- biomedical
- immunology
homepage_url: https://data.niaid.nih.gov/
id: nde
layout: resource_detail
license:
  id: https://opensource.org/licenses/Apache-2.0
  label: Apache-2.0
name: NIAID Data Ecosystem KG
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for NIAID Data Ecosystem KG
  format: http
  id: nde.sparql
  name: NIAID Data Ecosystem KG SPARQL
  original_source:
  - source: nde
    relation_type: prov:hadPrimarySource
  product_url: https://apps.okn.us/nde/sparql
- id: nde.tpf
  name: NIAID Data Ecosystem KG TPF
  description: Triple Pattern Fragments endpoint for NIAID Data Ecosystem KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/nde
  original_source:
  - source: nde
    relation_type: prov:hadPrimarySource
- category: GraphProduct
  description: RDF (Turtle) knowledge graph of the NIAID Data Ecosystem, harmonizing
    dataset and computational-tool metadata harvested from NIAID-funded and
    globally-relevant infectious and immune-mediated disease repositories. Served
    through the Proto-OKN FRINK federated SPARQL platform.
  format: ttl
  id: nde.graph
  name: NIAID Data Ecosystem KG (graph)
  product_url: https://frink.apps.renci.org/nde
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nde
  - relation_type: prov:hadPrimarySource
    source: immport
  - relation_type: prov:hadPrimarySource
    source: vdjserver
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
  - relation_type: prov:wasInfluencedBy
    source: sra
  - relation_type: prov:wasInfluencedBy
    source: omicsdi
  - relation_type: prov:wasInfluencedBy
    source: hubmap
  - relation_type: prov:wasInfluencedBy
    source: massive
  - relation_type: prov:wasInfluencedBy
    source: pdb
  - relation_type: prov:wasInfluencedBy
    source: lincs
publications:
- id: https://doi.org/10.48550/arXiv.2509.13524
  authors:
  - Ginger Tsueng
  - Emily Bullen
  - Candice Czech
  - Dylan Welzel
  - Leandro Collares
  - Jason Lin
  - Everaldo Rodolpho
  - Zubair Qazi
  - Nichollette Acosta
  - Lisa M. Mayer
  - Sudha Venkatachari
  - Zorana Mitrović Vučičević
  - Poromendro N. Burman
  - Deepti Jain
  - Jack DiGiovanna
  - Maria Giovanni
  - Asiyah Lin
  - Wilbert Van Panhuis
  - Laura D. Hughes
  - Andrew I. Su
  - Chunlei Wu
  doi: 10.48550/arXiv.2509.13524
  journal: arXiv
  preferred: true
  title: 'The NIAID Discovery Portal: A Unified Search Engine for Infectious and Immune-Mediated
    Disease Datasets'
  year: '2025'
repository: https://github.com/NIAID-Data-Ecosystem/nde-crawlers
taxon:
- NCBITaxon:9606
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-07-02T00:00:00Z'
---
NIAID Data Ecosystem KG

## Automated Evaluation

- View the automated evaluation: [nde automated evaluation](nde_eval_automated.html)
