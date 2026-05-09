---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: help@uniprot.org
    id: ebi
    label: UniProt Consortium
creation_date: '2025-03-09T00:00:00Z'
description: UniProt Protein Knowledge Base
domains:
  - biological systems
  - proteomics
  - biomedical
homepage_url: https://www.uniprot.org/
id: uniprot
infores_id: uniprot
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: uniprot
products:
  - category: GraphProduct
    compression: targz
    description: UniProt proteins from microbes, as graph nodes and edges
    format: kgx
    id: kg-microbe.graph.uniprot
    name: KG-Microbe UniProt microbe transform
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 4796343398
    product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-transformed-uniprot-microbes-20240924.tar.gz
    secondary_source:
      - source: kg-microbe
        relation_type: prov:wasInfluencedBy
  - category: Product
    compression: gzip
    description: The Reviewed (Swiss-Prot) section of UniProt proteins
    format: kgx
    id: uniprot.swissprot.xml
    name: Reviewed (Swiss-Prot) XML
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 925893980
    product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz
    secondary_source:
      - source: uniprot
        relation_type: prov:wasInfluencedBy
  - category: Product
    compression: gzip
    description: The Reviewed (Swiss-Prot) section of UniProt proteins
    format: fasta
    id: uniprot.swissprot.fasta
    name: Reviewed (Swiss-Prot) FASTA
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 93100075
    product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
    secondary_source:
      - source: uniprot
        relation_type: prov:wasInfluencedBy
  - category: Product
    compression: gzip
    description: The Unreviewed (TrEMBL) section of UniProt proteins
    format: xml
    id: uniprot.trembl.xml
    name: Unreviewed (TrEMBL) XML
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 243378751330
    product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.xml.gz
    secondary_source:
      - source: uniprot
        relation_type: prov:wasInfluencedBy
  - category: Product
    compression: gzip
    description: The Unreviewed (TrEMBL) section of UniProt proteins
    format: fasta
    id: uniprot.trembl.fasta
    name: Unreviewed (TrEMBL) FASTA
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 63579343267
    product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz
    secondary_source:
      - source: uniprot
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: Tab-delimited file of systematic ID, primary gene name (where assigned), chromosome, product description, UniProtKB accession, all synonyms, and product type (protein coding, ncRNA, etc.) for each gene
    format: tsv
    id: pombase.genes-products
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC-BY-4.0
    name: PomBase gene names and products
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
    product_url: https://www.pombase.org/data/names_and_identifiers/gene_IDs_names_products.tsv
    secondary_source:
      - source: pombase
        relation_type: prov:wasInfluencedBy
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: No Content-Length header found'
      - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length header found
  - category: MappingProduct
    description: Tab-delimited file with the PomBase systematic identifier for each protein-coding gene mapped to the corresponding UniProt accession number
    format: tsv
    id: pombase.to-uniprot
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC-BY-4.0
    name: PomBase to UniProt map
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
    product_file_size: 27617
    product_url: https://www.pombase.org/data/names_and_identifiers/PomBase2UniProt.tsv
    secondary_source:
      - source: pombase
        relation_type: prov:wasInfluencedBy
  - category: MappingProduct
    description: Mapping between chembl_35 target chembl_ids and UniProt accessions
    id: chembl.map_to_uniprot
    is_public: true
    name: ChEMBL map to UniProt
    original_source:
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 1012901
    product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_uniprot_mapping.txt
    secondary_source:
      - source: chembl
        relation_type: prov:wasInfluencedBy
  - category: MappingProduct
    compression: gzip
    description: Mapping of OMA identifiers to UniProt accession numbers
    format: tsv
    id: oma.mapping.uniprot
    name: OMA to UniProt Mapping
    original_source:
      - source: oma
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://omabrowser.org/oma/current/oma-uniprot.txt.gz
    secondary_source:
      - source: oma
        relation_type: prov:wasInfluencedBy
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
      - File was not able to be retrieved when checked on 2026-02-18_ Timeout connecting to URL
      - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when accessing file
      - File was not able to be retrieved when checked on 2026-01-03_ HTTP 502 error when accessing file
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
    description: DisGeNET data, including gene to disease associations and variant to disease associations (requires registration and subscription).
    id: disgenet.data
    name: DisGeNET Data
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: mgd
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: orphanet
        relation_type: prov:hadPrimarySource
      - source: psygenet
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: phewascat
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: finngen
        relation_type: prov:hadPrimarySource
      - source: clinicaltrialsgov
        relation_type: prov:hadPrimarySource
    product_url: https://www.disgenet.com/
    secondary_source:
      - source: disgenet
        relation_type: prov:wasInfluencedBy
  - category: MappingProduct
    compression: gzip
    description: Gene to RefSeq/UniProtKB collaboration data providing cross-references between gene records and protein databases
    format: tsv
    id: ncbigene.gene_refseq_uniprotkb_collab
    name: Gene RefSeq UniProtKB Collaboration Data
    original_source:
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 1182285769
    product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_refseq_uniprotkb_collab.gz
  - category: GraphProduct
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
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
    description: Neo4j database dump of the Clinical Knowledge Graph and additional relationships
    dump_format: neo4j
    edge_count: 220000000
    format: mixed
    id: cancer-genome-interpreter.clinicalkg.graph
    name: CKG Graph Dump
    node_count: 16000000
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: Product
    description: Integrated gene annotation data aggregated from HGNC, OMIM, Ensembl, NCBI Gene, UniProt and other genomic databases
    format: http
    id: genecards.gene.annotations
    name: GeneCards Gene Annotations
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
    product_url: https://www.genecards.org/
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
  - category: Product
    description: UniProt IDs for all targets in TTD
    format: txt
    id: ttd.uniprot-all
    name: All Target UniProt IDs
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P2-01-TTD_uniprot_all.txt
    secondary_source:
      - source: ttd
        relation_type: prov:wasInfluencedBy
    warnings:
      - File was not able to be retrieved when checked on 2025-10-31_ Error connecting to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
  - category: Product
    description: GO annotations for all UniProtKB entries
    format: txt
    id: goa.uniprot
    name: UniProt GOA Annotations
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/
    warnings:
      - File was not able to be retrieved when checked on 2025-11-26_ Error connecting to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/'
  - category: Product
    description: GO annotations for human proteins
    format: txt
    id: goa.human
    name: Human GOA Annotations
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/
    warnings:
      - File was not able to be retrieved when checked on 2025-11-26_ Error connecting to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/'
  - category: Product
    description: GO annotations for mouse proteins
    format: txt
    id: goa.mouse
    name: Mouse GOA Annotations
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/
    warnings:
      - File was not able to be retrieved when checked on 2025-12-04_ Error connecting to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/'
  - category: MappingProduct
    description: Files containing transitive assignments of InterPro matches, UniProtKB keywords, subcellular locations, EC numbers, or HAMAP matches to manually-selected GO terms
    format: txt
    id: goa.mapping-files
    name: GO Mapping Files
    original_source:
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
    product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/
    warnings:
      - File was not able to be retrieved when checked on 2025-11-26_ Error connecting to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'
  - category: GraphicalInterface
    description: Interactive web interface for exploring and visualizing kinase-substrate interactions
    format: http
    id: kinace.portal
    name: KinAce Web Portal
    original_source:
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: iptmnet
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: epsd
        relation_type: prov:hadPrimarySource
      - source: kinhub
        relation_type: prov:hadPrimarySource
      - source: coralkinome
        relation_type: prov:hadPrimarySource
      - source: darkkinasekb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
    product_url: https://kinace.kinametrix.com/
    secondary_source:
      - source: kinace
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
  - category: MappingProduct
    compression: zip
    description: A single delimited text file format containing a list of mappings between different identifiers stored in BioGRID and the identifiers used in downloads.
    format: tsv
    id: biogrid.identifiers
    latest_version: 5.0.252
    name: BIOGRID-IDENTIFIERS-LATEST.tab.zip
    original_source:
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
    product_url: https://downloads.thebiogrid.org/File/BioGRID/Latest-Release/BIOGRID-IDENTIFIERS-LATEST.tab.zip
    secondary_source:
      - source: biogrid
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Core UniBioMap graph edges file.
    format: csv
    id: unibiomap.links
    name: UniBioMap Graph Links
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 1406201678
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
  - category: GraphProduct
    description: Auxiliary UniBioMap graph annotations and metadata.
    format: tsv
    id: unibiomap.auxs
    name: UniBioMap Graph Auxiliaries
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 591290539
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
  - category: GraphProduct
    description: Predicted UniBioMap graph edges with confidence scores.
    format: csv
    id: unibiomap.pred
    name: UniBioMap Predicted Graph
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 2484982268
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
  - category: GraphProduct
    description: Full unfiltered UniBioMap predicted graph edges file.
    format: csv
    id: unibiomap.pred.full
    name: UniBioMap Predicted Graph (Full)
    original_source:
      - source: unibiomap
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: tcdb
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: batman
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: compath
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
    product_file_size: 6303875907
    product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
  - category: GraphProduct
    compression: gzip
    description: protein network data (full network, scored links between proteins)
    format: txt
    id: string.protein.links
    name: STRING Protein Links
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 138154280240
    product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: protein network data (full network, incl. subscores per channel)
    format: txt
    id: string.protein.links.detailed
    name: STRING Protein Links Detailed
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 203534412387
    product_url: https://stringdb-downloads.org/download/protein.links.detailed.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: 'protein network data (full network, incl. distinction: direct vs. interologs)'
    format: txt
    id: string.protein.links.full
    name: STRING Protein Links Full
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 214269334954
    product_url: https://stringdb-downloads.org/download/protein.links.full.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: protein network data (physical subnetwork, scored links between proteins)
    format: txt
    id: string.protein.physical.links
    name: STRING Protein Physical Links
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 11867396121
    product_url: https://stringdb-downloads.org/download/protein.physical.links.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: protein network data (physical subnetwork, incl. subscores per channel)
    format: txt
    id: string.protein.physical.links.detailed
    name: STRING Protein Physical Links Detailed
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 14859366689
    product_url: https://stringdb-downloads.org/download/protein.physical.links.detailed.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: 'protein network data (physical subnetwork, incl. distinction: direct vs. interologs)'
    format: txt
    id: string.protein.physical.links.full
    name: STRING Protein Physical Links Full
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 15528028374
    product_url: https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: association scores between orthologous groups
    format: txt
    id: string.cog.links
    name: STRING COG Links
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 185338269
    product_url: https://stringdb-downloads.org/download/COG.links.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: association scores (incl. subscores per channel)
    format: txt
    id: string.cog.links.detailed
    name: STRING COG Links Detailed
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 250279091
    product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
  - category: GraphProduct
    compression: gzip
    description: 'full database, part II: the networks (nodes, edges, scores,...)'
    id: string.database
    name: STRING Database Network Schema
    original_source:
      - source: biocyc
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: cog
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: dip
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: eggnog
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hprd
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: mint
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pdb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: pubmedcentral
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: simap
        relation_type: prov:hadPrimarySource
      - source: smart
        relation_type: prov:hadPrimarySource
      - source: swissmodel
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: progenomes
        relation_type: prov:hadPrimarySource
    product_file_size: 281505096430
    product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
  - category: GraphProduct
    description: ProteomeHD data files
    id: proteomehd.data
    name: ProteomeHD Data
    original_source:
      - source: proteomehd
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: goa
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/Rappsilber-Laboratory/ProteomeHD/tree/master/Data
  - category: Product
    description: TSV export of lipid-related enzymes with UniProt, Rhea, and evidence links.
    format: tsv
    id: swisslipid.enzymes
    name: SwissLipids Enzymes
    original_source:
      - source: swisslipid
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
    product_file_size: 126760
    product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=enzymes.tsv
  - category: MappingProduct
    description: TSV mapping between SwissLipids lipid entries and UniProtKB proteins.
    format: tsv
    id: swisslipid.lipids2uniprot
    name: SwissLipids Lipids to UniProt
    original_source:
      - source: swisslipid
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 37147786
    product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids2uniprot.tsv
  - category: Product
    description: uniprot Nodes TSV
    format: tsv
    id: obo-db-ingest.uniprot.tsv
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC-BY-4.0
    name: uniprot Nodes TSV
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 3801999
    product_url: https://w3id.org/biopragmatics/resources/uniprot/uniprot.tsv
    secondary_source:
      - source: obo-db-ingest
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: uniprot.ptm Nodes TSV
    format: tsv
    id: obo-db-ingest.uniprot.ptm.tsv
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC-BY-4.0
    name: uniprot.ptm Nodes TSV
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 6660
    product_url: https://w3id.org/biopragmatics/resources/uniprot.ptm/uniprot.ptm.tsv
    secondary_source:
      - source: obo-db-ingest
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Graph database dump and additional relationship files for the Clinical Knowledge Graph.
    format: neo4j
    id: ckg.graph
    name: CKG Graph Database Dump
    original_source:
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
repository: https://www.uniprot.org/help/downloads
taxon:
  - NCBITaxon:9606
  - NCBITaxon:10090
  - NCBITaxon:10116
  - NCBITaxon:7227
  - NCBITaxon:6239
  - NCBITaxon:7955
  - NCBITaxon:4932
  - NCBITaxon:3702
---

UniProt Protein Knowledge Base
