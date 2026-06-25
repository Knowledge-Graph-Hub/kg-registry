---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: Mutant Mouse Resource and Research Centers
  contact_details:
  - contact_type: url
    value: https://www.mmrrc.org/about/mmrrcContacts.php
creation_date: '2026-06-18T00:00:00Z'
description: >-
  The Mutant Mouse Resource and Research Centers (MMRRC) is the NIH-funded
  national public repository and distribution archive of genetically engineered
  and mutant laboratory mouse strains in the United States. It maintains live
  mice, cryopreserved embryos and sperm, embryonic stem cell lines, and
  hybridomas for tens of thousands of alleles, together with associated genotype
  and phenotype data. The MMRRC consortium comprises regionally distributed
  vivaria and an Informatics Coordination and Service Center, and its strain
  catalog and phenotype annotations serve as an upstream source for integrative
  knowledge graphs such as Monarch and the NCATS SRI Reference KG.
domains:
- organisms
- genomics
- phenotype
- biomedical
homepage_url: https://www.mmrrc.org/
id: mmrrc
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: "Mutant Mouse Resource and Research Centers"
products:
- category: Database
  description: Searchable online catalog of MMRRC mouse strains, including allele,
    gene, mutation type, phenotype (MPT), and associated publication information.
  format: http
  id: mmrrc.catalog
  name: MMRRC Strain Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  product_url: https://www.mmrrc.org/catalog/StrainCatalogSearchForm.php
- category: Dataset
  description: Bulk data download of the MMRRC strain catalog, providing strain
    identifiers, designations, genes, mutations, phenotype (MPT) annotations, and
    linked PubMed identifiers.
  format: mixed
  id: mmrrc.data-download
  name: MMRRC Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  product_url: https://www.mmrrc.org/about/data_download.php
- category: ProgrammingInterface
  description: MMRRC API providing programmatic access to strain catalog records
    and associated metadata for developers.
  format: http
  id: mmrrc.api
  name: MMRRC API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  product_url: https://www.mmrrc.org/methods/mmrrc_api.php
publications:
- authors:
  - Yuksel Agca
  - James Amos-Landgraf
  - Renee Araiza
  - Jennifer Brennan
  - Charisse Carlson
  - Dominic Ciavatta
  - Dave Clary
  - Craig Franklin
  - Ian Korf
  - Cathleen Lutz
  - Terry Magnuson
  - Fernando Pardo-Manuel de Villena
  - Oleg Mirochnitchenko
  - Samit Patel
  - Dan Port
  - Laura Reinholdt
  - K. C. Kent Lloyd
  doi: 10.1007/s00335-024-10070-3
  id: https://pubmed.ncbi.nlm.nih.gov/39304538/
  journal: Mamm Genome
  preferred: true
  title: 'The mutant mouse resource and research center (MMRRC) consortium: the
    US-based public mouse repository system'
  year: '2024'
---
# Mutant Mouse Resource and Research Centers

The Mutant Mouse Resource and Research Centers (MMRRC) is the NIH-funded
national public repository and distribution archive of genetically engineered
and mutant laboratory mouse strains in the United States. It maintains live
mice, cryopreserved embryos and sperm, embryonic stem cell lines, and
hybridomas for tens of thousands of alleles, together with associated genotype
and phenotype data.

The MMRRC consortium comprises regionally distributed vivaria and an
Informatics Coordination and Service Center. Its strain catalog and phenotype
(MPT) annotations are accessible through a searchable web catalog, bulk data
downloads, and a developer API, and serve as an upstream source for integrative
knowledge graphs such as Monarch and the NCATS SRI Reference KG.
