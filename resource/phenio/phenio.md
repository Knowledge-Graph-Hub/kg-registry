---
activity_status: active
category: Resource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jhc@lbl.gov
  - contact_type: github
    value: caufieldjh
  label: J. Harry Caufield
description: An ontology for accessing and comparing knowledge concerning phenotypes
  across species and genetic backgrounds.
domains:
- phenotype
homepage_url: https://monarch-initiative.github.io/phenio/
id: phenio
layout: resource_detail
license:
  id: https://opensource.org/license/bsd-3-clause
  label: BSD3
name: An integrated ontology for Phenomics
products:
- category: Product
  description: OWL version of phenio
  format: owl
  id: phenio.model
  license:
    id: https://opensource.org/license/bsd-3-clause
    label: BSD3
  name: phenio
  original_source:
  - phenio
  product_url: https://github.com/monarch-initiative/phenio/releases/latest/download/phenio.owl
  repository: https://github.com/monarch-initiative/phenio
  secondary_source:
  - phenio
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-06: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-07: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-12: HTTP 404 error
    when accessing file'
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.2.5
  description: PHENIO as a KGX graph
  format: kgx
  id: phenio.graph
  license:
    id: https://opensource.org/license/bsd-3-clause
    label: BSD3
  name: KG-Phenio
  original_source:
  - phenio
  product_file_size: 47081100
  product_url: https://kg-hub.berkeleybop.io/kg-phenio/20241203/kg-phenio.tar.gz
  repository: https://github.com/Knowledge-Graph-Hub/kg-phenio
  secondary_source:
  - phenio
repository: https://github.com/monarch-initiative/phenio
usages:
- description: PHENIO is used by the Monarch Initiative for cross-species inference.
    As an example, the disease of Parkinsonism may compared on the basis of its phenotype
    in humans vs. mouse genes and genotypes known to impact these phenotypes.
  id: cross-species-inference
  label: PHENIO is used by the Monarch Initiative for cross-species inference
  publications:
  - doi: doi:10.1093/nar/gkw1128
    id: doi:10.1093/nar/gkw1128
    preferred: true
    title: 'The Monarch Initiative: an integrative data and analytic platform connecting
      phenotypes to genotypes across species'
  type: actual
  url: https://monarchinitiative.org/HP:0001300#disease
  users:
  - category: Organization
    contact_details:
    - contact_type: url
      value: https://monarchinitiative.org/
    label: The Monarch Initiative
---
PHENIO