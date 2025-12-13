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
description: PrimeKG (Precision Medicine Knowledge Graph) integrates 20 high-quality
  biomedical resources to describe 17,080 diseases with over 4 million relationships
  across ten major biological scales.
domains:
- health
- precision medicine
- biomedical
- pathways
- systems biology
homepage_url: https://zitniklab.hms.harvard.edu/projects/PrimeKG
id: primekg
infores_id: primekg
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: PrimeKG
products:
- category: GraphProduct
  description: The full PrimeKG dataset containing disease relationships.
  id: primekg.graph
  name: PrimeKG Full Dataset
  original_source:
  - primekg
  product_url: https://dataverse.harvard.edu/api/access/datafile/6180620
  secondary_source:
  - primekg
  warnings:
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-13: HTTP 403 error
    when accessing file'
repository: https://github.com/mims-harvard/PrimeKG
---
### PrimeKG: A Knowledge Graph for Precision Medicine

PrimeKG is a large-scale Precision Medicine Knowledge Graph that provides a holistic view of diseases by integrating 20 high-quality biomedical resources. It describes 17,080 diseases with over 4 million relationships, enabling advanced network medicine and machine learning applications.

## Evaluation

- View the evaluation: [primekg evaluation](primekg_eval.html)