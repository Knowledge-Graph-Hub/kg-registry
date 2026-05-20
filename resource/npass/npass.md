---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: NPASS is a natural products database that integrates species sources, chemical structures, biological targets, quantitative activity data, and ADME-toxicity information.
domains:
  - drug discovery
homepage_url: https://bidd.group/NPASS/
id: npass
last_modified_date: '2026-05-20T00:00:00Z'
layout: resource_detail
name: NPASS
contacts:
  - category: Individual
    label: Hanbo Lin
    contact_details:
      - contact_type: email
        value: hblin23@m.fudan.edu.cn
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
---

# NPASS

NPASS connects natural products to their species sources, biological targets, bioactivity measurements, and related ADME-tox data for biomedical and pharmacological research.
