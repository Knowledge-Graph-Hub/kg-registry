---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: liangcheng@hrbmu.edu.cn
  label: Liang Cheng
creation_date: '2026-09-16T00:00:00Z'
description: gutMDisorder is a manually curated database of dysbiosis of the gut microbiota
  in disorders and under interventions such as medications, diets and probiotics.
  Each association records the microbe, the condition or intervention, the direction
  of change, the host and the supporting publication. Version 2.0 (2022) added associations
  curated from re-annotated raw sequencing data with manually curated host metadata,
  and interactive charts. Conditions are linked to MeSH and Disease Ontology terms
  and microbes to NCBI Taxonomy. Maintained at Harbin Medical University.
domains:
- biomedical
- microbiology
homepage_url: http://bio-annotation.cn/gutMDisorder/
id: gutmdisorder
last_modified_date: '2026-09-16T00:00:00Z'
layout: resource_detail
name: gutMDisorder
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching gut microbe associations with
    disorders and interventions, with a resource page listing the download files
  format: http
  id: gutmdisorder.site
  name: gutMDisorder web site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gutmdisorder
  product_url: http://bio-annotation.cn/gutMDisorder/
- category: Product
  description: All literature-curated gut microbe associations with disorders and
    interventions from gutMDisorder v2.0, as an Excel workbook
  format: mixed
  id: gutmdisorder.literature_associations
  name: gutMDisorder v2.0 literature associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gutmdisorder
  product_url: http://bio-annotation.cn/gutMDisorder/public/res/2.0-literature-associations.xlsx
- category: Product
  description: Gut microbe associations with disorders and interventions derived from
    re-annotated raw sequencing data in gutMDisorder v2.0, as an Excel workbook
  format: mixed
  id: gutmdisorder.rawdata_associations
  name: gutMDisorder v2.0 raw data associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gutmdisorder
  product_url: http://bio-annotation.cn/gutMDisorder/public/res/2.0-raw%20data-associations.xlsx
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
  - Qi C
  - Cai Y
  - Qian K
  - Li X
  - Ren J
  - Wang P
  - Fu T
  - Zhao T
  - Cheng L
  - Shi L
  - Zhang X
  doi: 10.1093/nar/gkac871
  id: https://www.ncbi.nlm.nih.gov/pubmed/36215029
  journal: Nucleic Acids Res
  preferred: true
  title: 'gutMDisorder v2.0: a comprehensive database for dysbiosis of gut microbiota
    in phenotypes and interventions'
  year: '2023'
- authors:
  - Cheng L
  - Qi C
  - Zhuang H
  - Fu T
  - Zhang X
  doi: 10.1093/nar/gkz843
  id: https://www.ncbi.nlm.nih.gov/pubmed/31584099
  journal: Nucleic Acids Res
  title: 'gutMDisorder: a comprehensive database for dysbiosis of the gut microbiota
    in disorders and interventions'
  year: '2020'
---
gutMDisorder is a manually curated database of changes in the gut microbiota
under disorders and interventions. It was first published in 2020 and updated
to version 2.0 in 2022. It comes from the same group at Harbin Medical
University as [GutMGene](gutmgene).

## Content

Each record links a gut microbe to a condition or an intervention and gives the
direction of change, the host organism, the sample type and the source
publication. Version 2.0 added a second track of associations computed from
re-annotated public raw sequencing data with manually curated host metadata.
Conditions carry MeSH and Disease Ontology identifiers and microbes carry NCBI
Taxonomy identifiers.

## Access

The site serves browse and search pages and a resource page with two Excel
workbooks, one for the literature-curated associations and one for the raw
data associations. The site did not answer from the curation network on
2026-09-16 and the product links were taken from an archived copy of the
resource page. I did not find a stated data license.

## Used by

[MicroMap](micromap) loads gutMDisorder as one of its microbe-disease
association sources.