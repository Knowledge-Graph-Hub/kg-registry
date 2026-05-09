---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: info@disgenet.com
    label: MedBioinformatics Solutions SL
creation_date: '2025-06-04T00:00:00Z'
description: DisGeNET is the world's largest and most extensive gene-disease association (GDA) network, integrating data from expert-curated repositories, GWAS catalogs, animal models, and scientific literature. It contains gene-disease associations, variant-disease associations, and disease-disease associations with extensive evidence supporting each connection.
domains:
  - biomedical
  - genomics
  - clinical
  - precision medicine
  - translational
  - drug discovery
homepage_url: https://www.disgenet.com/
id: disgenet
infores_id: disgenet
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
license:
  id: https://www.disgenet.com/Legal
  label: DisGeNET License
name: DisGeNET
products:
  - category: GraphProduct
    description: DisGeNET data, including gene to disease associations and variant to disease associations (requires registration and subscription).
    id: disgenet.data
    name: DisGeNET Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: mgd
      - relation_type: prov:hadPrimarySource
        source: rgd
      - relation_type: prov:hadPrimarySource
        source: orphanet
      - relation_type: prov:hadPrimarySource
        source: psygenet
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: phewascat
      - relation_type: prov:hadPrimarySource
        source: ukbiobank
      - relation_type: prov:hadPrimarySource
        source: finngen
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
    product_url: https://www.disgenet.com/
  - category: ProgrammingInterface
    description: API access to DisGeNET data (requires registration and subscription).
    format: http
    id: disgenet.api
    name: DisGeNET API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: disgenet
    product_url: https://www.disgenet.com/
  - category: GraphicalInterface
    description: Browser for DisGeNET data (requires registration and subscription).
    format: http
    id: disgenet.browser
    name: DisGeNET Browser
    original_source:
      - relation_type: prov:hadPrimarySource
        source: disgenet
    product_url: https://www.disgenet.com/search?view=ALL&idents=ALL&source=ALL&tab=GDA
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: loinc
      - relation_type: prov:hadPrimarySource
        source: icd10
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: obi
      - relation_type: prov:hadPrimarySource
        source: obib
      - relation_type: prov:hadPrimarySource
        source: edam
      - relation_type: prov:hadPrimarySource
        source: hsapdv
      - relation_type: prov:hadPrimarySource
        source: sbo
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: ordo
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: uo
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: pgo
      - relation_type: prov:hadPrimarySource
        source: gencode
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: hra
      - relation_type: prov:hadPrimarySource
        source: hubmap
      - relation_type: prov:hadPrimarySource
        source: sennet
      - relation_type: prov:hadPrimarySource
        source: stellar
      - relation_type: prov:hadPrimarySource
        source: dct
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: connectivitymap
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: msigdb
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: 4dn
      - relation_type: prov:hadPrimarySource
        source: erccrbp
      - relation_type: prov:hadPrimarySource
        source: erccreg
      - relation_type: prov:hadPrimarySource
        source: faldo
      - relation_type: prov:hadPrimarySource
        source: glycordf
      - relation_type: prov:hadPrimarySource
        source: glycocoo
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: kidsfirst
      - relation_type: prov:hadPrimarySource
        source: lincs
      - relation_type: prov:hadPrimarySource
        source: motrpac
      - relation_type: prov:hadPrimarySource
        source: mw
      - relation_type: prov:hadPrimarySource
        source: npo
      - relation_type: prov:hadPrimarySource
        source: sckan
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: biomarker
      - relation_type: prov:hadPrimarySource
        source: opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: ubkg
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
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: rtx-kg2
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
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: rtx-kg2
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
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: rtx-kg2
  - category: GraphicalInterface
    description: A browser interface for a knowledge graph for Alzheimer's Disease.
    format: http
    id: alzkb.browser
    name: AlzKB Graph Database Browser
    original_source:
      - relation_type: prov:hadPrimarySource
        source: aop-db
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: dsstox
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: hrpimp
      - relation_type: prov:hadPrimarySource
        source: lincs-l1000
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: pharmacotherapydb
      - relation_type: prov:hadPrimarySource
        source: pid
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: wikipathways
    product_url: https://alzkb.ai:7473/login
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: alzkb
      - relation_type: prov:wasInfluencedBy
        source: hetionet
  - category: GraphProduct
    description: Memgraph data release for AlzKB.
    id: alzkb.data
    name: AlzKB Data Release (Version 2.0.0)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: aop-db
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: dsstox
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: hrpimp
      - relation_type: prov:hadPrimarySource
        source: lincs-l1000
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: pharmacotherapydb
      - relation_type: prov:hadPrimarySource
        source: pid
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: wikipathways
    product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: alzkb
      - relation_type: prov:wasInfluencedBy
        source: hetionet
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: loinc
      - relation_type: prov:hadPrimarySource
        source: icd10
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: obi
      - relation_type: prov:hadPrimarySource
        source: obib
      - relation_type: prov:hadPrimarySource
        source: edam
      - relation_type: prov:hadPrimarySource
        source: hsapdv
      - relation_type: prov:hadPrimarySource
        source: sbo
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: ordo
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: uo
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: pgo
      - relation_type: prov:hadPrimarySource
        source: gencode
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: hra
      - relation_type: prov:hadPrimarySource
        source: hubmap
      - relation_type: prov:hadPrimarySource
        source: sennet
      - relation_type: prov:hadPrimarySource
        source: stellar
      - relation_type: prov:hadPrimarySource
        source: dct
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: connectivitymap
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: msigdb
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: 4dn
      - relation_type: prov:hadPrimarySource
        source: erccrbp
      - relation_type: prov:hadPrimarySource
        source: erccreg
      - relation_type: prov:hadPrimarySource
        source: faldo
      - relation_type: prov:hadPrimarySource
        source: glycordf
      - relation_type: prov:hadPrimarySource
        source: glycocoo
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: kidsfirst
      - relation_type: prov:hadPrimarySource
        source: lincs
      - relation_type: prov:hadPrimarySource
        source: motrpac
      - relation_type: prov:hadPrimarySource
        source: mw
      - relation_type: prov:hadPrimarySource
        source: npo
      - relation_type: prov:hadPrimarySource
        source: sckan
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: biomarker
      - relation_type: prov:hadPrimarySource
        source: opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: ubkg
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: cosmic
      - relation_type: prov:hadPrimarySource
        source: achilles
      - relation_type: prov:hadPrimarySource
        source: depmap
      - relation_type: prov:hadPrimarySource
        source: ccle
      - relation_type: prov:hadPrimarySource
        source: gdsc
      - relation_type: prov:hadPrimarySource
        source: cellosaurus
      - relation_type: prov:hadPrimarySource
        source: clue
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: pharmacodb
      - relation_type: prov:hadPrimarySource
        source: prism
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: lincs
      - relation_type: prov:hadPrimarySource
        source: compartments
      - relation_type: prov:hadPrimarySource
        source: offsides
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: drugcentral
      - relation_type: prov:hadPrimarySource
        source: repohub
      - relation_type: prov:hadPrimarySource
        source: chemicalchecker
      - relation_type: prov:hadPrimarySource
        source: repodb
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: opentargets
      - relation_type: prov:hadPrimarySource
        source: creeds
      - relation_type: prov:hadPrimarySource
        source: interpro
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: dorothea
      - relation_type: prov:hadPrimarySource
        source: progeny
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: huri
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: omnipath
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: bto
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: bioteque
  - category: ProcessProduct
    description: INDRA CoGEx is a graph database integrating causal relations, ontological relations, properties, and data, assembled at scale automatically from the scientific literature and structured sources. This is the code to build the graph.
    id: indra.cogex.code
    name: INDRA CoGEx Build Code
    original_source:
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: nihreporter
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: cellmarker
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: ccle
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: indra
    product_url: https://github.com/gyorilab/indra_cogex
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: indra
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: GraphProduct
    description: PheKnowLator graph files, including subsets with and without inverse relations.
    format: owl
    id: pheknowlator.graph
    latest_version: current_build
    name: PheKnowLator graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: pw
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: so
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: vo
      - relation_type: prov:hadPrimarySource
        source: bioportal
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: genemania
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: uniprot
    product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: pheknowlator
    versions:
      - v1.0.0
      - v2.0.0
      - v2.1.0
      - v3.0.2
      - v4.0.0
      - current_build
  - category: Product
    description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB) to better characterize adverse outcomes of toxicological interest that are relevant to human health and the environment. Since its inception, the AOP-DB has been developed with the aim of integrating AOP molecular target information with other publicly available datasets to facilitate computational analyses of AOP information.
    id: aop-db.data
    name: AOP-DB Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: aop-wiki
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: toxcast
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: 1000genomes
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
    product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: aop-db
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: cancer-genome-interpreter.clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: Product
    description: Disease association data integrated from OMIM, MalaCards, ClinVar, Orphanet, DisGeNET and other disease databases
    format: http
    id: genecards.disease.associations
    name: GeneCards Disease Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: omim
      - relation_type: prov:hadPrimarySource
        source: malacards
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: orphanet
      - relation_type: prov:hadPrimarySource
        source: disgenet
    product_url: https://www.genecards.org/
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 403 error when accessing file'
  - category: GraphProduct
    description: Graph database dump and additional relationship files for the Clinical Knowledge Graph.
    format: neo4j
    id: ckg.graph
    name: CKG Graph Database Dump
    original_source:
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: stitch
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: sider
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: phosphositeplus
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: oncokb
      - relation_type: prov:hadPrimarySource
        source: mutationds
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: foodb
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: corum
      - relation_type: prov:hadPrimarySource
        source: cancer-genome-interpreter
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: mod
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: ms
      - relation_type: prov:hadPrimarySource
        source: uo
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
  - authors:
      - Janet Piñero
      - Juan Manuel Ramírez-Anguita
      - Josep Saüch-Pitarch
      - Francesco Ronzano
      - Emilio Centeno
      - Ferran Sanz
      - Laura I. Furlong
    doi: 10.1093/nar/gkz1021
    id: doi:10.1093/nar/gkz1021
    journal: Nucleic Acids Research
    preferred: true
    title: The DisGeNET knowledge platform for disease genomics - 2019 update
    year: '2020'
