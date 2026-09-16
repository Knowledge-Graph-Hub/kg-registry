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
description: GMrepo (Gut Microbiome Data Repository) is a curated and consistently
  annotated database of human gut metagenomes and 16S rRNA amplicon datasets. Samples
  are grouped by manually curated host phenotype (health and disease, coded with MeSH)
  and their microbial contents are re-annotated with a common pipeline so that projects
  can be compared across datasets. Version 3 (2026) holds 890 projects and 118,965
  runs, 302 annotated diseases and 1,299 marker taxa for 167 phenotype pairs, with
  a Marker Consistency Index summarizing how reproducible each marker is across studies.
  Data are served through the web site and a RESTful API.
domains:
- biomedical
- microbiology
homepage_url: https://gmrepo.humangut.info/
id: gmrepo
last_modified_date: '2026-09-16T00:00:00Z'
layout: resource_detail
name: GMrepo
products:
- category: GraphicalInterface
  description: Web interface for browsing curated projects, runs, phenotypes, taxa
    and disease markers with graphical selectors and cross-dataset comparison
  format: http
  id: gmrepo.site
  name: GMrepo web site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gmrepo
  product_url: https://gmrepo.humangut.info/
- category: ProgrammingInterface
  connection_url: https://gmrepo.humangut.info/api/
  description: RESTful API giving programmable access to most database contents, such
    as curated project lists, runs and taxa associated with a phenotype MeSH identifier,
    and full taxonomic profiles by run. Example clients in R, Perl and Python are
    in the GMrepoProgrammableAccess repository.
  format: http
  id: gmrepo.api
  is_public: true
  name: GMrepo RESTful API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gmrepo
  product_url: https://github.com/evolgeniusteam/GMrepoProgrammableAccess
  repository: https://github.com/evolgeniusteam/GMrepoProgrammableAccess
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
  - Liu C
  - Wang X
  - Zhang Z
  - Wang W
  - Wang T
  - Zhao Y
  - Wang M
  - Chen WH
  doi: 10.1093/nar/gkaf1190
  id: https://www.ncbi.nlm.nih.gov/pubmed/41277537
  journal: Nucleic Acids Res
  preferred: true
  title: 'GMrepo v3: a curated human gut microbiome database with expanded disease
    coverage and enhanced cross-dataset biomarker analysis'
  year: '2026'
- authors:
  - Dai D
  - Zhu J
  - Sun C
  - Li M
  - Liu J
  - Wu S
  - Ning K
  - He LJ
  - Zhao XM
  - Chen WH
  doi: 10.1093/nar/gkab1019
  id: https://www.ncbi.nlm.nih.gov/pubmed/34788838
  journal: Nucleic Acids Res
  title: 'GMrepo v2: a curated human gut microbiome database with special focus on
    disease markers and cross-dataset comparison'
  year: '2022'
- authors:
  - Wu S
  - Sun C
  - Li Y
  - Wang T
  - Jia L
  - Lai S
  - Yang Y
  - Luo P
  - Dai D
  - Yang YQ
  - Luo Q
  - Gao NL
  - Ning K
  - He LJ
  - Zhao XM
  - Chen WH
  doi: 10.1093/nar/gkz764
  id: https://www.ncbi.nlm.nih.gov/pubmed/31504765
  journal: Nucleic Acids Res
  title: 'GMrepo: a database of curated and consistently annotated human gut metagenomes'
  year: '2020'
taxon:
- NCBITaxon:9606
---
GMrepo is a curated repository of human gut metagenomes and amplicon datasets.
It re-annotates the microbial content of public samples with one pipeline and
curates the host metadata by hand, so that samples from different projects can
be compared by phenotype.

## Content

GMrepo v3 (2026) holds 890 projects and 118,965 runs, of which 87,048 are 16S
rRNA and 31,917 are shotgun metagenomes. It annotates 302 diseases with MeSH
and reports 1,299 marker taxa, 726 species and 573 genera, across 167 phenotype
pairs drawn from 275 curated projects. A Marker Consistency Index gives the
share of studies in which a marker changes in the same direction.

## Access

The web site is at https://gmrepo.humangut.info/. A RESTful API under
`https://gmrepo.humangut.info/api/` answers POST requests for project lists,
phenotype associations and per-run taxonomic profiles. Example clients are in
the [GMrepoProgrammableAccess](https://github.com/evolgeniusteam/GMrepoProgrammableAccess)
repository. Earlier versions served bulk files under `/Downloads/`. On
2026-09-16 that path returned the site's HTML shell and not a file, so no bulk
download product is listed. I did not find a stated data license.

## Related

[mBodyMap](mbodymap) is a sister database from the same group that covers
microbes across body sites beyond the gut.

## Used by

[MicroMap](micromap) loads GMrepo as one of its gut microbiome sources.