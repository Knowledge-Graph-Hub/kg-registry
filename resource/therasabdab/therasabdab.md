---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: opig@stats.ox.ac.uk
  - contact_type: url
    value: https://opig.stats.ox.ac.uk/
  label: Oxford Protein Informatics Group (OPIG)
creation_date: '2026-11-12T00:00:00Z'
description: The Therapeutic Structural Antibody Database (Thera-SAbDab) tracks all
  antibody- and nanobody-derived therapeutics recognized by the World Health Organization
  International Nonproprietary Names (INN) programme, recording their variable domain
  sequences together with format, isotype, targets, companies, approved and investigated
  conditions, and highest clinical trial stage. Each therapeutic is linked to its
  exact (100% sequence identity) and near (95-99%) structural representatives in SAbDab,
  and these structural mappings are refreshed alongside SAbDab's weekly updates. New
  therapeutics are added with each WHO INN list, and clinical status is updated from
  AdisInsight.
domains:
- immunology
- pharmacology
- drug discovery
- proteomics
- protein structure
homepage_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/therasabdab
id: therasabdab
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: Therapeutic Structural Antibody Database (Thera-SAbDab)
products:
- category: GraphicalInterface
  description: Thera-SAbDab search interface for finding therapeutic antibodies by
    INN, target, format, clinical stage or sequence similarity, with summary pages
    linking each therapeutic to its matching SAbDab structures.
  format: http
  id: therasabdab.portal
  name: Thera-SAbDab Search Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: sabdab
  product_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/therasabdab/search/
- category: Product
  description: CSV table of all Thera-SAbDab therapeutics with format, isotype, clinical
    trial stage and status, heavy and light chain variable domain sequences, matching
    SAbDab structures at 100%, 99% and 95-98% sequence identity, INN proposal and
    recommendation years, targets, companies and conditions.
  format: csv
  id: therasabdab.sequences-structures
  name: Thera-SAbDab Sequences and Structures Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_file_size: 636357
  product_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/static/downloads/TheraSAbDab_SeqStruc_OnlineDownload.csv
publications:
- authors:
  - Raybould MIJ
  - Marks C
  - Lewis AP
  - Shi J
  - Bujotzek A
  - Taddese B
  - Deane CM
  doi: 10.1093/nar/gkz827
  id: doi:10.1093/nar/gkz827
  journal: Nucleic Acids Research
  preferred: true
  title: 'Thera-SAbDab: the Therapeutic Structural Antibody Database'
  year: '2020'
rrid: SCR_022093
---
# Therapeutic Structural Antibody Database (Thera-SAbDab)

Thera-SAbDab is a database of antibody and nanobody therapeutics recognized by the WHO INN programme, built by the Oxford Protein Informatics Group (OPIG) under an open-innovation agreement. It records the variable domain sequences and clinical metadata of each therapeutic and maps them to exact and near-identical structures in the Structural Antibody Database (SAbDab), which in turn draws from the Protein Data Bank.

The full therapeutic table can be downloaded as CSV or Excel from the search page. The Thera-SAbDab pages state no data license.
