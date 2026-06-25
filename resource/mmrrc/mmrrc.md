---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.mmrrc.org/about/mmrrcContacts.php
  label: Mutant Mouse Resource and Research Centers
creation_date: '2026-06-18T00:00:00Z'
description: The Mutant Mouse Resource and Research Centers (MMRRC) is the NIH-funded
  national public repository and distribution archive of genetically engineered and
  mutant laboratory mouse strains in the United States. It maintains live mice, cryopreserved
  embryos and sperm, embryonic stem cell lines, and hybridomas for tens of thousands
  of alleles, together with associated genotype and phenotype data. The MMRRC consortium
  comprises regionally distributed vivaria and an Informatics Coordination and Service
  Center, and its strain catalog and phenotype annotations serve as an upstream source
  for integrative knowledge graphs such as Monarch and the NCATS SRI Reference KG.
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
name: Mutant Mouse Resource and Research Centers
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
  description: Bulk data download of the MMRRC strain catalog, providing strain identifiers,
    designations, genes, mutations, phenotype (MPT) annotations, and linked PubMed
    identifiers.
  format: mixed
  id: mmrrc.data-download
  name: MMRRC Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  product_url: https://www.mmrrc.org/about/data_download.php
- category: ProgrammingInterface
  description: MMRRC API providing programmatic access to strain catalog records and
    associated metadata for developers.
  format: http
  id: mmrrc.api
  name: MMRRC API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  product_url: https://www.mmrrc.org/methods/mmrrc_api.php
- category: GraphProduct
  description: KGX distribution of the SRI-Reference KG
  format: kgx
  id: sri-reference-kg.graph
  name: SRI-Reference KG (KGX distribution)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sri-reference-kg
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: wormbase
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ddanat
  - relation_type: prov:hadPrimarySource
    source: ddpheno
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dpo
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: fypo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: wbbt
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: wbphenotype
  - relation_type: prov:hadPrimarySource
    source: xao
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: zfa
  - relation_type: prov:hadPrimarySource
    source: zfs
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: decipher
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  - relation_type: prov:hadPrimarySource
    source: cureid
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_file_size: 230046094
  product_url: https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.tar.gz
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
  title: 'The mutant mouse resource and research center (MMRRC) consortium: the US-based
    public mouse repository system'
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