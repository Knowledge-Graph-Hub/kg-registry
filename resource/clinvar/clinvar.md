---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: clinvar@ncbi.nlm.nih.gov
    id: ncbi
    label: ClinVar Team, National Center for Biotechnology Information (NCBI)
creation_date: '2025-06-04T00:00:00Z'
description: ClinVar is a freely accessible, public archive of reports of human genetic variations and their relationships to human health. It collects and presents data on variants found in patient samples, classifications for diseases and drug responses, and supporting evidence. ClinVar enables access to and communication about the clinical significance of genetic variants, providing healthcare professionals, researchers, and the public with vital information for interpreting genetic test results.
domains:
  - biomedical
  - genomics
  - clinical
  - precision medicine
  - health
  - translational
homepage_url: https://www.ncbi.nlm.nih.gov/clinvar/
id: clinvar
infores_id: clinvar
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: NCBI and NLM Data Usage Policies and Disclaimers
name: ClinVar
products:
  - category: Product
    description: Complete public data set in XML format containing comprehensive variant information, clinical significance classifications, and supporting evidence.
    format: xml
    id: clinvar.xml
    name: ClinVar XML
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/xml/
    original_source:
      - source: clinvar
        relation_type: prov:hadPrimarySource
  - category: Product
    description: ClinVar data in VCF format for GRCh37 human genome assembly, containing variant information and clinical significance.
    format: vcf
    id: clinvar.vcf.grch37
    name: ClinVar VCF (GRCh37)
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/
    original_source:
      - source: clinvar
        relation_type: prov:hadPrimarySource
  - category: Product
    description: ClinVar data in VCF format for GRCh38 human genome assembly, containing variant information and clinical significance.
    format: vcf
    id: clinvar.vcf.grch38
    name: ClinVar VCF (GRCh38)
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/
    original_source:
      - source: clinvar
        relation_type: prov:hadPrimarySource
  - category: Product
    description: Tab-delimited files summarizing variant data, gene-condition relationships, and other aspects of ClinVar data.
    format: tsv
    id: clinvar.tab
    name: ClinVar Tab-Delimited Files
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/
    original_source:
      - source: clinvar
        relation_type: prov:hadPrimarySource
  - category: ProgrammingInterface
    description: API access to ClinVar data through NCBI's E-utilities, supporting programmatic queries and data retrieval.
    format: http
    id: clinvar.api
    name: ClinVar API (E-utilities)
    product_url: https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/
    original_source:
      - source: clinvar
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Web interface for searching and browsing ClinVar data, with detailed variant information and evidence.
    format: http
    id: clinvar.web
    name: ClinVar Web Interface
    product_url: https://www.ncbi.nlm.nih.gov/clinvar/
    original_source:
      - source: clinvar
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: loinc
      - relation_type: prov:hadPrimarySource
        source: icd10
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: obi
      - relation_type: prov:hadPrimarySource
        source: obib
      - relation_type: prov:hadPrimarySource
        source: edam
      - relation_type: prov:hadPrimarySource
        source: hsapdv
      - relation_type: prov:hadPrimarySource
        source: sbo
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: ordo
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: uo
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: pgo
      - relation_type: prov:hadPrimarySource
        source: gencode
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: hra
      - relation_type: prov:hadPrimarySource
        source: hubmap
      - relation_type: prov:hadPrimarySource
        source: sennet
      - relation_type: prov:hadPrimarySource
        source: stellar
      - relation_type: prov:hadPrimarySource
        source: dct
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: connectivitymap
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: msigdb
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: 4dn
      - relation_type: prov:hadPrimarySource
        source: erccrbp
      - relation_type: prov:hadPrimarySource
        source: erccreg
      - relation_type: prov:hadPrimarySource
        source: faldo
      - relation_type: prov:hadPrimarySource
        source: glycordf
      - relation_type: prov:hadPrimarySource
        source: glycocoo
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: kidsfirst
      - relation_type: prov:hadPrimarySource
        source: lincs
      - relation_type: prov:hadPrimarySource
        source: motrpac
      - relation_type: prov:hadPrimarySource
        source: mw
      - relation_type: prov:hadPrimarySource
        source: npo
      - relation_type: prov:hadPrimarySource
        source: sckan
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: biomarker
      - relation_type: prov:hadPrimarySource
        source: opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: ubkg
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: loinc
      - relation_type: prov:hadPrimarySource
        source: icd10
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: obi
      - relation_type: prov:hadPrimarySource
        source: obib
      - relation_type: prov:hadPrimarySource
        source: edam
      - relation_type: prov:hadPrimarySource
        source: hsapdv
      - relation_type: prov:hadPrimarySource
        source: sbo
      - relation_type: prov:hadPrimarySource
        source: mi
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: ordo
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: uo
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: pgo
      - relation_type: prov:hadPrimarySource
        source: gencode
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: hra
      - relation_type: prov:hadPrimarySource
        source: hubmap
      - relation_type: prov:hadPrimarySource
        source: sennet
      - relation_type: prov:hadPrimarySource
        source: stellar
      - relation_type: prov:hadPrimarySource
        source: dct
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: connectivitymap
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: msigdb
      - relation_type: prov:hadPrimarySource
        source: wikipathways
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: 4dn
      - relation_type: prov:hadPrimarySource
        source: erccrbp
      - relation_type: prov:hadPrimarySource
        source: erccreg
      - relation_type: prov:hadPrimarySource
        source: faldo
      - relation_type: prov:hadPrimarySource
        source: glycordf
      - relation_type: prov:hadPrimarySource
        source: glycocoo
      - relation_type: prov:hadPrimarySource
        source: gtex
      - relation_type: prov:hadPrimarySource
        source: kidsfirst
      - relation_type: prov:hadPrimarySource
        source: lincs
      - relation_type: prov:hadPrimarySource
        source: motrpac
      - relation_type: prov:hadPrimarySource
        source: mw
      - relation_type: prov:hadPrimarySource
        source: npo
      - relation_type: prov:hadPrimarySource
        source: sckan
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: biomarker
      - relation_type: prov:hadPrimarySource
        source: opentargets
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: ubkg
  - category: GraphProduct
    description: DisGeNET data, including gene to disease associations and variant to disease associations (requires registration and subscription).
    id: disgenet.data
    name: DisGeNET Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: clingen
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: mgd
      - relation_type: prov:hadPrimarySource
        source: rgd
      - relation_type: prov:hadPrimarySource
        source: orphanet
      - relation_type: prov:hadPrimarySource
        source: psygenet
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
      - relation_type: prov:hadPrimarySource
        source: phewascat
      - relation_type: prov:hadPrimarySource
        source: ukbiobank
      - relation_type: prov:hadPrimarySource
        source: finngen
      - relation_type: prov:hadPrimarySource
        source: clinicaltrialsgov
    product_url: https://www.disgenet.com/
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: disgenet
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: GraphProduct
    description: PheKnowLator graph files, including subsets with and without inverse relations.
    format: owl
    id: pheknowlator.graph
    latest_version: current_build
    name: PheKnowLator graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: pw
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: so
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: vo
      - relation_type: prov:hadPrimarySource
        source: bioportal
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: genemania
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: uniprot
    product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: pheknowlator
    versions:
      - v1.0.0
      - v2.0.0
      - v2.1.0
      - v3.0.2
      - v4.0.0
      - current_build
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
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
      - relation_type: prov:hadPrimarySource
        source: phenio
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
        source: maxo
      - relation_type: prov:hadPrimarySource
        source: panther
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
      - relation_type: prov:wasInfluencedBy
        source: kg-monarch
  - category: Product
    description: Disease association data integrated from OMIM, MalaCards, ClinVar, Orphanet, DisGeNET and other disease databases
    format: http
    id: genecards.disease.associations
    name: GeneCards Disease Associations
    original_source:
      - relation_type: prov:hadPrimarySource
        source: omim
      - relation_type: prov:hadPrimarySource
        source: malacards
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: orphanet
      - relation_type: prov:hadPrimarySource
        source: disgenet
    product_url: https://www.genecards.org/
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 403 error when accessing file'
  - category: Product
    description: Genetic variant data from ClinVar, dbSNP, GWAS Catalog and other variant databases
    format: http
    id: genecards.variant.data
    name: GeneCards Variant Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: dbsnp
      - relation_type: prov:hadPrimarySource
        source: gwascatalog
    product_url: https://www.genecards.org/
    warnings:
      - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when accessing file
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 403 error when accessing file'
      - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 403 error when accessing file'
