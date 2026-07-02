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
- category: Organization
  contact_details:
  - contact_type: url
    value: https://geneontology.org/
  id: gene-ontology-consortium
  label: Gene Ontology Consortium
creation_date: '2025-03-16T00:00:00Z'
description: An ontology for describing the function of genes and gene products
domains:
- biomedical
- biological systems
homepage_url: http://geneontology.org/
id: go
infores_id: go
last_modified_date: '2026-06-22T00:00:00Z'
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 129706298
  product_url: http://purl.obolibrary.org/obo/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, in obo format
  format: obo
  id: go.obo
  name: GO (OBO Format edition)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 36555702
  product_url: http://purl.obolibrary.org/obo/go.obo
- category: OntologyProduct
  description: Equivalent to go.owl, in obograph json format
  format: json
  id: go.json
  name: GO (JSON edition)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go.json
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-01: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-07-02: No Content-Length
    header found'
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    with subsets of those ontologies
  format: owl
  id: go.extensions.go-plus.owl
  name: GO-Plus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 236488701
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.owl
- category: OntologyProduct
  description: As go-plus.owl, in obographs json format
  format: json
  id: go.extensions.go-plus.json
  name: GO-Plus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.json
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-01: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-07-02: No Content-Length
    header found'
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    excluding the external ontologies themselves
  format: owl
  id: go.go-base.owl
  name: GO Base Module
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 160974965
  product_url: http://purl.obolibrary.org/obo/go/go-base.owl
- category: OntologyProduct
  description: Basic version of the GO, filtered such that the graph is guaranteed
    to be acyclic and annotations can be propagated up the graph. The relations included
    are is a, part of, regulates, negatively regulates and positively regulates. This
    version excludes relationships that cross the 3 GO hierarchies.
  format: obo
  id: go.go-basic.obo
  name: GO-Basic, Filtered, for use with legacy tools
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 32126692
  product_url: http://purl.obolibrary.org/obo/go/go-basic.obo
