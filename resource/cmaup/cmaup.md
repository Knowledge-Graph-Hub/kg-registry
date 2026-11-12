---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bidd.group/
  label: Bioinformatics & Drug Design group (BIDD)
- category: Individual
  contact_details:
  - contact_type: email
    value: zengxian@fudan.edu.cn
  label: Xian Zeng
- category: Individual
  contact_details:
  - contact_type: email
    value: chenyuzong@sz.tsinghua.edu.cn
  label: Yu Zong Chen
creation_date: '2026-05-29T00:00:00Z'
description: CMAUP (Collective Molecular Activities of Useful Plants) is a database
  of plants and their chemical ingredients linked to experimentally measured activities
  against molecular targets, and through those targets to Gene Ontology terms, KEGG
  pathways and human diseases. Version 2.0 (2024 update) covers 60,222 ingredients,
  7,865 plants, 758 targets and 1,399 diseases, and adds oral bioavailability predictions,
  plant targets overlapping disease differentially expressed genes, clinical trial associations
  and plant-disease associations. All data are freely downloadable as tab-separated
  files.
domains:
- biomedical
- drug discovery
- pharmacology
- chemistry and biochemistry
- natural products
- organisms
- plants
funding:
- National Natural Science Foundation of China (NSFC) (32000479)
- National Natural Science Foundation of China (NSFC) (32200745)
- National Natural Science Foundation of China (NSFC) (82371781)
- National Key R&D Program of China (2019YFA0905900)
- Shanghai Science and Technology Funds (21QB1401800)
- Shanghai Sailing Program (21YF1401900)
homepage_url: https://bidd.group/CMAUP/
id: cmaup
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: CMAUP
products:
- category: Product
  description: Download page listing all CMAUP v2.0 and v1.0 bulk data files as tab-separated
    plain-text files.
  format: http
  id: cmaup.download-page
  name: CMAUP Download Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/download.html
- category: Product
  description: Tab-separated file of experimentally derived quantitative activity values for
    each ingredient-target pair in CMAUP v2.0, with references for each activity.
  format: tsv
  id: cmaup.download.ingredient-target-activities
  name: CMAUP v2.0 Ingredient-Target Activity Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Ingredient_Target_Associations_ActivityValues_References.txt
- category: Product
  description: Tab-separated file of CMAUP v2.0 plant ingredients with potent activity, with
    ChEMBL and PubChem identifiers, physicochemical properties, InChI, InChIKey
    and SMILES.
  format: tsv
  id: cmaup.download.ingredients-active
  name: CMAUP v2.0 Active Ingredients
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Ingredients_onlyActive.txt
- category: Product
  description: Tab-separated file of all CMAUP v2.0 plant ingredients with names, ChEMBL and
    PubChem identifiers, ADMETlab-calculated physicochemical properties, InChI,
    InChIKey and SMILES.
  format: tsv
  id: cmaup.download.ingredients-all
  name: CMAUP v2.0 All Ingredients
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Ingredients_All.txt
- category: Product
  description: Tab-separated file of human oral bioavailability indicators for all CMAUP v2.0
    ingredients, calculated with RDKit and evaluated using SwissADME criteria and
    the HobPre predictor.
  format: tsv
  id: cmaup.download.oral-bioavailability
  name: CMAUP v2.0 Ingredient Human Oral Bioavailability
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Human_Oral_Bioavailability_information_of_Ingredients_All.txt
- category: Product
  description: Tab-separated file of clinical investigations of individual plants or plant
    ingredients, with ClinicalTrials.gov registry numbers, titles and trial
    phases.
  format: tsv
  id: cmaup.download.plant-clinical-trials
  name: CMAUP v2.0 Plant Clinical Trial Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Plant_Clinical_Trials_Associations.txt
- category: Product
  description: Tab-separated file of associations between plants and human diseases at four
    levels of evidence (therapeutic target, reversion of disease transcriptomic
    change, clinical trials of plants, and clinical trials of plant ingredients).
  format: tsv
  id: cmaup.download.plant-disease-associations
  name: CMAUP v2.0 Plant-Human Disease Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Plant_Human_Disease_Associations.txt
- category: Product
  description: Tab-separated file of plant-ingredient pairs in CMAUP v2.0, limited to active
    ingredients.
  format: tsv
  id: cmaup.download.plant-ingredient-active
  name: CMAUP v2.0 Plant-Active Ingredient Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Plant_Ingredient_Associations_onlyActiveIngredients.txt
- category: Product
  description: Tab-separated file of all plant-ingredient pairs in CMAUP v2.0.
  format: tsv
  id: cmaup.download.plant-ingredient-all
  name: CMAUP v2.0 Plant-Ingredient Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Plant_Ingredient_Associations_allIngredients.txt
