---
activity_status: active
category: Ontology
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
creation_date: '2025-03-09T00:00:00Z'
description: Monochrom, also known as Chromo or CHR, is an automatic translation of
  UCSC chromosome bands to OWL classes. Each chromosome and chromosomal region is
  represented as an OWL class.
domains:
- chemistry and biochemistry
homepage_url: https://monarch-initiative.github.io/monochrom/
id: chr
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Monochrom Ontology
products:
- category: OntologyProduct
  description: OWL release of Monochrom Ontology
  format: owl
  id: chr.model.owl
  name: Monochrom Ontology OWL release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chr
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gff
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: skos
  product_file_size: 102365
  product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Monochrom (CHR), produced by KG-Bioportal from
    the BioPortal submission. The archive contains CHR_nodes.tsv and CHR_edges.tsv.
  edge_count: 5154
  format: kgx
  id: chr.kg-bioportal
  latest_version: '2025-10-15'
  name: CHR KGX graph (KG-Bioportal)
  node_count: 3115
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chr
  product_file_size: 118095
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/CHR.tar.gz
repository: https://github.com/monarch-initiative/monochrom/
---
Automatic translation of UCSC chromosome bands to OWL classes