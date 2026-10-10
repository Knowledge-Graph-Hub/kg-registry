---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
  label: Chris Mungall
  orcid: 0000-0002-6601-2165
creation_date: '2025-06-25T00:00:00Z'
description: Relationship types shared across multiple ontologies
domains:
- biological systems
- general
homepage_url: https://oborel.github.io/
id: ro
infores_id: ro
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Relation Ontology
products:
- category: OntologyProduct
  description: Canonical edition
  format: owl
  id: ro.owl
  name: Relation Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 132025
  product_url: http://purl.obolibrary.org/obo/ro.owl
- category: OntologyProduct
  description: The obo edition is less expressive than the OWL, and has imports merged
    in
  format: obo
  id: ro.obo
  name: Relation Ontology in obo format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 84333
  product_url: http://purl.obolibrary.org/obo/ro.obo
- category: OntologyProduct
  description: Relation Ontology in obojson format
  format: json
  id: ro.json
  name: Relation Ontology in obojson format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 114142
  product_url: http://purl.obolibrary.org/obo/ro.json
- category: OntologyProduct
  description: Minimal subset intended to work with BFO-classes
  format: owl
  id: ro.core.owl
  name: RO Core relations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 7819
  product_url: http://purl.obolibrary.org/obo/ro/core.owl
- category: OntologyProduct
  description: Axioms defined within RO and to be used in imports for other ontologies
  format: owl
  id: ro.ro-base.owl
  name: RO base ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 97499
  product_url: http://purl.obolibrary.org/obo/ro/ro-base.owl
- category: OntologyProduct
  description: For use in ecology and environmental science
  format: owl
  id: ro.subsets.ro-interaction.owl
  name: Interaction relations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 64252
  product_url: http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl
- category: OntologyProduct
  description: For use in neuroscience
  format: owl
  id: ro.subsets.ro-neuro.owl
  name: Neuroscience subset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 5164
  product_url: http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: genemania
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vo
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
- category: OntologyProduct
  description: OWL release of Monochrom Ontology
  format: owl
  id: chr.model.owl
  name: Monochrom Ontology OWL release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chr
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gff
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: skos
  product_file_size: 102365
  product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
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
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, Turtle format
  format: ttl
  id: hra-kg.graph.ttl
  name: HRA KG graph data, v2.2, Turtle format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 204030087
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.ttl
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, JSON-LD format
  format: jsonld
  id: hra-kg.graph.json
  name: HRA KG graph data, v2.2, JSON-LD format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 18043
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.json
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, RDF/XML format
  format: rdfxml
  id: hra-kg.graph.xml
  name: HRA KG graph data, v2.2, RDF/XML format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 185060502
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.xml
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, N-Triples format
  format: ntriples
  id: hra-kg.graph.nt
  name: HRA KG graph data, v2.2, N-Triples format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 291382102
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.nt
- category: GraphProduct
  description: The graph representation of the Human Reference Atlas (HRA) dataset,
    v2.2, N-Quads format
  format: nquads
  id: hra-kg.graph.nq
  name: HRA KG graph data, v2.2, N-Quads format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hra-kg
  - relation_type: prov:hadPrimarySource
    source: ccf
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hravs
  - relation_type: prov:hadPrimarySource
    source: lmha
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vccf
  product_file_size: 376981902
  product_url: https://cdn.humanatlas.io/digital-objects/collection/hra/v2.2/graph.nq
