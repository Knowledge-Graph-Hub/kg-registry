---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://glygen.org/contact-us/
  label: GlyGen Team
description: GlyGen is an integrated, data-driven resource for glycoproteins, glycans,
  and carbohydrate-active enzymes, providing researchers with comprehensive, high-quality
  data on glycobiology.
domains:
- chemistry and biochemistry
- biological systems
homepage_url: https://glygen.org/
id: glygen
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: GlyGen
products:
- category: GraphicalInterface
  description: Web interface for exploring GlyGen data
  id: glygen.site
  is_public: true
  name: GlyGen Website
  original_source:
  - glygen
  product_url: https://glygen.org/
  secondary_source:
  - glygen
- category: ProgrammingInterface
  description: RESTful API for accessing GlyGen data
  id: glygen.api
  is_public: true
  name: GlyGen API
  original_source:
  - glygen
  product_url: https://api.glygen.org/
  secondary_source:
  - glygen
- category: GraphicalInterface
  description: Interface for searching GlyGen protein and glycan data
  format: csv
  id: glygen.data.site
  name: GlyGen Data Downloads
  original_source:
  - glygen
  product_url: https://data.glygen.org/
  secondary_source:
  - glygen
- category: GraphProduct
  compression: zip
  description: Nodes from GlyGen Biomarker Database
  format: csv
  id: biomarkerkg.nodes.biomarker
  name: BKG Biomarker Nodes
  original_source:
  - glygen
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Biomarker.nodes.zip
  secondary_source:
  - biomarkerkg
publications:
- authors:
  - Kahsay R
  - Vora J
  - Navelkar R
  - Mousavi R
  - Bittremieux W
  - Bakker H
  - Moremen K
  - Ten F
  - Abrahams D
  - Campbell M
  - Glushka J
  - Ranzinger R
  - York W
  - Haslam S
  - Dell A
  - Packer N
  - Bourne P
  - Azadi P
  - Aoki-Kinoshita K
  - Lisacek F
  - Tiemeyer M
  - Neelamegham S
  doi: doi:10.1093/glycob/cwaa085
  id: doi:10.1093/glycob/cwaa085
  preferred: true
  title: GlyGen - Computational and informatics resources for glycoscience
  year: '2020'
repository: https://github.com/glygener/glygen-backend-api
---
GlyGen is a data integration and dissemination project for carbohydrate and glycoconjugate related data. It provides researchers with a comprehensive, integrated, and unified resource for glycan and glycoprotein information, bringing together data from multiple international data sources and partners.

The database integrates information from multiple sources, including:
- Protein sequences and associated data from UniProt
- Glycan structures from GlyTouCan
- Protein-glycan associations from UniCarbKB
- Glycan binding information from UniLectin
- Carbohydrate enzyme data from CAZy

GlyGen provides both a web interface for human users and programmatic access via a RESTful API for computational applications. The resource supports complex queries across multiple data types and provides visualization tools for glycan structures and protein-glycan interactions.

GlyGen is a collaborative effort between the University of Georgia, George Washington University, and international partners, funded by the National Institutes of Health (NIH) through the National Institute of General Medical Sciences (NIGMS).