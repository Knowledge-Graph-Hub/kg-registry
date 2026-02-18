---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: pier.buttigieg@awi.de
  - contact_type: github
    value: pbuttigieg
  label: Pier Luigi Buttigieg
  orcid: 0000-0002-4366-3088
description: An ontology of environmental systems, components, and processes.
domains:
- environment
homepage_url: http://environmentontology.org/
id: envo
layout: resource_detail
license:
  id: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Environment Ontology
products:
- category: OntologyProduct
  description: main ENVO OWL release
  format: owl
  id: envo.owl
  name: main ENVO OWL release
  product_url: http://purl.obolibrary.org/obo/envo.owl
  warnings:
  - 'File was not able to be retrieved when checked on 2026-02-18: Timeout connecting
    to URL'
- category: OntologyProduct
  description: ENVO in obographs JSON format
  format: json
  id: envo.json
  name: ENVO in obographs JSON format
  product_file_size: 653600
  product_url: http://purl.obolibrary.org/obo/envo.json
- category: OntologyProduct
  description: ENVO in OBO Format. May be lossy
  format: obo
  id: envo.obo
  name: ENVO in OBO Format. May be lossy
  product_file_size: 595276
  product_url: http://purl.obolibrary.org/obo/envo.obo
- category: OntologyProduct
  description: OBO-Basic edition of ENVO
  format: obo
  id: envo.subsets.envo-basic.obo
  name: OBO-Basic edition of ENVO
  product_file_size: 422465
  product_url: http://purl.obolibrary.org/obo/envo/subsets/envo-basic.obo
- category: OntologyProduct
  description: Earth Microbiome Project subset
  format: owl
  id: envo.subsets.envoEmpo.owl
  name: Earth Microbiome Project subset
  product_file_size: 19016
  product_url: http://purl.obolibrary.org/obo/envo/subsets/envoEmpo.owl
- category: OntologyProduct
  description: GSC Lite subset of ENVO
  format: obo
  id: envo.subsets.EnvO-Lite-GSC.obo
  name: GSC Lite subset of ENVO
  product_file_size: 12912
  product_url: http://purl.obolibrary.org/obo/envo/subsets/EnvO-Lite-GSC.obo
- category: GraphProduct
  compression: targz
  description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
  format: kgx
  id: kg-microbe.graph.raw
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: KG-Microbe KGX Graph - Raw
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 12464495186
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-raw-20250222.tar.gz
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 4623010863
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-function-20250222.tar.gz
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 4640682152
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
  secondary_source:
  - kg-microbe
repository: https://github.com/EnvironmentOntology/envo
---
## Description

An ontology of environmental systems, components, and processes.

## Contacts

- Pier Luigi Buttigieg (pier.buttigieg@awi.de) [ORCID: 0000-0002-4366-3088](https://orcid.org/0000-0002-4366-3088)

## Products

### main ENVO OWL release

main ENVO OWL release

**URL**: [http://purl.obolibrary.org/obo/envo.owl](http://purl.obolibrary.org/obo/envo.owl)

**Format**: owl

### ENVO in obographs JSON format

ENVO in obographs JSON format

**URL**: [http://purl.obolibrary.org/obo/envo.json](http://purl.obolibrary.org/obo/envo.json)

**Format**: json

### ENVO in OBO Format. May be lossy

ENVO in OBO Format. May be lossy

**URL**: [http://purl.obolibrary.org/obo/envo.obo](http://purl.obolibrary.org/obo/envo.obo)

**Format**: obo

### OBO-Basic edition of ENVO

OBO-Basic edition of ENVO

**URL**: [http://purl.obolibrary.org/obo/envo/subsets/envo-basic.obo](http://purl.obolibrary.org/obo/envo/subsets/envo-basic.obo)

**Format**: obo

### Earth Microbiome Project subset

Earth Microbiome Project subset

**URL**: [http://purl.obolibrary.org/obo/envo/subsets/envoEmpo.owl](http://purl.obolibrary.org/obo/envo/subsets/envoEmpo.owl)

**Format**: owl

### GSC Lite subset of ENVO

GSC Lite subset of ENVO

**URL**: [http://purl.obolibrary.org/obo/envo/subsets/EnvO-Lite-GSC.obo](http://purl.obolibrary.org/obo/envo/subsets/EnvO-Lite-GSC.obo)

**Format**: obo

## Publications

- [The environment ontology: contextualising biological and biomedical entities](https://doi.org/10.1186/2041-1480-4-43)
- [The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation](https://doi.org/10.1186/s13326-016-0097-6)

**Domains**: environment

---

*This resource was automatically synchronized from the OBO Foundry registry.*