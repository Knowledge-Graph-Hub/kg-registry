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
description: Monochrom, also known as Chromo or CHR, is an automatic translation of UCSC chromosome bands to OWL classes. Each chromosome and chromosomal region is represented as an OWL class.
domains:
  - chemistry and biochemistry
homepage_url: https://monarch-initiative.github.io/monochrom/
id: chr
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
      - source: chr
        relation_type: prov:hadPrimarySource
      - source: geno
        relation_type: prov:hadPrimarySource
      - source: gff
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: skos
        relation_type: prov:hadPrimarySource
    product_file_size: 102365
    product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
  - id: chr.kg-bioportal
    name: CHR KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of Monochrom (CHR), produced by KG-Bioportal from the BioPortal submission. The archive contains CHR_nodes.tsv and CHR_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/CHR.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: chr
        relation_type: prov:hadPrimarySource
    node_count: 3115
    edge_count: 5154
    latest_version: '2025-10-15'
repository: https://github.com/monarch-initiative/monochrom/
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-08-06T00:00:00Z'
---

Automatic translation of UCSC chromosome bands to OWL classes
