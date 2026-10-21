---
activity_status: orphaned
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/chembio-therapeutics/mlpcnprofiling
  label: Broad Institute, Chemical Biology and Therapeutics
creation_date: '2026-10-19T00:00:00Z'
description: MLPCN Profiling Data is a Broad Institute reference dataset of high-dimensional
  cellular profiling of small molecules screened through the NIH Molecular Libraries
  Probe Production Centers Network (MLPCN). It contains multiplex-cytological (image-based,
  Cell Painting-style) and gene-expression profiles for roughly 30,000 compounds in
  human U2OS cells, spanning diversity-oriented synthesis compounds, chemically diverse
  library compounds, and known bioactive landmark compounds. It was generated to test
  whether diversity of biological measurements, rather than of chemical structure,
  better predicts phenotypic screening performance (Wawer et al., 2014).
domains:
- drug discovery
- high-throughput screening
- cheminformatics
- chemistry and biochemistry
homepage_url: https://www.broadinstitute.org/chembio-therapeutics/mlpcnprofiling
id: mlpcn-profiling
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: MLPCN Profiling Data
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
- category: GraphicalInterface
  description: Broad Institute landing page describing the profiling assays, compound
    sets, and data download links.
  format: http
  id: mlpcn-profiling.portal
  name: MLPCN Profiling Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mlpcn-profiling
  product_url: https://www.broadinstitute.org/chembio-therapeutics/mlpcnprofiling
- category: Product
  compression: zip
  description: Complete archive of multiplex-cytological and gene-expression profiling
    data for the MLP-sponsored compound sets.
  format: mixed
  id: mlpcn-profiling.full-dataset
  name: MLP-sponsored Profiling Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mlpcn-profiling
  product_file_size: 382690558
  product_url: https://data.broadinstitute.org/csoft/mlpcn/Broad.HG005032.ProfilingData.zip
- category: Product
  compression: zip
  description: The profiling data subset accompanying Wawer et al. 2014 (PNAS).
  format: mixed
  id: mlpcn-profiling.pnas2014-dataset
  name: PNAS 2014 Profiling Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mlpcn-profiling
  product_file_size: 327620838
  product_url: https://data.broadinstitute.org/csoft/mlpcn/Broad.PNAS2014.ProfilingData.zip
publications:
- authors:
  - Mathias J. Wawer
  - Kejie Li
  - Sigrun M. Gustafsdottir
  - Vebjorn Ljosa
  - Nicole E. Bodycombe
  - et al.
  doi: 10.1073/pnas.1410933111
  id: doi:10.1073/pnas.1410933111
  journal: Proceedings of the National Academy of Sciences
  preferred: true
  title: Toward performance-diverse small-molecule libraries for cell-based phenotypic
    screening using multiplexed high-dimensional profiling
  year: '2014'
taxon:
- NCBITaxon:9606
---
# MLPCN Profiling Data

## Overview

MLPCN Profiling Data is a Broad Institute reference dataset of image-based (Cell Painting-style) morphological profiles and gene-expression profiles for roughly 30,000 small molecules screened through the NIH Molecular Libraries Probe Production Centers Network, in human U2OS cells. It underpins the finding that biological-measurement diversity can predict phenotypic screening performance better than chemical-structure diversity.

## Access

- Portal: Broad landing page with assay descriptions and download links.
- Bulk data: the full MLP-sponsored profiling archive and the PNAS 2014 subset (zipped).

This is a static 2013–2014 release; the pages and downloads are reachable but not actively maintained, so the resource is recorded with an activity status of orphaned.

## Citation

Please cite: Wawer MJ, Li K, Gustafsdottir SM, et al. Toward performance-diverse small-molecule libraries for cell-based phenotypic screening using multiplexed high-dimensional profiling. Proc Natl Acad Sci USA. 2014;111(30):10911–10916. doi:10.1073/pnas.1410933111