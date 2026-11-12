---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: weijiang@nuaa.edu.cn
  label: Wei Jiang
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.jianglab.cn/ncRNADrug/
  label: Group of Systems Biology and Pharmacogenomics, College of Automation Engineering,
    Nanjing University of Aeronautics and Astronautics
creation_date: '2026-11-12T00:00:00Z'
description: ncRNADrug is a database of validated and predicted non-coding RNAs (miRNAs,
  lncRNAs and circRNAs) associated with drug resistance or targeted by drugs. Its curated
  portion, manually extracted from more than 9,000 publications and integrated with
  the earlier SM2miR, D-lnc and ncDR resources, holds 29,551 drug resistance entries
  (9,195 ncRNAs, 266 drugs) and 32,969 drug-target entries (10,480 ncRNAs, 965 drugs).
  Predicted associations are derived by differential expression analysis of drug
  resistance and drug perturbation datasets from GEO, NCI60 (via CellMiner), GDSC with
  CCLE lncRNA profiles (via TANRIC), and CMap. ncRNAs are identified with miRBase,
  Ensembl, NONCODE and circBase identifiers, and drugs with DrugBank, PubChem and NCI
  DTP identifiers.
domains:
- genomics
- non-coding RNA
- pharmacology
- pharmacogenomics
homepage_url: http://www.jianglab.cn/ncRNADrug/
id: ncrnadrug
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: ncRNADrug
products:
- category: GraphicalInterface
  description: ncRNADrug web portal for browsing and searching ncRNA drug resistance
    and drug-target associations by drug, miRNA, lncRNA, circRNA, drug response or
    target, with an online tool for predicting ncRNAs targeted by drugs.
  format: http
  id: ncrnadrug.portal
  name: ncRNADrug Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  product_url: http://www.jianglab.cn/ncRNADrug/
- category: Product
  description: Download page listing the curated and predicted ncRNADrug association
    tables, each offered as tab-delimited text and as Excel workbooks.
  format: http
  id: ncrnadrug.downloads
  name: ncRNADrug Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  product_url: http://www.jianglab.cn/ncRNADrug/download.html
- category: Product
  description: Tab-delimited table of experimentally supported ncRNAs associated with
    drug resistance or drug response, manually curated from the literature, with ncRNA
    and drug identifiers, effect, target genes, pathways, detection method and condition.
  format: tsv
  id: ncrnadrug.drug-resistance-curated
  name: ncRNADrug Curated Drug Resistance Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: circbase
  product_file_size: 15627539
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DR_Curated.txt
- category: Product
  description: Tab-delimited table of experimentally supported ncRNAs targeted by
    drugs (drugs that regulate ncRNA expression), manually curated from the literature,
    with ncRNA and drug identifiers, regulation direction, detection method and condition.
  format: tsv
  id: ncrnadrug.drug-target-curated
  name: ncRNADrug Curated Drug Target Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: circbase
  product_file_size: 16640321
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DT_Curated.txt
- category: Product
  description: Tab-delimited table of ncRNAs predicted to be associated with drug
    resistance from differential expression analysis of resistant versus sensitive
    samples in GEO series.
  format: tsv
  id: ncrnadrug.drug-resistance-geo
  name: ncRNADrug Predicted Drug Resistance Associations from GEO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  product_file_size: 59928861
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DR_GEO.txt
- category: Product
  description: Tab-delimited table of miRNAs predicted to be associated with drug
    resistance from NCI60 cancer cell line drug response and miRNA expression data
    obtained through CellMiner.
  format: tsv
  id: ncrnadrug.drug-resistance-nci60
  name: ncRNADrug Predicted Drug Resistance Associations from NCI60
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: nci60
  - relation_type: prov:hadPrimarySource
    source: cellminer
  product_file_size: 23404017
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DR_NCI60.txt
- category: Product
  description: Tab-delimited table of lncRNAs predicted to be associated with drug
    resistance from GDSC drug response data and CCLE lncRNA expression profiles (via
    TANRIC).
  format: tsv
  id: ncrnadrug.drug-resistance-ccle
  name: ncRNADrug Predicted Drug Resistance Associations from CCLE
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: gdsc
  product_file_size: 40095682
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DR_CCLE.txt
- category: Product
  description: Tab-delimited table of ncRNAs predicted to be targeted by drugs from
    differential expression analysis of drug-treated versus control samples in GEO
    series.
  format: tsv
  id: ncrnadrug.drug-target-geo
  name: ncRNADrug Predicted Drug Target Associations from GEO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  product_file_size: 55064571
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DT_GEO.txt
- category: Product
  description: Tab-delimited table of lncRNAs predicted to be targeted by drugs from
    re-annotated CMap drug perturbation expression profiles.
  format: tsv
  id: ncrnadrug.drug-target-cmap
  name: ncRNADrug Predicted Drug Target Associations from CMap
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_file_size: 5404104
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DT_CMap.txt
publications:
- authors:
  - Cao X
  - Zhou X
  - Hou F
  - Huang YE
  - Yuan M
  - Long M
  - Chen S
  - Lei W
  - Zhu J
  - Chen J
  - Zhang T
  - Guo AY
  - Jiang W
  doi: 10.1093/nar/gkad1042
  id: doi:10.1093/nar/gkad1042
  journal: Nucleic Acids Research
  preferred: true
  title: 'ncRNADrug: a database for validated and predicted ncRNAs associated with
    drug resistance and targeted by drugs'
  year: '2024'
---
# ncRNADrug

ncRNADrug is a database of non-coding RNAs (miRNAs, lncRNAs and circRNAs) associated with drug resistance or regulated by drugs, maintained by the Group of Systems Biology and Pharmacogenomics at Nanjing University of Aeronautics and Astronautics. It combines manually curated, experimentally supported associations from the literature with associations predicted from drug response and drug perturbation expression data (GEO, NCI60, GDSC/CCLE and CMap).

The curated drug resistance (`DR_Curated.txt`) and drug target (`DT_Curated.txt`) tables, along with the predicted tables, are downloadable as tab-delimited text or Excel files. The website and paper describe the data as freely available but state no data license (the paper itself is CC BY 4.0).
