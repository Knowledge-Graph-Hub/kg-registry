---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: DrugCentral
creation_date: '2025-03-09T00:00:00Z'
description: DrugCentral is online drug information resource created and maintained
  by Division of Translational Informatics at University of New Mexico.
domains:
- health
homepage_url: https://drugcentral.org/
id: drugcentral
infores_id: drugcentral
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: DrugCentral
products:
- category: GraphProduct
  description: DrugCentral Automat
  format: kgx-jsonl
  id: automat.drugcentral
  infores_id: automat-drug-central
  name: drugcentral_automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/DrugCentral_Automat/dec0617490b49c7a/
- category: Product
  compression: gzip
  description: PostgreSQL (v14.5) database dump of all information in DrugCentral.
  format: postgres
  id: drugcentral.data
  name: DrugCentral Database dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 1400714190
  product_url: https://unmtid-dbs.net/download/drugcentral.dump.11012023.sql.gz
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  product_file_size: 376501785
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  product_url: https://arax.ncats.io/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
- category: GraphProduct
  description: Training data for the MIND knowledge graph containing 9,651,040 edges
  format: tsv
  id: mind.train
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Training Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  product_url: https://zenodo.org/records/8117748/files/train.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 429 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-18_ Timeout connecting
    to URL
- category: GraphProduct
  description: Test data for the MIND knowledge graph containing DrugCentral indications
  format: tsv
  id: mind.test
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Test Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  product_url: https://zenodo.org/records/8117748/files/test.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-18_ HTTP 429 error when
    accessing file
- category: GraphProduct
  description: Validation data for the MIND knowledge graph containing DrugCentral
    indications
  format: tsv
  id: mind.valid
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Validation Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  product_url: https://zenodo.org/records/8117748/files/valid.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 429 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-30_ Timeout connecting
    to URL
- category: Product
  description: Dictionary of entities in the MIND knowledge graph
  format: tsv
  id: mind.entities
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Entities Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  product_file_size: 5629618
  product_url: https://zenodo.org/records/8117748/files/entities.dict
- category: Product
  description: Dictionary of relations in the MIND knowledge graph
  format: tsv
  id: mind.relations
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: MIND Relations Dictionary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mind
  product_file_size: 1648
  product_url: https://zenodo.org/records/8117748/files/relations.dict
- category: Product
  description: Complete RepoDB dataset containing drug repositioning successes and
    failures, with approved drugs, indications, and clinical trial outcomes
  format: csv
  id: repodb.full_dataset
  name: RepoDB Full Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: repodb
  product_url: https://unmtid-shinyapps.net/shiny/repodb/session/98046b0f66cea75c432b5576c1ba2840/download/downloadFull?w=
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: HTTP 404 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-27_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-08-07_ No Content-Length
    header found
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Drug Approvals KP distributed via the NCATS
    Translator release site (release 2026_03_19; build dakp_0.5.3_c3f74ab4_2025sep1_4.3.6;
    source version 0.5.3; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 73999
  format: kgx-jsonl
  id: translator.dakp.graph
  latest_version: '2026_03_19'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator DAKP KGX Graph
  node_count: 3783
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/dakp/latest/
  versions:
  - '2026_03_19'
  - dakp_0.5.3_c3f74ab4_2025sep1_4.3.6
- category: Product
  description: drugcentral Nodes TSV
  format: tsv
  id: obo-db-ingest.drugcentral.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: drugcentral Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 407590
  product_url: https://w3id.org/biopragmatics/resources/drugcentral/drugcentral.tsv
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for DrugCentral distributed via the NCATS Translator
    release site (release 2026_03_19; build drugcentral_2023_11_01_82890f34_2025sep1_4.3.6;
    source version 2023_11_01; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 36494
  format: kgx-jsonl
  id: translator.drugcentral.graph
  latest_version: '2026_03_19'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator DrugCentral KGX Graph
  node_count: 5493
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/drugcentral/latest/
  versions:
  - '2026_03_19'
  - drugcentral_2023_11_01_82890f34_2025sep1_4.3.6
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
publications:
- authors:
  - Ursu O
  - Holmes J
  - Knockel J
  - Bologa CG
  - Yang JJ
  - Mathias SL
  - Nelson SJ
  - Oprea TI
  doi: doi:10.1093/nar/gkw993
  id: doi:10.1093/nar/gkw993
  title: 'DrugCentral: online drug compendium'
  year: '2017'
---
DrugCentral