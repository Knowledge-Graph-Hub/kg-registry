---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: davidos@ebi.ac.uk
      - contact_type: github
        value: dosumis
    label: David Osumi-Sutherland
    orcid: 0000-0002-7073-9172
creation_date: '2025-09-29T00:00:00Z'
description: The Provisional Cell Ontology (PCL) is an OBO Foundry ontology for draft cell type definitions derived from experimental evidence, especially single-cell and single-nucleus transcriptomics, that can later mature into conventionally defined Cell Ontology classes.
domains:
  - biological systems
homepage_url: https://github.com/obophenotype/provisional_cell_ontology
id: pcl
last_modified_date: '2026-05-23T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Provisional Cell Ontology
products:
  - category: OntologyProduct
    description: Main PCL release in OWL format
    format: owl
    id: pcl.owl
    name: Main PCL OWL release
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_file_size: 167561057
    product_url: http://purl.obolibrary.org/obo/pcl.owl
  - category: OntologyProduct
    description: Main PCL release in OBO format
    format: obo
    id: pcl.obo
    name: Main PCL OBO release
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_file_size: 39796128
    product_url: http://purl.obolibrary.org/obo/pcl.obo
  - category: OntologyProduct
    description: Main PCL release in OBOGraph JSON format
    format: json
    id: pcl.json
    name: Main PCL JSON release
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl.json
  - category: OntologyProduct
    description: PCL base release in OWL format
    format: owl
    id: pcl-base.owl
    name: PCL base release in OWL
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-base.owl
  - category: OntologyProduct
    description: PCL base release in OBO format
    format: obo
    id: pcl-base.obo
    name: PCL base release in OBO
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-base.obo
  - category: OntologyProduct
    description: PCL base release in OBOGraph JSON format
    format: json
    id: pcl-base.json
    name: PCL base release in JSON
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-base.json
  - category: OntologyProduct
    description: PCL full release in OWL format
    format: owl
    id: pcl-full.owl
    name: PCL full release in OWL
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-full.owl
  - category: OntologyProduct
    description: PCL full release in OBO format
    format: obo
    id: pcl-full.obo
    name: PCL full release in OBO
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-full.obo
  - category: OntologyProduct
    description: PCL full release in OBOGraph JSON format
    format: json
    id: pcl-full.json
    name: PCL full release in JSON
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-full.json
  - category: OntologyProduct
    description: PCL simple release in OWL format
    format: owl
    id: pcl-simple.owl
    name: PCL simple release in OWL
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-simple.owl
  - category: OntologyProduct
    description: PCL simple release in OBO format
    format: obo
    id: pcl-simple.obo
    name: PCL simple release in OBO
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-simple.obo
  - category: OntologyProduct
    description: PCL simple release in OBOGraph JSON format
    format: json
    id: pcl-simple.json
    name: PCL simple release in JSON
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pcl
    product_url: https://github.com/obophenotype/provisional_cell_ontology/releases/latest/download/pcl-simple.json
publications:
  - id: https://www.biorxiv.org/content/10.1101/2021.10.10.463703v1
    title: Brain Data Standards
  - id: https://pubmed.ncbi.nlm.nih.gov/34616062/
  - id: https://pubmed.ncbi.nlm.nih.gov/31435019/
  - id: https://pubmed.ncbi.nlm.nih.gov/29322913/
repository: https://github.com/obophenotype/provisional_cell_ontology
---

# Provisional Cell Ontology

The Provisional Cell Ontology (PCL) captures cell type definitions that are still
primarily grounded in experimental signatures, especially single-cell and single-nucleus
transcriptomics, rather than a stable set of classical defining properties. PCL terms
are intended to complement the Cell Ontology while those definitions mature, and may
later migrate into CL when they become conventionally defined.

PCL is maintained by the OBO Foundry and developed in the `obophenotype/provisional_cell_ontology`
repository using an ODK-based workflow. The repository README identifies the issue
tracker as the preferred channel for new term requests and corrections, while the OBO
Foundry entry and OLS provide the main public discovery surfaces.

## Access Points

- OBO Foundry entry: [PCL on OBO Foundry](https://obofoundry.org/ontology/pcl)
- Ontology browser: [PCL in OLS](https://www.ebi.ac.uk/ols4/ontologies/pcl)
- Source repository: [obophenotype/provisional_cell_ontology](https://github.com/obophenotype/provisional_cell_ontology)
- Issue tracker: [PCL GitHub issues](https://github.com/obophenotype/provisional_cell_ontology/issues)
- Latest releases: [PCL release assets](https://github.com/obophenotype/provisional_cell_ontology/releases/latest)
