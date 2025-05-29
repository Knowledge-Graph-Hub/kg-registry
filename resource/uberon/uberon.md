---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
description: An integrated cross-species anatomy ontology representing a variety of
  anatomical structures across taxonomic groups, with a focus on vertebrates and model
  organisms.
domains:
- anatomy and development
- organisms
homepage_url: https://obophenotype.github.io/uberon/
id: uberon
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC-BY-3.0
name: Uber-Anatomy Ontology
products:
- category: DataModelProduct
  description: OWL release of UBERON. The Complete ontology with merged imports.
  format: owl
  id: uberon.owl
  name: UBERON OWL release
  original_source:
  - uberon
  product_url: http://purl.obolibrary.org/obo/uberon.owl
  secondary_source:
  - uberon
- category: DataModelProduct
  description: OBO release of UBERON
  format: obo
  id: uberon.obo
  name: UBERON OBO release
  original_source:
  - uberon
  product_url: http://purl.obolibrary.org/obo/uberon.obo
  secondary_source:
  - uberon
- category: DataModelProduct
  description: Basic edition of UBERON in OWL format, with minimal imports
  format: owl
  id: uberon.basic.owl
  name: UBERON Basic OWL release
  original_source:
  - uberon
  product_url: http://purl.obolibrary.org/obo/uberon/basic.owl
  secondary_source:
  - uberon
- category: GraphProduct
  compression: zip
  description: Nodes from Uber-Anatomy Ontology
  format: csv
  id: biomarkerkg.nodes.anatomy
  name: BKG Anatomy Nodes
  original_source:
  - uberon
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Anatomy.nodes.zip
  secondary_source:
  - biomarkerkg
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
  - do
  - diseases
  - drugcentral
  - go
  - gwas-catalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  secondary_source:
  - spoke
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
  - do
  - diseases
  - drugcentral
  - go
  - gwas-catalog
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
repository: https://github.com/obophenotype/uberon
---
The Uber-Anatomy Ontology (UBERON) is a comprehensive cross-species anatomy ontology representing anatomical structures, cells, and tissues across metazoans. It serves as an integrative resource that connects various species-specific anatomy ontologies and provides a unified framework for comparative analysis.

UBERON covers anatomical structures from high-level anatomical systems down to specific cell types and tissues, with rich relationships between structures including developmental, functional, and topological connections. The ontology is designed to facilitate cross-species queries and comparisons, enabling researchers to identify homologous structures across diverse taxonomic groups.

As a key resource in the biomedical ontology ecosystem, UBERON is widely used in data integration projects, cross-species phenotype analysis, gene expression studies, and as a fundamental component of various knowledge graphs that require anatomical knowledge representation.