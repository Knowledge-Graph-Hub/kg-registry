---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@bioontology.org
  - contact_type: url
    value: https://www.bioontology.org/
  label: National Center for Biomedical Ontology (NCBO), Stanford
creation_date: '2025-08-20T00:00:00Z'
description: BioPortal is a comprehensive open repository and portal for biomedical
  ontologies and terminologies, providing search, browsing, mappings, versioned downloads,
  REST APIs, widgets, and analytics to support data integration, annotation, and semantic
  interoperability in the life and health sciences. As of 2025 it hosted 1,549 ontologies
  (1,182 public), including all OBO Foundry ontologies, which it pulls automatically,
  and selected UMLS vocabularies.
domains:
- biomedical
- clinical
- information technology
- general
homepage_url: https://bioportal.bioontology.org/
id: bioportal
infores_id: bioportal
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.bioontology.org/terms/
  label: BioPortal Terms of Use (individual ontologies carry their own licenses)
name: BioPortal
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing biomedical ontologies
    and mappings
  format: http
  id: bioportal.portal
  name: BioPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: obofoundry
  product_url: https://bioportal.bioontology.org/
- category: ProgrammingInterface
  description: REST API for ontology concepts, search, mappings, metrics, and downloads.
    Most endpoints require a free BioPortal API key.
  format: http
  id: bioportal.api
  name: BioPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: obofoundry
  product_url: https://data.bioontology.org/
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
  description: RDF/XML serialization of the eKG epidemiological knowledge graph
  format: rdfxml
  id: ekg.rdf
  name: eKG RDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_file_size: 3853565
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/ETOHA-OPEN/epidemicIE-DONs.rdf
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: GraphProduct
  description: Turtle serialization of the eKG epidemiological knowledge graph
  format: ttl
  id: ekg.ttl
  name: eKG TTL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_file_size: 3874916
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/ETOHA-OPEN/epidemicIE-DONs.ttl
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: ProgrammingInterface
  connection_url: https://data.jrc.ec.europa.eu/yasgui
  description: SPARQL query interface for eKG via the JRC Data Catalogue YASGUI (the
    former dedicated endpoint at api-vast.jrc.service.ec.europa.eu/sparql/ has been
    retired)
  format: http
  id: ekg.sparql
  name: eKG SPARQL endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_url: https://data.jrc.ec.europa.eu/yasgui
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: GraphicalInterface
  description: JRC Data Catalogue dataset landing page for browsing and downloading
    eKG (the former Virtuoso faceted browser at api-vast.jrc.service.ec.europa.eu/fct/
    has been retired)
  format: http
  id: ekg.browser
  name: eKG Data Catalogue Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_url: https://data.jrc.ec.europa.eu/dataset/89056048-7f5d-4d7c-96ad-f99d1c0f6601
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
  - relation_type: prov:wasInformedBy
    source: bioportal
  - relation_type: prov:wasInformedBy
    source: geonames
- category: GraphicalInterface
  description: NCBO BioPortal entry for browsing and exploring the GlycoCoO ontology
  format: http
  id: glycocoo.bioportal
  name: GlycoCoO BioPortal Entry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  product_url: https://bioportal.bioontology.org/ontologies/GLYCOCOO
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: GraphicalInterface
  description: NCBO BioPortal entry for browsing and exploring the GlycoRDF ontology
  format: http
  id: glycordf.bioportal
  name: GlycoRDF BioPortal Entry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: glycordf
  product_url: https://bioportal.bioontology.org/ontologies/GLYCORDF
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: GraphicalInterface
  description: Browsable listing of every KG-Bioportal graph, with node and edge counts,
    transform status, and a download link for each. This is the canonical index of
    the transforms; KG-Registry does not mirror the full inventory.
  format: http
  id: kg-bioportal.browser
  name: KG-Bioportal Graph Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-bioportal
  product_url: https://ncbo.github.io/kg-bioportal/graphs/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: bioportal
