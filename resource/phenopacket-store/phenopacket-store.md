---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://monarchinitiative.org/
  label: Monarch Initiative
creation_date: '2026-06-18T00:00:00Z'
description: Phenopacket Store is a curated collection of GA4GH Phenopackets describing
  individuals with rare and Mendelian disease, assembled from the medical literature
  by the Monarch Initiative and GA4GH community. Each phenopacket captures a case's
  observed and excluded phenotypic features encoded with the Human Phenotype Ontology
  (HPO), along with the underlying genetic variants and disease diagnosis. The collection
  provides standardized, machine-readable case data used to power phenotype-driven
  analyses such as genotype-phenotype correlation studies and diagnostic tool benchmarking.
domains:
- phenotype
- clinical
- genomics
- precision medicine
homepage_url: https://github.com/monarch-initiative/phenopacket-store
id: phenopacket-store
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/BSD-3-Clause
  label: BSD-3-Clause
name: Phenopacket Store
products:
- category: Product
  description: Versioned release of the Phenopacket Store collection of GA4GH phenopackets
    for rare and Mendelian disease cases, archived on Zenodo.
  format: json
  id: phenopacket-store.release
  name: Phenopacket Store Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_url: https://doi.org/10.5281/zenodo.13168726
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
repository: https://github.com/monarch-initiative/phenopacket-store
---
Phenopacket Store is a curated collection of GA4GH Phenopackets describing
individuals with rare and Mendelian disease, assembled from the published medical
literature by the Monarch Initiative and the broader GA4GH community. Each
phenopacket records a case's observed and excluded phenotypic features encoded
with the Human Phenotype Ontology (HPO), together with the causal genetic
variants and the disease diagnosis.

The collection provides standardized, machine-readable case data that power
phenotype-driven analyses, including genotype-phenotype correlation studies and
the benchmarking of phenotype-driven diagnostic tools. In KG-Registry, Phenopacket
Store serves as an upstream ingest source for the Monarch/SRI Reference Knowledge
Graph. Releases are versioned and archived on Zenodo.