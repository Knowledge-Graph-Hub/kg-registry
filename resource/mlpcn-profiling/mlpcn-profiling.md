---
activity_status: active
category: DataSource
creation_date: '2026-10-19T00:00:00Z'
description: Stub Resource page for mlpcn-profiling. This page was automatically generated
  because it was referenced by other resources.
domains:
- stub
id: mlpcn-profiling
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
name: Mlpcn-profiling
products:
- category: GraphicalInterface
  description: Web portal for browsing and searching predicted and known drug-side
    effect connections by drug or side effect, with side effect-GO term and side effect-phenotype
    networks.
  format: http
  id: sep-l1000.portal
  name: SEP-L1000 Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: offsides
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: mlpcn-profiling
  product_url: http://maayanlab.net/SEP-L1000/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: meddra
  - relation_type: prov:wasInformedBy
    source: drugbank
- category: Product
  compression: gzip
  description: 166-bit MACCS chemical fingerprint matrix for 41,774 drugs and small
    molecules from LINCS L1000 and MLPCN, computed with Open Babel from SMILES.
  format: csv
  id: sep-l1000.maccs-fingerprints
  name: SEP-L1000 MACCS Fingerprints
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mlpcn-profiling
  product_file_size: 1254411
  product_url: http://maayanlab.net/SEP-L1000/downloads/MACCS_bitmatrix.csv.gz
- category: Product
  description: Compound metadata for 41,774 LINCS L1000 and MLPCN small molecules
    with pert_id, name, PubChem CID, and SMILES.
  format: csv
  id: sep-l1000.smiles-metadata
  name: SEP-L1000 Compound SMILES Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mlpcn-profiling
  product_file_size: 4014816
  product_url: http://maayanlab.net/SEP-L1000/downloads/meta_SMILES.csv
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubchem
- category: Product
  compression: gzip
  description: Cell morphology profiles (812 Cell Painting image features) for 19,864
    small molecules from the Broad Institute MLPCN profiling dataset.
  format: csv
  id: sep-l1000.mlpcn-morphology
  name: SEP-L1000 MLPCN Morphological Profiles
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: mlpcn-profiling
  product_file_size: 55418948
  product_url: http://maayanlab.net/SEP-L1000/downloads/MLPCN_morplological_profiles.csv.gz
warnings:
- This is an automatically generated stub page. Please replace with accurate information
  about this resource.
---
# Mlpcn-profiling

This is an automatically generated stub page for mlpcn-profiling. Please update with proper information.