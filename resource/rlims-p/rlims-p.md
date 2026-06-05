---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://research.bioinformatics.udel.edu/text_mining/rlimsp2/
  label: RLIMS-P
creation_date: '2026-06-02T00:00:00Z'
description: RLIMS-P, the Rule-based Literature Mining System for Protein Phosphorylation,
  is a biomedical text-mining system that extracts protein kinases, substrates, phosphorylation
  sites, and evidence text from phosphorylation-related literature.
domains:
- biomedical
- literature
- proteomics
- biological systems
homepage_url: https://research.bioinformatics.udel.edu/text_mining/rlimsp2/
id: rlims-p
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: RLIMS-P
products:
- category: GraphicalInterface
  description: RLIMS-P web portal for searching phosphorylation information by keywords,
    organisms, date range, and PubMed identifiers, with extracted kinase, substrate,
    site, evidence text, and downloadable results.
  format: http
  id: rlims-p.portal
  name: RLIMS-P Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rlims-p
  product_url: https://research.bioinformatics.udel.edu/text_mining/rlimsp2/
  secondary_source:
  - relation_type: prov:used
    source: pubmed
- category: ProcessProduct
  description: Rule-based text-mining service for extracting protein phosphorylation
    events, including kinase, substrate, phosphorylation site, and textual evidence,
    from PubMed abstracts and selected literature corpora.
  id: rlims-p.text-mining-service
  name: RLIMS-P Text-Mining Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rlims-p
  product_url: https://research.bioinformatics.udel.edu/text_mining/rlimsp2/
  secondary_source:
  - relation_type: prov:used
    source: pubmed
- category: DocumentationProduct
  description: Annotation guidelines used with RLIMS-P protein phosphorylation literature-mining
    tasks.
  format: http
  id: rlims-p.annotation-guidelines
  name: RLIMS-P Annotation Guidelines
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rlims-p
  product_url: https://research.bioinformatics.udel.edu/text_mining/rlimsp2/files/RLIMS-P_AnnotationGuidelines.pdf
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: Current iPTMnet PTM record table with PTM type, source, UniProt protein,
    organism, site, enzyme, relation identifiers, and publication evidence.
  format: tsv
  id: iptmnet.ptm
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC BY-NC-SA 4.0
  name: iPTMnet PTM Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_file_size: 44116546
  product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/ptm.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dbptm
  - relation_type: prov:wasDerivedFrom
    source: dbsno
  - relation_type: prov:wasDerivedFrom
    source: efip
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: nextprot
  - relation_type: prov:wasDerivedFrom
    source: p3db
  - relation_type: prov:wasDerivedFrom
    source: phosphoelm
  - relation_type: prov:wasDerivedFrom
    source: phosphogrid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: phosphat
  - relation_type: prov:wasDerivedFrom
    source: pombase
  - relation_type: prov:wasDerivedFrom
    source: pubtator
  - relation_type: prov:wasDerivedFrom
    source: rlims-p
  - relation_type: prov:wasDerivedFrom
    source: signor
  - relation_type: prov:wasDerivedFrom
    source: uniprot
- category: ProcessProduct
  description: eFIP text-mining workflow for retrieving protein literature, extracting
    phosphorylation mentions, detecting protein-protein interaction mentions, and
    identifying temporal or causal relationships between phosphorylation and interaction
    events.
  id: efip.text-mining-system
  name: eFIP Text-Mining System
  original_source:
  - relation_type: prov:hadPrimarySource
    source: efip
  product_url: https://doi.org/10.1093/database/bas044
  secondary_source:
  - relation_type: prov:used
    source: rlims-p
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
publications:
- authors:
  - Manabu Torii
  - Cecilia N Arighi
  - Gang Li
  - Qinghua Wang
  - Cathy H Wu
  - K Vijay-Shanker
  doi: 10.1109/TCBB.2014.2372765
  id: doi:10.1109/TCBB.2014.2372765
  journal: IEEE/ACM Transactions on Computational Biology and Bioinformatics
  preferred: true
  title: 'RLIMS-P 2.0: a generalizable rule-based information extraction system for
    literature mining of protein phosphorylation information'
  year: '2015'
- doi: 10.1093/database/bau081
  id: doi:10.1093/database/bau081
  journal: Database
  title: RLIMS-P, an online text-mining tool for literature-based extraction of protein
    phosphorylation information
  year: '2014'
synonyms:
- Rule-based Literature Mining System for Protein Phosphorylation
---
# RLIMS-P

RLIMS-P is a rule-based biomedical text-mining system for extracting protein
phosphorylation events from the literature. Its extracted kinase, substrate,
site, and evidence-text records are also used by iPTMnet.