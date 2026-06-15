---
activity_status: active
category: DataSource
creation_date: '2026-06-15T00:00:00Z'
description: CollecTRI is a comprehensive collection of signed transcription factor
  (TF)-target gene regulatory interactions compiled from 12 different resources. It
  provides high-confidence regulons with expanded TF coverage and the sign (activation
  or repression) of each interaction, enabling accurate estimation of transcription
  factor activities from gene expression data. The regulons are distributed through
  the decoupler ecosystem and OmniPath for downstream enrichment and footprint analysis.
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
  description: The CollecTRI gene regulatory network of signed transcription factor-target
    gene interactions, compiled from 12 resources, provided as a table of TF-target
    regulons with the sign (weight) of each interaction.
  format: csv
  id: collectri.regulons
  name: CollecTRI Regulons
  original_source:
  - relation_type: prov:hadPrimarySource
    source: collectri
  product_url: https://github.com/saezlab/CollecTRI
- category: ProcessProduct
  description: Programmatic access to the CollecTRI regulons through the decoupler
    Python package, which retrieves the signed TF-target network for downstream transcription
    factor activity estimation.
  format: python
  id: collectri.decoupler
  name: CollecTRI via decoupler
  original_source:
  - relation_type: prov:hadPrimarySource
    source: collectri
  product_url: https://decoupler-py.readthedocs.io/
- category: DocumentationProduct
  description: Source code, construction scripts, benchmarking and case-study notebooks,
    and usage documentation for CollecTRI.
  format: http
  id: collectri.docs
  name: CollecTRI Repository and Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: collectri
  product_url: https://github.com/saezlab/CollecTRI
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
publications:
- authors:
  - "Sophia M\xFCller-Dott"
  - Eirini Tsirvouli
  - Miguel Vazquez
  - Ricardo O Ramirez Flores
  - Pau Badia-i-Mompel
  - Robin Fallegger
  - "D\xE9nes T\xFCrei"
  - "Astrid L\xE6greid"
  - Julio Saez-Rodriguez
  doi: doi:10.1093/nar/gkad841
  id: doi:10.1093/nar/gkad841
  journal: Nucleic Acids Research
  preferred: true
  title: Expanding the coverage of regulons from high-confidence prior knowledge for
    accurate estimation of transcription factor activities
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