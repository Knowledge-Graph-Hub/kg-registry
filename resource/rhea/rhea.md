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
  - 'File was not able to be retrieved when checked on 2025-08-06: HTTP 404 error
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
  - 'File was not able to be retrieved when checked on 2025-08-06: HTTP 404 error
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