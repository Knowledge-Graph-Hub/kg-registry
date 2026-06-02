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
- category: Product
  description: Current comprehensive GENCODE gene annotations for the mouse GRCm39
    genome assembly in GTF format
  format: gff
  id: gencode.mouse.gtf
  latest_version: M38
  name: GENCODE Mouse Annotations GTF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gencode
  product_file_size: 37627563
  product_url: https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M38/gencode.vM38.annotation.gtf.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: mgi
  - relation_type: prov:wasInformedBy
    source: ncbigene
- category: GraphProduct
  description: GP-KG tab-delimited knowledge graph containing 1,246,726 associations
    between 61,146 entities from multiple genotypic and phenotypic databases
  format: tsv
  id: kg-predict.gpkg
  name: GP-KG Knowledge Graph Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 48397035
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: string
  - relation_type: prov:wasDerivedFrom
    source: umls
- category: GraphicalInterface
  description: Web-based interface for searching, querying, and analyzing mouse data
    from MGI through MouseMine
  format: http
  id: mousemine.web
  name: MouseMine Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mousemine
  product_url: https://www.mousemine.org/mousemine/begin.do
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasInfluencedBy
    source: intermine
- category: ProgrammingInterface
  description: Programmatic access to MouseMine data via RESTful web services with
    client libraries for Perl, Python, Ruby, and Java
  format: http
  id: mousemine.api
  is_public: true
  name: MouseMine API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mousemine
  product_url: https://www.mousemine.org/mousemine/api.do
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasInfluencedBy
    source: intermine
- category: GraphicalInterface
  description: Pre-built query templates for common data retrieval tasks covering
    genome features, proteins, expression, interactions, phenotypes, diseases, and
    more
  format: http
  id: mousemine.templates
  name: MouseMine Query Templates
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mousemine
  product_url: https://www.mousemine.org/mousemine/templates.do
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasInfluencedBy
    source: intermine
- category: GraphicalInterface
  description: Custom query construction tool for building complex, iterative queries
    across multiple data types
  format: http
  id: mousemine.querybuilder
  name: MouseMine QueryBuilder
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mousemine
  product_url: https://www.mousemine.org/mousemine/customQuery.do
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasInfluencedBy
    source: intermine
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