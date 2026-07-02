---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: feedback@pharmgkb.org
  label: PharmGKB
creation_date: '2025-05-01T00:00:00Z'
description: PharmGKB collects, curates and disseminates knowledge about clinically
  actionable gene-drug associations and genotype-phenotype relationships.
domains:
- biomedical
- chemistry and biochemistry
- pharmacology
- genomics
- precision medicine
homepage_url: https://www.pharmgkb.org/
id: pharmgkb
infores_id: pharmgkb
last_modified_date: '2026-06-18T00:00:00Z'
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 1231768
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations.zip
- category: Product
  compression: zip
  description: Level of evidence 1-2 clinical annotation summaries
  format: tsv
  id: pharmgkb.clinicalannotations.loe
  name: PharmKB Clinical Annotations (LOE 1-2)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 271314
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations_LOE1-2.zip
- category: Product
  compression: zip
  description: Variant annotation summary
  format: tsv
  id: pharmgkb.variantannotations
  name: PharmKB Variant Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 4071535
  product_url: https://api.pharmgkb.org/v1/download/file/data/variantAnnotations.zip
- category: Product
  compression: zip
  description: Relationships summarized from PharmGKB annotations
  format: tsv
  id: pharmgkb.relationships
  name: PharmKB Relationships
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 1261136
  product_url: https://api.pharmgkb.org/v1/download/file/data/relationships.zip
- category: Product
  compression: zip
  description: Detailed clinical guideline annotations
  format: json
  id: pharmgkb.guidelineannotations
  name: PharmKB Clinical Guideline Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 811786
  product_url: https://api.pharmgkb.org/v1/download/file/data/guidelineAnnotations.json.zip
- category: Product
  compression: zip
  description: Drug label annotations
  format: tsv
  id: pharmgkb.druglabels
  name: PharmKB Drug Label Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 55911
  product_url: https://api.pharmgkb.org/v1/download/file/data/drugLabels.zip
