---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: mgiglio@som.umaryland.edu
  - contact_type: github
    value: mgiglio99
  label: Michelle Giglio
  orcid: 0000-0001-7628-5565
creation_date: '2025-09-29T00:00:00Z'
description: An ontology for experimental and other evidence statements.
domains:
- biomedical
- general
homepage_url: https://www.evidenceontology.org
id: eco
infores_id: eco
last_modified_date: '2026-06-18T00:00:00Z'
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
  - Nadendla S
  - Jackson R
  - Munro J
  - Quaglia F
  - Mészáros B
  - Olley D
  - Hobbs ET
  - Goralski SM
  - Chibucos M
  - Mungall CJ
  - Tosatto SCE
  - Erill I
  - Giglio MG
  doi: 10.1093/nar/gkab1025
  id: https://www.ncbi.nlm.nih.gov/pubmed/34986598
  journal: Nucleic Acids Res
  title: 'ECO: the Evidence and Conclusion Ontology, an update for 2022.'
  year: '2022'
- authors:
  - Giglio M
  - Tauber R
  - Nadendla S
  - Munro J
  - Olley D
  - Ball S
  - Mitraka E
  - Schriml LM
  - Gaudet P
  - Hobbs ET
  - Erill I
  - Siegele DA
  - Hu JC
  - Mungall C
  - Chibucos MC
  doi: 10.1093/nar/gky1036
  id: https://www.ncbi.nlm.nih.gov/pubmed/30407590
  journal: Nucleic Acids Res
  title: 'ECO, the Evidence & Conclusion Ontology: community standard for evidence information.'
  year: '2019'
- authors:
  - Chibucos MC
  - Mungall CJ
  - Balakrishnan R
  - Christie KR
  - Huntley RP
  - White O
  - Blake JA
  - Lewis SE
  - Giglio M
  doi: 10.1093/database/bau075
  id: https://www.ncbi.nlm.nih.gov/pubmed/25052702
  journal: Database (Oxford)
  title: Standardized description of scientific evidence using the Evidence Ontology (ECO)
  year: '2014'
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