---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: suzia@stanford.edu
  - contact_type: github
    value: suzialeksander
  label: Suzi Aleksander
  orcid: 0000-0001-6787-2901
description: An ontology for describing the function of genes and gene products
domains:
- biological systems
homepage_url: http://geneontology.org/
id: go
infores_id: go
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Gene Ontology
products:
- category: OntologyProduct
  description: The main ontology in OWL. This is self contained and does not have
    connections to other OBO ontologies
  format: owl
  id: go.owl
  name: GO (OWL edition)
  product_file_size: 127608493
  product_url: http://purl.obolibrary.org/obo/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, in obo format
  format: obo
  id: go.obo
  name: GO (OBO Format edition)
  product_file_size: 35266549
  product_url: http://purl.obolibrary.org/obo/go.obo
- category: OntologyProduct
  description: Equivalent to go.owl, in obograph json format
  format: json
  id: go.json
  name: GO (JSON edition)
  product_file_size: 77592125
  product_url: http://purl.obolibrary.org/obo/go.json
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    with subsets of those ontologies
  format: owl
  id: go.extensions.go-plus.owl
  name: GO-Plus
  product_file_size: 235965574
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.owl
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    excluding the external ontologies themselves
  format: owl
  id: go.go-base.owl
  name: GO Base Module
  product_file_size: 160571191
  product_url: http://purl.obolibrary.org/obo/go/go-base.owl
- category: OntologyProduct
  description: As go-plus.owl, in obographs json format
  format: json
  id: go.extensions.go-plus.json
  name: GO-Plus
  product_file_size: 131618305
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.json
- category: OntologyProduct
  description: Basic version of the GO, filtered such that the graph is guaranteed
    to be acyclic and annotations can be propagated up the graph. The relations included
    are is a, part of, regulates, negatively regulates and positively regulates. This
    version excludes relationships that cross the 3 GO hierarchies.
  format: obo
  id: go.go-basic.obo
  name: GO-Basic, Filtered, for use with legacy tools
  product_file_size: 31417323
  product_url: http://purl.obolibrary.org/obo/go/go-basic.obo
- category: OntologyProduct
  description: As go-basic.obo, in json format
  format: json
  id: go.go-basic.json
  name: GO-Basic, Filtered, for use with legacy tools (JSON)
  product_file_size: 67130778
  product_url: http://purl.obolibrary.org/obo/go/go-basic.json
- category: OntologyProduct
  description: Classes added to ncbitaxon for groupings such as prokaryotes
  format: owl
  id: go.extensions.go-taxon-groupings.owl
  name: GO Taxon Groupings
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl
  warnings:
  - 'File was not able to be retrieved when checked on 2025-11-04: HTTP 404 error
    when accessing file'
- category: OntologyProduct
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: owl
  id: go.snapshot.go.owl
  name: GO (OWL edition), daily snapshot release
  product_file_size: 127608493
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: obo
  id: go.snapshot.go.obo
  name: GO (OBO Format edition), daily snapshot release
  product_file_size: 35266549
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.obo
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
  - doid
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
  description: KGX Distribution of KG-Monarch
  edge_count: 14783802
  format: kgx
  id: kg-monarch.graph
  name: KGX Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 230877741
  product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch
  edge_count: 14783802
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl
  name: KGX JSON-L Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 315667976
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: RDF Distribution of KG-Monarch
  edge_count: 14783802
  format: rdfxml
  id: kg-monarch.graph.rdf
  name: RDF Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 879238775
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch
  dump_format: neo4j
  edge_count: 14783802
  id: kg-monarch.graph.neo4j
  name: Neo4j Dump of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 1438250397
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
  secondary_source:
  - kg-monarch
  warnings: []