- category: OntologyProduct
  description: As go-basic.obo, in json format
  format: json
  id: go.go-basic.json
  name: GO-Basic, Filtered, for use with legacy tools (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/go-basic.json
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-01: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-07-02: No Content-Length
    header found'
- category: OntologyProduct
  description: Classes added to ncbitaxon for taxon subsets such as prokaryotes
  format: owl
  id: go.extensions.go-taxon-subsets.owl
  name: GO Taxon Subsets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 5795
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-taxon-subsets.owl
- category: OntologyProduct
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: owl
  id: go.snapshot.go.owl
  name: GO (OWL edition), daily snapshot release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 129908636
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: obo
  id: go.snapshot.go.obo
  name: GO (OBO Format edition), daily snapshot release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 36684860
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.obo
- category: GraphicalInterface
  description: Official GO browser for ontology terms, gene products, and annotations.
  format: http
  id: go.amigo
  is_public: true
  name: AmiGO 2
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://amigo.geneontology.org/amigo
- category: ProgrammingInterface
  description: Official Gene Ontology API for term, annotation, and related programmatic
    access.
  format: http
  id: go.api
  is_public: true
  name: Gene Ontology API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://api.geneontology.org/
- category: GraphicalInterface
  description: Browser for searching and viewing Gene Ontology terms and GOA annotations
  format: http
  id: goa.quickgo
  name: QuickGO Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://www.ebi.ac.uk/QuickGO/
- category: Product
  description: FTP site containing current and archived GOA annotation files for all
    species
  format: http
  id: goa.ftp
  name: GOA FTP Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: uniprot
  - relation_type: prov:wasInformedBy
    source: rnacentral
  - relation_type: prov:wasInformedBy
    source: complexportal
- category: Product
  description: GO annotations for all UniProtKB entries
  format: txt
  id: goa.uniprot
  latest_version: '232'
  name: UniProt GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/
- category: Product
  description: GO annotations for human proteins
  format: txt
  id: goa.human
  name: Human GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/
- category: Product
  description: GO annotations for mouse proteins
  format: txt
  id: goa.mouse
  name: Mouse GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/MOUSE/
- category: MappingProduct
  description: Files containing transitive assignments of InterPro matches, UniProtKB
    keywords, subcellular locations, EC numbers, or HAMAP matches to manually-selected
    GO terms
  format: txt
  id: goa.mapping-files
  name: GO Mapping Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/
- category: Product
  description: GO annotations for PDB entries
  format: txt
  id: goa.pdb
  name: PDB GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: pdbe
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/PDB/
- category: Product
  description: GO annotations organized by proteomes
  format: txt
  id: goa.proteomes
  name: Proteomes GOA Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  product_url: https://ftp.ebi.ac.uk/pub/databases/GO/goa/proteomes/
- category: GraphProduct
  compression: gzip
  description: Pathway-like GO-CAM causal activity models distributed as RDF Turtle.
  format: ttl
  id: go.gocams.ttl
  name: GO-CAM TTL Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 3260184
  product_url: http://current.geneontology.org/products/ttl/pathway-like_go-cams.tar.gz
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
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
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  format: mixed
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  compression: targz
  description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
  format: kgx
  id: kg-microbe.graph.raw
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: KG-Microbe KGX Graph - Raw
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 4640682152
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
- category: GraphProduct
  description: Core UniBioMap graph edges file.
  format: csv
  id: unibiomap.links
  name: UniBioMap Graph Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 1406201678
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
- category: GraphProduct
  description: Auxiliary UniBioMap graph annotations and metadata.
  format: tsv
  id: unibiomap.auxs
  name: UniBioMap Graph Auxiliaries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 591290539
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
- category: GraphProduct
  description: Predicted UniBioMap graph edges with confidence scores.
  format: csv
  id: unibiomap.pred
  name: UniBioMap Predicted Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 2484982268
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
- category: GraphProduct
  description: Full unfiltered UniBioMap predicted graph edges file.
  format: csv
  id: unibiomap.pred.full
  name: UniBioMap Predicted Graph (Full)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: tcdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: batman
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: compath
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
- category: OntologyProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: cob
  - relation_type: prov:hadPrimarySource
    source: dc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: ma
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: oio
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semapv
  - relation_type: prov:hadPrimarySource
    source: skos
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: zfa
  product_file_size: 240665663
  product_url: https://www.ebi.ac.uk/efo/efo.owl
- category: OntologyProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: cob
  - relation_type: prov:hadPrimarySource
    source: dc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: ecto
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hancestro
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ido
  - relation_type: prov:hadPrimarySource
    source: ma
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: oio
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: omo
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semapv
  - relation_type: prov:hadPrimarySource
    source: skos
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: zfa
  product_file_size: 64058275
  product_url: https://www.ebi.ac.uk/efo/efo.obo
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  format: python
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/gyorilab/indra_cogex
- category: MappingProduct
  description: bigg.compartment SSSOM
  format: sssom
  id: obo-db-ingest.bigg.compartment.sssom.tsv
  license:
    id: http://bigg.ucsd.edu/license#license
    label: Custom
  name: bigg.compartment SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 242
  product_url: https://w3id.org/biopragmatics/resources/bigg.compartment/bigg.compartment.sssom.tsv
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, scored links between proteins)
  format: txt
  id: string.protein.links
  name: STRING Protein Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 138154280240
  product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, incl. subscores per channel)
  format: txt
  id: string.protein.links.detailed
  name: STRING Protein Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 203534412387
  product_url: https://stringdb-downloads.org/download/protein.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (full network, incl. distinction: direct vs.
    interologs)'
  format: txt
  id: string.protein.links.full
  name: STRING Protein Links Full
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 214269334954
  product_url: https://stringdb-downloads.org/download/protein.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, scored links between proteins)
  format: txt
  id: string.protein.physical.links
  name: STRING Protein Physical Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 11867396121
  product_url: https://stringdb-downloads.org/download/protein.physical.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, incl. subscores per channel)
  format: txt
  id: string.protein.physical.links.detailed
  name: STRING Protein Physical Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 14859366689
  product_url: https://stringdb-downloads.org/download/protein.physical.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (physical subnetwork, incl. distinction: direct
    vs. interologs)'
  format: txt
  id: string.protein.physical.links.full
  name: STRING Protein Physical Links Full
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 15528028374
  product_url: https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores between orthologous groups
  format: txt
  id: string.cog.links
  name: STRING COG Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 185338269
  product_url: https://stringdb-downloads.org/download/COG.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores (incl. subscores per channel)
  format: txt
  id: string.cog.links.detailed
  name: STRING COG Links Detailed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 250279091
  product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'full database, part II: the networks (nodes, edges, scores,...)'
  format: postgres
  id: string.database
  name: STRING Database Network Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: cog
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: dip
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: eggnog
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: progenomes
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: swissmodel
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_file_size: 281505096430
  product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
- description: The MechRepoNet knowledge graph in its original format
  format: mixed
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
- category: ProgrammingInterface
  description: Plover-hosted TRAPI web API for querying the Multiomics Microbiome
    knowledge graph
  format: http
  id: microbiomekg.api
  is_public: true
  name: MicrobiomeKG Plover TRAPI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: eupathdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: microbiomekg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://multiomics.transltr.io/mbkp
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: genemania
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vo
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
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
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
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
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: clinicalkg
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Graph database dump and additional relationship files for the Clinical
    Knowledge Graph.
  format: neo4j
  id: ckg.graph
  latest_version: '1'
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: CKG Graph Database Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cancer-genome-interpreter
  - relation_type: prov:hadPrimarySource
    source: ckg
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mod
  - relation_type: prov:hadPrimarySource
    source: ms
  - relation_type: prov:hadPrimarySource
    source: mutationds
  - relation_type: prov:hadPrimarySource
    source: oncokb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: phosphositeplus
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: Product
  description: Gene Ontology Causal Activity Model (GO-CAM) annotations manually curated
    by Gene Ontology biocurators linking genes, proteins, and biological processes.
    Distributed as the canonical noctua-models repository, where each model is stored
    as a Turtle (TTL) file.
  format: ttl
  id: cam-kp.go-cams
  name: Gene Ontology CAMs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cam-kp
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://github.com/geneontology/noctua-models
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_file_size: 376501785
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_file_size: 1807360397
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  format: http
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: rtx-kg2
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: smpdb
  product_url: https://arax.ncats.io/
