---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: marinkaz
  label: Marinka Zitnik
  orcid: 0000-0001-8530-7228
- category: Individual
  contact_details:
  - contact_type: email
    value: lucas_vittor@hms.harvard.edu
  label: Lucas Vittor
  orcid: 0009-0002-6978-0482
creation_date: '2026-11-24T00:00:00Z'
description: OptimusKG is a multimodal biomedical labeled property graph from the
  Zitnik Lab at Harvard Medical School, built from structured and semi-structured
  resources with type-specific metadata across molecular, anatomical, clinical, and
  environmental domains. It supersedes PrimeKG. Dataset version 3.2 has 192,813 nodes
  of 10 types and 21,834,669 edges.
domains:
- biomedical
- precision medicine
- pathways
- systems biology
funding:
- National Science Foundation (CAREER 2339524)
- ARPA-H Biomedical Data Fabric (BDF) Toolbox Program
- Harvard Data Science Initiative
homepage_url: https://optimuskg.ai
id: optimuskg
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0 (dataset); source-specific licenses apply; MIT License (code)
name: OptimusKG
products:
- category: GraphProduct
  description: All OptimusKG nodes in one Parquet file. Counts were read from the
    file.
  format: parquet
  id: optimuskg.nodes
  latest_version: '3.2'
  name: OptimusKG Nodes
  node_count: 192813
  original_source:
  - relation_type: prov:hadPrimarySource
    source: optimuskg
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: nsides
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 116094167
  product_url: https://dataverse.harvard.edu/api/access/datafile/14220908
- category: GraphProduct
  description: All OptimusKG edges in one Parquet file. Counts were read from the
    file.
  edge_count: 21834669
  format: parquet
  id: optimuskg.edges
  latest_version: '3.2'
  name: OptimusKG Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: optimuskg
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: nsides
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 179606962
  product_url: https://dataverse.harvard.edu/api/access/datafile/14220909
- category: GraphProduct
  description: Nodes of the largest connected component of OptimusKG.
  format: parquet
  id: optimuskg.lcc.nodes
  latest_version: '3.2'
  name: OptimusKG Largest Connected Component Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: optimuskg
  product_file_size: 116047497
  product_url: https://dataverse.harvard.edu/api/access/datafile/14220921
- category: GraphProduct
  description: Edges of the largest connected component of OptimusKG.
  format: parquet
  id: optimuskg.lcc.edges
  latest_version: '3.2'
  name: OptimusKG Largest Connected Component Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: optimuskg
  product_file_size: 179502680
  product_url: https://dataverse.harvard.edu/api/access/datafile/14220897
- category: Product
  description: Harvard Dataverse dataset with the full graph and separate Parquet
    files for each node and edge type.
  format: parquet
  id: optimuskg.dataverse
  latest_version: '3.2'
  name: OptimusKG on Harvard Dataverse
  original_source:
  - relation_type: prov:hadPrimarySource
    source: optimuskg
  product_url: https://doi.org/10.7910/DVN/IYNGEV
  warnings:
  - 'File was not able to be retrieved when checked on 2026-11-24: HTTP 202 error
    when accessing file'
- category: ProgrammingInterface
  description: Python package for downloading OptimusKG files and loading the graph
    as Polars data frames or a NetworkX graph.
  format: python
  id: optimuskg.client
  is_public: true
  license: &id001
    id: https://opensource.org/licenses/MIT
    label: MIT License
  name: OptimusKG Python Client
  original_source:
  - relation_type: prov:hadPrimarySource
    source: optimuskg
  product_url: https://pypi.org/project/optimuskg/
- category: ProcessProduct
  description: Kedro pipeline that builds OptimusKG, with an agent skill and an MCP
    Bundle for querying the graph.
  format: python
  id: optimuskg.code
  license: *id001
  name: OptimusKG Pipeline
  original_source:
  - relation_type: prov:hadPrimarySource
    source: optimuskg
  product_url: https://github.com/mims-harvard/OptimusKG
- category: DocumentationProduct
  description: Documentation for the OptimusKG data, client, and graph schema.
  format: http
  id: optimuskg.docs
  name: OptimusKG Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: optimuskg
  product_url: https://optimuskg.ai/docs
publications:
- authors:
  - Lucas Vittor
  - Ayush Noori
  - Iñaki Arango
  - Joaquín Polonuer
  - Sam Rodriques
  - Andrew White
  - David A. Clifton
  - Marinka Zitnik
  doi: 10.1038/s41597-026-08302-z
  id: doi:10.1038/s41597-026-08302-z
  journal: Scientific Data
  preferred: true
  title: Unifying biomedical knowledge in a modern multimodal graph
  year: '2026'
repository: https://github.com/mims-harvard/OptimusKG
taxon:
- NCBITaxon:9606
version: '3.2'
---
# OptimusKG

OptimusKG is a biomedical property graph from the Zitnik Lab at Harvard Medical School. It is built with
BioCypher and the Biolink Model, and it supersedes `primekg`.

The project reports 65 integrated resources and 18 ontologies. The sources listed on the node and edge
products are those named in the pipeline's input catalog; OnSIDES is recorded under its parent
resource, nSIDES, and many of the rest arrive through Open Targets. The project also lists a
protein-protein interaction table whose upstream databases the catalog does not name.

The published description on Dataverse gives slightly lower counts (190,939 nodes and 21,818,752 edges)
than the version 3.2 files.