- category: GraphProduct
  description: Merged KG with ontology-grounded KG and literature-based graph as TSV
    file
  format: tsv
  id: np-kg.graph.tsv
  name: NP-KG TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: np-kg
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: dideo
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: indra
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: oae
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semrep
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1074149258
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.tsv?download=1
- category: GraphProduct
  description: Merged KG with ontology-grounded KG and literature-based graph as NetworkX
    multidigraph object
  dump_format: gpickle
  format: mixed
  id: np-kg.graph.networkx
  name: NP-KG gpickle
  original_source:
  - relation_type: prov:hadPrimarySource
    source: np-kg
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: dideo
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: indra
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: oae
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semrep
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 936065236
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.gpickle?download=1
- category: GraphProduct
  description: KGX distribution of the SRI-Reference KG
  format: kgx
  id: sri-reference-kg.graph
  name: SRI-Reference KG (KGX distribution)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sri-reference-kg
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: wormbase
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ddanat
  - relation_type: prov:hadPrimarySource
    source: ddpheno
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dpo
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: fypo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: wbbt
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: wbphenotype
  - relation_type: prov:hadPrimarySource
    source: xao
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: zfa
  - relation_type: prov:hadPrimarySource
    source: zfs
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: decipher
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  - relation_type: prov:hadPrimarySource
    source: cureid
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_file_size: 230046094
  product_url: https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.tar.gz
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Relations Ontology (OBOREL), produced by KG-Bioportal
    from the BioPortal submission. The archive contains OBOREL_nodes.tsv and OBOREL_edges.tsv.
  edge_count: 2787
  format: kgx
  id: ro.kg-bioportal
  latest_version: '2025-12-17'
  name: OBOREL KGX graph (KG-Bioportal)
  node_count: 1234
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 62349
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/OBOREL.tar.gz
- category: ProcessProduct
  description: Build system for Brain_Cell_KG. A Docker Compose OBASK pipeline fetches
    the source OWL/RDF files listed in config/collectdata, loads them into an RDF4J
    triplestore and builds a Neo4j knowledge graph; Makefile targets generate ROBOT
    templates, OWL mapping files and Cypher-based CSV reports. No prebuilt graph dump
    or public Neo4j instance is released.
  format: http
  id: brain-cell-kg.repository
  name: Brain_Cell_KG repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: brain-cell-kg
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ro
  product_url: https://github.com/Cellular-Semantics/Brain_Cell_KG
  repository: https://github.com/Cellular-Semantics/Brain_Cell_KG
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
  description: Ontology for the Anatomy of the Insect SkeletoMuscular system (AISM)
    in OWL format
  format: owl
  id: aism.owl
  name: aism.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1378303
  product_url: http://purl.obolibrary.org/obo/aism.owl
- category: OntologyProduct
  description: Ontology for the Anatomy of the Insect SkeletoMuscular system (AISM)
    in OBO format
  format: obo
  id: aism.obo
  name: aism.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 896550
  product_url: http://purl.obolibrary.org/obo/aism.obo
- category: OntologyProduct
  description: Ontology for the Anatomy of the Insect SkeletoMuscular system (AISM)
    in JSON format
  format: json
  id: aism.json
  name: aism.json
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 929390
  product_url: http://purl.obolibrary.org/obo/aism.json
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
  description: Complete ontology, plus inter-ontology axioms, and imports modules
  format: owl
  id: cl.owl
  name: Main CL OWL edition
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: go
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
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 65879178
  product_url: http://purl.obolibrary.org/obo/cl.owl
- category: OntologyProduct
  description: Complete ontology, plus inter-ontology axioms, and imports modules
    merged in
  format: obo
  id: cl.obo
  name: CL obo format edition
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: go
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
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 17326417
  product_url: http://purl.obolibrary.org/obo/cl.obo
- category: OntologyProduct
  description: Complete ontology, plus inter-ontology axioms, and imports modules
    merged in
  format: json
  id: cl.json
  name: CL OBOGraph-JSON format edition
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: go
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
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 39845315
  product_url: http://purl.obolibrary.org/obo/cl.json
- category: OntologyProduct
  description: Basic version, no inter-ontology axioms
  format: owl
  id: cl.cl-basic.owl
  name: Basic CL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: go
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
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 9533929
  product_url: http://purl.obolibrary.org/obo/cl/cl-basic.owl
- category: OntologyProduct
  description: Basic version, no inter-ontology axioms
  format: obo
  id: cl.cl-basic.obo
  name: Basic CL (OBO version)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: go
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
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 3346117
  product_url: http://purl.obolibrary.org/obo/cl/cl-basic.obo
- category: OntologyProduct
  description: Basic version, no inter-ontology axioms
  format: json
  id: cl.cl-basic.json
  name: Basic CL (OBOGraph-JSON version)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: go
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
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 6060633
  product_url: http://purl.obolibrary.org/obo/cl/cl-basic.json
- category: OntologyProduct
  description: Collembola Anatomy Ontology in OWL format
  format: owl
  id: clao.owl
  name: clao.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clao
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 112550
  product_url: http://purl.obolibrary.org/obo/clao.owl
