---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: emanuelecavalleri
  - contact_type: email
    value: emanuele.cavalleri@unimi.it
  label: Emanuele Cavalleri
creation_date: '2025-08-25T00:00:00Z'
description: An ontology-based KG for representing interactions involving RNA molecules.
domains:
- drug discovery
- biomedical
- health
homepage_url: https://RNA-KG.biodata.di.unimi.it
id: rna-kg
last_modified_date: '2025-08-25T00:00:00Z'
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: RNA-KG
products:
- category: GraphProduct
  description: RNA-KG as a Neo4j Dump
  format: neo4j
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
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
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
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
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
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
  secondary_source:
  - rna-kg
publications:
- doi: 10.1038/s41597-024-03673-7
  id: doi:10.1038/s41597-024-03673-7
  title: An ontology-based knowledge graph for representing interactions involving
    RNA molecules
- doi: 10.48550/arXiv.2508.07427
  id: doi:10.48550/arXiv.2508.07427
  title: 'RNA-KG v2.0: An RNA-centered Knowledge Graph with Properties'
- doi: 10.1093/bioadv/vbaf109
  id: doi:10.1093/bioadv/vbaf109
  title: RNA knowledge-graph analysis through homogeneous embedding methods
repository: https://github.com/AnacletoLAB/RNA-KG
---
RNA-KG: An ontology-based KG for representing interactions involving RNA molecules

## Automated Evaluation

- View the automated evaluation: [rna-kg automated evaluation](rna-kg_eval_automated.html)
