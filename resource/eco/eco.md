---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  label: Michelle Giglio
  orcid: 0000-0001-7628-5565
  contact_details:
  - contact_type: email
    value: mgiglio@som.umaryland.edu
  - contact_type: github
    value: mgiglio99
creation_date: '2025-09-29T00:00:00Z'
description: An ontology for experimental and other evidence statements.
domains:
- biomedical
- general
homepage_url: https://www.evidenceontology.org
id: eco
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Evidence and Conclusion Ontology
products:
- category: OntologyProduct
  description: Evidence and Conclusion Ontology in OWL format
  format: owl
  id: eco.owl
  name: eco.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eco
  product_file_size: 346249
  product_url: http://purl.obolibrary.org/obo/eco.owl
- category: OntologyProduct
  description: Evidence and Conclusion Ontology in OBO format
  format: obo
  id: eco.obo
  name: eco.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eco
  product_file_size: 157676
  product_url: http://purl.obolibrary.org/obo/eco.obo
- category: Product
  description: TSV export of evidence annotations including ECO terms and supporting
    PMIDs.
  format: tsv
  id: swisslipid.evidences
  name: SwissLipids Evidences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: eco
  product_file_size: 47076
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=evidences.tsv
- category: Product
  description: Bulk download of DisProt data in multiple formats including JSON, TSV,
    FASTA, and GAF
  format: json
  id: disprot.downloads
  name: DisProt Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: disprot
  product_url: https://www.disprot.org/download
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: uniprot
  - relation_type: prov:wasInformedBy
    source: interpro
  - relation_type: prov:wasInformedBy
    source: go
  - relation_type: prov:wasInformedBy
    source: eco
- category: OntologyProduct
  description: IDP Ontology (IDPO) for representing functional aspects of intrinsically
    disordered proteins
  format: owl
  id: disprot.idpo
  name: IDP Ontology (IDPO)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: disprot
  product_file_size: 50945
  product_url: https://www.disprot.org/assets/data/IDPO_v0.3.0.owl
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: go
  - relation_type: prov:wasInformedBy
    source: eco
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/34986598
  title: 'ECO: the Evidence and Conclusion Ontology, an update for 2022.'
- id: https://www.ncbi.nlm.nih.gov/pubmed/30407590
  title: 'ECO, the Evidence & Conclusion Ontology: community standard for evidence
    information.'
- id: https://www.ncbi.nlm.nih.gov/pubmed/25052702
  title: Standardized description of scientific evidence using the Evidence Ontology
    (ECO)
repository: https://github.com/evidenceontology/evidenceontology
---
## Description

An ontology for experimental and other evidence statements.

## Contacts

- Michelle Giglio (mgiglio@som.umaryland.edu) [ORCID: 0000-0001-7628-5565](https://orcid.org/0000-0001-7628-5565)

## Products

### eco.owl

Evidence and Conclusion Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/eco.owl](http://purl.obolibrary.org/obo/eco.owl)

**Format**: owl

### eco.obo

Evidence and Conclusion Ontology in OBO format

**URL**: [http://purl.obolibrary.org/obo/eco.obo](http://purl.obolibrary.org/obo/eco.obo)

**Format**: obo

## Publications

- [ECO: the Evidence and Conclusion Ontology, an update for 2022.](https://www.ncbi.nlm.nih.gov/pubmed/34986598)
- [ECO, the Evidence & Conclusion Ontology: community standard for evidence information.](https://www.ncbi.nlm.nih.gov/pubmed/30407590)
- [Standardized description of scientific evidence using the Evidence Ontology (ECO)](https://www.ncbi.nlm.nih.gov/pubmed/25052702)

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
