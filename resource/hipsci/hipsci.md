---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.hipsci.org/
  label: Human Induced Pluripotent Stem Cells Initiative (HipSci)
creation_date: '2026-10-19T00:00:00Z'
description: The Human Induced Pluripotent Stem Cells Initiative (HipSci) generated
  a large, systematically characterised reference panel of human induced pluripotent
  stem cell (iPSC) lines from hundreds of phenotypically healthy donors and from cohorts
  of donors with inherited rare diseases, using a standardised derivation pipeline.
  Each line is profiled with assays including genotyping arrays, expression arrays,
  methylation arrays, RNA-seq, exome sequencing, proteomics mass spectrometry and
  high-content cellular phenotyping, with whole-genome sequencing for a subset. The
  data are deposited in EMBL-EBI archives (ENA, EGA, ArrayExpress and PRIDE), and
  the cell lines are available from the ECACC and EBiSC cell banks. The project was
  funded by the Wellcome Trust and the Medical Research Council, with partners including
  the Wellcome Sanger Institute, EMBL-EBI, King's College London, the University of
  Dundee, the University of Cambridge and UCL.
domains:
- cell biology
- biological systems
- genomics
- genetic variation
- gene expression profiling
- epigenomics
- proteomics
- rare disease
- biomedical
homepage_url: https://www.hipsci.org/
id: hipsci
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://www.hipsci.org/
  label: Open access for the open-access healthy volunteer cohort; managed access
    through EGA for other data (no single license stated)
name: Human Induced Pluripotent Stem Cells Initiative (HipSci)
products:
- category: GraphicalInterface
  description: HipSci cell line browser for finding iPSC lines by cohort, donor, assay
    and other attributes, with a page per line giving donor metadata, banking status
    and purchase links (ECACC and EBiSC), BioSamples accession, pluripotency and copy
    number quality information, and links to archived assay data.
  format: http
  id: hipsci.cell-line-browser
  is_public: true
  name: HipSci cell line browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hipsci
  product_url: https://www.hipsci.org/#/lines
- category: GraphicalInterface
  description: HipSci data browser listing assay data files per cell line (assay,
    description, instrument, archive and download link), donor tables and the most
    recent managed-access EGA datasets per cohort and assay, with CSV and TSV export
    of the file and donor tables.
  format: http
  id: hipsci.data-browser
  is_public: true
  name: HipSci data browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hipsci
  product_url: https://www.hipsci.org/#/data
publications:
- authors:
  - Ian Streeter
  - Peter W. Harrison
  - Adam Faulconbridge
  - The HipSci Consortium
  - Paul Flicek
  - Helen Parkinson
  - Laura Clarke
  doi: 10.1093/nar/gkw928
  id: https://doi.org/10.1093/nar/gkw928
  journal: Nucleic Acids Research
  preferred: true
  title: The human-induced pluripotent stem cell initiative-data resources for cellular
    genetics
  year: '2017'
- authors:
  - Helena Kilpinen
  - Angela Goncalves
  - Andreas Leha
  - Vackar Afzal
  - Kaur Alasoo
  - Sofie Ashford
  - Sendu Bala
  - Dalila Bensaddek
  - Francesco Paolo Casale
  - Oliver J. Culley
  - Petr Danecek
  - Adam Faulconbridge
  - Peter W. Harrison
  - Annie Kathuria
  - Davis McCarthy
  - Shane A. McCarthy
  - Ruta Meleckyte
  - Yasin Memari
  - Nathalie Moens
  - Filipa Soares
  - Alice Mann
  - Ian Streeter
  - Chukwuma A. Agu
  - Alex Alderton
  - Rachel Nelson
  - Sarah Harper
  - Minal Patel
  - Alistair White
  - Sharad R. Patel
  - Laura Clarke
  - Reena Halai
  - Christopher M. Kirton
  - Anja Kolb-Kokocinski
  - Philip Beales
  - Ewan Birney
  - Davide Danovi
  - Angus I. Lamond
  - Willem H. Ouwehand
  - Ludovic Vallier
  - Fiona M. Watt
  - Richard Durbin
  - Oliver Stegle
  - Daniel J. Gaffney
  doi: 10.1038/nature22403
  id: https://doi.org/10.1038/nature22403
  journal: Nature
  title: Common genetic variation drives molecular heterogeneity in human iPSCs
  year: '2017'
---
# Human Induced Pluripotent Stem Cells Initiative (HipSci)

## Overview

HipSci set out to build a large, high-quality reference panel of human induced
pluripotent stem cell (iPSC) lines for the research community. Lines were generated
from hundreds of donors with a standardised derivation pipeline, and each line was
extensively characterised. The 2017 Nature paper describes 711 iPSC lines from 301
healthy individuals. The panel also includes cohorts of donors with inherited rare
diseases, contributed by clinical partners such as the NIHR BioResource and UCL
institutes.

The project was funded by the Wellcome Trust and the Medical Research Council and
brought together the Wellcome Sanger Institute, EMBL-EBI, King's College London, the
University of Dundee, the University of Cambridge and UCL.

## Data Content

- Genotyping arrays and expression arrays on candidate iPSC lines and their parent
  somatic cells (used for quality control, including PluriTest pluripotency scores and
  copy number checks).
- RNA-seq, whole-exome sequencing and methylation arrays on lines selected for banking.
- Deep (30x) whole-genome sequencing for a subset of about 150 donors.
- Proteomics mass spectrometry (University of Dundee).
- High-content cellular phenotyping (King's College London).
- Donor metadata such as sex, age, ethnicity, disease status and tissue provider.

## Access

- Cell line browser: https://www.hipsci.org/#/lines
- Data browser: https://www.hipsci.org/#/data
- Data are archived at EMBL-EBI in ENA, EGA, ArrayExpress and PRIDE. Managed-access
  data are distributed by the European Genome-phenome Archive (EGA); access is requested
  through the Wellcome Sanger Institute's Electronic Data Access Mechanism.
- Cell lines are available from ECACC (academic researchers) and EBiSC (commercial
  users).

## License

HipSci does not publish a single data license. Data from the open-access healthy
volunteer cohort are openly available through the EMBL-EBI archives; other data are
under managed access through EGA and require an approved data access application.
