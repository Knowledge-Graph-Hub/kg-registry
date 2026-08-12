---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://darwinsark.org/
  - contact_type: github
    value: DarwinsArk
  label: Darwin's Ark
creation_date: '2026-08-12T00:00:00Z'
description: A community science project collecting owner-reported behavioral and
  physical survey data alongside whole genome sequence data for pet dogs, and releasing
  the combined dataset openly.
domains:
- genomics
- organisms
- phenotype
homepage_url: https://darwinsark.org/
id: darwins-ark
last_modified_date: '2026-08-12T00:00:00Z'
layout: resource_detail
name: Darwin's Ark
products:
- category: Product
  description: A PLINK binary fileset of genotypes from 3,277 dog whole genomes, with
    sample identifiers matching the dog identifiers used in the Darwin's Ark survey
    data files. Sequencing data are deposited under BioProject PRJNA675863.
  format: mixed
  id: darwins-ark.genotypes
  name: Darwin's Ark dog genotypes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: darwins-ark
  product_url: https://datadryad.org/dataset/doi:10.5061/dryad.83bk3jb4r
- category: Product
  description: Owner-reported survey data covering behavioral and physical traits
    for dogs enrolled in Darwin's Ark, keyed to the same dog identifiers as the genotype
    data.
  format: csv
  id: darwins-ark.surveys
  name: Darwin's Ark survey data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: darwins-ark
  product_url: https://datadryad.org/dataset/doi:10.5061/dryad.83bk3jb4r
- category: GraphicalInterface
  description: The Darwin's Ark website, where owners enroll dogs, complete behavioral
    surveys, and browse project results.
  format: http
  id: darwins-ark.website
  name: Darwin's Ark website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: darwins-ark
  product_url: https://darwinsark.org/
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
  - Kathryn A. Lord
  - Vista Sohrab
  - Kasia Bryc
  - Michelle E. White
  - Brittney Kenney
  - Kathleen Morrill Pirovich
  - Frances L. Chen
  - Elinor K. Karlsson
  doi: doi:10.1073/pnas.2421752122
  id: https://doi.org/10.1073/pnas.2421752122
  journal: Proceedings of the National Academy of Sciences
  preferred: true
  title: Genetic testing predicts appearance but not behavior in dogs
  year: '2025'
repository: https://github.com/DarwinsArk
synonyms:
- Darwin's Dogs
taxon:
- NCBITaxon:9615
---
Darwin's Ark is a community science project that pairs owner-reported survey data on dog behavior and physical traits with whole genome sequence data, and releases the combined dataset openly for reuse. It is run by researchers associated with UMass Chan Medical School and the Broad Institute.

The most recent open release covers genotypes from 3,277 dog whole genomes, distributed as a PLINK binary fileset keyed to the project's survey data, with underlying sequencing deposited under BioProject PRJNA675863.

The associated analysis examined 151 genetic variants that had been marketed as predictors of canine behavior and found that none reliably predicted how an individual dog actually behaves, while variants associated with aesthetic traits that differentiate breeds, such as height, leg length, and ear shape, did show strong associations. Darwin's Ark contributes mixed-breed genomes to the canine variant resources built downstream of it, including CanVAS and the Sniff Atlas.