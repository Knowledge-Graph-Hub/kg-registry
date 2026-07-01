---
activity_status: active
category: KnowledgeGraph
collection:
  - ber
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: marinka@hms.harvard.edu
      - contact_type: github
        value: marinkaz
    label: Marinka Zitnik
creation_date: '2025-03-09T00:00:00Z'
description: PrimeKG (Precision Medicine Knowledge Graph) integrates 20 high-quality biomedical resources to describe 17,080 diseases with over 4 million relationships across ten major biological scales.
domains:
  - biomedical
  - precision medicine
  - pathways
  - systems biology
homepage_url: https://zitniklab.hms.harvard.edu/projects/PrimeKG
id: primekg
infores_id: primekg
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: PrimeKG
products:
  - category: GraphProduct
    description: The full PrimeKG dataset containing disease relationships.
    format: csv
    id: primekg.graph
    name: PrimeKG Full Dataset
    original_source:
      - relation_type: prov:hadPrimarySource
        source: primekg
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: drugcentral
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: omim
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: umls
    product_url: https://dataverse.harvard.edu/api/access/datafile/6180620
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
      - File was not able to be retrieved when checked on 2026-02-04_ Timeout connecting to URL
repository: https://github.com/mims-harvard/PrimeKG
taxon:
  - NCBITaxon:9606
---

### PrimeKG: A Knowledge Graph for Precision Medicine

PrimeKG is a large-scale Precision Medicine Knowledge Graph that provides a holistic view of diseases by integrating 20 high-quality biomedical resources. It describes 17,080 diseases with over 4 million relationships, enabling advanced network medicine and machine learning applications.

## Evaluation

- View the evaluation: [primekg evaluation](primekg_eval.html)
