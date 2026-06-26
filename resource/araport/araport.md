---
activity_status: inactive
category: DataSource
collection:
- ber
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
  and Phytozome, and is used by downstream resources such as the Stress Knowledge
  Map.
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
  description: ThaleMine, the InterMine-based data warehouse originally developed
    for Araport, now hosted at the Bio-Analytic Resource for Plant Biology (BAR),
    serving Araport11-based gene and functional data.
  format: http
  id: araport.thalemine
  name: ThaleMine (BAR)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: araport
  product_url: https://bar.utoronto.ca/thalemine/
- category: GraphProduct
  description: Current PSS model in Systems Biology Graphical Notation XML format
  format: sbgnml
  id: skm.pss.live.sbgn
  name: PSS Live Download (SBGN-ML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 3204548
  product_url: https://skm.nib.si/downloads/pss/public/sbgn
- category: GraphProduct
  description: Current PSS model in Systems Biology Markup Language XML format
  format: sbml
  id: skm.pss.live.sbml
  name: PSS Live Download (SBML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 548527
  product_url: https://skm.nib.si/downloads/pss/public/sbml
- category: GraphProduct
  description: PSS model (v1.0.0, October 2023) in DOT Language format compatible
    with Graphviz. The live/current DOT export endpoint was retired upstream; this
    points to the latest published versioned DOT export.
  format: dot
  id: skm.pss.live.dot
  name: PSS Download (DOT, v1.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 405988
  product_url: https://skm.nib.si/downloads/pss-version/v1.0.0/graphviz
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are represented as nodes (as in PSS Explorer and database schema).
  format: sif
  id: skm.pss.live.sif.original.graph
  name: PSS Live Download, original (SIF/LGL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 161651
  product_url: https://skm.nib.si/downloads/pss/public/sif-edges
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are represented as nodes (as in PSS Explorer and database schema). This
    file contains the node annotations.
  format: sif
  id: skm.pss.live.sif.original.annotations
  name: PSS Live Download, original (SIF/LGL), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 401897
  product_url: https://skm.nib.si/downloads/pss/public/sif-nodes
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges.
  format: sif
  id: skm.pss.live.sif.projection.graph
  name: PSS Live Download, projection (SIF/LGL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 253631
  product_url: https://skm.nib.si/downloads/pss/public/rxn-edges
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges. This file contains the node annotations.
  format: sif
  id: skm.pss.live.sif.projection.annotations
  name: PSS Live Download, projection (SIF/LGL), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 163587
  product_url: https://skm.nib.si/downloads/pss/public/rxn-nodes
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges, FunctionalClusters are expanded to arabidopsis
    identifiers.
  format: sif
  id: skm.pss.live.sif.dinar.graph
  name: PSS Live Download, DiNAR (SIF/LGL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 361747
  product_url: https://skm.nib.si/downloads/pss/public/dinar-edges
- category: GraphProduct
  description: Current PSS model in Boolean network format compatible with BoolDog
    and BoolNet
  format: boolnet
  id: skm.pss.live.boolnet.graph
  name: PSS Live Downloads (BoolNet)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 53198
  product_url: https://skm.nib.si/downloads/pss/public/boolnet
- category: GraphProduct
  description: Current PSS model in Boolean network format compatible with BoolDog
    and BoolNet. This file contains the node annotations.
  format: boolnet
  id: skm.pss.live.boolnet.annotations
  name: PSS Live Downloads (BoolNet), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 70946
  product_url: https://skm.nib.si/downloads/pss/public/boolnet-annot
- category: GraphProduct
  description: Comprehensive Knowledge Network v2 in SIF/LGL format with 26,234 entities
    and ~500,000 interactions
  edge_count: 500000
  format: sif
  id: skm.ckn.v2.graph
  name: CKN v2 (June 2023)
  node_count: 26234
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 2732107
  product_url: https://skm.nib.si/downloads/ckn/v2-2023.06/edges
- category: GraphProduct
  description: Comprehensive Knowledge Network v2 in SIF/LGL format with 26,234 entities
    and ~500,000 interactions. This file contains the node annotations.
  format: sif
  id: skm.ckn.v2.annotations
  name: CKN v2 (June 2023), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 885747
  product_url: https://skm.nib.si/downloads/ckn/v2-2023.06/nodes
- category: GraphProduct
  description: Comprehensive Knowledge Network v1 in SIF/LGL format
  format: sif
  id: skm.ckn.v1.graph
  name: CKN v1 (June 2018)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 318666
  product_url: https://skm.nib.si/downloads/ckn/v1-2018.06/edges
- category: GraphProduct
  description: Comprehensive Knowledge Network v1 in SIF/LGL format. This file contains
    the node annotations.
  format: sif
  id: skm.ckn.v1.annotations
  name: CKN v1 (June 2018), node annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skm
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: araport
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_file_size: 702407
  product_url: https://skm.nib.si/downloads/ckn/v1-2018.06/nodes
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