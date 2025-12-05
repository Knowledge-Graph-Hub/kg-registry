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
  label: Monarch Initiative
description: The Monarch Initiative is an international consortium that leads key
  global standards and semantic data integration technologies. To maximize utility
  and impact, the Monarch platform is composed of multiple open-source, open-access
  components.
domains:
- health
homepage_url: https://kghub.org/kg-monarch/index.html
id: kg-monarch
last_modified_date: '2025-12-04T18:09:43Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: KG Monarch
products:
- category: GraphProduct
  description: KGX Distribution of KG-Monarch
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
  description: KGX JSON-Lines Distribution of KG-Monarch (Edges)
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
  description: RDF Distribution of KG-Monarch
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
  description: Neo4j Dump of KG-Monarch Edges
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
  description: DuckDB database of KG-Monarch
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
- category: ProcessProduct
  description: This repository is a code reference for the C-Path Knowledge Graph
    project, to increase discoverability of rare disease datasets through integration
    with the Monarch Knowlege Graph. Note that this is only a reference to scripts
    and queries associated with this project and is not provided as a runnable project
    because these workflows depend on an internal data catalog.
  format: python
  id: cpathkg.code
  name: C-Path Knowledge Graph Integration
  original_source:
  - biolink
  - kg-monarch
  product_url: https://gitlab.c-path.org/c-pathontology/c-path-knowledge-graph-integration
  secondary_source:
  - cpathkg
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
  description: Neo4j Dump of KG-Monarch
  dump_format: neo4j
  edge_count: 15107405
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
  node_count: 1360948
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
  - biolink:homologous_to
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
- category: DataProduct
  description: All associations from the Monarch Knowledge Graph in TSV format
  format: tsv
  id: kg-monarch.associations.all
  name: All Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/association.all.tsv.gz
- category: DataProduct
  description: Causal gene to disease associations
  format: tsv
  id: kg-monarch.associations.causal_gene_to_disease
  name: Causal Gene to Disease Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/causal_gene_to_disease_association.all.tsv.gz
- category: DataProduct
  description: Chemical or drug or treatment to disease or phenotypic feature associations
  format: tsv
  id: kg-monarch.associations.chemical_or_drug_to_disease
  name: Chemical/Drug/Treatment to Disease/Phenotypic Feature Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/chemical_or_drug_or_treatment_to_disease_or_phenotypic_feature_association.all.tsv.gz
- category: DataProduct
  description: Chemical to disease or phenotypic feature associations
  format: tsv
  id: kg-monarch.associations.chemical_to_disease
  name: Chemical to Disease/Phenotypic Feature Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/chemical_to_disease_or_phenotypic_feature_association.all.tsv.gz
- category: DataProduct
  description: Chemical to pathway associations
  format: tsv
  id: kg-monarch.associations.chemical_to_pathway
  name: Chemical to Pathway Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/chemical_to_pathway_association.all.tsv.gz
- category: DataProduct
  description: Correlated gene to disease associations
  format: tsv
  id: kg-monarch.associations.correlated_gene_to_disease
  name: Correlated Gene to Disease Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/correlated_gene_to_disease_association.all.tsv.gz
- category: DataProduct
  description: Disease or phenotypic feature to genetic inheritance associations
  format: tsv
  id: kg-monarch.associations.disease_to_inheritance
  name: Disease/Phenotypic Feature to Genetic Inheritance Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/disease_or_phenotypic_feature_to_genetic_inheritance_association.all.tsv.gz
- category: DataProduct
  description: Disease or phenotypic feature to location associations
  format: tsv
  id: kg-monarch.associations.disease_to_location
  name: Disease/Phenotypic Feature to Location Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/disease_or_phenotypic_feature_to_location_association.all.tsv.gz
- category: DataProduct
  description: Disease to phenotypic feature associations
  format: tsv
  id: kg-monarch.associations.disease_to_phenotype
  name: Disease to Phenotypic Feature Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/disease_to_phenotypic_feature_association.all.tsv.gz
- category: DataProduct
  description: Gene to expression site associations
  format: tsv
  id: kg-monarch.associations.gene_to_expression_site
  name: Gene to Expression Site Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/gene_to_expression_site_association.all.tsv.gz
- category: DataProduct
  description: Gene to gene homology associations
  format: tsv
  id: kg-monarch.associations.gene_to_gene_homology
  name: Gene to Gene Homology Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/gene_to_gene_homology_association.all.tsv.gz
- category: DataProduct
  description: Gene to pathway associations
  format: tsv
  id: kg-monarch.associations.gene_to_pathway
  name: Gene to Pathway Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/gene_to_pathway_association.all.tsv.gz
