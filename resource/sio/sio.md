---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: sio-ontology@googlegroups.com
  - contact_type: url
    value: https://semanticscience.org/
  label: Semanticscience
creation_date: '2026-06-02T00:00:00Z'
description: The Semanticscience Integrated Ontology (SIO) is an ontology of basic
  types and relations for representing physical, processual, and informational entities
  and supporting biomedical knowledge representation and discovery.
domains:
- biomedical
- biological systems
- information technology
homepage_url: https://semanticscience.org/
id: sio
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Semanticscience Integrated Ontology
products:
- category: OntologyProduct
  description: OWL release of the Semanticscience Integrated Ontology.
  format: owl
  id: sio.owl
  name: SIO OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sio
  product_file_size: 189217
  product_url: https://semanticscience.org/ontology/sio.owl
- category: GraphicalInterface
  description: BioPortal browser page for the Semanticscience Integrated Ontology.
  format: http
  id: sio.bioportal
  name: SIO BioPortal Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sio
  product_url: https://bioportal.bioontology.org/ontologies/SIO
- category: GraphProduct
  description: RDF knowledge graph materialized by the MetaBoKG workflow from public
    metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence,
    sample metadata, and environmental and taxonomic context. The repository documents
    generated per-job Turtle files under mapping/kg and loading into Virtuoso named
    graphs.
  format: mixed
  id: metabokg.graph
  latest_version: arXiv v1 demonstration
  name: MetaboKG RDF Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubmedcentral
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: redu
  product_url: https://github.com/HolobiomicsLab/MetaBoKG
  secondary_source:
  - relation_type: prov:used
    source: ms
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
  - relation_type: prov:used
    source: envo
  - relation_type: prov:used
    source: ncit
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: chmo
  - relation_type: prov:used
    source: sio
  - relation_type: prov:used
    source: prov-o
  - relation_type: prov:used
    source: dcat
  - relation_type: prov:used
    source: afo
  warnings:
  - No static public graph release or hosted endpoint was available in the GitHub
    repository when curated on 2026-06-02; the repository documents local Turtle materialization
    and Virtuoso loading.
- category: DataModelProduct
  description: Turtle schema files defining MetaBoKG classes, properties, and ReDU
    class hierarchies used by the generated knowledge graph.
  format: ttl
  id: metabokg.schema
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache License 2.0
  name: MetaBoKG RDF Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabokg
  product_url: https://github.com/HolobiomicsLab/MetaBoKG/tree/main/Schema
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: ms
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: envo
  - relation_type: prov:wasInformedBy
    source: ncit
  - relation_type: prov:wasInformedBy
    source: uberon
  - relation_type: prov:wasInformedBy
    source: chmo
  - relation_type: prov:wasInformedBy
    source: sio
  - relation_type: prov:wasInformedBy
    source: prov-o
  - relation_type: prov:wasInformedBy
    source: dcat
  - relation_type: prov:wasInformedBy
    source: afo
publications:
- authors:
  - Michel Dumontier
  - Christopher J Baker
  - Joachim Baran
  - Alison Callahan
  - Lap Chang
  - Leyla Chepelev
  - Jose Cruz-Toledo
  - Nicholas R Del Rio
  - Geraint Duck
  - Luke I Furlong
  doi: 10.1186/2041-1480-5-14
  id: doi:10.1186/2041-1480-5-14
  journal: Journal of Biomedical Semantics
  preferred: true
  title: The Semanticscience Integrated Ontology (SIO) for biomedical research and
    knowledge discovery
  year: '2014'
repository: https://github.com/micheldumontier/semanticscience
synonyms:
- SIO
---
# Semanticscience Integrated Ontology

SIO provides upper-level classes and relations for consistent knowledge representation across biomedical and semantic-web resources.