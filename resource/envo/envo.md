---
activity_status: active
category: Ontology
collection:
- obo-foundry
- ber
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
last_modified_date: '2026-10-10T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
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
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
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
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
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
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
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
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
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
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
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
    source: pmc
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
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Environment Ontology (ENVO), produced by KG-Bioportal
    from the BioPortal submission. The archive contains ENVO_nodes.tsv and ENVO_edges.tsv.
  edge_count: 15406
  format: kgx
  id: envo.kg-bioportal
  latest_version: '2026-06-26'
  name: ENVO KGX graph (KG-Bioportal)
  node_count: 8323
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envo
  product_file_size: 542367
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/ENVO.tar.gz
- category: OntologyProduct
  description: Current OWL release of ECSO (ECSO8.owl, version 0.10.0) in the DataONE
    sem-prov-ontologies repository, with merged imports of ENVO, PATO, CHEBI, RO,
    IAO and BFO terms
  format: owl
  id: ecso.owl
  name: ECSO OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecso
  product_file_size: 2310496
  product_url: https://raw.githubusercontent.com/DataONEorg/sem-prov-ontologies/main/ecso/ECSO8.owl
  secondary_source:
  - relation_type: prov:used
    source: oboe
  - relation_type: prov:used
    source: envo
  - relation_type: prov:used
    source: pato
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ro
  - relation_type: prov:used
    source: iao
  - relation_type: prov:used
    source: bfo
- category: OntologyProduct
  description: Full EnvThes SKOS thesaurus in Turtle, generated from the source spreadsheet
    by the sheet2rdf workflow in the EnvThes GitHub repository.
  format: ttl
  id: envthes.ttl
  name: EnvThes Turtle
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envthes
  - relation_type: prov:wasInfluencedBy
    source: envo
  product_file_size: 3138937
  product_url: https://raw.githubusercontent.com/LTER-Europe/EnvThes/main/EnvThes.ttl
  repository: https://github.com/LTER-Europe/EnvThes
- category: OntologyProduct
  description: Contains all AgrO terms and links to other relevant ontologies.
  format: owl
  id: agro.owl
  name: AgrO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agro
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: peco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: xco
  product_file_size: 463598
  product_url: http://purl.obolibrary.org/obo/agro.owl
- category: OntologyProduct
  description: Compositional Dietary Nutrition Ontology in OWL format
  format: owl
  id: cdno.owl
  name: cdno.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdno
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 590900
  product_url: http://purl.obolibrary.org/obo/cdno.owl
- category: OntologyProduct
  description: Compositional Dietary Nutrition Ontology in OBO format
  format: obo
  id: cdno.obo
  name: cdno.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdno
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 331277
  product_url: http://purl.obolibrary.org/obo/cdno.obo
- category: OntologyProduct
  description: An ontology of core ecological entities in OWL format
  format: owl
  id: ecocore.owl
  name: ecocore.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocore
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1287569
  product_url: http://purl.obolibrary.org/obo/ecocore.owl
- category: OntologyProduct
  description: An ontology of core ecological entities in OBO format
  format: obo
  id: ecocore.obo
  name: ecocore.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocore
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 834439
  product_url: http://purl.obolibrary.org/obo/ecocore.obo
- category: OntologyProduct
  description: Environmental conditions, treatments and exposures ontology in OWL
    format
  format: owl
  id: ecto.owl
  name: ecto.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: xco
  product_file_size: 2277332
  product_url: http://purl.obolibrary.org/obo/ecto.owl
- category: OntologyProduct
  description: Environmental conditions, treatments and exposures ontology in OBO
    format
  format: obo
  id: ecto.obo
  name: ecto.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: xco
  product_file_size: 1509031
  product_url: http://purl.obolibrary.org/obo/ecto.obo
- category: OntologyProduct
  description: Environmental conditions, treatments and exposures ontology in JSON
    format
  format: json
  id: ecto.json
  name: ecto.json
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: xco
  product_file_size: 1646990
  product_url: http://purl.obolibrary.org/obo/ecto.json