publications:
  - authors:
      - Landrum MJ
      - Chitipiralla S
      - Kaur K
      - Brown G
      - Chen C
      - Hart J
      - Hoffman D
      - Jang W
      - Liu C
      - Maddipatla Z
      - Maiti R
      - Mitchell J
      - Rezaie T
      - Riley G
      - Song G
      - Yang J
      - Ziyabari L
      - Russette A
      - Kattman BL
    doi: 10.1093/nar/gkae1090
    id: doi:10.1093/nar/gkae1090
    journal: Nucleic Acids Research
    preferred: true
    title: 'ClinVar: updates to support classifications of both germline and somatic variants'
    year: '2024'
  - authors:
      - Landrum MJ
      - Lee JM
      - Benson M
      - Brown GR
      - Chao C
      - Chitipiralla S
      - Gu B
      - Hart J
      - Hoffman D
      - Jang W
      - Karapetyan K
      - Katz K
      - Liu C
      - Maddipatla Z
      - Malheiro A
      - McDaniel K
      - Ovetsky M
      - Riley G
      - Zhou G
      - Holmes JB
      - Kattman BL
      - Maglott DR
    doi: 10.1093/nar/gkx1153
    id: doi:10.1093/nar/gkx1153
    journal: Nucleic Acids Research
    title: ClinVar - improving access to variant interpretations and supporting evidence
    year: '2018'
