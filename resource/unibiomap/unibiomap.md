---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: xfd997700@gmail.com
  - contact_type: github
    value: xfd997700
  label: Fanding Xu
  orcid: 0000-0001-7220-8693
creation_date: '2026-01-28T00:00:00Z'
description: UniBioMap (Unified Biomedical knowledge Map) is an AI-ready biomedical
  knowledge graph integrating over 30 heterogeneous resources through robust identifier
  normalization, covering 6 key entity types with 21 million curated relations across
  38 fine-grained types. A confident learning framework assigns reliability scores
  and predicts 34 million high-confidence triples, establishing a foundational resource
  for target identification and machine learning-based biomedical discovery.
domains:
- biomedical
- chemistry and biochemistry
- drug discovery
- genomics
- pathways
- biological systems
- systems biology
- phenotype
- proteomics
homepage_url: https://zhanggroup.org/UniBioMap/
id: unibiomap
last_modified_date: '2026-01-28T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: CC BY-NC 4.0
name: UniBioMap
products:
- category: GraphProduct
  description: Core UniBioMap graph edges file.
  format: csv
  id: unibiomap.links
  name: UniBioMap Graph Links
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 1406201678
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
- category: GraphProduct
  description: Auxiliary UniBioMap graph annotations and metadata.
  format: tsv
  id: unibiomap.auxs
  name: UniBioMap Graph Auxiliaries
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 591290539
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
- category: GraphProduct
  description: Predicted UniBioMap graph edges with confidence scores.
  format: csv
  id: unibiomap.pred
  name: UniBioMap Predicted Graph
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 2484982268
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
- category: GraphProduct
  description: Full unfiltered UniBioMap predicted graph edges file.
  format: csv
  id: unibiomap.pred.full
  name: UniBioMap Predicted Graph (Full)
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
- category: GraphProduct
  description: UniBioMap compound entity descriptions.
  format: json
  id: unibiomap.compound_desc
  name: UniBioMap Compound Descriptions
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/compound_desc.json
  secondary_source:
  - unibiomap
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-02-20: No Content-Length
    header found'
- category: GraphProduct
  description: UniBioMap protein entity descriptions.
  format: json
  id: unibiomap.protein_desc
  name: UniBioMap Protein Descriptions
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/protein_desc.json
  secondary_source:
  - unibiomap
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-02-20: No Content-Length
    header found'
- category: GraphProduct
  description: UniBioMap disease entity descriptions.
  format: json
  id: unibiomap.disease_desc
  name: UniBioMap Disease Descriptions
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/disease_desc.json
  secondary_source:
  - unibiomap
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-02-20: No Content-Length
    header found'
- category: GraphProduct
  description: UniBioMap Gene Ontology entity descriptions.
  format: json
  id: unibiomap.go_desc
  name: UniBioMap GO Descriptions
  original_source:
  - go
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/go_desc.json
  secondary_source:
  - unibiomap
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-02-20: No Content-Length
    header found'
- category: GraphProduct
  description: UniBioMap pathway entity descriptions.
  format: json
  id: unibiomap.pathway_desc
  name: UniBioMap Pathway Descriptions
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/pathway_desc.json
  secondary_source:
  - unibiomap
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-02-20: No Content-Length
    header found'
- category: GraphProduct
  description: UniBioMap phenotype entity descriptions.
  format: json
  id: unibiomap.phenotype_desc
  name: UniBioMap Phenotype Descriptions
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/phenotype_desc.json
  secondary_source:
  - unibiomap
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-02-20: No Content-Length
    header found'
- category: GraphicalInterface
  description: Web interface for browsing UniBioMap resources and documentation.
  format: http
  id: unibiomap.web
  name: UniBioMap Website
  original_source:
  - unibiomap
  product_url: https://zhanggroup.org/UniBioMap/
- category: ProcessProduct
  description: Source code and pipelines used to build the UniBioMap knowledge graph.
  id: unibiomap.code
  name: UniBioMap Code
  original_source:
  - unibiomap
  product_url: https://github.com/xfd997700/UniBioMap
  repository: https://github.com/xfd997700/UniBioMap
repository: https://github.com/xfd997700/UniBioMap
version: 1.0.0
---
UniBioMap