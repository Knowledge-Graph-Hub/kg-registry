---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: c.dudek@tu-braunschweig.de
  - contact_type: github
    value: chdudek
  label: Christian-Alexander Dudek
  orcid: 0000-0001-9117-7909
description: A structured controlled vocabulary for the source of an enzyme comprising
  tissues, cell lines, cell types and cell cultures.
domains:
- anatomy and development
homepage_url: http://www.brenda-enzymes.org
id: bto
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: BRENDA tissue / enzyme source
products:
- category: OntologyProduct
  description: BRENDA tissue / enzyme source in OWL format
  format: owl
  id: bto.owl
  name: bto.owl
  product_file_size: 722362
  product_url: http://purl.obolibrary.org/obo/bto.owl
- category: OntologyProduct
  description: BRENDA tissue / enzyme source in OBO format
  format: obo
  id: bto.obo
  name: bto.obo
  product_file_size: 479657
  product_url: http://purl.obolibrary.org/obo/bto.obo
- category: OntologyProduct
  description: BRENDA tissue / enzyme source in JSON format
  format: json
  id: bto.json
  name: bto.json
  product_file_size: 595708
  product_url: http://purl.obolibrary.org/obo/bto.json
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - do
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - do
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
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
repository: https://github.com/BRENDA-Enzymes/BTO
---
## Description

A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

## Contacts

- Christian-Alexander Dudek (c.dudek@tu-braunschweig.de) [ORCID: 0000-0001-9117-7909](https://orcid.org/0000-0001-9117-7909)

## Products

### bto.owl

BRENDA tissue / enzyme source in OWL format

**URL**: [http://purl.obolibrary.org/obo/bto.owl](http://purl.obolibrary.org/obo/bto.owl)

**Format**: owl

### bto.obo

BRENDA tissue / enzyme source in OBO format

**URL**: [http://purl.obolibrary.org/obo/bto.obo](http://purl.obolibrary.org/obo/bto.obo)

**Format**: obo

### bto.json

BRENDA tissue / enzyme source in JSON format

**URL**: [http://purl.obolibrary.org/obo/bto.json](http://purl.obolibrary.org/obo/bto.json)

**Format**: json

## Publications

- [The BRENDA Tissue Ontology (BTO): the first all-integrating ontology of all organisms for enzyme sources](https://www.ncbi.nlm.nih.gov/pubmed/21030441)

**Domains**: anatomy and development

---

*This resource was automatically synchronized from the OBO Foundry registry.*