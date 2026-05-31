---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: agbase@email.arizona.edu
  label: CGNC
creation_date: '2025-03-24T00:00:00Z'
description: CGNC is the Chicken Gene Nomenclature Consortium. It is  an international
  group of researchers interested in providing standardized gene nomenclature for
  chicken genes.
domains:
- organisms
homepage_url: https://birdgenenames.org/index.jsp
id: cgnc
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: CGNC
products:
- category: GraphicalInterface
  description: Official Chicken Gene Nomenclature Consortium portal for searching
    gene symbols, guidelines, downloads, and curation resources.
  format: http
  id: cgnc.portal
  name: CGNC Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgnc
  product_url: https://birdgenenames.org/index.jsp
- category: Product
  description: CGNC public downloads page for standardized chicken gene nomenclature
    data and related consortium resources.
  format: http
  id: cgnc.genes
  name: CGNC Genes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgnc
  product_url: https://birdgenenames.org/downloads.jsp
- category: Product
  description: cgnc OBO
  format: obo
  id: obo-db-ingest.cgnc.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgnc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 683991
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.obo
- category: Product
  description: cgnc OWL
  format: owl
  id: obo-db-ingest.cgnc.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgnc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 911421
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.owl
- category: Product
  description: cgnc OBO Graph JSON
  format: json
  id: obo-db-ingest.cgnc.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgnc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 861880
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.json
- category: MappingProduct
  description: cgnc SSSOM
  format: sssom
  id: obo-db-ingest.cgnc.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgnc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 258292
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.sssom.tsv
- category: Product
  description: cgnc Nodes TSV
  format: tsv
  id: obo-db-ingest.cgnc.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: cgnc Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cgnc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 406670
  product_url: https://w3id.org/biopragmatics/resources/cgnc/cgnc.tsv
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
# CGNC

The Chicken Gene Nomenclature Consortium (CGNC) coordinates standardized gene
names and symbols for chicken genes so that avian genomic data can be used more
consistently across databases, publications, and comparative genomics workflows.

This page uses the live CGNC portal and downloads page as the owned entry points
for the resource. The OBO-DB-Ingest derivatives remain attached here as
downstream products that re-express CGNC nomenclature data for ontology and
integration workflows.