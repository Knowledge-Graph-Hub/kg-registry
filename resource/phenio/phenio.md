---
activity_status: active
category: Ontology
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jhc@lbl.gov
  - contact_type: github
    value: caufieldjh
  label: J. Harry Caufield
creation_date: '2025-03-09T00:00:00Z'
description: PHENIO (Phenomics Integrated Ontology) is an application ontology for
  accessing and comparing knowledge concerning phenotypes across species and genetic
  backgrounds. Built with the Ontology Development Kit, it merges species-specific
  and cross-species phenotype ontologies (uPheno, HP, MP, ZP, XPO, FYPO, WBPhenotype,
  DDPHENO, DPO, OBA), anatomy and developmental stage ontologies (Uberon, CL, FBbt,
  ZFA, XAO, WBbt, EMAPA, DDANAT, and others), Mondo, GO, PATO, and supporting ontologies
  into a single resource that provides the ontological backbone of the Monarch Knowledge
  Graph.
domains:
- phenotype
homepage_url: https://monarch-initiative.github.io/phenio/
id: phenio
infores_id: phenio
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/license/bsd-3-clause
  label: BSD3
name: Phenomics Integrated Ontology (PHENIO)
products:
- category: OntologyProduct
  compression: gzip
  description: OWL version of PHENIO (full release), merging phenotype, anatomy,
    disease, chemical, gene, and upper-level ontologies imported via the ODK pipeline
  format: owl
  id: phenio.model
  license:
    id: https://opensource.org/license/bsd-3-clause
    label: BSD3
  name: phenio
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: fypo
  - relation_type: prov:hadPrimarySource
    source: wbphenotype
  - relation_type: prov:hadPrimarySource
    source: ddpheno
  - relation_type: prov:hadPrimarySource
    source: dpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: zfa
  - relation_type: prov:hadPrimarySource
    source: xao
  - relation_type: prov:hadPrimarySource
    source: wbbt
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: ddanat
  - relation_type: prov:hadPrimarySource
    source: zfs
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: chr
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
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
  - relation_type: prov:hadPrimarySource
    source: upheno
  product_file_size: 71579307
  product_url: https://github.com/Knowledge-Graph-Hub/kg-phenio/releases/latest/download/kg-phenio.tar.gz
  repository: https://github.com/Knowledge-Graph-Hub/kg-phenio
- category: OntologyProduct
  description: OBO Graphs JSON version of PHENIO (full release)
  format: json
  id: phenio.json
  license:
    id: https://opensource.org/license/bsd-3-clause
    label: BSD3
  name: phenio JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: fypo
  - relation_type: prov:hadPrimarySource
    source: wbphenotype
  - relation_type: prov:hadPrimarySource
    source: ddpheno
  - relation_type: prov:hadPrimarySource
    source: dpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: zfa
  - relation_type: prov:hadPrimarySource
    source: xao
  - relation_type: prov:hadPrimarySource
    source: wbbt
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: ddanat
  - relation_type: prov:hadPrimarySource
    source: zfs
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: chr
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  product_file_size: 1261625948
  product_url: https://github.com/monarch-initiative/phenio/releases/latest/download/phenio.json
  repository: https://github.com/monarch-initiative/phenio
- category: GraphProduct
  description: KGX Distribution of KG-Monarch
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  product_file_size: 230877741
  product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  product_file_size: 315667976
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
- category: GraphProduct
  description: RDF Distribution of KG-Monarch
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  product_file_size: 879238775
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch
  dump_format: neo4j
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  product_file_size: 1438250397
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
  warnings: []
