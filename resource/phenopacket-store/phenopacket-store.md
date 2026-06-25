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
  (HPO), along with the underlying genetic variants and disease diagnosis. The
  collection provides standardized, machine-readable case data used to power
  phenotype-driven analyses such as genotype-phenotype correlation studies and
  diagnostic tool benchmarking.
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
name: "Phenopacket Store"
products:
  - category: Product
    description: Versioned release of the Phenopacket Store collection of GA4GH
      phenopackets for rare and Mendelian disease cases, archived on Zenodo.
    format: json
    id: phenopacket-store.release
    name: Phenopacket Store Release
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phenopacket-store
    product_url: https://doi.org/10.5281/zenodo.13168726
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
