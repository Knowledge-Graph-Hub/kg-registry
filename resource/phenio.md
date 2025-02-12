---
layout: resource_detail
id: phenio
name: An integrated ontology for Phenomics
contacts:
- category: Individual
  email: jhc@lbl.gov
  github: caufieldjh
  label: J. Harry Caufield
description: An ontology for accessing and comparing knowledge concerning phenotypes across species and genetic backgrounds.
domain: phenotype
url: https://github.com/obophenotype/phenio
license:
  label: CC0 1.0
  id: https://creativecommons.org/publicdomain/zero/1.0/
products:
- id: phenio.owl
  description: OWL version of phenio
  url: https://github.com/monarch-initiative/phenio/releases/latest/download/phenio.owl
  name: phenio
  category: Product
- id: phenio.kgx
  name: phenio KG
  description: KGX version of phenio
  url: https://kg-hub.berkeleybop.io/kg-phenio/20241203/kg-phenio.tar.gz
  is_kgx: true
  category: GraphProduct
repository: https://github.com/monarch-initiative/phenio
usages:
- id: cross-species-inference
  label: PHENIO is used by the Monarch Initiative for cross-species inference
  description: PHENIO is used by the Monarch Initiative for cross-species inference. As an example, the disease of Parkinsonism may compared on the basis of its phenotype in humans vs. mouse genes and genotypes known to impact these phenotypes.
  url: https://monarchinitiative.org/HP:0001300#disease
  users:
  - category: Organization
    label: The Monarch Initiative
    url: https://monarchinitiative.org/
  publications:
  - preferred: true
    title: "The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species"
    doi: doi:10.1093/nar/gkw1128
    id: doi:10.1093/nar/gkw1128
  type: actual
activity_status: active
category: Resource
---

PHENIO
