---
category: Product
description: The proprietary clinical knowledge graph content itself, comprising IMO
  clinical interface terminology concepts, hierarchies, clinical relationships, and
  cross-maps to standard code systems including ICD-10-CM, ICD-10, SNOMED CT, CPT,
  LOINC, and RxNorm. Delivered under commercial license through the IMO Health APIs,
  EHR integrations, or bulk data agreements.
format: http
id: imo-knowledge-graph.data
name: IMO Health Knowledge Graph Content
original_source:
- relation_type: prov:hadPrimarySource
  source: imo-knowledge-graph
product_url: https://www.imohealth.com/knowledge-graph/
secondary_source:
- relation_type: prov:wasDerivedFrom
  source: cpt
- relation_type: prov:wasDerivedFrom
  source: icd10
- relation_type: prov:wasDerivedFrom
  source: icd10cm
- relation_type: prov:wasDerivedFrom
  source: loinc
- relation_type: prov:wasDerivedFrom
  source: rxnorm
- relation_type: prov:wasDerivedFrom
  source: snomedct
warnings:
- The knowledge graph content is proprietary and is not available as a public bulk
  download. Access requires a commercial agreement with IMO Health.
layout: product_detail
---
