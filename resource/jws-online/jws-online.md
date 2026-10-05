---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://jjj.biochem.sun.ac.za/
  label: JWS Online Team, Department of Biochemistry, Stellenbosch University
- category: Individual
  label: Jacky L. Snoep
creation_date: '2026-10-05T00:00:00Z'
description: JWS Online is a repository of curated kinetic models of biological systems
  with a browser-based simulation platform, developed by Jacky Snoep's group at Stellenbosch
  University with mirrors in Amsterdam and Manchester. It holds over 800 curated models
  (SBML-compliant, with downloads in SBML, Mathematica, JWS and PySCeS formats), a database
  of curated SED-ML simulation experiments for reproducing published figures, a model
  builder, and a REST API. Its models are shared with BioModels and integrated into
  FAIRDOMHub and FAIRDOM-SEEK.
domains:
- systems biology
- biological systems
- pathways
- metabolism
homepage_url: https://jjj.biochem.sun.ac.za/
id: jws-online
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: JWS Online
products:
- category: GraphicalInterface
  description: Web interface to browse the JWS Online database of curated kinetic models,
    filterable by organism, tissue, process and model type, with links to each model's
    detail page, schema and online simulator.
  format: http
  id: jws-online.models
  name: JWS Online Model Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jws-online
  product_url: https://jjj.biochem.sun.ac.za/models/
- category: Product
  description: Per-model downloads of curated JWS Online models in SBML (Level 3 Version
    1), with Mathematica, JWS and PySCeS exports also offered from the model database.
    Files are retrieved one model at a time via /models/<slug>/sbml/?download=1.
  format: xml
  id: jws-online.sbml
  name: JWS Online SBML Model Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jws-online
  product_url: https://jjj.biochem.sun.ac.za/models/achcar1/sbml/?download=1
- category: GraphicalInterface
  description: Database of curated simulation experiments (SED-ML) linked to JWS Online
    models, allowing one-click reproduction of figures from published papers, plus
    tools to build and upload simulations.
  format: http
  id: jws-online.simulations
  name: JWS Online Simulation Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jws-online
  product_url: https://jjj.biochem.sun.ac.za/models/experiments/
- category: GraphicalInterface
  description: Database of models submitted alongside manuscripts under review, curated
    by JWS Online on behalf of collaborating journals.
  format: http
  id: jws-online.manuscripts
  name: JWS Online Manuscript Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jws-online
  product_url: https://jjj.biochem.sun.ac.za/models/manuscripts/
- category: ProgrammingInterface
  description: REST API for listing and searching models and simulation experiments
    (by species or reaction ID), retrieving model and manuscript details as JSON, running
    time-course and steady-state analyses, and exporting or uploading models and simulations.
    Mostly usable without authentication.
  format: json
  id: jws-online.api
  is_public: true
  name: JWS Online REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jws-online
  product_url: https://jjj.biochem.sun.ac.za/rest/models/?format=json
- category: DocumentationProduct
  description: JWS Online 2.0 documentation covering model loading, upload, editing
    and building, the simulation environment, simulation experiments, the REST API,
    SED-ML support and the Docker image.
  format: http
  id: jws-online.docs
  name: JWS Online Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: jws-online
  product_url: https://jws-docs.readthedocs.io/
publications:
- authors:
  - Brett G. Olivier
  - Jacky L. Snoep
  doi: 10.1093/bioinformatics/bth200
  id: doi:10.1093/bioinformatics/bth200
  journal: Bioinformatics
  preferred: true
  title: Web-based kinetic modelling using JWS Online
  year: '2004'
- authors:
  - Martin Peters
  - Johann J Eicher
  - David D van Niekerk
  - Dagmar Waltemath
  - Jacky L Snoep
  doi: 10.1093/bioinformatics/btw831
  id: doi:10.1093/bioinformatics/btw831
  journal: Bioinformatics
  title: The JWS online simulation database
  year: '2017'
synonyms:
- JWS
- Java Web Simulation
---
# JWS Online

JWS Online is a systems biology resource for constructing, modifying and simulating kinetic models of biological systems, and for storing curated models. It was created in 2000 by Jacky Snoep and Brett Olivier and is developed by the Snoep group at Stellenbosch University, in collaboration with Hans Westerhoff's group at Vrije Universiteit Amsterdam.

## Servers

JWS Online runs on three servers with the same content:

- Stellenbosch: https://jjj.biochem.sun.ac.za/
- Amsterdam: https://jjj.bio.vu.nl/ (used in the documentation's REST examples)
- Manchester: https://jjj.mib.ac.uk/

The former domain jws-online.org did not respond when checked on 2026-10-04 and 2026-10-05. All three mirrors responded on 2026-10-05, though the Manchester and Amsterdam servers each timed out intermittently.

## Content

- **Model database**: 825 curated models (per the REST API on 2026-10-05), annotated with organism, tissue and process, downloadable as SBML, Mathematica, JWS or PySCeS files and simulatable in the browser (time evolution, steady state, metabolic control analysis, parameter scans, reaction plots, flux balance analysis).
- **Simulation database**: curated SED-ML simulation experiments that reproduce figures from published papers.
- **Manuscript database**: models curated for journal reviewers ahead of publication.
- **REST API**: under `/rest/` on each server; see the documentation.

JWS Online exchanges models with BioModels and is integrated into FAIRDOMHub and the FAIRDOM-SEEK platform. Models are identified at identifiers.org with the prefix `jws` (MIR:00000130).

No license for the models is stated on the site.
