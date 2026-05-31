---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: mgi-help@jax.org
  - contact_type: url
    value: https://www.jax.org/
  label: The Jackson Laboratory
creation_date: '2026-02-26T00:00:00Z'
description: Mouse Genome Informatics is the international database resource for the
  laboratory mouse, providing integrated genetic, genomic, and biological data to
  support studies of human health and disease.
domains:
- genomics
homepage_url: https://www.informatics.jax.org/
id: mgi
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: Mouse Genome Informatics
products:
- category: GraphicalInterface
  description: Main Mouse Genome Informatics portal for accessing mouse genes, alleles,
    phenotypes, disease models, and related reference data.
  format: http
  id: mgi.portal
  name: Mouse Genome Informatics Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mgi
  product_url: https://www.informatics.jax.org/
- category: Product
  description: mgi Nodes TSV
  format: tsv
  id: obo-db-ingest.mgi.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: mgi Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 6615249
  product_url: https://w3id.org/biopragmatics/resources/mgi/mgi.tsv
- category: GraphProduct
  description: Neo4j graph database integrating Enrichr gene set libraries with genes,
    terms, pathways, diseases, drugs, cell types, and other functional annotations
  dump_format: neo4j
  format: neo4j
  id: enrichr-kg.graph
  name: Enrichr-KG Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
---
# Mouse Genome Informatics

Mouse Genome Informatics (MGI) is The Jackson Laboratory's flagship knowledgebase
for the laboratory mouse. It integrates mouse genes, alleles, strains,
phenotypes, gene expression, disease models, and reference nomenclature so that
mouse biology can be used effectively in comparative and translational research.

This registry page treats the MGI portal as the owned entry point for the
resource itself. The downstream OBO-DB-Ingest and Enrichr-KG products are kept as
propagated products because they legitimately reuse MGI content in derivative
integration workflows.