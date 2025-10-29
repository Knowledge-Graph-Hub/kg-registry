---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@uniprot.org
  label: UniProt Consortium
description: UniProt Protein Knowledge Base
domains:
- biological systems
- proteomics
- biomedical
homepage_url: https://www.uniprot.org/
id: uniprot
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
  - uniprot
  product_file_size: 4796343398
  product_url: https://kghub.io/kg-microbe/KGMicrobe-transformed-uniprot-microbes-20240924.tar.gz
  secondary_source:
  - kg-microbe
- category: Product
  compression: gzip
  description: The Reviewed (Swiss-Prot) section of UniProt proteins
  format: kgx
  id: uniprot.swissprot.xml
  name: Reviewed (Swiss-Prot) XML
  original_source:
  - uniprot
  product_file_size: 925893980
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Reviewed (Swiss-Prot) section of UniProt proteins
  format: fasta
  id: uniprot.swissprot.fasta
  name: Reviewed (Swiss-Prot) FASTA
  original_source:
  - uniprot
  product_file_size: 93100075
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Unreviewed (TrEMBL) section of UniProt proteins
  format: xml
  id: uniprot.trembl.xml
  name: Unreviewed (TrEMBL) XML
  original_source:
  - uniprot
  product_file_size: 243378751330
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.xml.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Unreviewed (TrEMBL) section of UniProt proteins
  format: fasta
  id: uniprot.trembl.fasta
  name: Unreviewed (TrEMBL) FASTA
  original_source:
  - uniprot
  product_file_size: 63579343267
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz
  secondary_source:
  - uniprot
- category: Product
  description: Tab-delimited file of systematic ID, primary gene name (where assigned),
    chromosome, product description, UniProtKB accession, all synonyms, and product
    type (protein coding, ncRNA, etc.) for each gene
  format: tsv
  id: pombase.genes-products
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase gene names and products
  original_source:
  - uniprot
  - pombase
  product_url: https://www.pombase.org/data/names_and_identifiers/gene_IDs_names_products.tsv
  secondary_source:
  - pombase
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-10-28_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2025-10-29: No Content-Length
    header found'
- category: MappingProduct
  description: Tab-delimited file with the PomBase systematic identifier for each
    protein-coding gene mapped to the corresponding UniProt accession number
  format: tsv
  id: pombase.to-uniprot
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase to UniProt map
  original_source:
  - uniprot
  - pombase
  product_file_size: 27617
  product_url: https://www.pombase.org/data/names_and_identifiers/PomBase2UniProt.tsv
  secondary_source:
  - pombase
- category: MappingProduct
  description: Mapping between chembl_35 target chembl_ids and UniProt accessions
  id: chembl.map_to_uniprot
  is_public: true
  name: ChEMBL map to UniProt
  original_source:
  - chembl
  - uniprot
  product_file_size: 1012901
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_uniprot_mapping.txt
  secondary_source:
  - chembl
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to UniProt accession numbers
  format: tsv
  id: oma.mapping.uniprot
  name: OMA to UniProt Mapping
  original_source:
  - oma
  - uniprot
  product_url: https://omabrowser.org/oma/current/oma-uniprot.txt.gz
  secondary_source:
  - oma
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-28_ HTTP 502 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-21_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-08-13_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2025-10-29: Timeout connecting
    to URL'
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
  - mesh
  - pid
  - doid
  - diseases
  - drugcentral
  - go
  - gwascatalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_file_size: 376501785
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - clingen
  - clinvar
  - mgd
  - rgd
  - orphanet
  - psygenet
  - uniprot
  - disgenet
  - hp
  - gwascatalog
  - phewascat
  - ukbiobank
  - finngen
  - clinicaltrialsgov
  product_url: https://www.disgenet.com/
  secondary_source:
  - disgenet
