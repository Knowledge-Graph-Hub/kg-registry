---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: callahantiff
  label: Tiffany Callahan
description: "PheKnowLator (Phenotype Knowledge Translator; pkt_kg) is a customizable\
  \ knowledge graph (KG) construction framework enabling users to build large, heterogeneous\
  \ KGs that are Semantic Web compliant and amenable to OWL reasoning, generate property\
  \ graphs, and export to formats compatible with popular graph toolkits. The project\
  \ provides configurable build recipes (e.g., OWL, property graph), reproducible pipelines,\
  \ and documentation for deployment and usage in the GitHub Wiki."
domains:
- organisms
- biomedical
- genomics
homepage_url: https://github.com/callahantiff/PheKnowLator
id: pheknowlator
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: PheKnowLator
products:
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse relations.
  id: pheknowlator.graph
  name: PheKnowLator graph
  original_source:
  - cl
  - clo
  - chebi
  - go
  - hp
  - mondo
  - pw
  - pr
  - ro
  - so
  - uberon
  - vo
  - bioportal
  - clinvar
  - ctd
  - disgenet
  - ensembl
  - genemania
  - hgnc
  - hpa
  - ncbigene
  - medgen
  - reactome
  - string
  - uniprot
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  secondary_source:
  - pheknowlator
  latest_version: current_build
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
  format: owl
- category: ProcessProduct
  description: Code for generating PheKnowLator
  id: pheknowlator.code
  name: PheKnowLator code
  original_source:
  - pheknowlator
  product_url: https://github.com/callahantiff/PheKnowLator
  secondary_source:
  - pheknowlator
- category: ProcessProduct
  description: Code for generating MGMLink
  id: mgmlink.code
  name: MGMLink code
  original_source:
  - gutmgene
  - pheknowlator
  product_url: https://github.com/bsantan/MGMLink
  secondary_source:
  - mgmlink
- category: DocumentationProduct
  description: User and developer documentation for PheKnowLator, including build recipes and usage guides
  id: pheknowlator.doc
  name: PheKnowLator Wiki
  original_source:
  - pheknowlator
  product_url: https://github.com/callahantiff/PheKnowLator/wiki
  secondary_source:
  - pheknowlator
publications:
- authors:
  - Callahan TJ
  - Tripodi IJ
  - Hunter LE
  - Baumgartner WA Jr
  doi: 10.1101/2020.04.30.071407
  id: doi:10.1101/2020.04.30.071407
  journal: bioRxiv
  preferred: true
  title: '''A Framework for Automated Construction of Heterogeneous Large-Scale Biomedical
    Knowledge Graphs'''
  year: '2020'
repository: https://github.com/callahantiff/PheKnowLator
usages:
- id: phenoknowlator-build-framework
  label: PheKnowLator build framework
  description: PheKnowLator is used to build heterogeneous biomedical knowledge graphs with OWL semantics and property graph exports using configurable pipelines.
  url: https://github.com/callahantiff/PheKnowLator/wiki
  type: actual
---
PheKnowLator (Phenotype Knowledge Translator) or pkt_kg is the first fully customizable 
knowledge graph (KG) construction framework enabling users to build complex KGs that 
are Semantic Web compliant and amenable to automatic Web Ontology Language (OWL) 
reasoning, generate contemporary property graphs, and are importable by today’s popular 
graph toolkits.