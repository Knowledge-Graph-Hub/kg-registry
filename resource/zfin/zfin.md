---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: zfinadmn@zfin.org
  label: Zebrafish Information Network
description: Zebrafish Information Network, including the Zebrafish Anatomical Ontology
domains:
- biological systems
homepage_url: https://zfin.org/
id: zfin
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: ZFIN
products:
- category: Product
  description: Zebrafish Anatomical Ontology (OWL)
  id: zfin.zfa
  license:
    id: https://creativecommons.org/licenses/by/3.0/
    label: CC-BY-3.0
  name: ZFA
  original_source:
  - zfin
  product_file_size: 401588
  product_url: http://purl.obolibrary.org/obo/zfa.owl
  secondary_source:
  - zfin
- category: Product
  description: zfin OBO
  format: obo
  id: obo-db-ingest.zfin.obo
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OBO
  original_source:
  - zfin
  product_file_size: 2643947
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.obo
  secondary_source:
  - obo-db-ingest
- category: Product
  description: zfin OWL
  format: owl
  id: obo-db-ingest.zfin.owl
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OWL
  original_source:
  - zfin
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.owl
  secondary_source:
  - obo-db-ingest
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-01: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-31: HTTP 404 error
    when accessing file'
- category: Product
  description: zfin OBO Graph JSON
  format: json
  id: obo-db-ingest.zfin.json
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin OBO Graph JSON
  original_source:
  - zfin
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.json
  secondary_source:
  - obo-db-ingest
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-01: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-31: HTTP 404 error
    when accessing file'
- category: MappingProduct
  description: zfin SSSOM
  id: obo-db-ingest.zfin.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: zfin SSSOM
  original_source:
  - zfin
  product_file_size: 374627
  product_url: https://w3id.org/biopragmatics/resources/zfin/zfin.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: Product
  description: Phenotype of Zebrafish Genes
  format: tsv
  id: zfin.gene-to-phenotype
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: ZFIN clean gene to phenotype
  original_source:
  - zfin
  product_file_size: 42545110
  product_url: https://zfin.org/downloads/phenoGeneCleanData_fish.txt
  secondary_source:
  - zfin
- category: Product
  description: Phenotype of Zebrafish Genes
  format: tsv
  id: zfin.gene-to-publication
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: ZFIN gene to publication
  original_source:
  - zfin
  product_file_size: 39531152
  product_url: https://zfin.org/downloads/gene_publication.txt
  secondary_source:
  - zfin
- category: GraphProduct
  description: KGX Distribution of KG-Monarch
  edge_count: 14486132
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
  node_count: 1344798
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
  edge_count: 14486132
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
  node_count: 1344798
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
  edge_count: 14486132
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
  node_count: 1344798
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
  edge_count: 14486132
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
  node_count: 1344798
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
  edge_count: 14486132
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
  node_count: 1344798
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
  description: KGX JSON-Lines Distribution of KG-Monarch (Edges)
  edge_count: 14486132
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
  node_count: 1344798
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
  edge_count: 14486132
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
  node_count: 1344798
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
  edge_count: 14486132
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
  node_count: 1344798
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
  edge_count: 14486132
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
  node_count: 1344798
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
repository: https://github.com/ZFIN/
---
ZFIN