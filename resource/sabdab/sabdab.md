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
