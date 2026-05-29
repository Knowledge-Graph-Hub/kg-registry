---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: hblin23@m.fudan.edu.cn
  label: Hanbo Lin
creation_date: '2026-02-26T00:00:00Z'
description: NPASS is a natural products database that integrates species sources,
  chemical structures, biological targets, quantitative activity data, and ADME-toxicity
  information.
domains:
- drug discovery
homepage_url: https://bidd.group/NPASS/
id: npass
last_modified_date: '2026-05-20T00:00:00Z'
layout: resource_detail
name: NPASS
products:
- category: Product
  description: npass Nodes TSV
  format: tsv
  id: obo-db-ingest.npass.tsv
  license:
    id: https://creativecommons.org/licenses/by-nc/4.0/
    label: CC-BY-NC
  name: npass Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npass
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 2460413
  product_url: https://w3id.org/biopragmatics/resources/npass/npass.tsv
- category: GraphProduct
  description: The OREGANO knowledge graph dataset integrating drug, protein, gene,
    and disease information for drug repositioning.
  format: http
  id: oregano.graph
  name: OREGANO Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oregano
  product_url: https://gitub.u-bordeaux.fr/erias/oregano/-/tree/master/Data_OREGANO/Graphs
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cmaup
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: npass
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: bio2rdf
---
# NPASS

NPASS connects natural products to their species sources, biological targets, bioactivity measurements, and related ADME-tox data for biomedical and pharmacological research.