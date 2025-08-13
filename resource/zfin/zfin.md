---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: zfinadmn@zfin.org
  label: Zebrafish Information Network
description: Zebrafish Information Network, including the Zebrafish Anatomical Ontology
domains:
- biological systems
homepage_url: https://zfin.org/
id: zfin
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: ZFIN
products:
- category: Product
  description: Zebrafish Anatomical Ontology (OWL)
  id: zfin.zfa
  license:
    id: https://creativecommons.org/licenses/by/3.0/
    label: CC-BY-3.0
  name: ZFA
  original_source:
  - zfin
  product_file_size: 401588
  product_url: http://purl.obolibrary.org/obo/zfa.owl
  secondary_source:
  - zfin
- category: Product
  description: zfin OBO
  id: obo-db-ingest.zfin.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OBO
  original_source:
  - zfin
  product_file_size: 2643947
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: zfin OWL
  id: obo-db-ingest.zfin.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OWL
  original_source:
  - zfin
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.owl
  secondary_source:
  - obo-db-ingest
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: HTTP 404 error
    when accessing file'
- category: Product
  description: zfin OBO Graph JSON
  id: obo-db-ingest.zfin.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OBO Graph JSON
  original_source:
  - zfin
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.json
  secondary_source:
  - obo-db-ingest
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-12: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: HTTP 404 error
    when accessing file'
- category: MappingProduct
  description: zfin SSSOM
  id: obo-db-ingest.zfin.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin SSSOM
  original_source:
  - zfin
  product_file_size: 374627
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: Phenotype of Zebrafish Genes
  format: tsv
  id: zfin.gene-to-phenotype
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: ZFIN clean gene to phenotype
  original_source:
  - zfin
  product_file_size: 42545110
  product_url: https://zfin.org/downloads/phenoGeneCleanData_fish.txt
  secondary_source:
  - zfin
- category: Product
  description: Phenotype of Zebrafish Genes
  format: tsv
  id: zfin.gene-to-publication
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: ZFIN gene to publication
  original_source:
  - zfin
  product_file_size: 39531152
  product_url: https://zfin.org/downloads/gene_publication.txt
  secondary_source:
  - zfin
repository: https://github.com/ZFIN/
---
ZFIN