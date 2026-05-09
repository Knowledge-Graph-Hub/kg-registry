---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: support@clinicalgenome.org
      - contact_type: url
        value: https://clinicalgenome.org/about/contact-clingen/
    label: ClinGen
creation_date: '2025-06-04T00:00:00Z'
description: The Clinical Genome Resource (ClinGen) is a National Institutes of Health (NIH)-funded resource dedicated to building a central resource that defines the clinical relevance of genes and variants for use in precision medicine and research. ClinGen brings together clinical and research experts to develop standard approaches for interpreting genomic variants, curate evidence for gene-disease relationships, and share this knowledge through freely accessible databases.
domains:
  - genomics
  - biomedical
  - clinical
  - health
homepage_url: https://clinicalgenome.org/
id: clingen
infores_id: clingen
last_modified_date: '2026-01-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: ClinGen
products:
  - category: Product
    description: ClinGen Gene-Disease Validity curations assess the strength of evidence supporting or refuting a gene's role in a given disease. These curations classify evidence as Definitive, Strong, Moderate, Limited, No Reported Evidence, or Disputed.
    format: csv
    id: clingen.gene-disease
    name: Gene-Disease Validity Curations
    product_url: https://search.clinicalgenome.org/kb/gene-validity
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
  - category: Product
    description: ClinGen Dosage Sensitivity curations evaluate whether genes and genomic regions are sensitive to copy number variation. These curations determine if haploinsufficiency (loss of one copy) or triplosensitivity (gain of one copy) of a gene/region causes disease.
    format: tsv
    id: clingen.dosage
    name: Dosage Sensitivity Curations
    product_url: https://search.clinicalgenome.org/kb/gene-dosage
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
  - category: Product
    description: ClinGen Clinical Actionability evaluations assess the clinical actions available to manage risk for patients with specific genetic disorders. These curations score the actionability of gene-disease pairs based on severity, likelihood of disease, efficacy of interventions, and knowledge base.
    format: tsv
    id: clingen.actionability
    name: Clinical Actionability Curations
    product_url: https://search.clinicalgenome.org/kb/actionability
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
  - category: Product
    description: ClinGen Variant Pathogenicity curations assess the clinical significance of genetic variants based on ACMG/AMP guidelines. Expert panels classify variants as Pathogenic, Likely Pathogenic, Uncertain Significance, Likely Benign, or Benign.
    format: csv
    id: clingen.variant
    name: Variant Pathogenicity Curations
    product_url: https://search.clinicalgenome.org/kb/variant-pathogenicity/all
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
  - category: ProgrammingInterface
    description: REST API providing access to ClinGen's Evidence Repository for variant pathogenicity assessments. Allows programmatic retrieval of structured evidence used to evaluate the clinical significance of genetic variants.
    id: clingen.evrepo.api
    name: ClinGen Evidence Repository API
    product_url: https://erepo.clinicalgenome.org/evrepo/api/
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Web-based interface for accessing ClinGen's curated data. Allows users to search and browse curated gene-disease pairs, variant interpretations, and other ClinGen resources.
    id: clingen.web.interface
    name: ClinGen Search Interface
    product_url: https://search.clinicalgenome.org/
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
  - category: ProcessProduct
    description: Framework for standardized interpretation of genetic variants, including disease-specific modifications to the ACMG/AMP guidelines. These frameworks guide variant classification by expert panels and clinical laboratories.
    id: clingen.variant.frameworks
    name: Variant Interpretation Frameworks
    product_url: https://www.clinicalgenome.org/working-groups/sequence-variant-interpretation/
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: DisGeNET data, including gene to disease associations and variant to disease associations (requires registration and subscription).
    id: disgenet.data
    name: DisGeNET Data
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: mgd
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: orphanet
        relation_type: prov:hadPrimarySource
      - source: psygenet
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: phewascat
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: finngen
        relation_type: prov:hadPrimarySource
      - source: clinicaltrialsgov
        relation_type: prov:hadPrimarySource
    product_url: https://www.disgenet.com/
    secondary_source:
      - source: disgenet
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: KGX Distribution of KG-Monarch
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 230877741
    product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: KGX JSON-Lines Distribution of KG-Monarch
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 315667976
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: RDF Distribution of KG-Monarch
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 879238775
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Neo4j Dump of KG-Monarch
    dump_format: neo4j
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 1438250397
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
    warnings: []
  - category: GraphProduct
    description: DuckDB database of KG-Monarch
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 6827814912
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: KGX JSON-Lines Distribution of KG-Monarch (Edges)
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 15279494795
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.jsonl
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: KGX JSON-Lines Distribution of KG-Monarch (Nodes)
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 1149505896
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.jsonl
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Neo4j Dump of KG-Monarch Edges
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 4386388748
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_edges.neo4j.csv
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Neo4j Dump of KG-Monarch Nodes
    edge_count: 15371045
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
    node_count: 1449211
    original_source:
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
    predicates:
      - biolink:actively_involved_in
      - biolink:acts_upstream_of
      - biolink:acts_upstream_of_negative_effect
      - biolink:acts_upstream_of_or_within
      - biolink:acts_upstream_of_or_within_negative_effect
      - biolink:acts_upstream_of_or_within_positive_effect
      - biolink:acts_upstream_of_positive_effect
      - biolink:applied_to_treat
      - biolink:associated_with_increased_likelihood_of
      - biolink:caused_by
      - biolink:causes
      - biolink:colocalizes_with
      - biolink:contributes_to
      - biolink:disease_has_location
      - biolink:disrupts
      - biolink:enables
      - biolink:expressed_in
      - biolink:gene_associated_with_condition
      - biolink:genetically_associated_with
      - biolink:has_adverse_event
      - biolink:has_disease
      - biolink:has_gene
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
      - biolink:related_to
      - biolink:same_as
      - biolink:subclass_of
      - biolink:treats
      - biolink:treats_or_applied_or_studied_to_treat
    product_file_size: 349573789
    product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg_nodes.neo4j.csv
    secondary_source:
      - source: kg-monarch
        relation_type: prov:wasInfluencedBy
