---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.who.int/
  label: World Health Organization
creation_date: '2026-06-02T00:00:00Z'
description: The World Health Organization (WHO) is a United Nations specialized agency
  for international public health that publishes global health statistics, classifications,
  guidance, disease outbreak reports, and emergency information products.
domains:
- public health
- biomedical
- clinical
homepage_url: https://www.who.int/
id: who
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/3.0/igo/
  label: CC BY-NC-SA 3.0 IGO
name: World Health Organization
products:
- category: GraphicalInterface
  description: WHO public website for global health information, public health guidance,
    emergencies, publications, campaigns, news, and country information.
  format: http
  id: who.portal
  name: WHO Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/
- category: GraphicalInterface
  description: WHO Data Platform landing page linking WHO data portals including the
    Global Health Observatory, immunization data, GLAAS, NCD data, SRHR policy data,
    and other health data sites.
  format: http
  id: who.data-platform
  name: WHO Data Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://platform.who.int/data
- category: GraphicalInterface
  description: WHO Global Health Observatory portal for browsing global health data
    by indicators, countries, themes, featured datasets, dashboards, and publications.
  format: http
  id: who.gho
  name: WHO Global Health Observatory
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/data/gho
- category: ProgrammingInterface
  connection_url: https://ghoapi.azureedge.net/api/
  description: WHO Global Health Observatory OData API for querying WHO statistics
    and indicator data through the OData protocol.
  format: http
  id: who.gho-odata-api
  is_public: true
  name: WHO GHO OData API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/data/gho/info/gho-odata-api
- category: GraphicalInterface
  description: WHO Data hub (data.who.int), WHO's newer home for health data, with
    indicator pages, country profiles, and dashboards; indicator pages offer CSV downloads
    of the underlying data.
  format: http
  id: who.data-hub
  name: WHO Data Hub
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://data.who.int/
- category: GraphicalInterface
  description: WHO Institutional Repository for Information Sharing (IRIS), a DSpace
    repository of WHO publications, technical documents, governing body documents,
    and reports in multiple languages.
  format: http
  id: who.iris
  name: WHO IRIS
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://iris.who.int/
- category: ProgrammingInterface
  connection_url: https://iris.who.int/server/oai/request
  description: OAI-PMH 2.0 endpoint for harvesting metadata records from the WHO IRIS
    publications repository.
  format: http
  id: who.iris-oai-pmh
  is_public: true
  name: WHO IRIS OAI-PMH Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://iris.who.int/server/oai/request?verb=Identify
- category: GraphicalInterface
  description: WHO Disease Outbreak News page providing reports on confirmed and potential
    acute public health events of concern across hazards.
  format: http
  id: who.disease-outbreak-news
  name: WHO Disease Outbreak News
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/emergencies/disease-outbreak-news
- category: ProgrammingInterface
  connection_url: https://www.who.int/api/hubs/diseaseoutbreaknews
  description: WHO Sitefinity REST API endpoint for Disease Outbreak News items, exposing
    DON identifiers, titles, dates, overview, assessment, advice, and related metadata
    as JSON.
  format: json
  id: who.disease-outbreak-news-api
  is_public: true
  name: WHO Disease Outbreak News API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: who
  product_url: https://www.who.int/api/hubs/diseaseoutbreaknews/sfhelp
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
- category: Product
  description: CSV file containing the raw epidemiological information extractions
    used to derive eKG
  format: csv
  id: ekg.csv
  name: eKG Raw Extractions CSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ekg
  product_file_size: 185806
  product_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/ETOHA/corpus_processed/SUMMARIZED/OutputAnnotatedTexts-LLMs-ENSEMBLE_whoDons.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: who
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dailymed
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: fideo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
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
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
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
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: GraphProduct
  description: Source CSV tables for AcuKG, including acupoint therapeutic actions,
    indications, anatomy relationships, clinical trial links, and PubMed links.
  edge_count: 11527
  format: csv
  id: acukg.csv
  name: AcuKG CSV tables
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG
- category: GraphProduct
  description: RDF Turtle representation of AcuKG relationship tables.
  edge_count: 11527
  format: ttl
  id: acukg.rdf
  name: AcuKG RDF Turtle files
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_RDF
- category: GraphProduct
  description: JSON representation of AcuKG relationship tables.
  edge_count: 11527
  format: json
  id: acukg.json
  name: AcuKG JSON files
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_json
- category: Product
  description: Multilingual acupoint vocabulary listing the 361 standard acupoint
    codes with Chinese names, transliterations, English, Pinyin, Korean, and Vietnamese
    names.
  format: csv
  id: acukg.acupoint-vocabulary
  name: AcuKG local acupoint vocabulary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: who
  product_file_size: 14884
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/blob/main/local_acupoint_vocabulary.csv
- category: GraphicalInterface
  description: Thera-SAbDab search interface for finding therapeutic antibodies by
    INN, target, format, clinical stage or sequence similarity, with summary pages
    linking each therapeutic to its matching SAbDab structures.
  format: http
  id: therasabdab.portal
  name: Thera-SAbDab Search Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: sabdab
  product_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/therasabdab/search/
- category: Product
  description: CSV table of all Thera-SAbDab therapeutics with format, isotype, clinical
    trial stage and status, heavy and light chain variable domain sequences, matching
    SAbDab structures at 100%, 99% and 95-98% sequence identity, INN proposal and
    recommendation years, targets, companies and conditions.
  format: csv
  id: therasabdab.sequences-structures
  name: Thera-SAbDab Sequences and Structures Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_file_size: 636357
  product_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/static/downloads/TheraSAbDab_SeqStruc_OnlineDownload.csv
rrid: SCR_008505
synonyms:
- WHO
---
# World Health Organization

The World Health Organization (WHO) is the United Nations specialized agency for
international public health. It publishes global health statistics,
international classifications, technical guidance, and disease outbreak reports.

Data products include the Global Health Observatory (GHO), queryable through the
GHO OData API, and the newer WHO Data hub at data.who.int, to which WHO is moving
its indicator pages and dashboards. WHO publications are deposited in the IRIS
repository, which can be harvested over OAI-PMH. WHO Disease Outbreak News is
available as web pages and through a JSON API, and is an upstream source for the
eKG epidemiological knowledge graph.

WHO classifications have their own registry pages: ICD-10 (`icd10`) and ICD-11
(`icd11`), including the ICD-11 browser and API. The International Clinical
Trials Registry Platform is described at `who-ictrp`.

WHO content is mainly licensed under CC BY-NC-SA 3.0 IGO. ICD, ICF, and ICHI are
licensed under CC BY-ND 3.0 IGO. WHO data compilations come under WHO's own
data policy terms and conditions instead
(https://www.who.int/about/policies/publishing/data-policy/terms-and-conditions),
which permit use for public health purposes with attribution to WHO.