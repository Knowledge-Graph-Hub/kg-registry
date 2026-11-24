---
activity_status: active
category: Resource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: emmaco
  label: Emma Cooke
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.elsevier.com/products/scibite/contact-us
  label: Elsevier (SciBite)
creation_date: '2025-03-10T00:00:00Z'
description: SciBite, part of Elsevier, provides ontology-driven semantic technology for scientific
  text, including ontology management, named entity recognition, data enrichment, and search.
  It also publishes a public OWL version of HGNC.
domains:
- biological systems
- literature
- natural language processing
homepage_url: https://www.elsevier.com/products/scibite
id: scibite
infores_id: scibite
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
name: SciBite
products:
- category: OntologyProduct
  compression: zip
  description: This HGNC OWL file is generated from the data at https://www.genenames.org/.
    It contains all genes in HGNC organised in a shallow hierarchy, classified by their locus
    type and gene group. Gene groups are also derived from HGNC. The ontology contains approved
    gene symbol, approved gene name, previous names and symbols and mappings to external databases.
  format: owl
  id: scibite.hgnc
  latest_version: '2026-11-02'
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: SciBite HGNC
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: scibite
  product_file_size: 8087124
  product_url: https://raw.githubusercontent.com/elsevier-health/scibite-ontology/main/hgnc_2026-11-02.owl.zip
  repository: https://github.com/elsevier-health/scibite-ontology
- category: Product
  description: Previous releases of the SciBite HGNC OWL file, as zip archives.
  format: http
  id: scibite.hgnc.archive
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: SciBite HGNC Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: scibite
  - relation_type: prov:hadPrimarySource
    source: hgnc
  product_url: https://github.com/elsevier-health/scibite-ontology/tree/main/archive
repository: https://github.com/elsevier-health/scibite-ontology
rrid: SCR_003952
---

# SciBite

SciBite is part of Elsevier (scibite.com now redirects to the Elsevier site). Its products for
semantic enrichment and ontology management are commercial. Its public data product is an OWL version
of HGNC, regenerated about every two months. File names carry the release date, so the link on this
page goes out of date when a new release moves the old file to the `archive` folder.
