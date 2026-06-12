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
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
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
      - relation_type: prov:used
        source: mesh
      - relation_type: prov:used
        source: uberon
      - relation_type: prov:used
        source: snomedct
    product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_json
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
    title: 'AcuKG: a comprehensive knowledge graph for medical acupuncture'
    year: '2025'
repository: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture
taxon:
  - NCBITaxon:9606
---

AcuKG structures medical acupuncture knowledge for retrieval, decision support,
and ontology-aware analysis across acupoints, anatomy, conditions, evidence, and
therapeutic indications.
