---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: zhaoxia_zhang@uni-hohenheim.de
  - contact_type: url
    value: https://phosphat.uni-hohenheim.de/
  label: PhosPhAt
creation_date: '2026-06-02T00:00:00Z'
description: PhosPhAt is the Arabidopsis Protein Phosphorylation Site Database, collecting
  experimentally identified Arabidopsis phosphorylation sites, peptide annotations,
  kinase-target relationships, and plant-specific phosphorylation-site prediction
  tools.
domains:
- agriculture
- proteomics
- biological systems
homepage_url: https://phosphat.uni-hohenheim.de/
id: phosphat
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: PhosPhAt
products:
- category: GraphicalInterface
  description: PhosPhAt 4.0 web portal for searching Arabidopsis phosphorylation sites,
    kinase-target relationships, phosphopeptide records, mass spectra, and plant-specific
    phosphorylation-site predictions.
  id: phosphat.portal
  name: PhosPhAt Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphat
  product_url: https://phosphat.uni-hohenheim.de/
- category: Product
  description: Bulk CSV dataset of experimentally identified Arabidopsis phosphorylation
    sites from PhosPhAt 4.0.
  format: csv
  id: phosphat.experimental-sites
  name: PhosPhAt Experimental Sites CSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphat
  product_file_size: 311100115
  product_url: https://phosphat.uni-hohenheim.de/Phosphat_20221017.csv
  warnings: []
- category: Product
  description: PhosPhAt protein-with-motif CSV dataset for Arabidopsis phosphoproteins
    and motif annotations.
  format: csv
  id: phosphat.protein-motif
  name: PhosPhAt Protein with Motif CSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphat
  product_file_size: 52867920
  product_url: https://phosphat.uni-hohenheim.de/pepprotein_motif_2024.csv
  warnings: []
- category: ProcessProduct
  description: PhosPhAt plant-specific phosphorylation-site predictor trained on the
    experimental Arabidopsis serine, threonine, and tyrosine phosphorylation dataset.
  id: phosphat.predictor
  name: PhosPhAt Phosphorylation Site Predictor
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphat
  product_url: https://phosphat.uni-hohenheim.de/phosphat.html
  warnings: []
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
  - Matthias Zulawski
  - Roman Braginets
  - Waltraud X Schulze
  doi: 10.1093/nar/gks1081
  id: doi:10.1093/nar/gks1081
  journal: Nucleic Acids Research
  preferred: true
  title: PhosPhAt goes kinases - searchable protein kinase target information in the
    plant phosphorylation site database PhosPhAt
  year: '2012'
- authors:
  - Petra Durek
  - Rebecca Schmidt
  - Joshua L Heazlewood
  - Alexandra Jones
  - Denise MacLean
  - Alexander Nagel
  - Bettina Kersten
  - Waltraud X Schulze
  doi: 10.1093/nar/gkp810
  id: doi:10.1093/nar/gkp810
  journal: Nucleic Acids Research
  title: 'PhosPhAt: the Arabidopsis thaliana phosphorylation site database. An update'
  year: '2010'
- authors:
  - Joshua L Heazlewood
  - Petra Durek
  - Joachim Hummel
  - Joachim Selbig
  - Wolfram Weckwerth
  - Dirk Walther
  - Waltraud X Schulze
  doi: 10.1093/nar/gkm812
  id: doi:10.1093/nar/gkm812
  journal: Nucleic Acids Research
  title: PhosPhAt, a database of phosphorylation sites in Arabidopsis thaliana and
    a plant-specific phosphorylation site predictor
  year: '2007'
synonyms:
- Arabidopsis Protein Phosphorylation Site Database
taxon:
- NCBITaxon:3702
---
# PhosPhAt

PhosPhAt is an Arabidopsis phosphorylation-site resource with searchable
experimental phosphosite data, kinase-target information, bulk CSV downloads,
and a plant-specific phosphorylation-site predictor.