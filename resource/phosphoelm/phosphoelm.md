---
activity_status: orphaned
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: phospho@elm.eu.org
  - contact_type: url
    value: http://phospho.elm.eu.org/about.html
  label: Phospho.ELM
creation_date: '2026-06-02T00:00:00Z'
description: Phospho.ELM is a manually curated database of experimentally verified
  serine, threonine, and tyrosine phosphorylation sites in eukaryotic proteins, linking
  phosphorylation instances to kinases, species, sequence accessions, and literature
  references.
domains:
- biomedical
- proteomics
- biological systems
homepage_url: http://phospho.elm.eu.org/
id: phosphoelm
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: Phospho.ELM
products:
- category: GraphicalInterface
  description: Phospho.ELM HTTP web portal for searching experimentally verified phosphorylation
    sites by protein, accession, kinase, phosphopeptide-binding domain, organism group,
    and output format.
  id: phosphoelm.portal
  name: Phospho.ELM Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphoelm
  product_url: http://phospho.elm.eu.org/
- category: Product
  description: Phospho.ELM version 9.0 dataset request page for phosphorylation instances
    with accessions, sequences, residue positions, phosphorylated residues, PubMed
    identifiers, upstream kinases, evidence source class, species, and entry dates.
  format: mixed
  id: phosphoelm.dataset
  license:
    id: http://phospho.elm.eu.org/dumps/Phospho.Elm_AcademicLicense.pdf
    label: Phospho.ELM Academic License
  name: Phospho.ELM Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphoelm
  product_url: http://phospho.elm.eu.org/dataset.html
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ensembl
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  warnings: []
- category: ProcessProduct
  description: Phospho.ELM PhosphoBLAST search tool for comparing protein queries
    against the curated phosphorylated-peptide dataset.
  id: phosphoelm.phosphoblast
  name: Phospho.ELM PhosphoBLAST
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphoelm
  product_url: http://phospho.elm.eu.org/pELMBlastSearch.html
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: smart
  warnings: []
- category: ProgrammingInterface
  connection_url: http://phospho.elm.eu.org/webservice/phosphoELMdb.wsdl
  description: Prototype Phospho.ELM SOAP web service WSDL for programmatic access
    to Phospho.ELM database functions.
  format: http
  id: phosphoelm.webservice
  is_public: true
  name: Phospho.ELM Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phosphoelm
  product_url: http://phospho.elm.eu.org/webservice/phosphoELMdb.wsdl
- category: GraphProduct
  description: Current iPTMnet PTM record table with PTM type, source, UniProt protein,
    organism, site, enzyme, relation identifiers, and publication evidence.
  format: tsv
  id: iptmnet.ptm
  license:
    id: https://creativecommons.org/licenses/by-nc-sa/4.0/
    label: CC BY-NC-SA 4.0
  name: iPTMnet PTM Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iptmnet
  product_file_size: 44116546
  product_url: https://research.bioinformatics.udel.edu/iptmnet_data/files/current/ptm.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dbptm
  - relation_type: prov:wasDerivedFrom
    source: dbsno
  - relation_type: prov:wasDerivedFrom
    source: efip
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: nextprot
  - relation_type: prov:wasDerivedFrom
    source: p3db
  - relation_type: prov:wasDerivedFrom
    source: phosphoelm
  - relation_type: prov:wasDerivedFrom
    source: phosphogrid
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: phosphat
  - relation_type: prov:wasDerivedFrom
    source: pombase
  - relation_type: prov:wasDerivedFrom
    source: pubtator
  - relation_type: prov:wasDerivedFrom
    source: rlims-p
  - relation_type: prov:wasDerivedFrom
    source: signor
  - relation_type: prov:wasDerivedFrom
    source: uniprot
publications:
- authors:
  - Holger Dinkel
  - Claudia Chica
  - Allegra Via
  - Christian M Gould
  - Lars J Jensen
  - Toby J Gibson
  - Francesca Diella
  doi: 10.1093/nar/gkq1104
  id: doi:10.1093/nar/gkq1104
  journal: Nucleic Acids Research
  preferred: true
  title: Phospho.ELM, a database of phosphorylation sites - update 2011
  year: '2011'
- authors:
  - Francesca Diella
  - Christian M Gould
  - Claudia Chica
  - Allegra Via
  - Toby J Gibson
  doi: 10.1093/nar/gkm772
  id: doi:10.1093/nar/gkm772
  journal: Nucleic Acids Research
  title: Phospho.ELM, a database of phosphorylation sites - update 2008
  year: '2007'
- authors:
  - Francesca Diella
  - Scott Cameron
  - Christine Gemund
  - Rune Linding
  - Allegra Via
  - Bernhard Kuster
  - Thomas Sicheritz-Ponten
  - Nicolaj Blom
  - Toby J Gibson
  doi: 10.1186/1471-2105-5-79
  id: doi:10.1186/1471-2105-5-79
  journal: BMC Bioinformatics
  title: Phospho.ELM, a database of experimentally verified phosphorylation sites in eukaryotic proteins
  year: '2004'
synonyms:
- PhosphoELM
warnings:
- Phospho.ELM is reachable over HTTP, but its own release notes identify version 9.0
  from September 2010 as the current release.
---
# Phospho.ELM

Phospho.ELM is a literature-curated phosphorylation-site database for
eukaryotic proteins. Its legacy HTTP portal, dataset request form,
PhosphoBLAST search, and prototype WSDL endpoint remain documented, while the
latest release notes point to a 2010 dataset release.