---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: frederic.bastian@unil.ch
  - contact_type: github
    value: fbastian
  label: Frederic Bastian
  orcid: 0000-0002-9415-5104
description: An ontology representation of the NCBI organismal taxonomy
domains:
- biological systems
homepage_url: https://github.com/obophenotype/ncbitaxon
id: ncbitaxon
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: NCBI organismal classification
products:
- category: OntologyProduct
  description: Main release
  format: owl
  id: ncbitaxon.owl
  name: Main release
  product_file_size: 1677601760
  product_url: http://purl.obolibrary.org/obo/ncbitaxon.owl
- category: OntologyProduct
  description: OBO Format version of Main release
  format: obo
  id: ncbitaxon.obo
  name: OBO Format version of Main release
  product_file_size: 533396581
  product_url: http://purl.obolibrary.org/obo/ncbitaxon.obo
- category: OntologyProduct
  description: OBOGraphs JSON version of Main release
  format: json
  id: ncbitaxon.json
  name: OBOGraphs JSON version of Main release
  product_file_size: 1981974965
  product_url: http://purl.obolibrary.org/obo/ncbitaxon.json
- category: OntologyProduct
  description: taxslim
  format: owl
  id: ncbitaxon.subsets.taxslim.owl
  name: taxslim
  product_file_size: 37153972
  product_url: http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim.owl
- category: OntologyProduct
  description: taxslim disjointness axioms
  format: owl
  id: ncbitaxon.subsets.taxslim-disjoint-over-in-taxon.owl
  name: taxslim disjointness axioms
  product_file_size: 75476239
  product_url: http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim-disjoint-over-in-taxon.owl
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
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
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
- category: OntologyProduct
  description: OWL release of Monochrom Ontology
  format: owl
  id: chr.model.owl
  name: Monochrom Ontology OWL release
  original_source:
  - ro
  - go
  - ncbitaxon
  - iao
  - geno
  - skos
  - gff
  product_file_size: 102365
  product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
  secondary_source:
  - chr
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
- category: DataModelProduct
  description: The Basic subset of the Plant Trait Ontology in OBO format
  format: obo
  id: to-basic.obo
  latest_version: v2025-05-20
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Plant Trait Ontology Basic OBO
  original_source:
  - to
  - chebi
  - ro
  - ncbitaxon
  - go
  - omo
  - ecto
  - ido
  - oio
  - pato
  - envo
  - ohmi
  - iao
  - omrse
  - obi
  - peco
  - po
  - uberon
  - ogms
  - bfo
  product_file_size: 111996
  product_url: http://purl.obolibrary.org/obo/to/subsets/to-basic.obo
  secondary_source:
  - to
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
repository: https://github.com/obophenotype/ncbitaxon
---
## Description

An ontology representation of the NCBI organismal taxonomy

## Contacts

- Frederic Bastian (frederic.bastian@unil.ch) [ORCID: 0000-0002-9415-5104](https://orcid.org/0000-0002-9415-5104)

## Products

### Main release

Main release

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon.owl](http://purl.obolibrary.org/obo/ncbitaxon.owl)

**Format**: owl

### OBO Format version of Main release

OBO Format version of Main release

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon.obo](http://purl.obolibrary.org/obo/ncbitaxon.obo)

**Format**: obo

### OBOGraphs JSON version of Main release

OBOGraphs JSON version of Main release

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon.json](http://purl.obolibrary.org/obo/ncbitaxon.json)

**Format**: json

### taxslim

taxslim

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim.owl](http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim.owl)

**Format**: owl

### taxslim disjointness axioms

taxslim disjointness axioms

**URL**: [http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim-disjoint-over-in-taxon.owl](http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim-disjoint-over-in-taxon.owl)

**Format**: owl

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*