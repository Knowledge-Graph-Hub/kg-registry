---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: depmap@sanger.ac.uk
  - contact_type: url
    value: https://depmap.sanger.ac.uk/
  label: Cancer Dependency Map at Sanger, Wellcome Sanger Institute
creation_date: '2026-10-03T00:00:00Z'
description: Cell Model Passports is a curated database of preclinical cancer models,
  including cell lines and organoids, run by the Wellcome Sanger Institute as part
  of the Cancer Dependency Map at Sanger. For each model it holds relationships to
  other models, patient and clinical annotation, and genomic and functional datasets
  including mutations, copy number, RNA-seq expression, methylation, proteomics, CRISPR
  knockout screens, drug response, gene fusions and growth rates.
domains:
- biomedical
- cancer
- genomics
- gene expression profiling
- precision medicine
- pharmacology
homepage_url: https://cellmodelpassports.sanger.ac.uk/
id: cellmodelpassports
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  id: https://depmap.sanger.ac.uk/documentation/data-usage-policy/
  label: DepMap at Sanger Data Usage Policy (non-commercial research use)
name: Cell Model Passports
products:
- category: GraphicalInterface
  description: Cell Model Passports web portal for searching and browsing cancer cell
    line and organoid models, their clinical annotation and available genomic and
    functional datasets.
  format: http
  id: cellmodelpassports.portal
  name: Cell Model Passports Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  product_url: https://cellmodelpassports.sanger.ac.uk/
- category: ProgrammingInterface
  connection_url: https://api.cellmodelpassports.sanger.ac.uk/
  description: JSON:API (v1.0) REST API for models, genes and datasets such as mutations,
    with Swagger documentation.
  format: http
  id: cellmodelpassports.api
  is_public: true
  name: Cell Model Passports API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  product_url: https://api.cellmodelpassports.sanger.ac.uk/swagger
- category: Product
  description: Downloads page listing current and archived bulk files of model annotation
    and processed genomic and functional datasets (model lists, mutations, copy number,
    expression, proteomics, CRISPR screens, drug response).
  format: mixed
  id: cellmodelpassports.downloads
  name: Cell Model Passports Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  product_url: https://cellmodelpassports.sanger.ac.uk/downloads
- category: MappingProduct
  description: Annotated list of all cell line and organoid models with tissue, cancer
    type (NCIt), clinical and patient annotation, and cross-references to Cellosaurus
    RRIDs, COSMIC IDs, DepMap (Broad) IDs and CCLE names.
  format: csv
  id: cellmodelpassports.model_list
  name: Cell Model Passports Model List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: ncit
  product_file_size: 957555
  product_url: https://cog.sanger.ac.uk/cmp/download/model_list_20260921.csv
- category: MappingProduct
  description: Gene identifier table mapping Cell Model Passports gene IDs to HGNC,
    Ensembl, Entrez Gene, RefSeq, CCDS, COSMIC and UniProt identifiers.
  format: csv
  id: cellmodelpassports.gene_identifiers
  name: Cell Model Passports Gene Identifiers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: cosmic
  product_file_size: 3873087
  product_url: https://cog.sanger.ac.uk/cmp/download/gene_identifiers_20241212.csv
- category: Product
  compression: zip
  description: Combined somatic mutation calls from whole-exome, whole-genome and
    targeted sequencing of all models.
  format: csv
  id: cellmodelpassports.mutations_all
  name: Cell Model Passports All Mutations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  product_file_size: 305104654
  product_url: https://cog.sanger.ac.uk/cmp/download/mutations_all_20260724.zip
- category: Product
  compression: zip
  description: Processed RNA-seq gene expression for Sanger and Broad DepMap models,
    merged into a single dataset.
  format: csv
  id: cellmodelpassports.rnaseq_merged
  name: Cell Model Passports Merged RNA-seq Expression
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_file_size: 1291769946
  product_url: https://cog.sanger.ac.uk/cmp/download/rnaseq_merged_20260323.zip
- category: Product
  compression: zip
  description: Processed protein abundance (proteomics) data for cancer cell line
    models.
  format: csv
  id: cellmodelpassports.proteomics
  name: Cell Model Passports Proteomics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  product_file_size: 132153900
  product_url: https://cog.sanger.ac.uk/cmp/download/Proteomics_20250211.zip
- category: Product
  compression: zip
  description: Project Score CRISPR knockout gene fitness scores for Sanger and Broad
    DepMap (21Q2) cell line screens.
  format: csv
  id: cellmodelpassports.crispr_fitness_scores
  name: Cell Model Passports CRISPR Fitness Scores
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_file_size: 198873260
  product_url: https://cog.sanger.ac.uk/cmp/download/Project_Score2_fitness_scores_Sanger_v2_Broad_21Q2_20250624.zip
- category: Product
  description: GDSC2 fitted drug dose response values (IC50, AUC) for cancer cell
    lines, distributed through the Cell Model Passports downloads.
  format: xlsx
  id: cellmodelpassports.gdsc2_dose_response
  name: GDSC2 Fitted Dose Response
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellmodelpassports
  - relation_type: prov:hadPrimarySource
    source: gdsc
  product_file_size: 22112537
  product_url: https://cmp.cog.sanger.ac.uk/download/GDSC2_fitted_dose_response_27Oct23.xlsx
publications:
- authors:
  - Dieudonne van der Meer
  - Syd Barthorpe
  - Wanjuan Yang
  - Howard Lightfoot
  - Caitlin Hall
  - James Gilbert
  - Hayley E Francies
  - Mathew J Garnett
  doi: 10.1093/nar/gky872
  id: doi:10.1093/nar/gky872
  journal: Nucleic Acids Research
  preferred: true
  title: Cell Model Passports-a hub for clinical, genetic and functional datasets
    of preclinical cancer models
  year: '2019'
synonyms:
- CMP
---
# Cell Model Passports

Cell Model Passports is a curated database of preclinical cancer models, including
cell lines and organoids. It is run by the Wellcome Sanger Institute as part of the
Cancer Dependency Map at Sanger, and it includes models from the Human Cancer Model
Initiative (HCMI) and RNA-seq data from the Broad DepMap. The API reported 2,266
models on 2026-10-03 (the 2019 paper described over 1,200).

## Data

For each model it holds relationships to other models, patient and clinical
annotation, and genomic and functional datasets: mutations, copy number, RNA-seq
expression, methylation, proteomics, CRISPR knockout screens (Project Score), drug
response (GDSC), gene fusions and growth rates. The model list cross-references
Cellosaurus RRIDs, COSMIC IDs, DepMap (Broad) IDs and CCLE names.

## Access

- Web portal: https://cellmodelpassports.sanger.ac.uk/
- Downloads: https://cellmodelpassports.sanger.ac.uk/downloads (dated csv, xlsx and
  zip files; the full file catalogue is also available from the API at
  `/download_files?include=groups.files`)
- API: https://api.cellmodelpassports.sanger.ac.uk (Swagger docs at `/swagger`)

## License

Data are covered by the DepMap at Sanger Data Usage Policy, which grants a
non-exclusive, non-transferable right to use data files for internal research and
educational purposes and excludes resale and commercial services. The API
documentation states that use is free for non-commercial purposes, with prior
consent needed for commercial use.