- category: MappingProduct
  compression: gzip
  description: Gene to RefSeq/UniProtKB collaboration data providing cross-references
    between gene records and protein databases
  format: tsv
  id: ncbigene.gene_refseq_uniprotkb_collab
  name: Gene RefSeq UniProtKB Collaboration Data
  original_source:
  - refseq
  - ncbigene
  - uniprot
  product_file_size: 1182285769
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_refseq_uniprotkb_collab.gz
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  compatibility:
  - standard: biolink
  compression: zip
  description: Curated mechanistic drug–disease paths comprising the DrugMechDB dataset
    packaged as a downloadable archive.
  dump_format: other
  format: mixed
  id: drugmechdb.graph
  latest_version: 2.0.1
  name: DrugMechDB Graph Dataset
  original_source:
  - go
  - cl
  - mesh
  - chebi
  - drugbank
  - interpro
  - uberon
  - pr
  - ncbitaxon
  - reactome
  - hp
  - uniprot
  product_url: https://doi.org/10.5281/zenodo.8139357
  repository: https://github.com/SuLab/DrugMechDB
  versions:
  - 2.0.1
  - 2.0.0
  - 1.0.2
  - '1.0'
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - cl
  - clo
  - chebi
  - go
  - hp
  - mondo
  - pw
  - pr
  - ro
  - so
  - uberon
  - vo
  - bioportal
  - clinvar
  - ctd
  - disgenet
  - ensembl
  - genemania
  - hgnc
  - hpa
  - ncbigene
  - medgen
  - reactome
  - string
  - uniprot
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  secondary_source:
  - pheknowlator
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
  - biolink
  - chebi
  - ncbitaxon
  - ncbigene
  - mesh
  - pubchem
  - go
  - mondo
  - ncit
  - efo
  - uniprot
  - rhea
  - pr
  - uberon
  - panther
  - hgnc
  - drugbank
  - eupathdb
  product_url: https://multiomics.transltr.io/mbkp
  secondary_source:
  - microbiomekg
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: Product
  description: Integrated gene annotation data aggregated from HGNC, OMIM, Ensembl,
    NCBI Gene, UniProt and other genomic databases
  format: http
  id: genecards.gene.annotations
  name: GeneCards Gene Annotations
  original_source:
  - hgnc
  - omim
  - ensembl
  - ncbigene
  - uniprot
  - refseq
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-28_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-10-29: HTTP 403 error
    when accessing file'
- category: Product
  description: UniProt IDs for all targets in TTD
  format: txt
  id: ttd.uniprot-all
  name: All Target UniProt IDs
  original_source:
  - uniprot
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P2-01-TTD_uniprot_all.txt
  secondary_source:
  - ttd
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
  - 'File was not able to be retrieved when checked on 2025-10-29: Error connecting
    to URL: (''Connection aborted.'', ConnectionResetError(104, ''Connection reset
    by peer''))'
- category: Product
  description: GO annotations for all UniProtKB entries
  format: txt
  id: goa.uniprot
  name: UniProt GOA Annotations
  original_source:
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/'
  - 'File was not able to be retrieved when checked on 2025-10-29: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/'''
- category: Product
  description: GO annotations for human proteins
  format: txt
  id: goa.human
  name: Human GOA Annotations
  original_source:
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/'
  - 'File was not able to be retrieved when checked on 2025-10-29: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/'''
- category: Product
  description: GO annotations for mouse proteins
  format: txt
  id: goa.mouse
  name: Mouse GOA Annotations
  original_source:
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/'
  - 'File was not able to be retrieved when checked on 2025-10-29: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/'''
- category: MappingProduct
  description: Files containing transitive assignments of InterPro matches, UniProtKB
    keywords, subcellular locations, EC numbers, or HAMAP matches to manually-selected
    GO terms
  format: txt
  id: goa.mapping-files
  name: GO Mapping Files
  original_source:
  - interpro
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'
  - 'File was not able to be retrieved when checked on 2025-10-29: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'''
repository: https://www.uniprot.org/help/downloads
---
UniProt Protein Knowledge Base