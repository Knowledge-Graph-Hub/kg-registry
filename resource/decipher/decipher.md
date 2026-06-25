---
activity_status: active
category: DataSource
contacts:
- category: Organization
  homepage_url: https://www.sanger.ac.uk/
  id: wellcome-sanger-institute
  label: Wellcome Sanger Institute
creation_date: '2026-06-18T00:00:00Z'
description: DECIPHER (DatabasE of genomiC varIation and Phenotype in Humans using
  Ensembl Resources) is a web-based platform, hosted at the Wellcome Sanger Institute,
  that aggregates and shares anonymized clinical and genomic data on submicroscopic
  chromosomal imbalances and other genomic variants in patients with rare developmental
  and genetic disorders. It links genomic variants to associated phenotypes (using
  Human Phenotype Ontology terms) to support interpretation of variant pathogenicity
  and clinical diagnosis. DECIPHER integrates Ensembl genome resources and an international
  consortium of clinical genetics centers. It is an upstream data source for the SRI-Reference
  Knowledge Graph and the Monarch Initiative.
domains:
- genomics
- clinical
- phenotype
- precision medicine
homepage_url: https://www.deciphergenomics.org/
id: decipher
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: DECIPHER
products:
- category: GraphicalInterface
  description: DECIPHER web interface for browsing genomic variants, syndromes, and
    associated phenotypes in patients with rare developmental disorders.
  format: http
  id: decipher.web
  name: DECIPHER web platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: decipher
  product_url: https://www.deciphergenomics.org/
- category: Product
  description: DECIPHER downloadable datasets, including aggregated patient variant
    and phenotype data and supporting genomic annotation files.
  format: http
  id: decipher.downloads
  name: DECIPHER downloadable data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: decipher
  product_url: https://www.deciphergenomics.org/about/downloads/data
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
  - Helen V. Firth
  - Shola M. Richards
  - A. Paul Bevan
  - Stephen Clayton
  - Manuel Corpas
  - Diana Rajan
  - Steven Van Vooren
  - Yves Moreau
  - Roger M. Pettett
  - Nigel P. Carter
  doi: 10.1016/j.ajhg.2009.03.010
  id: https://pubmed.ncbi.nlm.nih.gov/19344873/
  journal: Am J Hum Genet
  preferred: true
  title: 'DECIPHER: Database of Chromosomal Imbalance and Phenotype in Humans Using
    Ensembl Resources'
  year: '2009'
---
# DECIPHER

DECIPHER (DatabasE of genomiC varIation and Phenotype in Humans using Ensembl
Resources) is a database and web platform hosted by the Wellcome Sanger Institute
that shares anonymized clinical and genomic data on submicroscopic chromosomal
imbalances and other genomic variants linked to patient phenotypes.

It supports interpretation of variant pathogenicity and clinical diagnosis of rare
developmental disorders, and serves as an upstream data source for the
SRI-Reference Knowledge Graph and the Monarch Initiative.