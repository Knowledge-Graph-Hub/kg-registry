---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Sabrina Toro
    orcid: 0000-0002-4142-7153
    contact_details:
      - contact_type: email
        value: Sabrina@tislab.org
      - contact_type: github
        value: sabrinatoro
creation_date: '2025-04-22T00:00:00Z'
description: A global community effort to harmonize multiple disease resources to yield a coherent merged ontology.
domains:
  - biomedical
homepage_url: https://monarch-initiative.github.io/mondo
id: mondo
infores_id: mondo
last_modified_date: '2026-04-15T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Mondo Disease Ontology
products:
  - category: OntologyProduct
    description: Complete ontology with merged imports.
    format: owl
    id: mondo.owl
    name: Mondo OWL edition
    product_file_size: 241954309
    product_url: http://purl.obolibrary.org/obo/mondo.owl
  - category: OntologyProduct
    description: OBO serialization of mondo.owl.
    format: obo
    id: mondo.obo
    name: Mondo OBO Format edition
    product_file_size: 51081036
    product_url: http://purl.obolibrary.org/obo/mondo.obo
  - category: OntologyProduct
    description: Obographs serialization of mondo.owl.
    format: obo
    id: mondo.json
    name: Mondo JSON edition
    product_file_size: 102877798
    product_url: http://purl.obolibrary.org/obo/mondo.json
  - category: OntologyProduct
    description: The main ontology plus axioms connecting to select external ontologies, excluding the external ontologies themselves
    format: owl
    id: mondo.mondo-base.owl
    name: Mondo Base Release
    product_file_size: 227201131
    product_url: http://purl.obolibrary.org/obo/mondo/mondo-base.owl
  - category: OntologyProduct
    description: The main ontology classes and their hierarchies, without references to external terms.
    format: owl
    id: mondo.mondo-simple.owl
    name: Mondo Simple Release
    product_file_size: 215504840
    product_url: http://purl.obolibrary.org/obo/mondo/mondo-simple.owl
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
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
    description: PheKnowLator graph files, including subsets with and without inverse relations.
    format: owl
    id: pheknowlator.graph
    latest_version: current_build
    name: PheKnowLator graph
    original_source:
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: bioportal
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: genemania
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
    secondary_source:
      - source: pheknowlator
        relation_type: prov:wasInfluencedBy
    versions:
      - v1.0.0
      - v2.0.0
      - v2.1.0
      - v3.0.2
      - v4.0.0
      - current_build
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
  - category: GraphProduct
    description: KGX distribution of the ICEES Exposures KP in Knowledge Graph Exchange (KGX) format, containing integrated clinical and environmental exposures data as a knowledge graph with 226 nodes and 14,342 edges
    format: kgx-jsonl
    id: icees-kg.graph
    name: KGX distribution of the ICEES Exposures KP
    original_source:
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: icees-kg
        relation_type: prov:hadPrimarySource
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/icees-kg/1.5.0/
    secondary_source:
      - source: icees-kg
        relation_type: prov:wasInfluencedBy
  - category: ProgrammingInterface
    description: Translator Reasoner API (TRAPI) endpoint for querying ICEES KG using standardized Translator protocols
    format: http
    id: icees-kg.trapi
    name: ICEES KG TRAPI API
    original_source:
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: icees-kg
        relation_type: prov:hadPrimarySource
    product_url: https://robokop.renci.org/api-docs/docs/automat/icees-kg-trapi
    secondary_source:
      - source: icees-kg
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: Meta knowledge graph and metadata describing the data sources, node types, edge types, and predicates available in ICEES KG
    format: json
    id: icees-kg.metadata
    name: ICEES KG Metadata
    original_source:
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: icees-kg
        relation_type: prov:hadPrimarySource
    product_url: https://robokop.renci.org/api-docs/docs/automat/metadata-metadata-get-icees-kg
    secondary_source:
      - source: icees-kg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: RNA-KG as a Neo4j Dump
    format: neo4j
    id: rna-kg.kg.neo4j
    name: RNA-KG Neo4j Dump
    original_source:
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: circbase
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
    product_file_size: 3976840239
    product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
    secondary_source:
      - source: rna-kg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: RNA-KG Nodes in CSV format
    format: csv
    id: rna-kg.kg.nodes
    name: RNA-KG Nodes
    original_source:
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: circbase
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
    product_file_size: 4424633304
    product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
    secondary_source:
      - source: rna-kg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: RNA-KG Edges in CSV format
    format: csv
    id: rna-kg.kg.edges
    name: RNA-KG Edges
    original_source:
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: circbase
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
    product_file_size: 18370248815
    product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
    secondary_source:
      - source: rna-kg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Integrated graph knowledge base combining Mendelian randomization causal estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships (Neo4j backend)
    format: neo4j
    id: epigraphdb.graph
    name: EpiGraphDB Graph Database
    original_source:
      - source: epigraphdb
        relation_type: prov:hadPrimarySource
      - source: kg-monarch
        relation_type: prov:hadPrimarySource
      - source: vectology
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: prsatlas
        relation_type: prov:hadPrimarySource
      - source: eqtlgen
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: cpic
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: semmeddb
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: mrbase
        relation_type: prov:hadPrimarySource
    product_url: https://docs.epigraphdb.org/graph-database/
    secondary_source:
      - source: epigraphdb
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
    description: Nodes for the Drug Approvals KP, v0.3.9
    format: kgx
    id: drug-approvals-kp.graph.nodes
    name: Drug Approvals KP Graph Nodes
    original_source:
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
    product_file_size: 701451
    product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.9.tsv
    secondary_source:
      - source: drug-approvals-kp
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Edges for the Drug Approvals KP, v0.3.9
    format: kgx
    id: drug-approvals-kp.graph.edges
    name: Drug Approvals KP Graph Edges
    original_source:
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
    product_file_size: 31052966
    product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_edges_v0.3.9.tsv
    secondary_source:
      - source: drug-approvals-kp
        relation_type: prov:wasInfluencedBy
  - category: MappingProduct
    description: MONDO SSSOM. Mappings from MONDO identifiers to other namespaces.
    format: sssom
    id: mondo.sssom
    name: MONDO SSSOM
    original_source:
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
    product_file_size: 1437457
    product_url: https://raw.githubusercontent.com/monarch-initiative/mondo/refs/heads/master/src/ontology/mappings/mondo.sssom.tsv
    secondary_source:
      - source: mondo
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: History file tracking changes to Mondo term mappings to CUIs
    format: txt
    id: medgen.mondo-history
    name: Mondo CUI History
    original_source:
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
    product_file_size: 1012883
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MONDO_CUI_history.txt
repository: https://github.com/monarch-initiative/mondo
taxon:
  - NCBITaxon:33208
