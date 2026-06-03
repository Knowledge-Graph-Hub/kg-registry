---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.sib.swiss/
    label: SIB Swiss Institute of Bioinformatics
creation_date: '2026-06-02T00:00:00Z'
description: neXtProt is a human protein knowledge platform that integrates manually curated UniProtKB/Swiss-Prot records with proteomics, genetic variation, expression, interaction, localization, and functional annotations.
domains:
  - proteomics
  - genomics
  - biomedical
homepage_url: https://www.nextprot.org/
id: nextprot
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: neXtProt
products:
  - category: GraphicalInterface
    description: neXtProt web platform for searching and browsing curated human protein entries, proteomics evidence, variants, expression, interactions, localization, and functional annotations.
    id: nextprot.portal
    name: neXtProt Web Platform
    original_source:
      - relation_type: prov:hadPrimarySource
        source: nextprot
    product_url: https://www.nextprot.org/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: uniprot
  - category: ProgrammingInterface
    connection_url: https://api.nextprot.org
    description: neXtProt REST API for programmatic access to human protein annotations and entry data.
    format: json
    id: nextprot.api
    is_public: true
    name: neXtProt API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: nextprot
    product_url: https://api.nextprot.org
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: uniprot
  - category: ProgrammingInterface
    description: neXtProt SPARQL endpoint for querying RDF representations of human protein knowledge.
    format: http
    id: nextprot.sparql
    is_public: true
    name: neXtProt SPARQL Endpoint
    original_source:
      - relation_type: prov:hadPrimarySource
        source: nextprot
    product_url: https://sparql.nextprot.org/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: uniprot
  - category: Product
    description: neXtProt downloadable human protein data, including flat files and RDF data products for local reuse.
    format: mixed
    id: nextprot.downloads
    name: neXtProt Downloads
    original_source:
      - relation_type: prov:hadPrimarySource
        source: nextprot
    product_url: https://www.nextprot.org/downloads
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: uniprot
  - category: GraphProduct
    description: Current iPTMnet PTM record table with PTM type, source, UniProt protein, organism, site, enzyme, relation identifiers, and publication evidence.
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
      - Monique Zahn-Zabal
      - Pierre-André Michel
      - Caroline Gateau
      - Lydie Lane
      - Amos Bairoch
    doi: 10.1093/nar/gkz995
    id: doi:10.1093/nar/gkz995
    journal: Nucleic Acids Research
    preferred: true
    title: 'The neXtProt knowledgebase in 2020: data, tools and usability improvements'
    year: '2020'
  - authors:
      - Pascale Gaudet
      - Pierre-André Michel
      - Monique Zahn-Zabal
      - Aurore Britan
      - Isabelle Cusin
      - Marcin Domagalski
    doi: 10.1093/nar/gkw1062
    id: doi:10.1093/nar/gkw1062
    journal: Nucleic Acids Research
    preferred: false
    title: 'The neXtProt knowledgebase on human proteins: 2017 update'
    year: '2017'
taxon:
  - NCBITaxon:9606
---

# neXtProt

neXtProt provides curated and integrated knowledge about human proteins through
a web platform, REST API, SPARQL endpoint, and downloadable data products. Its
protein and PTM annotations are also represented in downstream resources such as
iPTMnet.
