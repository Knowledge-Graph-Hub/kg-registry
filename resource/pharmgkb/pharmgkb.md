---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: feedback@pharmgkb.org
  label: PharmGKB
description: PharmGKB collects, curates and disseminates knowledge about clinically actionable gene-drug associations and genotype-phenotype relationships.
domains:
- health
- chemistry and biochemistry
homepage_url: https://www.pharmgkb.org/
id: pharmgkb
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: PharmGKB
products:
- category: Product
  compression: zip
  description: Clinical annotation summaries
  format: tsv
  id: pharmgkb.clinicalannotations
  name: PharmKB Clinical Annotations
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations.zip
- category: Product
  compression: zip
  description: Level of evidence 1-2 clinical annotation summaries
  format: tsv
  id: pharmgkb.clinicalannotations.loe
  name: PharmKB Clinical Annotations (LOE 1-2)
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations_LOE1-2.zip
- category: Product
  compression: zip
  description: Variant annotation summary
  format: tsv
  id: pharmgkb.variantannotations
  name: PharmKB Variant Annotations
  product_url: https://api.pharmgkb.org/v1/download/file/data/variantAnnotations.zip
- category: Product
  compression: zip
  description: Relationships summarized from PharmGKB annotations
  format: tsv
  id: pharmgkb.relationships
  name: PharmKB Relationships
  product_url: https://api.pharmgkb.org/v1/download/file/data/relationships.zip
- category: Product
  compression: zip
  description: Detailed clinical guideline annotations
  format: json
  id: pharmgkb.guidelineannotations
  name: PharmKB Clinical Guideline Annotations
  product_url: https://api.pharmgkb.org/v1/download/file/data/guidelineAnnotations.json.zip
- category: Product
  compression: zip
  description: Drug label annotations
  format: tsv
  id: pharmgkb.druglabels
  name: PharmKB Drug Label Annotations
  product_url: https://api.pharmgkb.org/v1/download/file/data/drugLabels.zip
- category: Product
  compression: zip
  description: Pathways data in BioPax XML format
  format: xml
  id: pharmgkb.pathways.biopax
  name: PharmKB Pathways (BioPax)
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways-biopax.zip
- category: Product
  compression: zip
  description: Pathways data in TSV format
  format: tsv
  id: pharmgkb.pathways.tsv
  name: PharmKB Pathways (TSV)
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways-tsv.zip
- category: Product
  compression: zip
  description: Pathways data in JSON format
  format: json
  id: pharmgkb.pathways.json
  name: PharmKB Pathways (JSON)
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways.json.zip
- category: Product
  compression: zip
  description: List of variant-drug pairs and level of evidence for all clinical annotations
  format: tsv
  id: pharmgkb.clinicalvariants
  name: PharmKB Clinical Variants
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalVariants.zip
- category: Product
  compression: zip
  description: List of objects that occur in PharmGKB literature annotations and pathways
  format: tsv
  id: pharmgkb.literatureoccurrences
  name: PharmKB Literature Occurrences
  product_url: https://api.pharmgkb.org/v1/download/file/data/occurrences.zip
- category: Product
  compression: zip
  description: Automatically identified possible relationships between variants and drugs from literature
  format: tsv
  id: pharmgkb.automatedannotations
  name: PharmKB Automated Annotations
  product_url: https://api.pharmgkb.org/v1/download/file/data/automated_annotations.zip
- category: Product
  compression: zip
  description: Summary of gene information used by PharmGKB and annotations
  format: tsv
  id: pharmgkb.genes
  name: PharmKB Genes
  product_url: https://api.pharmgkb.org/v1/download/file/data/genes.zip
- category: Product
  compression: zip
  description: Summary of variants annotated by PharmGKB that have been tracked in dbSNP
  format: tsv
  id: pharmgkb.variants
  name: PharmKB Variants
  product_url: https://api.pharmgkb.org/v1/download/file/data/variants.zip
- category: Product
  compression: zip
  description: Summaries of drug information annotated by PharmGKB
  format: tsv
  id: pharmgkb.drugs
  name: PharmKB Drugs
  product_url: https://api.pharmgkb.org/v1/download/file/data/drugs.zip
- category: Product
  compression: zip
  description: Summaries of chemical information annotated by PharmGKB
  format: tsv
  id: pharmgkb.chemicals
  name: PharmKB Chemicals
  product_url: https://api.pharmgkb.org/v1/download/file/data/chemicals.zip
- category: Product
  compression: zip
  description: Summary of disease and other phenotypes annotated by PharmGKB
  format: tsv
  id: pharmgkb.phenotypes
  name: PharmKB Phenotypes
  product_url: https://api.pharmgkb.org/v1/download/file/data/phenotypes.zip
- category: Product
  compression: csv
  description: Archive of papers of interest from May 2006 to April 2017
  format: csv
  id: pharmgkb.papers
  name: PharmKB Papers of Interest Archive
  product_url: https://api.pharmgkb.org/v1/download/file/attachment/PapersOfInterestArchive.csv
- category: Product
  compression: zip
  description: Haplotype frequencies from UK Biobank dataset using PharmCAT
  format: tsv
  id: pharmgkb.haplotypefrequencies.ukbb
  name: PharmKB UK Biobank Frequencies
  product_url: https://api.pharmgkb.org/v1/download/file/data/pharmgkb_haplotype_frequencies_UKBB.zip
- category: Product
  compression: zip
  description: Haplotype, phenotype, and activity score frequencies from AllOfUs dataset using PharmCAT
  format: tsv
  id: pharmgkb.haplotypefrequencies.allofus
  name: PharmKB AllOfUs Biobank Frequencies
  product_url: https://api.pharmgkb.org/v1/download/file/data/pharmgkb_haplotype_frequencies_AllOfUs.zip
repository: https://www.pharmgkb.org/downloads
---
PharmGKB