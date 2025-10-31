---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@disprot.org
  label: DisProt Team
- category: Individual
  contact_details:
  - contact_type: email
    value: biocomp@bio.unipd.it
  label: Damiano Piovesan
creation_date: '2025-10-30T00:00:00Z'
description: DisProt is a manually curated database of experimentally validated intrinsically
  disordered proteins (IDPs) and intrinsically disordered regions (IDRs), providing
  annotations for structural disorder and functional aspects of protein disorder.
domains:
- proteomics
- biological systems
homepage_url: https://www.disprot.org
id: disprot
infores_id: disprot
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: Creative Commons Attribution 4.0 International (CC BY 4.0)
name: DisProt
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching intrinsically disordered protein
    annotations with search filters and organism browsing
  format: http
  id: disprot.browser
  name: DisProt Browser
  original_source:
  - disprot
  product_url: https://www.disprot.org/browse
- category: Product
  description: Bulk download of DisProt data in multiple formats including JSON, TSV,
    FASTA, and GAF
  format: json
  id: disprot.downloads
  name: DisProt Downloads
  original_source:
  - disprot
  product_url: https://www.disprot.org/download
- category: ProgrammingInterface
  description: RESTful API for programmatic access to DisProt data
  format: http
  id: disprot.api
  is_public: true
  name: DisProt API
  original_source:
  - disprot
  product_url: https://www.disprot.org/api
- category: GraphicalInterface
  description: Deposition system for submitting experimental data on intrinsically
    disordered proteins
  id: disprot.deposition
  name: DisProt Deposition System
  original_source:
  - disprot
  product_url: https://deposition.disprot.org/
- category: OntologyProduct
  description: IDP Ontology (IDPO) for representing functional aspects of intrinsically
    disordered proteins
  format: owl
  id: disprot.idpo
  name: IDP Ontology (IDPO)
  original_source:
  - disprot
  product_file_size: 50945
  product_url: https://www.disprot.org/assets/data/IDPO_v0.3.0.owl
publications:
- category: Publication
  id: PMID:37904585
  preferred: true
- category: Publication
  id: PMID:34850135
- category: Publication
  id: PMID:31713636
---
# DisProt

## Overview

DisProt is the major manually curated repository of intrinsically disordered proteins (IDPs), covering both structural and functional aspects. Expert curators collect experimentally confirmed biological data on protein disorder, making it a valuable resource for the scientific community. DisProt is part of the ELIXIR infrastructure and serves the IDP Community.

## Data Content

DisProt provides comprehensive annotations for:

- **Intrinsically Disordered Regions (IDRs)**: Experimentally validated regions of structural disorder in proteins
- **Functional Annotations**: Biological functions associated with disordered regions
- **Experimental Evidence**: Curated experimental data supporting disorder and function annotations
- **Cross-references**: Integration with UniProt, InterPro, Gene Ontology, and Evidence Ontology

Current release (9.8, 2025_06) contains **3,201 entries** covering multiple organisms:
- Human: 952 entries
- Mouse: 198 entries  
- Rat: 89 entries
- Yeast: 209 entries
- E. coli: 8 entries
- Arabidopsis: 114 entries
- Fly: 64 entries

## Key Features

- Manual curation by expert biocurators following standardized guidelines
- Daily updates and maintenance
- Experimentally validated annotations from published scientific literature
- Thematic datasets on specific topics (e.g., age-related disorders)
- Integration with major biological databases
- Training materials and courses for biocuration

## Access Methods

- **Web Browser**: Interactive search and browse interface
- **Bulk Downloads**: Complete database exports in JSON, TSV, FASTA, and GAF formats
- **REST API**: Programmatic data access for computational workflows
- **Deposition System**: Portal for submitting new experimental data

## Use Cases

- Training and validation of disorder prediction methods (CAID - Critical Assessment of Protein Intrinsic Disorder Prediction)
- Studying structure-function relationships in disordered proteins
- Analyzing disease-associated protein disorder
- Developing computational tools for IDP analysis
- Meta-analyses of protein disorder across organisms

## IDP Ontology

DisProt maintains the IDP Ontology (IDPO) v0.3.0, which represents functional aspects of intrinsically disordered proteins. Available in JSON, OWL, and OBO formats with mappings to Gene Ontology and Evidence & Conclusion Ontology terms.

## Management

DisProt is maintained by the BioComputing UP group at the University of Padua, Italy, led by:
- Prof. Silvio C.E. Tosatto (Team Leader)
- Prof. Damiano Piovesan (Team Leader & Software Developer)
- Dr. Maria Cristina Aspromonte (DisProt Manager)

The project operates with an international Scientific Advisory Board and is funded by the European Union's Horizon 2020 programme (grant agreement No. 778247).

## Funding

European Union's Horizon 2020 research and innovation programme under grant agreement No. 778247.