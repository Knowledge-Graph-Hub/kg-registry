---
activity_status: active
category: Resource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jhc@lbl.gov
  - contact_type: github
    value: caufieldjh
  label: J. Harry Caufield
creation_date: '2025-03-09T00:00:00Z'
description: An ontology for accessing and comparing knowledge concerning phenotypes
  across species and genetic backgrounds.
domains:
- phenotype
homepage_url: https://monarch-initiative.github.io/phenio/
id: phenio
infores_id: phenio
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/license/bsd-3-clause
  label: BSD3
name: An integrated ontology for Phenomics
products:
- category: Product
  compression: gzip
  description: OWL version of phenio
  format: owl
  id: phenio.model
  license:
    id: https://opensource.org/license/bsd-3-clause
    label: BSD3
  name: phenio
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phenio
  product_file_size: 124412326
  product_url: https://github.com/monarch-initiative/phenio/releases/latest/download/phenio.owl.gz
  repository: https://github.com/monarch-initiative/phenio
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.2.5
  compression: targz
  description: PHENIO as a KGX graph
  format: kgx
  id: phenio.graph
  license:
    id: https://opensource.org/license/bsd-3-clause
    label: BSD3
  name: KG-Phenio
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phenio
  product_file_size: 71579307
  product_url: https://github.com/Knowledge-Graph-Hub/kg-phenio/releases/latest/download/kg-phenio.tar.gz
  repository: https://github.com/Knowledge-Graph-Hub/kg-phenio
- category: GraphProduct
  description: KGX Distribution of KG-Monarch
  edge_count: 15211571
  format: kgx
  id: kg-monarch.graph
  name: KGX Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 230877741
  product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch
  edge_count: 15211571
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl
  name: KGX JSON-L Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 315667976
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
- category: GraphProduct
  description: RDF Distribution of KG-Monarch
  edge_count: 15211571
  format: rdfxml
  id: kg-monarch.graph.rdf
  name: RDF Distribution of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 879238775
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch
  dump_format: neo4j
  edge_count: 15211571
  format: neo4j
  id: kg-monarch.graph.neo4j
  name: Neo4j Dump of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 1438250397
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
  warnings: []
- category: GraphProduct
  description: DuckDB database of KG-Monarch
  edge_count: 15211571
  format: mixed
  id: kg-monarch.graph.duckdb
  name: DuckDB database of KG-Monarch
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 6827814912
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb
- category: GraphProduct
  compression: targz
  description: KGX JSON-Lines Distribution of KG-Monarch (Edges)
  edge_count: 15211571
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl.edges
  name: KGX JSON-L Distribution of KG-Monarch Edges
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 487854288
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
- category: GraphProduct
  compression: targz
  description: KGX JSON-Lines Distribution of KG-Monarch (Nodes)
  edge_count: 15211571
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl.nodes
  name: KGX JSON-L Distribution of KG-Monarch Nodes
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 487854288
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch Edges
  edge_count: 15211571
  format: neo4j
  id: kg-monarch.graph.neo4j.edges
  name: Neo4j Dump of KG-Monarch Edges
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 4386388748
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.neo4j.csv
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch Nodes
  edge_count: 15211571
  format: neo4j
  id: kg-monarch.graph.neo4j.nodes
  name: Neo4j Dump of KG-Monarch Nodes
  node_categories:
  - biolink:AnatomicalEntity
  - biolink:BiologicalProcess
  - biolink:Case
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
  node_count: 1462594
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  predicates:
  - biolink:actively_involved_in
  - biolink:acts_upstream_of
  - biolink:acts_upstream_of_negative_effect
  - biolink:acts_upstream_of_or_within
  - biolink:acts_upstream_of_or_within_negative_effect
  - biolink:acts_upstream_of_or_within_positive_effect
  - biolink:acts_upstream_of_positive_effect
  - biolink:affects
  - biolink:applied_to_treat
  - biolink:associated_with_increased_likelihood_of
  - biolink:capable_of
  - biolink:caused_by
  - biolink:causes
  - biolink:coexists_with
  - biolink:colocalizes_with
  - biolink:contributes_to
  - biolink:correlated_with
  - biolink:derives_from
  - biolink:develops_from
  - biolink:directly_physically_interacts_with
  - biolink:disease_has_location
  - biolink:disrupts
  - biolink:enables
  - biolink:expressed_in
  - biolink:expresses
  - biolink:gene_associated_with_condition
  - biolink:genetically_associated_with
  - biolink:has_adverse_event
  - biolink:has_disease
  - biolink:has_gene
  - biolink:has_input
  - biolink:has_mode_of_inheritance
  - biolink:has_output
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:has_sequence_variant
  - biolink:homologous_to
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_active_in
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  - biolink:treats
  - biolink:treats_or_applied_or_studied_to_treat
  product_file_size: 349573789
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.neo4j.csv
- category: Product
  description: Phenio SQLite database in SemSQL format for ontology queries
  format: sqlite
  id: kg-monarch.phenio.semsql
  name: Phenio SQLite (SemSQL)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: phenio
  product_file_size: 3425435914
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/phenio.db.gz
- category: GraphProduct
  compression: targz
  description: KGX Distribution of KG-Alzheimers
  format: kgx
  id: kg-alzheimers.graph
  name: KGX Distribution of KG-Alzheimers
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-alzheimers
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: mesh
  product_file_size: 210868256
  product_url: https://kg-hub.berkeleybop.io/kg-alzheimers/current/kg-alzheimers.tar.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-07-01; no live download
    location was found (GitHub releases, kghub.io/current, and Zenodo all return 404
    or have no published artifact).
- category: GraphProduct
  description: KGX distribution of the SRI-Reference KG
  format: kgx
  id: sri-reference-kg.graph
  name: SRI-Reference KG (KGX distribution)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sri-reference-kg
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: wormbase
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ddanat
  - relation_type: prov:hadPrimarySource
    source: ddpheno
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dpo
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: fypo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: wbbt
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: wbphenotype
  - relation_type: prov:hadPrimarySource
    source: xao
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: zfa
  - relation_type: prov:hadPrimarySource
    source: zfs
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: decipher
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  - relation_type: prov:hadPrimarySource
    source: cureid
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_file_size: 230046094
  product_url: https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.tar.gz
repository: https://github.com/monarch-initiative/phenio
usages:
- description: PHENIO is used by the Monarch Initiative for cross-species inference.
    As an example, the disease of Parkinsonism may compared on the basis of its phenotype
    in humans vs. mouse genes and genotypes known to impact these phenotypes.
  id: cross-species-inference
  label: PHENIO is used by the Monarch Initiative for cross-species inference
  publications:
  - doi: doi:10.1093/nar/gkw1128
    id: doi:10.1093/nar/gkw1128
    preferred: true
    title: 'The Monarch Initiative: an integrative data and analytic platform connecting
      phenotypes to genotypes across species'
  type: actual
  url: https://monarchinitiative.org/HP:0001300#disease
  users:
  - category: Organization
    contact_details:
    - contact_type: url
      value: https://monarchinitiative.org/
    label: The Monarch Initiative
---
PHENIO