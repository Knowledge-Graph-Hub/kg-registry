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
description: MetaCyc is a curated database of experimentally elucidated metabolic
  pathways from all domains of life. MetaCyc contains pathways involved in both primary
  and secondary metabolism, as well as associated metabolites, reactions, enzymes,
  and genes. The goal of MetaCyc is to catalog the universe of metabolism by storing
  a representative sample of each experimentally elucidated pathway.
domains:
- biological systems
homepage_url: https://metacyc.org/
id: metacyc
infores_id: metacyc
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://metacyc.org/download.shtml
  label: Varies
name: MetaCyc
products:
- category: GraphicalInterface
  description: Official MetaCyc portal for browsing curated metabolic pathways, reactions,
    metabolites, enzymes, and genes across all domains of life.
  format: http
  id: metacyc.portal
  name: MetaCyc Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metacyc
  product_url: https://metacyc.org/
- category: ProgrammingInterface
  description: MetaCyc web services and APIs for programmatic access to pathway and
    metabolic reference data.
  format: http
  id: metacyc.api
  name: MetaCyc Web Services
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metacyc
  product_url: https://metacyc.org/web-services.shtml
- category: MappingProduct
  description: rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: rhea SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecocyc
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: m-csa
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 154171
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: GraphProduct
  compression: gzip
  description: HumanNet-XC v3 functional gene network extended by co-citation, distributed
    with Entrez Gene identifiers.
  edge_count: 1125494
  format: tsv
  id: humannet.network
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Network File
  node_count: 18462
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_file_size: 12310221
  product_url: https://www.inetbio.org/humannetv3/networks/HumanNet-XC.tsv.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: metacyc
  - relation_type: prov:wasDerivedFrom
    source: reactome
- category: GraphProduct
  compression: gzip
  description: HumanNet-XC v3 functional gene network extended by co-citation, distributed
    with gene symbols.
  edge_count: 1125494
  format: tsv
  id: humannet.network.symbol
  latest_version: v3
  license:
    id: http://creativecommons.org/licenses/by-sa/4.0/
    label: CC BY-SA 4.0
  name: HumanNet Network File (Gene Symbols)
  node_count: 18462
  original_source:
  - relation_type: prov:hadPrimarySource
    source: humannet
  product_file_size: 13925784
  product_url: https://www.inetbio.org/humannetv3/networks/HumanNet-XC.symbol.tsv.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: irefindex
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: metacyc
  - relation_type: prov:wasDerivedFrom
    source: reactome
---
# MetaCyc

MetaCyc is a curated reference database of experimentally elucidated metabolic
pathways drawn from all domains of life. It organizes pathways together with the
associated reactions, metabolites, enzymes, and genes, with the explicit goal of
capturing a representative sample of known metabolism.

In KG-Registry, the owned MetaCyc products are the live portal and the BioCyc web
services entry point. The `rhea` SSSOM and `spoke` graph entries remain attached
as propagated downstream products because they reuse MetaCyc content in broader
cross-resource integration workflows.