- category: OntologyProduct
  description: Collembola Anatomy Ontology in OBO format
  format: obo
  id: clao.obo
  name: clao.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clao
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 74344
  product_url: http://purl.obolibrary.org/obo/clao.obo
- category: OntologyProduct
  description: Clytia hemisphaerica Development and Anatomy Ontology in OWL format
  format: owl
  id: clyh.owl
  name: clyh.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clyh
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 13404
  product_url: http://purl.obolibrary.org/obo/clyh.owl
- category: OntologyProduct
  description: Clytia hemisphaerica Development and Anatomy Ontology in OBO format
  format: obo
  id: clyh.obo
  name: clyh.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clyh
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 9651
  product_url: http://purl.obolibrary.org/obo/clyh.obo
- category: OntologyProduct
  description: Coleoptera Anatomy Ontology (COLAO) in OWL format
  format: owl
  id: colao.owl
  name: colao.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: colao
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 164547
  product_url: http://purl.obolibrary.org/obo/colao.owl
- category: OntologyProduct
  description: Coleoptera Anatomy Ontology (COLAO) in OBO format
  format: obo
  id: colao.obo
  name: colao.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: colao
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 83585
  product_url: http://purl.obolibrary.org/obo/colao.obo
- category: OntologyProduct
  description: Ctenophore Ontology in OWL format
  format: owl
  id: cteno.owl
  name: cteno.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cteno
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 15458
  product_url: http://purl.obolibrary.org/obo/cteno.owl
- category: OntologyProduct
  description: The Echinoderm Anatomy and Development Ontology in OWL format
  format: owl
  id: ecao.owl
  name: ecao.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecao
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1546949
  product_url: http://purl.obolibrary.org/obo/ecao.owl
- category: OntologyProduct
  description: The Echinoderm Anatomy and Development Ontology in OBO format
  format: obo
  id: ecao.obo
  name: ecao.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecao
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1002010
  product_url: http://purl.obolibrary.org/obo/ecao.obo
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
- category: OntologyProduct
  description: Biological Imaging Methods Ontology in OWL format
  format: owl
  id: fbbi.owl
  name: fbbi.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fbbi
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 701623
  product_url: http://purl.obolibrary.org/obo/fbbi.owl
- category: OntologyProduct
  description: Biological Imaging Methods Ontology in OBO format
  format: obo
  id: fbbi.obo
  name: fbbi.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fbbi
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 195618
  product_url: http://purl.obolibrary.org/obo/fbbi.obo
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
  description: FuTRES Ontology of Vertebrate Traits in OWL format
  format: owl
  id: fovt.owl
  name: fovt.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fovt
  - relation_type: prov:hadPrimarySource
    source: bco
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 2587818
  product_url: http://purl.obolibrary.org/obo/fovt.owl
- category: OntologyProduct
  description: FuTRES Ontology of Vertebrate Traits in OBO format
  format: obo
  id: fovt.obo
  name: fovt.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fovt
  - relation_type: prov:hadPrimarySource
    source: bco
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1628339
  product_url: http://purl.obolibrary.org/obo/fovt.obo
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
  description: Genomic Epidemiology Ontology in OWL format
  format: owl
  id: genepio.owl
  name: genepio.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genepio
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 732830
  product_url: http://purl.obolibrary.org/obo/genepio.owl
- category: OntologyProduct
  description: The main ontology in OWL. This is self contained and does not have
    connections to other OBO ontologies
  format: owl
  id: go.owl
  name: GO (OWL edition)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 129706298
  product_url: http://purl.obolibrary.org/obo/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, in obo format
  format: obo
  id: go.obo
  name: GO (OBO Format edition)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 36555702
  product_url: http://purl.obolibrary.org/obo/go.obo
- category: OntologyProduct
  description: Equivalent to go.owl, in obograph json format
  format: json
  id: go.json
  name: GO (JSON edition)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_url: http://purl.obolibrary.org/obo/go.json
  warnings: []
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    with subsets of those ontologies
  format: owl
  id: go.extensions.go-plus.owl
  name: GO-Plus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 236488701
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.owl
- category: OntologyProduct
  description: As go-plus.owl, in obographs json format
  format: json
  id: go.extensions.go-plus.json
  name: GO-Plus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.json
  warnings: []
