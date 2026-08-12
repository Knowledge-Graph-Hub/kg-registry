---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: Brundage-VAIL
  label: David M. Brundage
creation_date: '2026-08-12T00:00:00Z'
description: A harmonized and imputed canine variant atlas, unifying genotypes from
  fifteen previously incomparable dog cohorts into a single set of 9.67 million variants
  on the CanFam4 reference assembly.
domains:
- genomics
- organisms
homepage_url: https://github.com/Brundage-VAIL/CanVAS
id: canvas
last_modified_date: '2026-08-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: CanVAS
products:
- category: Product
  description: The imputed CanVAS genotype set as a PLINK binary fileset, restricted
    to variants with minor allele frequency at or above 1%, in CanFam4 coordinates.
  format: mixed
  id: canvas.imputed
  latest_version: v1
  name: CanVAS imputed genotypes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: canvas
  product_url: https://zenodo.org/records/19186944
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dog10k
  - relation_type: prov:wasDerivedFrom
    source: darwins-ark
- category: Product
  description: The CanVAS backbone genotype set, comprising sites genotyped in at
    least 90% of samples prior to imputation, as a PLINK binary fileset in CanFam4
    coordinates.
  format: mixed
  id: canvas.backbone
  latest_version: v1
  name: CanVAS backbone genotypes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: canvas
  product_url: https://zenodo.org/records/19186944
- category: Product
  description: Sample-level metadata for the CanVAS cohort, including breed assignment
    and contributing study for each dog.
  format: tsv
  id: canvas.metadata
  name: CanVAS sample metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: canvas
  product_url: https://zenodo.org/records/19186944
- category: Product
  compression: gzip
  description: A sites-only VCF of the Sniff Atlas variant catalogue, containing allele
    frequencies for 9,667,790 imputed variants across 14,478 dogs and 188 breeds on
    the CanFam4 assembly, restricted to variants with allele frequency at or above
    1%.
  format: vcf
  id: sniff.atlas-vcf
  latest_version: 1.0.1
  name: Sniff Atlas sites VCF (v1.0.1)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sniff
  product_url: https://zenodo.org/records/20566358
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: canvas
  - relation_type: prov:wasDerivedFrom
    source: dog10k
  - relation_type: prov:wasDerivedFrom
    source: darwins-ark
publications:
- authors:
  - David M. Brundage
  doi: doi:10.64898/2026.04.13.718238
  id: https://doi.org/10.64898/2026.04.13.718238
  journal: bioRxiv
  preferred: true
  title: 'CanVAS: A Harmonized and Imputed Canine Variant Atlas'
  year: '2026'
repository: https://github.com/Brundage-VAIL/CanVAS
taxon:
- NCBITaxon:9615
version: v1
---
CanVAS is a harmonized and imputed canine variant atlas that unifies genotype data from fifteen research cohorts which had previously been incomparable because they used different genotyping arrays and reference genomes.

The atlas covers 15,451 dogs across more than 375 breeds, together with village dog populations and wild canids, and reports 9.67 million variants. Genotypes were harmonized to CanFam4 reference coordinates, standardized for probe identifiers and strand conventions, and imputed against the Dog10K reference panel using Beagle 5.4.

CanVAS supplies the variant layer underlying the Sniff Atlas.