---
activity_status: active
category: DataSource
collection:
  - ber
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: biocyc-support@sri.com
    label: MetaCyc
creation_date: '2025-03-17T00:00:00Z'
description: MetaCyc is a curated database of experimentally elucidated metabolic pathways from all domains of life. MetaCyc contains pathways involved in both primary and secondary metabolism, as well as associated metabolites, reactions, enzymes, and genes. The goal of MetaCyc is to catalog the universe of metabolism by storing a representative sample of each experimentally elucidated pathway.
domains:
  - biological systems
homepage_url: https://metacyc.org/
id: metacyc
infores_id: metacyc
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: https://metacyc.org/download.shtml
  label: Varies
name: MetaCyc
products:
  - category: MappingProduct
    description: rhea SSSOM
    format: sssom
    id: obo-db-ingest.rhea.sssom.tsv
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC-BY-4.0
    name: rhea SSSOM
    original_source:
      - source: rhea
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: metacyc
        relation_type: prov:hadPrimarySource
      - source: m-csa
        relation_type: prov:hadPrimarySource
      - source: ecocyc
        relation_type: prov:hadPrimarySource
    product_file_size: 154171
    product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
    secondary_source:
      - source: obo-db-ingest
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: The SPOKE knowledge graph containing nodes and edges from multiple biomedical data sources.
    id: spoke.graph
    name: SPOKE Graph
    original_source:
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: pid
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: lincs-l1000
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: bindingdb
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: bgee
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: chembl
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: civic
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: clinicaltrialsgov
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: metacyc
        relation_type: prov:hadPrimarySource
      - source: bv-brc
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: pathophenodb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: protcid
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: spoke
        relation_type: prov:wasInfluencedBy
---

MetaCyc
