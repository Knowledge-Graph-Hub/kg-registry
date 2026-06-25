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
- biomedical
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
  format: http
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
  product_url: https://spoke.ucsf.edu/data-tools
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
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
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
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  format: http
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
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_url: https://arax.ncats.io/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
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
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_url: https://zenodo.org/records/8117748/files/train.txt
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 429 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-18_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-06-24: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-06-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-25: No Content-Length
    header found'
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
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_url: https://zenodo.org/records/8117748/files/test.txt
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-18_ HTTP 429 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-24: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-06-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-25: No Content-Length
    header found'
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
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_url: https://zenodo.org/records/8117748/files/valid.txt
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-12-22_ HTTP 429 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-30_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-06-24: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-06-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-25: No Content-Length
    header found'
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
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
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
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
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
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-27_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-08-07_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-06-24: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-25: HTTP 404 error
    when accessing file'
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
- category: GraphicalInterface
  description: Browser for complete Hetionet v1.0 graph database in Neo4j
  format: http
  id: hetionet.neo4j
  name: Hetionet v1.0 Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://neo4j.het.io/browser/
- category: GraphProduct
  description: Hetionet v1.0 in JSON format
  format: json
  id: hetionet.data.json
  name: Hetionet v1.0 JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 131
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/json/hetionet-v1.0.json.bz2
- category: GraphProduct
  description: Hetionet v1.0 as a Neo4j database
  format: neo4j
  id: hetionet.data.neo4j
  name: Hetionet v1.0 Neo4j
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 132
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/neo4j/hetionet-v1.0.db.tar.bz2
- category: GraphProduct
  description: Hetionet v1.0 as SIF edges
  format: sif
  id: hetionet.data.edges
  name: Hetionet v1.0 edges (SIF)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 131
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-edges.sif.gz
- category: GraphProduct
  description: Hetionet v1.0 as TSV nodes
  format: tsv
  id: hetionet.data.nodes
  name: Hetionet v1.0 nodes (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 427128
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-nodes.tsv
- category: ProcessProduct
  description: Python package for creating, querying, and operating on hetnets (heterogeneous
    networks)
  id: hetnetpy
  name: hetnetpy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://github.com/hetio/hetnetpy
- category: GraphicalInterface
  description: Web application to search and explore connectivity between nodes in
    Hetionet
  format: http
  id: hetionet.search
  name: Hetnet Connectivity Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://het.io/search
- category: GraphProduct
  compression: gzip
  description: PharMeBINet V2 JSON release published on February 6, 2024.
  format: json
  id: pharmebinet.json
  latest_version: v2
  name: PharMeBINet JSON Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1942958027
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.json.gz/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 TSV release published on February 6, 2024.
  format: tsv
  id: pharmebinet.tsv
  latest_version: v2
  name: PharMeBINet TSV Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1922614551
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_tsv_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 GraphML release published on February 6, 2024.
  format: mixed
  id: pharmebinet.graphml
  latest_version: v2
  name: PharMeBINet GraphML Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 2027519087
  product_url: https://zenodo.org/api/records/17814889/files/PharMeBiNet_graphml_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j database release published on February 6, 2024.
  format: neo4j
  id: pharmebinet.neo4j
  latest_version: v2
  name: PharMeBINet Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3847978577
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j dump release published on February 6, 2024.
  dump_format: neo4j
  format: neo4j
  id: pharmebinet.neo4j.dump
  latest_version: v2
  name: PharMeBINet Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3598325722
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_dump_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: Product
  description: MySQL database dump files containing the complete TCRD relational database
    schema and data for local installation and analysis
  format: mysql
  id: tcrd.database_download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://unmtid-dbs.net/download/TCRD/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to TCRD data through Pharos
    for computational workflows and custom applications
  format: http
  id: tcrd.api
  is_public: true
  name: Pharos API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://pharos.nih.gov/api
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
- category: DocumentationProduct
  description: Comprehensive documentation describing TCRD data sources, schema structure,
    and usage guidelines
  format: http
  id: tcrd.documentation
  name: TCRD Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://unmtid-dbs.net/download/TCRD/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
- category: GraphProduct
  description: KGX nodes and edges for KG-COVID-19
  format: kgx
  id: kg-covid-19.graph
  name: KG-COVID-19 graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-covid-19
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cord-19
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://kghub.io/kg-covid-19/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-11-17_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-24: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-25: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: KGX Distribution of KG-IDG
  format: kgx
  id: kg-idg.graph
  name: KGX Distribution of KG-IDG
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-idg
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://kg-hub.berkeleybop.io/kg-idg/current/kg-microbe.tar.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-24: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-25: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
- category: GraphProduct
  description: The full PrimeKG dataset containing disease relationships.
  id: primekg.graph
  name: PrimeKG Full Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://dataverse.harvard.edu/api/access/datafile/6180620
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-04_ Timeout connecting
    to URL
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
  doi: 10.1093/nar/gkw993
  id: doi:10.1093/nar/gkw993
  journal: Nucleic Acids Research
  title: 'DrugCentral: online drug compendium'
  year: '2017'
---
DrugCentral