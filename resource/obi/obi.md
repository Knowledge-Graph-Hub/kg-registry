---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: bpeters@lji.org
  - contact_type: github
    value: bpeters42
  label: Bjoern Peters
  orcid: 0000-0002-8457-6693
creation_date: '2025-06-04T00:00:00Z'
description: An integrated ontology for the description of life-science and clinical
  investigations
domains:
- biomedical
- general
homepage_url: http://obi-ontology.org
id: obi
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Ontology for Biomedical Investigations
products:
- category: OntologyProduct
  description: The full version of OBI in OWL format
  format: owl
  id: obi.owl
  name: OBI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 723493
  product_url: http://purl.obolibrary.org/obo/obi.owl
- category: OntologyProduct
  description: The OBO-format version of OBI
  format: obo
  id: obi.obo
  name: OBI in OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 307971
  product_url: http://purl.obolibrary.org/obo/obi.obo
- category: OntologyProduct
  description: A collection of important high-level terms and their relations from
    OBI and other ontologies
  format: owl
  id: obi.obi_core.owl
  name: OBI Core
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 39447
  product_url: http://purl.obolibrary.org/obo/obi/obi_core.owl
- category: OntologyProduct
  description: Base module for OBI
  format: owl
  id: obi.obi-base.owl
  name: OBI Base module
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 617030
  product_url: http://purl.obolibrary.org/obo/obi/obi-base.owl
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: OntologyProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: cob
  - relation_type: prov:hadPrimarySource
    source: dc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: ma
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: oio
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semapv
  - relation_type: prov:hadPrimarySource
    source: skos
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: zfa
  product_file_size: 240665663
  product_url: https://www.ebi.ac.uk/efo/efo.owl
- category: OntologyProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: cob
  - relation_type: prov:hadPrimarySource
    source: dc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: ma
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: oio
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semapv
  - relation_type: prov:hadPrimarySource
    source: skos
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: zfa
  product_file_size: 64058275
  product_url: https://www.ebi.ac.uk/efo/efo.obo
- category: GraphProduct
  description: RDF dump of the Open Research Knowledge Graph distributed in N-Triples
    format.
  format: ntriples
  id: orkg.dump
  name: ORKG RDF Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orkg
  - relation_type: prov:hadPrimarySource
    source: wikidata
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 642902930
  product_url: https://orkg.org/files/rdf-dumps/rdf-export-orkg.nt
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Ontology for Biomedical Investigations (OBI),
    produced by KG-Bioportal from the BioPortal submission. The archive contains OBI_nodes.tsv
    and OBI_edges.tsv.
  edge_count: 16102
  format: kgx
  id: obi.kg-bioportal
  latest_version: '2026-05-08'
  name: OBI KGX graph (KG-Bioportal)
  node_count: 7552
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 578003
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/OBI.tar.gz
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
  description: Plant Gall Ontology in OWL format
  format: owl
  id: gallont.owl
  name: gallont.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gallont
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: flopo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: poro
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 91521
  product_url: http://purl.obolibrary.org/obo/gallont.owl
- category: OntologyProduct
  description: Plant Gall Ontology in OBO format
  format: obo
  id: gallont.obo
  name: gallont.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gallont
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: flopo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: poro
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 60631
  product_url: http://purl.obolibrary.org/obo/gallont.obo
- category: OntologyProduct
  description: Health Surveillance Ontology in OWL format
  format: owl
  id: hso.owl
  name: hso.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hso
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 138245
  product_url: http://purl.obolibrary.org/obo/hso.owl
- category: OntologyProduct
  description: clinical LABoratory Ontology in OWL format
  format: owl
  id: labo.owl
  name: labo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: labo
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: omiabis
  - relation_type: prov:hadPrimarySource
    source: omrse
  - relation_type: prov:hadPrimarySource
    source: opmi
  product_file_size: 47001
  product_url: http://purl.obolibrary.org/obo/labo.owl
- category: OntologyProduct
  description: Medical Action Ontology in OWL format
  format: owl
  id: maxo.owl
  name: maxo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 16448041
  product_url: http://purl.obolibrary.org/obo/maxo.owl
