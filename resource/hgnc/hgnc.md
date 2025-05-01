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
  description: hgnc OBO
  format: obo
  id: obo-db-ingest.hgnc.obo
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc OBO
  original_source:
  - hgnc
  product_url: https://w3id.org/biopragmatics/resources/hgnc/hgnc.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: hgnc OWL
  format: owl
  id: obo-db-ingest.hgnc.owl
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc OWL
  original_source:
  - hgnc
  product_url: https://w3id.org/biopragmatics/resources/hgnc/hgnc.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: hgnc OBO Graph JSON
  format: json
  id: obo-db-ingest.hgnc.json
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc OBO Graph JSON
  original_source:
  - hgnc
  product_url: https://w3id.org/biopragmatics/resources/hgnc/hgnc.json
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: hgnc SSSOM
  id: obo-db-ingest.hgnc.sssom.tsv
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc SSSOM
  original_source:
  - hgnc
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
- category: MappingProduct
  description: MONDO SSSOM. Mappings from MONDO identifiers to other namespaces.
  format: sssom
  id: mondo.sssom
  name: MONDO SSSOM
  original_source:
  - do
  - hp
  - hgnc
  product_url: https://raw.githubusercontent.com/monarch-initiative/mondo/refs/heads/master/src/ontology/mappings/mondo.sssom.tsv
  secondary_source:
  - mondo
- category: MappingProduct
  description: hgnc SSSOM
  id: obo-db-ingest.hgnc.sssom.tsv
  license:
    id: https://creativecommons.org.publicdomain/zero/1.0/
    label: CC0-1.0
  name: hgnc SSSOM
  original_source:
  - hgnc
  product_url: https://w3id.org/biopragmatics/resources/hgnc/hgnc.sssom.tsv
  secondary_source:
  - obo-db-ingest
repository: https://github.com/HGNC
---
HUGO Gene Nomenclature Committee