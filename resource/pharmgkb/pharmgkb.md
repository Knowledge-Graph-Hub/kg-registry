---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: feedback@pharmgkb.org
  label: PharmGKB
description: PharmGKB collects, curates and disseminates knowledge about clinically
  actionable gene-drug associations and genotype-phenotype relationships.
domains:
- health
- chemistry and biochemistry
- pharmacology
- genomics
- precision medicine
homepage_url: https://www.pharmgkb.org/
id: pharmgkb
infores_id: pharmgkb
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
  product_file_size: 1231768
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations.zip
- category: Product
  compression: zip
  description: Level of evidence 1-2 clinical annotation summaries
  format: tsv
  id: pharmgkb.clinicalannotations.loe
  name: PharmKB Clinical Annotations (LOE 1-2)
  product_file_size: 271314
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations_LOE1-2.zip
- category: Product
  compression: zip
  description: Variant annotation summary
  format: tsv
  id: pharmgkb.variantannotations
  name: PharmKB Variant Annotations
  product_file_size: 4071535
  product_url: https://api.pharmgkb.org/v1/download/file/data/variantAnnotations.zip
- category: Product
  compression: zip
  description: Relationships summarized from PharmGKB annotations
  format: tsv
  id: pharmgkb.relationships
  name: PharmKB Relationships
  product_file_size: 1261136
  product_url: https://api.pharmgkb.org/v1/download/file/data/relationships.zip
- category: Product
  compression: zip
  description: Detailed clinical guideline annotations
  format: json
  id: pharmgkb.guidelineannotations
  name: PharmKB Clinical Guideline Annotations
  product_file_size: 811786
  product_url: https://api.pharmgkb.org/v1/download/file/data/guidelineAnnotations.json.zip
- category: Product
  compression: zip
  description: Drug label annotations
  format: tsv
  id: pharmgkb.druglabels
  name: PharmKB Drug Label Annotations
  product_file_size: 55911
  product_url: https://api.pharmgkb.org/v1/download/file/data/drugLabels.zip
- category: Product
  compression: zip
  description: Pathways data in BioPax XML format
  format: xml
  id: pharmgkb.pathways.biopax
  name: PharmKB Pathways (BioPax)
  product_file_size: 645142
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways-biopax.zip
- category: Product
  compression: zip
  description: Pathways data in TSV format
  format: tsv
  id: pharmgkb.pathways.tsv
  name: PharmKB Pathways (TSV)
  product_file_size: 195089
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways-tsv.zip
- category: Product
  compression: zip
  description: Pathways data in JSON format
  format: json
  id: pharmgkb.pathways.json
  name: PharmKB Pathways (JSON)
  product_file_size: 1873189
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways.json.zip
- category: Product
  compression: zip
  description: List of variant-drug pairs and level of evidence for all clinical annotations
  format: tsv
  id: pharmgkb.clinicalvariants
  name: PharmKB Clinical Variants
  product_file_size: 74321
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalVariants.zip
- category: Product
  compression: zip
  description: List of objects that occur in PharmGKB literature annotations and pathways
  format: tsv
  id: pharmgkb.literatureoccurrences
  name: PharmKB Literature Occurrences
  product_file_size: 1918901
  product_url: https://api.pharmgkb.org/v1/download/file/data/occurrences.zip
- category: Product
  compression: zip
  description: Automatically identified possible relationships between variants and
    drugs from literature
  format: tsv
  id: pharmgkb.automatedannotations
  name: PharmKB Automated Annotations
  product_file_size: 1881822
  product_url: https://api.pharmgkb.org/v1/download/file/data/automated_annotations.zip
  warnings: []
- category: Product
  compression: zip
  description: Summary of gene information used by PharmGKB and annotations
  format: tsv
  id: pharmgkb.genes
  name: PharmKB Genes
  product_file_size: 2901222
  product_url: https://api.pharmgkb.org/v1/download/file/data/genes.zip
  warnings: []
- category: Product
  compression: zip
  description: Summary of variants annotated by PharmGKB that have been tracked in
    dbSNP
  format: tsv
  id: pharmgkb.variants
  name: PharmKB Variants
  product_file_size: 850310
  product_url: https://api.pharmgkb.org/v1/download/file/data/variants.zip
- category: Product
  compression: zip
  description: Summaries of drug information annotated by PharmGKB
  format: tsv
  id: pharmgkb.drugs
  name: PharmKB Drugs
  product_file_size: 717666
  product_url: https://api.pharmgkb.org/v1/download/file/data/drugs.zip
  warnings: []
- category: Product
  compression: zip
  description: Summaries of chemical information annotated by PharmGKB
  format: tsv
  id: pharmgkb.chemicals
  name: PharmKB Chemicals
  product_file_size: 836804
  product_url: https://api.pharmgkb.org/v1/download/file/data/chemicals.zip
  warnings: []
- category: Product
  compression: zip
  description: Summary of disease and other phenotypes annotated by PharmGKB
  format: tsv
  id: pharmgkb.phenotypes
  name: PharmKB Phenotypes
  product_file_size: 186836
  product_url: https://api.pharmgkb.org/v1/download/file/data/phenotypes.zip
- category: Product
  description: Archive of papers of interest from May 2006 to April 2017
  format: csv
  id: pharmgkb.papers
  name: PharmKB Papers of Interest Archive
  product_file_size: 126005
  product_url: https://api.pharmgkb.org/v1/download/file/attachment/PapersOfInterestArchive.csv
  warnings: []
