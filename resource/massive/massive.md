---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://ccms.ucsd.edu/
    label: UC San Diego Center for Computational Mass Spectrometry
creation_date: '2026-06-02T00:00:00Z'
description: MassIVE is a community mass spectrometry data repository developed by the NIH-funded UC San Diego Center for Computational Mass Spectrometry to support global, free exchange, browsing, redistribution, reanalysis, and publication-linked sharing of mass spectrometry datasets.
domains:
  - chemistry and biochemistry
  - biomedical
  - proteomics
homepage_url: https://massive.ucsd.edu/ProteoSAFe/static/massive.jsp
id: massive
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
name: MassIVE
publications:
  - authors:
      - Mingxun Wang
      - Jeremy J Carver
      - Vanessa V Phelan
      - Laura M Sanchez
      - Neha Garg
      - Yao Peng
      - Don Duy Nguyen
      - Jeramie Watrous
      - Clifford A Kapono
      - Tal Luzzatto-Knaan
      - Carla Porto
      - Amina Bouslimani
      - Alexey V Melnik
      - Michael J Meehan
      - Wei-Ting Liu
      - Max Crüsemann
      - Paul D Boudreau
      - Eduardo Esquenazi
      - Mario Sandoval-Calderón
      - Roland D Kersten
      - Laura A Pace
      - Robert A Quinn
      - Katherine R Duncan
      - Cheng-Chih Hsu
      - Dimitrios J Floros
      - Ronnie G Gavilan
      - Karin Kleigrewe
      - Trent Northen
      - Rachel J Dutton
      - Delphine Parrot
      - Erin E Carlson
      - Bertrand Aigle
      - Charlotte F Michelsen
      - Lars Jelsbak
      - Christian Sohlenkamp
      - Pavel Pevzner
      - Anna Edlund
      - Jeffrey McLean
      - Jörn Piel
      - Brian T Murphy
      - Lena Gerwick
      - Chih-Chuang Liaw
      - Yu-Liang Yang
      - Hans-Ulrich Humpf
      - Maria Maansson
      - Robert A Keyzers
      - Amy C Sims
      - Andrew R Johnson
      - Ashley M Sidebottom
      - Brian E Sedio
      - Andreas Klitgaard
      - Charles B Larson
      - Cristopher A Boya P
      - Daniel Torres-Mendoza
      - David J Gonzalez
      - Denise B Silva
      - Lucas M Marques
      - Daniel P Demarque
      - Egle Pociute
      - "Ellis C O'Neill"
      - Enora Briand
      - Eric J N Helfrich
      - Eve A Granatosky
      - Evgenia Glukhov
      - Florian Ryffel
      - Hailey Houson
      - Hosein Mohimani
      - Jenan J Kharbush
      - Yi Zeng
      - Julia A Vorholt
      - Kenji L Kurita
      - Pep Charusanti
      - Kerry L McPhail
      - Kristian Fog Nielsen
      - Lisa Vuong
      - Maryam Elfeki
      - Matthew F Traxler
      - Niclas Engene
      - Nobuhiro Koyama
      - Oliver B Vining
      - Ralph Baric
      - Ricardo R Silva
      - Samantha J Mascuch
      - Sophie Tomasi
      - Stefan Jenkins
      - Venkat Macherla
      - Thomas Hoffman
      - Vinayak Agarwal
      - Philip G Williams
      - Jingqui Dai
      - Ram Neupane
      - Joshua Gurr
      - Andrés M C Rodríguez
      - Anne Lamsa
      - Chen Zhang
      - Kathleen Dorrestein
      - Brendan M Duggan
      - Jehad Almaliti
      - Pierre-Marie Allard
      - Prasad Phapale
      - Louis-Felix Nothias
      - Theodore Alexandrov
      - Marc Litaudon
      - Jean-Luc Wolfender
      - Jennifer E Kyle
      - Thomas O Metz
      - Tyler Peryea
      - Dac-Trung Nguyen
      - Danielle VanLeer
      - Paul Shinn
      - Ajit Jadhav
      - Rolf Müller
      - Katrina M Waters
      - Wenyuan Shi
      - Xueting Liu
      - Lixin Zhang
      - Rob Knight
      - Paul R Jensen
      - Bernhard Ø Palsson
      - Kit Pogliano
      - Roger G Linington
      - Marcelino Gutiérrez
      - Norberto P Lopes
      - William H Gerwick
      - Bradley S Moore
      - Pieter C Dorrestein
      - Nuno Bandeira
    doi: 10.1038/nbt.3597
    id: https://doi.org/10.1038/nbt.3597
    journal: Nature Biotechnology
    title: Sharing and community curation of mass spectrometry data with Global Natural Products Social Molecular Networking
    year: '2016'
products:
  - category: GraphicalInterface
    description: MassIVE web portal for submitting, browsing, downloading, and reanalyzing public mass spectrometry datasets.
    format: http
    id: massive.portal
    name: MassIVE Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: massive
    product_url: https://massive.ucsd.edu/ProteoSAFe/static/massive.jsp
  - category: DocumentationProduct
    description: MassIVE documentation covering dataset sharing, public dataset access, reanalysis workflows, APIs, and related MassIVE services.
    format: http
    id: massive.docs
    name: MassIVE Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: massive
    product_url: https://ccms-ucsd.github.io/MassIVEDocumentation/
  - category: GraphProduct
    description: RDF knowledge graph materialized by the MetaBoKG workflow from public metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence, sample metadata, and environmental and taxonomic context. The repository documents generated per-job Turtle files under mapping/kg and loading into Virtuoso named graphs.
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
      - No static public graph release or hosted endpoint was available in the GitHub repository when curated on 2026-06-02; the repository documents local Turtle materialization and Virtuoso loading.
  - category: MappingProduct
    description: RML mappings and configuration templates used to transform GNPS, molecular networking, feature-based molecular networking, and ReDU data into RDF.
    format: http
    id: metabokg.rml_mappings
    license:
      id: https://www.apache.org/licenses/LICENSE-2.0
      label: Apache License 2.0
    name: MetaBoKG RML Mappings
    original_source:
      - relation_type: prov:hadPrimarySource
        source: metabokg
    product_url: https://github.com/HolobiomicsLab/MetaBoKG/tree/main/mapping/rml
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: gnps
      - relation_type: prov:wasInformedBy
        source: massive
      - relation_type: prov:wasInformedBy
        source: redu
  - category: GraphicalInterface
    description: Pan-ReDU dashboard and file-selection interface for exploring daily updated public metabolomics metadata and selecting public data for GNPS reanalysis.
    format: http
    id: redu.dashboard
    name: Pan-ReDU Dashboard
    original_source:
      - relation_type: prov:hadPrimarySource
        source: redu
    product_url: https://redu.gnps2.org/selection/
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: gnps
      - relation_type: prov:wasInformedBy
        source: massive
synonyms:
  - Mass Spectrometry Interactive Virtual Environment
  - MassIVE
---

# MassIVE

MassIVE is a public repository and analysis environment for mass spectrometry datasets. It supports dataset submission, access to public datasets, online reanalysis workflows, and publication-oriented dataset sharing.