- category: GraphProduct
  description: DuckDB database of KG-Monarch
  edge_count: 14783802
  id: kg-monarch.graph.duckdb
  name: DuckDB database of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 6827814912
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb
  secondary_source:
  - kg-monarch
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
  description: KGX JSON-Lines Distribution of KG-Monarch (Edges)
  edge_count: 14783802
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl.edges
  name: KGX JSON-L Distribution of KG-Monarch Edges
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 15279494795
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.jsonl
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch (Nodes)
  edge_count: 14783802
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl.nodes
  name: KGX JSON-L Distribution of KG-Monarch Nodes
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 1149505896
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.jsonl
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch Edges
  edge_count: 14783802
  format: neo4j
  id: kg-monarch.graph.neo4j.edges
  name: Neo4j Dump of KG-Monarch Edges
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 4386388748
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.neo4j.csv
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch Nodes
  edge_count: 14783802
  format: neo4j
  id: kg-monarch.graph.neo4j.nodes
  name: Neo4j Dump of KG-Monarch Nodes
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellularComponent
  - biolink:ChemicalEntity
  - biolink:Disease
  - biolink:Gene
  - biolink:Genotype
  - biolink:LifeStage
  - biolink:MolecularActivity
  - biolink:MolecularEntity
  - biolink:NamedThing
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:SequenceVariant
  node_count: 1366818
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:ameliorates_condition
  - biolink:associated_with_increased_likelihood_of
  - biolink:caused_by
  - biolink:causes
  - biolink:colocalizes_with
  - biolink:contraindicated_in
  - biolink:contributes_to
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_mode_of_inheritance
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:model_of
  - biolink:orthologous_to
  - biolink:part_of
  - biolink:participates_in
  - biolink:preventative_for_condition
  - biolink:related_to
  - biolink:subclass_of
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 349573789
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.neo4j.csv
  secondary_source:
  - kg-monarch
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
  - doid
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
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
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
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - chembl
  - sider
  - reactome
  - wikipathways
  - hp
  - nihreporter
  - disgenet
  - pubmed
  - gwascatalog
  - cellmarker
  - go
  - bgee
  - ccle
  - clinicaltrialsgov
  - indra
  product_url: https://github.com/gyorilab/indra_cogex
  secondary_source:
  - indra
- category: MappingProduct
  compression: gzip
  description: Gene to Gene Ontology mapping data providing functional annotations
    for genes
  format: tsv
  id: ncbigene.gene2go
  name: Gene to GO Mapping
  original_source:
  - go
  - ncbigene
  product_file_size: 1223833668
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2go.gz
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
- category: Product
  description: GO annotations for all UniProtKB entries
  format: txt
  id: goa.uniprot
  name: UniProt GOA Annotations
  original_source:
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/'
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/'
  - 'File was not able to be retrieved when checked on 2025-11-04: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/'''
- category: Product
  description: GO annotations for human proteins
  format: txt
  id: goa.human
  name: Human GOA Annotations
  original_source:
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/'
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/'
  - 'File was not able to be retrieved when checked on 2025-11-04: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/'''
- category: Product
  description: GO annotations for mouse proteins
  format: txt
  id: goa.mouse
  name: Mouse GOA Annotations
  original_source:
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/'
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/'
  - 'File was not able to be retrieved when checked on 2025-11-04: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/'''
- category: MappingProduct
  description: Files containing transitive assignments of InterPro matches, UniProtKB
    keywords, subcellular locations, EC numbers, or HAMAP matches to manually-selected
    GO terms
  format: txt
  id: goa.mapping-files
  name: GO Mapping Files
  original_source:
  - interpro
  - uniprot
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'
  - 'File was not able to be retrieved when checked on 2025-11-04: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/'''
- category: MappingProduct
  description: bigg.compartment SSSOM
  format: sssom
  id: obo-db-ingest.bigg.compartment.sssom.tsv
  license:
    id: http://bigg.ucsd.edu/license#license
    label: Custom
  name: bigg.compartment SSSOM
  original_source:
  - bigg
  - go
  product_file_size: 242
  product_url: https://w3id.org/biopragmatics/resources/bigg.compartment/bigg.compartment.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: Gene ontology annotations from the Gene Ontology Consortium
  format: http
  id: genecards.gene.ontology
  name: GeneCards Gene Ontology Annotations
  original_source:
  - go
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-31_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-04: HTTP 403 error
    when accessing file'
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
- category: Product
  description: GO annotations for PDB entries
  format: txt
  id: goa.pdb
  name: PDB GOA Annotations
  original_source:
  - pdbe
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/'
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/'
  - 'File was not able to be retrieved when checked on 2025-11-04: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/'''
- category: MappingProduct
  description: Mappings between InterPro entries and Gene Ontology (GO) terms
  format: tsv
  id: interpro.interpro2go
  name: InterPro to GO Mappings
  original_source:
  - go
  - interpro
  product_file_size: 3088718
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro2go
  secondary_source:
  - interpro
