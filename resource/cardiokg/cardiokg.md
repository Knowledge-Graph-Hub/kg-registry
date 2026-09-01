---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: github
        value: ImperialCollegeLondon
      - contact_type: url
        value: https://www.imperial.ac.uk/
    label: Imperial College London
creation_date: '2026-06-12T00:00:00Z'
description: CardioKG is a multimodal cardiovascular disease knowledge graph that integrates computer vision-derived cardiovascular phenotypes from biomedical imaging with biomedical database content to model gene, disease, phenotype, pathway, and drug relationships for gene-disease prediction, druggability assessment, and drug repurposing.
domains:
  - biomedical
  - clinical
  - medical imaging
  - precision medicine
homepage_url: https://doi.org/10.5281/zenodo.16025953
id: cardiokg
last_modified_date: '2026-09-01T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/license/mit/
  label: MIT License
name: CardioKG
products:
  - category: GraphProduct
    description: Neo4j construction artifacts for CardioKG, including Cypher scripts to create graph nodes and add edges. The GitHub repository is no longer available; these files are inside the archived Zenodo snapshot.
    dump_format: neo4j
    format: neo4j
    id: cardiokg.neo4j
    name: CardioKG Neo4j graph construction scripts
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cardiokg
      - relation_type: prov:hadPrimarySource
        source: ukbiobank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:used
        source: mesh
      - relation_type: prov:used
        source: mondo
      - relation_type: prov:used
        source: reactome
      - relation_type: prov:used
        source: kegg
      - relation_type: prov:used
        source: uniprot
      - relation_type: prov:used
        source: string
      - relation_type: prov:used
        source: opentargets
    product_url: https://doi.org/10.5281/zenodo.16025953
  - category: Product
    description: CardioKG supporting data tables for anatomy and cardiac magnetic resonance anatomy mappings. The GitHub repository is no longer available; these files are inside the archived Zenodo snapshot.
    format: csv
    id: cardiokg.data
    name: CardioKG supporting data tables
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cardiokg
      - relation_type: prov:hadPrimarySource
        source: ukbiobank
    product_url: https://doi.org/10.5281/zenodo.16025953
  - category: Product
    description: Generated CardioKG embeddings for gene-disease and medication-disease association prediction tasks. The GitHub repository is no longer available; these files are inside the archived Zenodo snapshot.
    id: cardiokg.embeddings
    name: CardioKG generated embeddings
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cardiokg
    product_url: https://doi.org/10.5281/zenodo.16025953
  - category: ProcessProduct
    description: Analysis notebooks and scripts for CardioKG graph construction, PageRank importance analysis, gene-disease association prediction, and drug repurposing. The GitHub repository is no longer available; these files are inside the archived Zenodo snapshot.
    id: cardiokg.workflow
    name: CardioKG analysis workflow
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cardiokg
    product_url: https://doi.org/10.5281/zenodo.16025953
  - category: Product
    compression: zip
    description: Archived CardioKG repository release on Zenodo.
    id: cardiokg.zenodo-archive
    name: CardioKG Zenodo archive
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cardiokg
    product_url: https://doi.org/10.5281/zenodo.16025953
publications:
  - authors:
      - Khaled Rjoob
      - Kathryn A. McGurk
      - Sean L. Zheng
      - Lara Curran
      - Mahmoud Ibrahim
      - Lingyao Zeng
      - Vladislav Kim
      - Shamin Tahasildar
      - Soodeh Kalaie
      - Deva S. Senevirathne
      - Parisa Gifani
      - Vladimir Losev
      - Jin Zheng
      - Wenjia Bai
      - Antonio de Marvao
      - James S. Ware
      - Christian Bender
      - Declan P. O'Regan
    doi: 10.1038/s44161-025-00757-4
    id: doi:10.1038/s44161-025-00757-4
    journal: Nature Cardiovascular Research
    title: A multimodal vision knowledge graph of cardiovascular disease
    year: '2025'
taxon:
  - NCBITaxon:9606
---

CardioKG combines cardiovascular imaging-derived phenotypes with biomedical knowledge
sources to support graph-based prediction of disease genes, pathway enrichment, and
drug repurposing opportunities for cardiovascular disease.

The project's GitHub repository (`ImperialCollegeLondon/cardioKG`) is no longer
available. The archived release deposited on Zenodo is the remaining source for the
graph construction scripts, supporting data tables, generated embeddings and analysis
notebooks, so the products above all resolve to that snapshot.