- category: Product
  description: Tab-separated file of molecular targets of plants that overlap with
    differentially expressed genes identified by transcriptomic analysis of 74
    diseases.
  format: tsv
  id: cmaup.download.plant-targets-degs
  name: CMAUP v2.0 Plant Targets Overlapping Disease DEGs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Plant_molecular_targets_overlapping_with_DEGs.txt
- category: Product
  description: Tab-separated file of CMAUP v2.0 plants with Latin names and NCBI Taxonomy
    identifiers and names at species, genus and family level.
  format: tsv
  id: cmaup.download.plants
  name: CMAUP v2.0 Plants
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Plants.txt
- category: DocumentationProduct
  description: Plain-text readme describing the data columns of each CMAUP v2.0 download
    file.
  format: txt
  id: cmaup.download.readme
  name: CMAUP v2.0 Download Readme
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/Download_Readme.txt
- category: Product
  description: Tab-separated file of CMAUP v2.0 molecular targets with gene symbols, protein
    names, UniProt, ChEMBL and TTD identifiers, and protein classes.
  format: tsv
  id: cmaup.download.targets
  name: CMAUP v2.0 Targets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Targets.txt
- category: Product
  description: RAR archive (about 152 MB) with index, sample metadata and DESeq2 results for
    disease-versus-control transcriptomic comparisons of 74 diseases, using
    RNA-seq data from sources including ARCHS4 and TCGA.
  format: mixed
  id: cmaup.download.transcriptomic-profiles
  name: CMAUP v2.0 Transcriptomic Profiling of 74 Diseases
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://bidd.group/CMAUP/downloadFiles/CMAUPv2.0_download_Transcriptomic_profiling_of_74_diseases.rar
- category: GraphicalInterface
  description: Web interface for searching and browsing CMAUP plants by usage class, target
    protein, Gene Ontology term, KEGG pathway, disease, geographic location and
    chemical ingredient, with activity values and source references.
  format: http
  id: cmaup.portal
  name: CMAUP Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://bidd.group/CMAUP/
- category: DocumentationProduct
  description: Nucleic Acids Research database article describing CMAUP, its data
    model, and its coverage of useful plants, ingredients, targets, pathways, and
    phenotypes.
  format: http
  id: cmaup.publication
  name: CMAUP Database Publication
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmaup
  product_url: https://doi.org/10.1093/nar/gky965
  warnings: []
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
publications:
- authors:
  - Hou D
  - Lin H
  - Feng Y
  - Zhou K
  - Li X
  - Yang Y
  - Wang S
  - Yang X
  - Wang J
  - Zhao H
  - Zhang X
  - Fan J
  - Lu S
  - Wang D
  - Zhu L
  - Ju D
  - Chen YZ
  - Zeng X
  doi: 10.1093/nar/gkad921
  id: doi:10.1093/nar/gkad921
  journal: Nucleic Acids Research
  preferred: true
  title: 'CMAUP database update 2024: extended functional and association information
    of useful plants for biomedical research'
  year: '2024'
- authors:
  - Zeng X
  - Zhang P
  - Wang Y
  - Qin C
  - Chen S
  - He W
  - Tao L
  - Tan Y
  - Gao D
  - Wang B
  - Chen Z
  - Chen W
  - Jiang YY
  - Chen YZ
  doi: 10.1093/nar/gky965
  id: doi:10.1093/nar/gky965
  journal: Nucleic Acids Research
  title: 'CMAUP: a database of collective molecular activities of useful plants'
  year: '2019'
synonyms:
- Collective Molecular Activities of Useful Plants
version: '2.0'
---
# CMAUP

CMAUP (Collective Molecular Activities of Useful Plants) is developed by the
Bioinformatics & Drug Design group (BIDD) with the School of Pharmacy, Fudan University.
It links useful plants (medicinal, edible and other) to their chemical ingredients,
the experimentally measured activities of those ingredients against molecular targets,
and the targets' Gene Ontology terms, KEGG pathways and associated human diseases.

The 2024 update (v2.0) expanded coverage to 60,222 ingredients, 7,865 plants, 758 targets
and 1,399 diseases, and added human oral bioavailability predictions (SwissADME and HobPre),
plant targets overlapping differentially expressed genes from transcriptomic profiles of
74 diseases, plant-relevant clinical trials from ClinicalTrials.gov, and plant-disease
associations at four levels of evidence. Entries link out to NCBI Taxonomy, PubChem,
ChEMBL, UniProt, KEGG, TTD and the Disease Ontology. All data are available as
tab-separated download files; v1.0 files remain downloadable as well.
