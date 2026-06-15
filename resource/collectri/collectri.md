---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: CollecTRI is a comprehensive collection of signed transcription factor (TF)-target gene regulatory interactions compiled from 12 different resources. It provides high-confidence regulons with expanded TF coverage and the sign (activation or repression) of each interaction, enabling accurate estimation of transcription factor activities from gene expression data. The regulons are distributed through the decoupler ecosystem and OmniPath for downstream enrichment and footprint analysis.
domains:
  - systems biology
  - genomics
  - pathways
homepage_url: https://github.com/saezlab/CollecTRI
id: collectri
last_modified_date: '2026-06-15T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gnu.org/licenses/gpl-3.0.en.html
  label: GPL-3.0
name: CollecTRI
products:
  - category: MappingProduct
    description: The CollecTRI gene regulatory network of signed transcription factor-target gene interactions, compiled from 12 resources, provided as a table of TF-target regulons with the sign (weight) of each interaction.
    format: csv
    id: collectri.regulons
    name: CollecTRI Regulons
    original_source:
      - relation_type: prov:hadPrimarySource
        source: collectri
    product_url: https://github.com/saezlab/CollecTRI
  - category: ProcessProduct
    description: Programmatic access to the CollecTRI regulons through the decoupler Python package, which retrieves the signed TF-target network for downstream transcription factor activity estimation.
    format: python
    id: collectri.decoupler
    name: CollecTRI via decoupler
    original_source:
      - relation_type: prov:hadPrimarySource
        source: collectri
    product_url: https://decoupler-py.readthedocs.io/
  - category: DocumentationProduct
    description: Source code, construction scripts, benchmarking and case-study notebooks, and usage documentation for CollecTRI.
    format: http
    id: collectri.docs
    name: CollecTRI Repository and Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: collectri
    product_url: https://github.com/saezlab/CollecTRI
publications:
  - authors:
      - Sophia Müller-Dott
      - Eirini Tsirvouli
      - Miguel Vazquez
      - Ricardo O Ramirez Flores
      - Pau Badia-i-Mompel
      - Robin Fallegger
      - Dénes Türei
      - Astrid Lægreid
      - Julio Saez-Rodriguez
    doi: doi:10.1093/nar/gkad841
    id: doi:10.1093/nar/gkad841
    journal: Nucleic Acids Research
    preferred: true
    title: Expanding the coverage of regulons from high-confidence prior knowledge for accurate estimation of transcription factor activities
    year: '2023'
repository: https://github.com/saezlab/CollecTRI
---

# CollecTRI

CollecTRI is a gene regulatory network resource that provides signed transcription
factor (TF)-target gene interactions compiled from 12 different resources. Each
interaction carries a sign indicating whether the TF activates or represses its
target, and the combined collection expands transcription factor coverage relative
to prior individual resources.

The regulons are designed for accurate estimation of transcription factor activities
from gene expression data and are accessible programmatically through the decoupler
Python package and the OmniPath database. The repository additionally provides the
scripts used to construct the network along with benchmarking and case-study
analyses.
