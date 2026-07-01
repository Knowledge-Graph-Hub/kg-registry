---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.broadinstitute.org/
  label: Broad Institute
creation_date: '2026-06-18T00:00:00Z'
description: 'ChemBank was a public, freely available collection of small-molecule
  screening data and cheminformatics resources developed by the Chemical Biology Program
  (formerly the Initiative for Chemical Genetics) at the Broad Institute. It assembled
  biological activity measurements from high-throughput screens together with chemical
  structures, compound annotations, and analysis tools, with the aim of helping researchers
  relate small molecules to their effects on biological systems. ChemBank is no longer
  maintained: its homepage at chembank.broadinstitute.org is defunct and now redirects
  away from the original database. It served as an upstream primary source for the
  Molecular Data Provider (MolePro) and the molecular-data-kp knowledge provider.'
domains:
- chemistry and biochemistry
- drug discovery
- pharmacology
homepage_url: http://chembank.broadinstitute.org/
id: chembank
infores_id: chembank
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: ChemBank
products:
- category: DocumentationProduct
  description: Archived snapshot of the former ChemBank homepage in the Internet Archive
    Wayback Machine, preserved because the original site (chembank.broadinstitute.org)
    is defunct.
  format: http
  id: chembank.wayback
  name: ChemBank homepage (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembank
  product_url: http://web.archive.org/web/20180524103413/http://chembank.broadinstitute.org/
- category: DocumentationProduct
  description: Primary publication describing ChemBank, its data model, and its cheminformatics
    tools (Nucleic Acids Research Database issue).
  format: http
  id: chembank.publication
  name: ChemBank NAR publication
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembank
  product_url: https://doi.org/10.1093/nar/gkm843
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
publications:
- authors:
  - Seiler KP
  - George GA
  - Happ MP
  - Bodycombe NE
  - Carrinski HA
  - Norton S
  - Brudz S
  - Sullivan JP
  - Muhlich J
  - Serrano M
  - Ferraiolo P
  - Tolliday NJ
  - Schreiber SL
  - Clemons PA
  doi: 10.1093/nar/gkm843
  id: https://www.ncbi.nlm.nih.gov/pubmed/17947324
  journal: Nucleic Acids Res
  preferred: true
  title: 'ChemBank: a small-molecule screening and cheminformatics resource database'
  year: '2008'
---
# ChemBank

ChemBank was a public, free small-molecule screening and cheminformatics resource
database produced by the Chemical Biology Program (originally the Initiative for
Chemical Genetics) at the Broad Institute. It collected raw and processed data from
high-throughput biological screens, chemical structures, and compound annotations,
and paired them with analysis and search tools so that investigators could explore
relationships between small molecules and biological activity.

The resource is now defunct. The original homepage at
`chembank.broadinstitute.org` no longer serves the database and redirects to an
unrelated Broad Institute page, so for this reason the resource is recorded with
`activity_status: inactive`. A historical snapshot of the homepage is preserved in
the Internet Archive Wayback Machine, and the original Nucleic Acids Research
publication remains the canonical description of the resource.

In KG-Registry, ChemBank is retained as a historical primary source. It served
upstream of the Molecular Data Provider (MolePro) / molecular-data-kp, which
transformed and integrated ChemBank content for downstream knowledge-graph use.