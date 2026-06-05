---
activity_status: active
category: DataSource
creation_date: '2026-05-29T00:00:00Z'
description: CMAUP is a database of collective molecular activities of useful plants,
  linking plant ingredients to targets, phenotypes, diseases, pathways, and traditional
  uses to support natural product and medicinal plant research.
domains:
- biomedical
- drug discovery
- pharmacology
- chemistry and biochemistry
id: cmaup
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: CMAUP
products:
- category: DocumentationProduct
  description: Nucleic Acids Research database article describing CMAUP, its data
    model, and its coverage of useful plants, ingredients, targets, pathways, and
    phenotypes.
  format: http
  id: cmaup.publication
  name: CMAUP Database Publication
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://academic.oup.com/nar/article/47/D1/D1118/5144144
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
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
publications:
- doi: doi:10.1093/nar/gky965
  id: https://doi.org/10.1093/nar/gky965
  journal: Nucleic Acids Research
  preferred: true
  title: 'CMAUP: a database of collective molecular activities of useful plants'
  year: '2019'
---
# CMAUP

CMAUP catalogs molecular activities associated with useful plants and their ingredients,
providing a literature-backed resource for connecting plant-derived compounds to
biological targets, pathways, diseases, and phenotypic effects.