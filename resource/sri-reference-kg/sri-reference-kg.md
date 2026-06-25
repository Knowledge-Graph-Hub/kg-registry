---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: kevinschaper@gmail.com
      - contact_type: github
        value: kevinschaper
    label: Kevin Schaper
    orcid: 0000-0003-3311-7320
description: The Monarch Initiative's SRI reference knowledge graph is a biomedical
  KG distribution and service layer that supports Translator-style querying across
  genes, diseases, phenotypes, variants, and related entities.
domains:
  - biomedical
homepage_url: https://monarchinitiative.org/kg/about
id: sri-reference-kg
infores_id: sri-reference-kg
layout: resource_detail
name: SRI-Reference KG
products:
  - category: ProgrammingInterface
    connection_url: https://api-v3.monarchinitiative.org/v3/docs
    description: Public API documentation for querying the Monarch Initiative knowledge
      graph that underlies the SRI reference KG distribution.
    format: http
    id: sri-reference-kg.api
    is_public: true
    name: Monarch KG API
    product_url: https://api-v3.monarchinitiative.org/v3/docs
    original_source:
      - source: sri-reference-kg
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: Documentation and status pages describing the Monarch knowledge graph,
      source inventory, downloads, and quality-control process.
    format: http
    id: sri-reference-kg.docs
    is_public: true
    name: Monarch KG Documentation
    product_url: https://monarchinitiative.org/kg/documentation
    original_source:
      - source: sri-reference-kg
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: KGX distribution of the SRI-Reference KG
    format: kgx
    id: sri-reference-kg.graph
    name: SRI-Reference KG (KGX distribution)
    product_file_size: 230046094
    product_url: https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.tar.gz
    original_source:
      - source: sri-reference-kg
        relation_type: prov:hadPrimarySource
      - source: alliance
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: biogrid
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: goa
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: mgi
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: orphanet
        relation_type: prov:hadPrimarySource
      - source: panther
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: wormbase
        relation_type: prov:hadPrimarySource
      - source: xenbase
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: phenio
        relation_type: prov:hadPrimarySource
      - source: bfo
        relation_type: prov:hadPrimarySource
      - source: bspo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: ddanat
        relation_type: prov:hadPrimarySource
      - source: ddpheno
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: dpo
        relation_type: prov:hadPrimarySource
      - source: eco
        relation_type: prov:hadPrimarySource
      - source: emapa
        relation_type: prov:hadPrimarySource
      - source: fbbt
        relation_type: prov:hadPrimarySource
      - source: fbdv
        relation_type: prov:hadPrimarySource
      - source: foodon
        relation_type: prov:hadPrimarySource
      - source: fypo
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: maxo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: mpath
        relation_type: prov:hadPrimarySource
      - source: nbo
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: ncit
        relation_type: prov:hadPrimarySource
      - source: oba
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: upheno
        relation_type: prov:hadPrimarySource
      - source: wbbt
        relation_type: prov:hadPrimarySource
      - source: wbls
        relation_type: prov:hadPrimarySource
      - source: wbphenotype
        relation_type: prov:hadPrimarySource
      - source: xao
        relation_type: prov:hadPrimarySource
      - source: xpo
        relation_type: prov:hadPrimarySource
      - source: zfa
        relation_type: prov:hadPrimarySource
      - source: zfs
        relation_type: prov:hadPrimarySource
      - source: zp
        relation_type: prov:hadPrimarySource
      - source: icd10cm
        relation_type: prov:hadPrimarySource
      - source: icd11
        relation_type: prov:hadPrimarySource
      - source: decipher
        relation_type: prov:hadPrimarySource
      - source: mmrrc
        relation_type: prov:hadPrimarySource
      - source: cureid
        relation_type: prov:hadPrimarySource
      - source: phenopacket-store
        relation_type: prov:hadPrimarySource
repository: https://github.com/monarch-initiative/monarch-app
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-06-18T00:00:00Z'
---

The SRI-Reference KG is the Monarch Initiative's biomedical knowledge graph as
packaged for downstream querying, download, and service integration. It brings
together curated data about genes, diseases, phenotypes, variants, genotypes,
pathways, and supporting ontologies so that applications can traverse a shared
graph of cross-species and clinical-research knowledge.

In practice, this resource is exposed through downloadable KG artifacts and the
Monarch API and web stack. The current distribution hosted under the Monarch data
site provides KGX and database-oriented outputs, while the Monarch documentation
and API pages describe the source inventory, quality-control reports, and query
surfaces built over the same graph content.

## Automated Evaluation

- View the automated evaluation: [sri-reference-kg automated evaluation](sri-reference-kg_eval_automated.html)
