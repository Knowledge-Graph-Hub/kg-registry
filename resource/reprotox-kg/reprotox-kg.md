---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: MaayanLab
  - contact_type: url
    value: https://maayanlab.cloud/
  label: Ma'ayan Lab
creation_date: '2025-09-23T00:00:00Z'
description: ReproTox-KG is a knowledge graph for structural birth defects and reproductive
  toxicology that integrates literature-derived and chemical evidence to support exploration
  of drug-birth defect relationships.
domains:
- biomedical
- toxicology
- drug discovery
homepage_url: https://maayanlab.cloud/reprotox-kg
id: reprotox-kg
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (no derivatives) among its sources: hp. Not accounted for, no known license:
    faers, lincs-l1000, sigcom-lincs.'
  id: https://hpo.jax.org/app/license
  inferred_from:
  - hp
  label: HPO License (free for any use with attribution and version display; content
    may not be altered)
  restrictiveness: no derivatives
  status: inferred
  unresolved_sources:
  - faers
  - lincs-l1000
  - sigcom-lincs
name: ReproTox-KG
products:
- category: GraphicalInterface
  description: Public web interface for querying and exploring ReproTox-KG relationships.
  format: http
  id: reprotox-kg.portal
  name: ReproTox-KG Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://maayanlab.cloud/reprotox-kg
- category: ProcessProduct
  description: Source repository for the ReproTox-KG website assets, schema, and ingestion
    notebooks.
  format: http
  id: reprotox-kg.code
  name: ReproTox-KG Source Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  product_url: https://github.com/MaayanLab/Reprotox-KG
- category: Product
  description: Knowledge graph schema definition used by ReproTox-KG.
  format: json
  id: reprotox-kg.schema
  name: ReproTox-KG Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  product_file_size: 15573
  product_url: https://github.com/MaayanLab/Reprotox-KG/blob/main/schema.json
- category: Product
  description: Downloads page listing the ReproTox-KG graph serializations and supporting
    tables (gene susceptibility scores, predicted placental crossing, birth defect
    frequencies, phenotype lists, and topology measures).
  format: http
  id: reprotox-kg.data
  name: ReproTox-KG Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://maayanlab.cloud/reprotox-kg/downloads
- category: GraphProduct
  description: Core ReproTox-KG graph linking birth defects, drugs, and genes from DrugShot, DrugEnrichr, and GeneShot literature co-mention evidence (1,433 nodes, 2,252 edges).
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
- category: GraphProduct
  description: Drug-to-gene up- and down-regulation edges from SigCom LINCS L1000 signatures (8,942 nodes, 225,509 edges).
  format: json
  id: reprotox-kg.graph.sigcom-lincs
  name: ReproTox-KG SigCom LINCS Drug-Gene Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  product_file_size: 114587395
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/sigcom_lincs_serialization.valid.json
- category: GraphProduct
  description: Drug-drug cosine similarity edges computed from LINCS L1000 signatures (4,523 nodes, 20,785 edges).
  format: json
  id: reprotox-kg.graph.drug-similarity
  name: ReproTox-KG LINCS Drug Similarity Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 15033998
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/sigcom_lincs_drug_similarity.valid.json
- category: GraphProduct
  description: Drug to birth defect associations from FAERS reports with male exposure (117 nodes, 179 edges).
  format: json
  id: reprotox-kg.graph.faers-male
  name: ReproTox-KG FAERS Male Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: faers
  product_file_size: 204731
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/drugsto_faers_male.valid.json
- category: GraphProduct
  description: Drug to birth defect associations from FAERS reports with female exposure (126 nodes, 193 edges).
  format: json
  id: reprotox-kg.graph.faers-female
  name: ReproTox-KG FAERS Female Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: faers
  product_file_size: 211020
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/drugsto_faers_female.valid.json
- category: GraphProduct
  description: Gene to birth defect phenotype associations from the Human Phenotype Ontology (5,152 nodes, 125,458 edges).
  format: json
  id: reprotox-kg.graph.hpo
  name: ReproTox-KG HPO Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: hp
  product_file_size: 50847638
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/hpo.valid.json
- category: GraphProduct
  description: Gene-gene positive and negative coexpression edges from ARCHS4 (17,964 nodes, 170,801 edges).
  format: json
  id: reprotox-kg.graph.archs4
  name: ReproTox-KG ARCHS4 Coexpression Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: archs4
  product_file_size: 93780518
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/archs4_coexpression.valid.json
- category: GraphProduct
  description: Birth defect phenotype to drug associations from DrugShot literature co-mentions (2,802 nodes, 12,502 edges).
  format: json
  id: reprotox-kg.graph.drugshot-hpo
  name: ReproTox-KG DrugShot HPO-Drug Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: drugshot
  product_file_size: 8941255
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/Drugshot_HPO_to_Drug.valid.json
- category: GraphProduct
  description: Birth defect phenotype to gene associations from GeneShot literature co-mentions (6,064 nodes, 13,487 edges).
  format: json
  id: reprotox-kg.graph.geneshot-hpo
  name: ReproTox-KG GeneShot HPO-Gene Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: geneshot
  product_file_size: 7214043
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/Geneshot_HPO_to_Gene.valid.json
- category: GraphProduct
  description: Drug-target edges from the Illuminating the Druggable Genome program (2,395 nodes, 7,326 edges).
  format: json
  id: reprotox-kg.graph.idg
  name: ReproTox-KG IDG Drug Target Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_file_size: 6380321
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/idg_drug_targets.valid.json
publications:
- authors:
  - Evangelista JE
  - Clarke DJB
  - Xie Z
  - Marino GB
  - Utti V
  - Jenkins SL
  - Ahooyi TM
  - Bologa CG
  - Yang JJ
  - Binder JL
  - Kumar P
  - Lambert CG
  - Grethe JS
  - Wenger E
  - Taylor D
  - Oprea TI
  - de Bono B
  - Ma'ayan A
  doi: 10.1038/s43856-023-00329-2
  id: PMID:37460679
  journal: Commun Med (Lond)
  preferred: true
  title: Toxicology knowledge graph for structural birth defects
  year: '2023'
repository: https://github.com/MaayanLab/Reprotox-KG
---
# ReproTox-KG

ReproTox-KG is a knowledge graph focused on reproductive toxicology and structural birth defects.

## Current Access Points

- Public interface: https://maayanlab.cloud/reprotox-kg
- Source repository: https://github.com/MaayanLab/Reprotox-KG

## Data

ReproTox-KG has BirthDefect, Gene, and Drug nodes. Its edges come from ARCHS4
coexpression, DrugEnrichr, DrugShot, FAERS, GeneShot, the Human Phenotype Ontology,
IDG drug targets, and SigCom LINCS L1000 signatures. The graph serializations on the
downloads page are dated November 2022; the repository was last updated in August 2023.
Neither the site nor the repository states a license for the data.

## Notes

The legacy reprotox-kg.net endpoints appear to have been retired. This entry now points to the currently maintained Ma'ayan Lab resources and removes stale URL-check warnings tied to the abandoned domain.

## Automated Evaluation

- View the automated evaluation: [reprotox-kg automated evaluation](reprotox-kg_eval_automated.html)