taxon:
  - NCBITaxon:9606
---

# DisGeNET

DisGeNET is the world's largest and most extensive gene-disease association network, integrating data from numerous expert-curated repositories, GWAS catalogs, animal models, and the scientific literature. It provides a comprehensive resource for investigating the genetic basis of human diseases and facilitates research in genomics, precision medicine, and drug discovery.

## Overview

DisGeNET version 25.1.1 (current as of June 2025) contains:
- 1,982,885 gene-disease associations (GDAs) between 29,460 genes and 42,277 diseases and phenotypes
- 4,397,303 variant-disease associations (VDAs) between 1,425,623 variants and 19,067 diseases and phenotypes
- Over 28 million disease-disease associations (DDAs) based on shared genes and variants
- 14,643 chemicals and drugs associated with GDAs and VDAs
- Over 13 million individual pieces of evidence supporting 6.38 million genotype-phenotype associations
- Evidence supported by 1.6 million scientific publications

## Data Sources

DisGeNET integrates data from multiple types of sources:

### Curated Sources
- Expert-curated databases: UniProt/SwissProt, ClinVar, PsyGeNET, Orphanet, ClinGen
- Model organism databases: Mouse Genome Database (MGD), Rat Genome Database (RGD)

### GWAS & Clinical Studies
- GWAS Catalog
- Phewas Catalog
- UK Biobank (545,400 VDAs between 1,330 clinical endpoints and 213,328 SNPs)
- FinnGen (2.7M VDAs between 2,026 clinical endpoints and 636,644 SNPs)
- Clinical trials data from ClinicalTrials.gov

### Literature-Based Sources
- Text-mined associations from scientific literature on human studies
- Text-mined associations from studies using animal models

## Applications

DisGeNET is designed to support multiple use cases:
- Target identification and validation for drug discovery
- Genomic data interpretation for precision medicine
- Disease mechanism exploration
- Drug repurposing
- Patient stratification
- Biomarker discovery
- Genetic test development

## Access & Availability

DisGeNET offers different access options based on user needs:
- Web platform for searching and exploring data
- API for programmatic access (requires registration)
- R package (disgenet2r) for data analysis within R
- Integration with multiple knowledge graphs like UBKG and RTX-KG2

Access to DisGeNET is tiered, with different plans available for academic researchers (free) and commercial users. The academic plan provides access to curated resources, while more comprehensive plans include text-mined data, drug/chemical annotations, and API access.