- category: Product
  compression: zip
  description: Pathways data in BioPax XML format
  format: xml
  id: pharmgkb.pathways.biopax
  name: PharmKB Pathways (BioPax)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 645142
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways-biopax.zip
- category: Product
  compression: zip
  description: Pathways data in TSV format
  format: tsv
  id: pharmgkb.pathways.tsv
  name: PharmKB Pathways (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 195089
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways-tsv.zip
- category: Product
  compression: zip
  description: Pathways data in JSON format
  format: json
  id: pharmgkb.pathways.json
  name: PharmKB Pathways (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 1873189
  product_url: https://api.pharmgkb.org/v1/download/file/data/pathways.json.zip
- category: Product
  compression: zip
  description: List of variant-drug pairs and level of evidence for all clinical annotations
  format: tsv
  id: pharmgkb.clinicalvariants
  name: PharmKB Clinical Variants
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 74321
  product_url: https://api.pharmgkb.org/v1/download/file/data/clinicalVariants.zip
- category: Product
  compression: zip
  description: List of objects that occur in PharmGKB literature annotations and pathways
  format: tsv
  id: pharmgkb.literatureoccurrences
  name: PharmKB Literature Occurrences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 1918901
  product_url: https://api.pharmgkb.org/v1/download/file/data/occurrences.zip
- category: Product
  compression: zip
  description: Automatically identified possible relationships between variants and
    drugs from literature
  format: tsv
  id: pharmgkb.automatedannotations
  name: PharmKB Automated Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 1881822
  product_url: https://api.pharmgkb.org/v1/download/file/data/automated_annotations.zip
  warnings: []
- category: Product
  compression: zip
  description: Summary of gene information used by PharmGKB and annotations
  format: tsv
  id: pharmgkb.genes
  name: PharmKB Genes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 850310
  product_url: https://api.pharmgkb.org/v1/download/file/data/variants.zip
- category: Product
  compression: zip
  description: Summaries of drug information annotated by PharmGKB
  format: tsv
  id: pharmgkb.drugs
  name: PharmKB Drugs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 717666
  product_url: https://api.pharmgkb.org/v1/download/file/data/drugs.zip
  warnings: []
- category: Product
  compression: zip
  description: Summaries of chemical information annotated by PharmGKB
  format: tsv
  id: pharmgkb.chemicals
  name: PharmKB Chemicals
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 836804
  product_url: https://api.pharmgkb.org/v1/download/file/data/chemicals.zip
  warnings: []
- category: Product
  compression: zip
  description: Summary of disease and other phenotypes annotated by PharmGKB
  format: tsv
  id: pharmgkb.phenotypes
  name: PharmKB Phenotypes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 186836
  product_url: https://api.pharmgkb.org/v1/download/file/data/phenotypes.zip
- category: Product
  description: Archive of papers of interest from May 2006 to April 2017
  format: csv
  id: pharmgkb.papers
  name: PharmKB Papers of Interest Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 126005
  product_url: https://api.pharmgkb.org/v1/download/file/attachment/PapersOfInterestArchive.csv
  warnings: []
- category: Product
  compression: zip
  description: Haplotype frequencies from UK Biobank dataset using PharmCAT
  format: tsv
  id: pharmgkb.haplotypefrequencies.ukbb
  name: PharmKB UK Biobank Frequencies
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
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
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 148487
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.obo
- category: Product
  description: pharmgkb.disease OWL
  format: owl
  id: obo-db-ingest.pharmgkb.disease.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.disease OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 178658
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.owl
- category: Product
  description: pharmgkb.disease OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.disease.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.disease OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 180080
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.json
- category: MappingProduct
  description: pharmgkb.disease SSSOM
  format: sssom
  id: obo-db-ingest.pharmgkb.disease.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.disease SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 62271
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.sssom.tsv
- category: Product
  description: pharmgkb.pathways OBO
  format: obo
  id: obo-db-ingest.pharmgkb.pathways.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.pathways OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 2776
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.pathways/pharmgkb.pathways.obo
- category: Product
  description: pharmgkb.pathways OWL
  format: owl
  id: obo-db-ingest.pharmgkb.pathways.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.pathways OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 3784
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.pathways/pharmgkb.pathways.owl
- category: Product
  description: pharmgkb.pathways OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.pathways.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.pathways OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 2947
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.pathways/pharmgkb.pathways.json
- category: Product
  description: pharmgkb.drug OBO
  format: obo
  id: obo-db-ingest.pharmgkb.drug.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 465956
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.obo
- category: Product
  description: pharmgkb.drug OWL
  format: owl
  id: obo-db-ingest.pharmgkb.drug.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 531402
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.owl
- category: Product
  description: pharmgkb.drug OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.drug.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 552557
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.json
- category: MappingProduct
  description: pharmgkb.drug SSSOM
  format: sssom
  id: obo-db-ingest.pharmgkb.drug.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 202221
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.sssom.tsv
- category: Product
  description: pharmgkb.gene OBO
  format: obo
  id: obo-db-ingest.pharmgkb.gene.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 2137084
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.obo
- category: Product
  description: pharmgkb.gene OWL
  format: owl
  id: obo-db-ingest.pharmgkb.gene.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 2542592
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.owl
- category: Product
  description: pharmgkb.gene OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.gene.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 2668332
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.json
- category: MappingProduct
  description: pharmgkb.gene SSSOM
  format: sssom
  id: obo-db-ingest.pharmgkb.gene.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 1621905
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.sssom.tsv
- category: Product
  description: pharmgkb.variant OBO
  format: obo
  id: obo-db-ingest.pharmgkb.variant.obo
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 102072
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.obo
- category: Product
  description: pharmgkb.variant OWL
  format: owl
  id: obo-db-ingest.pharmgkb.variant.owl
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 107225
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.owl
- category: Product
  description: pharmgkb.variant OBO Graph JSON
  format: json
  id: obo-db-ingest.pharmgkb.variant.json
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 92435
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.json
- category: MappingProduct
  description: pharmgkb.variant SSSOM
  format: sssom
  id: obo-db-ingest.pharmgkb.variant.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 56599
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.sssom.tsv
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  format: mixed
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: humannet
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharmkg
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://zenodo.org/record/4077338
- category: Product
  description: Pharmacogenomics data from PharmGKB, DrugBank and other pharmacogenomics
    sources
  format: http
  id: genecards.pharmacogenomics
  name: GeneCards Pharmacogenomics Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: GraphProduct
  description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing
    and integrating information from diverse biomedical resources including DRKG,
    iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome,
    SIDER, and others).
  format: mixed
  id: ibkh.graph
  name: iBKH Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drkg
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ibkh
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
- category: Product
  description: pharmgkb.disease Nodes TSV
  format: tsv
  id: obo-db-ingest.pharmgkb.disease.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.disease Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 85777
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.disease/pharmgkb.disease.tsv
- category: Product
  description: pharmgkb.drug Nodes TSV
  format: tsv
  id: obo-db-ingest.pharmgkb.drug.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.drug Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 55062
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.drug/pharmgkb.drug.tsv
- category: Product
  description: pharmgkb.gene Nodes TSV
  format: tsv
  id: obo-db-ingest.pharmgkb.gene.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.gene Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 757356
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.gene/pharmgkb.gene.tsv
- category: Product
  description: pharmgkb.pathways Nodes TSV
  format: tsv
  id: obo-db-ingest.pharmgkb.pathways.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.pathways Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 2140
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.pathways/pharmgkb.pathways.tsv
- category: Product
  description: pharmgkb.variant Nodes TSV
  format: tsv
  id: obo-db-ingest.pharmgkb.variant.tsv
  license:
    id: https://creativecommons.org/licenses/by-sa/4.0/
    label: CC-BY-SA-4.0
  name: pharmgkb.variant Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  product_file_size: 19203
  product_url: https://w3id.org/biopragmatics/resources/pharmgkb.variant/pharmgkb.variant.tsv
- category: GraphProduct
  description: The OREGANO knowledge graph dataset integrating drug, protein, gene,
    and disease information for drug repositioning.
  format: http
  id: oregano.graph
  name: OREGANO Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oregano
  product_url: https://gitub.u-bordeaux.fr/erias/oregano/-/tree/master/Data_OREGANO/Graphs
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cmaup
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: npass
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: bio2rdf
- category: GraphProduct
  compression: gzip
  description: PharMeBINet V2 JSON release published on February 6, 2024.
  format: json
  id: pharmebinet.json
  latest_version: v2
  name: PharMeBINet JSON Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1942958027
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.json.gz/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 TSV release published on February 6, 2024.
  format: tsv
  id: pharmebinet.tsv
  latest_version: v2
  name: PharMeBINet TSV Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1922614551
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_tsv_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 GraphML release published on February 6, 2024.
  format: mixed
  id: pharmebinet.graphml
  latest_version: v2
  name: PharMeBINet GraphML Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 2027519087
  product_url: https://zenodo.org/api/records/17814889/files/PharMeBiNet_graphml_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j database release published on February 6, 2024.
  format: neo4j
  id: pharmebinet.neo4j
  latest_version: v2
  name: PharMeBINet Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3847978577
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j dump release published on February 6, 2024.
  dump_format: neo4j
  format: neo4j
  id: pharmebinet.neo4j.dump
  latest_version: v2
  name: PharMeBINet Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3598325722
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_dump_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.2.1
  compression: gzip
  description: Human-scoped, Neo4j-ready subgraph of the BioBTree knowledge graph,
    exported as a biolink-typed KGX graph (~40M nodes / ~132M edges, ~8.3 GB compressed
    across separate node and edge files). A practical projection of the full graph
    for human-centric biomedical use. Published on Zenodo.
  edge_count: 132075627
  format: kgx
  id: biobtree.graph.human-subgraph
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC-BY-NC-SA-4.0
  name: BioBTree Knowledge Graph - Human Subgraph (KGX)
  node_categories:
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellLine
  - biolink:CellularComponent
  - biolink:CodingSequence
  - biolink:Disease
  - biolink:DiseaseOrPhenotypicFeature
  - biolink:Drug
  - biolink:Exon
  - biolink:Gene
  - biolink:GrossAnatomicalStructure
  - biolink:MacromolecularComplex
  - biolink:MolecularActivity
  - biolink:NoncodingRNAProduct
  - biolink:NucleicAcidSequenceMotif
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:ProteinDomain
  - biolink:ProteinFamily
  - biolink:Publication
  - biolink:RegulatoryRegion
  - biolink:SequenceVariant
  - biolink:SmallMolecule
  - biolink:Transcript
  node_count: 40160474
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  predicates:
  - biolink:actively_involved_in
  - biolink:affects
  - biolink:associated_with
  - biolink:close_match
  - biolink:derives_from
  - biolink:directly_physically_interacts_with
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:gene_product_of
  - biolink:has_adverse_event
  - biolink:has_gene_product
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:in_clinical_trials_for
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:member_of
  - biolink:mentions
  - biolink:orthologous_to
  - biolink:paralogous_to
  - biolink:participates_in
  - biolink:physically_interacts_with
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:transcribed_from
  - biolink:translates_to
  - biolink:treats_or_applied_or_studied_to_treat
  product_url: https://zenodo.org/records/20816742
- category: GraphProduct
  description: KGX nodes and edges for KG-COVID-19
  format: kgx
  id: kg-covid-19.graph
  name: KG-COVID-19 graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-covid-19
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cord-19
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://kghub.io/kg-covid-19/
  warnings:
  - 'Download offline as of 2026-07-01: the KG-Hub reorganization has taken this file
    offline. The kghub.io and kg-hub.berkeleybop.io hosts return HTTP 404 for all
    kg-covid-19 artifacts (current and dated) and the kg-hub-public-data S3 objects
    return HTTP 403. No replacement public download URL is available.'
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
publications:
- authors:
  - Whirl-Carrillo M
  - Huddart R
  - Gong L
  - Sangkuhl K
  - Thorn CF
  - Whaley R
  - Klein TE
  doi: 10.1002/cpt.2350
  id: https://www.ncbi.nlm.nih.gov/pubmed/34216021
  journal: Clin Pharmacol Ther
  preferred: true
  title: An Evidence-Based Framework for Evaluating Pharmacogenomics Knowledge for
    Personalized Medicine
  year: '2021'
repository: https://www.pharmgkb.org/downloads
taxon:
- NCBITaxon:9606
---
PharmGKB