---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.rnanut.net/lncrnadisease/
  label: LncRNADisease
creation_date: '2026-06-17T00:00:00Z'
description: LncRNADisease is a database of experimentally supported and predicted
  long non-coding RNA (lncRNA) and disease associations. It also curates lncRNA
  interactions at various molecular levels, including with proteins, RNA, miRNA, and
  DNA, to support studies of lncRNA function in disease.
domains:
- genomics
- clinical
homepage_url: http://www.rnanut.net/lncrnadisease/
id: lncrnadisease
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: LncRNADisease
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching lncRNA-disease associations
    and lncRNA interactions.
  format: http
  id: lncrnadisease.site
  is_public: true
  name: LncRNADisease Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  product_url: http://www.rnanut.net/lncrnadisease/
publications:
- authors:
  - Zhenyu Bao
  - Zhen Yang
  - Zhou Huang
  - Yiran Zhou
  - Qinghua Cui
  - Dong Dong
  doi: 10.1093/nar/gky905
  id: https://doi.org/10.1093/nar/gky905
  journal: Nucleic Acids Research
  preferred: true
  title: 'LncRNADisease 2.0: an updated database of long non-coding RNA-associated diseases'
  year: '2019'
---
# LncRNADisease

LncRNADisease is a curated database of associations between long non-coding RNAs
(lncRNAs) and human diseases. In addition to experimentally supported associations, it
integrates a tool for predicting novel lncRNA-disease associations and curates lncRNA
interactions across multiple molecular levels.

Content includes:

- Experimentally supported lncRNA-disease associations from the literature
- Predicted lncRNA-disease associations
- Curated lncRNA interactions with proteins, RNA, miRNA, and DNA

GeneCards integrates lncRNA-disease association data from LncRNADisease.
