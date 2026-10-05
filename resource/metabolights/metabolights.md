---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ebi.ac.uk/metabolights/
  - contact_type: github
    value: EBI-Metabolights
  id: ebi
  label: MetaboLights team, EMBL-EBI
creation_date: '2026-10-04T00:00:00Z'
description: MetaboLights is EMBL-EBI's open repository for metabolomics experiments
  and derived information. It holds study metadata in ISA-Tab format, raw and processed
  spectra, and metabolite identifications across species and techniques (mass spectrometry
  and NMR), and its reference layer links metabolites to ChEBI. It held 3,490 public
  studies on 2026-10-04. Studies submitted from April 2025 are released under CC0;
  earlier studies are governed by the EMBL-EBI Terms of Use.
domains:
- metabolomics
- chemistry and biochemistry
- biological systems
homepage_url: https://www.ebi.ac.uk/metabolights/
id: metabolights
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ebi.ac.uk/about/terms-of-use
  label: EMBL-EBI Terms of Use
name: MetaboLights
products:
- category: GraphicalInterface
  description: Web interface for searching, browsing and submitting MetaboLights metabolomics
    studies (MTBLS accessions) and their metabolite annotations.
  format: http
  id: metabolights.portal
  name: MetaboLights Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  product_url: https://www.ebi.ac.uk/metabolights/
- category: ProgrammingInterface
  description: MetaboLights RESTful web service (MtblsWS-Py) for listing studies and
    retrieving study metadata, ISA-Tab files and metabolite assignments, documented
    with an OpenAPI specification.
  format: http
  id: metabolights.api
  name: MetaboLights REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  product_url: https://www.ebi.ac.uk/metabolights/ws/
- category: Product
  description: FTP/HTTPS download area holding every public MetaboLights study as
    a directory of ISA-Tab metadata, raw and processed data files, organized by MTBLS
    accession.
  format: mixed
  id: metabolights.studies
  name: MetaboLights Public Studies Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  product_url: https://ftp.ebi.ac.uk/pub/databases/metabolights/studies/public/
- category: Product
  description: Complete EB-eye XML export of MetaboLights studies and metabolites,
    as used for EBI Search indexing, regenerated daily (about 369 MB on 2026-10-04).
  format: xml
  id: metabolights.ebeye.complete
  name: MetaboLights EB-eye Complete Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  product_file_size: 370291873
  product_url: https://ftp.ebi.ac.uk/pub/databases/metabolights/eb-eye/eb_eye_metabolights_complete.xml
- category: Product
  description: EB-eye XML export of MetaboLights study records only, regenerated daily
    (about 344 MB on 2026-10-04).
  format: xml
  id: metabolights.ebeye.studies
  name: MetaboLights EB-eye Studies Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  product_file_size: 344727382
  product_url: https://ftp.ebi.ac.uk/pub/databases/metabolights/eb-eye/eb_eye_metabolights_studies.xml
- category: MappingProduct
  description: JSON mapping from MetaboLights studies to the metabolites (ChEBI identifiers)
    reported in them, last updated in October 2020.
  format: json
  id: metabolights.study-metabolites
  name: MetaboLights Study to Metabolite Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: chebi
  product_file_size: 137433775
  product_url: https://ftp.ebi.ac.uk/pub/databases/metabolights/eb-eye/study_metabolites_mapping.json
- category: Product
  description: JSON list of the ChEBI identifiers of metabolites in the MetaboLights
    reference layer, last updated in October 2020.
  format: json
  id: metabolights.metabolites
  name: MetaboLights Reference Metabolite List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: chebi
  product_file_size: 341671
  product_url: https://ftp.ebi.ac.uk/pub/databases/metabolights/eb-eye/metabolites_complete.json
- category: DocumentationProduct
  description: MetaboLights help guides covering study submission, ISA-Tab metadata,
    data formats and downloads.
  format: http
  id: metabolights.docs
  name: MetaboLights Guides
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  product_url: https://www.ebi.ac.uk/metabolights/guides
- category: ProcessProduct
  description: GitHub organization holding the MetaboLights web service, submission
    tooling and pipelines.
  format: mixed
  id: metabolights.code
  name: MetaboLights Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metabolights
  product_url: https://github.com/EBI-Metabolights
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
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - Ozgur Yurekten
  - Thomas Payne
  - Noemi Tejera
  - Felix Xavier Amaladoss
  - Callum Martin
  - Mark Williams
  - Claire O’Donovan
  doi: 10.1093/nar/gkad1045
  id: doi:10.1093/nar/gkad1045
  journal: Nucleic Acids Research
  preferred: true
  title: 'MetaboLights: open data repository for metabolomics'
  year: '2024'
- authors:
  - Kenneth Haug
  - Reza M. Salek
  - Pablo Conesa
  - Janna Hastings
  - Paula de Matos
  - Mark Rijnbeek
  - Tejasvi Mahendraker
  - Mark Williams
  - Steffen Neumann
  - Philippe Rocca-Serra
  - Eamonn Maguire
  - Alejandra González-Beltrán
  - Susanna-Assunta Sansone
  - Julian L. Griffin
  - Christoph Steinbeck
  doi: 10.1093/nar/gks1004
  id: doi:10.1093/nar/gks1004
  journal: Nucleic Acids Research
  title: MetaboLights—an open-access general-purpose repository for metabolomics studies
    and associated meta-data
  year: '2013'
synonyms:
- MTBLS
---
# MetaboLights

MetaboLights is the metabolomics repository of EMBL-EBI. Each study has an MTBLS accession and is described in ISA-Tab, with sample, protocol and assay metadata alongside raw and processed mass spectrometry or NMR data and metabolite assignment files. Its reference layer describes metabolites, linked to ChEBI.

## Access

- **Portal**: https://www.ebi.ac.uk/metabolights/
- **REST API**: https://www.ebi.ac.uk/metabolights/ws/ (OpenAPI spec at `ws/api/spec.json`)
- **Downloads**: https://ftp.ebi.ac.uk/pub/databases/metabolights/ (public studies under `studies/public/`; EB-eye exports under `eb-eye/`)

The EB-eye study and complete exports were regenerated on 2026-10-04. The ChEBI metabolite list and study to metabolite mapping in `eb-eye/` were last updated in October 2020.

## License

Studies submitted from April 2025 are released under CC0. Earlier studies are governed by the [EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use), which impose no restrictions beyond those of the data submitters.

## Related resources

MetaboLights is indexed by OmicsDI and is a member of the metabolomics data-sharing community alongside the Metabolomics Workbench.