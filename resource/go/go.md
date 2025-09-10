---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@geneontology.org
  label: Gene Ontology Helpdesk
description: "The Gene Ontology resource, the world\u2019s largest source of information\
  \ on the functions of genes. This knowledge is both human-readable and machine-readable,\
  \ and is a foundation for computational analysis of large-scale molecular biology\
  \ and genetics experiments in biomedical research."
domains:
- biological systems
homepage_url: https://geneontology.org/
id: go
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Gene Ontology
products:
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
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
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
  - do
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
- category: DataModelProduct
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
  - do
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
- category: DataModelProduct
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
  - do
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
- category: DataModelProduct
  description: The latest release of Plant Trait Ontology in OWL format
  format: owl
  id: to.owl
  latest_version: v2025-05-20
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Plant Trait Ontology OWL
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
  product_file_size: 212124
  product_url: http://purl.obolibrary.org/obo/to.owl
  secondary_source:
  - to
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
- category: DataModelProduct
  description: The latest release of Plant Trait Ontology in OBO format
  format: obo
  id: to.obo
  latest_version: v2025-05-20
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Plant Trait Ontology OBO
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
  product_file_size: 158383
  product_url: http://purl.obolibrary.org/obo/to.obo
  secondary_source:
  - to
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
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
- description: The MechRepoNet knowledge graph in its original format
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - ctd
  - do
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
  - do
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
  compatibility:
  - standard: biolink
  compression: zip
  description: "Curated mechanistic drug\u2013disease paths comprising the DrugMechDB\
    \ dataset packaged as a downloadable archive."
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
- category: DataModelProduct
  description: PW OWL release
  format: owl
  id: pw.owl
  name: PW OWL
  original_source:
  - pw
  - iao
  - go
  product_file_size: 5403526
  product_url: http://purl.obolibrary.org/obo/pw.owl
  secondary_source:
  - pw
- category: DataModelProduct
  description: PW OBO release
  format: obo
  id: pw.obo
  name: PW OBO
  original_source:
  - pw
  - iao
  - go
  product_file_size: 1347302
  product_url: http://purl.obolibrary.org/obo/pw.obo
  secondary_source:
  - pw
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
- category: DataModelProduct
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
  id: doi:10.1038/75556
  title: 'Gene ontology: tool for the unification of biology'
  year: '2000'
- authors:
  - The Gene Ontology Consortium
  - Aleksander SA
  - Balhoff J
  - Carbon S
  - Cherry JM
  - Drabkin HJ
  - Ebert D
  - Feuermann M
  - Gaudet P
  - Harris NL
  - Hill DP
  - Lee R
  - Mi H
  - Moxon S
  - Mungall CJ
  - Muruganugan A
  - Mushayahama T
  - Sternberg PW
  - Thomas PD
  - Van Auken K
  - Ramsey J
  - Siegele DA
  - Chisholm RL
  - Fey P
  - Aspromonte MC
  - Nugnes MV
  - Quaglia F
  - Tosatto S
  - Giglio M
  - Nadendla S
  - Antonazzo G
  - Attrill H
  - dos Santos G
  - Marygold SJ
  - Strelets V
  - Tabone CJ
  - Thurmond J
  - Zhou P
  - Ahmed SH
  - Asanitthong P
  - Buitrago DL
  - Erdol MN
  - Gage MC
  - Kadhum MA
  - Li KYC
  - Long M
  - Michalak A
  - Pesala A
  - Pritazahra A
  - Saverimuttu SCC
  - Su R
  - Thurlow KE
  - Lovering RC
  - Logie C
  - Oliferenko S
  - Blake J
  - Christie K
  - Corbani L
  - Dolan ME
  - Drabkin HJ
  - Hill DP
  - Ni L
  - Sitnikov D
  - Smith C
  - Cuzick A
  - Seager J
  - Cooper L
  - Elser J
  - Jaiswal P
  - Gupta P
  - Jaiswal P
  - Naithani S
  - Lera-Ramirez M
  - Rutherford K
  - Wood V
  - De Pons JL
  - Dwinell MR
  - Hayman GT
  - Kaldunski ML
  - Kwitek AE
  - Laulederkind SJF
  - Tutaj MA
  - Vedi M
  - Wang S-J
  - "D\u2019Eustachio PD"
  - Aimo L
  - Axelsen K
  - Bridge A
  - Hyka-Nouspikel N
  - Morgat A
  - Aleksander SA
  - Cherry JM
  - Engel SR
  - Karra K
  - Miyasato SR
  - Nash RS
  - Skrzypek MS
  - Weng S
  - Wong ED
  - Bakker E
  - Berardini TZ
  - Reiser L
  - Auchincloss A
  - Axelsen K
  - Argoud-Puy G
  - Blatter M-C
  - Boutet E
  - Breuza L
  - Bridge A
  - Casals-Casas C
  - Coudert E
  - Estreicher A
  - Famiglietti ML
  - Feuermann M
  - Gos A
  - Gruaz-Gumowski N
  - Hulo C
  - Hyka-Nouspikel N
  - Jungo F
  - Le Mercier P
  - Lieberherr D
  - Masson P
  - Morgat A
  - Pedruzzi I
  - Pourcel L
  - Poux S
  - Rivoire C
  - Sundaram S
  - Bateman A
  - Bowler-Barnett E
  - Bye-A-Jee H
  - Denny P
  - Ignatchenko A
  - Ishtiaq R
  - Lock A
  - Lussi Y
  - Magrane M
  - Martin MJ
  - Orchard S
  - Raposo P
  - Speretta E
  - Tyagi N
  - Warner K
  - Zaru R
  - Diehl AD
  - Lee R
  - Chan J
  - Diamantakis S
  - Raciti D
  - Zarowiecki M
  - Fisher M
  - James-Zorn C
  - Ponferrada V
  - Zorn A
  - Ramachandran S
  - Ruzicka L
  - Westerfield M
  doi: 10.1093/genetics/iyad031
  id: doi:10.1093/genetics/iyad031
  title: The Gene Ontology knowledgebase in 2023
  year: '2023'
repository: https://github.com/geneontology
---
Gene Ontology