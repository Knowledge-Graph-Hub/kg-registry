---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://geneorganizer.huji.ac.il/
  label: Gene ORGANizer - The Hebrew University of Jerusalem
creation_date: '2026-06-17T00:00:00Z'
description: Gene ORGANizer is a tool and database that links genes to the body parts
  and organs they affect. It contains curated associations between human genes and
  the anatomical components in which their phenotypes manifest, supporting analysis
  of the physiological effects of genes.
domains:
- genomics
- anatomy and development
homepage_url: https://geneorganizer.huji.ac.il/
id: geneorganizer
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: Gene ORGANizer
products:
- category: GraphicalInterface
  description: Web tool for exploring associations between genes and the organs and
    body parts they affect.
  format: http
  id: geneorganizer.site
  is_public: true
  name: Gene ORGANizer Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  product_url: https://geneorganizer.huji.ac.il/
publications:
- authors:
  - David Gokhman
  - Guy Kelman
  - Adir Amartely
  - Guy Gershon
  - Shira Tsur
  - Liran Carmel
  doi: 10.1093/nar/gkx302
  id: https://doi.org/10.1093/nar/gkx302
  journal: Nucleic Acids Research
  preferred: true
  title: 'Gene ORGANizer: linking genes to the organs they affect'
  year: '2017'
---
# Gene ORGANizer

Gene ORGANizer is a tool for linking human genes to the organs and body parts they affect.
It is built on a large set of curated gene-organ associations derived from gene-phenotype
data, and it enables users to analyze and visualize the anatomical distribution of the
effects of genes.

Content and features include:

- Curated associations between genes and roughly 150 body parts
- Tools to enrich and visualize the organs affected by a set of genes
- Support for both individual gene queries and gene-set analyses

GeneCards integrates gene-organ association information from Gene ORGANizer.