- category: GraphProduct
  description: RNA-KG as a Neo4j Dump
  format: neo4j
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
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
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugmechdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://doi.org/10.5281/zenodo.8139357
  repository: https://github.com/SuLab/DrugMechDB
  versions:
  - 2.0.1
  - 2.0.0
  - 1.0.2
  - '1.0'
- category: GraphProduct
  description: RDF dump of the Open Research Knowledge Graph distributed in N-Triples
    format.
  format: ntriples
  id: orkg.dump
  name: ORKG RDF Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orkg
  - relation_type: prov:hadPrimarySource
    source: wikidata
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 642902930
  product_url: https://orkg.org/files/rdf-dumps/rdf-export-orkg.nt
- category: OntologyProduct
  description: OWL release of Monochrom Ontology
  format: owl
  id: chr.model.owl
  name: Monochrom Ontology OWL release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chr
  - relation_type: prov:hadPrimarySource
    source: geno
  - relation_type: prov:hadPrimarySource
    source: gff
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: skos
  product_file_size: 102365
  product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
- category: Product
  description: Gene ontology annotations from the Gene Ontology Consortium
  format: http
  id: genecards.gene.ontology
  name: GeneCards Gene Ontology Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: Product
  compression: 7z
  description: Compressed CSV file containing ProteomeHD v1.1, with 10,323 proteins
    measured across 294 SILAC ratios
  format: csv
  id: proteomehd.data
  name: ProteomeHD Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomehd
  product_file_size: 9427082
  product_url: https://raw.githubusercontent.com/Rappsilber-Laboratory/ProteomeHD/master/Data/ProteomeHD_v1_1.7z
- category: MappingProduct
  description: Mappings between InterPro entries and Gene Ontology (GO) terms
  format: tsv
  id: interpro.interpro2go
  name: InterPro to GO Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: interpro
  product_file_size: 3088718
  product_url: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro2go
- category: MappingProduct
  compression: gzip
  description: Gene to Gene Ontology mapping data providing functional annotations
    for genes
  format: tsv
  id: ncbigene.gene2go
  name: Gene to GO Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_file_size: 1322439983
  product_url: https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2go.gz