- category: OntologyProduct
  description: Medical Action Ontology in OBO format
  format: obo
  id: maxo.obo
  name: maxo.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 4180499
  product_url: http://purl.obolibrary.org/obo/maxo.obo
- category: OntologyProduct
  description: Medical Action Ontology in JSON format
  format: json
  id: maxo.json
  name: maxo.json
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 9856275
  product_url: http://purl.obolibrary.org/obo/maxo.json
- category: OntologyProduct
  description: Microbial Conditions Ontology in OWL format
  format: owl
  id: mco.owl
  name: mco.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mco
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: micro
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: omp
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: peco
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: zeco
  product_file_size: 772100
  product_url: http://purl.obolibrary.org/obo/mco.owl
- category: OntologyProduct
  description: Microbial Conditions Ontology in OBO format
  format: obo
  id: mco.obo
  name: mco.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mco
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: micro
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: omp
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: peco
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: zeco
  product_file_size: 409757
  product_url: http://purl.obolibrary.org/obo/mco.obo
- category: OntologyProduct
  description: Ontology for Nutritional Epidemiology in OWL format
  format: owl
  id: one.owl
  name: one.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: one
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ons
  product_file_size: 9258
  product_url: http://purl.obolibrary.org/obo/one.owl
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
  description: Process Chemistry Ontology in OWL format
  format: owl
  id: proco.owl
  name: proco.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proco
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cheminf
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: sbo
  product_file_size: 143615
  product_url: http://purl.obolibrary.org/obo/proco.owl
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
publications:
- authors:
  - Bandrowski A
  - Brinkman R
  - Brochhausen M
  - Brush MH
  - Bug B
  - Chibucos MC
  - Clancy K
  - Courtot M
  - Derom D
  - Dumontier M
  - Fan L
  - Fostel J
  - Fragoso G
  - Gibson F
  - Gonzalez-Beltran A
  - Haendel MA
  - He Y
  - Heiskanen M
  - Hernandez-Boussard T
  - Jensen M
  - Lin Y
  - Lister AL
  - Lord P
  - Malone J
  - Manduchi E
  - McGee M
  - Morrison N
  - Overton JA
  - Parkinson H
  - Peters B
  - Rocca-Serra P
  - Ruttenberg A
  - Sansone SA
  - Scheuermann RH
  - Schober D
  - Smith B
  - Soldatova LN
  - Stoeckert CJ Jr
  - Taylor CF
  - Torniai C
  - Turner JA
  - Vita R
  - Whetzel PL
  - Zheng J
  doi: 10.1371/journal.pone.0154556
  id: https://www.ncbi.nlm.nih.gov/pubmed/27128319
  journal: PLoS One
  title: The Ontology for Biomedical Investigations
  year: '2016'
repository: https://github.com/obi-ontology/obi
---
## Description

An integrated ontology for the description of life-science and clinical investigations

## Contacts

- Bjoern Peters (bpeters@lji.org) [ORCID: 0000-0002-8457-6693](https://orcid.org/0000-0002-8457-6693)

## Products

### OBI

The full version of OBI in OWL format

**URL**: [http://purl.obolibrary.org/obo/obi.owl](http://purl.obolibrary.org/obo/obi.owl)

**Format**: owl

### OBI in OBO

The OBO-format version of OBI

**URL**: [http://purl.obolibrary.org/obo/obi.obo](http://purl.obolibrary.org/obo/obi.obo)

**Format**: obo

### OBI Core

A collection of important high-level terms and their relations from OBI and other ontologies

**URL**: [http://purl.obolibrary.org/obo/obi/obi_core.owl](http://purl.obolibrary.org/obo/obi/obi_core.owl)

**Format**: owl

### OBI Base module

Base module for OBI

**URL**: [http://purl.obolibrary.org/obo/obi/obi-base.owl](http://purl.obolibrary.org/obo/obi/obi-base.owl)

**Format**: owl

## Publications

- [The Ontology for Biomedical Investigations](https://www.ncbi.nlm.nih.gov/pubmed/27128319)

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*