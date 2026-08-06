---
activity_status: active
category: DataModel
collection:
- ber
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
description: 'MIxS, or the Minimum Information about any (X) Sequence is a standard
  for describing the contextual information about the sampling and sequencing of any
  genomic sequence. The standard has Terms that describe characteristics of a sample
  that addresses: What is the source of the sequence? In what kind of environment
  was the sample collected? What methods were utilized to process the sample?'
domains:
- environment
homepage_url: https://w3id.org/mixs
id: mixs
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: MIxS
products:
- category: DataModelProduct
  description: OWL release of mixs
  id: mixs.model
  name: MIxS OWL release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mixs
  product_file_size: 154279
  product_url: https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/refs/heads/main/project/owl/mixs.owl.ttl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Minimal Information about any Sequence Ontology
    (MIXS), produced by KG-Bioportal from the BioPortal submission. The archive contains
    MIXS_nodes.tsv and MIXS_edges.tsv.
  edge_count: 7242
  format: kgx
  id: mixs.kg-bioportal
  latest_version: 7.0.1
  name: MIXS KGX graph (KG-Bioportal)
  node_count: 2391
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mixs
  product_file_size: 215427
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.08.02-6/MIXS.tar.gz
repository: https://github.com/GenomicsStandardsConsortium/mixs
---
mixs