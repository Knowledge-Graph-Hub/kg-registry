---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bioinformatics.udel.edu/
  label: University of Delaware Center for Bioinformatics and Computational Biology
creation_date: '2026-06-02T00:00:00Z'
description: eFIP, Extracting Functional Impact of Phosphorylation, is a text-mining
  system for finding literature evidence about phosphorylation-dependent protein-protein
  interactions and functional impacts.
domains:
- biomedical
- literature
- proteomics
homepage_url: http://proteininformationresource.org/efip
id: efip
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: eFIP
products:
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
  - 'File was not able to be retrieved when checked on 2026-06-13: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-15: HTTP 403 error
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
publications:
- authors:
  - Catalina O Tudor
  - Cecilia N Arighi
  - Qinghua Wang
  - Hongzhan Huang
  - Cathy H Wu
  doi: 10.1093/database/bas044
  id: doi:10.1093/database/bas044
  journal: Database
  preferred: true
  title: The eFIP system for text mining of protein interaction networks of phosphorylated
    proteins
  year: '2012'
warnings:
- The original standalone eFIP website is not clearly maintained; eFIP remains documented
  in the literature and as a text-mining source used by iPTMnet.
---
# eFIP

eFIP is a literature text-mining system designed to identify phosphorylation
events and their functional impact on protein interactions. It is also used as
one of the automated text-mining sources represented in iPTMnet.