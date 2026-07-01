---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: cjmungall@lbl.gov
      - contact_type: github
        value: cmungall
    label: Christopher J. Mungall
    orcid: 0000-0002-6601-2165
  - category: Organization
    contact_details:
      - contact_type: other
        contact_type_name: Monarch Initiative Community
        contact_type_url: https://groups.google.com/g/monarch-friends/
        value: monarch-friends
    id: monarchinitiative
    label: Monarch Initiative
creation_date: '2025-03-09T00:00:00Z'
description: The Monarch Initiative is an international consortium that leads key global standards and semantic data integration technologies. To maximize utility and impact, the Monarch platform is composed of multiple open-source, open-access components.
domains:
  - biomedical
homepage_url: https://monarchinitiative.org/kg/downloads
id: kg-monarch
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: KG Monarch
products:
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
  - category: ProcessProduct
    description: This repository is a code reference for the C-Path Knowledge Graph project, to increase discoverability of rare disease datasets through integration with the Monarch Knowlege Graph. Note that this is only a reference to scripts and queries associated with this project and is not provided as a runnable project because these workflows depend on an internal data catalog.
    format: python
    id: cpathkg.code
    name: C-Path Knowledge Graph Integration
    original_source:
      - relation_type: prov:hadPrimarySource
        source: biolink
      - relation_type: prov:hadPrimarySource
        source: cpathkg
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_url: https://gitlab.c-path.org/c-pathontology/c-path-knowledge-graph-integration
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
  - category: Product
    description: All associations from the Monarch Knowledge Graph in TSV format
    format: tsv
    id: kg-monarch.associations.all
    name: All Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 50883784
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/association.all.tsv.gz
  - category: Product
    description: Causal gene to disease associations
    format: tsv
    id: kg-monarch.associations.causal_gene_to_disease
    name: Causal Gene to Disease Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 173184
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/causal_gene_to_disease_association.all.tsv.gz
  - category: Product
    description: Chemical or drug or treatment to disease or phenotypic feature associations
    format: tsv
    id: kg-monarch.associations.chemical_or_drug_to_disease
    name: Chemical/Drug/Treatment to Disease/Phenotypic Feature Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 19562
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association.all.tsv.gz
  - category: Product
    description: Chemical to disease or phenotypic feature associations
    format: tsv
    id: kg-monarch.associations.chemical_to_disease
    name: Chemical to Disease/Phenotypic Feature Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 630460
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/chemical_entity_to_disease_or_phenotypic_feature_association.all.tsv.gz
  - category: Product
    description: Chemical to pathway associations
    format: tsv
    id: kg-monarch.associations.chemical_to_pathway
    name: Chemical to Pathway Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 2595240
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/chemical_entity_to_pathway_association.all.tsv.gz
  - category: Product
    description: Correlated gene to disease associations
    format: tsv
    id: kg-monarch.associations.correlated_gene_to_disease
    name: Correlated Gene to Disease Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 232463
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/correlated_gene_to_disease_association.all.tsv.gz
  - category: Product
    description: Disease or phenotypic feature to genetic inheritance associations
    format: tsv
    id: kg-monarch.associations.disease_to_inheritance
    name: Disease/Phenotypic Feature to Genetic Inheritance Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 240991
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/disease_or_phenotypic_feature_to_genetic_inheritance_association.all.tsv.gz
  - category: Product
    description: Disease or phenotypic feature to location associations
    format: tsv
    id: kg-monarch.associations.disease_to_location
    name: Disease/Phenotypic Feature to Location Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 22009
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/disease_or_phenotypic_feature_to_location_association.all.tsv.gz
  - category: Product
    description: Disease to phenotypic feature associations
    format: tsv
    id: kg-monarch.associations.disease_to_phenotype
    name: Disease to Phenotypic Feature Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 8305765
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/disease_to_phenotypic_feature_association.all.tsv.gz
  - category: Product
    description: Gene to expression site associations
    format: tsv
    id: kg-monarch.associations.gene_to_expression_site
    name: Gene to Expression Site Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 49551885
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/gene_to_expression_site_association.all.tsv.gz
  - category: Product
    description: Gene to gene homology associations
    format: tsv
    id: kg-monarch.associations.gene_to_gene_homology
    name: Gene to Gene Homology Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 39739502
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/gene_to_gene_homology_association.all.tsv.gz
  - category: Product
    description: Gene to pathway associations
    format: tsv
    id: kg-monarch.associations.gene_to_pathway
    name: Gene to Pathway Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 6256794
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/gene_to_pathway_association.all.tsv.gz
  - category: Product
    description: Gene to phenotypic feature associations
    format: tsv
    id: kg-monarch.associations.gene_to_phenotype
    name: Gene to Phenotypic Feature Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 21465491
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/gene_to_phenotypic_feature_association.all.tsv.gz
  - category: Product
    description: Genotype to disease associations
    format: tsv
    id: kg-monarch.associations.genotype_to_disease
    name: Genotype to Disease Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 486257
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/genotype_to_disease_association.all.tsv.gz
  - category: Product
    description: Genotype to gene associations
    format: tsv
    id: kg-monarch.associations.genotype_to_gene
    name: Genotype to Gene Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 4186637
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/genotype_to_gene_association.all.tsv.gz
  - category: Product
    description: Genotype to phenotypic feature associations
    format: tsv
    id: kg-monarch.associations.genotype_to_phenotype
    name: Genotype to Phenotypic Feature Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 22271794
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/genotype_to_phenotypic_feature_association.all.tsv.gz
  - category: Product
    description: Genotype to variant associations
    format: tsv
    id: kg-monarch.associations.genotype_to_variant
    name: Genotype to Variant Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 5898563
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/genotype_to_variant_association.all.tsv.gz
  - category: Product
    description: Macromolecular machine to biological process associations
    format: tsv
    id: kg-monarch.associations.macromolecular_machine_to_biological_process
    name: Macromolecular Machine to Biological Process Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 33957550
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/macromolecular_machine_to_biological_process_association.all.tsv.gz
  - category: Product
    description: Macromolecular machine to cellular component associations
    format: tsv
    id: kg-monarch.associations.macromolecular_machine_to_cellular_component
    name: Macromolecular Machine to Cellular Component Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 19600342
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/macromolecular_machine_to_cellular_component_association.all.tsv.gz
  - category: Product
    description: Macromolecular machine to molecular activity associations
    format: tsv
    id: kg-monarch.associations.macromolecular_machine_to_molecular_activity
    name: Macromolecular Machine to Molecular Activity Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 24519759
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/macromolecular_machine_to_molecular_activity_association.all.tsv.gz
  - category: Product
    description: Pairwise gene to gene interaction associations
    format: tsv
    id: kg-monarch.associations.pairwise_gene_to_gene_interaction
    name: Pairwise Gene to Gene Interaction Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 53935441
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/pairwise_gene_to_gene_interaction.all.tsv.gz
  - category: Product
    description: Variant to disease associations
    format: tsv
    id: kg-monarch.associations.variant_to_disease
    name: Variant to Disease Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 439945
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/variant_to_disease_association.all.tsv.gz
  - category: Product
    description: Variant to gene associations
    format: tsv
    id: kg-monarch.associations.variant_to_gene
    name: Variant to Gene Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 4273160
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/variant_to_gene_association.all.tsv.gz
  - category: Product
    description: Variant to phenotypic feature associations
    format: tsv
    id: kg-monarch.associations.variant_to_phenotype
    name: Variant to Phenotypic Feature Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 9841001
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/variant_to_phenotypic_feature_association.all.tsv.gz
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
  - category: Product
    compression: targz
    description: Solr index data for the Monarch Knowledge Graph search functionality
    id: kg-monarch.solr
    name: Solr Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
    product_file_size: 34691273954
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/solr.tar.gz
  - category: GraphProduct
    description: Integrated graph knowledge base combining Mendelian randomization causal estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships (Neo4j backend)
    format: neo4j
    id: epigraphdb.graph
    name: EpiGraphDB Graph Database
    original_source:
      - relation_type: prov:hadPrimarySource
        source: epigraphdb
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
      - relation_type: prov:hadPrimarySource
        source: vectology
      - relation_type: prov:hadPrimarySource
        source: ukbiobank
      - relation_type: prov:hadPrimarySource
        source: prsatlas
      - relation_type: prov:hadPrimarySource
        source: eqtlgen
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: cpic
      - relation_type: prov:hadPrimarySource
        source: opentargets
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: semmeddb
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: mrbase
    product_url: https://docs.epigraphdb.org/graph-database/
  - category: GraphicalInterface
    description: Web-based interface for searching and browsing comprehensive gene-centric information integrating data from over 200 sources
    format: http
    id: genecards.web.interface
    name: GeneCards Web Interface
    original_source:
      - relation_type: prov:hadPrimarySource
        source: 5srrnadb
      - relation_type: prov:hadPrimarySource
        source: alliance
      - relation_type: prov:hadPrimarySource
        source: alphafold
      - relation_type: prov:hadPrimarySource
        source: aminode
      - relation_type: prov:hadPrimarySource
        source: bgee
      - relation_type: prov:hadPrimarySource
        source: biocyc
      - relation_type: prov:hadPrimarySource
        source: biogps
      - relation_type: prov:hadPrimarySource
        source: biogrid
      - relation_type: prov:hadPrimarySource
        source: bitterdb
      - relation_type: prov:hadPrimarySource
        source: cdd
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: civic
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: compartments
      - relation_type: prov:hadPrimarySource
        source: cosmic
      - relation_type: prov:hadPrimarySource
        source: craft
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: dbsnp
      - relation_type: prov:hadPrimarySource
        source: dbsuper
      - relation_type: prov:hadPrimarySource
        source: dgidb
      - relation_type: prov:hadPrimarySource
        source: dgv
      - relation_type: prov:hadPrimarySource
        source: diseases
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: ena
      - relation_type: prov:hadPrimarySource
        source: encode
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: epd
      - relation_type: prov:hadPrimarySource
        source: fabric
      - relation_type: prov:hadPrimarySource
        source: fantom5
      - relation_type: prov:hadPrimarySource
        source: flybase
      - relation_type: prov:hadPrimarySource
        source: gard
      - relation_type: prov:hadPrimarySource
        source: gencode
      - relation_type: prov:hadPrimarySource
        source: genecards
      - relation_type: prov:hadPrimarySource
        source: geneorganizer
      - relation_type: prov:hadPrimarySource
        source: genomernai
      - relation_type: prov:hadPrimarySource
        source: glyconnect
      - relation_type: prov:hadPrimarySource
        source: glygen
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: gtopdb
      - relation_type: prov:hadPrimarySource
        source: gtrnadb
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: homologene
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: hprd
      - relation_type: prov:hadPrimarySource
        source: humancyc
      - relation_type: prov:hadPrimarySource
        source: icd10
      - relation_type: prov:hadPrimarySource
        source: icd11
      - relation_type: prov:hadPrimarySource
        source: iid
      - relation_type: prov:hadPrimarySource
        source: imgt
      - relation_type: prov:hadPrimarySource
        source: innatedb
      - relation_type: prov:hadPrimarySource
        source: intact
      - relation_type: prov:hadPrimarySource
        source: interpro
      - relation_type: prov:hadPrimarySource
        source: kg-monarch
      - relation_type: prov:hadPrimarySource
        source: lncbase
      - relation_type: prov:hadPrimarySource
        source: lncbook
      - relation_type: prov:hadPrimarySource
        source: lncipedia
      - relation_type: prov:hadPrimarySource
        source: lncrnadisease
      - relation_type: prov:hadPrimarySource
        source: malacards
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: medlineplus
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: mgi
      - relation_type: prov:hadPrimarySource
        source: mint
      - relation_type: prov:hadPrimarySource
        source: mirbase
      - relation_type: prov:hadPrimarySource
        source: mirgenedb
      - relation_type: prov:hadPrimarySource
        source: mirtarbase
      - relation_type: prov:hadPrimarySource
        source: modomics
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: ncit
      - relation_type: prov:hadPrimarySource
        source: nextprot
      - relation_type: prov:hadPrimarySource
        source: noncode
      - relation_type: prov:hadPrimarySource
        source: omim
      - relation_type: prov:hadPrimarySource
        source: opentargets
      - relation_type: prov:hadPrimarySource
        source: orphanet
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: pathwaycommons
      - relation_type: prov:hadPrimarySource
        source: paxdb
      - relation_type: prov:hadPrimarySource
        source: pdb
      - relation_type: prov:hadPrimarySource
        source: pdbe
      - relation_type: prov:hadPrimarySource
        source: pfam
      - relation_type: prov:hadPrimarySource
        source: pharmgkb
      - relation_type: prov:hadPrimarySource
        source: pid
      - relation_type: prov:hadPrimarySource
        source: pirsf
      - relation_type: prov:hadPrimarySource
        source: prosite
      - relation_type: prov:hadPrimarySource
        source: proteomicsdb
      - relation_type: prov:hadPrimarySource
        source: proteopedia
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: pubtator
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: refseq
      - relation_type: prov:hadPrimarySource
        source: rfam
      - relation_type: prov:hadPrimarySource
        source: rgd
      - relation_type: prov:hadPrimarySource
        source: rnacentral
      - relation_type: prov:hadPrimarySource
        source: scop
      - relation_type: prov:hadPrimarySource
        source: sfld
      - relation_type: prov:hadPrimarySource
        source: sgd
      - relation_type: prov:hadPrimarySource
        source: signor
      - relation_type: prov:hadPrimarySource
        source: silva
      - relation_type: prov:hadPrimarySource
        source: simap
      - relation_type: prov:hadPrimarySource
        source: smart
      - relation_type: prov:hadPrimarySource
        source: snodb
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: snopy
      - relation_type: prov:hadPrimarySource
        source: srpdb
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: tair
      - relation_type: prov:hadPrimarySource
        source: tarbase
      - relation_type: prov:hadPrimarySource
        source: tissues
      - relation_type: prov:hadPrimarySource
        source: treefam
      - relation_type: prov:hadPrimarySource
        source: ttd
      - relation_type: prov:hadPrimarySource
        source: ucnebase
      - relation_type: prov:hadPrimarySource
        source: ucsc
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: vista
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: wikipedia
      - relation_type: prov:hadPrimarySource
        source: wormbase
    product_url: https://www.genecards.org/
repository: https://github.com/monarch-initiative/monarch-ingest
---

The Monarch Initiative is an international consortium that leads key global standards and semantic data integration technologies. Monarch resources and integrated data are also foundational to many downstream applications and contexts; we work closely with a variety of stakeholders and resource-development communities to capture feedback and make improvements. To maximize utility and impact, the Monarch platform is composed of multiple open-source, open-access components. We promote provenance and transparency, enhanced use of standards and new technologies and improved data accessibility, end-user utility, and data submission. Learn more about the complete suite of Monarch resources on our organization's [documentation pages](https://monarch-initiative.github.io/monarch-documentation/).

## Evaluation

- View the evaluation: [kg-monarch evaluation](kg-monarch_eval.html)