- category: OntologyProduct
  description: FoodOn ontology with import file references and over 9,000 food products
  format: owl
  id: foodon.owl
  name: FoodOn ontology with import file references and over 9,000 food products
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: eo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 2852449
  product_url: http://purl.obolibrary.org/obo/foodon.owl
- category: OntologyProduct
  description: ONS latest release
  format: owl
  id: ons.owl
  name: ONS latest release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ons
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 215578
  product_url: http://purl.obolibrary.org/obo/ons.owl
- category: OntologyProduct
  description: Population and Community Ontology in OWL format
  format: owl
  id: pco.owl
  name: pco.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 62282
  product_url: http://purl.obolibrary.org/obo/pco.owl
- category: OntologyProduct
  description: Radiation Biology Ontology in OWL format
  format: owl
  id: rbo.owl
  name: rbo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rbo
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chmo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uo
  product_file_size: 1902434
  product_url: http://purl.obolibrary.org/obo/rbo.owl
- category: OntologyProduct
  description: Radiation Biology Ontology in OBO format
  format: obo
  id: rbo.obo
  name: rbo.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rbo
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chmo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uo
  product_file_size: 486142
  product_url: http://purl.obolibrary.org/obo/rbo.obo
- category: OntologyProduct
  description: Sickle Cell Disease Ontology in OWL format
  format: owl
  id: scdo.owl
  name: scdo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: scdo
  - relation_type: prov:hadPrimarySource
    source: apollo_sv
  - relation_type: prov:hadPrimarySource
    source: aro
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chmo
  - relation_type: prov:hadPrimarySource
    source: cmo
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dron
  - relation_type: prov:hadPrimarySource
    source: duo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: eupath
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: gsso
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: ico
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: idomal
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: opmi
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: symp
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: vt
  product_file_size: 367519
  product_url: http://purl.obolibrary.org/obo/scdo.owl
- category: OntologyProduct
  description: Sickle Cell Disease Ontology in OBO format
  format: obo
  id: scdo.obo
  name: scdo.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: scdo
  - relation_type: prov:hadPrimarySource
    source: apollo_sv
  - relation_type: prov:hadPrimarySource
    source: aro
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chmo
  - relation_type: prov:hadPrimarySource
    source: cmo
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dron
  - relation_type: prov:hadPrimarySource
    source: duo
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: eupath
  - relation_type: prov:hadPrimarySource
    source: exo
  - relation_type: prov:hadPrimarySource
    source: gaz
  - relation_type: prov:hadPrimarySource
    source: gsso
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: ico
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: idomal
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: opmi
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: symp
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: vt
  product_file_size: 324416
  product_url: http://purl.obolibrary.org/obo/scdo.obo
- category: OntologyProduct
  description: core ontology
  format: owl
  id: uberon.owl
  name: Uberon
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 98551256
  product_url: http://purl.obolibrary.org/obo/uberon.owl
- category: OntologyProduct
  description: Uberon edition that excludes external ontologies and most relations
  format: obo
  id: uberon.uberon-basic.obo
  name: Uberon basic
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 12146722
  product_url: http://purl.obolibrary.org/obo/uberon/uberon-basic.obo
- category: OntologyProduct
  description: Uberon plus all metazoan ontologies
  format: owl
  id: uberon.collected-metazoan.owl
  name: Uberon collected metazoan ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 284938816
  product_url: http://purl.obolibrary.org/obo/uberon/collected-metazoan.owl
- category: OntologyProduct
  description: Uberon and all metazoan ontologies with redundant species-specific
    terms removed
  format: owl
  id: uberon.composite-metazoan.owl
  name: Uberon composite metazoan ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 259794621
  product_url: http://purl.obolibrary.org/obo/uberon/composite-metazoan.owl
- category: OntologyProduct
  description: Uberon composite vertebrate ontology
  format: owl
  id: uberon.composite-vertebrate.owl
  name: Uberon composite vertebrate ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 126856799
  product_url: http://purl.obolibrary.org/obo/uberon/composite-vertebrate.owl
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