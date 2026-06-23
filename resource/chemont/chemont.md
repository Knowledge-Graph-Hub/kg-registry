---
activity_status: active
category: Ontology
creation_date: '2025-12-11T00:00:00Z'
description: ChemOnt (Chemical Ontology) is a comprehensive chemical ontology that
  provides a hierarchical classification of chemical entities. It is designed to support
  chemical informatics applications and enable semantic integration of chemical data
  across biomedical systems. ChemOnt is developed and maintained by the Wishart Lab
  and integrates chemical structures with ontological classifications.
domains:
- chemistry and biochemistry
homepage_url: http://classyfire.wishartlab.com/
id: chemont
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
name: ChemOnt
products:
- category: GraphicalInterface
  description: ClassyFire web interface for chemical classification and ontology exploration
  format: http
  id: chemont.classyfire
  name: ClassyFire Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chemont
  product_url: http://classyfire.wishartlab.com/
- category: OntologyProduct
  description: ChemOnt OBO format ontology file (version 2.1)
  format: obo
  id: chemont.obo
  name: ChemOnt OBO Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chemont
  product_file_size: 307900
  product_url: http://classyfire.wishartlab.com/system/downloads/1_0/chemont/ChemOnt_2_1.obo.zip
- category: GraphProduct
  description: Downloadable knowledge graph dump in TAR/GZ format containing complete
    FORUM data
  format: mixed
  id: forum.graph.dump
  name: FORUM Knowledge Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cheminf
  - relation_type: prov:hadPrimarySource
    source: chemont
  - relation_type: prov:hadPrimarySource
    source: cito
  - relation_type: prov:hadPrimarySource
    source: dc
  - relation_type: prov:hadPrimarySource
    source: fabio
  - relation_type: prov:hadPrimarySource
    source: forum
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: skos
  product_url: ftp://forum:Forum2021Cov!@ftp.semantic-metabolomics.org/dumps/2021/share.tar.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ FTP error_ timed
    out
  - 'File was not able to be retrieved when checked on 2026-06-18: FTP error: timed
    out'
  - 'File was not able to be retrieved when checked on 2026-06-22: FTP error: timed
    out'
publications:
- authors:
  - Djoumbou Feunang Y
  - Eisner R
  - Knox C
  - Chepelev L
  - Hastings J
  - Owen G
  - Fahy E
  - Steinbeck C
  - Subramanian S
  - Bolton E
  - Greiner R
  - Wishart DS
  doi: 10.1186/s13321-016-0174-y
  id: https://www.ncbi.nlm.nih.gov/pubmed/27867422
  journal: J Cheminform
  preferred: true
  title: 'ClassyFire: automated chemical classification with a comprehensive, computable
    taxonomy'
  year: '2016'
repository: https://github.com/wishartlab/chemontology
---
ChemOnt