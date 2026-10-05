---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/biomodels/
  - contact_type: github
    value: EBI-BioModels
  id: ebi
  label: BioModels team, EMBL-EBI
creation_date: '2026-10-04T00:00:00Z'
description: BioModels is EMBL-EBI's repository of mathematical models of biological
  and biomedical systems. It holds manually curated models, which are checked to reproduce
  the results of their reference publication and annotated with cross-references to
  ontologies and databases such as GO, ChEBI, UniProt and Reactome, alongside non-curated
  submitted models and models generated automatically from pathway resources. Models
  are mainly encoded in SBML and distributed as COMBINE archives (OMEX). The models
  and their annotations are dedicated to the public domain under CC0.
domains:
- systems biology
- biological systems
fairsharing_id: FAIRsharing.paz6mh
homepage_url: https://www.ebi.ac.uk/biomodels/
id: biomodels
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: BioModels
products:
- category: GraphicalInterface
  description: Web interface for searching, browsing and downloading curated and non-curated
    computational models, with model files, annotations, curation notes and links
    to the reference publications.
  format: http
  id: biomodels.portal
  name: BioModels Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomodels
  product_url: https://www.ebi.ac.uk/biomodels/
- category: ProgrammingInterface
  description: REST web services for searching BioModels, retrieving model metadata
    and files, and downloading models, documented with an interactive API reference.
  format: http
  id: biomodels.api
  name: BioModels REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomodels
  product_url: https://www.ebi.ac.uk/biomodels/docs/
- category: Product
  compression: other
  description: Last numbered BioModels Database release (release 31, June 2017) of
    the published models as SBML files in a tar.bz2 archive, about 184 MB compressed.
    Companion archives in the same directory hold the RDF annotations and all model
    files. Later models are only available through the portal and API.
  format: sbml
  id: biomodels.release.sbml
  latest_version: r31
  name: BioModels Database Release 31 SBML Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomodels
  product_url: https://ftp.ebi.ac.uk/pub/databases/biomodels/releases/latest/BioModels_Database-r31_pub-sbml_files.tar.bz2
  warnings:
  - The latest numbered release on the FTP site is release 31 from 2017; current models
    are not included. Checked on 2026-10-04.
- category: Product
  compression: other
  description: RDF export of BioModels models, one RDF/XML file per model describing
    its SBML structure and annotations, in a tar.bz2 archive of about 28 MB, last
    generated on 2020-11-12.
  format: rdfxml
  id: biomodels.rdf
  latest_version: '2020-11-12'
  name: BioModels RDF Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomodels
  product_url: https://ftp.ebi.ac.uk/pub/databases/biomodels/rdf/BioModels-RDF-export-latest.tar.bz2
- category: DocumentationProduct
  description: BioModels user guide covering model submission, curation, annotation
    and use of the repository.
  format: http
  id: biomodels.user-guide
  name: BioModels User Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomodels
  product_url: https://github.com/EBI-BioModels/user-guide
- category: ProcessProduct
  description: Source code for the BioModels platform and related tools, including
    the COMBINE archive libraries, in the EBI-BioModels GitHub organization.
  format: mixed
  id: biomodels.code
  name: BioModels Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomodels
  product_url: https://github.com/EBI-BioModels
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - Rahuman S Malik-Sheriff
  - Mihai Glont
  - Tung V N Nguyen
  - Krishna Tiwari
  - Matthew G Roberts
  - Ashley Xavier
  - Manh T Vu
  - Jinghao Men
  - Matthieu Maire
  - Sarubini Kananathan
  - Emma L Fairbanks
  - Johannes P Meyer
  - Chinmay Arankalle
  - Thawfeek M Varusai
  - Vincent Knight-Schrijver
  - Lu Li
  - Corina Dueñas-Roca
  - Gaurhari Dass
  - Sarah M Keating
  - Young M Park
  - Nicola Buso
  - Nicolas Rodriguez
  - Michael Hucka
  - Henning Hermjakob
  doi: 10.1093/nar/gkz1055
  id: doi:10.1093/nar/gkz1055
  journal: Nucleic Acids Research
  preferred: true
  title: BioModels—15 years of sharing computational models in life science
  year: '2019'
synonyms:
- BioModels Database
- BioModels Repository
---
# BioModels

BioModels is a repository of mathematical models of biological processes, run by EMBL-EBI. It has three main kinds of model:

- **Manually curated models**, which are checked to reproduce the results in their reference publication and are annotated with cross-references to ontologies and databases such as GO, ChEBI, UniProt and Reactome.
- **Non-curated models**, deposited by submitters and released without that check.
- **Automatically generated models**, built from pathway resources.

Models are mainly encoded in SBML, often with simulation descriptions in SED-ML, and are distributed as COMBINE archives (OMEX).

## Access

Models can be searched and downloaded through the web portal and the REST API. The FTP site holds the last numbered BioModels Database release (release 31, June 2017), an RDF export of the models from 2020, and other archives. Models added after 2017 are only available through the portal and the API.

## License

The terms of use dedicate the BioModels dataset, including the encoded models and their annotations, to the public domain under CC0.

BioModels is also indexed by OmicsDI.