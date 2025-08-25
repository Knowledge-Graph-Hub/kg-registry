---
layout: resource_detail
activity_status: active
id: rna-kg
name: RNA-KG
description: An ontology-based KG for representing interactions involving RNA molecules.
domains:
- drug discovery
- biomedical
- health
contacts:
- category: Individual
  label: Emanuele Cavalleri
  contact_details:
  - contact_type: github
    value: emanuelecavalleri
  - contact_type: email
    value: emanuele.cavalleri@unimi.it
homepage_url: https://RNA-KG.biodata.di.unimi.it
repository: https://github.com/AnacletoLAB/RNA-KG
category: KnowledgeGraph
products:
- description: RNA-KG as a Neo4j Dump
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
  dump_format: neo4j
  format: neo4j
  secondary_source:
  - rna-kg
- description: RNA-KG Nodes in CSV format
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
  format: csv
  secondary_source:
  - rna-kg
- description: RNA-KG Edges in CSV format
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
  format: csv
  secondary_source:
  - rna-kg
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
publications:
- doi: 10.1038/s41597-024-03673-7
  id: doi:10.1038/s41597-024-03673-7
  title: An ontology-based knowledge graph for representing interactions involving RNA molecules
- doi: 10.48550/arXiv.2508.07427
  id: doi:10.48550/arXiv.2508.07427
  title: "RNA-KG v2.0: An RNA-centered Knowledge Graph with Properties"
- doi: 10.1093/bioadv/vbaf109
  id: doi:10.1093/bioadv/vbaf109
  title: RNA knowledge-graph analysis through homogeneous embedding methods
creation_date: '2025-08-25T00:00:00Z'
last_modified_date: '2025-08-25T00:00:00Z'
---

RNA-KG: An ontology-based KG for representing interactions involving RNA molecules
