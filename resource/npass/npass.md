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
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
name: NPASS
publications:
- authors:
  - Zhao H
  - Yang Y
  - Wang S
  - Yang X
  - Zhou K
  - Xu C
  - Zhang X
  - Fan J
  - Hou D
  - Li X
  - Lin H
  - Tan Y
  - Wang S
  - Chu XY
  - Zhuoma D
  - Zhang F
  - Ju D
  - Zeng X
  - Chen YZ
  doi: 10.1093/nar/gkac1069
  id: https://www.ncbi.nlm.nih.gov/pubmed/36624664
  journal: Nucleic Acids Res
  preferred: true
  title: 'NPASS database update 2023: quantitative natural product activity and species
    source database for biomedical research'
  year: '2023'
products:
- category: GraphicalInterface
  description: Official NPASS portal for searching and browsing natural products,
    source organisms, targets, activity records, and associated ADME-tox data.
  format: http
  id: npass.portal
  name: NPASS Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npass
  product_url: https://bidd.group/NPASS/
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

NPASS is the Natural Product Activity and Species Source Database maintained by
the BIDD group. It connects natural products with their species sources,
chemical structures, biological targets, experimentally derived quantitative
activity data, and associated ADME-toxicity information.

The owned portal product above is the canonical entry point for the live NPASS
database. The OBO-DB-Ingest and OREGANO products remain on this page as
propagated downstream derivatives that cite NPASS as an upstream source.