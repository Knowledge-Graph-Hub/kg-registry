---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: yimingli99
    label: Yiming Li
creation_date: '2026-06-12T00:00:00Z'
description: AcuKG is a comprehensive medical acupuncture knowledge graph that integrates acupuncture textbooks, official sources, clinical trials, biomedical literature, and ontology mappings to represent acupoints, anatomical locations, conditions, therapeutic indications, action targets, and evidence relationships.
domains:
  - biomedical
  - clinical
  - anatomy and development
homepage_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture
id: acukg
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: snomedct.'
  id: https://www.snomed.org/snomed-ct/get-snomed
  inferred_from:
  - snomedct
  label: SNOMED CT Affiliate License
  restrictiveness: custom
  status: inferred
  unresolved_sources: []
name: AcuKG
products:
  - category: GraphProduct
    description: Source CSV tables for AcuKG, including acupoint therapeutic actions, indications, anatomy relationships, clinical trial links, and PubMed links.
    edge_count: 11527
    format: csv
    id: acukg.csv
    name: AcuKG CSV tables
    node_count: 1839
    original_source:
      - relation_type: prov:hadPrimarySource
        source: acukg
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: who
      - relation_type: prov:used
        source: mesh
      - relation_type: prov:used
        source: uberon
      - relation_type: prov:used
        source: snomedct
    product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG
  - category: GraphProduct
    description: RDF Turtle representation of AcuKG relationship tables.
    edge_count: 11527
    format: ttl
    id: acukg.rdf
    name: AcuKG RDF Turtle files
    node_count: 1839
    original_source:
      - relation_type: prov:hadPrimarySource
        source: acukg
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: who
      - relation_type: prov:used
        source: mesh
      - relation_type: prov:used
        source: uberon
      - relation_type: prov:used
        source: snomedct
    product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_RDF
  - category: GraphProduct
    description: JSON representation of AcuKG relationship tables.
    edge_count: 11527
    format: json
    id: acukg.json
    name: AcuKG JSON files
    node_count: 1839
    original_source:
      - relation_type: prov:hadPrimarySource
        source: acukg
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: who
      - relation_type: prov:used
        source: mesh
      - relation_type: prov:used
        source: uberon
      - relation_type: prov:used
        source: snomedct
    product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_json
  - category: Product
    description: Multilingual acupoint vocabulary listing the 361 standard acupoint codes with Chinese names, transliterations, English, Pinyin, Korean, and Vietnamese names.
    format: csv
    id: acukg.acupoint-vocabulary
    name: AcuKG local acupoint vocabulary
    original_source:
      - relation_type: prov:hadPrimarySource
        source: acukg
      - relation_type: prov:hadPrimarySource
        source: who
    product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/blob/main/local_acupoint_vocabulary.csv
  - category: Product
    description: List of MeSH descriptor IDs and terms used to normalize the conditions represented in AcuKG.
    format: csv
    id: acukg.mesh-conditions
    name: AcuKG MeSH condition list
    original_source:
      - relation_type: prov:hadPrimarySource
        source: acukg
      - relation_type: prov:wasDerivedFrom
        source: mesh
    product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/blob/main/MeSH-Condition.csv
publications:
- authors:
  - Yiming Li
  - Xueqing Peng
  - Suyuan Peng
  - Jianfu Li
  - Donghong Pei
  - Qin Zhang
  - Yiwei Lu
  - Yan Hu
  - Fang Li
  - Li Zhou
  - Yongqun He
  - Cui Tao
  - Hua Xu
  - Na Hong
  doi: 10.1093/jamia/ocaf179
  id: doi:10.1093/jamia/ocaf179
  journal: Journal of the American Medical Informatics Association
  preferred: true
  title: 'AcuKG: a comprehensive knowledge graph for medical acupuncture'
  year: '2026'
repository: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture
synonyms:
  - Acupuncture Knowledge Graph
taxon:
  - NCBITaxon:9606
---

AcuKG structures medical acupuncture knowledge for retrieval, decision support,
and ontology-aware analysis across acupoints, anatomy, conditions, evidence, and
therapeutic indications.

## Contents

AcuKG contains 1,839 entities (361 acupoints, 230 action targets, 447
indications, 404 anatomical locations, and 397 conditions) and 11,527 relations,
mapped to 1,836 standard concepts in three ontologies (SNOMED CT, UBERON, and
MeSH). Relation types include `direction_of`, `part_of`, `distance_of`,
`near_acupoint`, `located_near`, `has_clinicaltrials`, `has_pubmed`, `treats`,
and `has_target`.

## Sources and construction

Acupoint codes, names, and locations were extracted from the WHO standard
acupuncture point locations guideline; acupoint names, indications, and
traditional actions were collected from the Acufinder.com web resource. Evidence
links come from ClinicalTrials.gov and from PubMed clinical study articles
retrieved with the query in `pubmed_query.txt`. Entities were obtained with
rule-based and machine learning (CRF) named entity recognition and LLM-based
relation extraction, with human review, then mapped to SNOMED CT, UBERON, and
MeSH.

## Access

The graph is distributed in the GitHub repository as CSV tables (`AcuKG/`),
RDF Turtle (`AcuKG_RDF/`), and JSON (`AcuKG_json/`), along with relation subtype
statistics. The authors also used a Neo4j instance of the graph for an LLM
retrieval-augmented question-answering use case, but no public Neo4j endpoint is
provided.

## License

The repository does not declare a license. The license shown on this page is
inferred from its most restrictive source (SNOMED CT).