- category: GraphProduct
  description: DuckDB database of KG-Monarch
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  product_file_size: 6827814912
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb
- category: GraphProduct
  compression: targz
  description: KGX JSON-Lines Distribution of KG-Monarch (Edges)
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  product_file_size: 487854288
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
- category: GraphProduct
  compression: targz
  description: KGX JSON-Lines Distribution of KG-Monarch (Nodes)
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  product_file_size: 487854288
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch Edges
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
  product_file_size: 4386388748
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.neo4j.csv
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch Nodes
  edge_count: 16433147
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
  - biolink:ClinicalMeasurement
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
  node_count: 1670861
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
  - biolink:active_in
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
  - biolink:is_input_of
  - biolink:is_output_of
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:location_of
  - biolink:model_of
  - biolink:negatively_correlated_with
  - biolink:occurs_in
  - biolink:orthologous_to
  - biolink:overlaps
  - biolink:part_of
  - biolink:participates_in
  - biolink:positively_correlated_with
  - biolink:preceded_by
  - biolink:precedes
  - biolink:produced_by
  - biolink:produces
  - biolink:regulates
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:temporally_related_to
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
publications:
- authors:
  - "Tim E Putman"
  - "Kevin Schaper"
  - "Nicolas Matentzoglu"
  - "Vincent P Rubinetti"
  - "Faisal S Alquaddoomi"
  - "Corey Cox"
  - "J Harry Caufield"
  - "Glass Elsarboukh"
  - "Sarah Gehrke"
  - "Harshad Hegde"
  - "Justin T Reese"
  - "Ian Braun"
  - "Richard M Bruskiewich"
  - "Luca Cappelletti"
  - "Seth Carbon"
  - "Anita R Caron"
  - "Lauren E Chan"
  - "Christopher G Chute"
  - "Katherina G Cortes"
  - "Vinícius De Souza"
  - "Tommaso Fontana"
  - "Nomi L Harris"
  - "Emily L Hartley"
  - "Eric Hurwitz"
  - "Julius O B Jacobsen"
  - "Madan Krishnamurthy"
  - "Bryan J Laraway"
  - "James A McLaughlin"
  - "Julie A McMurry"
  - "Sierra A T Moxon"
  - "Kathleen R Mullen"
  - "Shawn T O'Neil"
  - "Kent A Shefchek"
  - "Ray Stefancsik"
  - "Sabrina Toro"
  - "Nicole A Vasilevsky"
  - "Ramona L Walls"
  - "Patricia L Whetzel"
  - "David Osumi-Sutherland"
  - "Damian Smedley"
  - "Peter N Robinson"
  - "Christopher J Mungall"
  - "Melissa A Haendel"
  - "Monica C Munoz-Torres"
  doi: 10.1093/nar/gkad1082
  id: doi:10.1093/nar/gkad1082
  journal: Nucleic Acids Research
  preferred: true
  title: 'The Monarch Initiative in 2024: an analytic platform integrating phenotypes,
    genes and diseases across species'
  year: '2024'
repository: https://github.com/monarch-initiative/phenio
synonyms:
- PHENIO
- An integrated ontology for Phenomics
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

# Phenomics Integrated Ontology (PHENIO)

## Overview

PHENIO is an application ontology for accessing and comparing knowledge concerning phenotypes across species and genetic backgrounds. It is developed by the Monarch Initiative using the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit) and provides the ontological backbone of the Monarch Knowledge Graph.

## Composition

According to the PHENIO ODK configuration (`src/ontology/phenio-odk.yaml`), PHENIO merges:

- **Phenotype ontologies**: uPheno, HP, MP, ZP, XPO, FYPO, WBPhenotype, DDPHENO, DPO, OBA, plus uPheno bridge and alignment axioms
- **Anatomy and development ontologies**: Uberon, CL, FBbt, ZFA, XAO, WBbt, EMAPA, DDANAT, ZFS, FBdv, WBls, HsapDv, BSPO
- **Disease and biological process ontologies**: Mondo, GO
- **Supporting ontologies and vocabularies**: BFO, RO, PATO, ChEBI (slim), PRO (slim), SO, ECO, NCBITaxon (taxslim), MPATH, NBO, FoodOn, Monochrom (CHR), NCBI Gene, HGNC

SSSOM mappings from Uberon, CL, and uPheno (uPheno-OBA) are also used in the build.

## Access

- Latest OWL release: [phenio.owl.gz](https://github.com/monarch-initiative/phenio/releases/latest/download/phenio.owl.gz)
- Latest OBO Graphs JSON release: [phenio.json](https://github.com/monarch-initiative/phenio/releases/latest/download/phenio.json)
- KGX graph (KG-Phenio, which adds uPheno cross-species mappings): [kg-phenio.tar.gz](https://github.com/Knowledge-Graph-Hub/kg-phenio/releases/latest/download/kg-phenio.tar.gz)
- Documentation: [https://monarch-initiative.github.io/phenio/](https://monarch-initiative.github.io/phenio/)
- Repository: [https://github.com/monarch-initiative/phenio](https://github.com/monarch-initiative/phenio)

## Citation

Putman TE, et al. The Monarch Initiative in 2024: an analytic platform integrating phenotypes, genes and diseases across species. Nucleic Acids Research. 2024. doi:10.1093/nar/gkad1082

## Information Resource ID

This resource has the Information Resource identifier: `infores:phenio`
