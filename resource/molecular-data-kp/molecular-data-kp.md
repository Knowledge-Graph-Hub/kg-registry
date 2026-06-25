---
activity_status: active
category: KnowledgeGraph
collection:
  - translator
contacts:
  - category: Individual
    label: Sandrine Muller
    orcid: 0000-0001-5998-3003
description: MolePro is a Molecular Data Provider translating molecular scale to systems scale through a Reasoner API. It is a Translator Knowledge Provider.
domains:
  - biomedical
homepage_url: https://github.com/broadinstitute/molecular-data-provider/
id: molecular-data-kp
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: MolePro
products:
  - category: GraphProduct
    description: KGX nodes for Molecular Data KP
    format: kgx
    id: molecular-data-kp.graph.nodes
    name: Nodes for Molecular Data KP
    original_source:
      - source: molecular-data-kp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
      - source: pharos
        relation_type: prov:hadPrimarySource
      - source: tcrd
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: rxnorm
        relation_type: prov:hadPrimarySource
      - source: pharmgkb
        relation_type: prov:hadPrimarySource
      - source: bigg
        relation_type: prov:hadPrimarySource
      - source: depmap
        relation_type: prov:hadPrimarySource
      - source: ctrp
        relation_type: prov:hadPrimarySource
      - source: cmap
        relation_type: prov:hadPrimarySource
      - source: kinomescan
        relation_type: prov:hadPrimarySource
      - source: dsstoxdb
        relation_type: prov:hadPrimarySource
      - source: gelinea
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: drugrephub
        relation_type: prov:hadPrimarySource
    product_file_size: 3676906360
    product_url: https://molepro.s3.amazonaws.com/nodes.tsv
  - category: GraphProduct
    description: KGX edges for Molecular Data KP
    format: kgx
    id: molecular-data-kp.graph.edges
    name: Edges for Molecular Data KP
    original_source:
      - source: molecular-data-kp
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
      - source: pharos
        relation_type: prov:hadPrimarySource
      - source: tcrd
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: unichem
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: inchikey
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: rxnorm
        relation_type: prov:hadPrimarySource
      - source: pharmgkb
        relation_type: prov:hadPrimarySource
      - source: bigg
        relation_type: prov:hadPrimarySource
      - source: depmap
        relation_type: prov:hadPrimarySource
      - source: ctrp
        relation_type: prov:hadPrimarySource
      - source: cmap
        relation_type: prov:hadPrimarySource
      - source: kinomescan
        relation_type: prov:hadPrimarySource
      - source: dsstoxdb
        relation_type: prov:hadPrimarySource
      - source: gelinea
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: drugrephub
        relation_type: prov:hadPrimarySource
    product_file_size: 20140191116
    product_url: https://molepro.s3.amazonaws.com/edges.tsv
  - category: ProgrammingInterface
    connection_url: https://translator.broadinstitute.org/molecular_data_provider/api
    description: Open API for Molecular Data KP
    id: molecular-data-kp.api
    is_public: true
    name: Open API for Molecular Data KP
    original_source:
      - source: molecular-data-kp
        relation_type: prov:hadPrimarySource
    product_url: https://translator.broadinstitute.org/molecular_data_provider/api
repository: https://github.com/broadinstitute/molecular-data-provider/
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-06-18T00:00:00Z'
---

A Translator Knowledge Provider for molecular data.

contacts:
- category: Individual
 Sandrine Muller, Vlado Dancik, and Larry Chung

## Automated Evaluation

- View the automated evaluation: [molecular-data-kp automated evaluation](molecular-data-kp_eval_automated.html)
