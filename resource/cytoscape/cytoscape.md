---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://cytoscape.org/
    label: Cytoscape Consortium
creation_date: '2026-06-02T00:00:00Z'
description: Cytoscape is an open-source platform for visualizing, analyzing, and integrating complex networks with biological and other attribute data.
domains:
  - biomedical
  - biological systems
  - information technology
  - pathways
homepage_url: https://cytoscape.org/
id: cytoscape
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/lgpl-2.1.html
  label: LGPL-2.1
name: Cytoscape
products:
  - category: GraphicalInterface
    description: Cross-platform Cytoscape desktop application for complex network visualization, molecular interaction analysis, and integration of network attribute data.
    id: cytoscape.desktop
    name: Cytoscape Desktop
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cytoscape
    product_url: https://cytoscape.org/download.html
    repository: https://github.com/cytoscape/cytoscape
  - category: GraphicalInterface
    description: Cytoscape App Store for discovering and installing Cytoscape apps that extend analysis, visualization, and data integration workflows.
    id: cytoscape.app-store
    name: Cytoscape App Store
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cytoscape
    product_url: https://apps.cytoscape.org/
  - category: ProgrammingInterface
    description: CyREST-powered Cytoscape Automation interface for executing reproducible Cytoscape workflows from external tools such as Python, R, and Jupyter.
    id: cytoscape.automation-api
    is_public: true
    name: Cytoscape Automation API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cytoscape
    product_url: https://apps.cytoscape.org/apps/cyrest
  - category: Product
    description: Open-source Cytoscape app that brings GeneMANIA gene function prediction, downloadable data sets, command-line tools, and Cytoscape Automation support to desktop network analysis workflows
    format: http
    id: genemania.cytoscape-app
    latest_version: 3.5.3
    name: GeneMANIA Cytoscape App
    original_source:
      - relation_type: prov:hadPrimarySource
        source: genemania
    product_url: https://apps.cytoscape.org/apps/genemania
    repository: https://github.com/GeneMANIA/genemania
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: cytoscape
publications:
  - authors:
      - Paul Shannon
      - Andrew Markiel
      - Owen Ozier
      - Nitin S Baliga
      - Jonathan T Wang
      - Daniel Ramage
    doi: 10.1101/gr.1239303
    id: doi:10.1101/gr.1239303
    journal: Genome Research
    preferred: true
    title: 'Cytoscape: a software environment for integrated models of biomolecular interaction networks'
    year: '2003'
repository: https://github.com/cytoscape/cytoscape
---

# Cytoscape

Cytoscape is an open-source network analysis and visualization platform widely
used for molecular interaction networks, pathways, systems biology, and other
complex network data. Its ecosystem includes the desktop application, an app
store, and automation interfaces for workflow-based analysis.
