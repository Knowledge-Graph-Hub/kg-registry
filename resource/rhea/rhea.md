---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: Rhea Team
description: Rhea is an expert-curated knowledgebase of chemical and transport reactions
  of biological interest.
domains:
- chemistry and biochemistry
homepage_url: https://www.rhea-db.org/
id: rhea
infores_id: rhea
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Rhea
products:
- category: Product
  description: rhea OBO
  format: obo
  id: obo-db-ingest.rhea.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea OBO
  original_source:
  - rhea
  product_file_size: 4826502
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: rhea OWL
  format: owl
  id: obo-db-ingest.rhea.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea OWL
  original_source:
  - rhea
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.owl
  secondary_source:
  - obo-db-ingest
  warnings:
  - File was not able to be retrieved when checked on 2025-12-08_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-07_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-09-11_ Error connecting
    to URL_ HTTPSConnectionPool(host='w3id.org', port=443)_ Max retries exceeded with
    url_ /biopragmatics/resources/rhea/rhea.owl (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7fa35c761be0>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - File was not able to be retrieved when checked on 2025-09-11_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2025-12-08: HTTP 404 error
    when accessing file'
- category: Product
  description: rhea OBO Graph JSON
  format: json
  id: obo-db-ingest.rhea.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea OBO Graph JSON
  original_source:
  - rhea
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.json
  secondary_source:
  - obo-db-ingest
  warnings:
  - File was not able to be retrieved when checked on 2025-12-08_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-07_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-09-11_ Error connecting
    to URL_ HTTPSConnectionPool(host='w3id.org', port=443)_ Max retries exceeded with
    url_ /biopragmatics/resources/rhea/rhea.json (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection
    object at 0x7fa35c7716d0>_ Failed to establish a new connection_ [Errno 101] Network
    is unreachable'))
  - File was not able to be retrieved when checked on 2025-09-11_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2025-12-08: HTTP 404 error
    when accessing file'
- category: MappingProduct
  description: Rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: Rhea SSSOM
  original_source:
  - rhea
  - reactome
  - kegg
  - metacyc
  - m-csa
  - ecocyc
  product_file_size: 154171
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
  secondary_source:
  - obo-db-ingest
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
  compression: targz
  description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
  format: kgx
  id: kg-microbe.graph.raw
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: KG-Microbe KGX Graph - Raw
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 12464495186
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-raw-20250222.tar.gz
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 4623010863
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-function-20250222.tar.gz
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 4640682152
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
  secondary_source:
  - kg-microbe
publications:
- authors:
  - Bansal P
  - Morgat A
  - Axelsen KB
  - Muthukrishnan V
  - Coudert E
  - Aimo L
  - Hyka-Nouspikel N
  - Gasteiger E
  - Kerhornou A
  - Neto TB
  - Pozzato M
  - Blatter MC
  - Ignatchenko A
  - Redaschi N
  - Bridge A
  doi: doi:10.1093/nar/gkab1016
  id: doi:10.1093/nar/gkab1016
  preferred: true
  title: Rhea, the reaction knowledgebase in 2022
  year: '2021'
---
Rhea is an expert-curated knowledgebase of chemical and transport reactions of biological interest. Enzyme-catalyzed and spontaneously occurring reactions are curated from peer-reviewed literature and represented in a computationally tractable manner by using the ChEBI (Chemical Entities of Biological Interest) ontology to describe reaction participants.

Rhea covers the reactions described by the IUBMB Enzyme Nomenclature as well as many additional reactions and can be used for enzyme annotation, genome-scale metabolic modeling and omics-related analyses. Rhea is the standard for enzyme and transporter annotation in UniProtKB.