- category: Product
  description: Manifest of every transform attempt, giving the BioPortal acronym,
    status, node and edge counts, source submission, and release download URL for
    each ontology. Refreshed with each monthly transform run.
  format: yaml
  id: kg-bioportal.manifest
  name: KG-Bioportal Transform Manifest
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-bioportal
  product_file_size: 341106
  product_url: https://github.com/ncbo/kg-bioportal/releases/latest/download/onto_stats.yaml
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: bioportal
- category: GraphProduct
  compression: targz
  description: KGX TSV graphs for all successfully transformed BioPortal ontologies,
    published as one gzipped tar archive per ontology on the latest release. Individual
    archives are at https://github.com/ncbo/kg-bioportal/releases/latest/download/<ACRONYM>.tar.gz
    and contain <ACRONYM>_nodes.tsv and <ACRONYM>_edges.tsv.
  format: kgx
  id: kg-bioportal.graphs
  latest_version: latest
  name: KG-Bioportal KGX Graphs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-bioportal
  product_url: https://github.com/ncbo/kg-bioportal/releases/latest
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: bioportal
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including
    names, synonyms, URI formats, local identifier patterns, providers and mappings
    to the prefixes of other registries.
  format: json
  id: bioregistry.registry.json
  name: Bioregistry JSON Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes
    in other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology
    registry, Cellosaurus, UniProt and NCBI.
  format: sssom
  id: bioregistry.sssom
  name: Bioregistry SSSOM Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing agri-food ontologies and
    semantic artefacts, their metadata, FAIRness scores, and mappings. The former address
    https://agroportal.lirmm.fr/ redirects here.
  format: http
  id: agroportal.portal
  name: AgroPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://agroportal.eu/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: ProgrammingInterface
  description: REST API for ontologies, classes, search, mappings, metrics, annotation, and
    downloads of hosted semantic artefacts. Requests require a free API key, obtained by creating
    an AgroPortal account. The former address https://data.agroportal.lirmm.fr/ redirects
    here.
  format: http
  id: agroportal.api
  name: AgroPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://data.agroportal.eu/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: GraphicalInterface
  description: Annotator service that tags free text with terms from AgroPortal ontologies.
  format: http
  id: agroportal.annotator
  name: AgroPortal Annotator
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://agroportal.eu/annotator
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: DocumentationProduct
  description: Documentation for the OntoPortal software that AgroPortal runs on, covering
    installation, administration, and use of OntoPortal-based portals.
  format: http
  id: agroportal.ontoportal-docs
  name: OntoPortal Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agroportal
  product_url: https://ontoportal.github.io/documentation/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: GraphicalInterface
  description: Web portal for searching and browsing the AberOWL ontology repository, viewing
    class hierarchies and metadata, and running DL and SPARQL-rewriting queries.
  format: http
  id: aberowl.portal
  is_public: true
  name: AberOWL Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: https://aber-owl.net/
- category: ProgrammingInterface
  description: REST API (FastAPI, documented with Swagger UI) for listing ontologies, retrieving
    classes, full-text search and DL queries (subclass, superclass, equivalent) across the
    AberOWL repository.
  format: http
  id: aberowl.api
  is_public: true
  name: AberOWL REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: https://aber-owl.net/api/docs
  warnings:
  - When checked on 2026-10-04, listing, search and statistics endpoints responded, but DL
    query endpoints (/api/dlquery, /api/dlquery_all) returned "API server is down!".
- category: Product
  description: JSON listing of all ontologies in AberOWL with metadata, reasoner status, class
    counts and relative download URLs for the mirrored OWL files.
  format: json
  id: aberowl.ontology-list
  is_public: true
  name: AberOWL Ontology Listing
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: https://aber-owl.net/api/listOntologies
- category: GraphicalInterface
  description: Web portal for searching, browsing and visualizing ecological ontologies, thesauri
    and their mappings, with ontology recommender, text annotator and submission of new semantic
    artefacts.
  format: http
  id: ecoportal.portal
  name: EcoPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecoportal
  product_url: https://ecoportal.lifewatch.eu/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: ProgrammingInterface
  description: OntoPortal REST API for EcoPortal ontologies, classes, search, mappings, metrics,
    annotation and downloads. Requests require an API key, available free with an EcoPortal
    account.
  format: http
  id: ecoportal.api
  name: EcoPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecoportal
  product_url: https://data.ecoportal.lifewatch.eu/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: GraphicalInterface
  description: NCBO BioPortal entry for browsing and searching ECSO
  format: http
  id: ecso.bioportal
  name: ECSO BioPortal Entry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecso
  product_url: https://bioportal.bioontology.org/ontologies/ECSO
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  warnings:
  - Page returned HTTP 403 to automated requests when checked on 2026-10-05. The BioPortal
    REST API still lists the ontology.
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing French biomedical ontologies
    and terminologies and the mappings between them, with recommender and landscape views.
  format: http
  id: sifr-bioportal.portal
  name: SIFR BioPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sifr-bioportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://bioportal.lirmm.fr/
