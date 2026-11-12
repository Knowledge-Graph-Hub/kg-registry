---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: opig@stats.ox.ac.uk
  - contact_type: url
    value: https://opig.stats.ox.ac.uk/
  label: Oxford Protein Informatics Group (OPIG)
creation_date: '2026-11-12T00:00:00Z'
description: The Structural Antibody Database (SAbDab) collects and annotates all
  publicly available, experimentally determined antibody and nanobody structures,
  updated weekly from the Protein Data Bank. Each structure is annotated with experimental
  details, heavy and light chain pairings, CDR sequences, antigen details,
  species, resolution and affinity data where available, and structures are offered
  pre-numbered under standard antibody numbering schemes. SAbDab-nano tracks single-domain
  antibody (nanobody) structures. The current release, SAbDab2, adds sequence, CDR
  and antigen-sequence similarity searches, a REST API, and bulk summary and structure
  downloads aimed at machine learning use.
domains:
- immunology
- proteomics
- protein structure
homepage_url: https://sabdab.opig.stats.ox.ac.uk/
id: sabdab
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Structural Antibody Database (SAbDab)
products:
- category: GraphicalInterface
  description: SAbDab2 web portal for searching antibody and nanobody structures by
    attributes, sequence, CDR or antigen sequence, with structure viewers, statistics
    and downloads.
  format: http
  id: sabdab.portal
  name: SAbDab2 Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_url: https://sabdab.opig.stats.ox.ac.uk/
- category: ProgrammingInterface
  description: SAbDab REST API for retrieving antibody, antibody instance, antigen
    and PDB entry records, running sequence similarity searches, and requesting summary
    and structure downloads; documented with an OpenAPI specification.
  format: http
  id: sabdab.api
  name: SAbDab REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_url: https://sabdab.opig.stats.ox.ac.uk/api/docs
- category: Product
  description: CSV summary of all antibody structures in SAbDab, one row per antibody
    instance, with PDB ID, chain identifiers, variable domain and CDR sequences, antigen
    chains and type, organisms, experimental method, resolution and dates.
  format: csv
  id: sabdab.summary
  name: SAbDab All Structures Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_url: https://sabdab.opig.stats.ox.ac.uk/api/download/all-summary
- category: Product
  description: CSV summary of all single-domain antibody (nanobody) structures in
    SAbDab.
  format: csv
  id: sabdab.single-domain-summary
  name: SAbDab Single-Domain Antibody Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_url: https://sabdab.opig.stats.ox.ac.uk/api/download/all-single-domain-summary
- category: Product
  description: Tar archive of all SAbDab antibody structure files, built as a download
    job through the SAbDab API.
  format: mixed
  id: sabdab.structures
  name: SAbDab All Structures Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_url: https://sabdab.opig.stats.ox.ac.uk/api/download/all-structures
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
    source: alliance
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
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: chip-atlas
  - relation_type: prov:hadPrimarySource
    source: civic
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
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: drugcentral
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
    source: faers
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: gnomad
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gpn-star
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hmdd
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mavedb
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
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panelapp
  - relation_type: prov:hadPrimarySource
    source: pangolin
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
    source: revel
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: saprot
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: spliceai
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://sugi.bio/biobtree/api/
- category: GraphicalInterface
  description: Thera-SAbDab search interface for finding therapeutic antibodies by
    INN, target, format, clinical stage or sequence similarity, with summary pages
    linking each therapeutic to its matching SAbDab structures.
  format: http
  id: therasabdab.portal
  name: Thera-SAbDab Search Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: sabdab
  product_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/therasabdab/search/
- category: Product
  description: CSV table of all Thera-SAbDab therapeutics with format, isotype, clinical
    trial stage and status, heavy and light chain variable domain sequences, matching
    SAbDab structures at 100%, 99% and 95-98% sequence identity, INN proposal and
    recommendation years, targets, companies and conditions.
  format: csv
  id: therasabdab.sequences-structures
  name: Thera-SAbDab Sequences and Structures Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: therasabdab
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: sabdab
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_file_size: 636357
  product_url: https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/static/downloads/TheraSAbDab_SeqStruc_OnlineDownload.csv
publications:
- authors:
  - Capel HL
  - Vavourakis O
  - Williams BH
  - Taylor CR
  - Deane CM
  doi: 10.1093/nar/gkag1091
  id: doi:10.1093/nar/gkag1091
  journal: Nucleic Acids Research
  preferred: true
  title: 'SAbDab2: the structural antibody database in the age of machine learning'
  year: '2026'
- authors:
  - Dunbar J
  - Krawczyk K
  - Leem J
  - Baker T
  - Fuchs A
  - Georges G
  - Shi J
  - Deane CM
  doi: 10.1093/nar/gkt1043
  id: doi:10.1093/nar/gkt1043
  journal: Nucleic Acids Research
  title: 'SAbDab: the structural antibody database'
  year: '2014'
- authors:
  - Schneider C
  - Raybould MIJ
  - Deane CM
  doi: 10.1093/nar/gkab1050
  id: doi:10.1093/nar/gkab1050
  journal: Nucleic Acids Research
  title: 'SAbDab in the age of biotherapeutics: updates including SAbDab-nano, the
    nanobody structure tracker'
  year: '2022'
rrid: SCR_022096
---
# Structural Antibody Database (SAbDab)

SAbDab is a database of all publicly available antibody structures, harvested weekly from the Protein Data Bank and annotated in a consistent way, built and maintained by the Oxford Protein Informatics Group (OPIG) at the University of Oxford. It underpins related OPIG resources including Thera-SAbDab, which maps therapeutic antibody sequences onto SAbDab structures.

The current SAbDab2 site (https://sabdab.opig.stats.ox.ac.uk/, which the older https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/sabdab address redirects to) provides search, a REST API and bulk downloads. The data are made available under a CC BY 4.0 license.