- category: Product
  compression: zip
  description: Haplotype frequencies from UK Biobank dataset using PharmCAT
  format: tsv
  id: pharmgkb.haplotypefrequencies.ukbb
  name: PharmKB UK Biobank Frequencies
  product_file_size: 30925
  product_url: https://api.pharmgkb.org/v1/download/file/data/pharmgkb_haplotype_frequencies_UKBB.zip
  warnings: []
- category: Product
  compression: zip
  description: Haplotype, phenotype, and activity score frequencies from AllOfUs dataset
    using PharmCAT
  format: tsv
  id: pharmgkb.haplotypefrequencies.allofus
  name: PharmKB AllOfUs Biobank Frequencies
  product_file_size: 58421
  product_url: https://api.pharmgkb.org/v1/download/file/data/pharmgkb_haplotype_frequencies_AllOfUs.zip
- category: Product
  description: pharmgkb.disease OBO
  format: obo
  id: obo-db-ingest.pharmgkb.disease.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.disease OBO
  original_source:
  - pharmgkb
  product_file_size: 148487
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.disease OWL
  format: owl
  id: obo-db-ingest.pharmgkb.disease.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.disease OWL
  original_source:
  - pharmgkb
  product_file_size: 178658
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.disease OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.disease.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.disease OBO Graph JSON
  original_source:
  - pharmgkb
  product_file_size: 180080
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.json
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: pharmgkb.disease SSSOM
  format: sssom
  id: obo-db-ingest.pharmgkb.disease.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.disease SSSOM
  original_source:
  - pharmgkb
  product_file_size: 62271
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.pathways OBO
  format: obo
  id: obo-db-ingest.pharmgkb.pathways.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.pathways OBO
  original_source:
  - pharmgkb
  product_file_size: 2776
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.pathways/pharmgkb.pathways.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.pathways OWL
  format: owl
  id: obo-db-ingest.pharmgkb.pathways.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.pathways OWL
  original_source:
  - pharmgkb
  product_file_size: 3784
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.pathways/pharmgkb.pathways.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.pathways OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.pathways.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.pathways OBO Graph JSON
  original_source:
  - pharmgkb
  product_file_size: 2947
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.pathways/pharmgkb.pathways.json
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.drug OBO
  format: obo
  id: obo-db-ingest.pharmgkb.drug.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug OBO
  original_source:
  - pharmgkb
  product_file_size: 465956
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.drug OWL
  format: owl
  id: obo-db-ingest.pharmgkb.drug.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug OWL
  original_source:
  - pharmgkb
  product_file_size: 531402
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.drug OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.drug.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug OBO Graph JSON
  original_source:
  - pharmgkb
  product_file_size: 552557
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.json
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: pharmgkb.drug SSSOM
  format: sssom
  id: obo-db-ingest.pharmgkb.drug.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug SSSOM
  original_source:
  - pharmgkb
  product_file_size: 202221
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.gene OBO
  format: obo
  id: obo-db-ingest.pharmgkb.gene.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene OBO
  original_source:
  - pharmgkb
  product_file_size: 2137084
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.gene OWL
  format: owl
  id: obo-db-ingest.pharmgkb.gene.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene OWL
  original_source:
  - pharmgkb
  product_file_size: 2542592
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.gene OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.gene.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene OBO Graph JSON
  original_source:
  - pharmgkb
  product_file_size: 2668332
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.json
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: pharmgkb.gene SSSOM
  format: sssom
  id: obo-db-ingest.pharmgkb.gene.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene SSSOM
  original_source:
  - pharmgkb
  product_file_size: 1621905
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.variant OBO
  format: obo
  id: obo-db-ingest.pharmgkb.variant.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant OBO
  original_source:
  - pharmgkb
  product_file_size: 102072
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.variant OWL
  format: owl
  id: obo-db-ingest.pharmgkb.variant.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant OWL
  original_source:
  - pharmgkb
  product_file_size: 107225
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.owl
  secondary_source:
  - obo-db-ingest
- category: Product
  description: pharmgkb.variant OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.variant.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant OBO Graph JSON
  original_source:
  - pharmgkb
  product_file_size: 92435
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.json
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: pharmgkb.variant SSSOM
  format: sssom
  id: obo-db-ingest.pharmgkb.variant.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant SSSOM
  original_source:
  - pharmgkb
  product_file_size: 56599
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  product_url: https://zenodo.org/record/4077338
  secondary_source:
  - pharmkg
- category: Product
  description: Pharmacogenomics data from PharmGKB, DrugBank and other pharmacogenomics
    sources
  format: http
  id: genecards.pharmacogenomics
  name: GeneCards Pharmacogenomics Data
  original_source:
  - pharmgkb
  - drugbank
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-08_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-08_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-08: HTTP 403 error
    when accessing file'
- category: GraphProduct
  description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing
    and integrating information from diverse biomedical resources including DRKG,
    iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome,
    SIDER, and others).
  id: ibkh.graph
  name: iBKH Knowledge Graph
  original_source:
  - drkg
  - idisk
  - brenda
  - ctd
  - drugbank
  - kegg
  - pharmgkb
  - reactome
  - sider
  - tissues
  - bgee
  - doid
  - uberon
  - cl
  - hgnc
  - chembl
  - chebi
repository: https://www.pharmgkb.org/downloads
---
PharmGKB