---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: nicolevasilevsky
  label: Nicole Vasilevsky
  orcid: 0000-0001-5208-3432
- category: Individual
  contact_details:
  - contact_type: github
    value: sabrinatoro
  label: Sabrina Toro
  orcid: 0000-0002-4142-7153
description: "The Mondo Disease Ontology (Mondo) aims to harmonize disease definitions\
  \ across the world. The name Mondo comes from the Latin word \u2018mundus\u2019\
  \ and means \u2018for the world.\u2019"
domains:
- health
homepage_url: https://mondo.monarchinitiative.org/
id: mondo
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Mondo Disease Ontology
products:
- category: DataModelProduct
  description: OWL release of MONDO. The Complete ontology with merged imports.
  format: owl
  id: mondo.owl
  name: Mondo Disease Ontology OWL release
  original_source:
  - mondo
  product_file_size: 238595949
  product_url: https://purl.obolibrary.org/obo/mondo.owl
  secondary_source:
  - mondo
- category: DataModelProduct
  description: OBO release of MONDO.
  format: obo
  id: mondo.obo
  name: Mondo Disease Ontology OBO release
  original_source:
  - mondo
  product_file_size: 52503800
  product_url: https://purl.obolibrary.org/obo/mondo.obo
  secondary_source:
  - mondo
- category: DataModelProduct
  description: JSON release of MONDO (obograph json).
  format: json
  id: mondo.json
  name: Mondo Disease Ontology JSON release
  original_source:
  - mondo
  product_file_size: 102814241
  product_url: https://purl.obolibrary.org/obo/mondo.json
  secondary_source:
  - mondo
- category: ProcessProduct
  description: Utility code for supporting the operations of the Human Disease Ontology
  id: do.code.utils
  name: DO.utils
  original_source:
  - do
  product_url: https://github.com/DiseaseOntology/DO.utils
  secondary_source:
  - do
- category: MappingProduct
  description: MONDO SSSOM. Mappings from MONDO identifiers to other namespaces.
  format: sssom
  id: mondo.sssom
  name: MONDO SSSOM
  original_source:
  - do
  - hp
  - hgnc
  product_file_size: 1437457
  product_url: https://raw.githubusercontent.com/monarch-initiative/mondo/refs/heads/master/src/ontology/mappings/mondo.sssom.tsv
  secondary_source:
  - mondo
- category: GraphProduct
  description: Nodes for the Drug Approvals KP, v0.3.9
  format: kgx
  id: drug-approvals-kp.graph.nodes
  name: Drug Approvals KP Graph Nodes
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_file_size: 701451
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.9.tsv
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  description: Edges for the Drug Approvals KP, v0.3.9
  format: kgx
  id: drug-approvals-kp.graph.edges
  name: Drug Approvals KP Graph Edges
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_file_size: 31052966
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_edges_v0.3.9.tsv
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_file_size: 376501785
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  - semmeddb
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2
- category: DataModelProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_file_size: 240665663
  product_url: https://www.ebi.ac.uk/efo/efo.owl
  secondary_source:
  - efo
- category: DataModelProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_file_size: 64058275
  product_url: https://www.ebi.ac.uk/efo/efo.obo
  secondary_source:
  - efo
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - cl
  - clo
  - chebi
  - go
  - hp
  - mondo
  - pw
  - pr
  - ro
  - so
  - uberon
  - vo
  - bioportal
  - clinvar
  - ctd
  - disgenet
  - ensembl
  - genemania
  - hgnc
  - hpa
  - ncbigene
  - medgen
  - reactome
  - string
  - uniprot
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  secondary_source:
  - pheknowlator
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
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
- category: ProgrammingInterface
  description: TRAPI web API for querying MicrobiomeKG
  format: http
  id: microbiomekg.api
  name: MicrobiomeKG Plover API
  original_source:
  - biolink
  - chebi
  - ncbitaxon
  - ncbigene
  - mesh
  - pubchem
  - go
  - mondo
  - ncit
  - efo
  - uniprot
  - rhea
  - pr
  - uberon
  - panther
  - hgnc
  - drugbank
  - eupathdb
  product_url: https://multiomics.transltr.io/mbkp
  secondary_source:
  - microbiomekg
repository: https://github.com/DiseaseOntology/HumanDiseaseOntology
---
MONDO Disease Ontology