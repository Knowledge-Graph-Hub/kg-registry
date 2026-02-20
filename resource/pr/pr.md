---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: dan5@georgetown.edu
  - contact_type: github
    value: nataled
  label: Darren Natale
  orcid: 0000-0001-5809-9523
description: An ontological representation of protein-related entities
domains:
- chemistry and biochemistry
homepage_url: http://proconsortium.org
id: pr
infores_id: pr
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: PRotein Ontology (PRO)
products:
- category: OntologyProduct
  description: PRO after reasoning has been applied, OWL format. Add '.gz' for compressed.
  format: owl
  id: pr.owl
  name: pro_reasoned.owl
  product_url: http://purl.obolibrary.org/obo/pr.owl
- category: OntologyProduct
  description: PRO after reasoning has been applied, OBO format.
  format: obo
  id: pr.obo
  name: pro_reasoned.obo
  product_url: http://purl.obolibrary.org/obo/pr.obo
- category: OntologyProduct
  description: PRO without reasoning applied, OWL format. Add '.gz' for compressed.
  format: owl
  id: pr-asserted.owl
  name: pro_nonreasoned.owl
  product_url: http://purl.obolibrary.org/obo/pr-asserted.owl
  warnings:
  - 'File was not able to be retrieved when checked on 2026-02-20: HTTP 404 error
    when accessing file'
- category: OntologyProduct
  description: PRO without reasoning applied, OBO format.
  format: obo
  id: pr-asserted.obo
  name: pro_nonreasoned.obo
  product_url: http://purl.obolibrary.org/obo/pr-asserted.obo
  warnings:
  - 'File was not able to be retrieved when checked on 2026-02-20: HTTP 404 error
    when accessing file'
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - ctd
  - doid
  - go
  - chebi
  - reactome
  - interpro
  - hp
  - cl
  - pr
  - uberon
  - ncbitaxon
  - hetionet
  - complexportal
  - rnacentral
  - mirtarbase
  - unii
  - biolink
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
  secondary_source:
  - mechreponet
- category: OntologyProduct
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
  - doid
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
- category: OntologyProduct
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
  - doid
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
  compatibility:
  - standard: biolink
  compression: zip
  description: Curated mechanistic drug–disease paths comprising the DrugMechDB dataset
    packaged as a downloadable archive.
  dump_format: other
  format: mixed
  id: drugmechdb.graph
  latest_version: 2.0.1
  name: DrugMechDB Graph Dataset
  original_source:
  - go
  - cl
  - mesh
  - chebi
  - drugbank
  - interpro
  - uberon
  - pr
  - ncbitaxon
  - reactome
  - hp
  - uniprot
  product_url: https://doi.org/10.5281/zenodo.8139357
  repository: https://github.com/SuLab/DrugMechDB
  versions:
  - 2.0.1
  - 2.0.0
  - 1.0.2
  - '1.0'
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
repository: https://github.com/PROconsortium/PRoteinOntology
---
## Description

An ontological representation of protein-related entities

## Contacts

- Darren Natale (dan5@georgetown.edu) [ORCID: 0000-0001-5809-9523](https://orcid.org/0000-0001-5809-9523)

## Products

### pro_reasoned.owl

PRO after reasoning has been applied, OWL format. Add '.gz' for compressed.

**URL**: [http://purl.obolibrary.org/obo/pr.owl](http://purl.obolibrary.org/obo/pr.owl)

**Format**: owl

### pro_reasoned.obo

PRO after reasoning has been applied, OBO format.

**URL**: [http://purl.obolibrary.org/obo/pr.obo](http://purl.obolibrary.org/obo/pr.obo)

**Format**: obo

### pro_nonreasoned.owl

PRO without reasoning applied, OWL format. Add '.gz' for compressed.

**URL**: [http://purl.obolibrary.org/obo/pr-asserted.owl](http://purl.obolibrary.org/obo/pr-asserted.owl)

**Format**: owl

### pro_nonreasoned.obo

PRO without reasoning applied, OBO format.

**URL**: [http://purl.obolibrary.org/obo/pr-asserted.obo](http://purl.obolibrary.org/obo/pr-asserted.obo)

**Format**: obo

## Publications

- [Protein Ontology (PRO): enhancing and scaling up the representation of protein entities](https://www.ncbi.nlm.nih.gov/pubmed/27899649)

**Domains**: chemistry and biochemistry

---

*This resource was automatically synchronized from the OBO Foundry registry.*