---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: SCKAN (SPARC Connectivity Knowledge base of the Autonomic Nervous system) is a curated knowledge base representing neural circuit connectivity in the autonomic nervous system, derived from SPARC data, anatomical expert interviews, and scientific literature. It supports reasoning and querying of central and peripheral nervous system-end organ circuitry, including detailed ApiNATOMY models for organs such as bladder, heart, colon, stomach, spleen, pancreas, and airways.
domains:
  - biological systems
  - anatomy and development
id: sckan
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: SCKAN
products:
  - category: GraphicalInterface
    name: SCKAN Query Interface (Docker)
    id: sckan.query_interface
    description: Interactive computational notebook (Org mode) for querying SCKAN via SPARQL and Cypher, supporting parameterized queries, code blocks, and graphical results. Distributed as a Docker image.
    format: http
    product_url: https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan#download-docker-and-x11
  - category: Product
    name: SCKAN ApiNATOMY Models
    id: sckan.apinatomy
    description: Detailed ApiNATOMY models of neural circuits for organs including bladder, heart, colon, stomach, spleen, pancreas, and airways. Models are available in open-physiology repositories.
    format: http
    product_url: https://github.com/open-physiology/apinatomy-models
  - category: DocumentationProduct
    name: SCKAN Documentation and Tutorials
    id: sckan.docs
    description: Documentation, setup instructions, tutorials, and example queries for using and exploring SCKAN.
    format: http
    product_url: https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan
  - category: Product
    name: SCKAN Data Release
    id: sckan.data_release
    description: Latest SCKAN data release, including curated knowledge and models, available via Zenodo.
    format: http
    product_url: https://doi.org/10.5281/zenodo.5337441
---

# SCKAN

SCKAN is the SPARC Connectivity Knowledge base of the Autonomic Nervous system, supporting reasoning and querying of neural circuit connectivity. It includes detailed ApiNATOMY models, a computational notebook interface, and extensive documentation. For more information, see the [SCKAN documentation](https://github.com/SciCrunch/sparc-curation/tree/master/docs/sckan).
