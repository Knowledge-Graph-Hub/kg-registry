---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: url
    value: http://www.organchip.cn/about
  label: Zhongze Gu
creation_date: '2026-10-04T00:00:00Z'
description: The Knowledge Graph & Large Language Model-Enhanced Organ on a Chip Database
  (KLOCD) is a web platform for organ-on-a-chip research, drug discovery and toxicology
  from Professor Zhongze Gu's team at Southeast University (Nanjing, China). It consolidates
  data from public sources into sub-databases of drugs, chemicals, gene expression
  datasets, diseases, toxicants, literature, patents and organ-on-chip models. At
  its core is OCKG, an organ-on-chip knowledge graph linking organ chips, diseases,
  genes and compounds, which supports a drug repurposing tool and a retrieval-augmented
  natural language question answering assistant. KLOCD succeeds the Organ-on-a-Chip
  Database (Ocdb) previously served at the same address.
domains:
- drug discovery
- drug repositioning
- toxicology
- biomedical
- machine learning
- information technology
homepage_url: http://www.organchip.cn/
id: klocd
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: ctd, togows, unichem. Not accounted for, no
    known license: gene-expression-omnibus.'
  id: https://ctdbase.org/about/legal.jsp
  inferred_from:
  - ctd
  - togows
  - unichem
  label: Custom
  restrictiveness: custom
  status: inferred
  unresolved_sources:
  - gene-expression-omnibus
name: Knowledge Graph & Large Language Model-Enhanced Organ on a Chip Database
products:
- category: GraphProduct
  description: Organ-on-Chip Knowledge Graph (OCKG) linking organ-on-chip models with
    diseases, genes, compounds and other biomedical entities. Version 1.0 has 76,540
    nodes of 17 types and 2,315,561 relationships of 21 types. It is browsable through
    the KLOCD web interface and underlies its drug repurposing and question answering
    tools.
  format: http
  id: klocd.ockg
  latest_version: '1.0'
  name: Organ-on-Chip Knowledge Graph (OCKG)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: klocd
  product_url: http://www.organchip.cn/search/tools
  versions:
  - '1.0'
  warnings:
  - No bulk download or API is offered; OCKG is available only through the KLOCD web
    interface, and some features require a login.
- category: GraphicalInterface
  description: KLOCD web interface for searching its drug, chemical, gene expression
    dataset, disease, toxicant, literature, patent and organ-on-chip model sub-databases,
    built from PubMed, PubChem, TogoWS, UniChem, DrugBank, ChEMBL, ClinicalTrials.gov,
    AACT, the European Medicines Agency, CTD, NCBI GEO, openFDA and Disease Ontology,
    among other public sources.
  format: http
  id: klocd.portal
  name: KLOCD Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: klocd
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: togows
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: ema
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: doid
  product_url: http://www.organchip.cn/
- category: GraphicalInterface
  description: Drug repurposing tool that uses link prediction and reinforcement learning
    over OCKG to suggest drug candidates for diseases.
  format: http
  id: klocd.drug-repurposing
  name: KLOCD Drug Repurposing
  original_source:
  - relation_type: prov:hadPrimarySource
    source: klocd
  product_url: http://www.organchip.cn/search/tools
- category: GraphicalInterface
  description: Retrieval-augmented question answering assistant that combines OCKG
    data with large language models to answer biomedical questions in natural language.
  format: http
  id: klocd.qa-assistant
  name: KLOCD Intelligent Assistant
  original_source:
  - relation_type: prov:hadPrimarySource
    source: klocd
  product_url: http://www.organchip.cn/search/tools
publications:
- authors:
  - Lincao Jiang
  - Qiwei Li
  - Weicheng Liang
  - Xuan Du
  - Yi Yang
  - Zilin Zhang
  - Lili Xu
  - Jing Zhang
  - Jian Li
  - Zaozao Chen
  - Zhongze Gu
  doi: 10.3390/bioengineering9110685
  id: doi:10.3390/bioengineering9110685
  journal: Bioengineering
  preferred: true
  title: Organ-On-A-Chip Database Revealed - Achieving the Human Avatar in Silicon
  year: '2022'
synonyms:
- KLOCD
- Ocdb
- Organ-on-a-Chip Database
---
# Knowledge Graph & Large Language Model-Enhanced Organ on a Chip Database (KLOCD)

KLOCD is a web platform for organ-on-a-chip research, drug discovery and toxicology.
It consolidates data from public databases into eight sub-databases (drugs,
chemicals, gene expression datasets, diseases, toxicants, literature, patents and
organ-on-chip models) and adds AI tools built on its knowledge graph.

## OCKG

The Organ-on-Chip Knowledge Graph (OCKG) links organ chips, diseases, genes and
compounds. Version 1.0 has 76,540 nodes of 17 types and 2,315,561 relationships of 21
types. It supports two tools:

- **Drug repurposing**: link prediction and reinforcement learning over OCKG to
  predict drug-disease associations.
- **Intelligent assistant**: a retrieval-augmented question answering system that
  combines OCKG data with large language models.

## Data Sources

The Help page lists these sources: PubMed, the FDA, PubChem, TogoWS, UniChem,
DrugBank, ChEMBL, LiverTox, ClinicalTrials.gov, AACT, the CDC, Health Canada, the
European Medicines Agency, CTD and the NCI Biospecimen Research Database. Its "GSA"
gene expression datasets were retrieved from NCBI GEO, and the homepage also links
Disease Ontology and openFDA. For literature that is not open access, KLOCD stores
only titles, abstracts and links.

## History

KLOCD succeeds the Organ-on-a-Chip Database (Ocdb), which a 2022 review from the same
group described at the same address (http://www.organchip.cn/). Ocdb collected
literature, patents, toxicological and pharmaceutical data, and was built on MySQL.

## Access and Terms

KLOCD is served over HTTP only; HTTPS connections failed when checked on 2026-10-03.
Some features require registration and login, and no bulk download or API is offered.
No license is stated: the Help page says all data sources are open-access databases
used according to their own terms. No public contact email was found; the About page
names Professor Zhongze Gu as the team lead.
