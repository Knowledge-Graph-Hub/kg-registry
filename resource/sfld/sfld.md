---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://sfld.rbvi.ucsf.edu/
  label: SFLD - University of California, San Francisco
creation_date: '2026-06-17T00:00:00Z'
description: The Structure-Function Linkage Database (SFLD) is a resource that links
  enzyme sequence, structure, and chemical function. It organizes functionally
  diverse enzyme superfamilies by mapping the specific chemical reactions catalyzed
  by members to the conserved structural features that enable those reactions.
domains:
- proteomics
- chemistry and biochemistry
homepage_url: http://sfld.rbvi.ucsf.edu/
id: sfld
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: Structure-Function Linkage Database
products:
- category: GraphicalInterface
  description: Web interface for browsing enzyme superfamilies and their sequence,
    structure, and function relationships.
  format: http
  id: sfld.site
  is_public: true
  name: SFLD Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sfld
  product_url: http://sfld.rbvi.ucsf.edu/
publications:
- authors:
  - Eyal Akiva
  - Shoshana Brown
  - Daniel E. Almonacid
  - Alan E. Barber
  - Ashley F. Custer
  - Michael A. Hicks
  - Conrad C. Huang
  - Florian Lauck
  - Susan T. Mashiyama
  - Elaine C. Meng
  - David Mischel
  - John H. Morris
  - Sunil Ojha
  - Alexandra M. Schnoes
  - Doug Stryke
  - Jeffrey M. Yunes
  - Thomas E. Ferrin
  - Gemma L. Holliday
  - Patricia C. Babbitt
  doi: 10.1093/nar/gkt1130
  id: https://doi.org/10.1093/nar/gkt1130
  journal: Nucleic Acids Research
  preferred: true
  title: The Structure-Function Linkage Database
  year: '2014'
---
# Structure-Function Linkage Database

The Structure-Function Linkage Database (SFLD) is a manually curated resource that
describes the relationships between the sequences, structures, and chemical functions of
enzymes within functionally diverse superfamilies. It hierarchically links the partial
reactions and conserved active-site features that underlie enzyme chemistry.

Content includes:

- Functionally diverse enzyme superfamilies organized by subgroup and family
- Mappings between conserved structural features and catalyzed chemical reactions
- Sequence and structure annotations supporting functional inference

GeneCards integrates enzyme structure-function relationships from SFLD.
