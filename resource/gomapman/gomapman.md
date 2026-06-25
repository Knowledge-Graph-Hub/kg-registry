---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nib.si/eng
  label: National Institute of Biology (NIB), Slovenia
creation_date: '2026-06-18T00:00:00Z'
description: GoMapMan is a manually curated, open database that integrates, consolidates,
  and visualizes plant gene functional annotations organized within the MapMan ontology,
  a hierarchical scheme of functional "bins" tailored to plant biology. It maps genes
  to MapMan bins across several crop and model plant species, including Arabidopsis,
  potato, and tomato, and harmonizes annotations drawn from multiple sources into
  a single consolidated, expert-reviewed resource. The portal provides interactive
  browsing and visualization of the ontology and gene-to-bin mappings, and its curated
  mappings are widely reused to annotate genes in plant systems-biology and transcriptomics
  analyses. It is an upstream source for the Stress Knowledge Map (SKM).
domains:
- genomics
- pathways
- agriculture
- systems biology
homepage_url: https://gomapman.nib.si/
id: gomapman
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: GoMapMan
products:
- category: GraphicalInterface
  description: Web portal for browsing, searching, and visualizing the MapMan ontology
    and manually curated plant gene functional annotations across supported crop and
    model plant species.
  format: http
  id: gomapman.portal
  name: GoMapMan Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gomapman
  product_url: https://gomapman.nib.si/
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
  - Ramsak Z
  - Baebler S
  - Rotter A
  - Korbar M
  - Mozetic I
  - Usadel B
  - Gruden K
  doi: 10.1093/nar/gkt1056
  id: https://www.ncbi.nlm.nih.gov/pubmed/24194592
  journal: Nucleic Acids Res
  preferred: true
  title: 'GoMapMan: integration, consolidation and visualization of plant gene annotations
    within the MapMan ontology'
  year: '2014'
---
## Description

GoMapMan is a manually curated database developed at the National Institute of
Biology (NIB) in Slovenia that integrates, consolidates, and visualizes plant
gene functional annotations within the MapMan ontology. The MapMan ontology
organizes gene functions into a hierarchy of plant-oriented functional "bins,"
and GoMapMan assigns genes to these bins for a range of crop and model plant
species, including Arabidopsis, potato, and tomato. By bringing together
annotations from multiple upstream sources and subjecting them to expert
curation, GoMapMan produces a harmonized, high-quality set of gene-to-function
mappings that can be browsed and visualized interactively through its web
portal. These curated mappings are reused to annotate genes in plant
systems-biology and transcriptomics workflows, and GoMapMan serves as an
upstream source for the Stress Knowledge Map (SKM).

## Products

- **GoMapMan Web Portal** — a graphical web interface for browsing, searching,
  and visualizing the MapMan ontology and the curated gene functional
  annotations across supported plant species.