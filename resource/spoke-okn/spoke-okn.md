---
id: spoke-okn
name: SPOKE-OKN
description: The spoke-okn (SPOKE Open Knowledge Network) KG is a comprehensive biomedical
  and environmental health knowledge graph that integrates diverse data across genomics,
  environmental science, and public health.
activity_status: active
homepage_url: https://spoke.ucsf.edu
contacts:
- category: Individual
  label: Sergio Baranzini
  contact_details:
  - contact_type: email
    value: sergio.baranzini@ucsf.edu
  - contact_type: github
    value: baranzini-lab
license:
  id: https://spoke.rbvi.ucsf.edu/docs/licenses.html
  label: Multiple licenses (see individual data sources)
products:
- id: spoke-okn.sparql
  name: SPOKE-OKN SPARQL
  description: SPARQL endpoint for SPOKE-OKN
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/spoke-okn/sparql
  original_source:
  - source: spoke-okn
    relation_type: prov:hadPrimarySource
- id: spoke-okn.tpf
  name: SPOKE-OKN TPF
  description: Triple Pattern Fragments endpoint for SPOKE-OKN
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/spoke-okn
  original_source:
  - source: spoke-okn
    relation_type: prov:hadPrimarySource
- id: spoke-okn.graph
  name: SPOKE-OKN Graph
  description: The SPOKE-OKN knowledge graph, an OKN-hosted RDF publication of the
    SPOKE biomedical and environmental health knowledge graph, served through FRINK
    query services.
  category: GraphProduct
  format: ttl
  product_url: https://spoke.ucsf.edu
  original_source:
  - source: spoke-okn
    relation_type: prov:hadPrimarySource
  - source: spoke
    relation_type: prov:wasDerivedFrom
  secondary_source:
  - source: bgee
    relation_type: prov:wasInfluencedBy
  - source: bindingdb
    relation_type: prov:wasInfluencedBy
  - source: bv-brc
    relation_type: prov:wasInfluencedBy
  - source: chembl
    relation_type: prov:wasInfluencedBy
  - source: civic
    relation_type: prov:wasInfluencedBy
  - source: cl
    relation_type: prov:wasInfluencedBy
  - source: clinicaltrialsgov
    relation_type: prov:wasInfluencedBy
  - source: diseases
    relation_type: prov:wasInfluencedBy
  - source: doid
    relation_type: prov:wasInfluencedBy
  - source: drugbank
    relation_type: prov:wasInfluencedBy
  - source: drugcentral
    relation_type: prov:wasInfluencedBy
  - source: foodb
    relation_type: prov:wasInfluencedBy
  - source: gdsc
    relation_type: prov:wasInfluencedBy
  - source: go
    relation_type: prov:wasInfluencedBy
  - source: gwascatalog
    relation_type: prov:wasInfluencedBy
  - source: hpa
    relation_type: prov:wasInfluencedBy
  - source: interpro
    relation_type: prov:wasInfluencedBy
  - source: kegg
    relation_type: prov:wasInfluencedBy
  - source: lincs-l1000
    relation_type: prov:wasInfluencedBy
  - source: mesh
    relation_type: prov:wasInfluencedBy
  - source: metacyc
    relation_type: prov:wasInfluencedBy
  - source: ncbigene
    relation_type: prov:wasInfluencedBy
  - source: ncbitaxon
    relation_type: prov:wasInfluencedBy
  - source: omim
    relation_type: prov:wasInfluencedBy
  - source: pathophenodb
    relation_type: prov:wasInfluencedBy
  - source: pfam
    relation_type: prov:wasInfluencedBy
  - source: pid
    relation_type: prov:wasInfluencedBy
  - source: protcid
    relation_type: prov:wasInfluencedBy
  - source: pubmed
    relation_type: prov:wasInfluencedBy
  - source: reactome
    relation_type: prov:wasInfluencedBy
  - source: sider
    relation_type: prov:wasInfluencedBy
  - source: string
    relation_type: prov:wasInfluencedBy
  - source: uberon
    relation_type: prov:wasInfluencedBy
  - source: uniprot
    relation_type: prov:wasInfluencedBy
  - source: wikipathways
    relation_type: prov:wasInfluencedBy
collection:
- okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
domains:
- biomedical
- genomics
- clinical
- precision medicine
- pharmacology
publications:
- authors:
  - John H Morris
  - Karthik Soman
  - Rabia E Akbas
  - Xiaoyuan Zhou
  - Brett Smith
  - Elaine C Meng
  - Conrad C Huang
  - Gabriel Cerono
  - Gregory Schenk
  - Angela Rizk-Jackson
  - A Harroud
  - Lindsey Sanders
  - Simon V Costes
  - Kaustuv Bharat
  - Amit Chakraborty
  - Alex Pico
  - T Mardirossian
  - Michael Keiser
  - Atul Tang
  - J Hardi
  - Y Shi
  - Mark Musen
  - S Israni
  - Sui Huang
  - Peter W Rose
  - Charlotte A Nelson
  - Sergio E Baranzini
  doi: 10.1093/bioinformatics/btad080
  id: https://doi.org/10.1093/bioinformatics/btad080
  journal: Bioinformatics
  preferred: true
  title: 'The scalable precision medicine open knowledge engine (SPOKE): a massive
    knowledge graph of biomedical information'
  year: '2023'
- authors:
  - Sergio E Baranzini
  - Katy Borner
  - John Morris
  - Charlotte A Nelson
  - Karthik Soman
  - Erica Schleimer
  - Michael Keiser
  - Atul Butte
  - Mark Musen
  - Sui Huang
  doi: 10.1002/aaai.12037
  id: https://doi.org/10.1002/aaai.12037
  journal: AI Magazine
  title: A biomedical open knowledge network harnesses the power of AI to understand
    deep human biology
  year: '2022'
repository: https://github.com/baranzini-lab/SPOKE
---
SPOKE-OKN

## Description

SPOKE-OKN is the OKN-hosted publication of the SPOKE biomedical knowledge graph,
exposed through FRINK query services for the OKN ecosystem. The underlying SPOKE
project integrates data from many curated biomedical resources to connect genes,
diseases, compounds, pathways, phenotypes, and clinical concepts for precision
medicine and translational research use cases.

The current SPOKE publications describe a graph assembled from dozens of source
databases and ontologies, with weekly rebuilds and use cases spanning drug
discovery, disease mechanism analysis, and knowledge-guided analysis of clinical
data. The OKN deployment provides web-query access to that graph through FRINK.

## Evaluation

- View the evaluation: [spoke-okn evaluation](spoke-okn_eval_automated.html)

*This resource was automatically synchronized from the FRINK OKN registry.*