publications:
  - id: https://doi.org/10.1093/genetics/iyaf215
    title: 'Mondo: Integrating Disease Terminology Across Communities'
  - id: https://www.medrxiv.org/content/10.1101/2022.04.13.22273750
    title: 'Mondo: Unifying diseases for the world, by the world'
---

## Description

A global community effort to harmonize multiple disease resources to yield a coherent merged ontology.

## Contacts

- Sabrina Toro (Sabrina@tislab.org) [ORCID: 0000-0002-4142-7153](https://orcid.org/0000-0002-4142-7153)

## Products

### Mondo OWL edition

Complete ontology with merged imports.

**URL**: [http://purl.obolibrary.org/obo/mondo.owl](http://purl.obolibrary.org/obo/mondo.owl)

**Format**: owl

### Mondo OBO Format edition

OBO serialization of mondo.owl.

**URL**: [http://purl.obolibrary.org/obo/mondo.obo](http://purl.obolibrary.org/obo/mondo.obo)

**Format**: obo

### Mondo JSON edition

Obographs serialization of mondo.owl.

**URL**: [http://purl.obolibrary.org/obo/mondo.json](http://purl.obolibrary.org/obo/mondo.json)

**Format**: obo

### Mondo Base Release

The main ontology plus axioms connecting to select external ontologies, excluding the external ontologies themselves

**URL**: [http://purl.obolibrary.org/obo/mondo/mondo-base.owl](http://purl.obolibrary.org/obo/mondo/mondo-base.owl)

**Format**: owl

### Mondo Simple Release

The main ontology classes and their hierarchies, without references to external terms.

**URL**: [http://purl.obolibrary.org/obo/mondo/mondo-simple.owl](http://purl.obolibrary.org/obo/mondo/mondo-simple.owl)

**Format**: owl

## Publications

- [Mondo: Integrating Disease Terminology Across Communities](https://doi.org/10.1093/genetics/iyaf215)
- [Mondo: Unifying diseases for the world, by the world](https://www.medrxiv.org/content/10.1101/2022.04.13.22273750)

**Domains**: biomedical

**Taxon**: NCBITaxon:33208

---

*This resource was automatically synchronized from the OBO Foundry registry.*
