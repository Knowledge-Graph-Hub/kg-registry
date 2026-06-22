---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: swisslipids@sib.swiss
  label: SwissLipids team
creation_date: '2025-03-09T00:00:00Z'
description: SwissLipids is a knowledge resource for lipids and their biology.
domains:
- chemistry and biochemistry
homepage_url: https://www.swisslipids.org/
id: swisslipid
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: SwissLipids
products:
- category: GraphicalInterface
  description: Main SwissLipids interface for browsing lipid classes and analytes.
  format: http
  id: swisslipid.portal
  name: SwissLipids Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_url: https://www.swisslipids.org/
- category: Product
  description: TSV export of lipid-related enzymes with UniProt, Rhea, and evidence
    links.
  format: tsv
  id: swisslipid.enzymes
  name: SwissLipids Enzymes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 126760
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=enzymes.tsv
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
  description: TSV export of SwissLipids links to Gene Ontology terms with taxon context.
  format: tsv
  id: swisslipid.go
  name: SwissLipids GO Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 48388
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=go.tsv
- category: Product
  description: Comprehensive TSV catalogue of SwissLipids lipid entities and identifiers.
  format: tsv
  id: swisslipid.lipids
  name: SwissLipids Lipids
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_file_size: 76772233
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids.tsv
- category: MappingProduct
  description: TSV mapping between SwissLipids lipid entries and UniProtKB proteins.
  format: tsv
  id: swisslipid.lipids2uniprot
  name: SwissLipids Lipids to UniProt
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 37147786
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids2uniprot.tsv
- category: Product
  description: TSV export of lipid tissue and cell annotations with taxon and evidence
    tags.
  format: tsv
  id: swisslipid.tissues
  name: SwissLipids Tissues
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_file_size: 9540
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=tissues.tsv
- category: ProgrammingInterface
  connection_url: https://www.swisslipids.org/#/api
  description: Public API page for programmatic SwissLipids access.
  format: http
  id: swisslipid.api
  is_public: true
  name: SwissLipids API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_url: https://www.swisslipids.org/#/api
- category: Product
  compression: gzip
  description: swisslipid Nodes TSV
  format: tsv
  id: obo-db-ingest.swisslipid.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: swisslipid Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_file_size: 9655893
  product_url: https://w3id.org/biopragmatics/resources/slm/slm.tsv.gz
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
  - Aimo L
  - Liechti R
  - Hyka-Nouspikel N
  - Niknejad A
  - Gleizes A
  - Götz L
  - Kuznetsov D
  - David FPA
  - van der Goot FG
  - Riezman H
  - Bougueleret L
  - Xenarios I
  - Bridge A
  doi: 10.1093/bioinformatics/btv285
  id: doi:10.1093/bioinformatics/btv285
  journal: Bioinformatics
  preferred: true
  title: The SwissLipids knowledgebase for lipid biology
  year: '2015'
repository: https://www.swisslipids.org/
synonyms:
- slm
- swisslipid
---
# SwissLipids

SwissLipids is a curated knowledge resource for lipids and lipid biology
developed by SIB Swiss Institute of Bioinformatics teams. It combines a browseable
web interface with downloadable reference tables for lipid entities, enzyme
associations, GO annotations, tissues, evidences, and lipid-to-UniProt mappings.

In KG-Registry, SwissLipids is represented both as a public portal and as a set
of concrete downloadable products that support identifier mapping, lipid
classification, and metabolism-oriented integration workflows. The downstream
OBO-DB-Ingest TSV remains attached as a propagated derivative of the underlying
SwissLipids content.