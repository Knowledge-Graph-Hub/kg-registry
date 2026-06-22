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
creation_date: '2025-07-10T00:00:00Z'
description: An ontology of environmental systems, components, and processes.
domains:
- environment
homepage_url: http://environmentontology.org/
id: envo
last_modified_date: '2026-04-15T00:00:00Z'
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  product_file_size: 819909
  product_url: http://purl.obolibrary.org/obo/envo.owl
- category: OntologyProduct
  description: ENVO in obographs JSON format
  format: json
  id: envo.json
  name: ENVO in obographs JSON format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  product_file_size: 653600
  product_url: http://purl.obolibrary.org/obo/envo.json
- category: OntologyProduct
  description: ENVO in OBO Format. May be lossy
  format: obo
  id: envo.obo
  name: ENVO in OBO Format. May be lossy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  product_file_size: 595276
  product_url: http://purl.obolibrary.org/obo/envo.obo
- category: OntologyProduct
  description: OBO-Basic edition of ENVO
  format: obo
  id: envo.subsets.envo-basic.obo
  name: OBO-Basic edition of ENVO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  product_file_size: 422465
  product_url: http://purl.obolibrary.org/obo/envo/subsets/envo-basic.obo
- category: OntologyProduct
  description: Earth Microbiome Project subset
  format: owl
  id: envo.subsets.envoEmpo.owl
  name: Earth Microbiome Project subset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  product_file_size: 19016
  product_url: http://purl.obolibrary.org/obo/envo/subsets/envoEmpo.owl
- category: OntologyProduct
  description: GSC Lite subset of ENVO
  format: obo
  id: envo.subsets.EnvO-Lite-GSC.obo
  name: GSC Lite subset of ENVO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
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
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 4640682152
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
- category: GraphProduct
  description: RDF knowledge graph materialized by the MetaBoKG workflow from public
    metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence,
    sample metadata, and environmental and taxonomic context. The repository documents
    generated per-job Turtle files under mapping/kg and loading into Virtuoso named
    graphs.
  format: mixed
  id: metabokg.graph
  latest_version: arXiv v1 demonstration
  name: MetaboKG RDF Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: redu
  product_url: https://github.com/HolobiomicsLab/MetaBoKG
  secondary_source:
  - relation_type: prov:used
    source: ms
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
  - relation_type: prov:used
    source: envo
  - relation_type: prov:used
    source: ncit
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: chmo
  - relation_type: prov:used
    source: sio
  - relation_type: prov:used
    source: prov-o
  - relation_type: prov:used
    source: dcat
  - relation_type: prov:used
    source: afo
  warnings:
  - No static public graph release or hosted endpoint was available in the GitHub
    repository when curated on 2026-06-02; the repository documents local Turtle materialization
    and Virtuoso loading.
- category: DataModelProduct
  description: Turtle schema files defining MetaBoKG classes, properties, and ReDU
    class hierarchies used by the generated knowledge graph.
  format: ttl
  id: metabokg.schema
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache License 2.0
  name: MetaBoKG RDF Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  product_url: https://github.com/HolobiomicsLab/MetaBoKG/tree/main/Schema
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: ms
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: envo
  - relation_type: prov:wasInformedBy
    source: ncit
  - relation_type: prov:wasInformedBy
    source: uberon
  - relation_type: prov:wasInformedBy
    source: chmo
  - relation_type: prov:wasInformedBy
    source: sio
  - relation_type: prov:wasInformedBy
    source: prov-o
  - relation_type: prov:wasInformedBy
    source: dcat
  - relation_type: prov:wasInformedBy
    source: afo
publications:
- authors:
  - Pier Buttigieg
  - Norman Morrison
  - Barry Smith
  - Christopher J Mungall
  - Suzanna E Lewis
  doi: 10.1186/2041-1480-4-43
  id: https://doi.org/10.1186/2041-1480-4-43
  journal: Journal of Biomedical Semantics
  title: 'The environment ontology: contextualising biological and biomedical entities'
  year: '2013'
- authors:
  - Pier Luigi Buttigieg
  - Evangelos Pafilis
  - Suzanna E. Lewis
  - Mark P. Schildhauer
  - Ramona L. Walls
  - Christopher J. Mungall
  doi: 10.1186/s13326-016-0097-6
  id: https://doi.org/10.1186/s13326-016-0097-6
  journal: Journal of Biomedical Semantics
  title: 'The environment ontology in 2016: bridging domains with increased scope,
    semantic density, and interoperation'
  year: '2016'
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