---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: addiehl@buffalo.edu
  - contact_type: github
    value: addiehl
  label: Alexander Diehl
  orcid: 0000-0001-9990-8331
description: The Cell Ontology is a structured controlled vocabulary for cell types
  in animals.
domains:
- anatomy and development
homepage_url: https://obophenotype.github.io/cell-ontology/
id: cl
infores_id: cl
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Cell Ontology
products:
- category: OntologyProduct
  description: Complete ontology, plus inter-ontology axioms, and imports modules
  format: owl
  id: cl.owl
  name: Main CL OWL edition
  product_file_size: 64529552
  product_url: http://purl.obolibrary.org/obo/cl.owl
- category: OntologyProduct
  description: Complete ontology, plus inter-ontology axioms, and imports modules
    merged in
  format: obo
  id: cl.obo
  name: CL obo format edition
  product_file_size: 16759306
  product_url: http://purl.obolibrary.org/obo/cl.obo
- category: OntologyProduct
  description: Complete ontology, plus inter-ontology axioms, and imports modules
    merged in
  format: json
  id: cl.json
  name: CL OBOGraph-JSON format edition
  product_file_size: 37217868
  product_url: http://purl.obolibrary.org/obo/cl.json
- category: OntologyProduct
  description: Basic version, no inter-ontology axioms
  format: owl
  id: cl.cl-basic.owl
  name: Basic CL
  product_file_size: 8509431
  product_url: http://purl.obolibrary.org/obo/cl/cl-basic.owl
- category: OntologyProduct
  description: Basic version, no inter-ontology axioms
  format: obo
  id: cl.cl-basic.obo
  name: Basic CL (OBO version)
  product_file_size: 2918556
  product_url: http://purl.obolibrary.org/obo/cl/cl-basic.obo
- category: OntologyProduct
  description: Basic version, no inter-ontology axioms
  format: json
  id: cl.cl-basic.json
  name: Basic CL (OBOGraph-JSON version)
  product_file_size: 4955842
  product_url: http://purl.obolibrary.org/obo/cl/cl-basic.json
- category: OntologyProduct
  description: complete CL but with no imports or external axioms
  format: owl
  id: cl.cl-base.owl
  name: CL base module
  product_file_size: 11471475
  product_url: http://purl.obolibrary.org/obo/cl/cl-base.owl
- category: OntologyProduct
  description: complete CL but with no imports or external axioms
  format: obo
  id: cl.cl-base.obo
  name: CL base module (OBO version)
  product_file_size: 3317655
  product_url: http://purl.obolibrary.org/obo/cl/cl-base.obo
- category: OntologyProduct
  description: complete CL but with no imports or external axioms
  format: json
  id: cl.cl-base.json
  name: CL base module (OBOGraph-JSON version)
  product_file_size: 6597689
  product_url: http://purl.obolibrary.org/obo/cl/cl-base.json
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
  - doid
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
  - connectivitymap
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
  - sckan
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
  - doid
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
  - connectivitymap
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
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - pubmed
  - mesh
  - pid
  - doid
  - diseases
  - drugcentral
  - go
  - gwascatalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
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
repository: https://github.com/obophenotype/cell-ontology
taxon:
- NCBITaxon:33208
---
## Description

The Cell Ontology is a structured controlled vocabulary for cell types in animals.

## Contacts

- Alexander Diehl (addiehl@buffalo.edu) [ORCID: 0000-0001-9990-8331](https://orcid.org/0000-0001-9990-8331)

## Products

### Main CL OWL edition

Complete ontology, plus inter-ontology axioms, and imports modules

**URL**: [http://purl.obolibrary.org/obo/cl.owl](http://purl.obolibrary.org/obo/cl.owl)

**Format**: owl

### CL obo format edition

Complete ontology, plus inter-ontology axioms, and imports modules merged in

**URL**: [http://purl.obolibrary.org/obo/cl.obo](http://purl.obolibrary.org/obo/cl.obo)

**Format**: obo

### CL OBOGraph-JSON format edition

Complete ontology, plus inter-ontology axioms, and imports modules merged in

**URL**: [http://purl.obolibrary.org/obo/cl.json](http://purl.obolibrary.org/obo/cl.json)

**Format**: json

### Basic CL

Basic version, no inter-ontology axioms

**URL**: [http://purl.obolibrary.org/obo/cl/cl-basic.owl](http://purl.obolibrary.org/obo/cl/cl-basic.owl)

**Format**: owl

### Basic CL (OBO version)

Basic version, no inter-ontology axioms

**URL**: [http://purl.obolibrary.org/obo/cl/cl-basic.obo](http://purl.obolibrary.org/obo/cl/cl-basic.obo)

**Format**: obo

### Basic CL (OBOGraph-JSON version)

Basic version, no inter-ontology axioms

**URL**: [http://purl.obolibrary.org/obo/cl/cl-basic.json](http://purl.obolibrary.org/obo/cl/cl-basic.json)

**Format**: json

### CL base module

complete CL but with no imports or external axioms

**URL**: [http://purl.obolibrary.org/obo/cl/cl-base.owl](http://purl.obolibrary.org/obo/cl/cl-base.owl)

**Format**: owl

### CL base module (OBO version)

complete CL but with no imports or external axioms

**URL**: [http://purl.obolibrary.org/obo/cl/cl-base.obo](http://purl.obolibrary.org/obo/cl/cl-base.obo)

**Format**: obo

### CL base module (OBOGraph-JSON version)

complete CL but with no imports or external axioms

**URL**: [http://purl.obolibrary.org/obo/cl/cl-base.json](http://purl.obolibrary.org/obo/cl/cl-base.json)

**Format**: json

## Publications

- [The Cell Ontology 2016: enhanced content, modularization, and ontology interoperability.](https://www.ncbi.nlm.nih.gov/pubmed/27377652)

**Domains**: anatomy and development

**Taxon**: NCBITaxon:33208

---

*This resource was automatically synchronized from the OBO Foundry registry.*