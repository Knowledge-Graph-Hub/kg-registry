---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: callahantiff
    label: Tiffany Callahan
description: PheKnowLator (Phenotype Knowledge Translator; pkt_kg) is a customizable knowledge graph (KG) construction framework enabling users to build large, heterogeneous KGs that are Semantic Web compliant and amenable to OWL reasoning, generate property graphs, and export to formats compatible with popular graph toolkits. The project provides configurable build recipes (e.g., OWL, property graph), reproducible pipelines, and documentation for deployment and usage in the GitHub Wiki.
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
    format: owl
    id: pheknowlator.graph
    latest_version: current_build
    name: PheKnowLator graph
    original_source:
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: bioportal
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: genemania
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
    secondary_source:
      - source: pheknowlator
        relation_type: prov:wasInfluencedBy
    versions:
      - v1.0.0
      - v2.0.0
      - v2.1.0
      - v3.0.2
      - v4.0.0
      - current_build
  - category: ProcessProduct
    description: Code for generating PheKnowLator
    id: pheknowlator.code
    name: PheKnowLator code
    original_source:
      - source: pheknowlator
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/callahantiff/PheKnowLator
    secondary_source:
      - source: pheknowlator
        relation_type: prov:wasInfluencedBy
  - category: ProcessProduct
    description: Code for generating MGMLink
    id: mgmlink.code
    name: MGMLink code
    original_source:
      - source: gutmgene
        relation_type: prov:hadPrimarySource
      - source: pheknowlator
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/bsantan/MGMLink
    secondary_source:
      - source: mgmlink
        relation_type: prov:wasInfluencedBy
  - category: DocumentationProduct
    description: User and developer documentation for PheKnowLator, including build recipes and usage guides
    id: pheknowlator.doc
    name: PheKnowLator Wiki
    original_source:
      - source: pheknowlator
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/callahantiff/PheKnowLator/wiki
    secondary_source:
      - source: pheknowlator
        relation_type: prov:wasInfluencedBy
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
    title: '''A Framework for Automated Construction of Heterogeneous Large-Scale Biomedical Knowledge Graphs'''
    year: '2020'
repository: https://github.com/callahantiff/PheKnowLator
usages:
  - description: PheKnowLator is used to build heterogeneous biomedical knowledge graphs with OWL semantics and property graph exports using configurable pipelines.
    id: phenoknowlator-build-framework
    label: PheKnowLator build framework
    type: actual
    url: https://github.com/callahantiff/PheKnowLator/wiki
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2025-08-26T00:00:00Z'
---

PheKnowLator (Phenotype Knowledge Translator) or pkt_kg is the first fully customizable 
knowledge graph (KG) construction framework enabling users to build complex KGs that 
are Semantic Web compliant and amenable to automatic Web Ontology Language (OWL) 
reasoning, generate contemporary property graphs, and are importable by today’s popular 
graph toolkits.

## Evaluation

- View the evaluation: [pheknowlator evaluation](pheknowlator_eval.html)