- category: GraphicalInterface
  description: Browser for searching and viewing Gene Ontology terms and GOA annotations
  format: http
  id: goa.quickgo
  name: QuickGO Browser
  original_source:
  - go
  product_url: https://www.ebi.ac.uk/QuickGO/
- category: Product
  description: FTP site containing current and archived GOA annotation files for all
    species
  format: http
  id: goa.ftp
  name: GOA FTP Site
  original_source:
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/'
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/'
  - 'File was not able to be retrieved when checked on 2025-11-04: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/'''
- category: Product
  description: GO annotations organized by proteomes
  format: txt
  id: goa.proteomes
  name: Proteomes GOA Annotations
  original_source:
  - go
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/'
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/'
  - 'File was not able to be retrieved when checked on 2025-11-04: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/'''
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
repository: https://github.com/geneontology/go-ontology
taxon:
- NCBITaxon:1
---
## Description

An ontology for describing the function of genes and gene products

## Contacts

- Suzi Aleksander (suzia@stanford.edu) [ORCID: 0000-0001-6787-2901](https://orcid.org/0000-0001-6787-2901)

## Products

### GO (OWL edition)

The main ontology in OWL. This is self contained and does not have connections to other OBO ontologies

**URL**: [http://purl.obolibrary.org/obo/go.owl](http://purl.obolibrary.org/obo/go.owl)

**Format**: owl

### GO (OBO Format edition)

Equivalent to go.owl, in obo format

**URL**: [http://purl.obolibrary.org/obo/go.obo](http://purl.obolibrary.org/obo/go.obo)

**Format**: obo

### GO (JSON edition)

Equivalent to go.owl, in obograph json format

**URL**: [http://purl.obolibrary.org/obo/go.json](http://purl.obolibrary.org/obo/go.json)

**Format**: json

### GO-Plus

The main ontology plus axioms connecting to select external ontologies, with subsets of those ontologies

**URL**: [http://purl.obolibrary.org/obo/go/extensions/go-plus.owl](http://purl.obolibrary.org/obo/go/extensions/go-plus.owl)

**Format**: owl

### GO Base Module

The main ontology plus axioms connecting to select external ontologies, excluding the external ontologies themselves

**URL**: [http://purl.obolibrary.org/obo/go/go-base.owl](http://purl.obolibrary.org/obo/go/go-base.owl)

**Format**: owl

### GO-Plus

As go-plus.owl, in obographs json format

**URL**: [http://purl.obolibrary.org/obo/go/extensions/go-plus.json](http://purl.obolibrary.org/obo/go/extensions/go-plus.json)

**Format**: json

### GO-Basic, Filtered, for use with legacy tools

Basic version of the GO, filtered such that the graph is guaranteed to be acyclic and annotations can be propagated up the graph. The relations included are is a, part of, regulates, negatively regulates and positively regulates. This version excludes relationships that cross the 3 GO hierarchies.

**URL**: [http://purl.obolibrary.org/obo/go/go-basic.obo](http://purl.obolibrary.org/obo/go/go-basic.obo)

**Format**: obo

### GO-Basic, Filtered, for use with legacy tools (JSON)

As go-basic.obo, in json format

**URL**: [http://purl.obolibrary.org/obo/go/go-basic.json](http://purl.obolibrary.org/obo/go/go-basic.json)

**Format**: json

### GO Taxon Groupings

Classes added to ncbitaxon for groupings such as prokaryotes

**URL**: [http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl](http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl)

**Format**: owl

### GO (OWL edition), daily snapshot release

Equivalent to go.owl, but released daily. Note the snapshot release is not archived.

**URL**: [http://purl.obolibrary.org/obo/go/snapshot/go.owl](http://purl.obolibrary.org/obo/go/snapshot/go.owl)

**Format**: owl

### GO (OBO Format edition), daily snapshot release

Equivalent to go.owl, but released daily. Note the snapshot release is not archived.

**URL**: [http://purl.obolibrary.org/obo/go/snapshot/go.obo](http://purl.obolibrary.org/obo/go/snapshot/go.obo)

**Format**: obo

## Publications

- [Gene ontology: tool for the unification of biology. The Gene Ontology Consortium](https://www.ncbi.nlm.nih.gov/pubmed/10802651)
- [The Gene Ontology resource: enriching a GOld mine](https://www.ncbi.nlm.nih.gov/pubmed/33290552)

**Domains**: biological systems

**Taxon**: NCBITaxon:1

---

*This resource was automatically synchronized from the OBO Foundry registry.*