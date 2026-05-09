---
activity_status: active
category: KnowledgeGraph
collection:
  - translator
  - ber
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: gglusman@isbscience.org
      - contact_type: github
        value: gglusman
    label: "Gwênlyn Glusman"
creation_date: '2025-08-30T00:00:00Z'
description: MicrobiomeKG is an integrative knowledge graph resource for multi-omics microbiome data linking microbial taxa, genes, metabolites, host phenotypes, pathways, and clinical variables to support systems biology analyses and translational research.
domains:
  - biomedical
  - systems biology
  - microbiome
homepage_url: https://multiomics.transltr.io/mbkp
id: microbiomekg
last_modified_date: '2025-08-30T00:00:00Z'
layout: resource_detail
name: MicrobiomeKG
products:
  - category: ProgrammingInterface
    description: TRAPI web API for querying MicrobiomeKG
    format: http
    id: microbiomekg.api
    name: MicrobiomeKG Plover API
    original_source:
      - source: biolink
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: eupathdb
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: microbiomekg
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://multiomics.transltr.io/mbkp
publications:
  - doi: 10.3389/fsysb.2025.1544432
    id: doi:10.3389/fsysb.2025.1544432
    journal: Frontiers in Systems Biology
    title: 'MicrobiomeKG: an integrative knowledge graph for multi-omics microbiome translational research'
    year: '2025'
taxon:
  - NCBITaxon:9606
  - NCBITaxon:2
---

# MicrobiomeKG

MicrobiomeKG is an integrative knowledge graph for microbiome multi-omics and translational research, connecting microbial taxa, genes, metabolites, pathways, phenotypes, and clinical features. It aims to enable complex querying, hypothesis generation, and systems-level analyses by harmonizing heterogeneous microbiome-related datasets.

## Automated Evaluation

- View the automated evaluation: [microbiomekg automated evaluation](microbiomekg_eval_automated.html)
