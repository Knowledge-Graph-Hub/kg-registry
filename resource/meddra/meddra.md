---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://admin.ich.org/page/meddra
    label: ICH MedDRA Maintenance and Support Services Organisation
creation_date: '2026-06-02T00:00:00Z'
description: MedDRA, the Medical Dictionary for Regulatory Activities, is an ICH standardized medical terminology used internationally for registration, documentation, safety monitoring, and pharmacovigilance of medical products.
domains:
  - clinical
  - biomedical
  - pharmacology
  - clinical coding
  - pharmacovigilance
homepage_url: https://admin.ich.org/page/meddra
id: meddra
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: MedDRA
products:
  - category: Product
    description: MedDRA terminology release files maintained and distributed by the MedDRA MSSO for subscribers, supporting regulatory coding and pharmacovigilance workflows.
    format: txt
    id: meddra.release-files
    name: MedDRA Terminology Release Files
    original_source:
      - relation_type: prov:hadPrimarySource
        source: meddra
    product_url: https://www.meddra.org/subscription
  - category: GraphicalInterface
    description: MedDRA Web-Based Browser provided for MedDRA subscribers to search and view MedDRA terminology content.
    format: http
    id: meddra.web-browser
    name: MedDRA Web-Based Browser
    original_source:
      - relation_type: prov:hadPrimarySource
        source: meddra
    product_url: https://mssotools.com/MSSOWeb/wbb/wbb_index.html
  - category: DocumentationProduct
    description: ICH MedDRA page describing the terminology, governance, MSSO maintenance, and regulatory use cases.
    format: http
    id: meddra.ich-page
    name: ICH MedDRA Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: meddra
    product_url: https://admin.ich.org/page/meddra
  - category: Product
    description: Quarterly data extracts in ASCII format containing demographic, drug, reaction, outcome, and source information for reported adverse events
    format: txt
    id: faers.quarterly_data_ascii
    latest_version: 2026Q1
    name: FAERS Quarterly Data Files (ASCII)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: faers
    product_url: https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: meddra
  - category: Product
    description: Quarterly data extracts in XML format adhering to ICH E2B standards for international safety reporting
    format: xml
    id: faers.quarterly_data_xml
    latest_version: 2026Q1
    name: FAERS Quarterly Data Files (XML)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: faers
    product_url: https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: meddra
  - category: Product
    description: Babel compendia, one file per Biolink type (for example Gene, Protein, Disease,
      ChemicalEntity, SmallMolecule, AnatomicalEntity). Each line is a JSON object for one clique,
      listing its identifiers with labels, descriptions and taxa, plus the preferred name and
      information content. Files carry a .txt extension; the Gene and Protein files (about 17.8
      GB and 46.7 GB) are also split into parts.
    format: json
    id: babel.compendia
    latest_version: 2026jul22
    name: Babel Compendia
    original_source:
      - relation_type: prov:hadPrimarySource
        source: babel
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: pubchem
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: pubmed
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: pmc
      - relation_type: prov:hadPrimarySource
        source: umls
      - relation_type: prov:hadPrimarySource
        source: chembl
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: mgi
      - relation_type: prov:hadPrimarySource
        source: rgd
      - relation_type: prov:hadPrimarySource
        source: mesh
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: hmdb
      - relation_type: prov:hadPrimarySource
        source: unii
      - relation_type: prov:hadPrimarySource
        source: rxnorm
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: snomedct
      - relation_type: prov:hadPrimarySource
        source: fma
      - relation_type: prov:hadPrimarySource
        source: rhea
      - relation_type: prov:hadPrimarySource
        source: ncit
      - relation_type: prov:hadPrimarySource
        source: meddra
      - relation_type: prov:hadPrimarySource
        source: wormbase
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: zfin
      - relation_type: prov:hadPrimarySource
        source: flybase
      - relation_type: prov:hadPrimarySource
        source: smpdb
      - relation_type: prov:hadPrimarySource
        source: omim
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: panther
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: complexportal
      - relation_type: prov:hadPrimarySource
        source: drugbank
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: kegg
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: gtopdb
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: orphanet
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: emapa
      - relation_type: prov:hadPrimarySource
        source: sgd
      - relation_type: prov:hadPrimarySource
        source: drugcentral
      - relation_type: prov:hadPrimarySource
        source: cl
    product_url: https://stars.renci.org/var/babel_outputs/latest/compendia/
  - category: ProcessProduct
    description: Code used to build iDISK 1.0 from its source databases, including normalization
      against UMLS and MedDRA.
    format: python
    id: idisk.code
    name: iDISK Build Code
    original_source:
    - relation_type: prov:hadPrimarySource
      source: idisk
    - relation_type: prov:hadPrimarySource
      source: umls
    - relation_type: prov:hadPrimarySource
      source: meddra
    product_url: https://github.com/jvasilakes/iDISK
publications:
  - authors:
      - Brown EG
      - Wood L
      - Wood S
    doi: 10.2165/00002018-199920020-00002
    id: https://www.ncbi.nlm.nih.gov/pubmed/10082069
    journal: Drug Saf
    preferred: true
    title: The Medical Dictionary for Regulatory Activities (MedDRA)
    year: '1999'
synonyms:
  - Medical Dictionary for Regulatory Activities
warnings:
  - MedDRA terminology files and browser access are controlled through the MedDRA MSSO subscription model; access conditions should be checked before reuse.
---

# MedDRA

MedDRA is the international medical terminology maintained by the ICH MedDRA
MSSO for regulatory reporting, safety monitoring, and pharmacovigilance. FAERS
uses MedDRA terminology for adverse-event reaction coding in its quarterly data
files.
