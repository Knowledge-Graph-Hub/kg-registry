---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: smtifahim@gmail.com
  label: Fahim Imam
  orcid: 0000-0003-4752-543X
creation_date: '2025-09-29T00:00:00Z'
description: Neuronal cell types
domains:
- anatomy and development
- biological systems
- cell biology
- neuroscience
homepage_url: http://neuinfo.org/
id: nif_cell
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: NIF Cell
products:
- category: OntologyProduct
  description: NIF Cell ontology in Turtle format (SciCrunch NIF-Ontology repository)
  format: ttl
  id: nif_cell.ttl
  name: NIF Cell (Turtle)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nif_cell
  product_file_size: 246672
  product_url: https://raw.githubusercontent.com/SciCrunch/NIF-Ontology/master/ttl/NIF-Cell.ttl
- category: OntologyProduct
  description: Main NIFSTD ontology file in Turtle format from the master branch,
    which imports the NIF module files (cell, gross anatomy, dysfunction, function,
    investigation, molecule, quality, subcellular and neuron bridge modules) and bridge
    files to Uberon, ChEBI, the Disease Ontology, the Gene Ontology and an NCBITaxon
    slim. Also resolvable at http://ontology.neuinfo.org/NIF/ttl/nif.ttl.
  format: ttl
  id: nif-ontology.nif.ttl
  latest_version: 3.1 - January 15, 2018
  name: NIFSTD (nif.ttl, master branch)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nif-ontology
  - relation_type: prov:hadPrimarySource
    source: nif_cell
  - relation_type: prov:hadPrimarySource
    source: nif_dysfunction
  - relation_type: prov:hadPrimarySource
    source: nif_grossanatomy
  product_file_size: 1077
  product_url: https://raw.githubusercontent.com/SciCrunch/NIF-Ontology/master/ttl/nif.ttl
publications: []
use_instead:
- cl
---
## Description

A legacy ontology of neuronal cell types derived from NIFSTD (the Neuroscience
Information Framework Standard ontologies). It is obsolete and has been replaced
by the Cell Ontology (CL).

## Contacts

- Fahim Imam (smtifahim@gmail.com) [ORCID: 0000-0003-4752-543X](https://orcid.org/0000-0003-4752-543X)

## Products

### NIF Cell (Turtle)

NIF Cell ontology in Turtle format (SciCrunch NIF-Ontology repository)

**URL**: [https://raw.githubusercontent.com/SciCrunch/NIF-Ontology/master/ttl/NIF-Cell.ttl](https://raw.githubusercontent.com/SciCrunch/NIF-Ontology/master/ttl/NIF-Cell.ttl)

**Format**: ttl

**Domains**: anatomy and development

---

*This resource was automatically synchronized from the OBO Foundry registry.*