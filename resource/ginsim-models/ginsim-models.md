---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ginsim.github.io/contact/
  - contact_type: email
    value: ginsim-users@googlegroups.com
  - contact_type: github
    value: GINsim
  label: GINsim team
creation_date: '2026-10-05T00:00:00Z'
description: The GINsim model repository collects curated logical (Boolean and multi-valued)
  models of gene regulatory and signalling networks, maintained by the GINsim team
  (Claudine Chaouiya, Pedro T. Monteiro, Aurelien Naldi and Denis Thieffry). Its 70
  model pages, from a 1995 phage lambda lysis-lysogeny model to a 2024 promyelocytic
  leukaemia model, cover development, cell cycle, cell fate, immune cell differentiation
  and cancer signalling in organisms such as Drosophila, yeasts and mammals. Each
  page gives the taxon, biological process, authors and reference publications, and
  provides the model in the GINsim zginml format, with SBML-qual files and Jupyter
  notebooks for some models. The repository is part of the GINsim website, whose content
  is available under CC BY-NC-SA 4.0 unless stated otherwise.
domains:
- systems biology
- biological systems
homepage_url: https://ginsim.github.io/models/
id: ginsim-models
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: GINsim Model Repository
products:
- category: GraphicalInterface
  description: Web table of the 70 logical models in the repository, filterable by
    model name, taxon, biological process, year and authors, linking to one page per
    model with a description, reference publications and model file downloads.
  format: http
  id: ginsim-models.repository
  name: GINsim Model Repository Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ginsim-models
  product_url: https://ginsim.github.io/models/
- category: Product
  compression: zip
  description: Logical models in the GINsim zginml format (a zip archive holding the
    GINML XML regulatory graph and associated settings), downloadable from each model
    page. About 90 zginml files cover the 70 models.
  format: xml
  id: ginsim-models.zginml
  name: GINsim Model Files (zginml)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ginsim-models
  product_url: https://ginsim.github.io/models/
- category: Product
  description: Logical models exported in SBML Level 3 qualitative models (SBML-qual)
    format, downloadable from the model pages. Only nine SBML-qual files, for seven
    models, were present when checked on 2026-10-05; the other models are distributed
    in zginml only, which GINsim can export to SBML-qual.
  format: sbml
  id: ginsim-models.sbml-qual
  name: GINsim Model Files (SBML-qual)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ginsim-models
  product_url: https://ginsim.github.io/models/
- category: Product
  description: Directory of the GINsim website GitHub repository (mkdocs branch) holding
    the source of every model page, with the zginml and SBML-qual model files, Jupyter
    notebooks, figures and supplementary files. New models can be contributed by pull
    request.
  format: mixed
  id: ginsim-models.github
  name: GINsim Model Repository Sources on GitHub
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ginsim-models
  product_url: https://github.com/GINsim/GINsim.github.io/tree/mkdocs/docs/models
- category: ProcessProduct
  description: GINsim (Gene Interaction Network simulation), a Java desktop application
    for building, simulating and analysing logical models of regulatory networks,
    including state transition graphs, stable state and trap space search, model reduction
    and export to formats such as SBML-qual, NuSMV and Petri nets. Version 3.1 (January
    2026) requires Java 11 or later.
  format: java
  id: ginsim-models.software
  latest_version: '3.1'
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.html
    label: GPL-3.0
  name: GINsim Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ginsim-models
  product_file_size: 40731588
  product_url: https://ginsim.github.io/install/GINsim-3.1-with-deps.jar
  repository: https://github.com/GINsim/GINsim
- category: DocumentationProduct
  description: GINsim user documentation covering the graphical interface, logical
    regulatory graphs, perturbations, model reduction, simulation and dynamical analyses,
    and supported import and export formats.
  format: http
  id: ginsim-models.docs
  name: GINsim Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ginsim-models
  product_url: https://ginsim.github.io/documentation/
- category: GraphicalInterface
  description: Former location of the GINsim model repository on the ginsim.org website,
    hosted at IGC and INESC-ID before the move to GitHub Pages.
  format: http
  id: ginsim-models.legacy-repository
  name: GINsim Model Repository (ginsim.org)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ginsim-models
  product_url: http://ginsim.org/models_repository
  warnings:
  - When checked on 2026-10-05 the URL returned HTTP 200 but served a domain parking
    page ("ginsim.org is coming soon") instead of the model repository.
publications:
- authors:
  - Aurélien Naldi
  - Céline Hernandez
  - Wassim Abou-Jaoudé
  - Pedro T. Monteiro
  - Claudine Chaouiya
  - Denis Thieffry
  doi: 10.3389/fphys.2018.00646
  id: doi:10.3389/fphys.2018.00646
  journal: Frontiers in Physiology
  preferred: true
  title: Logical Modeling and Analysis of Cellular Regulatory Networks With GINsim
    3.0
  year: '2018'
- authors:
  - Claudine Chaouiya
  - Aurélien Naldi
  - Denis Thieffry
  doi: 10.1007/978-1-61779-361-5_23
  id: doi:10.1007/978-1-61779-361-5_23
  journal: Methods in Molecular Biology
  title: Logical Modelling of Gene Regulatory Networks with GINsim
  year: '2012'
- authors:
  - A. Gonzalez Gonzalez
  - A. Naldi
  - L. Sánchez
  - D. Thieffry
  - C. Chaouiya
  doi: 10.1016/j.biosystems.2005.10.003
  id: doi:10.1016/j.biosystems.2005.10.003
  journal: Biosystems
  title: 'GINsim: A software suite for the qualitative modelling, simulation and analysis
    of regulatory networks'
  year: '2006'
repository: https://github.com/GINsim/GINsim.github.io
synonyms:
- GINsim model library
- GINsim models
---
# GINsim Model Repository

The GINsim model repository is the model library of GINsim (Gene Interaction Network simulation), a tool for logical modelling of regulatory networks developed by Claudine Chaouiya, Pedro T. Monteiro, Aurélien Naldi, Denis Thieffry and colleagues. It holds 70 curated logical (Boolean and multi-valued) models of regulatory and signalling networks, each on its own page with the taxon, biological process, authors, reference publications and downloadable model files.

## Content

Models span from 1995 to 2024 and cover topics such as the phage lambda lysis-lysogeny decision, Drosophila segmentation and signalling pathways, yeast and mammalian cell cycles, T helper cell differentiation, and cancer signalling and treatment response.

## Formats and Access

- Every model is available in GINsim's zginml format (a zip archive of the GINML XML graph).
- SBML-qual files are provided for a few models; GINsim can export any model to SBML-qual.
- The website and model files are maintained in the [GINsim.github.io](https://github.com/GINsim/GINsim.github.io) repository, and new models can be added by pull request.

The repository moved from ginsim.org to GitHub Pages. The old `ginsim.org` address now shows a domain parking page.

## License

The GINsim website content, including the model repository, is available under CC BY-NC-SA 4.0 unless stated otherwise on specific pages. The GINsim software has been licensed under GPL-3.0 since version 2.9.3.