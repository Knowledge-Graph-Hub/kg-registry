---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.arabidopsis.org/
  label: The Arabidopsis Information Resource (TAIR), Phoenix Bioinformatics
creation_date: '2026-06-18T00:00:00Z'
description: Araport (the Arabidopsis Information Portal) was a J. Craig Venter Institute
  (JCVI) project that provided an integrated data warehouse, genome browser, and analysis
  apps for Arabidopsis thaliana research. Its central product, Araport11, is the complete
  2016/2017 reannotation of the A. thaliana Col-0 reference genome, refining gene
  models and adding non-coding RNAs based on extensive RNA-seq evidence. The Araport
  web portal was retired around 2018 after funding ended, with its data and services
  migrated to TAIR, NCGR, and the Bio-Analytic Resource (BAR/ThaleMine). The Araport11
  gene/locus annotation remains a standard reference annotation, distributed via TAIR
  and Phytozome, and is used by downstream resources such as the Stress Knowledge Map.
domains:
- genomics
- organisms
- agriculture
homepage_url: https://www.araport.org/
id: araport
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Araport (Arabidopsis Information Portal)
products:
- category: DataSource
  description: The Araport11 reannotation of the Arabidopsis thaliana Col-0 reference
    genome (gene models, transcripts, and non-coding RNAs), distributed through the
    JGI Phytozome plant genomics portal.
  format: gff
  id: araport.araport11
  name: Araport11 Genome Annotation (Phytozome)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: araport
  product_url: https://phytozome-next.jgi.doe.gov/info/Athaliana_Araport11
- category: GraphicalInterface
  description: ThaleMine, the InterMine-based data warehouse originally developed for
    Araport, now hosted at the Bio-Analytic Resource for Plant Biology (BAR), serving
    Araport11-based gene and functional data.
  format: http
  id: araport.thalemine
  name: ThaleMine (BAR)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: araport
  product_url: https://bar.utoronto.ca/thalemine/
publications:
- authors:
  - Cheng CY
  - Krishnakumar V
  - Chan AP
  - Thibaud-Nissen F
  - Schobel S
  - Town CD
  doi: 10.1111/tpj.13415
  id: https://www.ncbi.nlm.nih.gov/pubmed/27862469
  journal: Plant J
  preferred: true
  title: 'Araport11: a complete reannotation of the Arabidopsis thaliana reference
    genome'
  year: '2017'
---
# Araport (Arabidopsis Information Portal)

## Description

Araport, the Arabidopsis Information Portal, was a J. Craig Venter Institute
(JCVI) project that delivered an integrated, community-facing data warehouse and
set of web applications for *Arabidopsis thaliana* genomics. Its flagship output
was **Araport11**, a complete reannotation of the *A. thaliana* Col-0 reference
genome published in 2016/2017, which updated gene models and incorporated newly
characterized non-coding RNAs using deep RNA-seq evidence.

After project funding ended, the Araport web portal was sunset around 2018, and
its functionality was distributed across The Arabidopsis Information Resource
(TAIR, arabidopsis.org), the National Center for Genome Resources (NCGR), and
the Bio-Analytic Resource for Plant Biology (BAR). Although the portal itself is
inactive, the Araport11 annotation lives on as a standard reference annotation
served through TAIR and JGI Phytozome, and it is the gene/locus annotation used
by the Stress Knowledge Map (SKM).

## Products

- **Araport11 Genome Annotation (Phytozome)** — the Araport11 reannotation of the
  Arabidopsis Col-0 reference genome (gene models, transcripts, non-coding RNAs),
  distributed via the JGI Phytozome plant genomics portal.
- **ThaleMine (BAR)** — the InterMine-based data warehouse originally built for
  Araport, now hosted at the Bio-Analytic Resource for Plant Biology, serving
  Araport11-based gene and functional data.
