---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: hgnc@genenames.org
  label: HUGO Gene Nomenclature Committee
description: HGNC is the HUGO Gene Nomenclature Committee. It is a resource for approved
  human gene names.
domains:
- biological systems
fairsharing_id: FAIRsharing.amcv1e
homepage_url: https://www.genenames.org/
id: hgnc
infores_id: hgnc
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0-1.0
name: HGNC
products:
- category: Product
  description: HGNC OBO
  format: obo
  id: obo-db-ingest.hgnc.obo
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: HGNC OBO
  original_source:
  - hgnc
  product_file_size: 4253807
  product_url: https://w3id.org/biopragmatics/resources/hgnc/hgnc.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  compression: gzip
  description: HGNC OWL
  format: owl
  id: obo-db-ingest.hgnc.owl
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: HGNC OWL
  original_source:
  - hgnc
  product_file_size: 6489789
  product_url: https://w3id.org/biopragmatics/resources/hgnc/hgnc.owl.gz
  secondary_source:
  - obo-db-ingest
- category: Product
  compression: gzip
  description: HGNC OBO Graph JSON
  format: json
  id: obo-db-ingest.hgnc.json
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: HGNC OBO Graph JSON
  original_source:
  - hgnc
  product_file_size: 4855839
  product_url: https://w3id.org/biopragmatics/resources/hgnc/hgnc.json.gz
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: hgnc SSSOM
  id: obo-db-ingest.hgnc.sssom.tsv
  license:
    id: https://creativecommons.org.publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc SSSOM
  original_source:
  - hgnc
  product_file_size: 1816550
  product_url: https://w3id.org/biopragmatics/resources/hgnc/hgnc.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: hgnc.genegroup OBO
  format: obo
  id: obo-db-ingest.hgnc.genegroup.obo
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc.genegroup OBO
  original_source:
  - hgnc
  product_file_size: 185057
  product_url: https://w3id.org/biopragmatics/resources/hgnc.genegroup/hgnc.genegroup.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: hgnc.genegroup OWL
  format: owl
  id: obo-db-ingest.hgnc.genegroup.owl
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc.genegroup OWL
  original_source:
  - hgnc
  product_file_size: 231939
  product_url: https://w3id.org/biopragmatics/resources/hgnc.genegroup/hgnc.genegroup.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: hgnc.genegroup OBO Graph JSON
  format: json
  id: obo-db-ingest.hgnc.genegroup.json
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc.genegroup OBO Graph JSON
  original_source:
  - hgnc
  product_file_size: 207059
  product_url: https://w3id.org/biopragmatics/resources/hgnc.genegroup/hgnc.genegroup.json
  secondary_source:
  - obo-db-ingest
- category: Product
  compression: zip
  description: This HGNC OWL file is generated from the data at https://www.genenames.org/.
    It contains all genes in HGNC organised in a shallow hierarchy, classified by
    their locus type and gene group. Gene groups are also derived from HGNC. The ontology
    contains approved gene symbol, approved gene name, previous names and symbols
    and mappings to external databases.
  format: owl
  id: scibite.hgnc
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: SciBite HGNC
  original_source:
  - hgnc
  product_url: https://github.com/elsevier-health/scibite-ontology/blob/main/hgnc_2025_02_04.owl.zip
  repository: https://github.com/elsevier-health/scibite-ontology
  secondary_source:
  - scibite
  warnings:
  - File was not able to be retrieved when checked on 2026-01-06_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-06_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-06: HTTP 404 error
    when accessing file'
- category: MappingProduct
  description: MONDO SSSOM. Mappings from MONDO identifiers to other namespaces.
  format: sssom
  id: mondo.sssom
  name: MONDO SSSOM
  original_source:
  - doid
  - hp
  - hgnc
  product_file_size: 1437457
  product_url: https://raw.githubusercontent.com/monarch-initiative/mondo/refs/heads/master/src/ontology/mappings/mondo.sssom.tsv
  secondary_source:
  - mondo
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
  description: HGNC Automat
  format: kgx-jsonl
  id: automat.hgnc
  infores_id: automat-hgnc
  name: hgnc_automat
  original_source:
  - hgnc
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/HGNC_Automat/dee31cfce74e5944/
  secondary_source:
  - automat
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
- category: MappingProduct
  description: Public mapping of MIM numbers to NCBI Gene IDs, Ensembl Gene IDs, and
    HGNC symbols
  format: tsv
  id: omim.mim2gene
  name: OMIM mim2gene.txt
  original_source:
  - omim
  - ncbigene
  - ensembl
  - hgnc
  product_file_size: 974440
  product_url: https://www.omim.org/static/omim/data/mim2gene.txt
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
- category: GraphicalInterface
  description: Web portal for searching and browsing ncRNA sequences, structures,
    and annotations
  format: http
  id: rnacentral.portal
  name: RNAcentral Portal
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to RNAcentral data
  format: http
  id: rnacentral.api
  name: RNAcentral REST API
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/api
- category: Product
  description: FTP archive with current and archived release files (sequences and
    annotations)
  format: http
  id: rnacentral.ftp
  name: RNAcentral FTP Archive
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
- category: DataModelProduct
  description: Public PostgreSQL database for direct SQL access to RNAcentral data
  format: postgres
  id: rnacentral.public-db
  name: RNAcentral Public Postgres Database
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/help/public-database
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
  - File was not able to be retrieved when checked on 2026-01-06_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-06_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-01-06: HTTP 403 error
    when accessing file'
- category: GraphicalInterface
  description: Interactive web interface for exploring and visualizing kinase-substrate
    interactions
  format: http
  id: kinace.portal
  name: KinAce Web Portal
  original_source:
  - phosphositeplus
  - iptmnet
  - uniprot
  - epsd
  - kinhub
  - coralkinome
  - darkkinasekb
  - hgnc
  - kegg
  - interpro
  product_url: https://kinace.kinametrix.com/
  secondary_source:
  - kinace
- category: GraphProduct
  description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing
    and integrating information from diverse biomedical resources including DRKG,
    iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome,
    SIDER, and others).
  id: ibkh.graph
  name: iBKH Knowledge Graph
  original_source:
  - drkg
  - idisk
  - brenda
  - ctd
  - drugbank
  - kegg
  - pharmgkb
  - reactome
  - sider
  - tissues
  - bgee
  - doid
  - uberon
  - cl
  - hgnc
  - chembl
  - chebi
- category: MappingProduct
  compression: zip
  description: A single delimited text file format containing a list of mappings between
    different identifiers stored in BioGRID and the identifiers used in downloads.
  format: tsv
  id: biogrid.identifiers
  latest_version: 5.0.252
  name: BIOGRID-IDENTIFIERS-LATEST.tab.zip
  original_source:
  - biogrid
  - uniprot
  - ncbigene
  - zfin
  - xenbase
  - hgnc
  product_url: https://downloads.thebiogrid.org/File/BioGRID/Latest-Release/BIOGRID-IDENTIFIERS-LATEST.tab.zip
  secondary_source:
  - biogrid
repository: https://github.com/HGNC
taxon:
- NCBITaxon:9606
---
HUGO Gene Nomenclature Committee