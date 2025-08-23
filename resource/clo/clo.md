---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: zhengj2007@gmail.com
  - contact_type: github
    value: zhengj2007
  label: Jie Zheng
  orcid: 0000-0002-2999-0103
description: The Cell Line Ontology (CLO) is a community-driven ontology to standardize
  and integrate cell line information and support computer-assisted reasoning.
domains:
- anatomy and development
homepage_url: https://github.com/CLO-Ontology/CLO
id: clo
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC-BY-3.0
name: Cell Line Ontology
products:
- category: DataModelProduct
  description: CLO merged OWL release
  format: owl
  id: clo.owl
  name: CLO OWL
  original_source:
  - clo
  - chebi
  - uberon
  - ncbitaxon
  - do
  - bfo
  - iao
  - dc
  - skos
  - efo
  - ro
  product_file_size: 2121232
  product_url: http://purl.obolibrary.org/obo/clo.owl
  secondary_source:
  - clo
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
publications:
- authors:
  - Sarntivijai S
  - Lin Y
  - Xiang Z
  - Meehan TF
  - Diehl AD
  - Vempati UD
  - Schürer TC
  - et al.
  doi: 10.1186/2041-1480-5-37
  id: doi:10.1186/2041-1480-5-37
  journal: Journal of Biomedical Semantics
  preferred: true
  title: 'CLO: The Cell Line Ontology'
  year: '2014'
repository: https://github.com/CLO-ontology/CLO
---
# Cell Line Ontology

CLO unifies cell line information across sources into a standardized, logically defined
format and provides a foundation for data integration and reasoning.