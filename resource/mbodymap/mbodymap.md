---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: evolgeniusteam
  label: Chen Lab (evolgeniusteam)
creation_date: '2026-09-16T00:00:00Z'
description: mBodyMap is a curated database of microbes across the human body and
  their associations with health and diseases. It re-annotates the microbial contents
  of public metagenomic and amplicon samples with a common pipeline and manually curates
  the metadata of the human hosts, then organizes samples by body site and by disease
  so that datasets can be integrated and compared. At publication (2022) it held 63,148
  runs, 14,401 metagenomes and 48,747 amplicons, from 136 projects across 22 body
  sites and 56 diseases, with precomputed abundance and prevalence for 6,247 species
  in 1,645 genera stratified by body site and disease.
domains:
- biomedical
- microbiology
homepage_url: https://mbodymap.microbiome.cloud/
id: mbodymap
last_modified_date: '2026-09-16T00:00:00Z'
layout: resource_detail
name: mBodyMap
products:
- category: GraphicalInterface
  description: Web interface for browsing microbes by body site, by health and disease
    phenotype and by taxon, with curated project and run pages and graphical comparisons
    of abundance and prevalence
  format: http
  id: mbodymap.site
  name: mBodyMap web site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mbodymap
  product_url: https://mbodymap.microbiome.cloud/
- category: ProgrammingInterface
  description: REST API and MCP server over the production MicroMap Neo4j graph, with
    endpoints for taxa, diseases, metabolites, drugs, genes, proteins, pathways, biomarker
    signatures, papers, cross-feeding networks, provenance and graph traversal. Access
    requires a Graphomics API key. The API application code is in the open-source
    repository.
  format: http
  id: micromap.api
  is_neo4j: true
  is_public: false
  name: MicroMap API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: micromap
  - relation_type: prov:wasDerivedFrom
    source: ncbitaxon
  - relation_type: prov:wasDerivedFrom
    source: disbiome
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: chembl
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: semmeddb
  - relation_type: prov:wasDerivedFrom
    source: gutmdisorder
  - relation_type: prov:wasDerivedFrom
    source: bugsigdb
  - relation_type: prov:wasDerivedFrom
    source: gmrepo
  - relation_type: prov:wasDerivedFrom
    source: mbodymap
  product_url: https://www.graphomics.com/docs
publications:
- authors:
  - Jin H
  - Hu G
  - Sun C
  - Duan Y
  - Zhang Z
  - Liu Z
  - Zhao XM
  - Chen WH
  doi: 10.1093/nar/gkab973
  id: https://www.ncbi.nlm.nih.gov/pubmed/34718713
  journal: Nucleic Acids Res
  preferred: true
  title: 'mBodyMap: a curated database for microbes across human body and their associations
    with health and diseases'
  year: '2022'
taxon:
- NCBITaxon:9606
---
mBodyMap is a curated database of microbes across the human body and their
associations with health and disease. It comes from the same group as
[GMrepo](gmrepo) and extends the same approach past the gut to 22 body sites.

## Content

At publication in 2022 the database held 63,148 runs from 136 projects,
covering 22 body sites and 56 diseases. Samples are re-annotated with one
pipeline and the host metadata are curated by hand. Precomputed abundance and
prevalence are given for 6,247 species and 1,645 genera, stratified by body
site and by disease. Phenotypes carry MeSH identifiers and taxa carry NCBI
Taxonomy identifiers.

## Access

The web site is at https://mbodymap.microbiome.cloud/. It is a single-page
application with pages for body sites, phenotypes, taxa, projects and runs. I
did not find a bulk download or a documented API on 2026-09-16 and I did not
find a stated data license.

## Used by

[MicroMap](micromap) loads mBodyMap for body-site associations.