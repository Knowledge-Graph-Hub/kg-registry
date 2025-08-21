---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: joncison
  label: Jon Ison
- category: Individual
  contact_details:
  - contact_type: github
    value: matuskalas
  label: Matúš Kalaš
- category: Individual
  contact_details:
  - contact_type: github
    value: hmenager
  label: Hervé Ménager
description: EDAM is an ontology of bioscientific data analysis and data management, covering
  topics, operations, data, identifiers, and formats. It supports semantic annotation of tools,
  workflows, training, and provenance metadata across life sciences.
domains:
- information technology
- biological systems
homepage_url: https://edamontology.org/
id: edam
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: EDAM Ontology
products:
- category: DataModelProduct
  description: EDAM OWL release
  format: owl
  id: edam.owl
  name: EDAM OWL
  original_source:
  - edam
  - dc
  - skos
  product_url: http://edamontology.org/EDAM.owl
  secondary_source:
  - edam
- category: DataModelProduct
  description: EDAM TSV export
  format: tsv
  id: edam.tsv
  name: EDAM TSV
  original_source:
  - edam
  - dc
  - skos
  product_url: https://edamontology.org/EDAM.tsv
  secondary_source:
  - edam
- category: DataModelProduct
  description: EDAM CSV export
  format: csv
  id: edam.csv
  name: EDAM CSV
  original_source:
  - edam
  - dc
  - skos
  product_url: https://edamontology.org/EDAM.csv
  secondary_source:
  - edam
publications:
- authors:
  - Ison J
  - Kalaš M
  - Jonassen I
  - Bolser D
  - Uludag M
  - et al.
  doi: 10.1093/bioinformatics/btt113
  id: doi:10.1093/bioinformatics/btt113
  journal: Bioinformatics
  preferred: true
  title: 'EDAM: an ontology of bioinformatics operations, types of data and identifiers, topics and formats'
  year: '2013'
repository: https://github.com/edamontology/edamontology
---

EDAM provides a simple, four-branch structure (Topic, Operation, Data, Format) to organise
concepts prevalent in computational biology and bioinformatics, enabling consistent
annotation and discovery of resources.