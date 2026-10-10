---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
creation_date: '2026-10-10T00:00:00Z'
description: DrugEnrichr is a drug set enrichment analysis tool from the Ma'ayan Laboratory.
  It has the Enrichr interface and statistics, but serves drug sets instead of gene
  sets. Users submit a list of drugs and test it against 29 drug set libraries (109,284
  terms) built from drug-target, mechanism-of-action, side-effect, pharmacogenomic,
  literature, and L1000 drug-perturbation sources, with results ranked by p-value,
  adjusted p-value, z-score, and combined score.
domains:
- pharmacology
- drug discovery
- drug repositioning
homepage_url: https://maayanlab.cloud/DrugEnrichr/
id: drugenrichr
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
name: DrugEnrichr
products:
- category: GraphicalInterface
  description: Web interface for submitting drug lists, viewing enrichment results
    against drug set libraries, browsing the libraries, and searching drug set terms.
  format: http
  id: drugenrichr.portal
  name: DrugEnrichr Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugenrichr
  product_url: https://maayanlab.cloud/DrugEnrichr/
- category: ProgrammingInterface
  description: REST API following the Enrichr pattern, with endpoints to add a drug
    list, view it, run enrichment against a chosen library, export results, and map
    drug names. Documented on the help page.
  format: json
  id: drugenrichr.api
  is_public: true
  name: DrugEnrichr API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugenrichr
  product_url: https://maayanlab.cloud/DrugEnrichr/help#api
- category: Product
  description: Statistics for the 29 drug set libraries (109,284 terms) served by
    DrugEnrichr, built from ATC, the Drug Repurposing Hub, KINOMEscan, PharmGKB and
    OFFSIDES, DrugCentral, CREEDS, Geneshot, L1000FWD, SIDER, and STITCH. Each library
    can be downloaded as a GMT-style text file from the geneSetLibrary endpoint (mode=text&libraryName=<library>).
  format: json
  id: drugenrichr.libraries
  name: DrugEnrichr Drug Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugenrichr
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  product_file_size: 4251
  product_url: https://maayanlab.cloud/DrugEnrichr/datasetStatistics
- category: GraphProduct
  description: Core ReproTox-KG graph linking birth defects, drugs, and genes from
    DrugShot, DrugEnrichr, and GeneShot literature co-mention evidence (1,433 nodes,
    2,252 edges).
  format: json
  id: reprotox-kg.graph.core
  name: ReproTox-KG Core Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: drugshot
  - relation_type: prov:hadPrimarySource
    source: drugenrichr
  product_file_size: 1649245
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/reprotox_serialization.valid.json
publications:
- authors:
  - Chen EY
  - Tan CM
  - Kou Y
  - Duan Q
  - Wang Z
  - Meirelles GV
  - Clark NR
  - Ma'ayan A
  doi: 10.1186/1471-2105-14-128
  id: PMID:23586463
  journal: BMC Bioinformatics
  preferred: true
  title: 'Enrichr: interactive and collaborative HTML5 gene list enrichment analysis
    tool'
  year: '2013'
- authors:
  - Kuleshov MV
  - Jones MR
  - Rouillard AD
  - Fernandez NF
  - Duan Q
  - Wang Z
  - Koplev S
  - Jenkins SL
  - Jagodnik KM
  - Lachmann A
  - McDermott MG
  - Monteiro CD
  - Gundersen GW
  - Ma'ayan A
  doi: 10.1093/nar/gkw377
  id: PMID:27141961
  journal: Nucleic Acids Res
  title: 'Enrichr: a comprehensive gene set enrichment analysis web server 2016 update'
  year: '2016'
---
# DrugEnrichr

DrugEnrichr is a drug set enrichment analysis tool from the Ma'ayan Laboratory at the Icahn School of Medicine at Mount Sinai, announced in May 2020 and developed by Maxim Kuleshov, Eryk Kropiwnicki, and Avi Ma'ayan. It reuses the Enrichr interface and statistics, but searches drug sets instead of gene sets.

## Libraries

DrugEnrichr serves 29 drug set libraries with 109,284 terms in total. They come from the Anatomical Therapeutic Chemical classification, the Drug Repurposing Hub (mechanisms of action and targets), KINOMEscan, PharmGKB (variants and OFFSIDES side effects), DrugCentral targets, CREEDS drug signatures, Geneshot gene-drug associations and predictions, L1000FWD (signatures, enriched GO terms and KEGG pathways, and predicted side effects), SIDER (indications and side effects), and STITCH targets. Each library can be downloaded as a GMT-style text file.

## Access and terms

DrugEnrichr has a web interface and a REST API that follows the Enrichr pattern. It has no paper of its own; the site asks users to cite the Enrichr papers. The site states no license or terms of use (its terms section is empty), and the source code is not public.