- category: DataProduct
  description: Gene to phenotypic feature associations
  format: tsv
  id: kg-monarch.associations.gene_to_phenotype
  name: Gene to Phenotypic Feature Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/gene_to_phenotypic_feature_association.all.tsv.gz
- category: DataProduct
  description: Genotype to disease associations
  format: tsv
  id: kg-monarch.associations.genotype_to_disease
  name: Genotype to Disease Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/genotype_to_disease_association.all.tsv.gz
- category: DataProduct
  description: Genotype to gene associations
  format: tsv
  id: kg-monarch.associations.genotype_to_gene
  name: Genotype to Gene Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/genotype_to_gene_association.all.tsv.gz
- category: DataProduct
  description: Genotype to phenotypic feature associations
  format: tsv
  id: kg-monarch.associations.genotype_to_phenotype
  name: Genotype to Phenotypic Feature Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/genotype_to_phenotypic_feature_association.all.tsv.gz
- category: DataProduct
  description: Genotype to variant associations
  format: tsv
  id: kg-monarch.associations.genotype_to_variant
  name: Genotype to Variant Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/genotype_to_variant_association.all.tsv.gz
- category: DataProduct
  description: Macromolecular machine to biological process associations
  format: tsv
  id: kg-monarch.associations.macromolecular_machine_to_biological_process
  name: Macromolecular Machine to Biological Process Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/macromolecular_machine_to_biological_process_association.all.tsv.gz
- category: DataProduct
  description: Macromolecular machine to cellular component associations
  format: tsv
  id: kg-monarch.associations.macromolecular_machine_to_cellular_component
  name: Macromolecular Machine to Cellular Component Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/macromolecular_machine_to_cellular_component_association.all.tsv.gz
- category: DataProduct
  description: Macromolecular machine to molecular activity associations
  format: tsv
  id: kg-monarch.associations.macromolecular_machine_to_molecular_activity
  name: Macromolecular Machine to Molecular Activity Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/macromolecular_machine_to_molecular_activity_association.all.tsv.gz
- category: DataProduct
  description: Pairwise gene to gene interaction associations
  format: tsv
  id: kg-monarch.associations.pairwise_gene_to_gene_interaction
  name: Pairwise Gene to Gene Interaction Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/pairwise_gene_to_gene_interaction.all.tsv.gz
- category: DataProduct
  description: Variant to disease associations
  format: tsv
  id: kg-monarch.associations.variant_to_disease
  name: Variant to Disease Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/variant_to_disease_association.all.tsv.gz
- category: DataProduct
  description: Variant to gene associations
  format: tsv
  id: kg-monarch.associations.variant_to_gene
  name: Variant to Gene Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/variant_to_gene_association.all.tsv.gz
- category: DataProduct
  description: Variant to phenotypic feature associations
  format: tsv
  id: kg-monarch.associations.variant_to_phenotype
  name: Variant to Phenotypic Feature Associations
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/tsv/all_associations/variant_to_phenotypic_feature_association.all.tsv.gz
- category: DataProduct
  description: Phenio SQLite database in SemSQL format for ontology queries
  format: sqlite
  id: kg-monarch.phenio.semsql
  name: Phenio SQLite (SemSQL)
  original_source:
  - phenio
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/phenio.db.gz
- category: DataProduct
  description: Solr index data for the Monarch Knowledge Graph search functionality
  format: tar.gz
  id: kg-monarch.solr
  name: Solr Data
  original_source:
  - kg-monarch
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/solr.tar.gz
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - epigraphdb
  - kg-monarch
  - vectology
  - ukbiobank
  - prsatlas
  - eqtlgen
  - mondo
  - gtex
  - ensembl
  - cpic
  - opentargets
  - efo
  - semmeddb
  - intact
  - string
  - reactome
  - mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
  secondary_source:
  - epigraphdb
repository: https://github.com/monarch-initiative/monarch-ingest
---
The Monarch Initiative is an international consortium that leads key global standards and semantic data integration technologies. Monarch resources and integrated data are also foundational to many downstream applications and contexts; we work closely with a variety of stakeholders and resource-development communities to capture feedback and make improvements. To maximize utility and impact, the Monarch platform is composed of multiple open-source, open-access components. We promote provenance and transparency, enhanced use of standards and new technologies and improved data accessibility, end-user utility, and data submission. Learn more about the complete suite of Monarch resources on our organization's [documentation pages](https://monarch-initiative.github.io/monarch-documentation/).

## Evaluation

- View the evaluation: [kg-monarch evaluation](kg-monarch_eval.html)