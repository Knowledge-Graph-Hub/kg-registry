---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@scicrunch.org
  - contact_type: github
    value: SciCrunch
  label: SciCrunch
creation_date: '2026-11-12T00:00:00Z'
description: The NIF Standard Ontology (NIFSTD) is a collection of modular ontologies
  developed for the Neuroscience Information Framework (NIF) that provides terms and
  concepts for neuroscience and biology, including neurons, brain regions, subcellular
  components, molecules, dysfunctions, investigation techniques and resources. It
  is maintained by SciCrunch in the NIF-Ontology GitHub repository as Turtle files,
  with nif.ttl importing the NIF modules and bridge files to external ontologies such
  as Uberon, ChEBI, the Disease Ontology, the Gene Ontology and an NCBITaxon slim.
  New terms can be requested through the issue tracker or InterLex. The ontology is
  licensed under CC BY 4.0 and the repository also hosts the release artifacts of
  the SPARC Connectivity Knowledge Base of the Autonomic Nervous System (SCKAN).
domains:
- neuroscience
- anatomy and development
- biological systems
- cell biology
homepage_url: https://github.com/SciCrunch/NIF-Ontology
id: nif-ontology
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: NIF Standard Ontology
products:
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
  product_url: https://raw.githubusercontent.com/SciCrunch/NIF-Ontology/master/ttl/nif.ttl
- category: OntologyProduct
  description: NIFSTD ontology file in Turtle format from the dev branch, which carries
    the latest developments ahead of master.
  format: ttl
  id: nif-ontology.nif-dev.ttl
  name: NIFSTD (nif.ttl, dev branch)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nif-ontology
  product_url: https://raw.githubusercontent.com/SciCrunch/NIF-Ontology/dev/ttl/nif.ttl
- category: OntologyProduct
  description: NIF-Ontology GitHub repository holding the NIFSTD Turtle files (ttl/
    directory, with bridge, external, generated and utility subdirectories), documentation,
    and an issue tracker for new term requests. Workflows that ingest external content
    are maintained separately in the pyontutils repository.
  format: http
  id: nif-ontology.repository
  name: NIF-Ontology GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nif-ontology
  product_url: https://github.com/SciCrunch/NIF-Ontology
  repository: https://github.com/SciCrunch/NIF-Ontology
- category: DocumentationProduct
  description: Documentation for developing and using NIFSTD, covering development
    setup (including loading in Protege), editing processes, the import chain, external
    sources, neurons and brain regions.
  format: http
  id: nif-ontology.docs
  name: NIF-Ontology Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nif-ontology
  product_url: https://github.com/SciCrunch/NIF-Ontology/tree/master/docs
- category: Product
  description: Latest SCKAN data release on Zenodo (concept DOI, resolving to the
    newest version), containing the raw data inputs with the Blazegraph journal file,
    the SciGraph database, and a Docker data image bundling both with server configuration
    files.
  format: http
  id: sckan.data_release
  name: SCKAN Data Release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sparc
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: nif-ontology
  product_url: https://doi.org/10.5281/zenodo.5337441
publications:
- authors:
  - Bug WJ
  - Ascoli GA
  - Grethe JS
  - Gupta A
  - Fennema-Notestine C
  - Laird AR
  - Larson SD
  - Rubin D
  - Shepherd GM
  - Turner JA
  - Martone ME
  doi: 10.1007/s12021-008-9032-z
  id: doi:10.1007/s12021-008-9032-z
  journal: Neuroinformatics
  preferred: true
  title: 'The NIFSTD and BIRNLex Vocabularies: Building Comprehensive Ontologies for
    Neuroscience'
  year: '2008'
- authors:
  - Imam FT
  - Larson SD
  - Bandrowski A
  - Grethe JS
  - Gupta A
  - Martone ME
  doi: 10.3389/fgene.2012.00111
  id: doi:10.3389/fgene.2012.00111
  journal: Frontiers in Genetics
  title: 'Development and use of Ontologies Inside the Neuroscience Information Framework:
    A Practical Approach'
  year: '2012'
repository: https://github.com/SciCrunch/NIF-Ontology
rrid: SCR_005414
synonyms:
- NIFSTD
- NIF-Ontology
- NIF Ontology
- NIF Standard
- Neuroscience Information Framework Standard Ontology
version: 3.1 - January 15, 2018
---
# NIF Standard Ontology

The NIF Standard Ontology (NIFSTD) is a neuroscience ontology originally built for the Neuroscience Information Framework (NIF). It is organized as a set of modules covering neurons and other cell types, gross anatomy, subcellular components, molecules, dysfunctions, functions, qualities, investigations and resources, together with bridge files that link NIF terms to external ontologies such as Uberon, ChEBI, the Disease Ontology, the Gene Ontology and NCBITaxon.

SciCrunch maintains NIFSTD as Turtle files in the NIF-Ontology GitHub repository, where nif.ttl is the entry point; the latest changes are made on the dev branch. New terms can be requested through the GitHub issue tracker or contributed via InterLex. The contents are licensed under CC BY 4.0. The repository's GitHub releases also carry the SCKAN data releases.