- category: ProgrammingInterface
  description: OntoPortal REST API for ontologies, classes, search, mappings, metrics, submissions,
    and the annotator. Endpoints require a free SIFR BioPortal API key.
  format: http
  id: sifr-bioportal.api
  name: SIFR BioPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sifr-bioportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://data.bioportal.lirmm.fr/
- category: ProcessProduct
  description: SIFR Annotator, a semantic annotation service for French biomedical text and
    clinical notes that tags text with concepts from the ontologies hosted in SIFR BioPortal.
    It ports the NCBO Annotator to French, adding lemmatization, negation, experiencer and
    temporality detection, and scoring. Available as a web form and through the REST API (/annotator,
    API key required).
  format: http
  id: sifr-bioportal.annotator
  name: SIFR Annotator
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sifr-bioportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://bioportal.lirmm.fr/annotator
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing biodiversity ontologies
    and semantic artefacts, with mappings, a recommender, and a landscape view of the catalogue.
  format: http
  id: biodivportal.portal
  name: BiodivPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodivportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://biodivportal.gfbio.org/
- category: ProgrammingInterface
  description: OntoPortal REST API for artefact metadata, concepts, search, mappings, annotation,
    recommendation, and downloads. Requests require a BiodivPortal API key, available with
    a free account.
  format: http
  id: biodivportal.api
  name: BiodivPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biodivportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://data.biodivportal.gfbio.org/
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing Earth and environmental
    science ontologies and semantic artefacts, with mappings, a recommender, and a landscape
    view of the catalogue.
  format: http
  id: earthportal.portal
  name: EarthPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: earthportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://earthportal.eu/
- category: ProgrammingInterface
  description: OntoPortal REST API for artefact metadata, concepts, search, mappings, annotation,
    and downloads. Requests require an EarthPortal API key, available with a free account.
  format: http
  id: earthportal.api
  name: EarthPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: earthportal
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://data.earthportal.eu/
- category: GraphicalInterface
  description: BioPortal page for OBOE (acronym OBOE), providing browsing, search, and download
    of the ontology. The latest submission is version 1.2, released 2019-09-17.
  format: http
  id: oboe.bioportal
  name: OBOE on BioPortal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oboe
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://bioportal.bioontology.org/ontologies/OBOE
publications:
- authors:
  - Jennifer Vendetti
  - Nomi L Harris
  - Michael V Dorf
  - Alex Skrenchuk
  - J Harry Caufield
  - Rafael S Gonçalves
  - John B Graybeal
  - Harshad Hegde
  - Timothy Redmond
  - Christopher J Mungall
  - Mark A Musen
  doi: 10.1093/nar/gkaf402
  id: doi:10.1093/nar/gkaf402
  journal: Nucleic Acids Research
  title: 'BioPortal: an open community resource for sharing, searching, and utilizing
    biomedical ontologies'
  year: '2025'
- doi: 10.1093/nar/gkr469
  id: doi:10.1093/nar/gkr469
  journal: Nucleic Acids Research
  title: 'BioPortal: enhanced functionality via new Web services from the National
    Center for Biomedical Ontology to access and use ontologies in software applications'
  year: '2011'
- doi: 10.1093/nar/gkp440
  id: doi:10.1093/nar/gkp440
  journal: Nucleic Acids Research
  title: 'BioPortal: ontologies and integrated data resources at the click of a mouse'
  year: '2009'
repository: https://github.com/ncbo
warnings:
- Some ontologies have distinct licenses; review individual ontology license metadata
  before reuse.
---
# BioPortal

BioPortal hosts over a thousand biomedical ontologies with search, mappings, visualization, downloads, and programmatic access.