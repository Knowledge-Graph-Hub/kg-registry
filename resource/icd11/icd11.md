---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: ICD-11 is the eleventh revision of the International Classification of
  Diseases and serves as the World Health Organization's global standard for diagnostic
  health information.
domains:
- clinical
homepage_url: https://icd.who.int/en
id: icd11
last_modified_date: '2026-05-20T00:00:00Z'
layout: resource_detail
name: ICD-11
products:
- category: Product
  description: icd11 Nodes TSV
  format: tsv
  id: obo-db-ingest.icd11.tsv
  license:
    id: https://creativecommons.org/licenses/by-nc-nd/3.0/igo/deed.en
    label: CC-BY-ND-3.0-IGO
  name: icd11 Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 4174868
  product_url: https://w3id.org/biopragmatics/resources/icd11/icd11.tsv
- category: GraphicalInterface
  description: Main Raras portal for searching rare diseases, symptoms, genes, and
    patient communities
  format: http
  id: raras.portal
  name: Raras Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: raras
  - relation_type: prov:wasInformedBy
    source: mondo
  - relation_type: prov:wasInformedBy
    source: omim
  - relation_type: prov:wasInformedBy
    source: orphanet
  - relation_type: prov:wasInformedBy
    source: icd10
  - relation_type: prov:wasInformedBy
    source: icd11
  - relation_type: prov:wasInformedBy
    source: wikidata
  - relation_type: prov:wasInformedBy
    source: clinvar
  product_url: https://raras.org/
- category: GraphicalInterface
  description: Rare disease encyclopedia for browsing disease families, disease records,
    and related knowledge graph content
  format: http
  id: raras.encyclopedia
  name: Raras Encyclopedia
  original_source:
  - relation_type: prov:hadPrimarySource
    source: raras
  - relation_type: prov:wasInformedBy
    source: mondo
  - relation_type: prov:wasInformedBy
    source: omim
  - relation_type: prov:wasInformedBy
    source: orphanet
  - relation_type: prov:wasInformedBy
    source: icd10
  - relation_type: prov:wasInformedBy
    source: icd11
  - relation_type: prov:wasInformedBy
    source: wikidata
  - relation_type: prov:wasInformedBy
    source: clinvar
  product_url: https://raras.org/explorar
---
# ICD-11

ICD-11 is the WHO-maintained disease classification used for coding, reporting, analytics, and interoperability across health systems.