publications:
  - authors:
      - Rehm HL
      - Berg JS
      - Brooks LD
      - Bustamante CD
      - Evans JP
      - Landrum MJ
      - Ledbetter DH
      - et al.
    doi: doi:10.1056/NEJMsr1406261
    id: https://doi.org/10.1056/NEJMsr1406261
    journal: New England Journal of Medicine
    preferred: true
    title: "ClinGen — The Clinical Genome Resource"
    year: '2015'
  - authors:
      - ClinGen Consortium
    doi: doi:10.1016/j.gim.2024.101228
    id: https://doi.org/10.1016/j.gim.2024.101228
    journal: Genetics in Medicine
    title: 'The Clinical Genome Resource (ClinGen): Advancing genomic knowledge through global curation'
    year: '2024'
taxon:
  - NCBITaxon:9606
---

# ClinGen - Clinical Genome Resource

## Overview

The Clinical Genome Resource (ClinGen) is a National Institutes of Health (NIH)-funded resource dedicated to building a central database that defines the clinical relevance of genes and variants for use in precision medicine and research. Founded in 2013, ClinGen is a collaborative effort involving more than 2,700 contributors from over 72 countries who work to curate and standardize information about genomic variants and their relationship to human health.

ClinGen serves as a critical bridge between genomic research and clinical application, enabling better interpretation of genetic testing results and improving patient care through enhanced variant classification. The resource addresses the challenge of interpreting the vast amount of genomic data being generated by modern sequencing technologies.

## Mission and Activities

ClinGen's primary goal is to improve patient care by ensuring that clinicians, researchers, and patients have access to reliable genomic information. The resource achieves this through several key curation activities:

