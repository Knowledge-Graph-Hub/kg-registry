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
  interoperability in the life and health sciences.
domains:
- biomedical
- clinical
- information technology
- general
homepage_url: https://bioportal.bioontology.org/
id: bioportal
infores_id: bioportal
last_modified_date: '2025-09-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.bioontology.org/terms/
  label: BioPortal Terms of Use (includes attribution & reuse conditions)
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
  product_url: https://bioportal.bioontology.org/
- category: ProgrammingInterface
  description: REST API for ontology concepts, search, mappings, metrics, and downloads
  format: http
  id: bioportal.api
  name: BioPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: http://data.bioontology.org/
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
publications:
- authors:
  - Jennifer Vendetti
  - "Nomi\_L Harris"
  - "Michael\_V Dorf"
  - Alex Skrenchuk
  - "J\_Harry Caufield"
  - "Rafael\_S Gon\xE7alves"
  - "John\_B Graybeal"
  - Harshad Hegde
  - Timothy Redmond
  - "Christopher\_J Mungall"
  - "Mark\_A Musen"
  doi: 10.1093/nar/gkaf402
  id: doi:10.1093/nar/gkaf402
  journal: Nucleic Acids Research
  title: 'BioPortal: an open community resource for sharing, searching, and utilizing
    biomedical ontologies'
  year: '2025'
taxon:
- NCBITaxon:9606
warnings:
- Some ontologies have distinct licenses; review individual ontology license metadata
  before reuse.
repository: https://github.com/ncbo
---
# BioPortal

BioPortal hosts over a thousand biomedical ontologies with search, mappings, visualization, downloads, and programmatic access.