taxon:
  - NCBITaxon:9606
---

# ClinVar

ClinVar is a freely accessible, public archive maintained by the National Center for Biotechnology Information (NCBI) that catalogs the relationships between human genetic variations and phenotypes, with supporting evidence. It serves as a critical resource for the clinical genetics community by providing a centralized repository of variant interpretations and their clinical significance.

## Overview

ClinVar collects, curates, and distributes information about:
- Human genomic variations (from single nucleotide variants to large structural variants)
- Clinical significance classifications (pathogenic, likely pathogenic, uncertain significance, likely benign, benign)
- Supporting evidence for classifications
- Relationships between variants and diseases or drug responses
- Submitter information and review status

The database integrates submissions from clinical testing laboratories, research groups, expert panels, and professional societies, making it a comprehensive resource for variant interpretation in clinical settings.

## Content

ClinVar contains data on variants across the entire human genome, including:

- **Variant classifications**: Clinical significance determinations from submitters
- **Variant details**: HGVS expressions, genomic locations, allele identifiers
- **Condition information**: Medical conditions associated with variants, mapped to MedGen
- **Evidence details**: Supporting evidence for classifications, including case data, functional studies, and population frequencies
- **Submitter information**: Source of variant classifications and contact details
- **Review status**: Level of expert review for each classification, from no assertion criteria to practice guideline
- **Version history**: Previous versions of submitted records and changes over time

ClinVar accepts submissions for variants identified through various methods, including clinical testing, research, and literature curation. It does not include GWAS data or variants observed but not classified.

## Data Access

ClinVar data is available through multiple channels:

1. **Web Interface**: Interactive search and browsing, with detailed variant pages
2. **API Access**: Programmatic access via NCBI's E-utilities for integration into bioinformatics workflows
3. **Data Downloads**: Full and partial data dumps in multiple formats:
   - XML files containing the complete dataset
   - VCF files for GRCh37 and GRCh38 assemblies
   - Tab-delimited summary files of variants, gene-disease relationships, and more

The data is updated weekly on the website, with comprehensive monthly releases available for download on the first Thursday of each month.

## Integration and Collaboration

ClinVar works closely with the ClinGen project and other initiatives to improve the quality and interpretation of genomic variants. It provides data exchange mechanisms with numerous resources, including:

- NCBI resources (Gene, MedGen, dbSNP, dbVar)
- External databases (OMIM, GTR, Variation Viewer)
- Professional organization guidelines and expert panel evaluations

As a vital component of the clinical genomics ecosystem, ClinVar continuously evolves to meet the needs of the genetics community and support the implementation of precision medicine.
