---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: frederic.bastian@unil.ch
      - contact_type: github
        value: fbastian
    label: Frederic Bastian
    orcid: 0000-0002-9415-5104
creation_date: '2025-05-28T00:00:00Z'
description: An ontology representation of the NCBI organismal taxonomy
domains:
  - biological systems
homepage_url: https://github.com/obophenotype/ncbitaxon
id: ncbitaxon
infores_id: ncbi-taxon
last_modified_date: '2026-04-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: NCBI organismal classification
products:
  - category: OntologyProduct
    description: Main release
    format: owl
    id: ncbitaxon.owl
    name: Main release
    product_file_size: 1915871262
    product_url: http://purl.obolibrary.org/obo/ncbitaxon.owl
  - category: OntologyProduct
    description: OBO Format version of Main release
    format: obo
    id: ncbitaxon.obo
    name: OBO Format version of Main release
    product_file_size: 654510820
    product_url: http://purl.obolibrary.org/obo/ncbitaxon.obo
  - category: OntologyProduct
    description: OBOGraphs JSON version of Main release
    format: json
    id: ncbitaxon.json
    name: OBOGraphs JSON version of Main release
    product_url: http://purl.obolibrary.org/obo/ncbitaxon.json
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
  - category: OntologyProduct
    description: taxslim
    format: owl
    id: ncbitaxon.subsets.taxslim.owl
    name: taxslim
    product_file_size: 39898238
    product_url: http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim.owl
  - category: OntologyProduct
    description: taxslim disjointness axioms
    format: owl
    id: ncbitaxon.subsets.taxslim-disjoint-over-in-taxon.owl
    name: taxslim disjointness axioms
    product_file_size: 75398508
    product_url: http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim-disjoint-over-in-taxon.owl
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
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
    product_file_size: 12464495186
    product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-raw-20250222.tar.gz
    secondary_source:
      - source: kg-microbe
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    compression: targz
    description: The core KG KG-Microbe-Core with ontologies, organismal traits, and growth preferences.
    format: kgx
    id: kg-microbe.graph.core
    name: KG-Microbe KGX Graph - Core
    original_source:
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
    secondary_source:
      - source: kg-microbe
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    compression: targz
    description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
    format: kgx
    id: kg-microbe.graph.biomedical
    name: KG-Microbe KGX Graph - Biomedical
    original_source:
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
    secondary_source:
      - source: kg-microbe
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    compression: targz
    description: Core plus Uniprot genome annotations
    format: kgx
    id: kg-microbe.graph.function
    name: KG-Microbe KGX Graph - Function
    original_source:
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
    product_file_size: 4623010863
    product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-function-20250222.tar.gz
    secondary_source:
      - source: kg-microbe
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    compression: targz
    description: Biomedical plus Uniprot genome annotations
    format: kgx
    id: kg-microbe.graph.biomedical-function
    name: KG-Microbe KGX Graph - Biomedical-Function
    original_source:
      - source: envo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: bacdive
        relation_type: prov:hadPrimarySource
      - source: mediadive
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: ec
        relation_type: prov:hadPrimarySource
      - source: bactotraits
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disbiome
        relation_type: prov:hadPrimarySource
      - source: metpo
        relation_type: prov:hadPrimarySource
    product_file_size: 4640682152
    product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
    secondary_source:
      - source: kg-microbe
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: The SPOKE knowledge graph containing nodes and edges from multiple biomedical data sources.
    id: spoke.graph
    name: SPOKE Graph
    original_source:
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pid
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: lincs-l1000
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: civic
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: clinicaltrialsgov
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: metacyc
        relation_type: prov:hadPrimarySource
      - source: bv-brc
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: pathophenodb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: protcid
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: spoke
        relation_type: prov:wasInfluencedBy
  - description: The MechRepoNet knowledge graph in its original format
    id: mechreponet.kg
    name: MechRepoNet Knowledge Graph
    original_source:
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: hetionet
        relation_type: prov:hadPrimarySource
      - source: complexportal
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
      - source: mirtarbase
        relation_type: prov:hadPrimarySource
      - source: unii
        relation_type: prov:hadPrimarySource
      - source: biolink
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
    secondary_source:
      - source: mechreponet
        relation_type: prov:wasInfluencedBy
  - category: ProgrammingInterface
    description: TRAPI web API for querying MicrobiomeKG
    format: http
    id: microbiomekg.api
    name: MicrobiomeKG Plover API
    original_source:
      - source: biolink
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: eupathdb
        relation_type: prov:hadPrimarySource
    product_url: https://multiomics.transltr.io/mbkp
    secondary_source:
      - source: microbiomekg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
    format: kgx-jsonl
    id: rtx-kg2.graph.nodes
    name: RTX-KG2.10.1c KGX JSONL Nodes
    original_source:
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
      - source: rtx-kg2
        relation_type: prov:hadPrimarySource
      - source: semmeddb
        relation_type: prov:hadPrimarySource
    product_file_size: 376501785
    product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
    secondary_source:
      - source: rtx-kg2
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
    format: kgx-jsonl
    id: rtx-kg2.graph.edges
    name: RTX-KG2.10.1c KGX JSONL Edges
    original_source:
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
      - source: rtx-kg2
        relation_type: prov:hadPrimarySource
      - source: semmeddb
        relation_type: prov:hadPrimarySource
    product_file_size: 1807360397
    product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
    secondary_source:
      - source: rtx-kg2
        relation_type: prov:wasInfluencedBy
  - category: ProgrammingInterface
    description: Neo4j distribution of the RTX-KG2 as a graph database
    dump_format: neo4j
    id: rtx-kg2.neo4j
    is_neo4j: true
    is_public: false
    name: RTX-KG2 Neo4j
    original_source:
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
      - source: rtx-kg2
        relation_type: prov:hadPrimarySource
      - source: semmeddb
        relation_type: prov:hadPrimarySource
    product_url: https://arax.ncats.io/
    secondary_source:
      - source: rtx-kg2
        relation_type: prov:wasInfluencedBy
  - category: OntologyProduct
    description: OWL release of Monochrom Ontology
    format: owl
    id: chr.model.owl
    name: Monochrom Ontology OWL release
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: geno
        relation_type: prov:hadPrimarySource
      - source: skos
        relation_type: prov:hadPrimarySource
      - source: gff
        relation_type: prov:hadPrimarySource
    product_file_size: 102365
    product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
    secondary_source:
      - source: chr
        relation_type: prov:wasInfluencedBy
  - category: OntologyProduct
    description: The latest release of EFO in OWL format
    format: owl
    id: efo.owl
    name: EFO OWL
    original_source:
      - source: bfo
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: cob
        relation_type: prov:hadPrimarySource
      - source: dc
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: ecto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: fbbt
        relation_type: prov:hadPrimarySource
      - source: fbdv
        relation_type: prov:hadPrimarySource
      - source: fma
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hancestro
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: ido
        relation_type: prov:hadPrimarySource
      - source: ma
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: mpath
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: oba
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: ogms
        relation_type: prov:hadPrimarySource
      - source: oio
        relation_type: prov:hadPrimarySource
      - source: omit
        relation_type: prov:hadPrimarySource
      - source: omo
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: po
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: semapv
        relation_type: prov:hadPrimarySource
      - source: skos
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: to
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: wbls
        relation_type: prov:hadPrimarySource
      - source: zfa
        relation_type: prov:hadPrimarySource
    product_file_size: 240665663
    product_url: https://www.ebi.ac.uk/efo/efo.owl
    secondary_source:
      - source: efo
        relation_type: prov:wasInfluencedBy
  - category: OntologyProduct
    description: The latest release of EFO in OBO format
    format: obo
    id: efo.obo
    name: EFO OBO
    original_source:
      - source: bfo
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: cob
        relation_type: prov:hadPrimarySource
      - source: dc
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: ecto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: fbbt
        relation_type: prov:hadPrimarySource
      - source: fbdv
        relation_type: prov:hadPrimarySource
      - source: fma
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hancestro
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: ido
        relation_type: prov:hadPrimarySource
      - source: ma
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: mpath
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: oba
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: ogms
        relation_type: prov:hadPrimarySource
      - source: oio
        relation_type: prov:hadPrimarySource
      - source: omit
        relation_type: prov:hadPrimarySource
      - source: omo
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: po
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: semapv
        relation_type: prov:hadPrimarySource
      - source: skos
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: to
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: wbls
        relation_type: prov:hadPrimarySource
      - source: zfa
        relation_type: prov:hadPrimarySource
    product_file_size: 64058275
    product_url: https://www.ebi.ac.uk/efo/efo.obo
    secondary_source:
      - source: efo
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    compatibility:
      - standard: biolink
    compression: zip
    description: "Curated mechanistic drug–disease paths comprising the DrugMechDB dataset packaged as a downloadable archive."
    dump_format: other
    format: mixed
    id: drugmechdb.graph
    latest_version: 2.0.1
    name: DrugMechDB Graph Dataset
    original_source:
      - source: go
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://doi.org/10.5281/zenodo.8139357
    repository: https://github.com/SuLab/DrugMechDB
    versions:
      - 2.0.1
      - 2.0.0
      - 1.0.2
      - '1.0'
  - category: GraphProduct
    description: RDF dump of the Open Research Knowledge Graph distributed in N-Triples format.
    format: ntriples
    id: orkg.dump
    name: ORKG RDF Dump
    original_source:
      - source: orkg
        relation_type: prov:hadPrimarySource
      - source: wikidata
        relation_type: prov:hadPrimarySource
      - source: geonames
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: omit
        relation_type: prov:hadPrimarySource
      - source: iao
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: stato
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
    product_file_size: 642902930
    product_url: https://orkg.org/api/rdf/dump
    secondary_source:
      - source: orkg
        relation_type: prov:wasInfluencedBy
publications: []
repository: https://github.com/obophenotype/ncbitaxon
---

## Description

An ontology representation of the NCBI organismal taxonomy

## Contacts

- Frederic Bastian (frederic.bastian@unil.ch) [ORCID: 0000-0002-9415-5104](https://orcid.org/0000-0002-9415-5104)

## Products

### Main release

Main release

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon.owl](http://purl.obolibrary.org/obo/ncbitaxon.owl)

**Format**: owl

### OBO Format version of Main release

OBO Format version of Main release

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon.obo](http://purl.obolibrary.org/obo/ncbitaxon.obo)

**Format**: obo

### OBOGraphs JSON version of Main release

OBOGraphs JSON version of Main release

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon.json](http://purl.obolibrary.org/obo/ncbitaxon.json)

**Format**: json

### taxslim

taxslim

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim.owl](http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim.owl)

**Format**: owl

### taxslim disjointness axioms

taxslim disjointness axioms

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim-disjoint-over-in-taxon.owl](http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim-disjoint-over-in-taxon.owl)

**Format**: owl

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*