- **Gene-Disease Validity**: Evaluating the strength of evidence supporting relationships between genes and diseases. Gene Curation Expert Panels (GCEPs) classify evidence for gene-disease relationships as Definitive, Strong, Moderate, Limited, No Reported Evidence, or Disputed.

- **Variant Pathogenicity**: Assessing whether specific genetic variants cause disease. Variant Curation Expert Panels (VCEPs) apply the ACMG/AMP guidelines to classify variants as Pathogenic, Likely Pathogenic, Uncertain Significance, Likely Benign, or Benign.

- **Dosage Sensitivity**: Determining if changes in gene copy number (deletions or duplications) result in disease. The Dosage Sensitivity Working Group evaluates whether gains or losses of specific genomic regions lead to clinical phenotypes.

- **Clinical Actionability**: Evaluating medical interventions available for individuals with genetic conditions. The Actionability Working Group assesses what clinical interventions are available for patients with specific genetic disorders and scores their actionability.

- **Somatic Cancer Variant Interpretation**: Curating the clinical significance of genomic alterations in cancer. The Somatic Cancer Working Group applies specialized frameworks to classify cancer-related variants.

## Expert Panels

ClinGen coordinates numerous Expert Panels composed of international experts who evaluate evidence and generate consensus interpretations of genomic variants. As of 2025, there are over 60 active Variant Curation Expert Panels (VCEPs) and Gene Curation Expert Panels (GCEPs) focusing on specific diseases or genes including:

- Hereditary cancer syndromes (BRCA1/2, TP53, PTEN, etc.)
- Cardiovascular disorders (cardiomyopathies, arrhythmias)
- Neurodevelopmental disorders
- Inborn errors of metabolism
- Kidney disorders
- Hearing loss
- RASopathies
- Hereditary eye disorders

These panels follow standardized frameworks to ensure consistency across interpretations and periodically review their classifications as new evidence emerges.

## Data Sharing and Access

All curated content from ClinGen is freely available to the scientific and medical communities under a CC0 1.0 Universal license. The data can be accessed through:

1. The ClinGen website and search interfaces at [clinicalgenome.org](https://clinicalgenome.org/)
2. Downloadable files in various formats (CSV, TSV, BED) from the [ClinGen Downloads page](https://search.clinicalgenome.org/kb/downloads)
3. RESTful APIs for programmatic access, including the Evidence Repository API
4. Integration with other resources like ClinVar, NCBI's database of genomic variation
5. Variant curation interfaces that allow expert panels to submit evidence-based classifications

ClinGen also partners with patient registries and data sharing platforms like GenomeConnect to enhance the collection of phenotypic information associated with genetic variants.

## Impact on Clinical Practice

ClinGen resources are widely used in clinical genomics, serving as an authoritative source for variant interpretation in genetic testing. In 2018, the FDA recognized ClinGen as the first FDA-designated public genetic variant database, allowing test developers to use ClinGen's variant classifications as clinical validity support for genetic tests without the need for additional FDA review.

The resource has significantly improved standardization in variant interpretation across laboratories through:

- Development and refinement of the ACMG/AMP variant interpretation guidelines
- Creation of disease-specific modifications to these guidelines
- Providing a framework for resolving differences in variant interpretation between laboratories
- Supporting clinical decision-making for healthcare providers managing patients with genetic conditions

ClinGen has also established formal partnerships with other genomic resources including ClinVar, CPIC (Clinical Pharmacogenetics Implementation Consortium), PharmGKB, and international genomic medicine initiatives to enhance the global standardization of genomic information.

## Community Curation and Education

ClinGen supports community involvement through:

- The ClinGen Community Curation (C3) program that enables researchers, clinicians, and trainees to contribute to gene and variant curation
- Educational resources and training materials for variant interpretation
- Regular webinars and workshops for the genomic medicine community
- Support for implementation of genomic medicine in diverse healthcare settings

Through these efforts, ClinGen is driving the advancement of precision medicine by creating a standardized, centralized resource for clinically relevant genomic knowledge.
