---
activity_status: active
category: DataSource
creation_date: '2026-01-28T00:00:00Z'
description: A pathway mapping and harmonization framework for integrating and comparing
  pathway knowledge across multiple pathway databases.
domains:
- pathways
- biological systems
homepage_url: https://compath.scai.fraunhofer.de/
id: compath
last_modified_date: '2026-02-15T00:00:00Z'
layout: resource_detail
name: ComPath
products:
- category: GraphicalInterface
  description: Main ComPath portal for pathway database harmonization and analysis.
  format: http
  id: compath.portal
  name: ComPath Portal
  product_url: https://compath.scai.fraunhofer.de/
- category: GraphicalInterface
  description: Overview interface for pathway databases integrated in ComPath.
  format: http
  id: compath.overview
  name: ComPath Overview
  product_url: https://compath.scai.fraunhofer.de/overview
- category: GraphicalInterface
  description: Interface for pathway similarity comparisons.
  format: http
  id: compath.similarity
  name: ComPath Similarity Explorer
  product_url: https://compath.scai.fraunhofer.de/similarity
- category: GraphicalInterface
  description: Catalog interface for browsing curated pathway mappings.
  format: http
  id: compath.catalog
  name: ComPath Catalog
  product_url: https://compath.scai.fraunhofer.de/catalog
- category: DocumentationProduct
  description: Curation protocol and methodology documentation for ComPath mappings.
  format: http
  id: compath.curation-protocol
  name: ComPath Curation Protocol
  product_url: https://compath.scai.fraunhofer.de/curation_protocol
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
  - uci
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
  - uci
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
  - uci
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
  - uci
  - omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
synonyms:
- ComPath
---
# ComPath

ComPath is a framework and web resource for integrating, comparing, and curating mappings
across pathway knowledge databases.