- category: GraphProduct
  description: GO term hierarchy edges
  format: csv
  id: prokn.go.goterm.is_a.goterm.edges
  name: ProKN GO Term Hierarchy Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 11917762
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.GOTerm.IS_A.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of GO term edges
  format: csv
  id: prokn.go.protein.acts_upstream_of.goterm.edges
  name: ProKN GO Acts Upstream Of Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 158931
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of negative effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_negative_effect.goterm.edges
  name: ProKN GO Acts Upstream Negative Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 10441
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within.goterm.edges
  name: ProKN GO Acts Upstream Or Within Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 714349
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within negative effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within_negative_effect.goterm.edges
  name: ProKN GO Acts Upstream Or Within Negative Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4257
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of or within positive effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_or_within_positive_effect.goterm.edges
  name: ProKN GO Acts Upstream Or Within Positive Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 13894
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_OR_WITHIN_POSITIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein acts upstream of positive effect edges
  format: csv
  id: prokn.go.protein.acts_upstream_of_positive_effect.goterm.edges
  name: ProKN GO Acts Upstream Positive Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 32541
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ACTS_UPSTREAM_OF_POSITIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein colocalizes with GO term edges
  format: csv
  id: prokn.go.protein.colocalizes_with.goterm.edges
  name: ProKN GO Colocalizes Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 261555
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.COLOCALIZES_WITH.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein contributes to GO term edges
  format: csv
  id: prokn.go.protein.contributes_to.goterm.edges
  name: ProKN GO Contributes To Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 310541
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.CONTRIBUTES_TO.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein enables GO term edges
  format: csv
  id: prokn.go.protein.enables.goterm.edges
  name: ProKN GO Enables Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 53141599
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.ENABLES.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein involved in GO term edges
  format: csv
  id: prokn.go.protein.involved_in.goterm.edges
  name: ProKN GO Involved In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 43447452
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.INVOLVED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein active in GO term edges
  format: csv
  id: prokn.go.protein.is_active_in.goterm.edges
  name: ProKN GO Active In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1630623
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.IS_ACTIVE_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein located in GO term edges
  format: csv
  id: prokn.go.protein.located_in.goterm.edges
  name: ProKN GO Located In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 50784436
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.LOCATED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not acts upstream of or within edges
  format: csv
  id: prokn.go.protein.not_acts_upstream_of_or_within.goterm.edges
  name: ProKN GO Not Acts Upstream Or Within Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1796
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ACTS_UPSTREAM_OF_OR_WITHIN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not acts upstream of or within negative effect edges
  format: csv
  id: prokn.go.protein.not_acts_upstream_of_or_within_negative_effect.goterm.edges
  name: ProKN GO Not Acts Upstream Negative Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 455
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ACTS_UPSTREAM_OF_OR_WITHIN_NEGATIVE_EFFECT.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not colocalizes with GO term edges
  format: csv
  id: prokn.go.protein.not_colocalizes_with.goterm.edges
  name: ProKN GO Not Colocalizes Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 3336
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_COLOCALIZES_WITH.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not contributes to GO term edges
  format: csv
  id: prokn.go.protein.not_contributes_to.goterm.edges
  name: ProKN GO Not Contributes Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 3198
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_CONTRIBUTES_TO.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not enables GO term edges
  format: csv
  id: prokn.go.protein.not_enables.goterm.edges
  name: ProKN GO Not Enables Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 129748
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_ENABLES.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not involved in GO term edges
  format: csv
  id: prokn.go.protein.not_involved_in.goterm.edges
  name: ProKN GO Not Involved In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 143198
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_INVOLVED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not active in GO term edges
  format: csv
  id: prokn.go.protein.not_is_active_in.goterm.edges
  name: ProKN GO Not Active In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 893
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_IS_ACTIVE_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not located in GO term edges
  format: csv
  id: prokn.go.protein.not_located_in.goterm.edges
  name: ProKN GO Not Located In Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 52743
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_LOCATED_IN.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein not part of GO term edges
  format: csv
  id: prokn.go.protein.not_part_of.goterm.edges
  name: ProKN GO Not Part Of Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 4731
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.NOT_PART_OF.GOTerm.edges.csv
- category: GraphProduct
  description: GO protein part of GO term edges
  format: csv
  id: prokn.go.protein.part_of.goterm.edges
  name: ProKN GO Part Of Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 3629548
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/GO.Protein.PART_OF.GOTerm.edges.csv
- category: Product
  description: TSV export of SwissLipids links to Gene Ontology terms with taxon context.
  format: tsv
  id: swisslipid.go
  name: SwissLipids GO Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 48388
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=go.tsv
- category: GraphProduct
  description: UniBioMap Gene Ontology entity descriptions.
  format: json
  id: unibiomap.go_desc
  name: UniBioMap GO Descriptions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: unibiomap
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/go_desc.json
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ No Content-Length
    header found
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to Gene Ontology terms
  format: tsv
  id: oma.mapping.go
  name: OMA to GO Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://omabrowser.org/All/oma-go.txt.gz
  warnings: []
- category: Product
  compression: gzip
  description: Gene association file for Reactome GO annotations
  format: txt
  id: reactome.go-associations.txt
  name: Reactome Gene Association File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 835232
  product_url: https://download.reactome.org/96/gene_association.reactome.gz
- category: Product
  description: Mapping from Reactome pathways to Gene Ontology terms
  format: txt
  id: reactome.pathways.go-terms.txt
  name: Reactome Pathways to GO Terms
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 60582
  product_url: https://download.reactome.org/96/Pathways2GoTerms_human.txt
- category: GraphProduct
  description: Neo4j graph database integrating Enrichr gene set libraries with genes,
    terms, pathways, diseases, drugs, cell types, and other functional annotations
  dump_format: neo4j
  format: neo4j
  id: enrichr-kg.graph
  name: Enrichr-KG Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
  product_file_size: 522141103
  product_url: https://s3.amazonaws.com/maayan-kg/enrichr-kg/dumps/enrichr-kg-042123.dump
- category: Product
  description: Edge-table CSV snapshot from the Enrichr-KG downloads page using source.relation.target
    edge triples
  format: csv
  id: enrichr-kg.edges-csv
  name: Enrichr-KG Edge CSV Snapshot
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 35177347
  product_url: https://s3.amazonaws.com/maayan-kg/enrichr-kg/current/GO_Biological_Process_2021.GO_BP.Gene.edges.csv
- category: GraphProduct
  description: Merged knowledge graph data files containing over 400,000 nodes and
    5,000,000 edges integrating gene expression, molecular interactions, functions,
    pathways, homology-based annotations, and environmental exposures from Planteome,
    EMBL-EBI Expression Atlas, and other sources. Available as tab-separated value
    files in KGX format with nodes and edges following the Biolink model.
  format: kgx
  id: genophenoenvo-kg.data
  name: GenoPhenoEnvo KG Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genophenoenvo-kg
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: peco
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: interpro
  product_url: https://datacommons.cyverse.org/browse/iplant/home/shared/genophenoenvo
- category: GraphicalInterface
  description: Browser for complete Hetionet v1.0 graph database in Neo4j
  format: http
  id: hetionet.neo4j
  name: Hetionet v1.0 Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://neo4j.het.io/browser/
