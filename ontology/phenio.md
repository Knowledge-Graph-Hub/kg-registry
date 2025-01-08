---
layout: ontology_detail
id: phenio
title: An integrated ontology for Phenomics
contact:
  email: jmcl@ebi.ac.uk
  github: jamesamcl
  label: James McLaughlin
  orcid: 0000-0002-8361-2795
description: An ontology for accessing and comparing knowledge concerning phenotypes across species and genetic backgrounds.
domain: phenotype
homepage: https://github.com/obophenotype/phenio
license:
  label: CC0 1.0
  url: https://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: PHENIO
uri_prefix: https://w3id.org/phenio/
products:
- id: phenio.owl
  description: OWL version of phenio
  ontology_purl: https://github.com/monarch-initiative/phenio/releases/latest/download/phenio.owl
  title: phenio
- id: phenio.kgx
  title: phenio KG
  description: KGX version of phenio
  ontology_purl: https://kg-hub.berkeleybop.io/kg-phenio/20241203/kg-phenio.tar.gz
  type: kgx
repository: https://github.com/monarch-initiative/phenio
tracker: https://github.com/monarch-initiative/phenio/issues
usages:
- description: phenio is used by the Monarch Initiative for cross-species inference.
  examples:
  - description: Characteristic neurologic anomaly resulting form degeneration of dopamine-generating cells in the substantia nigra, a region of the midbrain, characterized clinically by shaking, rigidity, slowness of movement and difficulty with walking and gait.
    url: https://monarchinitiative.org/phenotype/HP:0001300#disease
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/27899636
    title: 'The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species '
  type: analysis
  user: https://monarchinitiative.org/
activity_status: active
---
