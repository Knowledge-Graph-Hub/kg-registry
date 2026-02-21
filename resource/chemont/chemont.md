---
activity_status: active
category: Ontology
description: ChemOnt (Chemical Ontology) is a comprehensive chemical ontology that
  provides a hierarchical classification of chemical entities. It is designed to support
  chemical informatics applications and enable semantic integration of chemical data
  across biomedical systems. ChemOnt is developed and maintained by the Wishart Lab
  and integrates chemical structures with ontological classifications.
domains:
- chemistry and biochemistry
homepage_url: http://classyfire.wishartlab.com/
id: chemont
layout: resource_detail
name: ChemOnt
products:
- category: GraphicalInterface
  description: ClassyFire web interface for chemical classification and ontology exploration
  id: chemont.classyfire
  name: ClassyFire Web Interface
  product_url: http://classyfire.wishartlab.com/
- category: OntologyProduct
  description: ChemOnt OBO format ontology file (version 2.1)
  format: obo
  id: chemont.obo
  name: ChemOnt OBO Ontology
  product_file_size: 307900
  product_url: http://classyfire.wishartlab.com/system/downloads/1_0/chemont/ChemOnt_2_1.obo.zip
- category: GraphProduct
  description: Downloadable knowledge graph dump in TAR/GZ format containing complete
    FORUM data
  id: forum.graph.dump
  name: FORUM Knowledge Graph Dump
  original_source:
  - mesh
  - chebi
  - cito
  - fabio
  - dc
  - cheminf
  - skos
  - chemont
  - pubchem
  - pubmed
  product_url: ftp://forum:Forum2021Cov!@ftp.semantic-metabolomics.org/dumps/2021/share.tar.gz
  secondary_source:
  - forum
  warnings:
  - File was not able to be retrieved when checked on 2026-02-20_ FTP error_ timed
    out
  - File was not able to be retrieved when checked on 2026-02-20_ FTP error_ timed
    out
  - 'File was not able to be retrieved when checked on 2026-02-21: FTP error: timed
    out'
repository: https://github.com/wishartlab/chemontology
---
ChemOnt