---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: g.gkoutos@gmail.com
  - contact_type: github
    value: gkoutos
  label: George Gkoutos
  orcid: 0000-0002-2061-091X
creation_date: '2025-06-04T00:00:00Z'
description: An ontology of phenotypic qualities (properties, attributes or characteristics)
domains:
- phenotype
homepage_url: https://github.com/pato-ontology/pato/
id: pato
infores_id: pato
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Phenotype And Trait Ontology
products:
- category: OntologyProduct
  description: Phenotype And Trait Ontology in OWL format
  format: owl
  id: pato.owl
  name: pato.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pato
  product_file_size: 1205348
  product_url: http://purl.obolibrary.org/obo/pato.owl
- category: OntologyProduct
  description: Phenotype And Trait Ontology in OBO format
  format: obo
  id: pato.obo
  name: pato.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pato
  product_file_size: 110437
  product_url: http://purl.obolibrary.org/obo/pato.obo
- category: OntologyProduct
  description: Phenotype And Trait Ontology in JSON format
  format: json
  id: pato.json
  name: pato.json
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pato
  product_file_size: 883967
  product_url: http://purl.obolibrary.org/obo/pato.json
- category: OntologyProduct
  description: Includes axioms linking to other ontologies, but no imports of those
    ontologies
  format: owl
  id: pato.pato-base.owl
  name: pato.pato-base.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pato
  product_file_size: 180954
  product_url: http://purl.obolibrary.org/obo/pato/pato-base.owl
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
  description: The NLM-CKN knowledge graph of cellular phenotypes. It is built from
    triple assertions (subject-predicate-object) that link single-cell genomics experimental
    data (from the CELLxGENE Census) and computationally derived NS-Forest marker
    genes to the Cell Ontology and other reference ontologies, augmented with literature-derived
    assertions from text mining/NLP. The graph is produced by the NLM-CKN ETL pipeline
    as an ArangoDB archive and served via the web application at https://nlm-ckn.org.
  format: http
  id: nlm-ckn.graph
  name: nlm-ckn-graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm-ckn
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://nlm-ckn.org
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: cl
  - relation_type: prov:wasInfluencedBy
    source: uberon
  - relation_type: prov:wasInfluencedBy
    source: pato
  - relation_type: prov:wasInfluencedBy
    source: mondo
  - relation_type: prov:wasInfluencedBy
    source: hsapdv
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Phenotypic Quality Ontology (PATO), produced by
    KG-Bioportal from the BioPortal submission. The archive contains PATO_nodes.tsv
    and PATO_edges.tsv.
  edge_count: 31234
  format: kgx
  id: pato.kg-bioportal
  latest_version: '2025-05-14'
  name: PATO KGX graph (KG-Bioportal)
  node_count: 9032
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pato
  product_file_size: 804645
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/PATO.tar.gz
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
  description: Mass spectrometry ontology in OBO format
  format: obo
  id: ms.obo
  name: ms.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: uo
  product_file_size: 1143028
  product_url: http://purl.obolibrary.org/obo/ms.obo
- category: OntologyProduct
  description: Mass spectrometry ontology in OWL format
  format: owl
  id: ms.owl
  name: ms.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: uo
  product_file_size: 4925738
  product_url: http://purl.obolibrary.org/obo/ms.owl
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
  description: Pathogen Host Interaction Phenotype Ontology in OWL format
  format: owl
  id: phipo.owl
  name: phipo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phipo
  - relation_type: prov:hadPrimarySource
    source: pato
  product_file_size: 1709467
  product_url: http://purl.obolibrary.org/obo/phipo.owl
- category: OntologyProduct
  description: Pathogen Host Interaction Phenotype Ontology in OBO format
  format: obo
  id: phipo.obo
  name: phipo.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phipo
  - relation_type: prov:hadPrimarySource
    source: pato
  product_file_size: 1133552
  product_url: http://purl.obolibrary.org/obo/phipo.obo
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
  - Gkoutos GV
  - Schofield PN
  - Hoehndorf R
  doi: 10.1093/bib/bbx035
  id: https://www.ncbi.nlm.nih.gov/pubmed/28387809
  journal: Brief Bioinform
  title: 'The anatomy of phenotype ontologies: principles, properties and applications'
  year: '2018'
- authors:
  - Gkoutos GV
  - Green EC
  - Mallon AM
  - Hancock JM
  - Davidson D
  doi: 10.1186/gb-2004-6-1-r8
  id: https://www.ncbi.nlm.nih.gov/pubmed/15642100
  journal: Genome Biol
  title: Using ontologies to describe mouse phenotypes
  year: '2005'
repository: https://github.com/pato-ontology/pato
---
## Description

An ontology of phenotypic qualities (properties, attributes or characteristics)

## Contacts

- George Gkoutos (g.gkoutos@gmail.com) [ORCID: 0000-0002-2061-091X](https://orcid.org/0000-0002-2061-091X)

## Products

### pato.owl

Phenotype And Trait Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/pato.owl](http://purl.obolibrary.org/obo/pato.owl)

**Format**: owl

### pato.obo

Phenotype And Trait Ontology in OBO format

**URL**: [http://purl.obolibrary.org/obo/pato.obo](http://purl.obolibrary.org/obo/pato.obo)

**Format**: obo

### pato.json

Phenotype And Trait Ontology in JSON format

**URL**: [http://purl.obolibrary.org/obo/pato.json](http://purl.obolibrary.org/obo/pato.json)

**Format**: json

### pato.pato-base.owl

Includes axioms linking to other ontologies, but no imports of those ontologies

**URL**: [http://purl.obolibrary.org/obo/pato/pato-base.owl](http://purl.obolibrary.org/obo/pato/pato-base.owl)

**Format**: owl

## Publications

- [The anatomy of phenotype ontologies: principles, properties and applications](https://www.ncbi.nlm.nih.gov/pubmed/28387809)
- [Using ontologies to describe mouse phenotypes](https://www.ncbi.nlm.nih.gov/pubmed/15642100)

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*