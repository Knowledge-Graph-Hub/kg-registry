---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: agbase@email.arizona.edu
  label: CGNC
description: CGNC is the Chicken Gene Nomenclature Consortium. It is  an international
  group of researchers interested in providing standardized gene nomenclature for
  chicken genes.
domains:
- organisms
homepage_url: http://birdgenenames.org/cgnc/
id: cgnc
layout: resource_detail
name: CGNC
products:
- category: Product
  description: All CGNC public data, including CGNC ID, Entrez Gene ID, Ensembl Gene
    ID, gene symbol, gene name, gene synonym, curation status and last edit date.
  format: tsv
  id: cgnc.genes
  name: CGNC Genes
  original_source:
  - cgnc
  product_url: http://birdgenenames.org/cgnc/downloads.jsp?file=standard
  secondary_source:
  - cgnc
  warnings:
  - File was not able to be retrieved when checked on 2025-11-25_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-26: HTTP 404 error
    when accessing file'
- category: Product
  description: cgnc OBO
  format: obo
  id: obo-db-ingest.cgnc.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc OBO
  original_source:
  - cgnc
  product_file_size: 683991
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: cgnc OWL
  format: owl
  id: obo-db-ingest.cgnc.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc OWL
  original_source:
  - cgnc
  product_file_size: 911421
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: cgnc OBO Graph JSON
  format: json
  id: obo-db-ingest.cgnc.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc OBO Graph JSON
  original_source:
  - cgnc
  product_file_size: 861880
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.json
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: cgnc SSSOM
  format: sssom
  id: obo-db-ingest.cgnc.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc SSSOM
  original_source:
  - cgnc
  product_file_size: 258292
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.sssom.tsv
  secondary_source:
  - obo-db-ingest
publications:
- authors:
  - Burt DW
  - CarrÎ W
  - Fell M
  - Law AS
  - Antin PB
  - Maglott DR
  - Weber JA
  - Schmidt CJ
  - Burgess SC
  - McCarthy FM
  doi: 10.1186/1471-2164-10-S2-S5
  id: doi:10.1186/1471-2164-10-S2-S5
  title: The Chicken Gene Nomenclature Committee report
  year: '2009'
---
CGNC