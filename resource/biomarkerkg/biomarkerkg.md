---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  label: MaayanLab
description: Biomarker Knowledge Graph (BKG) is a comprehensive resource for biomarker
  data that integrates multiple biomedical resources to connect biomarkers with anatomical
  structures, compounds, conditions, roles, and variants.
domains:
- health
- biological systems
homepage_url: https://bkg.dev.maayanlab.cloud/
id: biomarkerkg
layout: resource_detail
name: Biomarker Knowledge Graph
products:
- category: GraphicalInterface
  description: Web interface to explore and query the Biomarker Knowledge Graph
  id: biomarkerkg.site
  name: BKG Explorer
  original_source:
  - biomarkerkg
  product_url: https://bkg.dev.maayanlab.cloud/
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Nodes from Uber-Anatomy Ontology
  format: csv
  id: biomarkerkg.nodes.anatomy
  name: BKG Anatomy Nodes
  original_source:
  - uberon
  product_file_size: 332
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Anatomy.nodes.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Nodes from GlyGen Biomarker Database
  format: csv
  id: biomarkerkg.nodes.biomarker
  name: BKG Biomarker Nodes
  original_source:
  - glygen
  product_file_size: 1252064
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Biomarker.nodes.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Nodes from PubChem Database
  format: csv
  id: biomarkerkg.nodes.compound
  name: BKG Compound Nodes
  original_source:
  - pubchem
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Compound.nodes.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Nodes from Human Disease Ontology
  format: csv
  id: biomarkerkg.nodes.condition
  name: BKG Condition Nodes
  original_source:
  - do
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Condition.nodes.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Nodes from OBCI
  format: csv
  id: biomarkerkg.nodes.role
  name: BKG Role Nodes
  original_source:
  - biomarkerkg
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Role.nodes.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Nodes from dbSNP
  format: csv
  id: biomarkerkg.nodes.variant
  name: BKG Variant Nodes
  original_source:
  - dbsnp
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Variant.nodes.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Biomarker to Anatomy relationships (determined_using_sample_from)
  format: csv
  id: biomarkerkg.edges.anatomy
  name: BKG Anatomy Edges
  original_source:
  - biomarkerkg
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Anatomy.edges.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Biomarker to Compound relationships (indicated_by_above_normal_level_of,
    indicated_by_below_normal_level_of)
  format: csv
  id: biomarkerkg.edges.compound
  name: BKG Compound Edges
  original_source:
  - biomarkerkg
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Compound.edges.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Biomarker to Condition relationships (diagnostic_for, indicates_risk_of_developing,
    prognostic_for)
  format: csv
  id: biomarkerkg.edges.condition
  name: BKG Condition Edges
  original_source:
  - biomarkerkg
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Condition.edges.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Biomarker to Role relationships (has_best_classification)
  format: csv
  id: biomarkerkg.edges.role
  name: BKG Role Edges
  original_source:
  - biomarkerkg
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Role.edges.zip
  secondary_source:
  - biomarkerkg
- category: GraphProduct
  compression: zip
  description: Biomarker to Variant relationships (indicated_by_presence_of)
  format: csv
  id: biomarkerkg.edges.variant
  name: BKG Variant Edges
  original_source:
  - biomarkerkg
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Variant.edges.zip
  secondary_source:
  - biomarkerkg
repository: https://github.com/MaayanLab/BiomarkerKG
---
The Biomarker Knowledge Graph (BKG) is a comprehensive resource that integrates biomarker data across multiple dimensions including anatomical structures, compounds, conditions, roles, and variants. This knowledge graph serves as a centralized platform for biomarker research, enabling researchers to explore complex relationships between biomarkers and various biological and clinical entities.

BKG supports biomarker discovery, validation, and application by connecting heterogeneous biomedical data sources into a unified graph structure. The platform includes an interactive explorer tool for visualization and analysis of biomarker relationships, as well as downloadable datasets for integration with other bioinformatics workflows.