- category: GraphProduct
  description: Hetionet v1.0 in JSON format
  format: json
  id: hetionet.data.json
  name: Hetionet v1.0 JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 131
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/json/hetionet-v1.0.json.bz2
- category: GraphProduct
  description: Hetionet v1.0 as a Neo4j database
  format: neo4j
  id: hetionet.data.neo4j
  name: Hetionet v1.0 Neo4j
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 132
  product_url: https://github.com/hetio/hetionet/blob/master/hetnet/neo4j/hetionet-v1.0.db.tar.bz2
- category: GraphProduct
  description: Hetionet v1.0 as SIF edges
  format: sif
  id: hetionet.data.edges
  name: Hetionet v1.0 edges (SIF)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 131
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-edges.sif.gz
- category: GraphProduct
  description: Hetionet v1.0 as TSV nodes
  format: tsv
  id: hetionet.data.nodes
  name: Hetionet v1.0 nodes (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_file_size: 427128
  product_url: https://github.com/hetio/hetionet/blob/main/hetnet/tsv/hetionet-v1.0-nodes.tsv
- category: ProcessProduct
  description: Python package for creating, querying, and operating on hetnets (heterogeneous
    networks)
  format: python
  id: hetnetpy
  name: hetnetpy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://github.com/hetio/hetnetpy
- category: GraphicalInterface
  description: Web application to search and explore connectivity between nodes in
    Hetionet
  format: http
  id: hetionet.search
  name: Hetnet Connectivity Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  product_url: https://het.io/search
- category: GraphProduct
  description: Neo4j knowledge graph containing lncRNAs, protein-coding genes, regulatory
    interactions, and disease associations
  dump_format: neo4j
  format: neo4j
  id: lncrnalyzr.graph
  name: lncRNAlyzr Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lncrnalyzr
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: doid
  product_url: https://github.com/MaayanLab/lncRNAlyzr
- category: GraphicalInterface
  description: Graphical interface for MedKG
  format: http
  id: medkb.site
  name: MedKG Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medkg
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: http://pitools.niper.ac.in/medkg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: medkg
- category: GraphProduct
  description: The OREGANO knowledge graph dataset integrating drug, protein, gene,
    and disease information for drug repositioning.
  format: http
  id: oregano.graph
  name: OREGANO Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oregano
  product_url: https://gitub.u-bordeaux.fr/erias/oregano/-/tree/master/Data_OREGANO/Graphs
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cmaup
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: npass
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: bio2rdf
- category: GraphProduct
  compression: gzip
  description: PharMeBINet V2 JSON release published on February 6, 2024.
  format: json
  id: pharmebinet.json
  latest_version: v2
  name: PharMeBINet JSON Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1942958027
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.json.gz/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 TSV release published on February 6, 2024.
  format: tsv
  id: pharmebinet.tsv
  latest_version: v2
  name: PharMeBINet TSV Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 1922614551
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_tsv_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 GraphML release published on February 6, 2024.
  format: mixed
  id: pharmebinet.graphml
  latest_version: v2
  name: PharMeBINet GraphML Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 2027519087
  product_url: https://zenodo.org/api/records/17814889/files/PharMeBiNet_graphml_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j database release published on February 6, 2024.
  format: neo4j
  id: pharmebinet.neo4j
  latest_version: v2
  name: PharMeBINet Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3847978577
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  compression: zip
  description: PharMeBINet V2 Neo4j dump release published on February 6, 2024.
  dump_format: neo4j
  format: neo4j
  id: pharmebinet.neo4j.dump
  latest_version: v2
  name: PharMeBINet Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmebinet
  product_file_size: 3598325722
  product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_dump_24_02_06.zip/content
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: adrecs
  - relation_type: prov:wasDerivedFrom
    source: aelous
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: bindingdb
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: cl
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: ddinter
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: efo
  - relation_type: prov:wasDerivedFrom
    source: fideo
  - relation_type: prov:wasDerivedFrom
    source: foodon
  - relation_type: prov:wasDerivedFrom
    source: gencc
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hetionet
  - relation_type: prov:wasDerivedFrom
    source: hgnc
  - relation_type: prov:wasDerivedFrom
    source: hippie
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: iid
  - relation_type: prov:wasDerivedFrom
    source: iptmnet
  - relation_type: prov:wasDerivedFrom
    source: markerdb
  - relation_type: prov:wasDerivedFrom
    source: med-rt
  - relation_type: prov:wasDerivedFrom
    source: mirbase
  - relation_type: prov:wasDerivedFrom
    source: mondo
  - relation_type: prov:wasDerivedFrom
    source: ncbigene
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: ptmd
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: qptm
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: refseq
  - relation_type: prov:wasDerivedFrom
    source: rnadisease
  - relation_type: prov:wasDerivedFrom
    source: rnainter
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: smpdb
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: Product
  description: Bulk download of DisProt data in multiple formats including JSON, TSV,
    FASTA, and GAF
  format: json
  id: disprot.downloads
  name: DisProt Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: disprot
  product_url: https://www.disprot.org/download
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: uniprot
  - relation_type: prov:wasInformedBy
    source: interpro
  - relation_type: prov:wasInformedBy
    source: go
  - relation_type: prov:wasInformedBy
    source: eco
- category: OntologyProduct
  description: IDP Ontology (IDPO) for representing functional aspects of intrinsically
    disordered proteins
  format: owl
  id: disprot.idpo
  name: IDP Ontology (IDPO)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: disprot
  product_file_size: 50945
  product_url: https://www.disprot.org/assets/data/IDPO_v0.3.0.owl
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: go
  - relation_type: prov:wasInformedBy
    source: eco
- category: GraphProduct
  compression: gzip
  description: HumanNet-XC v3 functional gene network extended by co-citation, distributed
    with Entrez Gene identifiers.
  edge_count: 1125494
  format: tsv
  id: humannet.network
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Network File
  node_count: 18462
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_file_size: 12310221
  product_url: https://www.inetbio.org/humannetv3/networks/HumanNet-XC.tsv.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: metacyc
  - relation_type: prov:wasDerivedFrom
    source: reactome
- category: GraphProduct
  compression: gzip
  description: HumanNet-XC v3 functional gene network extended by co-citation, distributed
    with gene symbols.
  edge_count: 1125494
  format: tsv
  id: humannet.network.symbol
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Network File (Gene Symbols)
  node_count: 18462
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_file_size: 13925784
  product_url: https://www.inetbio.org/humannetv3/networks/HumanNet-XC.symbol.tsv.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: metacyc
  - relation_type: prov:wasDerivedFrom
    source: reactome
- category: GraphProduct
  description: GP-KG tab-delimited knowledge graph containing 1,246,726 associations
    between 61,146 entities from multiple genotypic and phenotypic databases
  format: tsv
  id: kg-predict.gpkg
  name: GP-KG Knowledge Graph Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 48397035
  product_url: http://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: string
  - relation_type: prov:wasDerivedFrom
    source: umls
- category: Product
  description: Downloadable gene set files in GMT, XML, and other formats for human
    collections including hallmarks, curated pathways, ontologies, and computational
    signatures; free registration is required for downloads
  format: mixed
  id: msigdb.downloads.human
  name: MSigDB Human Gene Sets Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
  secondary_source:
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mirbase
  - relation_type: prov:used
    source: pid
  - relation_type: prov:used
    source: reactome
  - relation_type: prov:used
    source: wikipathways
  warnings:
  - Downloads redirect unauthenticated users to the GSEA/MSigDB login page; registration
    is free but required for direct file access.
- category: Product
  description: Downloadable gene set files for mouse collections including mouse-ortholog
    hallmarks, curated pathways, ontologies, and cell type signatures; free registration
    is required for downloads
  format: mixed
  id: msigdb.downloads.mouse
  name: MSigDB Mouse Gene Sets Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: msigdb
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
  secondary_source:
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mirbase
  - relation_type: prov:used
    source: pid
  - relation_type: prov:used
    source: reactome
  - relation_type: prov:used
    source: wikipathways
  warnings:
  - Downloads redirect unauthenticated users to the GSEA/MSigDB login page; registration
    is free but required for direct file access.
- category: ProgrammingInterface
  description: TRAPI 1.4 API for predicted drug treatments, drug-disease associations,
    similar entities, model metadata, and explanation endpoints
  format: http
  id: openpredict.api
  name: OpenPredict API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openpredict
  product_url: https://openpredict.semanticscience.org/docs
  secondary_source:
  - relation_type: prov:used
    source: biolink
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: omim
- category: Product
  description: Pre-computed prediction outputs exposed through API operations for
    predicted drugs, predicted diseases, similar entities, and evidence paths
  format: mixed
  id: openpredict.predictions
  name: OpenPredict Prediction Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openpredict
  product_url: https://openpredict.semanticscience.org/docs
  secondary_source:
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:used
    source: go
  - relation_type: prov:used
    source: hp
  - relation_type: prov:used
    source: kegg
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: omim
  warnings:
  - Prediction results are exposed through POST/GET API operations rather than as
    a stable public bulk data file.
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
- category: OntologyProduct
  description: Classes added to ncbitaxon for groupings such as prokaryotes
  format: owl
  id: go.extensions.go-taxon-groupings.owl
  name: GO Taxon Groupings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
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
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.2.1
  compression: gzip
  description: Human-scoped, Neo4j-ready subgraph of the BioBTree knowledge graph,
    exported as a biolink-typed KGX graph (~40M nodes / ~132M edges, ~8.3 GB compressed
    across separate node and edge files). A practical projection of the full graph
    for human-centric biomedical use. Published on Zenodo.
  edge_count: 132075627
  format: kgx
  id: biobtree.graph.human-subgraph
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC-BY-NC-SA-4.0
  name: BioBTree Knowledge Graph - Human Subgraph (KGX)
  node_categories:
  - biolink:BiologicalProcess
  - biolink:Cell
  - biolink:CellLine
  - biolink:CellularComponent
  - biolink:CodingSequence
  - biolink:Disease
  - biolink:DiseaseOrPhenotypicFeature
  - biolink:Drug
  - biolink:Exon
  - biolink:Gene
  - biolink:GrossAnatomicalStructure
  - biolink:MacromolecularComplex
  - biolink:MolecularActivity
  - biolink:NoncodingRNAProduct
  - biolink:NucleicAcidSequenceMotif
  - biolink:OrganismTaxon
  - biolink:Pathway
  - biolink:PhenotypicFeature
  - biolink:Protein
  - biolink:ProteinDomain
  - biolink:ProteinFamily
  - biolink:Publication
  - biolink:RegulatoryRegion
  - biolink:SequenceVariant
  - biolink:SmallMolecule
  - biolink:Transcript
  node_count: 40160474
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  predicates:
  - biolink:actively_involved_in
  - biolink:affects
  - biolink:associated_with
  - biolink:close_match
  - biolink:derives_from
  - biolink:directly_physically_interacts_with
  - biolink:enables
  - biolink:expressed_in
  - biolink:gene_associated_with_condition
  - biolink:gene_product_of
  - biolink:has_adverse_event
  - biolink:has_gene_product
  - biolink:has_part
  - biolink:has_participant
  - biolink:has_phenotype
  - biolink:in_clinical_trials_for
  - biolink:in_taxon
  - biolink:interacts_with
  - biolink:is_sequence_variant_of
  - biolink:located_in
  - biolink:member_of
  - biolink:mentions
  - biolink:orthologous_to
  - biolink:paralogous_to
  - biolink:participates_in
  - biolink:physically_interacts_with
  - biolink:related_to
  - biolink:same_as
  - biolink:subclass_of
  - biolink:transcribed_from
  - biolink:translates_to
  - biolink:treats_or_applied_or_studied_to_treat
  product_url: https://zenodo.org/records/20816742
- category: GraphProduct
  compression: tar
  description: Knowledge graph containing plant traits data from Planteome and EOL
    TraitBank
  format: kgx
  id: eco-kg.graph
  name: eco-KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eco-kg
  - relation_type: prov:hadPrimarySource
    source: eol-traitbank
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: maizegdb
  - relation_type: prov:hadPrimarySource
    source: planteome
  - relation_type: prov:hadPrimarySource
    source: rapdb
  product_url: https://github.com/Knowledge-Graph-Hub/eco-kg
- category: GraphProduct
  description: GenomicKB 1.0 Neo4j Database Dump (Requires license)
  dump_format: neo4j
  format: http
  id: genomickb.graph
  name: GenomicKB Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genomickb
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: endb
  - relation_type: prov:hadPrimarySource
    source: enhanceratlas
  - relation_type: prov:hadPrimarySource
    source: ccre
  - relation_type: prov:hadPrimarySource
    source: fire
  - relation_type: prov:hadPrimarySource
    source: motifmap
  product_url: https://available-inventions.umich.edu/product/genomickb-a-knowledgebase-for-the-human-genome
- category: GraphProduct
  description: GP_KG.txt
  edge_count: 1246726
  format: txt
  id: gp-kg.graph
  name: GP-KG
  node_count: 61146
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gp-kg
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: goa
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: phenomebrowser
  - relation_type: prov:wasDerivedFrom
    source: treatkb
  product_file_size: 48397035
  product_url: http://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
- category: GraphProduct
  description: KGX nodes and edges for KG-COVID-19
  format: kgx
  id: kg-covid-19.graph
  name: KG-COVID-19 graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-covid-19
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cord-19
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://kghub.io/kg-covid-19/
  warnings:
  - 'Download offline as of 2026-07-01: the KG-Hub reorganization has taken this file
    offline. The kghub.io and kg-hub.berkeleybop.io hosts return HTTP 404 for all
    kg-covid-19 artifacts (current and dated) and the kg-hub-public-data S3 objects
    return HTTP 403. No replacement public download URL is available.'
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: KGX Distribution of KG-IDG
  format: kgx
  id: kg-idg.graph
  name: KGX Distribution of KG-IDG
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-idg
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://kg-hub.berkeleybop.io/kg-idg/current/kg-idg.tar.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-01: HTTP 404 error.
    The kg-hub.berkeleybop.io host is being reorganized and KG-IDG downloads are pending
    relocation to a new home; no live download is currently available.'
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: Merged KG with ontology-grounded KG and literature-based graph as TSV
    file
  format: tsv
  id: np-kg.graph.tsv
  name: NP-KG TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: np-kg
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: dideo
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: indra
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: oae
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semrep
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1074149258
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.tsv?download=1
- category: GraphProduct
  description: Merged KG with ontology-grounded KG and literature-based graph as NetworkX
    multidigraph object
  dump_format: gpickle
  format: mixed
  id: np-kg.graph.networkx
  name: NP-KG gpickle
  original_source:
  - relation_type: prov:hadPrimarySource
    source: np-kg
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: dideo
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: indra
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: oae
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: semrep
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 936065236
  product_url: https://zenodo.org/records/12536780/files/NP-KG_v3.0.0.gpickle?download=1
- category: GraphProduct
  description: The full PrimeKG dataset containing disease relationships.
  format: csv
  id: primekg.graph
  name: PrimeKG Full Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: primekg
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://dataverse.harvard.edu/api/access/datafile/6180620
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-04_ Timeout connecting
    to URL
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
- category: GraphProduct
  description: Integrated rare-disease knowledge graph produced by the RD-Clust workflow,
    connecting rare diseases to genes, phenotypes, Gene Ontology terms, drugs/ligands,
    and pathway interactions. Distributed as the processed disease ontograph within
    the RD-Clust repository.
  format: http
  id: ncatsgardkg.graph
  name: NCATS GARD Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncatsgardkg
  - relation_type: prov:hadPrimarySource
    source: gard
  product_url: https://github.com/ncats/RD-Clust/tree/main/data/processed
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hp
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: mondo
  - relation_type: prov:wasInfluencedBy
    source: orphanet
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: pharos
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: chebi
  - relation_type: prov:wasInfluencedBy
    source: pubchem
  - relation_type: prov:wasInfluencedBy
    source: pathwaycommons
- category: GraphProduct
  description: The SPOKE-OKN knowledge graph, an OKN-hosted RDF publication of the
    SPOKE biomedical and environmental health knowledge graph, served through FRINK
    query services.
  format: ttl
  id: spoke-okn.graph
  name: SPOKE-OKN Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke-okn
  - relation_type: prov:wasDerivedFrom
    source: spoke
  product_url: https://spoke.ucsf.edu
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bgee
  - relation_type: prov:wasInfluencedBy
    source: bindingdb
  - relation_type: prov:wasInfluencedBy
    source: bv-brc
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: civic
  - relation_type: prov:wasInfluencedBy
    source: cl
  - relation_type: prov:wasInfluencedBy
    source: clinicaltrialsgov
  - relation_type: prov:wasInfluencedBy
    source: diseases
  - relation_type: prov:wasInfluencedBy
    source: doid
  - relation_type: prov:wasInfluencedBy
    source: drugbank
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: foodb
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: gwascatalog
  - relation_type: prov:wasInfluencedBy
    source: hpa
  - relation_type: prov:wasInfluencedBy
    source: interpro
  - relation_type: prov:wasInfluencedBy
    source: kegg
  - relation_type: prov:wasInfluencedBy
    source: lincs-l1000
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: metacyc
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: ncbitaxon
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pathophenodb
  - relation_type: prov:wasInfluencedBy
    source: pfam
  - relation_type: prov:wasInfluencedBy
    source: pid
  - relation_type: prov:wasInfluencedBy
    source: protcid
  - relation_type: prov:wasInfluencedBy
    source: pubmed
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: sider
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: uberon
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
publications:
- authors:
  - Ashburner M
  - Ball CA
  - Blake JA
  - Botstein D
  - Butler H
  - Cherry JM
  - Davis AP
  - Dolinski K
  - Dwight SS
  - Eppig JT
  - Harris MA
  - Hill DP
  - Issel-Tarver L
  - Kasarskis A
  - Lewis S
  - Matese JC
  - Richardson JE
  - Ringwald M
  - Rubin GM
  - Sherlock G
  doi: 10.1038/75556
  id: https://www.ncbi.nlm.nih.gov/pubmed/10802651
  journal: Nat Genet
  title: 'Gene ontology: tool for the unification of biology. The Gene Ontology Consortium'
  year: '2000'
- authors:
  - Gene Ontology Consortium
  doi: 10.1093/nar/gkaa1113
  id: https://www.ncbi.nlm.nih.gov/pubmed/33290552
  journal: Nucleic Acids Res
  title: 'The Gene Ontology resource: enriching a GOld mine'
  year: '2021'
repository: https://github.com/geneontology/go-ontology
synonyms:
- GO
taxon:
- NCBITaxon:1
---
## Overview

The Gene Ontology (GO) is a consortium-maintained ontology and knowledge resource for describing gene product function across species. It organizes biology into molecular function, biological process, and cellular component terms, and supports a large ecosystem of annotation, browsing, download, and programmatic access services.

## Scope

This page focuses on official GO products: ontology releases, GO Consortium browsers and APIs, GO annotation download surfaces, and GO-CAM causal activity model distributions. It does not enumerate downstream third-party knowledge graphs that merely ingest GO.

## Access

Use AmiGO and QuickGO for browsing, the GO API for programmatic access, OBO PURLs for ontology files, and the GOA / current release download directories for annotation and GO-CAM artifacts.

---

*This resource was automatically synchronized from the OBO Foundry registry and then curated with additional GO Consortium access points.*