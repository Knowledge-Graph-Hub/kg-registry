---
activity_status: active
category: DataModel
description: A controlled vocabulary to describe phenotypic traits in plants. Each trait is a distinguishable feature, characteristic, quality or phenotypic feature of a developing or mature plant.
domains:
- agriculture
- biomedical
id: to
layout: resource_detail
name: Plant Trait Ontology
repository: https://github.com/Planteome/plant-trait-ontology
homepage_url: http://browser.planteome.org/amigo/term/TO:0000387
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
version: v2023-07-17
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jaiswalp@science.oregonstate.edu
  - contact_type: github
    value: jaiswalp
  label: Pankaj Jaiswal
  orcid: 0000-0002-1005-8383
publications:
- id: doi:10.1093/nar/gkx1152
  doi: 10.1093/nar/gkx1152
  preferred: true
  title: The Planteome database - an integrated resource for reference ontologies, plant genomics and phenomics
  year: 2018
  journal: Nucleic Acids Research
  authors:
  - Laurel Cooper
  - Austin Meier
  - Marie-Angélique Laporte
  - Justin L. Elser
  - Chris Mungall
  - Brandon T. Sinn
  - Dario Cavaliere
  - Seth Carbon
  - Nathan A. Dunn
  - Barry Smith
  - Botong Qu
  - Justin Preece
  - Eugene Zhang
  - Sinisa Todorovic
  - Georgios Gkoutos
  - John H. Doonan
  - Dennis W. Stevenson
  - Elizabeth Arnaud
  - Pankaj Jaiswal
usages:
- id: planteome.usage
  label: Planteome
  description: Planteome uses TO to describe traits for genes and germplasm
  url: http://planteome.org/
  type: actual
products:
- category: DataModelProduct
  description: The latest release of Plant Trait Ontology in OWL format
  format: owl
  id: to.owl
  name: Plant Trait Ontology OWL
  product_url: http://purl.obolibrary.org/obo/to.owl
  latest_version: v2025-05-20
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  original_source:
  - to
  - chebi
  - ro
  - ncbitaxon
  - go
  - omo
  - ecto
  - ido
  - oio
  - pato
  - envo
  - ohmi
  - iao
  - omrse
  - obi
  - peco
  - po
  - uberon
  - ogms
  - bfo
  secondary_source:
  - to
- category: DataModelProduct
  description: The latest release of Plant Trait Ontology in OBO format
  format: obo
  id: to.obo
  name: Plant Trait Ontology OBO
  product_url: http://purl.obolibrary.org/obo/to.obo
  latest_version: v2025-05-20
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  original_source:
  - to
  - chebi
  - ro
  - ncbitaxon
  - go
  - omo
  - ecto
  - ido
  - oio
  - pato
  - envo
  - ohmi
  - iao
  - omrse
  - obi
  - peco
  - po
  - uberon
  - ogms
  - bfo
  secondary_source:
  - to
- category: DataModelProduct
  description: The Basic subset of the Plant Trait Ontology in OBO format
  format: obo
  id: to-basic.obo
  name: Plant Trait Ontology Basic OBO
  product_url: http://purl.obolibrary.org/obo/to/subsets/to-basic.obo
  latest_version: v2025-05-20
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  original_source:
  - to
  - chebi
  - ro
  - ncbitaxon
  - go
  - omo
  - ecto
  - ido
  - oio
  - pato
  - envo
  - ohmi
  - iao
  - omrse
  - obi
  - peco
  - po
  - uberon
  - ogms
  - bfo
  secondary_source:
  - to
creation_date: 2025-07-10
last_modified_date: 2025-07-10
---
# Plant Trait Ontology (TO)

The Plant Trait Ontology (TO) is a controlled vocabulary to describe phenotypic traits in plants. Each trait is a distinguishable feature, characteristic, quality or phenotypic feature of a developing or mature plant.

## Overview

The Plant Trait Ontology is part of the [Planteome Project](http://planteome.org/), which provides a suite of reference ontologies for plants and annotations that link plant traits to ontology terms. This facilitates cross-species querying and analysis of plant traits, genomes, and genetic diversity data.

## Applications

The Plant Trait Ontology is used by various platforms:

- **[Planteome](http://planteome.org/)** uses TO to describe traits for genes and germplasm
- **[Gramene](http://gramene.org/)** uses PO for the annotation of plant genes and QTLs

## Resources

The ontology is maintained on GitHub at [https://github.com/Planteome/plant-trait-ontology](https://github.com/Planteome/plant-trait-ontology) and is available in both OWL and OBO formats through permanent URLs at purl.obolibrary.org.

## License

The Plant Trait Ontology is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), allowing for free use, redistribution, and adaptation with appropriate attribution.