- category: OntologyProduct
  description: Basic version of the GO, filtered such that the graph is guaranteed
    to be acyclic and annotations can be propagated up the graph. The relations included
    are is a, part of, regulates, negatively regulates and positively regulates. This
    version excludes relationships that cross the 3 GO hierarchies.
  format: obo
  id: go.go-basic.obo
  name: GO-Basic, Filtered, for use with legacy tools
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 32126692
  product_url: http://purl.obolibrary.org/obo/go/go-basic.obo
- category: OntologyProduct
  description: As go-basic.obo, in json format
  format: json
  id: go.go-basic.json
  name: GO-Basic, Filtered, for use with legacy tools (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_url: http://purl.obolibrary.org/obo/go/go-basic.json
  warnings: []
- category: OntologyProduct
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: owl
  id: go.snapshot.go.owl
  name: GO (OWL edition), daily snapshot release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 129908636
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: obo
  id: go.snapshot.go.obo
  name: GO (OBO Format edition), daily snapshot release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 36684860
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.obo
- category: OntologyProduct
  description: Classes added to ncbitaxon for groupings such as prokaryotes
  format: owl
  id: go.extensions.go-taxon-groupings.owl
  name: GO Taxon Groupings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl
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
  description: Lepidoptera Anatomy Ontology in OWL format
  format: owl
  id: lepao.owl
  name: lepao.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lepao
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 141799
  product_url: http://purl.obolibrary.org/obo/lepao.owl
- category: OntologyProduct
  description: Lepidoptera Anatomy Ontology in OBO format
  format: obo
  id: lepao.obo
  name: lepao.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lepao
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 74809
  product_url: http://purl.obolibrary.org/obo/lepao.obo
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
  description: The main ontology in OWL
  format: owl
  id: ontoavida.owl
  name: OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ontoavida
  - relation_type: prov:hadPrimarySource
    source: fbcv
  - relation_type: prov:hadPrimarySource
    source: gsso
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: stato
  product_file_size: 472853
  product_url: http://purl.obolibrary.org/obo/ontoavida.owl
- category: OntologyProduct
  description: Equivalent to ontoavida.owl, in obo format
  format: obo
  id: ontoavida.obo
  name: OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ontoavida
  - relation_type: prov:hadPrimarySource
    source: fbcv
  - relation_type: prov:hadPrimarySource
    source: gsso
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: stato
  product_file_size: 240082
  product_url: http://purl.obolibrary.org/obo/ontoavida.obo
- category: OntologyProduct
  description: Provisional Cell Ontology in OWL format
  format: owl
  id: pcl.owl
  name: pcl.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
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
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 167561057
  product_url: http://purl.obolibrary.org/obo/pcl.owl
- category: OntologyProduct
  description: Provisional Cell Ontology in OBO format
  format: obo
  id: pcl.obo
  name: pcl.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pcl
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
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
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 39796128
  product_url: http://purl.obolibrary.org/obo/pcl.obo
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
  description: planaria-ontology in OWL format
  format: owl
  id: plana.owl
  name: plana.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: plana
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 178099
  product_url: http://purl.obolibrary.org/obo/plana.owl
- category: OntologyProduct
  description: planaria-ontology in OBO format
  format: obo
  id: plana.obo
  name: plana.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: plana
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 120490
  product_url: http://purl.obolibrary.org/obo/plana.obo
- category: OntologyProduct
  description: Planarian Phenotype Ontology in OWL format
  format: owl
  id: planp.owl
  name: planp.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: planp
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: plana
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 535526
  product_url: http://purl.obolibrary.org/obo/planp.owl
- category: OntologyProduct
  description: Planarian Phenotype Ontology in OBO format
  format: obo
  id: planp.obo
  name: planp.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: planp
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: plana
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 339560
  product_url: http://purl.obolibrary.org/obo/planp.obo
- category: OntologyProduct
  description: Porifera Ontology in OWL format
  format: owl
  id: poro.owl
  name: poro.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: poro
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 62597
  product_url: http://purl.obolibrary.org/obo/poro.owl
- category: OntologyProduct
  description: Porifera Ontology in OBO format
  format: obo
  id: poro.obo
  name: poro.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: poro
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 54580
  product_url: http://purl.obolibrary.org/obo/poro.obo
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
  description: Performance Summary Display Ontology in OWL format
  format: owl
  id: psdo.owl
  name: psdo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: psdo
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: stato
  product_file_size: 9703
  product_url: http://purl.obolibrary.org/obo/psdo.owl
- category: OntologyProduct
  description: Plant Stress Ontology in OWL format
  format: owl
  id: pso.owl
  name: pso.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pso
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 365840
  product_url: http://purl.obolibrary.org/obo/pso.owl
- category: OntologyProduct
  description: Plant Stress Ontology in OBO format
  format: obo
  id: pso.obo
  name: pso.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pso
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 241726
  product_url: http://purl.obolibrary.org/obo/pso.obo
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
- category: OntologyProduct
  description: Unipathway in OWL format
  format: owl
  id: upa.owl
  name: upa.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: upa
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 798911
  product_url: http://purl.obolibrary.org/obo/upa.owl
- category: OntologyProduct
  description: Unipathway in OBO format
  format: obo
  id: upa.obo
  name: upa.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: upa
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 454223
  product_url: http://purl.obolibrary.org/obo/upa.obo
- category: OntologyProduct
  description: Xenopus Phenotype Ontology in OWL format
  format: owl
  id: xpo.owl
  name: xpo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: xao
  product_file_size: 97539811
  product_url: http://purl.obolibrary.org/obo/xpo.owl
- category: OntologyProduct
  description: Xenopus Phenotype Ontology in OBO format
  format: obo
  id: xpo.obo
  name: xpo.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: xao
  product_file_size: 11508476
  product_url: http://purl.obolibrary.org/obo/xpo.obo
- category: OntologyProduct
  description: Zebrafish Phenotype Ontology in OWL format
  format: owl
  id: zp.owl
  name: zp.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: zfa
  product_file_size: 170306263
  product_url: http://purl.obolibrary.org/obo/zp.owl
- category: OntologyProduct
  description: Zebrafish Phenotype Ontology in OBO format
  format: obo
  id: zp.obo
  name: zp.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: zfa
  product_file_size: 15870641
  product_url: http://purl.obolibrary.org/obo/zp.obo
publications:
- authors:
  - Barry Smith
  - Werner Ceusters
  - Bert Klagges
  - Jacob Köhler
  - Anand Kumar
  - Jane Lomax
  - Chris Mungall
  - Fabian Neuhaus
  - Alan L Rector
  - Cornelius Rosse
  doi: 10.1186/gb-2005-6-5-r46
  id: https://www.ncbi.nlm.nih.gov/pubmed/15892874
  journal: Genome Biol
  preferred: true
  title: Relations in biomedical ontologies
  year: '2005'
repository: https://github.com/oborel/obo-relations
---
## Description

Relationship types shared across multiple ontologies

## Contacts

- Chris Mungall (cjmungall@lbl.gov) [ORCID: 0000-0002-6601-2165](https://orcid.org/0000-0002-6601-2165)

## Products

### Relation Ontology

Canonical edition

**URL**: [http://purl.obolibrary.org/obo/ro.owl](http://purl.obolibrary.org/obo/ro.owl)

**Format**: owl

### Relation Ontology in obo format

The obo edition is less expressive than the OWL, and has imports merged in

**URL**: [http://purl.obolibrary.org/obo/ro.obo](http://purl.obolibrary.org/obo/ro.obo)

**Format**: obo

### Relation Ontology in obojson format

Relation Ontology in obojson format

**URL**: [http://purl.obolibrary.org/obo/ro.json](http://purl.obolibrary.org/obo/ro.json)

**Format**: json

### RO Core relations

Minimal subset intended to work with BFO-classes

**URL**: [http://purl.obolibrary.org/obo/ro/core.owl](http://purl.obolibrary.org/obo/ro/core.owl)

**Format**: owl

### RO base ontology

Axioms defined within RO and to be used in imports for other ontologies

**URL**: [http://purl.obolibrary.org/obo/ro/ro-base.owl](http://purl.obolibrary.org/obo/ro/ro-base.owl)

**Format**: owl

### Interaction relations

For use in ecology and environmental science

**URL**: [http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl)

**Format**: owl

### Ecology subset

Ecology subset

**URL**: [http://purl.obolibrary.org/obo/ro/subsets/ro-eco.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-eco.owl)

**Format**: owl

### Neuroscience subset

For use in neuroscience

**URL**: [http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl)

**Format**: owl

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*